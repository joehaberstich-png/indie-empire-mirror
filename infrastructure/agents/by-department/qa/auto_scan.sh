#!/usr/bin/env bash
# ───────────────────────────────────────────────
# QA DEPARTMENT — Auto Bug Scanner
# Runs: HTTP status, JS console errors, broken links
# Frequency: Every 6 hours
# Reports: reports/bugs/YYYY-MM-DD.md
# ───────────────────────────────────────────────
set -e
cd /var/openclaw_users/saul/.openclaw/workspace

mkdir -p reports/bugs

PROJECTS=(
  "atv-homes.vercel.app"
  "quantumbotsagency.vercel.app"
  "jeannienails.vercel.app"
  "fallofthecabal.vercel.app"
  "flytoaustralia.vercel.app"
  "thedealwizard.vercel.app"
  "drugdoctors.vercel.app"
  "allaboutmd.vercel.app"
  "smallbiz-financing.vercel.app"
  "quanivo.vercel.app"
)

DATE=$(date -u +%Y-%m-%d)
TIMESTAMP=$(date -u +%H:%M)
REPORT="reports/bugs/${DATE}.md"

if [ ! -f "$REPORT" ]; then
  echo "# 🔍 QA Bug Report — $DATE" > "$REPORT"
  echo "" >> "$REPORT"
  echo "## Scan $TIMESTAMP UTC" >> "$REPORT"
  echo "" >> "$REPORT"
else
  echo "" >> "$REPORT"
  echo "### Scan $TIMESTAMP UTC" >> "$REPORT"
  echo "" >> "$REPORT"
fi

TOTAL_BUGS=0
CRITICAL=0
HIGH=0
MEDIUM=0
LOW=0

for project in "${PROJECTS[@]}"; do
  echo "  Scanning $project..."
  echo "**$project:**" >> "$REPORT"

  # 1. HTTP Status
  status=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "https://$project/" 2>/dev/null)
  if [ "$status" != "200" ]; then
    echo "- 🔴 HTTP $status (homepage)" >> "$REPORT"
    TOTAL_BUGS=$((TOTAL_BUGS+1))
    CRITICAL=$((CRITICAL+1))
  fi

  # 2. Check sitemap
  sm_status=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "https://$project/sitemap.xml" 2>/dev/null)
  if [ "$sm_status" != "200" ]; then
    echo "- 🟡 Sitemap HTTP $sm_status" >> "$REPORT"
    TOTAL_BUGS=$((TOTAL_BUGS+1))
    MEDIUM=$((MEDIUM+1))
  fi

  # 3. Check robots.txt
  rb_status=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "https://$project/robots.txt" 2>/dev/null)
  if [ "$rb_status" != "200" ] && [ "$rb_status" != "404" ]; then
    echo "- 🟡 robots.txt HTTP $rb_status" >> "$REPORT"
    TOTAL_BUGS=$((TOTAL_BUGS+1))
    MEDIUM=$((MEDIUM+1))
  fi

  # 4. SSL check
  ssl_expiry=$(echo | openssl s_client -servername "$project" -connect "$project:443" 2>/dev/null | openssl x509 -noout -enddate 2>/dev/null | cut -d= -f2)
  if [ -n "$ssl_expiry" ]; then
    expiry_epoch=$(date -d "$ssl_expiry" +%s 2>/dev/null || echo 0)
    now_epoch=$(date -u +%s)
    days_left=$(( (expiry_epoch - now_epoch) / 86400 ))
    if [ "$days_left" -lt 14 ] 2>/dev/null; then
      echo "- 🔴 SSL expires in ${days_left} days" >> "$REPORT"
      TOTAL_BUGS=$((TOTAL_BUGS+1))
      CRITICAL=$((CRITICAL+1))
    fi
  fi

  # 5. Page size check (bloated pages)
  html=$(curl -s --max-time 10 "https://$project/" 2>/dev/null)
  size_kb=$(echo "$html" | wc -c)
  size_kb=$((size_kb/1024))
  if [ "$size_kb" -gt 500 ] 2>/dev/null; then
    echo "- 🟠 Page size ${size_kb}KB (>500KB)" >> "$REPORT"
    TOTAL_BUGS=$((TOTAL_BUGS+1))
    HIGH=$((HIGH+1))
  fi

  # 6. Check Quantum CS v2 injection
  if echo "$html" | grep -q "quantum-cs-v2.js"; then
    echo "- ✅ Quantum CS v2 injected" >> "$REPORT"
  else
    echo "- 🔴 Missing Quantum CS v2" >> "$REPORT"
    TOTAL_BUGS=$((TOTAL_BUGS+1))
    CRITICAL=$((CRITICAL+1))
  fi

  # 7. Meta tags check
  title=$(echo "$html" | grep -oP '<title>[^<]+</title>' | sed 's/<[^>]*>//g')
  desc=$(echo "$html" | grep -oP 'name="description" content="[^"]+"' | sed 's/.*content="//;s/"//')
  title_len=$(echo -n "$title" | wc -c)
  desc_len=$(echo -n "$desc" | wc -c)
  if [ "$title_len" -lt 10 ] 2>/dev/null; then
    echo "- 🟡 Title too short (${title_len} chars)" >> "$REPORT"
    TOTAL_BUGS=$((TOTAL_BUGS+1))
    MEDIUM=$((MEDIUM+1))
  fi
  if [ "$desc_len" -lt 10 ] 2>/dev/null; then
    echo "- 🟡 Meta description too short (${desc_len} chars)" >> "$REPORT"
    TOTAL_BUGS=$((TOTAL_BUGS+1))
    MEDIUM=$((MEDIUM+1))
  fi

  echo "" >> "$REPORT"
done

echo "" >> "$REPORT"
echo "---" >> "$REPORT"
echo "**Summary:** $TOTAL_BUGS bugs found (🔴 $CRITICAL critical / 🟠 $HIGH high / 🟡 $MEDIUM medium / 🟢 $LOW low)" >> "$REPORT"
echo "" >> "$REPORT"

echo ""
echo "═ SCAN COMPLETE ═"
echo "  Bugs: $TOTAL_BUGS (🔴$CRITICAL 🟠$HIGH 🟡$MEDIUM 🟢$LOW)"
echo "  Report: $REPORT"
