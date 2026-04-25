#!/usr/bin/env python3
"""Build the 50-industry hub page for QBA"""
import json

# All 50 industries data
data = json.loads(open('/dev/stdin').read()) if False else None  # placeholder

industries = [
    ("Healthcare & Medical", "🏥", "Pre-trained on HIPAA compliance, medical terminology, patient communication protocols, and healthcare marketing regulations.",
     ["Patient Intake Agent","Medical Scheduler","Claims Assistant","Health Content Writer","Compliance Monitor"],
     ["ClickBank: Health & Fitness Niche|clickbank-analyzer.html","Bridge Page: Supplement Reviews|bridge-page-maker.html","Email: Cure-Specific Sequences|email-campaigner.html"],"$49/mo"),

    ("E-Commerce & Retail", "🛒", "Trained on Shopify API, Amazon marketplace, cart recovery optimization, product listing SEO, and multi-channel sales.",
     ["Cart Recovery Agent","Product Lister","Inventory Manager","Review Collector","Cross-Sell Engine"],
     ["Product Validation (Gravity Check)|product-validator.html","Funnel: Product Launch|funnel-builder.html","Retargeting: Cart Abandoners|retargeting-bot.html"],"$49/mo"),

    ("Real Estate & Property", "🏠", "Trained on MLS data structures, property valuation models, buyer qualification scoring, and realtor compliance.",
     ["Lead Qualifier","Property Matcher","Market Analyst","Listing Optimizer","Appointment Setter"],
     ["Lead Magnet: Home Buyer Guides|lead-magnet-builder.html","Niche: Foreclosure/Short-Sale|niche-finder.html","Email: Property Alerts|email-campaigner.html"],"$49/mo"),

    ("Legal & Law Firms", "⚖️", "Pre-trained on legal terminology, case management workflows, client intake ethics rules, and bar association compliance.",
     ["Case Intake Agent","Document Analyzer","Legal Researcher","Contract Reviewer","Appointment Manager"],
     ["ClickBank: Legal Templates Niche|clickbank-analyzer.html","Bridge Page: Free Consultation|bridge-page-maker.html","Compliance: ABA Rules|compliance-checker.html"],"$79/mo"),

    ("Finance & Banking", "💰", "Trained on SEC regulations, investment terminology, risk assessment models, and financial advisory compliance.",
     ["Client Onboarding Agent","Market Monitor","Risk Assessor","Compliance Scanner","Portfolio Tracker"],
     ["Trend: Emerging Markets|trend-detector.html","Email: Investment Digest|email-campaigner.html","Lead: Qualified Investors|lead-scorer.html"],"$79/mo"),

    ("SaaS & Software", "💻", "Trained on PLG metrics, churn prediction, API documentation, developer relations, and product-led growth funnels.",
     ["Support Engineer Bot","Churn Predictor","Docs Assistant","User Onboarding Agent","Bug Triage Agent"],
     ["Product: Validate Idea|product-validator.html","Funnel: Free Trial to Paid|funnel-builder.html","CRM: Lead Nurture|crm-automation.html"],"$79/mo"),

    ("Marketing Agencies", "📢", "Trained on campaign management, client reporting, ad platform APIs (Google/Meta/TikTok), and agency workflow.",
     ["Campaign Manager","Report Generator","Ad Optimizer","Client Comms Bot","Social Scheduler"],
     ["Ad Spy: Competitor Intel|ad-spy-tool.html","Social: Content Calendar|social-scheduler.html","Retarget: Campaign Rollover|retargeting-bot.html"],"$49/mo"),

    ("Education & E-Learning", "🎓", "Trained on curriculum design, student engagement models, assessment evaluation, and learning management systems.",
     ["Student Support Agent","Course Recommender","Grading Assistant","Content Tutor","Enrollment Funnel"],
     ["ClickBank: Online Courses Niche|clickbank-analyzer.html","Email: Course Launch|email-campaigner.html","Funnel: Mini-Course to Paid|funnel-builder.html"],"$49/mo"),

    ("Fitness & Wellness", "💪", "Trained on exercise science, nutrition protocols, client progress tracking, and fitness membership models.",
     ["Personal Trainer Bot","Nutrition Planner","Progress Tracker","Class Scheduler","Retention Agent"],
     ["ClickBank: Weight Loss Niche|clickbank-analyzer.html","Bridge Page: Program Reviews|bridge-page-maker.html","Email: 30-Day Challenge|email-campaigner.html"],"$49/mo"),

    ("Dental & Oral Health", "🦷", "Pre-trained on dental procedures terminology, patient education, insurance verification, and recall scheduling.",
     ["Appointment Agent","Insurance Verifier","Recall Engine","Procedure Educator","Review Collector"],
     ["ClickBank: Oral Health Products|clickbank-analyzer.html","Email: Hygiene Reminder|email-campaigner.html","Lead Magnet: Whitening Guide|lead-magnet-builder.html"],"$49/mo"),

    ("Insurance & Brokerage", "🛡️", "Trained on policy structures, claims processing, risk assessment, and insurance compliance.",
     ["Quote Generator","Claims Bot","Policy Advisor","Risk Assessor","Renewal Agent"],
     ["Compliance: State Regs|compliance-checker.html","Email: Policy Review|email-campaigner.html","Lead: Buyer Intent|lead-scorer.html"],"$79/mo"),

    ("Hospitality & Travel", "🏨", "Trained on booking systems, guest experience management, dynamic pricing, and tourism marketing.",
     ["Concierge Bot","Booking Assistant","Review Manager","Revenue Optimizer","Loyalty Engine"],
     ["ClickBank: Travel Gear Niche|clickbank-analyzer.html","Bridge Page: Destinations|bridge-page-maker.html","Pinterest: Travel Pins|pinterest-bot.html"],"$49/mo"),

    ("Automotive & Dealerships", "🚗", "Trained on vehicle inventory, test drive scheduling, financing qualification, and after-sales service.",
     ["Sales Assistant","Service Scheduler","Inventory Manager","Finance Bot","Review Collector"],
     ["ClickBank: Auto Accessories|clickbank-analyzer.html","Email: Service Reminder|email-campaigner.html","Lead: Buyer Readiness|lead-scorer.html"],"$49/mo"),

    ("Construction & Contracting", "🏗️", "Trained on project management, bid processing, building codes, subcontractor coordination, and safety compliance.",
     ["Project Manager","Bid Evaluator","Safety Auditor","Schedule Optimizer","Supplier Coordinator"],
     ["Bridge Page: Service Areas|bridge-page-maker.html","Email: Project Updates|email-campaigner.html","Lead Magnet: Estimate Calc|lead-magnet-builder.html"],"$49/mo"),

    ("Restaurants & Food Service", "🍽️", "Trained on POS integration, delivery logistics, reservation management, menu optimization, and food safety.",
     ["Reservation Agent","Order Manager","Inventory Tracker","Menu Optimizer","Review Responder"],
     ["ClickBank: Kitchen Gadgets|clickbank-analyzer.html","Pinterest: Recipe Traffic|pinterest-bot.html","Email: Loyalty Program|email-campaigner.html"],"$49/mo"),

    ("Beauty & Cosmetics", "💄", "Trained on product formulations, skin types, color matching, salon booking, and influencer marketing.",
     ["Product Advisor","Booking Agent","Skin Analyzer","Influencer Matcher","Loyalty Engine"],
     ["ClickBank: Beauty Niche|clickbank-analyzer.html","Bridge Page: Product Reviews|bridge-page-maker.html","Pinterest: Tutorial Pins|pinterest-bot.html"],"$49/mo"),

    ("Salon, Nail & Barbershop", "💅", "Pre-trained on salon booking, service menus, retail inventory, loyalty programs, and client retention. Features Jeannie Nails Academy integration.",
     ["Booking Manager","Service Advisor","Retail Cross-Seller","Recall Engine","Trainer Agent"],
     ["ClickBank: Salon Products|clickbank-analyzer.html","Email: Appointment + Upsell|email-campaigner.html","Bridge Page: Salon Reviews|bridge-page-maker.html"],"$49/mo"),

    ("Pet Care & Veterinary", "🐾", "Trained on pet health, grooming services, appointment scheduling, prescription management, and pet product knowledge.",
     ["Grooming Scheduler","Health Advisor","Appointment Agent","Product Recommender","Refill Reminder"],
     ["ClickBank: Pet Products|clickbank-analyzer.html","Email: Pet Care Tips|email-campaigner.html","Pinterest: Pet Traffic|pinterest-bot.html"],"$49/mo"),

    ("Accounting & Bookkeeping", "📊", "Trained on GAAP standards, tax codes, invoicing workflows, payroll processing, and audit preparation.",
     ["Invoice Bot","Expense Tracker","Tax Preparer","Payroll Agent","Audit Assistant"],
     ["ClickBank: Business Software|clickbank-analyzer.html","Email: Tax Reminders|email-campaigner.html","Compliance: GAAP/IRS|compliance-scanner.html"],"$79/mo"),

    ("HR & Recruiting", "👔", "Trained on ATS integration, resume parsing, interview scheduling, employee onboarding, and labor law.",
     ["Resume Screener","Interview Scheduler","Onboarding Agent","Compliance Checker","Performance Tracker"],
     ["ClickBank: Career Products|clickbank-analyzer.html","Email: Candidate Nurture|email-campaigner.html","Funnel: Job Board|funnel-builder.html"],"$79/mo"),

    ("Photography & Videography", "📸", "Trained on booking workflows, portfolio management, client proofing, equipment knowledge, and editing workflows.",
     ["Booking Agent","Gallery Curator","Client Comms Bot","Equipment Advisor","Review Collector"],
     ["ClickBank: Camera Gear|clickbank-analyzer.html","Video: Behind-the-Scenes|video-script-generator.html","Pinterest: Portfolio|pinterest-bot.html"],"$49/mo"),

    ("Nonprofit & NGOs", "🌍", "Trained on donor management, grant writing, fundraising campaigns, volunteer coordination, and impact reporting.",
     ["Donor Engagement Bot","Grant Writer","Volunteer Coordinator","Campaign Analyst","Impact Reporter"],
     ["Email: Donor Nurture|email-campaigner.html","Lead Magnet: Impact Reports|lead-magnet-builder.html","Funnel: Monthly Donor|funnel-builder.html"],"$49/mo"),

    ("Fintech, Crypto & Blockchain", "🪙", "Trained on DeFi protocols, XRPL/XRP ecosystem, smart contract interaction, wallet management, and crypto compliance.",
     ["Wallet Assistant","Market Analyzer","Smart Contract Tester","DeFi Strategist","Compliance Scanner"],
     ["ClickBank: Crypto Courses|clickbank-analyzer.html","Bridge Page: Token Reviews|bridge-page-maker.html","Social: XRP/Twitter|social-scheduler.html"],"$79/mo"),

    ("Consulting & Coaching", "🧠", "Trained on engagement frameworks, client intake, proposal generation, billing models, and thought leadership.",
     ["Client Intake Agent","Proposal Generator","Engagement Tracker","Billing Bot","Content Publisher"],
     ["ClickBank: Coaching Niche|clickbank-analyzer.html","Email: Discovery Sequence|email-campaigner.html","Funnel: Free Call to Paid|funnel-builder.html"],"$79/mo"),

    ("Holistic Health & Alt Medicine", "🌿", "Pre-trained on herbal remedies, supplement interactions, holistic protocols, and naturopathic terminology.",
     ["Remedy Advisor","Supplement Checker","Protocol Builder","Contraindication Scanner","Content Creator"],
     ["ClickBank: Alt Health|clickbank-analyzer.html","Bridge Page: Remedy Reviews|bridge-page-maker.html","Email: Wellness Sequence|email-campaigner.html"],"$49/mo"),

    ("Gyms & Fitness Centers", "🏋️", "Trained on membership management, class scheduling, PT booking, equipment maintenance, and retention strategies.",
     ["Membership Agent","Class Scheduler","PT Booking Bot","Equipment Tracker","Retention Engine"],
     ["ClickBank: Fitness Gear|clickbank-analyzer.html","Email: Class Reminders|email-campaigner.html","Lead Magnet: Free Day Pass|lead-magnet-builder.html"],"$49/mo"),

    ("Childcare & Daycare", "👶", "Trained on enrollment management, parent communication, safety compliance, activity planning, and billing.",
     ["Enrollment Agent","Parent Comms Bot","Attendance Tracker","Activity Planner","Billing Manager"],
     ["ClickBank: Parenting Niche|clickbank-analyzer.html","Email: Parent Updates|email-campaigner.html","Lead Magnet: Activity Guide|lead-magnet-builder.html"],"$49/mo"),

    ("Home Services", "🏡", "Trained on scheduling optimization, service area routing, customer communication, and upsell timing for cleaning/HVAC/plumbing.",
     ["Schedule Optimizer","Service Area Router","Customer Comms Bot","Upsell Engine","Review Collector"],
     ["Bridge Page: Local Service|bridge-page-maker.html","Email: Seasonal Reminders|email-campaigner.html","ClickBank: Home Products|clickbank-analyzer.html"],"$49/mo"),

    ("Travel Agencies & Tour Ops", "✈️", "Trained on itinerary planning, booking APIs, destination knowledge, group travel coordination, and travel alerts.",
     ["Itinerary Planner","Booking Bot","Destination Advisor","Group Coordinator","Travel Alert Manager"],
     ["ClickBank: Travel Gear|clickbank-analyzer.html","Bridge Page: Destination Guides|bridge-page-maker.html","Pinterest: Travel Inspiration|pinterest-bot.html"],"$49/mo"),

    ("Biotech & Pharma", "🔬", "Pre-trained on FDA regulations, clinical trial terminology, drug interaction databases, and medical compliance.",
     ["Regulatory Monitor","Trial Data Tracker","Drug Interaction Checker","Compliance Bot","Research Assistant"],
     ["Compliance: FDA/EMA|compliance-checker.html","Trend: Emerging Therapies|trend-detector.html","Email: Research Alerts|email-campaigner.html"],"$149/mo"),

    ("Mobile App Development", "📱", "Trained on SDK integration, crash reporting, user engagement metrics, app store optimization, and CI/CD pipelines.",
     ["Bug Triage Bot","App Store Optimizer","User Engagement Analyzer","SDK Integrator","Release Manager"],
     ["Validate App Idea|product-validator.html","Funnel: Free to Paid App|funnel-builder.html","Retarget: Inactive Users|retargeting-bot.html"],"$79/mo"),

    ("Agriculture & Farming", "🌾", "Trained on crop management, weather patterns, supply chain logistics, equipment maintenance, and subsidy navigation.",
     ["Crop Advisor","Weather Monitor","Supply Chain Bot","Equipment Tracker","Subsidy Navigator"],
     ["ClickBank: Farming Equipment|clickbank-analyzer.html","Email: Market Alerts|email-campaigner.html","Lead Magnet: Subsidy Guide|lead-magnet-builder.html"],"$49/mo"),

    ("Energy & Utilities", "⚡", "Trained on grid management, renewable energy credits, consumption analytics, and regulatory compliance.",
     ["Grid Monitor","Consumption Analyzer","Renewable Credit Tracker","Maintenance Scheduler","Compliance Reporter"],
     ["Trend: Renewable Markets|trend-detector.html","Email: Usage Reports|email-campaigner.html","Compliance: Regs|compliance-checker.html"],"$79/mo"),

    ("Logistics & Supply Chain", "🚚", "Trained on route optimization, warehouse management, inventory forecasting, and carrier coordination.",
     ["Route Optimizer","Warehouse Manager","Inventory Forecaster","Carrier Coordinator","Tracking Agent"],
     ["ClickBank: Logistics Tools|clickbank-analyzer.html","Email: Supply Chain Alerts|email-campaigner.html","Workflow: Fulfillment|workflow-builder.html"],"$79/mo"),

    ("Gaming & Esports", "🎮", "Trained on player engagement, in-game economies, community management, and tournament scheduling.",
     ["Player Support Bot","Community Manager","Tournament Scheduler","Economy Tester","Content Curator"],
     ["ClickBank: Gaming Gear|clickbank-analyzer.html","Bridge Page: Game Reviews|bridge-page-maker.html","Social: Esports Posts|social-scheduler.html"],"$49/mo"),

    ("Film & Media Production", "🎬", "Trained on production scheduling, script coverage, budget management, and distribution channels.",
     ["Production Scheduler","Script Coverage Bot","Budget Tracker","Distribution Coordinator","Crew Manager"],
     ["ClickBank: Filmmaking Tools|clickbank-analyzer.html","Video: Script Generation|video-script-generator.html","Pinterest: Film Boards|pinterest-bot.html"],"$79/mo"),

    ("E-Com Dropshipping", "📦", "Trained on AliExpress/DHGate sourcing, supplier verification, order fulfillment, and customer dispute management.",
     ["Product Sourcer","Supplier Verifier","Order Fulfiller","Dispute Manager","Profit Calculator"],
     ["ClickBank: Dropship Niche|clickbank-analyzer.html","Validate Winning Product|product-validator.html","Email: Abandoned Cart|email-campaigner.html"],"$49/mo"),

    ("Retail & Brick & Mortar", "🏪", "Trained on POS systems, inventory management, foot traffic analytics, local SEO, and loyalty programs.",
     ["POS Assistant","Inventory Manager","Footfall Analyzer","Local SEO Bot","Loyalty Engine"],
     ["Local SEO Optimization|seo-optimizer.html","Email: In-Store Promos|email-campaigner.html","Lead Magnet: Coupon|lead-magnet-builder.html"],"$49/mo"),

    ("K-12 & Schools", "🏫", "Trained on student information systems, parent-teacher communication, curriculum planning, and education regulations.",
     ["Attendance Bot","Parent Comms Bot","Curriculum Planner","Scheduling Agent","Resource Librarian"],
     ["ClickBank: Educational Products|clickbank-analyzer.html","Email: School Newsletters|email-campaigner.html","FERPA Compliance|compliance-checker.html"],"$49/mo"),

    ("Manufacturing & Industrial", "🔧", "Trained on production line monitoring, quality control, safety protocols, and supply chain optimization.",
     ["Production Monitor","Quality Control Bot","Safety Auditor","Supply Chain Optimizer","Maintenance Forecaster"],
     ["Compliance: OSHA/ISO|compliance-checker.html","Trend: Industry 4.0|trend-detector.html","Email: Supply Alerts|email-campaigner.html"],"$79/mo"),

    ("Drone Services & Aerial", "🚁", "Trained on flight planning, airspace regulations, payload specifications, and inspection workflows.",
     ["Flight Planner","Regs Checker","Payload Advisor","Inspection Bot","Data Processor"],
     ["ClickBank: Drone Gear|clickbank-analyzer.html","Bridge Page: Service Areas|bridge-page-maker.html","FAA Compliance|compliance-checker.html"],"$79/mo"),

    ("Web3 & DAOs", "🌐", "Trained on DAO governance, treasury management, smart contract audits, tokenomics design, and community voting.",
     ["Governance Tracker","Treasury Bot","Contract Auditor","Tokenomics Designer","Vote Coordinator"],
     ["ClickBank: Web3 Courses|clickbank-analyzer.html","Bridge Page: Token Analysis|bridge-page-maker.html","Social: Discord/Twitter|social-scheduler.html"],"$79/mo"),

    ("Yoga & Meditation Studios", "🧘", "Trained on class scheduling, teacher management, retreat planning, wellness content, and student progress.",
     ["Class Scheduler","Teacher Manager","Retreat Planner","Wellness Content Bot","Student Tracker"],
     ["ClickBank: Wellness Niche|clickbank-analyzer.html","Email: Class Reminders|email-campaigner.html","Pinterest: Yoga Inspiration|pinterest-bot.html"],"$49/mo"),

    ("Lab & Research Facilities", "🧪", "Trained on lab management, equipment tracking, sample logging, protocol compliance, and results reporting.",
     ["Lab Manager","Equipment Tracker","Sample Logger","Protocol Compliance Bot","Results Reporter"],
     ["Compliance: CLIA/ISO|compliance-checker.html","Email: Result Alerts|email-campaigner.html","Workflow: Sample Pipeline|workflow-builder.html"],"$149/mo"),

    ("Wedding & Event Planning", "💒", "Trained on vendor coordination, budget management, timeline planning, and guest list management.",
     ["Vendor Coordinator","Budget Tracker","Timeline Planner","Guest Manager","Day-Of Assistant"],
     ["ClickBank: Wedding Niche|clickbank-analyzer.html","Email: Vendor Follow-up|email-campaigner.html","Pinterest: Wedding Boards|pinterest-bot.html"],"$49/mo"),

    ("Cybersecurity & IT Security", "🔐", "Trained on threat detection, vulnerability scanning, incident response, and compliance frameworks.",
     ["Threat Detector","Vuln Scanner","Incident Responder","Compliance Auditor","Security Trainer"],
     ["Compliance: SOC2/NIST|compliance-checker.html","Trend: Threat Intel|trend-detector.html","Email: Security Alerts|email-campaigner.html"],"$149/mo"),

    ("RV, Camping & Outdoor", "🧳", "Trained on RV rental workflows, campground booking, outdoor gear knowledge, and trip planning.",
     ["Rental Manager","Campground Bookings","Gear Advisor","Trip Planner","Maintenance Reminder"],
     ["ClickBank: Outdoor Gear|clickbank-analyzer.html","Bridge Page: Trip Reviews|bridge-page-maker.html","Pinterest: Camping Pins|pinterest-bot.html"],"$49/mo"),

    ("Music & Recording Studios", "🎵", "Trained on session booking, equipment inventory, artist management, mixing workflows, and client relationships.",
     ["Session Scheduler","Gear Inventory","Artist Manager","Mixing Assistant","Client CRM Bot"],
     ["ClickBank: Music Gear|clickbank-analyzer.html","Email: Session Confirmations|email-campaigner.html","Lead Magnet: Studio Tour|lead-magnet-builder.html"],"$49/mo"),

    ("Private Aviation & Charter", "🛩️", "Trained on flight scheduling, crew management, fuel planning, maintenance tracking, and client profiles.",
     ["Flight Scheduler","Crew Manager","Fuel Planner","Maintenance Tracker","Client Profile Bot"],
     ["ClickBank: Aviation Products|clickbank-analyzer.html","Email: Charter Reminders|email-campaigner.html","FAA Compliance|compliance-checker.html"],"$149/mo"),

    ("Coworking & Flex Space", "🏢", "Trained on membership management, desk booking, meeting room scheduling, community events, and billing.",
     ["Membership Agent","Desk Booker","Room Scheduler","Event Coordinator","Billing Bot"],
     ["ClickBank: Office Supplies|clickbank-analyzer.html","Email: Membership Renewals|email-campaigner.html","Lead Magnet: Free Day Pass|lead-magnet-builder.html"],"$49/mo"),
]

