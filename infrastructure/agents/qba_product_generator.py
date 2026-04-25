#!/usr/bin/env python3
"""
Quantum Bots Agency — Week 2-5 Product Page Generator
Builds 40 product pages (10 per week) across Content, Marketing, Research, E-Commerce categories
Each page: full pricing table, feature list, Stripe buy links, QBA branding, responsive design
"""

import os, json

SITE = "/var/openclaw_users/saul/.openclaw/workspace/site/quantumbotsagency"
PRODUCTS_DIR = f"{SITE}/products"
QBA_BRAND = "⚡ Powered by Quantum Bots Agency → quantumbotsagency.com"
STRIPE_LINK = "https://buy.stripe.com/7sYdR96za9IpfzY0jYa3u0d"

# ─── Week 2: Content & SEO Tools (10 products) ───
WEEK2 = [
    {
        "slug": "seo-optimizer",
        "name": "SEO Optimizer",
        "tagline": "Automated on-page SEO, keyword clustering, and content optimization engine",
        "price": 47,
        "category": "Content & SEO",
        "features": [
            "Auto-optimize existing content for 50+ ranking factors",
            "Keyword clustering engine — group 1,000+ keywords by intent",
            "TF-IDF analysis against top 10 competitors per keyword",
            "Automated meta title & description generator (A/B tested)",
            "Internal link recommendation engine",
            "Schema markup generator (Article, FAQ, Product, Review)",
            "Content gap analysis — find what competitors rank for that you don't",
            "Weekly SERP position tracking for 500 keywords",
            "Bulk optimization — 100 pages at once"
        ],
        "icon": "🎯"
    },
    {
        "slug": "social-scheduler",
        "name": "Social Scheduler",
        "tagline": "AI-powered multi-platform content scheduler with optimal timing algorithms",
        "price": 37,
        "category": "Content & SEO",
        "features": [
            "Schedule across 10 platforms: FB, IG, Twitter, LinkedIn, Pinterest, TikTok, YouTube, Tumblr, Reddit, Quora",
            "Quantum timing algorithm — posts when your audience is most active per timezone",
            "Content queue with auto-fill from RSS feeds + trending topics",
            "Hashtag optimizer — analyzes top performing hashtags per platform",
            "Bulk CSV upload — schedule 100 posts in 2 clicks",
            "Auto-retry on failed posts — platform API errors handled",
            "Analytics dashboard — engagement, reach, click-through per post",
            "Team collaboration — assign posts, approval workflow",
            "Evergreen recycling — auto-repost top content on a schedule"
        ],
        "icon": "📅"
    },
    {
        "slug": "pinterest-bot",
        "name": "Pinterest Bot",
        "tagline": "Automated Pinterest growth engine — pins, boards, and traffic on autopilot",
        "price": 27,
        "category": "Content & SEO",
        "features": [
            "Auto-create 50+ pins per day from existing content",
            "Smart board assignment — categorizes pins by topic match",
            "Rich pin generator — auto-adds product info, prices, availability",
            "SEO pin descriptions — keyword-optimized with CTA",
            "Board creation & naming — auto-organize by niche",
            "Tailwind-compatible export — use with approved scheduler",
            "Seasonal pin rotation — freshens old pins automatically",
            "Analytics — impressions, saves, click-through per board",
            "100 Pinterest accounts supported per license"
        ],
        "icon": "📌"
    },
    {
        "slug": "email-campaigner",
        "name": "Email Campaigner",
        "tagline": "Quantum-optimized email sequences with predictive open rates",
        "price": 57,
        "category": "Content & SEO",
        "features": [
            "7-email nurture sequences — welcome, abandoned cart, re-engagement, post-purchase",
            "Quantum subject line optimizer — predicts open rate before sending",
            "Personalization engine — merge tags, behavioral triggers, segment-based content",
            "A/B testing — subject lines, body copy, CTAs, send times",
            "Automated list cleaning — removes bounces, unsubscribes, spam traps",
            "SMTP rotator — 10 built-in SMTP servers to protect deliverability",
            "Spam score checker — tests against SpamAssassin before send",
            "Analytics — opens, clicks, conversions, revenue per email"
        ],
        "icon": "📧"
    },
    {
        "slug": "lead-magnet-builder",
        "name": "Lead Magnet Builder",
        "tagline": "AI generates high-converting lead magnets from any URL or topic",
        "price": 47,
        "category": "Content & SEO",
        "features": [
            "Generate PDF lead magnets from any URL — ebook, checklist, template, guide",
            "Choose from 12 formats: PDF, Notion, Google Doc, Slide deck, Spreadsheet",
            "Lead magnet landing page generator — opt-in form + download page",
            "Email capture integration — Mailchimp, ConvertKit, AWeber, ActiveCampaign, SendGrid",
            "Multi-variant testing — 3 headline variants tested automatically",
            "Analytics — downloads, conversion rate, email acquisition cost",
            "White-label — remove QBA branding on Pro tier"
        ],
        "icon": "🧲"
    },
    {
        "slug": "bridge-page-maker",
        "name": "Bridge Page Maker",
        "tagline": "Affiliate bridge pages that rank and convert — no platform bans",
        "price": 37,
        "category": "Content & SEO",
        "features": [
            "Generate 'Top 5' review pages, comparison tables, and buyer guides",
            "Link cloaking — outgoing affiliate links masked as internal URLs",
            "Value-first layout — 3 paragraphs of advice before any affiliate link",
            "SEO-optimized template — schema-marked reviews, auto-generated FAQs",
            "One-click deploy to custom domain or subdomain",
            "A/B testing — 4 page variants tested for conversion rate",
            "FTC compliance built in — auto-disclosure placement",
            "Platform-safe — built to pass FB, Google, TikTok content review"
        ],
        "icon": "🌉"
    },
    {
        "slug": "analytics-dashboard",
        "name": "Analytics Dashboard",
        "tagline": "Unified analytics across all your products, campaigns, and platforms",
        "price": 67,
        "category": "Content & SEO",
        "features": [
            "Connect unlimited data sources — GA4, Stripe, social platforms, CRMs",
            "Custom dashboard builder — drag-and-drop widgets",
            "Real-time metrics — active users, revenue, conversion rate, ROAS",
            "Automated reports — daily/weekly/monthly PDF export",
            "Goal tracking — set targets, get alerts on milestones",
            "Cohort analysis — retention, LTV, churn by segment",
            "Custom alerts — Slack, email, SMS when KPIs cross thresholds"
        ],
        "icon": "📊"
    },
    {
        "slug": "clickbank-analyzer",
        "name": "ClickBank Analyzer",
        "tagline": "Real-time Gravity scoring, competitor ad spy, and Blue Ocean niche finder",
        "price": 47,
        "category": "Content & SEO",
        "features": [
            "Real-time Gravity scores for ALL ClickBank marketplace products",
            "Gravity targeting — filter products between 50-200 (sweet spot)",
            "Competitor ad spy — see which ads are running per product",
            "Blue Ocean finder — high payout + low competition intersections",
            "Affiliate link validator — check if your links are active",
            "Commission history — track upsell rates, refund rates per product",
            "Category trends — which niches are rising/falling daily",
            "Export to CSV — build your product research database"
        ],
        "icon": "🔍"
    },
    {
        "slug": "ad-spy-tool",
        "name": "Ad Spy Tool",
        "tagline": "Spy on competitor ads across Facebook, Google, TikTok, and Native",
        "price": 67,
        "category": "Content & SEO",
        "features": [
            "Ad library search — FB Ads Library, Google Ads Transparency, TikTok Ad Library",
            "Ad copy analyzer — extract winning hooks, angles, CTAs",
            "Creative analyzer — image/text ratio, color schemes, video length",
            "Landing page scraper — harvest competitor funnel structure",
            "Spend estimator — estimated ad spend per competitor per day",
            "Alerts — get notified when competitors launch new ads",
            "Export ad reports — build your swipe file for inspiration"
        ],
        "icon": "🕵️"
    },
    {
        "slug": "keyword-explorer",
        "name": "Keyword Explorer Pro",
        "tagline": "Quantum-scale keyword research with intent scoring and difficulty analysis",
        "price": 57,
        "category": "Content & SEO",
        "features": [
            "100,000 keyword suggestions per seed keyword",
            "Intent scoring — informational, navigational, commercial, transactional",
            "Keyword difficulty — predicts ranking probability with ML model",
            "SERP feature analysis — featured snippets, People Also Ask, video carousels",
            "Long-tail keyword generator — find zero-competition gold mines",
            "Cluster builder — group keywords by topic for pillar pages",
            "Weekly rank tracking for 1,000 keywords",
            "Export to CSV, Google Sheets, or Ahrefs format"
        ],
        "icon": "🔎"
    }
]

