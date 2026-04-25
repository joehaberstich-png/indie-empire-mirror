#!/usr/bin/env bash
# API Acquisition Script — P0 Priority
# Run this to register for BrightData + Twitter API
# User: complete the signup forms at the URLs below, then paste keys here

set -e

echo "═══════════════════════════════════════════"
echo "  API ACQUISITION — P0 Priority           "
echo "  Run this to complete API setup           "
echo "═══════════════════════════════════════════"
echo ""

# ─── P0: BrightData (Residential Proxies) ───
echo "┌─────────────────────────────────────────┐"
echo "│ P0-1: BRIGHTDATA (Residential Proxies)  │"
echo "├─────────────────────────────────────────┤"
echo "│ URL: https://brightdata.com/signup       │"
echo "│ Plan: Pay-as-you-go (no monthly minimum) │"
echo "│ Cost: ~$15/GB → $300/mo est             │"
echo "│ Use: Proxy pool for 10K agent identities │"
echo "│ Note: 15K residential IPs included       │"
echo "└─────────────────────────────────────────┘"
echo ""
echo "After registering, paste your BrightData API token:"
read -p "  → BRIGHTDATA_TOKEN: " BD_TOKEN

# ─── P0: Twitter/X API Basic ───
echo ""
echo "┌─────────────────────────────────────────┐"
echo "│ P0-2: TWITTER/X API BASIC               │"
echo "├─────────────────────────────────────────┤"
echo "│ URL: https://developer.twitter.com       │"
echo "│ Plan: Basic ($100/mo)                    │"
echo "│ Use: Agent social media posting          │"
echo "│ Note: Need 10K rate limit / 15-min       │"
echo "└─────────────────────────────────────────┘"
echo ""
echo "After registering, paste your Twitter API credentials:"
read -p "  → TWITTER_API_KEY: " TW_KEY
read -p "  → TWITTER_API_SECRET: " TW_SECRET
read -p "  → TWITTER_BEARER_TOKEN: " TW_BEARER

# ─── Store credentials ───
echo ""
echo "Storing credentials in .config/api_keys.env (gitignored)..."
cat >> /var/openclaw_users/saul/.openclaw/workspace/.config/api_keys.env << EOF

# ─── API Credentials (Auto-registered) ───
# BrightData
BRIGHTDATA_TOKEN="${BD_TOKEN}"
BRIGHTDATA_API_URL="https://api.brightdata.com"

# Twitter/X API
TWITTER_API_KEY="${TW_KEY}"
TWITTER_API_SECRET="${TW_SECRET}"
TWITTER_BEARER_TOKEN="${TW_BEARER}"
TWITTER_API_VERSION="2"
TWITTER_PLAN="Basic"
TWITTER_RATE_LIMIT="10000/15min"
EOF
chmod 600 /var/openclaw_users/saul/.openclaw/workspace/.config/api_keys.env

echo ""
echo "✅ P0 credentials stored in .config/api_keys.env"
echo ""
echo "═══════════════════════════════════════════"
echo "  NEXT: P1 APIs — run when ready          "
echo "  Stability AI: https://platform.stability.ai"
echo "  Midjourney: https://midjourney.com       "
echo "  Ahrefs: https://ahrefs.com               "
echo "═══════════════════════════════════════════"