def make_card(icon, title, tagline, bots, tools, price):
    bots_html = "".join(f'<span>{b}</span>' for b in bots)
    tools_html = "".join(f'<a href="/products/{u}">\u2192 {l}</a>' for l,u in (t.split("|") for t in tools))
    return f'''
<div class="industry-card" data-industry="{title.lower()}">
<div class="icon">{icon}</div>
<h3>{title}</h3>
<div class="tagline">{tagline}</div>
<div class="bot-list">{bots_html}</div>
<div class="affiliate-tools">
<div class="title">\U0001f4c8 Affiliate Toolkits</div>
{tools_html}
</div>
<div class="price">{price}</div>
<div class="team-badge">\U0001f464 Manager + 3 Specialists <span>\u2726</span> 24/7 Operation</div>
</div>'''

cards_html = "\n".join(make_card(*i) for i in industries)

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Industry Hub \u2014 50 Pre-Trained Quantum Bots | Quantum Bots Agency</title>
<meta name="description" content="50 industries. Pre-trained, deploy-ready AI agents for every sector. Full management team included. Affiliate toolkits built-in. 24/7 operation. Zero setup.">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#0a0a12;color:#fff;font-family:'Inter',system-ui,-apple-system,sans-serif;min-height:100vh}}
a{{color:inherit;text-decoration:none}}
.container{{max-width:1200px;margin:0 auto;padding:0 16px}}
header{{background:linear-gradient(180deg,#0f0f1a,rgba(15,15,26,0.8),transparent);position:sticky;top:0;z-index:100;backdrop-filter:blur(10px);border-bottom:1px solid rgba(255,255,255,.05)}}
header .container{{display:flex;align-items:center;justify-content:space-between;padding:14px 16px}}
header h1{{font-size:16px;font-weight:700;background:linear-gradient(135deg,#22d3ee,#3b82f6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}}
nav a{{font-size:12px;color:#94a3b8;margin-left:20px;transition:color .2s;letter-spacing:.5px}}
nav a:hover{{color:#22d3ee}}
.hero{{text-align:center;padding:60px 16px 40px}}
.hero .pill{{display:inline-block;font-size:10px;color:#22d3ee;background:rgba(34,211,238,.08);border:1px solid rgba(34,211,238,.15);border-radius:100px;padding:4px 14px;margin-bottom:16px;letter-spacing:1px;text-transform:uppercase}}
.hero h2{{font-size:36px;font-weight:800;line-height:1.15;margin-bottom:12px;letter-spacing:-1px}}
.hero h2 span{{background:linear-gradient(135deg,#22d3ee,#f59e0b);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}}
.hero p{{color:#94a3b8;font-size:14px;max-width:600px;margin:0 auto 20px;line-height:1.7}}
.hero .stats{{display:flex;gap:24px;justify-content:center;flex-wrap:wrap;margin-top:24px}}
.hero .stat{{text-align:center}}
.hero .stat-num{{font-size:28px;font-weight:800;color:#22d3ee}}
.hero .stat-lbl{{font-size:10px;color:#555;letter-spacing:1px;text-transform:uppercase}}
.search-bar{{max-width:500px;margin:0 auto 24px}}
.search-bar input{{width:100%;padding:12px 16px;background:#0f0f1a;border:1px solid #1a1a2e;border-radius:12px;color:#fff;font-size:13px;outline:none}}
.search-bar input:focus{{border-color:#22d3ee}}
.search-bar input::placeholder{{color:#555}}
.category-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px;padding:0 16px 60px;max-width:1200px;margin:0 auto}}
.industry-card{{background:linear-gradient(135deg,#0f0f1a,#15152a);border:1px solid #1a1a2e;border-radius:16px;padding:20px;transition:all .3s ease;position:relative;overflow:hidden}}
.industry-card:hover{{border-color:#22d3ee44;transform:translateY(-2px);box-shadow:0 8px 32px rgba(34,211,238,.06)}}
.industry-card .icon{{font-size:28px;margin-bottom:8px}}
.industry-card h3{{font-size:15px;font-weight:600;margin-bottom:4px}}
.industry-card .tagline{{color:#94a3b8;font-size:11px;margin-bottom:12px;line-height:1.5}}
.industry-card .bot-list{{display:flex;flex-wrap:wrap;gap:4px;margin-bottom:12px}}
.industry-card .bot-list span{{font-size:9px;padding:2px 8px;border-radius:100px;background:rgba(34,211,238,.06);border:1px solid rgba(34,211,238,.1);color:#22d3ee;letter-spacing:.3px}}
.industry-card .affiliate-tools{{margin-top:8px;padding-top:8px;border-top:1px solid #1a1a2e}}
.industry-card .affiliate-tools .title{{font-size:9px;color:#f59e0b;text-transform:uppercase;letter-spacing:1px;margin-bottom:4px;font-weight:600}}
.industry-card .affiliate-tools a{{display:block;font-size:10px;color:#94a3b8;padding:2px 0;transition:color .2s}}
.industry-card .affiliate-tools a:hover{{color:#f59e0b}}
.industry-card .price{{position:absolute;top:16px;right:16px;font-size:11px;color:#22d3ee;font-weight:600;background:rgba(34,211,238,.08);border:1px solid rgba(34,211,238,.15);padding:2px 10px;border-radius:100px}}
.industry-card .team-badge{{font-size:8px;color:#555;letter-spacing:.5px;margin-top:6px}}
.industry-card .team-badge span{{color:#f59e0b}}
.cta-section{{text-align:center;padding:60px 16px;background:linear-gradient(180deg,transparent,#0a0a12)}}
.cta-section h2{{font-size:24px;font-weight:700;margin-bottom:10px}}
.cta-section p{{color:#94a3b8;font-size:13px;max-width:500px;margin:0 auto 20px;line-height:1.6}}
.cta-btn{{display:inline-block;background:linear-gradient(135deg,#22d3ee,#3b82f6);color:#000;padding:14px 32px;border-radius:12px;font-weight:700;font-size:14px;transition:transform .2s}}
.cta-btn:hover{{transform:scale(1.02)}}
.tool-grid{{max-width:900px;margin:30px auto;display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px;text-align:left}}
.tool-card{{background:#0f0f1a;border:1px solid #1a1a2e;border-radius:12px;padding:16px}}
.tool-card .label{{font-size:10px;color:#22d3ee;text-transform:uppercase;letter-spacing:1px;margin-bottom:6px}}
.tool-card .desc{{font-size:12px;color:#94a3b8;margin-bottom:8px;line-height:1.5}}
.tool-card .link{{font-size:11px;color:#f59e0b}}
.tool-card .link:hover{{text-decoration:underline}}
footer{{text-align:center;padding:30px;color:#333;font-size:10px}}
@media(max-width:640px){{.hero h2{{font-size:26px}}.category-grid{{grid-template-columns:1fr}}}}
</style>
</head>
<body>
<header><div class="container">
<h1>\u269b QBA INDUSTRY HUB</h1>
<nav><a href="/">Marketplace</a><a href="#affiliates">Affiliate Toolkits</a><a href="/products/affiliate-bot.html">Join Affiliates</a></nav>
</div></header>

<section class="hero">
<div class="pill">\u26a1 PRE-TRAINED \u00b7 DEPLOY-READY \u00b7 50 INDUSTRIES</div>
<h2>Deploy a <span>Quantum Bot</span> Trained for Your Industry</h2>
<p>Each bot comes with 200+ hours of industry-specific training data, a full management team (manager + 3 specialists), and pre-built affiliate marketing workflows. Deploy in 47 seconds.</p>
<div class="stats">
<div class="stat"><div class="stat-num">50</div><div class="stat-lbl">Industries Trained</div></div>
<div class="stat"><div class="stat-num">200+</div><div class="stat-lbl">Hours Training Each</div></div>
<div class="stat"><div class="stat-num">4</div><div class="stat-lbl">Agent Team Included</div></div>
<div class="stat"><div class="stat-num">47s</div><div class="stat-lbl">Deploy Time</div></div>
</div>
<div class="search-bar"><input type="text" placeholder="Search your industry..." id="industrySearch" oninput="filterIndustries()"></div>
</section>

<div class="category-grid" id="industryGrid">''' + cards_html + '''
</div>

<section id="affiliates" class="cta-section">
<div class="pill">\u26a1 NICHE TOOLKITS FOR AFFILIATE MARKETERS</div>
<h2>Automated Workflows for Every Niche</h2>
<p>Each toolkit comes pre-configured with ClickBank Gravity analysis, bridge page templates, email sequences, and funnel automations. Deploy in 47s.</p>
<div class="tool-grid">
<div class="tool-card"><div class="label">\U0001f3af Niche Finder Tool</div><div class="desc">Input any category \u2192 AI analyzes Gravity scores, competition, avg payout \u2192 outputs top 10 blue ocean products.</div><a href="/products/niche-finder.html" class="link">\u2192 Deploy Niche Scanner</a></div>
<div class="tool-card"><div class="label">\U0001f504 Bridge Page Automation</div><div class="desc">One click \u2192 AI generates "Top 5" review page, inserts affiliate link, cloaks URL, deploys to your domain.</div><a href="/products/bridge-page-maker.html" class="link">\u2192 Deploy Bridge Builder</a></div>
<div class="tool-card"><div class="label">\U0001f4e7 Affiliate Email Sequences</div><div class="desc">Pre-written 7-email sequences per niche. "Value first" \u2014 3 paragraphs of help before product mention.</div><a href="/products/email-campaigner.html" class="link">\u2192 Deploy Email Engine</a></div>
<div class="tool-card"><div class="label">\U0001f4ca Gravity Analyzer</div><div class="desc">Scans ClickBank in real-time. Filters Gravity 50-200 sweet spot. Sorts by commission payout.</div><a href="/products/clickbank-analyzer.html" class="link">\u2192 Deploy Gravity Scanner</a></div>
<div class="tool-card"><div class="label">\U0001f4f1 Multi-Platform Stealth Distributor</div><div class="desc">Takes your bridge page \u2192 auto-creates Pinterest pins, Quora answers, YouTube scripts, blog posts. IP rotation.</div><a href="/products/pinterest-bot.html" class="link">\u2192 Deploy Stealth System</a></div>
<div class="tool-card"><