# ─── Week 3: Marketing & Conversion Tools (10 products) ───
WEEK3 = [
    {
        "slug": "social-proof-engine",
        "name": "Social Proof Engine",
        "tagline": "FOMO-driven conversion optimization with live social proof injections",
        "price": 37,
        "category": "Marketing & Conversion",
        "features": ["Live purchase notifications (configurable: X people bought this)", "Countdown timers for limited-time offers", "Live visitor counter", "Recent review rotator", "Stock scarcity indicators ('Only 3 left')", "Customizable widget design (position, color, animation)", "A/B testing — which proof type converts best per page"]
    },
    {
        "slug": "ab-testing-engine",
        "name": "A/B Testing Engine",
        "tagline": "Multi-variant testing on autopilot — winner auto-selected",
        "price": 47,
        "category": "Marketing & Conversion",
        "features": ["Headline, CTA, image, and layout testing", "Statistical significance calculator", "Winner auto-promotion after confidence threshold", "Traffic split — 50/50, 70/30, or custom ratios", "Heatmap integration — see where users click per variant", "Revenue tracking per variant", "Test history with full data export"]
    },
    {
        "slug": "funnel-builder",
        "name": "Funnel Builder",
        "tagline": "Drag-and-drop sales funnel builder with quantum optimization",
        "price": 77,
        "category": "Marketing & Conversion",
        "features": ["Visual funnel editor — drag, drop, connect", "Pre-built funnel templates (click-through, VSL, webinar, quiz)", "One-click upsell/downsell/order bump placement", "Stripe checkout integration with payment routing", "Email sequence auto-triggered at funnel stage", "A/B testing per funnel step", "Analytics — conversion rate, drop-off point, revenue per step"]
    },
    {
        "slug": "retargeting-bot",
        "name": "Retargeting Bot",
        "tagline": "Automated multi-channel retargeting campaigns with predictive timing",
        "price": 57,
        "category": "Marketing & Conversion",
        "features": ["Facebook Pixel + Google Ads + TikTok Pixel integration", "Segment-based retargeting (cart abandoners, page viewers, past buyers)", "Dynamic ad creative generation per segment", "Frequency capping — max 3 views per user per day", "Cross-device retargeting", "Budget optimization — highest ROAS segments get more spend", "ROAS reporting per retargeting campaign"]
    },
    {
        "slug": "traffic-analyzer",
        "name": "Traffic Analyzer",
        "tagline": "Deep traffic source analysis with attribution modeling",
        "price": 47,
        "category": "Marketing & Conversion",
        "features": ["Traffic source detection — organic, paid, social, direct, referral", "UTM parameter auto-builder", "Attribution modeling — first-click, last-click, linear, time-decay", "Bot traffic filtering (exclude crawlers, scrapers)", "Geo analysis — traffic by country, region, city", "Device breakdown — desktop, mobile, tablet conversion rates", "Custom report export"]
    },
    {
        "slug": "lead-scorer",
        "name": "Lead Scorer",
        "tagline": "ML-powered lead scoring — prioritize who to call first",
        "price": 47,
        "category": "Marketing & Conversion",
        "features": ["Behavioral scoring — page visits, email opens, time on site", "Demographic scoring — industry, company size, job title", "Predictive ML model — trained on your past conversion data", "CRM integration — HubSpot, Salesforce, Pipedrive", "Auto-assignment — highest scores routed to top sales reps", "Decay scoring — score decreases if lead goes cold", "Alert on high-value lead engagement"]
    },
    {
        "slug": "conversion-optimizer",
        "name": "Conversion Optimizer",
        "tagline": "Real-time conversion rate optimization with quantum algorithms",
        "price": 57,
        "category": "Marketing & Conversion",
        "features": ["Real-time page element testing (headlines, CTAs, images)", "Heatmap + scroll map + click map generation", "Session recording — watch 100% of user sessions", "Form analysis — which fields cause abandonment", "Exit intent detection + popup trigger", "Quantum recommendation engine — suggests page changes ranked by lift", "Revenue impact projection per change"]
    },
    {
        "slug": "budget-allocator",
        "name": "Budget Allocator",
        "tagline": "Quantum-optimized budget distribution across ad platforms",
        "price": 37,
        "category": "Marketing & Conversion",
        "features": ["Connect ad accounts — FB, Google, TikTok, LinkedIn, Pinterest", "Real-time ROAS comparison across platforms", "Auto-reallocation — move budget to highest ROAS platform", "Budget caps per platform per day", "Forecast modeling — what happens if budget increases 20%", "Multi-currency support", "Weekly budget performance report"]
    },
    {
        "slug": "crm-sync",
        "name": "CRM Sync Pro",
        "tagline": "Two-way CRM synchronization across all your tools",
        "price": 47,
        "category": "Marketing & Conversion",
        "features": ["Bi-directional sync — HubSpot, Salesforce, Pipedrive, Zoho, Close", "Field mapping — custom field matching between systems", "De-duplication — merge duplicate contacts automatically", "Activity logging — calls, emails, meetings logged to CRM", "Webhook triggers — CRM events fire automations", "Bulk import/export — CSV, JSON, XML", "Sync conflict resolution rules"]
    },
    {
        "slug": "custom-dashboard",
        "name": "Custom Dashboard Builder",
        "tagline": "Build unlimited custom dashboards from any data source",
        "price": 37,
        "category": "Marketing & Conversion",
        "features": ["Drag-and-drop widget editor", "50+ chart types (bar, line, pie, funnel, heatmap, table)", "SQL query editor for custom data pulls", "Data source connectors — 100+ integrations", "Role-based dashboards — different views for exec, manager, analyst", "Scheduled PDF/email reports", "Public dashboard sharing option"]
    }
]

