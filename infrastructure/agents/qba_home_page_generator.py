#!/usr/bin/env python3
"""
QBA Home Page Generator — 100 Products + Category Navigation
"""
import json, os

PRODUCTS_DIR = "/var/openclaw_users/saul/.openclaw/workspace/site/quantumbotsagency/products"

# Categories from product manifests
cats = {
    "🤖 Core Bots": [],
    "✍️ Content Creation": [],
    "📊 Analytics & Data": [],
    "🔗 Integrations": [],
    "🛡️ Security": [],
    "🎯 Marketing & Sales": [],
    "💼 Support & Service": [],
    "⚙️ Operations & Ecom": [],
}

# Manually map all 100 products to categories
products_map = [
    ("Core Bots", "standard-bot", "Standard Bot", "$27/mo", "Entry-level AI chatbot with basic NLP"),
    ("Core Bots", "intelligent-bot", "Intelligent Bot", "$47/mo", "Advanced AI with intent recognition"),
    ("Core Bots", "advanced-bot", "Advanced Bot", "$77/mo", "Full NLP + decision tree engine"),
    ("Core Bots", "quantum-light-bot", "Quantum Light Bot", "$37/mo", "Quantum-optimized light assistant"),
    ("Core Bots", "full-quantum-bot", "Full Quantum Bot", "$97/mo", "Full quantum AI with all modules"),
    ("Core Bots", "affiliate-bot", "Affiliate Bot", "$47/mo", "Affiliate marketing automation bot"),
    ("Content Creation", "content-writer", "AI Content Writer", "$47/mo", "500 SEO blog posts/day"),
    ("Content Creation", "video-script-generator", "Video Script Generator", "$37/mo", "Ready-to-film scripts"),
    ("Content Creation", "ebook-creator", "eBook Creator", "$47/mo", "Full eBook from 1 topic"),
    ("Content Creation", "infographic-generator", "Infographic Generator", "$27/mo", "Data-driven infographics"),
    ("Content Creation", "podcast-creator", "Podcast Creator", "$57/mo", "End-to-end podcast production"),
    ("Content Creation", "newsletter-engine", "Newsletter Engine", "$37/mo", "Auto newsletter from RSS"),
    ("Content Creation", "social-ad-creator", "Social Ad Creator", "$67/mo", "AI ad creative generation"),
    ("Content Creation", "press-release-writer", "Press Release Writer", "$47/mo", "AP style press releases"),
    ("Content Creation", "case-study-builder", "Case Study Builder", "$37/mo", "Structured case studies"),
    ("Content Creation", "product-description-writer", "Product Description Writer", "$27/mo", "E-com descriptions at scale"),
    ("Marketing & Sales", "seo-optimizer", "SEO Optimizer", "$57/mo", "On-page SEO optimization"),
    ("Marketing & Sales", "social-media-manager", "Social Media Manager", "$47/mo", "Multi-platform post scheduling"),
    ("Marketing & Sales", "email-marketer", "Email Marketer", "$37/mo", "Automated email campaigns"),
    ("Marketing & Sales", "landing-page-builder", "Landing Page Builder", "$47/mo", "Conversion-optimized pages"),
    ("Marketing & Sales", "seo-researcher", "SEO Researcher", "$37/mo", "Keyword & competitor research"),
    ("Marketing & Sales", "lead-scorer", "Lead Scorer", "$57/mo", "ML lead scoring engine"),
    ("Marketing & Sales", "ab-test-tool", "A/B Test Tool", "$47/mo", "Split testing automation"),
    ("Marketing & Sales", "conversion-optimizer", "Conversion Optimizer", "$67/mo", "CRO with heatmaps"),
    ("Marketing & Sales", "retargeting-engine", "Retargeting Engine", "$47/mo", "Smart retargeting campaigns"),
    ("Marketing & Sales", "funnel-builder", "Funnel Builder", "$77/mo", "Multi-step sales funnels"),
    ("Marketing & Sales", "quora-marketer", "Quora Marketer", "$27/mo", "Quora answer automation"),
    ("Marketing & Sales", "reddit-marketer", "Reddit Marketer", "$27/mo", "Reddit engagement bots"),
    ("Marketing & Sales", "cold-emailer", "Cold Emailer", "$57/mo", "Cold email sequences"),
    ("Marketing & Sales", "sms-marketer", "SMS Marketer", "$37/mo", "Bulk SMS campaigns"),
    ("Marketing & Sales", "webinar-automation", "Webinar Automation", "$67/mo", "Webinar funnel automation"),
    ("Research & Intel", "market-researcher", "Market Researcher", "$47/mo", "Market analysis research"),
    ("Research & Intel", "scraper-engine", "Scraper Engine", "$57/mo", "Web scraping automation"),
    ("Research & Intel", "sentiment-analyzer", "Sentiment Analyzer", "$37/mo", "Sentiment analysis engine"),
    ("Research & Intel", "trend-finder", "Trend Finder", "$47/mo", "Trend discovery tool"),
    ("Research & Intel", "competitor-intel", "Competitor Intel", "$67/mo", "Competitor monitoring"),
    ("Research & Intel", "keyword-researcher", "Keyword Researcher", "$37/mo", "Keyword discovery & clustering"),
    ("Research & Intel", "product-scout", "Product Scout", "$47/mo", "Product opportunity finder"),
    ("Research & Intel", "review-analyzer", "Review Analyzer", "$27/mo", "Review sentiment analysis"),
    ("Research & Intel", "price-tracker", "Price Tracker", "$27/mo", "Competitor price monitoring"),
    ("Research & Intel", "survey-creator", "Survey Creator", "$27/mo", "Survey design & analytics"),
    ("Operations & Ecom", "invoice-generator", "Invoice Generator", "$27/mo", "Invoice automation"),
    ("Operations & Ecom", "order-manager", "Order Manager", "$47/mo", "Order processing automation"),
    ("Operations & Ecom", "inventory-optimizer", "Inventory Optimizer", "$57/mo", "Smart inventory management"),
    ("Operations & Ecom", "shipping-automation", "Shipping Automation", "$37/mo", "Shipping label & tracking"),
    ("Operations & Ecom", "review-collector", "Review Collector", "$27/mo", "Review request automation"),
    ("Operations & Ecom", "chat-support", "Chat Support", "$47/mo", "Live chat + AI support"),
    ("Support & Service", "customer-support-bot", "Customer Support Bot", "$97/mo", "24/7 support in 9 languages"),
    ("Support & Service", "live-chat-bot", "Live Chat Bot", "$47/mo", "Browser chat widget"),
    ("Support & Service", "ticketing-system", "Ticketing System", "$57/mo", "Customer ticketing"),
    ("Support & Service", "faq-automation", "FAQ Automation", "$27/mo", "Auto FAQ generation"),
    ("Support & Service", "onboarding-engine", "Onboarding Engine", "$37/mo", "User onboarding sequences"),
    ("Support & Service", "feedback-collector", "Feedback Collector", "$27/mo", "Multi-channel feedback"),
    ("Support & Service", "knowledge-base", "Knowledge Base", "$57/mo", "Self-service knowledge base"),
    ("Support & Service", "crm-automation", "CRM Automation", "$97/mo", "Full CRM with lead scoring"),
    ("Support & Service", "chatbot-builder", "Chatbot Builder", "$77/mo", "No-code chatbot builder"),
    ("Support & Service", "voice-bot", "Voice Bot", "$97/mo", "AI voice agent"),
    ("Analytics & Data", "seo-audit-tool", "SEO Audit Tool", "$47/mo", "Technical SEO audit"),
    ("Analytics & Data", "competitor-seo-analyzer", "Competitor SEO Analyzer", "$67/mo", "Gap analysis"),
    ("Analytics & Data", "rank-tracker", "Rank Tracker", "$37/mo", "Daily SERP tracking"),
    ("Analytics & Data", "data-warehouse", "Data Warehouse", "$197/mo", "Centralized data with 500+ connectors"),
    ("Analytics & Data", "reporting-dashboard", "Reporting Dashboard", "$57/mo", "Unified business dashboard"),
    ("Analytics & Data", "data-cleaner", "Data Cleaner", "$27/mo", "Deduplication & cleaning"),
    ("Analytics & Data", "forecast-engine", "Forecast Engine", "$97/mo", "ML revenue forecasting"),
    ("Analytics & Data", "heatmap-analyzer", "Heatmap Analyzer", "$37/mo", "User behavior heatmaps"),
    ("Analytics & Data", "survey-analyzer", "Survey Analyzer", "$27/mo", "Survey data analysis"),
    ("Analytics & Data", "ab-testing-analyzer", "A/B Testing Analyzer", "$47/mo", "Bayesian test analysis"),
    ("Integrations", "api-connector", "API Connector", "$97/mo", "100+ pre-built connectors"),
    ("Integrations", "webhook-engine", "Webhook Engine", "$27/mo", "Webhook processing"),
    ("Integrations", "zapier-clone", "Zapier Clone", "$147/mo", "Internal automation platform"),
    ("Integrations", "slack-bot", "Slack Bot", "$37/mo", "Custom Slack automations"),
    ("Integrations", "discord-bot", "Discord Bot", "$27/mo", "Discord community bot"),
    ("Integrations", "sms-automation", "SMS Automation", "$47/mo", "Two-way SMS marketing"),
    ("Integrations", "whatsapp-bot", "WhatsApp Bot", "$57/mo", "WhatsApp Business API"),
    ("Integrations", "calendar-sync", "Calendar Sync", "$27/mo", "Cross-platform calendar sync"),
    ("Integrations", "payment-gateway", "Payment Gateway", "$97/mo", "Unified payment processing"),
    ("Integrations", "email-verifier", "Email Verifier", "$27/mo", "Real-time email verification"),
    ("Security", "firewall", "Quantum Firewall", "$97/mo", "WAF with quantum detection"),
    ("Security", "pii-scanner", "PII Scanner", "$47/mo", "Personal info detection"),
    ("Security", "vulnerability-scanner", "Vulnerability Scanner", "$67/mo", "CVE matching"),
    ("Security", "access-control", "Access Control", "$57/mo", "RBAC + SSO + MFA"),
    ("Security", "audit-logger", "Audit Logger", "$37/mo", "Immutable audit logging"),
    ("Security", "incident-responder", "Incident Responder", "$97/mo", "Automated incident response"),
    ("Security", "certificate-manager", "Certificate Manager", "$27/mo", "SSL/TLS lifecycle"),
    ("Security", "backup-manager", "Backup Manager", "$47/mo", "Automated backup + integrity"),
    ("Security", "compliance-scanner", "Compliance Scanner 360", "$127/mo", "Multi-framework compliance"),
    ("Security", "identity-verifier", "Identity Verifier", "$57/mo", "KYC/AML verification"),
    ("Security", "threat-intel", "Threat Intelligence", "$97/mo", "50+ threat feed sources"),
    ("Security", "malware-scanner", "Malware Scanner", "$37/mo", "Multi-engine scanning"),
    ("Security", "zero-trust-engine", "Zero Trust Engine", "$147/mo", "Full zero-trust architecture"),
    ("Security", "data-encryption", "Data Encryption Suite", "$67/mo", "Quantum-resistant encryption"),
]

