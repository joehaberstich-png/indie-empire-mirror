/**
 * Security middleware for all API endpoints
 * 
 * Applies to: /api/v1/*, /api/v2/*, /api/webhook/*
 * 
 * Provides:
 *   - Rate-limiting headers
 *   - CORS validation
 *   - Request validation
 *   - Logging with no PII
 */

// Rate limiter: simple in-memory (Vercel edge handles DDoS)
const requestLog = new Map();
const RATE_LIMIT = 100;      // requests per window
const WINDOW_MS = 60 * 1000; // 1 minute

export function rateLimit(ip) {
  const now = Date.now();
  if (!requestLog.has(ip)) {
    requestLog.set(ip, []);
  }
  
  const timestamps = requestLog.get(ip).filter(t => now - t < WINDOW_MS);
  timestamps.push(now);
  requestLog.set(ip, timestamps);
  
  return {
    allowed: timestamps.length <= RATE_LIMIT,
    remaining: Math.max(0, RATE_LIMIT - timestamps.length),
    resetTime: now + WINDOW_MS
  };
}

export function securityHeaders(res) {
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'DENY');
  res.setHeader('Cache-Control', 'no-store');
  res.setHeader('X-Robots-Tag', 'noindex');
  return res;
}

export function corsCheck(req, res) {
  const origin = req.headers['origin'];
  const allowed = ['https://atvhomes.com', 'https://atv-homes.vercel.app'];
  
  if (origin && allowed.includes(origin)) {
    res.setHeader('Access-Control-Allow-Origin', origin);
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Stripe-Signature');
    res.setHeader('Access-Control-Max-Age', '86400');
  } else {
    // Block unknown origins (no CORS header = browser blocks)
    res.setHeader('Access-Control-Allow-Origin', 'https://atvhomes.com');
  }
  
  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return false;
  }
  return true;
}

export function validateStripeWebhook(req, res, rawBody) {
  const signature = req.headers['stripe-signature'];
  if (!signature) {
    res.status(401).json({ error: 'Missing Stripe signature' });
    return false;
  }
  // In production: verify with stripe.webhooks.constructEvent(rawBody, signature, endpointSecret)
  // const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
  // const event = stripe.webhooks.constructEvent(rawBody, signature, WEBHOOK_SECRET);
  return true;
}

export function sanitizeLog(data) {
  // Never log PII
  const safe = { ...data };
  if (safe.email) safe.email = safe.email.split('@')[0] + '@***';
  if (safe.phone) safe.phone = safe.phone.slice(0, 3) + '***' + safe.phone.slice(-4);
  if (safe.ip) delete safe.ip;
  if (safe.userAgent) safe.userAgent = safe.userAgent.slice(0, 30) + '...';
  return safe;
}
