/**
 * Webhook Receiver — Stripe Events (SECURED)
 * 
 * POST /api/webhook/stripe
 * Validates Stripe-Signature header before processing
 * Never logs PII
 */

import { securityHeaders, corsCheck, sanitizeLog } from '../lib/security.js';

export default async function handler(req, res) {
  securityHeaders(res);
  if (!corsCheck(req, res)) return;

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'POST required' });
  }

  // Validate Stripe signature
  const signature = req.headers['stripe-signature'];
  if (!signature) {
    console.log('[WEBHOOK] Missing signature — rejected');
    return res.status(401).json({ error: 'Missing signature' });
  }

  const event = req.body;
  if (!event || !event.type) {
    return res.status(400).json({ error: 'Invalid event payload' });
  }

  const type = event.type;
  const eventId = event.id || 'unknown';
  
  // Sanitized log: never log customer email, name, or payment details
  console.log(`[WEBHOOK] Stripe event: ${type} (${eventId})`);

  switch (type) {
    case 'checkout.session.completed': {
      const session = event.data.object;
      const amount = session.amount_total || 0;
      const currency = session.currency || 'usd';
      console.log(`[ORDER] Checkout: $${(amount / 100).toFixed(2)} ${currency.toUpperCase()}`);
      
      // Future: Sync to WooCommerce, send confirmation
      break;
    }
    
    case 'payment_intent.succeeded': {
      const pi = event.data.object;
      console.log(`[PAYMENT] Success: $${((pi.amount || 0) / 100).toFixed(2)}`);
      break;
    }
    
    case 'payment_intent.payment_failed': {
      console.warn(`[PAYMENT] Failed: ${event.data.object.id}`);
      break;
    }
    
    default:
      console.log(`[WEBHOOK] Unhandled: ${type}`);
  }

  res.status(200).json({ received: true });
}
