
// 🚀 GRANDMASTER API ENGINE v3.0
// Every quantum trade gets: REST API + Plugins + Webhooks + Cache + Rate Limit
// One unified engine, injected into every trade agent

const QUANTUM_API = (() => {
  'use strict';

  // === CONFIG ===
  const VERSION = '3.0.0';
  const CACHE_TTL = 30000; // 30s default
  const MAX_PLUGINS = 50;
  const RATE_WINDOW = 60000; // 1 min
  const MAX_RPM = 60; // requests per minute (free tier safe)

  // === CORE ===
  const _cache = new Map();
  const _rateMap = new Map();
  const _plugins = new Map();
  const _webhooks = new Map();
  const _routes = new Map();
  const _metrics = { requests: 0, cacheHits: 0, cacheMisses: 0, errors: 0, avgLatency: 0 };

  // === TRADE REGISTRY (all 50 trades auto-register here) ===
  const TRADES = {};

  // === CACHE LAYER ===
  const cache = {
    get(key) {
      const entry = _cache.get(key);
      if (!entry) { _metrics.cacheMisses++; return null; }
      if (Date.now() > entry.expires) { _cache.delete(key); _metrics.cacheMisses++; return null; }
      _metrics.cacheHits++;
      return entry.data;
    },
    set(key, data, ttl = CACHE_TTL) {
      _cache.set(key, { data, expires: Date.now() + ttl });
    },
    clear(pattern) {
      if (!pattern) { _cache.clear(); return; }
      for (const k of _cache.keys()) {
        if (k.includes(pattern)) _cache.delete(k);
      }
    },
    stats() {
      const entries = _cache.size;
      const hits = _metrics.cacheHits;
      const misses = _metrics.cacheMisses;
      const ratio = (hits + misses) > 0 ? (hits / (hits + misses) * 100).toFixed(1) : 0;
      return { entries, hits, misses, hitRatio: ratio + '%' };
    }
  };

  // === RATE LIMITER (multi-key rotation ready) ===
  const rateLimit = {
    check(key, maxRpm = MAX_RPM) {
      const now = Date.now();
      const window = Math.floor(now / RATE_WINDOW);
      const bucketKey = `${key}:${window}`;
      const count = (_rateMap.get(bucketKey) || 0) + 1;
      _rateMap.set(bucketKey, count);
      // Cleanup old windows
      if (_rateMap.size > 1000) {
        const currentWindow = Math.floor(now / RATE_WINDOW);
        for (const k of _rateMap.keys()) {
          if (!k.endsWith(`:${currentWindow}`)) _rateMap.delete(k);
        }
      }
      return {
        allowed: count <= maxRpm,
        remaining: Math.max(0, maxRpm - count),
        resetMs: RATE_WINDOW - (now % RATE_WINDOW)
      };
    }
  };

  // === PLUGIN SYSTEM ===
  const plugins = {
    register(id, plugin) {
      if (_plugins.size >= MAX_PLUGINS) throw new Error(`Max ${MAX_PLUGINS} plugins`);
      if (!id || !plugin || !plugin.handler) throw new Error('Plugin needs id + handler function');
      _plugins.set(id, {
        ...plugin,
        id,
        registered: new Date().toISOString(),
        calls: 0,
        errors: 0,
        lastCall: null
      });
      return { ok: true, plugin: id, total: _plugins.size };
    },
    unregister(id) {
      return _plugins.delete(id);
    },
    get(id) { return _plugins.get(id) || null; },
    list() {
      return Array.from(_plugins.values()).map(p => ({
        id: p.id, name: p.name, version: p.version, calls: p.calls, errors: p.errors, status: 'registered'
      }));
    },
    async run(id, context, input) {
      const plugin = _plugins.get(id);
      if (!plugin) throw new Error(`Plugin '${id}' not found`);
      try {
        plugin.calls++;
        plugin.lastCall = Date.now();
        const result = await plugin.handler(context, input);
        return result;
      } catch (e) {
        plugin.errors++;
        _metrics.errors++;
        throw e;
      }
    },
    async runAll(context, input) {
      const results = {};
      for (const [id, plugin] of _plugins) {
        try {
          results[id] = await plugin.handler(context, input);
        } catch (e) {
          results[id] = { error: e.message };
        }
      }
      return results;
    }
  };

  // === WEBHOOK ENGINE ===
  const webhooks = {
    register(event, url, secret = null) {
      if (!_webhooks.has(event)) _webhooks.set(event, []);
      _webhooks.get(event).push({ url, secret, created: Date.now() });
      return { ok: true, event, total: _webhooks.get(event).length };
    },
    async fire(event, payload) {
      const hooks = _webhooks.get(event) || [];
      const results = [];
      for (const hook of hooks) {
        try {
          const body = JSON.stringify(payload);
          const headers = { 'Content-Type': 'application/json' };
          if (hook.secret) {
            const sig = hmac(hook.secret, body);
            headers['X-Webhook-Signature'] = sig;
          }
          // Fire-and-forget via fetch
          fetch(hook.url, { method: 'POST', headers, body }).catch(() => {});
          results.push({ url: hook.url, status: 'fired' });
        } catch (e) {
          results.push({ url: hook.url, status: 'error', error: e.message });
        }
      }
      return results;
    }
  };

  // === ROUTER ===
  const router = {
    register(method, path, handler, meta = {}) {
      const key = `${method}:${path}`;
      _routes.set(key, { handler, meta, calls: 0 });
      return { ok: true, route: key };
    },
    async handle(method, path, req) {
      const key = `${method}:${path}`;
      const route = _routes.get(key);
      if (!route) {
        // Try pattern matching
        for (const [k, r] of _routes) {
          const [rmethod, rpath] = k.split(':');
          if (rmethod !== method) continue;
          const pattern = rpath.replace(/:([^/]+)/g, '(?<$1>[^/]+)');
          const match = path.match(new RegExp(`^${pattern}$`));
          if (match) {
            req.params = match.groups || {};
            route.calls++;
            _metrics.requests++;
            const start = Date.now();
            try {
              const result = await r.handler(req);
              _metrics.avgLatency = (_metrics.avgLatency * (_metrics.requests - 1) + (Date.now() - start)) / _metrics.requests;
              return result;
            } catch (e) {
              _metrics.errors++;
              throw e;
            }
          }
        }
        return { error: 'Not found', status: 404 };
      }
      route.calls++;
      _metrics.requests++;
      const start = Date.now();
      try {
        const result = await route.handler(req);
        _metrics.avgLatency = (_metrics.avgLatency * (_metrics.requests - 1) + (Date.now() - start)) / _metrics.requests;
        return result;
      } catch (e) {
        _metrics.errors++;
        throw e;
      }
    },
    list() {
      return Array.from(_routes.entries()).map(([k, r]) => {
        const [method, path] = k.split(':');
        return { method, path, calls: r.calls, ...r.meta };
      });
    }
  };

  // === TRADE REGISTRATION ===
  function registerTrade(tradeId, name, config) {
    TRADES[tradeId] = {
      id: tradeId,
      name,
      config,
      api: { calls: 0, errors: 0, lastCall: null },
      registered: new Date().toISOString()
    };
    return TRADES[tradeId];
  }

  function getTrade(id) { return TRADES[id] || null; }
  function listTrades() { return Object.values(TRADES); }

  // === HEALTH ===
  function health() {
    const uptime = process.uptime ? Math.floor(process.uptime()) : 0;
    const h = uptime > 0 ? Math.floor(uptime / 3600) : 0;
    const m = uptime > 0 ? Math.floor((uptime % 3600) / 60) : 0;
    return {
      status: 'operational',
      version: VERSION,
      uptime: `${h}h ${m}m`,
      trades: Object.keys(TRADES).length,
      plugins: _plugins.size,
      routes: _routes.size,
      webhooks: _webhooks.size,
      cache: cache.stats(),
      metrics: {
        requests: _metrics.requests,
        errors: _metrics.errors,
        avgLatency: _metrics.avgLatency.toFixed(0) + 'ms'
      }
    };
  }

  // === UTILITY ===
  function hmac(secret, data) {
    // Simple HMAC for webhooks (Node's crypto when available)
    try {
      const crypto = require('crypto');
      return crypto.createHmac('sha256', secret).update(data).digest('hex');
    } catch {
      // Fallback
      let hash = 0;
      for (const c of (secret + data)) { hash = ((hash << 5) - hash) + c.charCodeAt(0); hash |= 0; }
      return hash.toString(16);
    }
  }

  // === EXPORT ===
  return {
    VERSION,
    cache,
    rateLimit,
    plugins,
    webhooks,
    router,
    registerTrade,
    getTrade,
    listTrades,
    health
  };
})();

// Auto-export for Node/CommonJS
if (typeof module !== 'undefined' && module.exports) {
  module.exports = QUANTUM_API;
}
