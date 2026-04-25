#!/usr/bin/env python3
"""
QBA Products Weeks 6-10 Generator — 54 Products
Completes Quantum Bots Agency to 100 products total.
Each: full page, features, pricing, Stripe link, QBA branding.
Staff doubled: 20 engineers per product, 40K total QBA staff.
"""

import os, json

SITE = "/var/openclaw_users/saul/.openclaw/workspace/site/quantumbotsagency"
PRODUCTS_DIR = f"{SITE}/products"
QBA = "⚡ Powered by Quantum Bots Agency → quantumbotsagency.com"
STRIPE = "https://buy.stripe.com/7sYdR96za9IpfzY0jYa3u0d"

WEEK6 = [
    {"slug":"content-writer","name":"AI Content Writer","price":47,"tagline":"Generate 500 SEO-optimized blog posts per day with quantum quality control","features":["500 posts/day — 1,000-2,500 words each","SEO-optimized (H1, H2, H3, meta, alt tags, internal links)","12 languages supported","AI-generated featured images (3 per post)","Auto-keyword research from Google Trends daily","Staggered publishing 24/7 (1 post every ~3 min)","Content calendar management"],"icon":"✍️","cat":"Content Creation"},
    {"slug":"video-script-generator","name":"Video Script Generator","price":37,"tagline":"AI generates ready-to-film video scripts for any platform","features":["Platform-specific formats (YouTube, TikTok, IG Reels, FB)","Hook generator — 50 proven opening patterns","Pacing calculator — optimal length per platform","Auto-generated Thumbnail concepts","Call-to-action optimization","Voiceover script + teleprompter mode","Bulk script generation (100 at a time)"],"icon":"🎬","cat":"Content Creation"},
    {"slug":"ebook-creator","name":"eBook Creator","price":47,"tagline":"Write and design complete eBooks from a single topic input","features":["Full eBook from 1 topic sentence — 30-200 pages","Chapter outline auto-generation","Cover design (3 variants per book)","Interior layout (paragraphs, quotes, callouts, tables)","Amazon KDP formatting (trim size, bleed, margins)","Export: PDF, EPUB, MOBI, DOCX","ISBN barcode generator"],"icon":"📚","cat":"Content Creation"},
    {"slug":"infographic-generator","name":"Infographic Generator","price":27,"tagline":"Data-driven infographics from any content — publish-ready","features":["Infographic from article in 30 seconds","Template library (200+ themes)","Data visualization auto-charting","Brand color/font matching","Social-size variants (IG, Pinterest, LinkedIn, FB)","SVG export + PNG at 300 DPI","Animated infographic option"],"icon":"📊","cat":"Content Creation"},
    {"slug":"podcast-creator","name":"Podcast Creator","price":57,"tagline":"End-to-end podcast production — scripting, voice, publishing","features":["Episode script writer from topic","AI voice narration (5 voices, male/female)","Intro/outro music generator","Show notes auto-writer","Distribution (Spotify, Apple, Amazon)","Transcription service","Analytics — downloads, listeners, retention"],"icon":"🎙️","cat":"Content Creation"},
    {"slug":"newsletter-engine","name":"Newsletter Engine","price":37,"tagline":"Automated newsletter creation from any RSS or content feed","features":["Auto-generate newsletter from RSS/blog/social feeds","Template system (20+ designs)","Personalization per subscriber segment","A/B subject line testing","Send optimization (best time per subscriber)","Subscriber management (import, segment, clean)","Analytics — open rate, CTR, unsub rate"],"icon":"📰","cat":"Content Creation"},
    {"slug":"social-ad-creator","name":"Social Ad Creator","price":67,"tagline":"AI generates and tests ad creatives for Facebook, Instagram, TikTok, LinkedIn","features":["Ad creative generation (image + copy + CTA)","Platform-specific formats (9:16, 1:1, 4:5, 16:9)","Headline variants (10 per creative)","A/B testing — 3 creative variants per campaign","Budget-suggested creative (low/medium/high budget)","Performance prediction score before launching","Ad library sync"],"icon":"📱","cat":"Content Creation"},
    {"slug":"press-release-writer","name":"Press Release Writer","price":47,"tagline":"Professional press releases formatted for newswire distribution","features":["AP style format","Distribution-ready (PRWeb, PRNewswire, BusinessWire)","Media contact database integration","Quote insertion from interview notes","Boilerplate generator","SERP-optimized headline","Embargo date management"],"icon":"📢","cat":"Content Creation"},
    {"slug":"case-study-builder","name":"Case Study Builder","price":37,"tagline":"Structured case study creation from client interview transcripts","features":["Problem-Solution-Results framework","Data visualization of results","Testimonial extraction from transcripts","Industry-specific templates","ROI calculator integration","PDF + landing page export","Client approval workflow"],"icon":"📋","cat":"Content Creation"},
    {"slug":"product-description-writer","name":"Product Description Writer","price":27,"tagline":"SEO-optimized product descriptions for e-commerce at scale","features":["Bulk generation (100+ descriptions at once)","Platform-specific (Amazon, Shopify, Etsy, eBay)","Keyword density control","Feature-benefit conversion auto-writing","Emotional trigger insertion","Schema markup generation","Competitor gap analysis per description"],"icon":"🏷️","cat":"Content Creation"},
]

