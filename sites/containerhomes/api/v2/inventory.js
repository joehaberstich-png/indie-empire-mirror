/**
 * Inventory & Order Status API (SECURED)
 * 
 * GET  /api/v2/inventory     — Current stock levels for all models
 * GET  /api/v2/inventory/{id} — Single model stock
 */

import { securityHeaders, corsCheck } from '../lib/security.js';

const MODELS = {
  "20ft-expandable": {
    name: "20FT Expandable",
    price: 14995,
    stock: 47,
    leadTime: "45 days",
    inProduction: true,
    nextBatch: "2026-05-15"
  },
  "20ft-premium": {
    name: "20FT Premium",
    price: 19995,
    stock: 23,
    leadTime: "45 days",
    inProduction: true,
    nextBatch: "2026-05-20"
  },
  "40ft-deluxe": {
    name: "40FT Deluxe",
    price: 24995,
    stock: 12,
    leadTime: "45 days",
    inProduction: true,
    nextBatch: "2026-05-25"
  },
  "40ft-premium": {
    name: "40FT Premium",
    price: 34995,
    stock: 8,
    leadTime: "60 days",
    inProduction: true,
    nextBatch: "2026-06-01"
  }
};

export default async function handler(req, res) {
  securityHeaders(res);
  if (!corsCheck(req, res)) return;

  const url = new URL(req.url, 'http://localhost');
  const path = url.pathname.replace('/api/v2/inventory', '').replace(/^\/+/, '');
  const lowerPath = path.toLowerCase();

  // All models
  if (!lowerPath) {
    return res.status(200).json({
      lastUpdated: new Date().toISOString(),
      totalModels: Object.keys(MODELS).length,
      totalStock: Object.values(MODELS).reduce((s, m) => s + m.stock, 0),
      models: MODELS
    });
  }

  // Single model
  const model = MODELS[lowerPath];
  if (model) {
    return res.status(200).json(model);
  }

  return res.status(404).json({ error: 'Model not found', available: Object.keys(MODELS) });
}