# ─── Week 4: Research & Intel (10 products) ───
WEEK4 = [
    {
        "slug": "competitor-tracker",
        "name": "Competitor Tracker",
        "tagline": "24/7 competitive intelligence — know every move your rivals make",
        "price": 67,
        "category": "Research & Intel",
        "features": ["Website change monitoring — track product, price, content changes", "Social media tracking — new posts, engagement spikes, follower growth", "Ad monitoring — new campaigns, creative changes, budget shifts", "Pricing alerts — email/Slack when competitor changes price", "Email monitoring — subscribe to competitor newsletters automatically", "Job posting tracker — see hiring patterns for strategic intel", "Weekly competitive brief generated and delivered"]
    },
    {
        "slug": "trend-detector",
        "name": "Trend Detector",
        "tagline": "Early trend detection from 50+ sources — be first to market",
        "price": 47,
        "category": "Research & Intel",
        "features": ["50 data sources: Google Trends, Twitter, Reddit, Quora, news, patent filings", "Trend scoring — velocity, volume, longevity prediction", "Niche-specific filters — find trends in your industry only", "Alert system — notified when trend crosses threshold", "Historical analysis — see how similar trends performed", "Export trend data for content calendar planning", "API access for custom integration"]
    },
    {
        "slug": "market-analyzer",
        "name": "Market Analyzer",
        "tagline": "Deep market analysis with TAM, SAM, SOM calculations",
        "price": 57,
        "category": "Research & Intel",
        "features": ["TAM/SAM/SOM calculator per niche", "Competitive landscape mapping — market share chart", "Pricing analysis — competitor price distribution", "Customer persona generator from market data", "Market growth rate projection", "Regulatory risk assessment", "Export market analysis report as PDF"]
    },
    {
        "slug": "content-gap-finder",
        "name": "Content Gap Finder",
        "tagline": "Find content gaps your competitors haven't filled — rank instantly",
        "price": 37,
        "category": "Research & Intel",
        "features": ["Compare your domain vs 5 competitors for keyword overlap", "Gap scoring — how many competitors rank, how hard to break in", "Zero-competition keywords filter", "Keyword difficulty threshold adjustable (0-100)", "Content brief generator for each gap", "Priority ranking — which gaps to fill first by traffic potential", "Weekly gap analysis delivered"]
    },
    {
        "slug": "audience-profiler",
        "name": "Audience Profiler",
        "tagline": "Quantum-powered audience segmentation and profiling",
        "price": 47,
        "category": "Research & Intel",
        "features": ["Import audience from CRM, email list, or social followers", "Demographic segmentation — age, gender, location, income", "Psychographic profiling — interests, values, lifestyle clusters", "Behavioral segmentation — purchase history, engagement patterns", "Lookalike audience generator for ad platforms", "Persona document auto-generation", "Audience overlap analysis"]
    },
    {
        "slug": "sentiment-analyzer",
        "name": "Sentiment Analyzer",
        "tagline": "Real-time brand sentiment monitoring across the open web",
        "price": 47,
        "category": "Research & Intel",
        "features": ["Brand mention monitoring — social, news, forums, reviews", "Sentiment scoring — positive, negative, neutral with confidence", "Trend tracking — sentiment change over time", "Alert on negative sentiment spikes", "Competitor sentiment comparison", "Thematic analysis — what topics drive positive/negative sentiment", "Weekly sentiment report"]
    },
    {
        "slug": "price-tracker",
        "name": "Price Tracker",
        "tagline": "Automated competitor price monitoring with dynamic repricing",
        "price": 37,
        "category": "Research & Intel",
        "features": ["Track competitor prices daily", "Price change alerts — email/Slack/webhook", "Price history charts — see pricing patterns over time", "Repricing rule engine — auto-adjust based on competitor moves", "MAP compliance monitoring — enforce minimum advertised price", "Competitor promotion tracking — sale events, coupons, bundles", "Export price data as CSV"]
    },
    {
        "slug": "product-validator",
        "name": "Product Validator",
        "tagline": "Validate product ideas with market data before building",
        "price": 47,
        "category": "Research & Intel",
        "features": ["Search volume analysis for product-related keywords", "Existing competitor count and quality assessment", "Review sentiment analysis for similar products", "Price point optimization — what the market will bear", "Profit margin calculator after fees, ads, COGS", "Demand forecast — projected monthly sales", "Go/No-go recommendation with confidence score"]
    },
    {
        "slug": "niche-finder",
        "name": "Niche Finder Pro",
        "tagline": "Blue Ocean niche discovery engine — find profitable niches with low competition",
        "price": 67,
        "category": "Research & Intel",
        "features": ["Cross-reference 50+ niche criteria: search volume, competition, payout, trend", "Profitability score — estimated monthly earnings per niche", "Keyword availability — how many keywords have low competition", "Affiliate network compatibility — ClickBank, Amazon, ShareASale, CJ", "Entry barrier assessment — cost, complexity, regulation", "Seasonality analysis — which months peak per niche", "Top 10 niche recommendations with data backing"]
    },
    {
        "slug": "backlink-checker",
        "name": "Backlink Checker Pro",
        "tagline": "Full backlink audit and analysis with toxic link detection",
        "price": 47,
        "category": "Research & Intel",
        "features": ["Full backlink profile audit — 1M+ links per domain", "Toxic link detection — Google penalty risk score per link", "Link quality scoring — DA, relevance, anchor text, follow/nofollow", "Competitor backlink comparison — find link opportunities", "Link building suggestions — broken links, unlinked mentions, guest post targets", "Disavow file generator for toxic links", "Weekly backlink monitoring with change alerts"]
    }
]

