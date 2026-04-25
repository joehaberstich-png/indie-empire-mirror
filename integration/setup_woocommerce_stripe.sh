#!/usr/bin/env bash
# WooCommerce + Stripe Integration Script
# Run after quantumbotsagency.com DNS is live and WordPress/WooCommerce is installed
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG="$SCRIPT_DIR/../.config/integrations.env"

# Load credentials (not in git)
if [ -f "$CONFIG" ]; then
  source "$CONFIG"
else
  echo "ERROR: .config/integrations.env not found. Store credentials first."
  exit 1
fi

echo "=== WooCommerce + Stripe Integration ==="
echo "Store: $WC_STORE_URL"
echo ""

# 1. Verify WooCommerce REST API is accessible
WC_HEALTH=$(curl -s -o /dev/null -w "%{http_code}" \
  -u "${WC_CONSUMER_KEY}:${WC_CONSUMER_SECRET}" \
  "${WC_STORE_URL}/wp-json/${WC_API_VERSION}/")
echo "WooCommerce API health: $WC_HEALTH"

if [ "$WC_HEALTH" != "200" ]; then
  echo "ERROR: WooCommerce API not reachable. Check URL and credentials."
  exit 1
fi

# 2. Configure Stripe payment gateway
echo ""
echo "Configuring Stripe payment gateway..."
curl -s -X PUT \
  -u "${WC_CONSUMER_KEY}:${WC_CONSUMER_SECRET}" \
  -H "Content-Type: application/json" \
  -d '{
    "enabled": true,
    "title": "Credit Card (Stripe)",
    "description": "Pay securely with your credit card via Stripe",
    "settings": {
      "publishable_key": "'"${STRIPE_PUBLISHABLE_KEY}"'",
      "secret_key": "'"${STRIPE_SECRET_KEY}"'",
      "test_mode": false
    }
  }' \
  "${WC_STORE_URL}/wp-json/${WC_API_VERSION}/payment_gateways/stripe" | jq '.id, .enabled, .title'

# 3. Create product categories for all 100 products
echo ""
echo "Creating product categories..."
declare -a CATEGORIES=(
  "AI Bots"
  "Affiliate Marketing"
  "Quantum Hosting"
  "Content Creation"
  "Marketing Automation"
  "Research & Intel"
  "Operations"
  "E-Commerce"
  "Data & Analytics"
  "Security & Compliance"
  "White Label Services"
)

for cat in "${CATEGORIES[@]}"; do
  echo "  Creating category: $cat"
  curl -s -X POST \
    -u "${WC_CONSUMER_KEY}:${WC_CONSUMER_SECRET}" \
    -H "Content-Type: application/json" \
    -d '{"name": "'"${cat}"'", "description": "'"${cat}" - Product category for Quantum Bots Agency"}"}' \
    "${WC_STORE_URL}/wp-json/${WC_API_VERSION}/products/categories" | jq -r '.id, .name'
done

# 4. Create monthly subscription products for 5 bot tiers
echo ""
echo "Creating subscription products..."
declare -a PRODUCTS=(
  "Standard Bot:97:AI Bots:Basic automation with rule-based triggers. Single-platform operation."
  "Advanced Bot:197:AI Bots:Pattern recognition + ML. Multi-platform with 3 API connectors."
  "Intelligent Bot:497:AI Bots:Neural network engine. Self-learning. Cross-platform orchestration."
  "Quantum-Light Bot:997:AI Bots:Quantum-inspired optimization. Real-time market adaptation."
  "Full Quantum Bot:2497:AI Bots:True quantum decision engine. Entanglement-based optimization."
  "Affiliate Marketing Bot:47:Affiliate Marketing:Dedicated affiliate automation. ClickBank, Amazon, ShareASale + CJ."
)

