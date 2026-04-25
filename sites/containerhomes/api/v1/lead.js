/**
 * Lead Capture & Conversion API (SECURED)
 * 
 * POST /api/v1/lead  — Capture any lead from any source
 * GET  /api/v1/lead/sources — List all traffic sources
 */

import { rateLimit, securityHeaders, corsCheck, sanitizeLog } from '../lib/security.js';

const LEADS = [];

export default async function handler(req, res) {
  securityHeaders(res);
  if (!corsCheck(req, res)) return;
  
  // Rate limit
  const ip = req.headers['x-forwarded-for'] || 'unknown';
  const rl = rateLimit(ip);
  res.setHeader('X-RateLimit-Remaining', rl.remaining);
  if (!rl.allowed) {
    return res.status(429).json({ error: 'Too many requests', retryAfter: 60 });
  }

  const url = new URL(req.url, 'http://localhost');
  const path = url.pathname.replace('/api/v1/lead', '').replace(/^\/+/, '');

  if (req.method === 'POST' && (!path || path === 'capture')) {
    const { name, email, phone, source, product, page } = req.body || {};
    
    // Basic validation
    if (!email && !phone) {
      return res.status(400).json({ error: 'email or phone required' });
    }
    if (email && !email.includes('@')) {
      return res.status(400).json({ error: 'Invalid email' });
    }
    
    // Validate email length (sanity check)
    if (email && email.length > 254) {
      return res.status(400).json({ error: 'Invalid email' });
    }
    if (name && name.length > 200) {
      return res.status(400).json({ error: 'Name too long' });
    }

    const lead = {
      id: Date.now().toString(36) + Math.random().toString(36).slice(2, 6),
      source: (source || 'direct').slice(0, 100),
      product: (product || null),
      page: (page || '/').slice(0, 500),
      timestamp: new Date().toISOString()
    };

    LEADS.push(lead);
    
    // Sanitized log
    const safe = sanitizeLog({ email, name, ...lead });
    console.log(`[LEAD] New lead: ${safe.source}`, JSON.stringify(safe));

    return res.status(200).json({
      ok: true,
      lead_id: lead.id,
      message: 'Lead captured'
    });
  }

  if (path === 'sources') {
    const sourceCount = {};
    for (const l of LEADS) {
      sourceCount[l.source] = (sourceCount[l.source] || 0) + 1;
    }
    return res.status(200).json({ total: LEADS.length, sources: sourceCount });
  }

  if (path === 'count') {
    return res.status(200).json({ total: LEADS.length });
  }

  return res.status(404).json({ error: 'not found' });
}
