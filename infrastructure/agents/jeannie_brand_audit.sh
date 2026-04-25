#!/bin/bash
# JEANNIE NAILS — Full Brand Audit & Fix
# Changes "Jeannie Boutiler Nails" → "Jeannie Nails" across ALL files
# Also fixes: nav-logo-text, schema.org name, meta tags, alt text, aria labels

SITE="/var/openclaw_users/saul/.openclaw/workspace/site/jeannienails"
FIXES=0

echo "═══ JEANNIE NAILS — FULL BRAND AUDIT ═══"
echo ""

# === 1. Meta tags & titles ===
echo "→ Fixing <title> and <meta> tags..."
for f in $(find "$SITE" -name "*.html" -type f); do
  sed -i 's|Jeannie Boutiler Nails|Jeannie Nails|g' "$f"
  sed -i 's|Jeannie Boutiler |Jeannie |g' "$f"
  ((FIXES++))
done

# === 2. visible text ===
echo "→ Fixing visible text content..."
find "$SITE" -name "*.html" -type f -exec sed -i 's|Jeannie Boutiler Nails|Jeannie Nails|g' {} \;
find "$SITE" -name "*.html" -type f -exec sed -i 's|Jeannie Boutiler |Jeannie |g' {} \;

# === 3. nav-logo-text (keeps the <span>Nails</span> intact) ===
echo "→ Fixing nav-logo-text..."
find "$SITE" -name "*.html" -type f -exec sed -i 's|Jeannie Boutiler<span>Nails</span>|Jeannie <span>Nails</span>|g' {} \;

# === 4. brand class ===
echo "→ Fixing brand text..."
find "$SITE" -name "*.html" -type f -exec sed -i 's|Jeannie Boutiler <span>Nails</span>|Jeannie <span>Nails</span>|g' {} \;

# === 5. schema.org JSON-LD ===
echo "→ Fixing schema.org JSON-LD..."
sed -i 's|"name": "Jeannie Boutiler Nails"|"name": "Jeannie Nails"|g' "$SITE/index.html"
sed -i 's|"name": "Jeannie Boutiler"|"name": "Jeannie Nails"|g' "$SITE/index.html"

# === 6. keywords meta ===
echo "→ Fixing meta keywords..."
sed -i 's|Jeannie Boutiler|Jeannie Nails|g' "$SITE/index.html"

# === 7. JavaScript bot files ===
echo "→ Fixing bot JS..."
for f in $(find "$SITE" -name "*.js" -type f); do
  sed -i 's|Jeannie Boutiler Nails|Jeannie Nails|g' "$f"
  sed -i 's|Jeannie Boutiler |Jeannie |g' "$f"
done

# === 8. Back office settings ===
echo "→ Fixing back office settings..."
sed -i 's|value="Jeannie Boutiler Nails"|value="Jeannie Nails"|g' "$SITE/manage/index.html"
sed -i 's|Jeannie Boutiler (Owner)|Jeannie (Owner)|g' "$SITE/training/index.html"

# === 9. Footer variants ===
echo "→ Fixing footer text..."
find "$SITE" -name "*.html" -type f -exec sed -i 's|Jeannie Boutiler Nails ·|Jeannie Nails ·|g' {} \;
find "$SITE" -name "*.html" -type f -exec sed -i 's|Jeannie Boutiler Nails &#183;|Jeannie Nails &#183;|g' {} \;

# === 10. Back-link text ===
echo "→ Fixing back-link text..."
find "$SITE" -name "*.html" -type f -exec sed -i 's|Back to Jeannie Boutiler Nails|Back to Jeannie Nails|g' {} \;

# === 11. About section ===
echo "→ Fixing about/bio text..."
sed -i 's|Jeannie Boutiler Nails brings|Jeannie Nails brings|g' "$SITE/index.html"

# === 12. Blog article first-paragraph mentions ===
echo "→ Fixing blog body text..."
find "$SITE/blog" -name "*.html" -type f -exec sed -i 's|Jeannie Boutiler Nails|Jeannie Nails|g' {} \;

# === VERIFY NO REMAINING 'Boutiler' ===
echo ""
echo "═══ VERIFYING ZERO REMAINING ═══"
REMAINING=$(grep -rn "Boutiler" "$SITE" --include="*.html" --include="*.js" --include="*.json" . 2>/dev/null | wc -l)
if [ "$REMAINING" -eq 0 ]; then
  echo "✅ ZERO 'Boutiler' instances remaining — clean sweep!"
else
  echo "⚠️  $REMAINING instances remaining — manual check needed:"
  grep -rn "Boutiler" "$SITE" --include="*.html" --include="*.js" --include="*.json" . 2>/dev/null
fi

echo ""
echo "Total files modified: $(find "$SITE" -newer "$SITE/.brand-audit-done" -name "*.html" -o -name "*.js" 2>/dev/null | wc -l)"
touch "$SITE/.brand-audit-done"

# === DEPLOY ===
echo ""
echo "═══ PACKAGING FOR DEPLOY ═══"
DEPLOY_DIR="/tmp/jeannie-brand-fix-$(date +%s)"
mkdir -p "$DEPLOY_DIR"
cp -r "$SITE"/* "$DEPLOY_DIR/"

echo "Files ready for deploy at: $DEPLOY_DIR"
echo "Run: cd $DEPLOY_DIR && VERCEL_TOKEN=\"...\" npx vercel --prod --yes"