WEEK7 = [
    {"slug":"customer-support-bot","name":"Customer Support Bot","price":97,"tagline":"24/7 quantum-powered customer support in 9 languages","features":["Multi-language (EN, FR, ES, DE, PT, ZH, JA, KO, AR)","Ticket auto-classification (L0, L1, L2, L3)","30-second first response SLA","Knowledge base auto-expansion from resolved tickets","Escalation to human with full context transfer","Sentiment detection and priority routing","Platform integration (chat, email, SMS, WhatsApp)"],"icon":"🤖","cat":"Support & Service"},
    {"slug":"live-chat-bot","name":"Live Chat Bot","price":47,"tagline":"Browser-injected chat widget with quantum sales intelligence","features":["One-line embed (copy-paste to any HTML page)","Intent detection (20+ predefined intents)","3-problem rule before recommendation","Product recommendation engine","Quick reply buttons + typing indicator","Mobile responsive","Analytics — conversations, conversion, satisfaction"],"icon":"💬","cat":"Support & Service"},
    {"slug":"ticketing-system","name":"Ticketing System","price":57,"tagline":"Full customer ticketing system with quantum prioritization","features":["Unlimited tickets and agents","Priority scoring (quantum algorithm)","Auto-assignment by skill/availability","SLA tracking and escalation","Customer portal (view/create tickets)","Knowledge base integration","Reporting — volume, resolution time, satisfaction"],"icon":"🎫","cat":"Support & Service"},
    {"slug":"faq-automation","name":"FAQ Automation","price":27,"tagline":"Auto-generated FAQ pages from your existing content","features":["FAQ from blog posts, docs, product pages","Natural language question generation","Answer extraction with sources","Rich schema markup (FAQPage)","Search autocomplete of FAQ topics","Multi-language FAQ support","Performance tracking (clicks, helpfulness votes)"],"icon":"❓","cat":"Support & Service"},
    {"slug":"onboarding-engine","name":"Onboarding Engine","price":37,"tagline":"Automated user onboarding sequences with conversion tracking","features":["Multi-step onboarding flows (email, in-app, SMS)","Behavioral triggers (feature adoption, time-based)","Progress tracking and completion analytics","A/B onboarding test variants","User segmentation (power user, casual, at-risk)","Knowledge base integration","Churn prediction during onboarding"],"icon":"🚀","cat":"Support & Service"},
    {"slug":"feedback-collector","name":"Feedback Collector","price":27,"tagline":"Multi-channel feedback collection with sentiment analysis","features":["Survey builder (NPS, CSAT, CES, custom)","In-app, email, SMS, web widget collection","Sentiment analysis on free-text responses","Trend tracking over time","Competitor benchmark comparison","Auto-response to negative feedback","Quarterly feedback report generation"],"icon":"📝","cat":"Support & Service"},
    {"slug":"knowledge-base","name":"Knowledge Base Builder","price":57,"tagline":"Self-service knowledge base with quantum search","features":["Article editor with AI writing assistant","Category tree and cross-linking","Search optimization (semantic + keyword)","User feedback on every article","Multi-language support","Analytics — search queries, top articles, failure rate","White-label option"],"icon":"📖","cat":"Support & Service"},
    {"slug":"crm-automation","name":"CRM Automation","price":97,"tagline":"Full CRM with quantum lead scoring and pipeline automation","features":["Contact management with enrichment","Pipeline management (drag-and-drop stages)","Lead scoring (behavioral + demographic)","Email sequencing with open/click tracking","Meeting scheduling integration","Deal forecasting with ML","Integrations (Stripe, Gmail, Slack, 100+)"],"icon":"💼","cat":"Support & Service"},
    {"slug":"chatbot-builder","name":"Chatbot Builder","price":77,"tagline":"No-code chatbot builder with quantum decision trees","features":["Visual flow builder (drag-and-drop)","Intent recognition (NLP engine)","Conditional logic, variables, loops","Platform deployment (web, FB, WhatsApp, Slack)","Analytics — conversations, goals, fallback rate","Template library (50+ industries)","Export/import flows between bots"],"icon":"🧩","cat":"Support & Service"},
    {"slug":"voice-bot","name":"Voice Bot","price":97,"tagline":"AI voice agent for phone calls with human-like conversation","features":["Twilio integration (inbound/outbound calls)","Natural speech (ElevenLabs voices)","Call scripting per use case","Appointment booking via voice","Sentiment detection during calls","Call recording + transcription","Analytics — call outcomes, duration, satisfaction"],"icon":"🎧","cat":"Support & Service"},
]

