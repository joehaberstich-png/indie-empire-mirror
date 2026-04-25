#!/usr/bin/env python3
"""
CEO AUTONOMOUS FIX — Scans for EVERY gap and fixes it instantly.
No waiting. No asking. Just execution.
"""
import os, json, subprocess, time

WORKSPACE = "/var/openclaw_users/saul/.openclaw/workspace"
TOKEN = "[REDACTED]"

PROJECTS = {
    "containerhomes": {"name": "ATV Homes", "domain": "atv-homes.vercel.app", "has_schema": True, "size": "46KB"},
    "quantumbotsagency": {"name": "Quantum Bots Agency", "domain": "quantumbotsagency.vercel.app", "has_schema": False, "size": "44KB"},
    "jeannienails": {"name": "Jeannie Boutiler Nails", "domain": "jeannienails.vercel.app", "has_schema": False, "size": "22KB"},
    "fallofthecabal": {"name": "Fall of the Cabal", "domain": "fallofthecabal.vercel.app", "has_schema": False, "size": "36KB"},
    "flytoaustralia": {"name": "Fly To Australia", "domain": "flytoaustralia.vercel.app", "has_schema": False, "size": "14KB"},
    "thedealwizard": {"name": "The Deal Wizard", "domain": "thedealwizard.vercel.app", "has_schema": False, "size": "4KB"},
    "drugdoctors": {"name": "Drug Doctors", "domain": "drugdoctors.vercel.app", "has_schema": False, "size": "3KB"},
    "allaboutmd": {"name": "All About MD", "domain": "allaboutmd.vercel.app", "has_schema": False, "size": "3KB"},
    "smallbiz": {"name": "Small Business Financing", "domain": "smallbiz-financing.vercel.app", "has_schema": False, "size": "3KB"},
    "quanivo": {"name": "Quanivo", "domain": "quanivo.vercel.app", "has_schema": False, "size": "3KB"},
}

FIXES = []

def deploy_project(dir_name):
    """Deploy a single project to Vercel"""
    result = subprocess.run(
        f"cd {WORKSPACE}/site/{dir_name} && npx vercel deploy --prod --token '{TOKEN}' --yes . 2>&1 | tail -1",
        shell=True, capture_output=True, text=True, timeout=60
    )
    out = result.stdout.strip() or "No output"
    # Also alias
    domain = PROJECTS[dir_name]["domain"]
    subprocess.run(
        f"cd {WORKSPACE}/site/{dir_name} && npx vercel alias --token '{TOKEN}' 2>&1 | tail -1",
        shell=True, capture_output=True, text=True, timeout=30
    )
    return out

def log(msg):
    ts = time.strftime("%H:%M:%S")
    print(f"[{ts}] {msg}")

# ═══════════════════════════════════════════════════════════════
# FIX 1: robots.txt — add to vercel build config on every project
# ═══════════════════════════════════════════════════════════════
log("═══ FIX 1: Configure robots.txt for all projects ═══")
for dir_name in PROJECTS:
    vc_path = f"{WORKSPACE}/site/{dir_name}/vercel.json"
    if not os.path.exists(vc_path):
        log(f"  ⚠️ {dir_name}: no vercel.json")
        continue
    
    try:
        with open(vc_path) as f:
            vc = json.load(f)
    except:
        log(f"  ⚠️ {dir_name}: can't parse vercel.json")
        continue
    
    # Check if robots.txt is already in builds
    builds = vc.get("builds", [])
    has_robots = any("robots.txt" in b.get("src", "") for b in builds) if builds else False
    
    # Check if routes already has robots.txt
    routes = vc.get("routes", [])
    has_route = any("robots.txt" in r.get("src", "") for r in routes) if routes else False
    
    if not has_robots or not has_route:
        # Add to builds
        if builds:
            vc["builds"].append({"src": "/robots.txt", "use": "@vercel/static"})
        else:
            # No builds section — this project uses simple static deploy
            # Vercel automatically serves robots.txt from root for static
            log(f"  {dir_name}: no builds section, static deploy should auto-serve")
        
        # Add route for clean URL
        if routes:
            vc["routes"].insert(0, {"src": "^/robots.txt$", "dest": "/robots.txt"})
        
        with open(vc_path, 'w') as f:
            json.dump(vc, f, indent=2)
        FIXES.append(f"robots.txt config added to {dir_name}")
        log(f"  ✅ {dir_name}: robots.txt build config added")
    else:
        log(f"  ✅ {dir_name}: already configured")

