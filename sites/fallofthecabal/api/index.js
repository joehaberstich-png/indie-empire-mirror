// Fall of the Cabal — Waitlist API with Email Dispatch
const fs = require('fs');
const path = require('path');
const { dispatchCampaign } = require('./email.js');

const DATA_DIR = '/tmp/fotc_data';
const WAITLIST_FILE = path.join(DATA_DIR, 'waitlist.json');
const CAMPAIGNS_FILE = path.join(DATA_DIR, 'campaigns.json');

function init() {
  if (!fs.existsSync(DATA_DIR)) fs.mkdirSync(DATA_DIR, { recursive: true });
  if (!fs.existsSync(WAITLIST_FILE)) fs.writeFileSync(WAITLIST_FILE, JSON.stringify({ entries: [], nextId: 1 }));
  if (!fs.existsSync(CAMPAIGNS_FILE)) fs.writeFileSync(CAMPAIGNS_FILE, JSON.stringify({ campaigns: [] }));
}

function read(file) {
  try { return JSON.parse(fs.readFileSync(file, 'utf8')); } catch(e) { return { entries: [], nextId: 1 }; }
}

function write(file, data) {
  fs.writeFileSync(file, JSON.stringify(data, null, 2));
}

init();

module.exports = async (req, res) => {
  const url = new URL(req.url, 'http://localhost');
  const pathParts = url.pathname.replace('/api/', '').split('/');
  const endpoint = pathParts[0];

  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,POST,OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();

  // ─── SUBSCRIBE ───
  if (endpoint === 'subscribe' && req.method === 'POST') {
    let body = '';
    for await (const chunk of req) body += chunk;
    const { email, name, source, ref } = JSON.parse(body);
    if (!email || !email.includes('@')) return res.status(400).json({ error: 'Valid email required.' });

    const data = read(WAITLIST_FILE);
    if (data.entries.find(e => e.email === email.toLowerCase())) {
      return res.status(200).json({ success: true, existing: true, message: 'Already on the list, Operative.' });
    }

    const id = data.nextId++;
    const refCode = btoa(email).replace(/=/g, '').substring(0, 8).toUpperCase();
    const now = new Date().toISOString();
    const entry = {
      id, email: email.toLowerCase(), name: name || '', source: source || 'direct',
      refCode, referredBy: ref || '', referrals: 0,
      isFounder: data.entries.length < 1000,
      launchPhase: 'BETA',
      disclaimer: 'All NFTs and game assets are in beta. Not an investment. Subject to change.',
      createdAt: now, lastEmailSent: null, campaignHistory: []
    };
    data.entries.push(entry);
    if (ref) {
      const referrer = data.entries.find(e => e.refCode === ref.toUpperCase());
      if (referrer) referrer.referrals++;
    }
    write(WAITLIST_FILE, data);

    return res.status(200).json({
      success: true, refCode,
      isFounder: entry.isFounder, position: data.entries.length,
      launchPhase: 'BETA',
      disclaimer: 'All NFTs and game assets are in beta. Not an investment. Subject to change.',
      message: entry.isFounder
        ? 'Founder Token slot confirmed! You are within the first 1,000.'
        : 'You are on the list. Founder spots are all taken.'
    });
  }

  // ─── COUNT ───
  if (endpoint === 'count' && req.method === 'GET') {
    const data = read(WAITLIST_FILE);
    return res.status(200).json({ count: data.entries.length });
  }

  // ─── LEADERBOARD ───
  if (endpoint === 'leaderboard' && req.method === 'GET') {
    const data = read(WAITLIST_FILE);
    const top = data.entries.filter(e => e.referrals > 0).sort((a, b) => b.referrals - a.referrals).slice(0, 100)
      .map(e => ({ name: e.name || 'Anonymous', referrals: e.referrals }));
    return res.status(200).json({ leaderboard: top });
  }

  // ─── ADMIN: LEADS ───
  if (endpoint === 'admin' && pathParts[1] === 'leads' && req.method === 'GET') {
    if (req.headers.authorization !== 'Bearer fotc_admin_2026') return res.status(401).json({ error: 'Unauthorized' });
    const data = read(WAITLIST_FILE);
    return res.status(200).json({
      total: data.entries.length, founders: data.entries.filter(e => e.isFounder).length,
      referrals: data.entries.reduce((sum, e) => sum + e.referrals, 0),
      entries: data.entries
    });
  }

  // ─── ADMIN: EXPORT CSV ───
  if (endpoint === 'admin' && pathParts[1] === 'export' && req.method === 'GET') {
    if (req.headers.authorization !== 'Bearer fotc_admin_2026') return res.status(401).json({ error: 'Unauthorized' });
    const data = read(WAITLIST_FILE);
    const csv = ['email,name,refCode,referredBy,referrals,isFounder,createdAt']
      .concat(data.entries.map(e => `${e.email},${e.name},${e.refCode},${e.referredBy},${e.referrals},${e.isFounder},${e.createdAt}`))
      .join('\n');
    res.setHeader('Content-Type', 'text/csv');
    res.setHeader('Content-Disposition', 'attachment; filename=fotc_waitlist.csv');
    return res.status(200).send(csv);
  }

  // ─── ADMIN: SEND EMAIL CAMPAIGN ───
  if (endpoint === 'admin' && pathParts[1] === 'campaign' && req.method === 'POST') {
    if (req.headers.authorization !== 'Bearer fotc_admin_2026') return res.status(401).json({ error: 'Unauthorized' });
    let body = '';
    for await (const chunk of req) body += chunk;
    const { subject, htmlContent, sendTo } = JSON.parse(body);

    const data = read(WAITLIST_FILE);
    const campaigns = read(CAMPAIGNS_FILE);
    const campaignId = campaigns.campaigns.length + 1;

    let filterFn = null;
    if (sendTo === 'founders') filterFn = (e) => e.isFounder;

    const result = await dispatchCampaign(campaignId, subject, htmlContent, filterFn);

    const campaign = {
      id: campaignId, subject, sendTo: sendTo || 'all',
      recipientCount: result.total, sent: result.sent, queued: result.queued,
      sentAt: new Date().toISOString(), opens: 0
    };
    campaigns.campaigns.push(campaign);
    write(CAMPAIGNS_FILE, campaigns);

    let note = '';
    if (result.sent > 0) note += `${result.sent} delivered via SendGrid. `;
    if (result.queued > 0) note += `${result.queued} queued to outbox. `;
    if (!note) note = 'No recipients found.';

    const sg = !!(process.env.SENDGRID_API_KEY);
    const mg = !!(process.env.MAILGUN_API_KEY && process.env.MAILGUN_DOMAIN);
    if (!sg && !mg && result.queued > 0) {
      note += ' Set SENDGRID_API_KEY in Vercel env vars for real-time delivery. Free: 100/day.';
    }

    return res.status(200).json({ success: true, campaignId, recipients: result.total, sent: result.sent, queued: result.queued, note });
  }

  // ─── ADMIN: GET CAMPAIGNS ───
  if (endpoint === 'admin' && pathParts[1] === 'campaigns' && req.method === 'GET') {
    if (req.headers.authorization !== 'Bearer fotc_admin_2026') return res.status(401).json({ error: 'Unauthorized' });
    const campaigns = read(CAMPAIGNS_FILE);
    return res.status(200).json(campaigns);
  }

  // ─── ADMIN: OUTBOX ───
  if (endpoint === 'admin' && pathParts[1] === 'outbox' && req.method === 'GET') {
    if (req.headers.authorization !== 'Bearer fotc_admin_2026') return res.status(401).json({ error: 'Unauthorized' });
    const outboxDir = '/tmp/fotc_data/outbox';
    let files = [];
    try { files = fs.readdirSync(outboxDir); } catch(e) {}
    const emails = files.filter(f => f.endsWith('.json')).map(f => {
      try { return JSON.parse(fs.readFileSync(path.join(outboxDir, f), 'utf8')); } catch(e) { return null; }
    }).filter(Boolean);
    return res.status(200).json({ total: emails.length, emails });
  }

  return res.status(404).json({ error: 'Not found' });
};
