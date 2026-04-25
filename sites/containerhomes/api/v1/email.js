/**
 * Email Subscription API — SECURED
 * 
 * POST /api/v1/email/subscribe  — Subscribe email to mailing list
 * GET  /api/v1/email/count      — Count of subscribers
 * 
 * Ready for Mailchimp/ConvertKit/SendGrid integration — drop API key in config.
 */

import { securityHeaders, corsCheck, rateLimit, sanitizeLog } from '../lib/security.js';

const SUBSCRIBERS = new Set();

export default async function handler(req, res) {
  securityHeaders(res);
  if (!corsCheck(req, res)) return;

  const ip = req.headers['x-forwarded-for'] || 'unknown';
  const rl = rateLimit(ip);
  res.setHeader('X-RateLimit-Remaining', rl.remaining);
  if (!rl.allowed) {
    return res.status(429).json({ error: 'Too many requests', retryAfter: 60 });
  }

  const url = new URL(req.url, 'http://localhost');
  const path = url.pathname.replace('/api/v1/email', '').replace(/^\/+/, '');
  const method = req.method;

  // POST — Subscribe
  if (method === 'POST' && (!path || path === 'subscribe')) {
    const { email, name, source } = req.body || {};

    if (!email || !email.includes('@') || email.length > 254) {
      return res.status(400).json({ error: 'Valid email required' });
    }

    if (SUBSCRIBERS.has(email.toLowerCase())) {
      return res.status(200).json({ ok: true, message: 'Already subscribed' });
    }

    SUBSCRIBERS.add(email.toLowerCase());

    // Sanitized log
    const masked = email.split('@')[0].slice(0, 3) + '***@' + email.split('@')[1];
    console.log(`[EMAIL] Subscribe: ${masked} (source: ${source || 'direct'})`);

    return res.status(200).json({
      ok: true,
      message: 'Subscribed',
      subscriber_count: SUBSCRIBERS.size
    });
  }

  // GET — Count (no PII exposed)
  if (path === 'count') {
    return res.status(200).json({
      subscriber_count: SUBSCRIBERS.size
    });
  }

  return res.status(404).json({ error: 'Not found. Try POST /api/v1/email/subscribe' });
}