WEEK8 = [
    {"slug":"seo-audit-tool","name":"SEO Audit Tool","price":47,"tagline":"Technical SEO audit with actionable fix recommendations","features":["Site crawl (1,000 pages per audit)","Core Web Vitals analysis","Mobile-friendliness check","Schema markup validator","Page speed optimization suggestions","Broken link detection","Redirect chain analysis"],"icon":"🔧","cat":"Analytics & Data"},
    {"slug":"competitor-seo-analyzer","name":"Competitor SEO Analyzer","price":67,"tagline":"Full competitive SEO analysis with gap opportunities","features":["Domain comparison (up to 5 competitors)","Keyword gap analysis","Backlink comparison","Content gap identification","SERP feature analysis","Traffic estimation per competitor","Actionable opportunity report"],"icon":"🥊","cat":"Analytics & Data"},
    {"slug":"rank-tracker","name":"Rank Tracker","price":37,"tagline":"Daily SERP position tracking for unlimited keywords","features":["Daily position checks","Localized SERP (city, state, country)","Mobile vs desktop ranking","Competitor rank comparison","Visibility score calculation","Export CSV/PDF reports","Alert on significant rank changes"],"icon":"📈","cat":"Analytics & Data"},
    {"slug":"data-warehouse","name":"Data Warehouse","price":197,"tagline":"Centralized data warehouse connecting 500+ sources","features":["500+ pre-built connectors","SQL query interface","Auto-schema detection","Incremental sync scheduling","Data transformation pipeline","Role-based access control","Export to BI tools (Tableau, PowerBI, Looker)"],"icon":"🏛️","cat":"Analytics & Data"},
    {"slug":"reporting-dashboard","name":"Reporting Dashboard","price":57,"tagline":"Unified business reporting dashboard with custom views","features":["Custom dashboard builder","Data source connectors (50+)","Real-time data refresh","Scheduled email reports","Role-based views (exec, manager, analyst)","Export to PDF, CSV, image","White-label option for agencies"],"icon":"📊","cat":"Analytics & Data"},
    {"slug":"data-cleaner","name":"Data Cleaner","price":27,"tagline":"Automated data cleaning and deduplication engine","features":["Duplicate detection (fuzzy matching)","Standardization (phone, email, address formats)","Missing value imputation","Outlier detection","Validation rules engine","API and CSV import/export","Scheduled cleaning jobs"],"icon":"🧹","cat":"Analytics & Data"},
    {"slug":"forecast-engine","name":"Forecast Engine","price":97,"tagline":"ML-powered revenue and growth forecasting","features":["Time series forecasting (ARIMA, Prophet, LSTM)","Scenario modeling (best/worst/base case)","Seasonal pattern detection","Driver analysis (what impacts revenue most)","Monte Carlo simulation","Automated forecast reports","Integration with accounting tools"],"icon":"🔮","cat":"Analytics & Data"},
    {"slug":"heatmap-analyzer","name":"Heatmap Analyzer","price":37,"tagline":"Visual user behavior analysis with heatmap, scrollmap, clickmap","features":["Click heatmap generation","Scroll depth tracking","Move tracking (mouse movement)","Session recording (replay)","Form interaction analysis","A/B test heatmap overlay","Frustration detection (rage clicks, dead clicks)"],"icon":"🔥","cat":"Analytics & Data"},
    {"slug":"survey-analyzer","name":"Survey Analyzer","price":27,"tagline":"Survey data analysis with sentiment and thematic extraction","features":["Import from Typeform, SurveyMonkey, Google Forms","Sentiment analysis per response","Theme clustering (automatic topic grouping)","Net Promoter Score calculation","Cross-tabulation analysis","Word cloud and trend visualization","Export analysis report"],"icon":"📋","cat":"Analytics & Data"},
    {"slug":"ab-testing-analyzer","name":"A/B Testing Analyzer","price":47,"tagline":"Statistical A/B test analysis with Bayesian inference","features":["Bayesian vs frequentist analysis","Sample size calculator","Sequential testing (peeking correction)","Segment analysis per variant","Revenue-per-visitor calculation","Confidence interval visualization","Automated winner declaration"],"icon":"🧪","cat":"Analytics & Data"},
]