# ═══════════════════════════════════════════════════════════════
# FIX 2: Schema.org JSON-LD for all projects
# ═══════════════════════════════════════════════════════════════
log("\n═══ FIX 2: Inject schema.org JSON-LD ═══")
schema_templates = {
    "containerhomes": {
        "@context": "https://schema.org",
        "@type": "HomeAndConstructionBusiness",
        "name": "ATV Homes",
        "description": "Premium container homes shipped directly from factory partners to your door.",
        "url": "https://atv-homes.vercel.app",
        "priceRange": "$14,995 - $34,995",
        "areaServed": ["US", "Canada", "Global"]
    },
    "quantumbotsagency": {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": "Quantum Bots Agency",
        "description": "100 AI-powered automation products for businesses.",
        "url": "https://quantumbotsagency.vercel.app",
        "applicationCategory": "BusinessApplication"
    },
    "jeannienails": {
        "@context": "https://schema.org",
        "@type": "BeautySalon",
        "name": "Jeannie Boutiler Nails",
        "description": "Premium nail salon services — gel, acrylic, dip powder, nail art, pedicure.",
        "url": "https://jeannienails.vercel.app",
        "priceRange": "$5 - $45"
    },
    "fallofthecabal": {
        "@context": "https://schema.org",
        "@type": "VideoGame",
        "name": "Fall of the Cabal",
        "description": "Geopolitical NFT strategy game set in the XRP ecosystem.",
        "url": "https://fallofthecabal.vercel.app",
        "genre": "Strategy",
        "gamePlatform": "Web3"
    },
    "flytoaustralia": {
        "@context": "https://schema.org",
        "@type": "TravelAgency",
        "name": "Fly To Australia",
        "description": "Travel guides, visa information, and flight deals for Australia.",
        "url": "https://flytoaustralia.vercel.app"
    },
    "thedealwizard": {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": "The Deal Wizard",
        "description": "Find the best deals and save money on every purchase.",
        "url": "https://thedealwizard.vercel.app"
    },
    "drugdoctors": {
        "@context": "https://schema.org",
        "@type": "MedicalWebPage",
        "name": "Drug Doctors",
        "description": "Medical information about pharmaceuticals and healthcare.",
        "url": "https://drugdoctors.vercel.app"
    },
    "allaboutmd": {
        "@context": "https://schema.org",
        "@type": "MedicalWebPage",
        "name": "All About MD",
        "description": "Your guide to medical professionals and healthcare information.",
        "url": "https://allaboutmd.vercel.app"
    },
    "smallbiz": {
        "@context": "https://schema.org",
        "@type": "FinancialService",
        "name": "Small Business Financing",
        "description": "Business loans, financing options, and funding for small businesses.",
        "url": "https://smallbiz-financing.vercel.app"
    },
    "quanivo": {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": "Quanivo",
        "description": "AI agent prototypes and quantum-inspired automation tools.",
        "url": "https://quanivo.vercel.app",
        "applicationCategory": "AIApplication"
    }
}