for product in "${PRODUCTS[@]}"; do
  NAME="${product%%:*}"
  REST="${product#*:}"
  PRICE="${REST%%:*}"
  CAT="${REST##*:}"
  
  echo "  Creating: $NAME (\$${PRICE}/mo)"
  
  # Get category ID
  CAT_ID=$(curl -s \
    -u "${WC_CONSUMER_KEY}:${WC_CONSUMER_SECRET}" \
    "${WC_STORE_URL}/wp-json/${WC_API_VERSION}/products/categories?search=${CAT}" | jq '.[0].id')
  
  curl -s -X POST \
    -u "${WC_CONSUMER_KEY}:${WC_CONSUMER_SECRET}" \
    -H "Content-Type: application/json" \
    -d '{
      "name": "'"${NAME}"'",
      "type": "simple",
      "regular_price": "'"${PRICE}"'",
      "description": "'"${NAME}" - '"${REST#*:}"'"",
      "short_description": "'"${REST#*:}"'",
      "categories": [{"id": '"${CAT_ID}"'}],
      "attributes": [{"name": "Billing", "options": ["Monthly"]}],
      "meta_data": [{"key": "_subscription_period", "value": "month"}]
    }' \
    "${WC_STORE_URL}/wp-json/${WC_API_VERSION}/products" | jq -r '.id, .name, .price'
done

# 5. Create hosting products with free domain metadata
echo ""
echo "Creating hosting products..."
declare -a HOSTING=(
  "Quantum Static:9:1 website, 5GB storage, 50GB bandwidth, PQC TLS 1.3, Daily backups:1"
  "Quantum Starter:19:3 websites, 20GB storage, 200GB bandwidth, PQC TLS 1.3, Daily backups:1"
  "Quantum Business:49:10 websites, 100GB storage, 1TB bandwidth, PQC TLS 1.3, 6hr backups:2"
  "Quantum Agency:99:25 websites, 500GB storage, 5TB bandwidth, PQC TLS 1.3, 3hr backups:3"
  "Quantum Enterprise:199:100 websites, 2TB storage, 20TB bandwidth, PQC TLS + SIEM, 1hr backups:5"
  "Quantum White Label:499:Unlimited websites, 5TB storage, 50TB bandwidth, PQC TLS + reseller, 30min backups:10"
  "Quantum Dedicated:999:Unlimited + dedicated, 10TB NVMe, 100TB bandwidth, Continuous backups:25"
  "Quantum Sovereign:2499:Unlimited + air-gapped, 50TB encrypted, 500TB bandwidth, Geo-redundant:50"
  "Quantum Military:4999:Unmetered everything, 200TB + HSM, 24/7 dedicated security:100"
)

CAT_ID=$(curl -s \
  -u "${WC_CONSUMER_KEY}:${WC_CONSUMER_SECRET}" \
  "${WC_STORE_URL}/wp-json/${WC_API_VERSION}/products/categories?search=Quantum Hosting" | jq '.[0].id')

for plan in "${HOSTING[@]}"; do
  NAME="${plan%%:*}"
  REST="${plan#*:}"
  PRICE="${REST%%:*}"
  REST2="${REST#*:}"
  DESC="${REST2%:*}"
  DOMAINS="${REST2##*:}"
  
  echo "  Creating: $NAME (\$${PRICE}/mo, ${DOMAINS} free domain(s))"
  
  curl -s -X POST \
    -u "${WC_CONSUMER_KEY}:${WC_CONSUMER_SECRET}" \
    -H "Content-Type: application/json" \
    -d '{
      "name": "'"${NAME}"'",
      "type": "simple",
      "regular_price": "'"${PRICE}"'",
      "description": "'"${DESC}"'",
      "categories": [{"id": '"${CAT_ID}"'}],
      "meta_data": [
        {"key": "free_domains", "value": "'"${DOMAINS}"'"},
        {"key": "_subscription_period", "value": "month"}
      ]
    }' \
    "${WC_STORE_URL}/wp-json/${WC_API_VERSION}/products" | jq -r '.id, .name, .price'
done

echo ""
echo "=== Integration Complete ==="
echo "Stripe live mode enabled"
echo "Product categories created"
echo "Subscription products configured"
echo ""
echo "Next step: Verify products in WordPress admin → WooCommerce → Products"
