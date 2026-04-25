#!/bin/bash
# QUANTUM HEALTH SCAN v1.0
# Checks: HTTP status, broken pages, missing JS/CSS, video tags, canvas elements, sitemap integrity
set -e
cd /var/openclaw_users/saul/.openclaw/workspace

DATE=$(date +%Y-%m-%d_%H%M)
OUTPUT="reports/health-scan-${DATE}.md"
mkdir -p reports

echo "# 🏆 Quantum Health Scan — $(date -u '+%Y-%m-%d %H:%M UTC')" > "$OUTPUT"
echo "" >> "$OUTPUT"

SCORE=0
TOTAL=0
BROKEN=0

scan_project() {
  local name="$1"
  local url="$2"
  local local_dir="$3"
  
  TOTAL=$((TOTAL + 1))
  echo "" >> "$OUTPUT"
  echo "## ✅ $name" >> "$OUTPUT"
  echo "**URL**: $url" >> "$OUTPUT"
  echo "**Local**: $local_dir" >> "$OUTPUT"
  echo "" >> "$OUTPUT"
  
  # 1. HTTP status
  local http_code=$(curl -sL -o /tmp/scan_${name// /_}.html -w "%{http_code}" "$url" 2>/dev/null)
  if [ "$http_code" = "200" ] || [ "$http_code" = "307" ]; then
    echo "- **HTTP Status**: \`$http_code\` ✅" >> "$OUTPUT"
  else
    echo "- **HTTP Status**: \`$http_code\` ❌" >> "$OUTPUT"
    BROKEN=$((BROKEN + 1))
  fi
  
  # 2. Page size
  local size=$(wc -c < /tmp/scan_${name// /_}.html 2>/dev/null | tr -d ' ')
  echo "- **Page Size**: ${size} bytes" >> "$OUTPUT"
  
  # 3. Word count (meaningful content)
  local words=$(sed 's/<[^>]*>//g' /tmp/scan_${name// /_}.html 2>/dev/null | wc -w | tr -d ' ')
  echo "- **Content Words**: $words" >> "$OUTPUT"
  
  local html_content=$(cat /tmp/scan_${name// /_}.html 2>/dev/null)
  
  # 4. Check for broken/missing JS references
  local js_refs=$(echo "$html_content" | grep -oP 'src="[^"]+\.js"' | sed 's/src="//;s/"$//' | sort -u)
  local js_missing=0
  while IFS= read -r js; do
    [ -z "$js" ] && continue
    local js_url="${url%%/*}/$js"
    local js_code=$(curl -sL -o /dev/null -w "%{http_code}" "$js_url" 2>/dev/null)
    if [ "$js_code" != "200" ]; then
      # Try relative to the local dir
      local local_js="${local_dir}/${js#/}"
      if [ ! -f "$local_js" ]; then
        js_missing=$((js_missing + 1))
        echo "  - ❌ Missing JS: \`$js\` (HTTP $js_code)" >> "$OUTPUT"
      fi
    fi
  done <<< "$js_refs"
  if [ "$js_missing" -eq 0 ]; then
    echo "- **JS Assets**: All found ✅" >> "$OUTPUT"
  else
    echo "- **JS Assets**: $js_missing missing ❌" >> "$OUTPUT"
  fi
  
  # 5. Check for broken CSS
  local css_refs=$(echo "$html_content" | grep -oP 'href="[^"]+\.css"' | sed 's/href="//;s/"$//' | sort -u)
  local css_missing=0
  while IFS= read -r css; do
    [ -z "$css" ] && continue
    # Check locally
    local local_css="${local_dir}/${css#/}"
    if [ ! -f "$local_css" ]; then
      css_missing=$((css_missing + 1))
      echo "  - ❌ Missing CSS: \`$css\`" >> "$OUTPUT"
    fi
  done <<< "$css_refs"
  if [ "$css_missing" -eq 0 ]; then
    echo "- **CSS Assets**: All found ✅" >> "$OUTPUT"
  else
    echo "- **CSS Assets**: $css_missing missing ❌" >> "$OUTPUT"
  fi
  
  # 6. Check for video tags
  local video_count=$(echo "$html_content" | grep -ci '<video\|<source.*\.\(mp4\|webm\|ogg\)' 2>/dev/null)
  if [ "$video_count" -gt 0 ]; then
    echo "- **Video Tags**: $video_count found" >> "$OUTPUT"
    
    # Check if videos are empty placeholders (all placeholder)
    local placeholder_count=$(echo "$html_content" | grep -ci "placeholder\|Coming Soon\|trailer-coming\|vid-label" 2>/dev/null)
    if [ "$placeholder_count" -gt 0 ] && [ "$video_count" -le "$placeholder_count" ]; then
      echo "  - ⚠️  All video elements are placeholders (coming soon)" >> "$OUTPUT"
    fi
    
    # Check for broken video sources
    local video_sources=$(echo "$html_content" | grep -oP 'src="[^"]+\.(mp4|webm|ogg)"' | sed 's/src="//;s/"$//')
    while IFS= read -r vsrc; do
      [ -z "$vsrc" ] && continue
      local local_video="${local_dir}/${vsrc#/}"
      if [ ! -f "$local_video" ] && [[ "$vsrc" != http* ]]; then
        echo "  - ❌ Missing video: \`$vsrc\`" >> "$OUTPUT"
      fi
    done <<< "$video_sources"
  else
    echo "- **Video Tags**: None found" >> "$OUTPUT"
  fi
  
  # 7. Check for canvas/WebGL elements
  local canvas_count=$(echo "$html_content" | grep -ci '<canvas' 2>/dev/null)
  local webgl_count=$(echo "$html_content" | grep -ci 'webgl\|getContext.*2d\|three\.js\|babylon\|pixi' 2>/dev/null)
  if [ "$canvas_count" -gt 0 ] || [ "$webgl_count" -gt 0 ]; then
    echo "- **Canvas/WebGL**: $canvas_count canvas elements, $webgl_count WebGL references" >> "$OUTPUT"
  else
    echo "- **Canvas/WebGL**: None found" >> "$OUTPUT"
  fi
  
  # 8. Check meta tags
  local meta_desc=$(echo "$html_content" | grep -oP '<meta name="description" content="[^"]*"' | head -1)
  if [ -n "$meta_desc" ]; then
    echo "- **Meta Description**: Present ✅" >> "$OUTPUT"
  else
    echo "- **Meta Description**: MISSING ❌" >> "$OUTPUT"
  fi
  
  # 9. Check viewport meta
  if echo "$html_content" | grep -qi 'viewport'; then
    echo "- **Viewport Meta**: Present ✅" >> "$OUTPUT"
  else
    echo "- **Viewport Meta**: MISSING ❌" >> "$OUTPUT"
  fi
  
  # 10. Check sitemap
  local sitemap_url="${url%/}/sitemap.xml"
  local sitemap_code=$(curl -sL -o /dev/null -w "%{http_code}" "$sitemap_url" 2>/dev/null)
  if [ "$sitemap_code" = "200" ]; then
    local sitemap_urls=$(curl -sL "$sitemap_url" 2>/dev/null | grep -ocP '<loc>' || echo 0)
    echo "- **Sitemap**: HTTP $sitemap_code ✅ ($sitemap_urls URLs)" >> "$OUTPUT"
  else
    echo "- **Sitemap**: HTTP $sitemap_code (no sitemap)" >> "$OUTPUT"
  fi
  
  # 11. Quantum CS v2 check
  if echo "$html_content" | grep -qi "quantum-cs-v2\|quantum-cs\|qcs-btn\|9 Languages"; then
    echo "- **Quantum CS v2**: Injected ✅" >> "$OUTPUT"
  else
    echo "- **Quantum CS v2**: MISSING ❌" >> "$OUTPUT"
  fi
  
  # 12. Image loading check
  local img_tags=$(echo "$html_content" | grep -oP 'src="[^"]+\.(jpg|jpeg|png|gif|webp|svg)"' | sed 's/src="//;s/"$//')
  local img_broken=0
  while IFS= read -r img; do
    [ -z "$img" ] && continue
    local local_img="${local_dir}/${img#/}"
    if [ ! -f "$local_img" ]; then
      img_broken=$((img_broken + 1))
    fi
  done <<< "$img_tags"
  if [ "$img_broken" -eq 0 ]; then
    echo "- **Images**: All found locally ✅" >> "$OUTPUT"
  else
    echo "- **Images**: $img_broken could not be verified locally" >> "$OUTPUT"
  fi
  
  echo "" >> "$OUTPUT"
  echo "---" >> "$OUTPUT"
}

# ─── SCAN ALL PROJECTS ───

scan_project "ATV Homes / Container Homes" "https://atv-homes.vercel.app" "site/containerhomes"
scan_project "Quantum Bots Agency" "https://quantum-bots-agency.vercel.app" "site/quantumbotsagency"
scan_project "Jeannie Nails" "https://jeannienails.vercel.app" "site/jeannienails"
scan_project "Fall of the Cabal" "https://fallofthecabal.vercel.app" "site/fallofthecabal"
scan_project "Fly To Australia" "https://flytoaustralia.vercel.app" "site/flytoaustralia"
scan_project "The Deal Wizard" "https://thedealwizard.vercel.app" "site/thedealwizard"
scan_project "Drug Doctors" "https://drugdoctors.vercel.app" "site/drugdoctors"
scan_project "All About MD" "https://allaboutmd.vercel.app" "site/allaboutmd"
scan_project "Small Biz Financing" "https://smallbiz-financing.vercel.app" "site/smallbiz"
scan_project "Quanivo Agency" "https://quanivo.vercel.app" "site/quanivo"

# Summry
echo "" >> "$OUTPUT"
echo "# 📊 Summary" >> "$OUTPUT"
echo "- **Projects Scanned**: $TOTAL" >> "$OUTPUT"
echo "- **HTTP Errors**: $BROKEN" >> "$OUTPUT"

echo ""
echo "═══════════════════════════════════════════"
echo "  QUANTUM HEALTH SCAN COMPLETE"
echo "  $TOTAL projects scanned | $BROKEN issues found"
echo "  Report: $OUTPUT"
echo "═══════════════════════════════════════════"