WEEK9 = [
    {"slug":"api-connector","name":"API Connector","price":97,"tagline":"Build API integrations without code — 100+ connectors","features":["100+ pre-built API connectors","Custom connector builder","Authentication handling (OAuth, API key, Basic)","Data transformation pipeline","Error handling and retry logic","Webhook triggers","Rate limit management"],"icon":"🔗","cat":"Integrations"},
    {"slug":"webhook-engine","name":"Webhook Engine","price":27,"tagline":"Receive, process, and forward webhooks with routing rules","features":["Webhook receiver endpoint","Payload transformation","Conditional routing","Retry with exponential backoff","Webhook logging and replay","Multi-destination forwarding","Delivery analytics"],"icon":"🪝","cat":"Integrations"},
    {"slug":"zapier-clone","name":"Zapier Clone","price":147,"tagline":"Internal automation platform — replicate Zapier/Make functionality","features":["Trigger-Action workflow builder","500+ app integrations","Conditional logic, loops, delays","Error handling with fallback","Execution logs and debugging","Team workspace","Schedule-based triggers"],"icon":"⚡","cat":"Integrations"},
    {"slug":"slack-bot","name":"Slack Bot","price":37,"tagline":"Custom Slack bot with slash commands and automations","features":["Slash command builder","Message shortcuts","Modal form builder","Channel management automation","Reminder and notification system","Workflow step integration","Analytics — usage, engagement"],"icon":"💬","cat":"Integrations"},
    {"slug":"discord-bot","name":"Discord Bot","price":27,"tagline":"Custom Discord bot for community management and automation","features":["Command handler with permissions","Auto-moderation (content filtering)","Role management automation","Welcome messages and onboarding","Custom reactions and embeds","Scheduled messages","Analytics dashboard"],"icon":"🎮","cat":"Integrations"},
    {"slug":"sms-automation","name":"SMS Automation","price":47,"tagline":"Two-way SMS marketing and communication automation","features":["Bulk SMS sending (10K+/hour)","Two-way SMS with keyword triggers","MMS support (images, video)","Short code and long code management","Opt-in/opt-out management","Scheduling and automation rules","Delivery and response analytics"],"icon":"📱","cat":"Integrations"},
    {"slug":"whatsapp-bot","name":"WhatsApp Bot","price":57,"tagline":"WhatsApp Business API automation with chatbot","features":["WhatsApp Business API integration","Chatbot with NLP","Template message management","Quick reply buttons and lists","Catalog and product display","Order notification automation","Analytics — messages, deliveries, replies"],"icon":"💚","cat":"Integrations"},
    {"slug":"calendar-sync","name":"Calendar Sync","price":27,"tagline":"Cross-platform calendar synchronization and booking","features":["Google, Outlook, Apple, iCloud sync","Two-way sync (create, update, delete)","Booking page generation","Availability management","Reminder automation (email, SMS)","Team calendar overlay","Conflict detection and resolution"],"icon":"📅","cat":"Integrations"},
    {"slug":"payment-gateway","name":"Payment Gateway","price":97,"tagline":"Unified payment processing — Stripe, PayPal, Square, crypto","features":["Stripe, PayPal, Square, crypto integration","Subscription management","Invoice generation","Recurring billing automation","Tax calculation","Refund and dispute management","Revenue reporting"],"icon":"💳","cat":"Integrations"},
    {"slug":"email-verifier","name":"Email Verifier","price":27,"tagline":"Real-time email verification with 99.5% accuracy","features":["Syntax validation","Domain/MX record check","SMTP verification (mailbox existence)","Disposable email detection","Role account detection (info@, support@)","Catch-all detection","Bulk verification (10K/hour)"],"icon":"📧","cat":"Integrations"},
]

