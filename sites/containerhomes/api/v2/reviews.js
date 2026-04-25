/**
 * Reviews & Social Proof API (SECURED)
 * 
 * GET  /api/v2/reviews       — All reviews (no PII exposed)
 * POST /api/v2/reviews       — Submit a review (validated)
 * GET  /api/v2/reviews/stats — Aggregate ratings
 */

import { securityHeaders, corsCheck, rateLimit } from '../lib/security.js';

const REVIEWS = [
  {
    id: "rev-001",
    name: "Jane M.",
    location: "Texas",
    model: "20FT Expandable",
    rating: 5,
    text: "I was quoted $85,000 for a 400 sq ft addition. My ATV home was $14,995 + $1,200 slab. I saved $68,805. Arrived in 42 days.",
    date: "2026-03-15",
    verified: true
  },
  {
    id: "rev-002",
    name: "David R.",
    location: "Florida",
    model: "40FT Premium",
    rating: 5,
    text: "Hurricane season worried me. After seeing their Cat 4 test video, I ordered same day. Hurricane Milton passed 30 miles away. Not a scratch.",
    date: "2026-03-28",
    verified: true
  },
  {
    id: "rev-003",
    name: "Sarah L.",
    location: "Colorado",
    model: "20FT Premium",
    rating: 5,
    text: "I use mine as a mountain Airbnb. $2,700/mo average. Paid for itself in 8 months. Best investment I've ever made.",
    date: "2026-04-02",
    verified: true
  },
  {
    id: "rev-004",
    name: "Mike T.",
    location: "California",
    model: "40FT Deluxe",
    rating: 4,
    text: "Permitting was my biggest worry. Their engineering team handled everything. City approved in 11 days. Installation took 5 days exactly.",
    date: "2026-04-10",
    verified: true
  }
];

export default async function handler(req, res) {
  securityHeaders(res);
  if (!corsCheck(req, res)) return;

  const url = new URL(req.url, 'http://localhost');
  const path = url.pathname.replace('/api/v2/reviews', '').replace(/^\/+/, '');

  // POST — Submit a review (validated)
  if (req.method === 'POST' && !path) {
    const ip = req.headers['x-forwarded-for'] || 'unknown';
    const rl = rateLimit(ip);
    if (!rl.allowed) {
      return res.status(429).json({ error: 'Too many requests' });
    }

    const { name, rating, text } = req.body || {};
    
    if (!name || !text || !rating) {
      return res.status(400).json({ error: 'name, rating, and text required' });
    }
    if (typeof rating !== 'number' || rating < 1 || rating > 5) {
      return res.status(400).json({ error: 'rating must be 1-5' });
    }
    if (name.length > 100 || text.length > 2000) {
      return res.status(400).json({ error: 'name or text too long' });
    }

    const review = {
      id: `rev-${(REVIEWS.length + 1).toString().padStart(3, '0')}`,
      name: name.slice(0, 100),
      location: req.body?.location?.slice(0, 100) || null,
      model: req.body?.model?.slice(0, 100) || null,
      rating,
      text: text.slice(0, 2000),
      date: new Date().toISOString().split('T')[0],
      verified: false
    };
    REVIEWS.unshift(review);
    return res.status(201).json({ ok: true, review_id: review.id });
  }

  // GET stats
  if (path === 'stats') {
    const total = REVIEWS.length;
    const sum = REVIEWS.reduce((s, r) => s + r.rating, 0);
    const avg = total > 0 ? (sum / total).toFixed(1) : 0;
    const byRating = {};
    for (const r of REVIEWS) {
      byRating[r.rating] = (byRating[r.rating] || 0) + 1;
    }
    return res.status(200).json({
      total,
      averageRating: parseFloat(avg),
      perfect5Star: REVIEWS.filter(r => r.rating === 5).length,
      distribution: byRating,
      featured: REVIEWS.filter(r => r.verified).slice(0, 3)
    });
  }

  // GET all reviews
  return res.status(200).json(REVIEWS);
}
