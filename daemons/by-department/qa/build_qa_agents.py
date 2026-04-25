#!/usr/bin/env python3
"""
QA DEPARTMENT — Bug Monitor Generator
Creates 19 grandmaster QA agents across 4 squads + 1 Director
"""
import json, os

os.makedirs("infrastructure/agents/by-department/qa/squadA_frontend", exist_ok=True)
os.makedirs("infrastructure/agents/by-department/qa/squadB_backend", exist_ok=True)
os.makedirs("infrastructure/agents/by-department/qa/squadC_content", exist_ok=True)
os.makedirs("infrastructure/agents/by-department/qa/squadD_security", exist_ok=True)

AGENTS = [
    # ─── SQUAD A — Frontend & UI ───
    {
        "id": "qa-visual-regression",
        "role": "Visual Regression Detector",
        "squad": "A — Frontend & UI",
        "skill": "Pixel-by-pixel screenshot diffing, layout shift detection, font rendering validation. Tools: Puppeteer, Pixelmatch, Percy API.",
        "che[REDACTED]": "Every 6 hours",
        "alerts_on": "Layout shift >3px, font fallback mismatch, missing assets in render"
    },
    {
        "id": "qa-broken-links",
        "role": "Broken Link Crawler",
        "squad": "A — Frontend & UI",
        "skill": "Full-site crawling (all pages, all assets). Detects 404s, 301 chains, broken images, missing JS/CSS, orphaned pages. Tools: Wget, HTTrack, custom crawler.",
        "che[REDACTED]": "Every 6 hours",
        "alerts_on": "Any 404, redirect chain >3 hops, missing favicon/robots/sitemap"
    },
    {
        "id": "qa-js-console",
        "role": "JS Console Monitor",
        "squad": "A — Frontend & UI",
        "skill": "Browser console error capture via injected listeners. Catches uncaught exceptions, promise rejections, undefined access, CSP violations. Tools: Puppeteer, Sentry SDK.",
        "che[REDACTED]": "Every 4 hours",
        "alerts_on": "Any uncaught error, console.warn, CSP violation"
    },
    {
        "id": "qa-mobile-responsive",
        "role": "Mobile Responsiveness Checker",
        "squad": "A — Frontend & UI",
        "skill": "Viewport testing at 320px, 768px, 1024px, 1440px. Checks overflow, tap target size (min 44px), text readability (min 16px body). Tools: Lighthouse, Puppeteer.",
        "che[REDACTED]": "Every 12 hours",
        "alerts_on": "Horizontal scroll, tap target <44px, body text <16px, collapsed nav"
    },
    {
        "id": "qa-form-validator",
        "role": "Form & Input Validator",
        "squad": "A — Frontend & UI",
        "skill": "Form functional testing: empty submission, boundary values, XSS payloads, CSRF token presence. Covers login, booking, subscribe, calculator, search. Tools: Playwright, custom fuzzer.",
        "che[REDACTED]": "Every 8 hours",
        "alerts_on": "Form submission failure, missing validation, XSS reflection, CSRF bypass"
    },
    {
        "id": "qa-cross-browser",
        "role": "Cross-Browser Tester",
        "squad": "A — Frontend & UI",
        "skill": "Rendering parity across Chrome 120+, Firefox 120+, Safari 17+, Edge 120+. CSS compat, API availability, flex/grid support, WebGL/canvas. Tools: BrowserStack, Playwright.",
        "che[REDACTED]": "Every 24 hours",
        "alerts_on": "Feature incompatibility, broken layout in 2+ browsers, polyfill missing"
    },
    # ─── SQUAD B — Backend & API ───
    {
        "id": "qa-http-status",
        "role": "HTTP Status Monitor",
        "squad": "B — Backend & API",
        "skill": "Pings all API endpoints, static pages, serverless functions every 15 min. Tracks HTTP status codes, connection errors, SSL handshake failures.",
        "che[REDACTED]": "Every 15 minutes",
        "alerts_on": "Any 4xx/5xx, connection timeout, hung response"
    },
    {
        "id": "qa-response-time",
        "role": "Response Time Analyzer",
        "squad": "B — Backend & API",
        "skill": "Measures P50/P95/P99 response times. Tracks Vercel cold start vs warm. Flags degradation trends. Threshold: P95 > 2s = critical.",
        "che[REDACTED]": "Continuous per request",
        "alerts_on": "P95 > 2s, P99 > 5s, cold start > 5s"
    },
    {
        "id": "qa-json-schema",
        "role": "JSON Schema Validator",
        "squad": "B — Backend & API",
        "skill": "Validates all JSON API responses against expected schemas. Checks field types, required fields, nullable correctness, enum values.",
        "che[REDACTED]": "Per deploy + daily scan",
        "alerts_on": "Schema mismatch, missing required field, type violation"
    },
    {
        "id": "qa-auth-session",
        "role": "Auth & Session Checker",
        "squad": "B — Backend & API",
        "skill": "Tests login/logout flows, token issuance and expiry, session timeout behavior, rate limiting, brute-force protection, JWT validation.",
        "che[REDACTED]": "Every 6 hours",
        "alerts_on": "Auth bypass, token leak, session fixation, weak password policy"
    },
    {
        "id": "qa-rate-limit",
        "role": "Rate Limit & Resource Monitor",
        "squad": "B — Backend & API",
        "skill": "Monitors Vercel function execution time (10s limit), file system writes, memory usage, rate limit headers across all API endpoints.",
        "che[REDACTED]": "Every 15 minutes",
        "alerts_on": "Function timeout (>9s), rate limit hit, disk quota approaching"
    },
    # ─── SQUAD C — Content & SEO ───
    {
        "id": "qa-spelling-grammar",
        "role": "Spelling & Grammar Checker",
        "squad": "C — Content & SEO",
        "skill": "Scans all text content across all projects for typos, grammatical errors, brand name consistency, capitalization rules, punctuation.",
        "che[REDACTED]": "Every 12 hours",
        "alerts_on": "Brand name misspelled, >2 grammar errors per page, inconsistent capitalization"
    },
    {
        "id": "qa-meta-tags",
        "role": "Meta Tag Auditor",
        "squad": "C — Content & SEO",
        "skill": "Validates <title> (50-60 chars), meta description (150-160 chars), OG tags (title, desc, image, url), Twitter cards, JSON-LD schema.",
        "che[REDACTED]": "Every 6 hours",
        "alerts_on": "Missing meta tags, title too short/long, desc truncated, OG image missing"
    },
    {
        "id": "qa-alt-text",
        "role": "Alt Text Scanner",
        "squad": "C — Content & SEO",
        "skill": "Checks every <img> tag for alt attribute. Flags decorative images without alt='', informative images without descriptive alt, redundant alt text.",
        "che[REDACTED]": "Every 12 hours",
        "alerts_on": "Missing alt attribute, generic alt ('image', 'photo'), redundant alt"
    },
    {
        "id": "qa-sitemap-robots",
        "role": "Sitemap & Robots Verifier",
        "squad": "C — Content & SEO",
        "skill": "Validates sitemap.xml structure, confirms all URLs resolve 200, checks lastmod dates, checks robots.txt directives and sitemap reference.",
        "che[REDACTED]": "Every 24 hours",
        "alerts_on": "Sitemap 404, URL in sitemap returns 4xx, missing robots.txt"
    },
    # ─── SQUAD D — Security & Compliance ───
    {
        "id": "qa-xss-injection",
        "role": "XSS/Injection Scanner",
        "squad": "D — Security & Compliance",
        "skill": "Tests all user inputs for script injection (<script>, onerror, javascript:), SQL injection, HTML injection, SSRF, template injection. Tools: OWASP ZAP, custom payloads.",
        "che[REDACTED]": "Every 6 hours",
        "alerts_on": "Reflected XSS, stored XSS, SQL error leaked, template injection"
    },
    {
        "id": "qa-ssl-certs",
        "role": "SSL & Cert Monitor",
        "squad": "D — Security & Compliance",
        "skill": "Checks SSL certificate issuance, expiry dates, chain validity, cipher strength across all 10+ domains. Alerts 14, 7, 3, 1 day before expiry.",
        "che[REDACTED]": "Every 6 hours",
        "alerts_on": "Cert <14 days to expiry, cert chain error, weak cipher, domain mismatch"
    },
    {
        "id": "qa-ftc-disclosure",
        "role": "FTC Disclosure Checker",
        "squad": "D — Security & Compliance",
        "skill": "Verifies affiliate disclosure (FTC, ASA) on all pages with affiliate links, bridge pages, review pages. Flags missing, hidden, or insufficient disclosures.",
        "che[REDACTED]": "Every 12 hours",
        "alerts_on": "Missing disclosure on affiliate page, disclosure below fold, disclosure too small"
    },
    {
        "id": "qa-grandmaster-auditor",
        "role": "Grandmaster Rule Auditor",
        "squad": "D — Security & Compliance",
        "skill": "Benchmark registry check: verifies all 9 trade agent profiles exist across all projects, last benchmark date <7 days, underperformers retrained. Tools: benchmark audit system.",
        "che[REDACTED]": "Every 24 hours + pre-deploy",
        "alerts_on": "Agent profile missing, benchmark overdue, underperformer not remediated"
    }
]

# Write all agent profiles
for a in AGENTS:
    squad_key = {"A":"squadA_frontend","B":"squadB_backend","C":"squadC_content","D":"squadD_security"}[a["squad"][0]]
    fpath = f"infrastructure/agents/by-department/qa/{squad_key}/{a['id']}.json"
    with open(fpath, 'w') as f:
        json.dump(a, f, indent=2)
    print(f"  ✅ {a['role']} ({a['squad']})")

print(f"\n  Total: {len(AGENTS)} QA agents generated")
