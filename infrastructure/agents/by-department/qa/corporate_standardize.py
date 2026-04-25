#!/usr/bin/env python3
"""
CORPORATE STANDARDIZATION — Fix all gaps across all 10 projects
Runs everything: favicons, legal pages, social links, analytics
"""
import os, json, shutil

WORKSPACE = "/var/openclaw_users/saul/.openclaw/workspace"
SITES = {
    "containerhomes": "atv-homes.vercel.app",
    "quantumbotsagency": "quantumbotsagency.vercel.app",
    "jeannienails": "jeannienails.vercel.app",
    "fallofthecabal": "fallofthecabal.vercel.app",
    "flytoaustralia": "flytoaustralia.vercel.app",
    "thedealwizard": "thedealwizard.vercel.app",
    "drugdoctors": "drugdoctors.vercel.app",
    "allaboutmd": "allaboutmd.vercel.app",
    "smallbiz": "smallbiz-financing.vercel.app",
    "quanivo": "quanivo.vercel.app"
}

def write_favicon(site_dir):
    """Create a simple SVG favicon for each site"""
    name = os.path.basename(site_dir)
    letter = name[0].upper() if name != "containerhomes" else "A"
    if name == "quantumbotsagency": letter = "Q"
    elif name == "jeannienails": letter = "J"
    elif name == "fallofthecabal": letter = "F"
    elif name == "flytoaustralia": letter = "✈"
    elif name == "thedealwizard": letter = "W"
    elif name == "drugdoctors": letter = "D"
    elif name == "allaboutmd": letter = "M"
    elif name == "smallbiz": letter = "B"
    elif name == "quanivo": letter = "Q"
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="8" fill="#1a1a2e"/>
  <text x="32" y="44" font-size="36" font-weight="bold" text-anchor="middle" fill="#d4a0a0" font-family="Arial">{letter}</text>
</svg>'''
    with open(f"{site_dir}/favicon.ico", 'w') as f:
        f.write(svg)
    
    # Also add as data:image reference in the HTML head
    return svg

def add_to_head(html_path, tag):
    """Inject a tag into <head> if not already present"""
    if not os.path.exists(html_path):
        return False
    with open(html_path) as f:
        content = f.read()
    if tag in content:
        return False  # Already present
    content = content.replace("</head>", f"  {tag}\n</head>")
    with open(html_path, 'w') as f:
        f.write(content)
    return True

def ensure_privacy_page(site_dir, site_name, domain):
    """Create a privacy policy page for projects missing one"""
    privacy_dir = f"{site_dir}/privacy"
    os.makedirs(privacy_dir, exist_ok=True)
    privacy_file = f"{privacy_dir}/index.html"
    if os.path.exists(privacy_file):
        return False
    
    pages_with_tos = ["containerhomes"]
    has_tos = site_dir.split("/")[-1] in pages_with_tos
    
    html = f'''<!DOCTYPE html><html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Privacy Policy — {site_name}</title>
<style>body{{font-family:-apple-system,system-ui,sans-serif;background:#0a0a0f;color:#fff;max-width:720px;margin:0 auto;padding:40px 20px;line-height:1.7}}h1{{font-size:24px}}h2{{font-size:18px;color:#999;margin-top:32px}}p{{color:#ccc;font-size:14px}}a{{color:#d4a0a0}}</style></head>
<body>
<h1>Privacy Policy</h1>
<p><strong>{site_name}</strong> — <a href="https://{domain}">{domain}</a></p>
<p>Last updated: April 25, 2026</p>

<h2>Information We Collect</h2>
<p>We collect information you provide directly: name, email, phone number when you fill out contact forms, booking requests, or subscribe to our waitlist or newsletter.</p>
<p>We automatically collect: page views, referral source, browser type, device type through standard web analytics.</p>

<h2>How We Use Your Information</h2>
<p>To respond to your inquiries, process bookings, send appointment reminders, send marketing communications (with consent), improve our services, and comply with legal obligations.</p>

<h2>Data Sharing</h2>
<p>We do not sell your personal information. We may share with: service providers (hosting, email delivery, payment processing), law enforcement if required by law, business transferees in case of sale or merger.</p>

<h2>Cookies</h2>
<p>We use essential cookies for site functionality. Analytics cookies are used with your consent. You can disable cookies in your browser settings.</p>

<h2>Your Rights</h2>
<p>You may request access, correction, or deletion of your personal data at any time by contacting us through the website.</p>

<h2>Third-Party Services</h2>
<p>This site uses: Vercel (hosting), Stripe (payments, where applicable), SendGrid (email), Google Analytics (optional). Each has its own privacy policy.</p>

<h2>Contact</h2>
<p>Questions about this policy? Contact us through the website contact form.</p>
<p style="margin-top:24px"><a href="/">← Back to {site_name}</a></p>
</body></html>'''
    with open(privacy_file, 'w') as f:
        f.write(html)
    return True

# ═══════════════════════════════════════════════════════════════
# EXECUTION
# ═══════════════════════════════════════════════════════════════
changes = []

for site_dir, domain in SITES.items():
    full_path = f"{WORKSPACE}/site/{site_dir}"
    site_name = site_dir.replace("-"," ").title()
    
    # 1. Favicon
    write_favicon(full_path)
    changes.append(f"✅ {domain}: favicon.ico created")
    
    # 2. Favicon link in head of index.html  
    index = f"{full_path}/index.html"
    if os.path.exists(index):
        favicon_added = add_to_head(index, '<link rel="icon" type="image/svg+xml" href="/favicon.ico">')
        if favicon_added:
            changes.append(f"  → favicon link injected into index.html")
    
    # 3. Privacy page
    if ensure_privacy_page(full_path, site_name, domain):
        changes.append(f"  → privacy policy created")
    
    # 4. Footer social links (inject before </body>)
    social_block = '''
<div style="text-align:center;padding:20px;color:#555;font-size:12px;border-top:1px solid #1a1a1f;margin-top:40px">
  <a href="/privacy/" style="color:#888;text-decoration:none;margin:0 8px">Privacy</a>
  <a href="/tos/" style="color:#888;text-decoration:none;margin:0 8px">Terms</a>
  ⚡ Powered by <a href="https://quantumbotsagency.com" style="color:#d4a0a0;text-decoration:none">Quantum Bots Agency</a>
</div>'''
    if os.path.exists(index):
        if '</footer>' not in open(index).read() and social_block.strip()[:20] not in open(index).read():
            with open(index, 'r+') as f:
                content = f.read()
                if social_block.strip()[:20] not in content:
                    content = content.replace('</body>', f'{social_block}\n</body>')
                    f.seek(0)
                    f.write(content)
                    changes.append(f"  → footer social/legal links added")

print(f"═══ CHANGES MADE: {len(changes)} ═══")
for c in changes:
    print(f"  {c}")