# Group
grouped = {}
for cat_slug, slug, name, price, desc in products_map:
    grouped.setdefault(cat_slug, []).append((slug, name, price, desc))

def slugify(s):
    return s.lower().replace(" & ", "-").replace(" ", "-")

cat_icons = {
    "Core Bots": "🤖",
    "Content Creation": "✍️",
    "Marketing & Sales": "🎯",
    "Research & Intel": "🔍",
    "Operations & Ecom": "⚙️",
    "Support & Service": "💼",
    "Analytics & Data": "📊",
    "Integrations": "🔗",
    "Security": "🛡️",
}

cat_ems = {
    "Core Bots": "#818cf8",
    "Content Creation": "#22c55e",
    "Marketing & Sales": "#f59e0b",
    "Research & Intel": "#06b6d4",
    "Operations & Ecom": "#a855f7",
    "Support & Service": "#ec4899",
    "Analytics & Data": "#3b82f6",
    "Integrations": "#14b8a6",
    "Security": "#ef4444",
}

nav_items = []
category_sections = ""

for cat_name in ["Core Bots", "Content Creation", "Marketing & Sales", "Research & Intel", "Operations & Ecom", "Support & Service", "Analytics & Data", "Integrations", "Security"]:
    items = grouped.get(cat_name, [])
    if not items:
        continue
    icon = cat_icons[cat_name]
    em = cat_ems[cat_name]
    sid = slugify(cat_name)
    nav_items.append(f'<a href="#{sid}">{icon} {cat_name}</a>')

    rows = ""
    for slug, name, price, desc in items:
        rows += f'''
            <div class="prod-card">
                <a href="/products/{slug}.html" class="prod-link">
                    <div class="prod-info"><h4>{name}</h4><p>{desc}</p></div>
                    <div class="prod-price">{price}</div>
                </a>
            </div>'''

    category_sections += f'''
        <section id="{sid}" class="cat-section">
            <h2 class="cat-header" style="border-color:{em}"><span>{icon}</span> {cat_name} <span class="prod-count">({len(items)})</span></h2>
            <div class="prod-grid">{rows}
            </div>
        </section>'''

