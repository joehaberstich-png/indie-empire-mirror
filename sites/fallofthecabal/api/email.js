// Fall of the Cabal — Email Dispatch Engine
// Supports SendGrid + file-based fallback
const fs = require('fs');
const path = require('path');

const DATA_DIR = '/tmp/fotc_data';
const WAITLIST_FILE = path.join(DATA_DIR, 'waitlist.json');
const CAMPAIGNS_FILE = path.join(DATA_DIR, 'campaigns.json');

function read(file) {
  try { return JSON.parse(fs.readFileSync(file, 'utf8')); } catch(e) { 
    if (file === WAITLIST_FILE) return { entries: [], nextId: 1 };
    if (file === CAMPAIGNS_FILE) return { campaigns: [] };
    return {};
  }
}

function write(file, data) {
  fs.writeFileSync(file, JSON.stringify(data, null, 2));
}

// Load waitlist data
const data = read(WAITLIST_FILE);
const campaigns = read(CAMPAIGNS_FILE);

// ─── SENDGRID (if key is set) ───
const SENDGRID_KEY = process.env.SENDGRID_API_KEY || '';
const FROM_EMAIL = 'noreply@fallofthecabal.com';
const FROM_NAME = 'The Gardener — Fall of the Cabal';

async function sendViaSendgrid(to, subject, html) {
  if (!SENDGRID_KEY) return false;
  try {
    const res = await fetch('https://api.sendgrid.com/v3/mail/send', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${SENDGRID_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        personalizations: [{ to: [{ email: to }] }],
        from: { email: FROM_EMAIL, name: FROM_NAME },
        subject,
        content: [{ type: 'text/html', value: html }]
      })
    });
    return res.ok;
  } catch(e) { return false; }
}

// ─── MAILGUN FALLBACK (if SendGrid not configured) ───
async function sendViaMailgun(to, subject, html) {
  // Mailgun free tier: 100 emails/day, no credit card
  const MAILGUN_KEY = process.env.MAILGUN_API_KEY || '';
  const MAILGUN_DOMAIN = process.env.MAILGUN_DOMAIN || '';
  if (!MAILGUN_KEY || !MAILGUN_DOMAIN) return false;
  
  try {
    const form = new URLSearchParams();
    form.append('from', `${FROM_NAME} <${FROM_EMAIL}>`);
    form.append('to', to);
    form.append('subject', subject);
    form.append('html', html);
    
    const res = await fetch(`https://api.mailgun.net/v3/${MAILGUN_DOMAIN}/messages`, {
      method: 'POST',
      headers: { 'Authorization': 'Basic ' + btoa('api:' + MAILGUN_KEY) },
      body: form
    });
    return res.ok;
  } catch(e) { return false; }
}

// ─── FILE-BASED FALLBACK ───
// When no email API is configured, queue emails to /tmp/fotc_outbox/
// These can be downloaded and imported into any email platform
function queueToOutbox(email, name, subject, htmlContent, campaignId) {
  const outboxDir = path.join(DATA_DIR, 'outbox');
  if (!fs.existsSync(outboxDir)) fs.mkdirSync(outboxDir, { recursive: true });
  
  // Personalize
  const content = htmlContent
    .replace(/\{\{NAME\}\}/g, name || 'Operative')
    .replace(/\{\{EMAIL\}\}/g, email);
  
  const entry = { to: email, name, subject, content, campaignId, queuedAt: new Date().toISOString() };
  const safeEmail = email.replace(/[@.]/g, '_');
  fs.writeFileSync(path.join(outboxDir, `${campaignId}_${safeEmail}.json`), JSON.stringify(entry));
  return true;
}

// ─── CAMPAIGN DISPATCH ───
async function dispatchCampaign(campaignId, subject, htmlContent, filterFn) {
  const recipients = data.entries.filter(filterFn || (() => true));
  let sent = 0, failed = 0, queued = 0;
  
  for (const entry of recipients) {
    const to = entry.email;
    const name = entry.name;
    
    // Personalize content
    const personalized = htmlContent
      .replace(/\{\{NAME\}\}/g, name || 'Operative')
      .replace(/\{\{EMAIL\}\}/g, to)
      .replace(/\{\{REFCODE\}\}/g, entry.refCode || '')
      .replace(/\{\{LINK\}\}/g, `https://fallofthecabal.vercel.app/?ref=${entry.refCode || ''}`);
    
    // Try SendGrid first, then Mailgun, then queue
    let delivered = false;
    if (SENDGRID_KEY) delivered = await sendViaSendgrid(to, subject, personalized);
    if (!delivered && process.env.MAILGUN_API_KEY) delivered = await sendViaMailgun(to, subject, personalized);
    
    if (delivered) {
      sent++;
      entry.lastEmailSent = new Date().toISOString();
      if (!entry.campaignHistory) entry.campaignHistory = [];
      entry.campaignHistory.push(campaignId);
    } else {
      queueToOutbox(to, name, subject, personalized, campaignId);
      queued++;
      entry.lastEmailSent = new Date().toISOString();
      if (!entry.campaignHistory) entry.campaignHistory = [];
      entry.campaignHistory.push(campaignId);
    }
  }
  
  write(WAITLIST_FILE, data);
  return { sent, failed, queued, total: recipients.length };
}

module.exports = { dispatchCampaign, queueToOutbox, data, campaigns };