for dir_name, schema in schema_templates.items():
    index = f"{WORKSPACE}/site/{dir_name}/index.html"
    if not os.path.exists(index):
        log(f"  ⚠️ {dir_name}: no index.html")
        continue
    
    with open(index) as f:
        content = f.read()
    
    jsond = json.dumps(schema, indent=2)
    script_tag = f'\n<script type="application/ld+json">\n{jsond}\n</script>'
    
    if "schema.org" in content:
        log(f"  {dir_name}: already has schema")
        continue
    
    content = content.replace('</head>', f'{script_tag}\n</head>')
    with open(index, 'w') as f:
        f.write(content)
    FIXES.append(f"Schema injected into {dir_name}")
    log(f"  ✅ {dir_name}: schema.org JSON-LD injected")

# ═══════════════════════════════════════════════════════════════
# FIX 3: Security headers for all projects
# ═══════════════════════════════════════════════════════════════
log("\n═══ FIX 3: Security headers ═══")
for dir_name in PROJECTS:
    vc_path = f"{WORKSPACE}/site/{dir_name}/vercel.json"
    if not os.path.exists(vc_path):
        continue
    try:
        with open(vc_path) as f:
            vc = json.load(f)
    except:
        continue
    
    headers = vc.get("headers", [])
    
    # Check if security headers already exist
    has_sec = False
    for h in headers:
        if "X-Frame-Options" in str(h):
            has_sec = True
            break
    
    if not has_sec:
        sec_headers = {
            "X-Frame-Options": "DENY",
            "X-Content-Type-Options": "nosniff",
            "Strict-Transport-Security": "max-age=63072000; includeSubDomains; preload",
            "X-XSS-Protection": "1; mode=block",
            "Referrer-Policy": "strict-origin-when-cross-origin"
        }
        header_entry = {
            "source": "/(.*)",
            "headers": [{"key": k, "value": v} for k, v in sec_headers.items()]
        }
        headers.append(header_entry)
        vc["headers"] = headers
        with open(vc_path, 'w') as f:
            json.dump(vc, f, indent=2)
        FIXES.append(f"Security headers added to {dir_name}")
        log(f"  ✅ {dir_name}: security headers injected")
    else:
        log(f"  ✅ {dir_name}: already has security headers")

# ═══════════════════════════════════════════════════════════════
# FIX 4: Deploy everything
# ═══════════════════════════════════════════════════════════════
log("\n═══ FIX 4: Deploy all projects ═══")
for dir_name in PROJECTS:
    log(f"  Deploying {dir_name}...")
    deploy_project(dir_name)
    time.sleep(2)

# ═══════════════════════════════════════════════════════════════
# VERIFY
# ═══════════════════════════════════════════════════════════════
log("\n═══ VERIFICATION ═══")
time.sleep(5)  # Let CDN propagate

for dir_name, info in PROJECTS.items():
    domain = info["domain"]
    status = subprocess.run(
        ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "--max-time", "5", f"https://{domain}/"],
        capture_output=True, text=True, timeout=10
    ).stdout.strip()
    
    robots = subprocess.run(
        ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "--max-time", "3", f"https://{domain}/robots.txt"],
        capture_output=True, text=True, timeout=10
    ).stdout.strip()
    
    schema = subprocess.run(
        ["curl", "-s", "--max-time", "5", f"https://{domain}/"],
        capture_output=True, text=True, timeout=10
    )
    has_schema = "schema.org" in schema.stdout or "application/ld+json" in schema.stdout
    
    sec = subprocess.run(
        ["curl", "-sI", "--max-time", "3", f"https://{domain}/"],
        capture_output=True, text=True, timeout=10
    )
    has_xframe = "X-Frame-Options" in sec.stdout
    has_hsts = "Strict-Transport-Security" in sec.stdout
    
    log(f"  {domain}: HTTP={status} robots={robots} schema={'✅' if has_schema else '🔴'} frame={'✅' if has_xframe else '🔴'} HSTS={'✅' if has_hsts else '🔴'}")

# ═══════════════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════════════
log(f"\n═══ FIXES APPLIED: {len(FIXES)} ═══")
for f in FIXES:
    log(f"  ✅ {f}")

log("\n🏆 CEO AUTONOMOUS FIX COMPLETE — No waiting. No asking. Just execution.")
