# Fall of the Cabal — Email Integration Setup

## Option 1: SendGrid (Recommended) — Free: 100 emails/day

1. Go to https://signup.sendgrid.com — create free account (no credit card)
2. Verify your email and login
3. Go to Settings → API Keys → Create API Key
4. Choose "Full Access" or "Restricted Access" with Mail Send permission

Run this to set it:
```bash
# Then paste your key when prompted
```

## Option 2: Mailgun — Free: 100 emails/day, also no credit card

1. Go to https://www.mailgun.com/ — sign up free
2. Verify email, get a sandbox domain
3. Get your API key from Settings → API Keys

```bash
npx vercel env add MAILGUN_DOMAIN production --token [REDACTED]
```

## How it works after setup:
1. When you click "Dispatch Campaign" in the admin panel → sends via SendGrid/Mailgun in real-time
2. If no API key → emails queue to /tmp/fotc_data/outbox/
3. You can download the outbox CSV from admin → Export tab, or via API

## Current Status
- ✅ Waitlist form captures name + email + referral codes
- ✅ Admin dashboard shows all leads
- ✅ 7 pre-built email templates (Welcome → Intel Drops → Referral → Trailer → Mint → Launch)
- ❌ No email API key set yet — emails queue to outbox until you add one