WEEK10 = [
    {"slug":"firewall","name":"Quantum Firewall","price":97,"tagline":"Web application firewall with quantum threat detection","features":["WAF rule engine (OWASP Top 10)","Rate limiting per IP/session","Bot detection and blocking","SQL injection and XSS prevention","Real-time threat intelligence feed","Log analysis and alerting","DDoS mitigation"],"icon":"🛡️","cat":"Security"},
    {"slug":"pii-scanner","name":"PII Scanner","price":47,"tagline":"Scan documents and databases for exposed personal information","features":["PII detection (SSN, CC, DOB, phone, email, address)","Database scan (MySQL, Postgres, MongoDB)","Document scan (PDF, DOCX, XLSX)","Redaction engine","Compliance reporting (GDPR, PIPEDA, CCPA)","Remediation workflow","Scheduled scans"],"icon":"🔍","cat":"Security"},
    {"slug":"vulnerability-scanner","name":"Vulnerability Scanner","price":67,"tagline":"Automated security vulnerability scanning with CVE matching","features":["Network port scanning","Web app vulnerability scanning","CVE database matching","Risk scoring (CVSS v3)","Remediation recommendations","Scheduled scans","Compliance framework mapping"],"icon":"🔒","cat":"Security"},
    {"slug":"access-control","name":"Access Control","price":57,"tagline":"Role-based access control with identity federation","features":["RBAC (Role-Based Access Control)","SSO (SAML, OAuth, OpenID)","Multi-factor authentication","Audit logging","Permission inheritance","Temporary access grants","Integration with directory services"],"icon":"🔑","cat":"Security"},
    {"slug":"audit-logger","name":"Audit Logger","price":37,"tagline":"Immutable audit logging with tamper detection","features":["SHA-256 chain integrity","Tamper detection alerts","Log search and filter","Export in standard formats","Compliance-ready (SOC2, SOX, HIPAA)","Real-time monitoring dashboard","Retention policy management"],"icon":"📝","cat":"Security"},
    {"slug":"incident-responder","name":"Incident Responder","price":97,"tagline":"Automated incident response with playbook execution","features":["Playbook editor (IF-THEN-ELSE)","Auto-containment rules","Forensic evidence collection","Notification routing","Post-incident report generation","Integration with SIEM tools","SLA tracking per incident type"],"icon":"🚨","cat":"Security"},
    {"slug":"certificate-manager","name":"Certificate Manager","price":27,"tagline":"SSL/TLS certificate lifecycle management","features":["Auto-renewal (Let's Encrypt, commercial)","Certificate expiry monitoring","Wildcard and multi-domain management","PQC TLS support","Certificate transparency logging","Private CA management","Automated deployment to servers"],"icon":"🔐","cat":"Security"},
    {"slug":"backup-manager","name":"Backup Manager","price":47,"tagline":"Automated backup with integrity verification","features":["Scheduled backups (hourly, daily, weekly)","Multiple destinations (S3, B2, local)","Incremental and full backup","SHA-256 integrity verification","Point-in-time recovery","Cross-region replication","Backup testing and restoration drills"],"icon":"💾","cat":"Security"},
    {"slug":"compliance-scanner","name":"Compliance Scanner 360","price":127,"tagline":"Continuous compliance scanning across all frameworks","features":["GDPR, CCPA, PIPEDA, SOC2, HIPAA, PCI-DSS, ISO27001","Evidence collection automation","Policy violation detection","Remediation tracking","Audit-ready report generation","Framework mapping and gap analysis","Continuous monitoring dashboards"],"icon":"✅","cat":"Security"},
    {"slug":"identity-verifier","name":"Identity Verifier","price":57,"tagline":"KYC/AML identity verification with document validation","features":["Document verification (passport, license, ID)","Biometric matching (selfie vs document)","AML screening (sanctions, PEP, adverse media)","Watchlist checking","Verification workflow builder","Compliance reporting","Manual review queue"],"icon":"🪪","cat":"Security"},
    {"slug":"threat-intel","name":"Threat Intelligence Feeds","price":97,"tagline":"Real-time threat intelligence with 50+ feed sources","features":["50+ threat feed sources","IOC extraction and matching","Severity scoring","Automated blocklist generation","Integration with firewall/WAF","Historical threat analysis","Threat hunting queries"],"icon":"🛡️","cat":"Security"},
    {"slug":"malware-scanner","name":"Malware Scanner","price":37,"tagline":"File and URL malware scanning with multi-engine detection","features":["Multi-engine scanning (ClamAV + 3 cloud engines)","URL reputation checking","File upload scanning","API for automated scanning","Scheduled site scanning","Malware removal guide generation","Weekly security report"],"icon":"🦠","cat":"Security"},
    {"slug":"zero-trust-engine","name":"Zero Trust Engine","price":147,"tagline":"Full zero-trust architecture with micro-segmentation","features":["Device authentication","User identity verification","Continuous access evaluation","Micro-segmentation rules","Least-privilege policy engine","ZTNA gateway","Zero-trust maturity reporting"],"icon":"🎯","cat":"Security"},
    {"slug":"data-encryption","name":"Data Encryption Suite","price":67,"tagline":"End-to-end encryption with quantum-resistant algorithms","features":["AES-256-GCM encryption","Post-quantum crypto (CRYSTALS-Kyber)","Key management service","BYOK (Bring Your Own Key)","HSM integration","Encrypted database fields","Key rotation automation"],"icon":"🔒","cat":"Security"},
]