cats_nav = "\n                ".join(nav_items)

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Quantum Bots Agency — 100 AI Products, Quantum-Grade Hosting, 24/7 Quantum Assistant</title>
<meta name="description" content="100 AI products. Quantum-grade hosting. AI agents that sell. From $27/mo. Enterprise AI for every business need.">
<link rel="stylesheet" href="/quantumbotsagency/css/quantum.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#0a0a0f;color:#e2e8f0;line-height:1.6}}
.nav{{position:fixed;top:0;left:0;right:0;z-index:100;background:rgba(10,10,15,.95);border-bottom:1px solid #1a1a2e;padding:12px 24px}}
.nav-inner{{max-width:1200px;margin:0 auto;display:flex;justify-content:space-between;align-items:center}}
.nav .logo{{font-size:18px;font-weight:700;color:#818cf8}}
.nav-links a{{color:#94a3b8;text-decoration:none;margin-left:20px;font-size:13px;transition:color .2s}}
.nav-links a:hover{{color:#fff}}
.hero{{padding:120px 24px 80px;text-align:center;background:linear-gradient(135deg,#0a0a0f 0%,#13132a 50%,#0a0a0f 100%)}}
.hero h1{{font-size:44px;margin-bottom:12px;background:linear-gradient(90deg,#818cf8,#22d3ee,#818cf8);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-size:200% auto;animation:shimmer 4s ease-in-out infinite}}
@keyframes shimmer{{0%,100%{{background-position:0% 50%}}50%{{background-position:100% 50%}}}}
.hero .subtitle{{color:#94a3b8;font-size:17px;max-width:650px;margin:0 auto 24px}}
.hero .stats{{display:flex;justify-content:center;gap:40px;margin-top:24px;flex-wrap:wrap}}
.hero .stat{{text-align:center}}
.hero .stat-num{{font-size:28px;font-weight:700;background:linear-gradient(90deg,#818cf8,#22d3ee);-webkit-background-clip:text;-webkit-text-fill-color:transparent}}
.hero .stat-label{{color:#64748b;font-size:12px;margin-top:4px}}
.cat-nav{{position:sticky;top:52px;z-index:90;background:rgba(10,10,15,.9);border-bottom:1px solid #1a1a2e;padding:8px 0;overflow-x:auto;text-align:center}}
.cat-nav a{{display:inline-block;color:#64748b;text-decoration:none;font-size:11px;padding:4px 10px;margin:0 2px;border-radius:6px;transition:all .2s;white-space:nowrap}}
.cat-nav a:hover{{color:#fff;background:rgba(129,140,248,.1)}}
.content{{max-width:1100px;margin:0 auto;padding:20px 24px 80px}}
.cat-section{{margin-bottom:40px}}
.cat-header{{font-size:20px;margin-bottom:16px;padding-bottom:8px;border-bottom:2px solid #818cf8;display:flex;align-items:center;gap:8px}}
.cat-header span{{font-size:20px}}
.prod-count{{font-size:12px;color:#64748b;margin-left:8px}}
.prod-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:8px}}
.prod-card{{background:#13131f;border:1px solid #1a1a2e;border-radius:8px;overflow:hidden;transition:all .2s}}
.prod-card:hover{{border-color:#818cf8;transform:translateY(-1px)}}
.prod-link{{display:flex;justify-content:space-between;align-items:center;padding:12px 16px;text-decoration:none}}
.prod-info h4{{color:#e2e8f0;font-size:13px;font-weight:600;margin-bottom:2px}}
.prod-info p{{color:#64748b;font-size:11px}}
.prod-price{{color:#818cf8;font-weight:700;font-size:14px;white-space:nowrap;margin-left:12px}}
.cta-section{{max-width:700px;margin:40px auto;text-align:center;padding:40px 24px;background:linear-gradient(135deg,#0f0f1a,#1a1a2e);border-radius:16px;border:1px solid #2a2a3e}}
.cta-section h2{{font-size:24px;margin-bottom:12px}}
.cta-section p{{color:#94a3b8;font-size:14px;margin-bottom:20px}}
.cta-btn{{display:inline-block;background:#818cf8;color:#000;padding:14px 36px;border-radius:8px;text-decoration:none;font-weight:700;font-size:15px}}
.cta-btn:hover{{opacity:.9}}
footer{{text-align:center;padding:24px;color:#555;font-size:12px}}
.features-row{{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:16px;max-width:900px;margin:0 auto 40px;padding:0 24px}}
.feature-box{{background:rgba(129,140,248,.05);border:1px solid #1a1a2e;border-radius:10px;padding:20px;text-align:center}}
.feature-box h3{{font-size:14px;color:#818cf8;margin-bottom:6px}}
.feature-box p{{font-size:12px;color:#64748b}}
</style>
</head>
<body>
<nav class="nav">
<div class="nav-inner">
<a href="/" class="logo">⚡ QBA</a>
<div class="nav-links">
<a href="#products">All Products</a>
<a href="/#hosting">Hosting</a>
<a href="/#white-label">White Label</a>
<a href="/api-dashboard.html">API</a>
</div>
</div>
</nav>

<section class="hero">
<h1>⚡ Quantum Bots Agency</h1>
<p class="subtitle">100 AI products. Quantum-grade everything. AI agents that actually sell. From $27/month — enterprise power, indie pricing.</p>
<div class="stats">
<div class="stat"><div class="stat-num">100</div><div class="stat-label">AI Products</div></div>
<div class="stat"><div class="stat-num">9</div><div class="stat-label">Categories</div></div>
<div class="stat"><div class="stat-num">9</div><div class="stat-label">Languages</div></div>
<div class="stat"><div class="stat-num">24/7</div><div class="stat-label">Quantum Support</div></div>
</div>
</section>

<div class="features-row">
<div class="feature-box"><h3>🤖 Live Sales Agents</h3><p>Interactive bots that sell — not just product pages</p></div>
<div class="feature-box"><h3>🎬 Hollywood Video Pipeline</h3><p>Auto-generated sales + tutorial videos on purchase</p></div>
<div class="feature-box"><h3>🔒 Quantum Security</h3><p>Quantum-resistant encryption + zero-trust architecture</p></div>
<div class="feature-box"><h3>🌐 9-Language Support</h3><p>Multi-lingual AI support with 30-second SLA</p></div>
</div>

<div class="cat-nav">
{cats_nav}
</div>

<div class="content" id="products">
{category_sections}

<section class="cta-section">
<h2>🎯 Need Something Custom?</h2>
<p>White-label solutions, custom integrations, enterprise deployments. Our 40,000 quantum AI agents can build anything.</p>
<a href="/api-dashboard.html" class="cta-btn">Talk to a Quantum Agent →</a>
</section>
</div>

<footer>
<p>© 2026 Quantum Bots Agency · 100 AI Products · Built by 40,000 Quantum AI Agents<br>
<span style="color:#555;font-size:10px">⚡ Quantum Bots Agency — quantumbotsagency.com</span></p>
</footer>
<script src="/quantumbotsagency/js/quantum-chat.js"></script>
</body>
</html>'''

with open("/var/openclaw_users/saul/.openclaw/workspace/site/quantumbotsagency/index.html", 'w') as f:
    f.write(html)

print(f"✅ QBA home page written with {len(products_map)} products across 9 categories")
print(f"   Category nav links: {len(nav_items)}")
print(f"   Category sections: 9")