# ─── Week 5: Operations & E-Commerce (10 products) ───
WEEK5 = [
    {
        "slug": "task-manager",
        "name": "Task Manager Quantum",
        "tagline": "Quantum-prioritized task management for teams of any size",
        "price": 37,
        "category": "Operations & Workflow",
        "features": ["Unlimited tasks, projects, and teams", "Quantum prioritization — auto-order tasks by impact + urgency", "Time tracking with auto-suggested estimates", "Dependencies and blockers tracking", "Kanban, list, and calendar views", "Automation rules — assign, move, tag tasks automatically", "Slack, email, and webhook integration"]
    },
    {
        "slug": "workflow-builder",
        "name": "Workflow Builder",
        "tagline": "Visual workflow automation without code",
        "price": 47,
        "category": "Operations & Workflow",
        "features": ["Drag-and-drop workflow editor", "200+ triggers and 500+ actions", "Conditional logic — if/then/else, loops, delays", "Zapier/Make compatible — export/import workflows", "Error handling — retry, fallback, alert on failure", "Workflow templates for common processes", "Execution logs and debugging tools"]
    },
    {
        "slug": "invoice-generator",
        "name": "Invoice Generator",
        "tagline": "Automated invoice creation and payment tracking",
        "price": 27,
        "category": "Operations & Workflow",
        "features": ["Auto-generate invoices from Stripe/subscription data", "Custom invoice templates with brand colors/logo", "Recurring invoice automation", "Payment tracking — paid, overdue, cancelled status", "Late payment reminders (1, 3, 7, 14 days)", "Multi-currency invoice support", "PDF export and email delivery"]
    },
    {
        "slug": "contract-analyzer",
        "name": "Contract Analyzer",
        "tagline": "AI contract review — flag risks, obligations, and deadlines",
        "price": 57,
        "category": "Operations & Workflow",
        "features": ["Upload any PDF/DOCX contract for AI analysis", "Risk flagging — liability, indemnification, termination clauses", "Obligation extraction — deadlines, reporting, payment schedules", "Comparison mode — compare contract vs standard template", "Compliance check — GDPR, CCPA, PIPEDA clause detection", "Key terms summary in plain English", "Export analysis report"]
    },
    {
        "slug": "compliance-checker",
        "name": "Compliance Checker",
        "tagline": "Automated compliance scanning across 30+ regulatory frameworks",
        "price": 67,
        "category": "Operations & Workflow",
        "features": ["30+ frameworks: GDPR, CCPA, PIPEDA, FTC, FDA, HIPAA, SOC2", "Website compliance scan — cookie consent, privacy policy, ToS", "Ad compliance check — FTC endorsement guidelines, platform policies", "FTC disclosure verification for affiliate content", "Email compliance (CAN-SPAM, CASL) auto-scan", "Violation report with fix recommendations", "Continuous monitoring with change alerts"]
    },
    {
        "slug": "report-generator",
        "name": "Report Generator",
        "tagline": "Automated reports from any data source — PDF, CSV, interactive",
        "price": 37,
        "category": "Operations & Workflow",
        "features": ["Schedule reports daily, weekly, monthly", "Connect any data source (GA4, Stripe, social, CRM, SQL)", "Template builder with drag-and-drop sections", "Conditional formatting — highlight metrics above/below target", "PDF, CSV, HTML, and interactive web report output", "Auto-distribute to email list or Slack channel", "White-label reports — remove QBA logo"]
    },
    {
        "slug": "store-builder",
        "name": "Store Builder",
        "tagline": "One-click e-commerce store with quantum conversion optimization",
        "price": 97,
        "category": "E-Commerce & Sales",
        "features": ["Full e-commerce store in 5 minutes — products, cart, checkout", "Stripe payment integration with 40+ payment methods", "Product management — variants, inventory, digital downloads", "SEO-optimized product pages with schema markup", "Order management dashboard", "Shipping calculator and tax auto-calculation", "Analytics — revenue, orders, conversion rate, AOV"]
    },
    {
        "slug": "product-listing-optimizer",
        "name": "Product Listing Optimizer",
        "tagline": "Optimize product listings for Amazon, Shopify, and Etsy",
        "price": 37,
        "category": "E-Commerce & Sales",
        "features": ["Title optimization — keyword placement, length, readability scoring", "Bullet point generator — highlight 5 key benefits with keywords", "Description writer — SEO-optimized product descriptions", "Image tag suggestions — alt text, file naming", "Backend keyword stuffing optimizer", "Competitor listing comparison — see what top sellers do better", "Listing score — A/B test before publishing"]
    },
    {
        "slug": "cart-recoverer",
        "name": "Cart Recoverer",
        "tagline": "Automated abandoned cart recovery with quantum timing",
        "price": 47,
        "category": "E-Commerce & Sales",
        "features": ["Track 100% of abandoned carts across all pages", "Recovery email sequence (1hr, 6hr, 24hr, 72hr)", "SMS recovery for opted-in customers", "Discount offer optimization — find the minimum discount that converts", "Real-time dashboard — recovery rate, recovered revenue, AOV", "A/B test recovery message timing and content", "Stripe/WooCommerce/Shopify integration"]
    },
    {
        "slug": "subscription-manager",
        "name": "Subscription Manager",
        "tagline": "Full subscription lifecycle management with churn prediction",
        "price": 57,
        "category": "E-Commerce & Sales",
        "features": ["Create and manage subscription plans (weekly, monthly, yearly)", "Proration engine — handle plan changes mid-cycle", "Churn prediction ML model — flag at-risk subscribers", "Retention offer automation — discount, pause, downgrade options", "Revenue forecasting — MRR, ARR, churn rate projections", "Failed payment recovery — retry logic + email/SMS alerts", "Customer portal — subscribers manage own plans"]
    }
]