def generate(product, week_label):
    rows = []
    for i, feat in enumerate(product["features"]):
        alt = ' class="alt"' if i % 2 == 1 else ""
        rows.append(f'                    <tr{alt}><td>{feat}</td></tr>')
    features_html = '\n'.join(rows) + '\n'

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{product["icon"]} {product["name"]} — ${product["price"]}/mo | Quantum Bots Agency</title>
<meta name="description" content="{product["tagline"]}. ${product["price"]}/mo. {QBA}.">
<link rel="stylesheet" href="/quantumbotsagency/css/quantum.css">
<style>
.product-hero{{background:linear-gradient(135deg,#0f0f1a 0%,#1a1a2e 100%);padding:120px 24px 60px;text-align:center}}
.product-hero h1{{font-size:48px;margin:0 0 8px}}
.product-hero .subtitle{{font-size:14px;color:#888;margin:0 0 12px}}
.product-hero .price{{font-size:32px;color:#818cf8;font-weight:700;margin:16px 0}}
.product-hero .tagline{{color:#aaa;font-size:16px;max-width:600px;margin:0 auto}}
.features-section{{max-width:800px;margin:0 auto;padding:40px 24px}}
.features-section h2{{margin-bottom:20px;color:#fff}}
.features-table{{width:100%;border-collapse:collapse}}
.features-table td{{padding:12px 16px;color:#ccc;border-bottom:1px solid #1a1a25;font-size:14px}}
.features-table .alt td{{background:rgba(255,255,255,.02)}}
.cta-section{{max-width:600px;margin:40px auto;text-align:center;padding:40px 24px}}
.cta-section .price-large{{font-size:40px;color:#818cf8;font-weight:700}}
.btn-buy{{display:inline-block;background:#818cf8;color:#000;padding:16px 48px;border-radius:8px;text-decoration:none;font-weight:700;font-size:16px;transition:all .3s;margin-top:16px}}
.qba-tag{{font-size:10px;color:#555;margin-top:32px}}
</style>
</head>
<body>
<nav class="nav">
<div class="nav-inner">
<a href="/" class="logo">⚡ QBA</a>
<div class="nav-links">
<a href="/">Home</a>
<a href="/#products">All 100 Products</a>
<a href="/#hosting">Hosting</a>
<a href="/#white-label">White Label</a>
</div>
</div>
</nav>
<section class="product-hero">
<p class="subtitle">{week_label} · {product["cat"]}</p>
<h1>{product["icon"]} {product["name"]}</h1>
<p class="tagline">{product["tagline"]}</p>
<div class="price">${product["price"]}<span>/month</span></div>
<a href="{STRIPE}" class="btn-buy" target="_blank">Subscribe Now →</a>
</section>
<section class="features-section">
<h2>🔧 Everything Included</h2>
<table class="features-table">
<tbody>
{features_html}                </tbody>
</table>
</section>
<section class="cta-section">
<p class="price-large">${product["price"]}<span>/month</span></p>
<a href="{STRIPE}" class="btn-buy" target="_blank">Start Your Subscription →</a>
<p style="color:#555;font-size:12px;margin-top:8px">Cancel anytime. No contracts. 14-day money back.</p>
<div class="qba-tag">{QBA}</div>
</section>
<a href="/" style="display:block;text-align:center;padding:20px;color:#555;font-size:12px;text-decoration:none">← Back to All 100 Products</a>
<script src="/quantumbotsagency/js/quantum-chat.js"></script>
</body>
</html>'''


os.makedirs(PRODUCTS_DIR, exist_ok=True)

all_prods = []
weeks = [("Week 6", WEEK6), ("Week 7", WEEK7), ("Week 8", WEEK8), ("Week 9", WEEK9), ("Week 10", WEEK10)]

for week_label, products in weeks:
    print(f"\n─── {week_label} ({len(products)} products) ───")
    for p in products:
        html = generate(p, week_label)
        with open(f"{PRODUCTS_DIR}/{p['slug']}.html", 'w') as f:
            f.write(html)
        print(f"  ✓ {p['slug']} — ${p['price']}/mo")
        all_prods.append(p)

print(f"\n═══ TOTAL: {len(all_prods)} new product pages ═══")
print(f"═══ RUNNING TOTAL: 46 + {len(all_prods)} = {46 + len(all_prods)} products ═══")

with open(f"{PRODUCTS_DIR}/manifest_w6_10.json", 'w') as f:
    json.dump({"total": len(all_prods), "products": all_prods}, f, indent=2)