def generate_product_page(product, week_label):
    """Generate a complete product page HTML."""
    rows = []
    for i, feat in enumerate(product["features"]):
        alt = ' class="alt"' if i % 2 == 1 else ""
        rows.append('                    <tr' + alt + '><td>' + feat + '</td></tr>')
    features_html = '\n'.join(rows) + '\n'
    # Clean up the f-string reference below - the template uses {features_html}
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{(product.get("icon","🔷"))} {product["name"]} — ${product["price"]}/mo | Quantum Bots Agency</title>
<meta name="description" content="{product["tagline"]}. ${product["price"]}/mo. {QBA_BRAND}.">
<link rel="stylesheet" href="/quantumbotsagency/css/quantum.css">
<link rel="stylesheet" href="/quantumbotsagency/css/quantum-chat.css">
<style>
.product-hero{{background:linear-gradient(135deg,#0f0f1a 0%,#1a1a2e 100%);padding:120px 24px 60px;text-align:center}}
.product-hero h1{{font-size:48px;margin:0 0 8px}}
.product-hero .subtitle{{font-size:14px;color:#888;margin:0 0 12px}}
.product-hero .price{{font-size:32px;color:#818cf8;font-weight:700;margin:16px 0}}
.product-hero .price span{{font-size:16px;color:#888}}
.product-hero .tagline{{color:#aaa;font-size:16px;max-width:600px;margin:0 auto}}
.features-section{{max-width:800px;margin:0 auto;padding:40px 24px}}
.features-section h2{{margin-bottom:20px;color:#fff}}
.features-table{{width:100%;border-collapse:collapse}}
.features-table td{{padding:12px 16px;color:#ccc;border-bottom:1px solid #1a1a25;font-size:14px}}
.features-table .alt td{{background:rgba(255,255,255,.02)}}
.cta-section{{max-width:600px;margin:40px auto;text-align:center;padding:40px 24px}}
.cta-section .price-large{{font-size:40px;color:#818cf8;font-weight:700}}
.cta-section .price-large span{{font-size:18px;color:#888}}
.btn-buy{{display:inline-block;background:#818cf8;color:#000;padding:16px 48px;border-radius:8px;text-decoration:none;font-weight:700;font-size:16px;transition:all .3s;margin-top:16px}}
.btn-buy:hover{{background:#6366f1;transform:translateY(-2px)}}
.btn-monthly{{background:transparent;border:1px solid #333;color:#888;padding:12px 32px;border-radius:8px;text-decoration:none;font-size:13px;margin-top:12px;display:inline-block}}
.back-link{{display:block;text-align:center;padding:20px;color:#555;font-size:12px;text-decoration:none}}
.back-link:hover{{color:#888}}
.qba-tag{{font-size:10px;color:#555;margin-top:32px}}
</style>
</head>
<body>
<nav class="nav">
<div class="nav-inner">
<a href="/" class="logo">⚡ QBA</a>
<div class="nav-links">
<a href="/">Home</a>
<a href="/#products">All Products</a>
<a href="/#hosting">Hosting</a>
<a href="/#white-label">White Label</a>
</div>
</div>
</nav>

<section class="product-hero">
<p class="subtitle">{week_label} · {product["category"]}</p>
<h1>{(product.get("icon","🔷"))} {product["name"]}</h1>
<p class="tagline">{product["tagline"]}</p>
<div class="price">${product["price"]}<span>/month</span></div>
<a href="{STRIPE_LINK}" class="btn-buy" target="_blank">Subscribe Now →</a>
<a href="#features" class="btn-monthly">See all features ↓</a>
</section>

<section id="features" class="features-section">
<h2>🔧 Everything Included</h2>
<table class="features-table">
<tbody>
{features_html}                </tbody>
</table>
</section>

<section class="cta-section">
<p class="price-large">${product["price"]}<span>/month</span></p>
<a href="{STRIPE_LINK}" class="btn-buy" target="_blank">Start Your Subscription →</a>
<p style="color:#555;font-size:12px;margin-top:8px">Cancel anytime. No contracts. 14-day money back.</p>
<div class="qba-tag">{QBA_BRAND}</div>
</section>

<a href="/" class="back-link">← Back to All Products</a>

<script src="/quantumbotsagency/js/quantum-chat.js"></script>
</body>
</html>'''


def generate_all():
    """Generate all 40 product pages."""
    os.makedirs(PRODUCTS_DIR, exist_ok=True)
    
    all_products = []
    
    weeks = [
        ("Week 2", "Content & SEO", WEEK2),
        ("Week 3", "Marketing & Conversion", WEEK3),
        ("Week 4", "Research & Intel", WEEK4),
        ("Week 5", "Operations & E-Commerce", WEEK5),
    ]
    
    for week_label, category, products in weeks:
        print(f"\n{'='*50}")
        print(f"{week_label}: {category}")
        print(f"{'='*50}")
        
        for product in products:
            html = generate_product_page(product, week_label)
            filepath = os.path.join(PRODUCTS_DIR, f"{product['slug']}.html")
            with open(filepath, 'w') as f:
                f.write(html)
            print(f"  ✓ {product['slug']} — ${product['price']}/mo")
            all_products.append(product)
    
    # Generate master product index
    print(f"\n{'='*50}")
    print(f"Total: {len(all_products)} product pages generated")
    print(f"{'='*50}")
    
    # Save product manifest for main site
    manifest = {
        "total": len(all_products),
        "products": all_products,
        "generated_at": "2026-04-24T18:26:00Z"
    }
    with open(f"{SITE}/products/manifest.json", 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"Manifest saved to: {PRODUCTS_DIR}/{all_products[0]['slug']}.html ... {all_products[-1]['slug']}.html")

if __name__ == "__main__":
    generate_all()