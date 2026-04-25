import json

industries = [
    ("Healthcare & Medical", "🏥", "Pre-trained on HIPAA compliance, medical terminology, patient communication, and healthcare regs.",
     ["Patient Intake","Medical Scheduler","Claims Assistant","Health Writer","Compliance Monitor"],
     ["ClickBank: Health Niche|clickbank-analyzer.html","Bridge Page: Reviews|bridge-page-maker.html","Email: Cure Sequences|email-campaigner.html"],"$49/mo"),
    ("E-Commerce & Retail", "🛒", "Trained on Shopify API, cart recovery, listing SEO, inventory, and multi-channel sales.",
     ["Cart Recovery","Product Lister","Inventory Manager","Review Collector","Cross-Sell Engine"],
     ["Product Validation|product-validator.html","Funnel: Product Launch|funnel-builder.html","Retarget: Cart Abandoners|retargeting-bot.html"],"$49/mo"),
    ("Real Estate & Property", "🏠", "Trained on MLS data, property valuation, buyer qualification, and realtor compliance.",
     ["Lead Qualifier","Property Matcher","Market Analyst","Listing Optimizer","Appt Setter"],
     ["Lead Magnet: Buyer Guides|lead-magnet-builder.html","Niche: Foreclosure|niche-finder.html","Email: Property Alerts|email-campaigner.html"],"$49/mo"),
    ("Legal & Law Firms", "⚖️", "Pre-trained on legal terminology, case management, client intake ethics, and bar compliance.",
     ["Case Intake","Doc Analyzer","Legal Researcher","Contract Reviewer","Appt Manager"],
     ["ClickBank: Legal Templates|clickbank-analyzer.html","Bridge: Free Consult|bridge-page-maker.html","Compliance: ABA Rules|compliance-checker.html"],"$79/mo"),
    ("Finance & Banking", "💰", "Trained on SEC regs, investment terminology, risk assessment, and advisory compliance.",
     ["Client Onboarding","Market Monitor","Risk Assessor","Compliance Scanner","Portfolio Tracker"],
     ["Trend: Emerging Markets|trend-detector.html","Email: Investment Digest|email-campaigner.html","Lead: Qualified Investors|lead-scorer.html"],"$79/mo"),
    ("SaaS & Software", "💻", "Trained on PLG metrics, churn prediction, API docs, dev relations, and product-led growth.",
     ["Support Engineer","Churn Predictor","Docs Assistant","User Onboarding","Bug Triage"],
     ["Validate Idea|product-validator.html","Funnel: Trial to Paid|funnel-builder.html","CRM: Lead Nurture|crm-automation.html"],"$79/mo"),
    ("Marketing Agencies", "📢", "Trained on campaign management, client reporting, ad APIs (Google/Meta/TikTok).",
     ["Campaign Manager","Report Generator","Ad Optimizer","Client Comms","Social Scheduler"],
     ["Ad Spy: Competitor Intel|ad-spy-tool.html","Social: Content Calendar|social-scheduler.html","Retarget: Rollover|retargeting-bot.html"],"$49/mo"),
    ("Education & E-Learning", "🎓", "Trained on curriculum design, student engagement, assessment, and LMS systems.",
     ["Student Support","Course Recommender","Grading Assistant","Content Tutor","Enrollment Funnel"],
     ["ClickBank: Courses|clickbank-analyzer.html","Email: Course Launch|email-campaigner.html","Funnel: Mini to Paid|funnel-builder.html"],"$49/mo"),
    ("Fitness & Wellness", "💪", "Trained on exercise science, nutrition protocols, client tracking, and memberships.",
     ["Personal Trainer Bot","Nutrition Planner","Progress Tracker","Class Scheduler","Retention Agent"],
     ["ClickBank: Weight Loss|clickbank-analyzer.html","Bridge: Program Reviews|bridge-page-maker.html","Email: 30-Day Challenge|email-campaigner.html"],"$49/mo"),
    ("Dental & Oral Health", "🦷", "Pre-trained on dental procedures, patient education, insurance verification, recall.",
     ["Appt Agent","Insurance Verifier","Recall Engine","Procedure Educator","Review Collector"],
     ["ClickBank: Oral Health|clickbank-analyzer.html","Email: Hygiene Reminder|email-campaigner.html","Lead Magnet: Whitening|lead-magnet-builder.html"],"$49/mo"),
    ("Insurance & Brokerage", "🛡️", "Trained on policy structures, claims processing, risk assessment, and compliance.",
     ["Quote Generator","Claims Bot","Policy Advisor","Risk Assessor","Renewal Agent"],
     ["Compliance: State Regs|compliance-checker.html","Email: Policy Review|email-campaigner.html","Lead: Buyer Intent|lead-scorer.html"],"$79/mo"),
    ("Hospitality & Travel", "🏨", "Trained on booking systems, guest experience, dynamic pricing, and tourism marketing.",
     ["Concierge Bot","Booking Assistant","Review Manager","Revenue Optimizer","Loyalty Engine"],
     ["ClickBank: Travel Gear|clickbank-analyzer.html","Bridge: Destinations|bridge-page-maker.html","Pinterest: Travel Pins|pinterest-bot.html"],"$49/mo"),
    ("Automotive & Dealerships", "🚗", "Trained on vehicle inventory, test drive scheduling, financing, after-sales.",
     ["Sales Assistant","Service Scheduler","Inventory Manager","Finance Bot","Review Collector"],
     ["ClickBank: Auto Accessories|clickbank-analyzer.html","Email: Service Reminder|email-campaigner.html","Lead: Buyer Readiness|lead-scorer.html"],"$49/mo"),
    ("Construction & Contracting", "🏗️", "Trained on project management, bid processing, building codes, subcontractor coordination.",
     ["Project Manager","Bid Evaluator","Safety Auditor","Schedule Optimizer","Supplier Coordinator"],
     ["Bridge: Service Areas|bridge-page-maker.html","Email: Project Updates|email-campaigner.html","Lead Magnet: Estimate|lead-magnet-builder.html"],"$49/mo"),
    ("Restaurants & Food Service", "🍽️", "Trained on POS integration, delivery logistics, reservations, menu optimization.",
     ["Reservation Agent","Order Manager","Inventory Tracker","Menu Optimizer","Review Responder"],
     ["ClickBank: Kitchen Gadgets|clickbank-analyzer.html","Pinterest: Recipe Traffic|pinterest-bot.html","Email: Loyalty Program|email-campaigner.html"],"$49/mo"),
    ("Beauty & Cosmetics", "💄", "Trained on product formulations, skin types, color matching, salon booking, influencers.",
     ["Product Advisor","Booking Agent","Skin Analyzer","Influencer Matcher","Loyalty Engine"],
     ["ClickBank: Beauty Niche|clickbank-analyzer.html","Bridge: Product Reviews|bridge-page-maker.html","Pinterest: Tutorial Pins|pinterest-bot.html"],"$49/mo"),
    ("Salon, Nail & Barbershop", "💅", "Features Jeannie Nails Academy integration. Salon booking, menu, retail cross-sell, retention.",
     ["Booking Manager","Service Advisor","Retail Cross-Seller","Recall Engine","Trainer Agent"],
     ["ClickBank: Salon Products|clickbank-analyzer.html","Email: Appt + Upsell|email-campaigner.html","Bridge: Salon Reviews|bridge-page-maker.html"],"$49/mo"),
    ("Pet Care & Veterinary", "🐾", "Trained on pet health, grooming, appointments, prescriptions, and product knowledge.",
     ["Grooming Scheduler","Health Advisor","Appt Agent","Product Recommender","Refill Reminder"],
     ["ClickBank: Pet Products|clickbank-analyzer.html","Email: Pet Care Tips|email-campaigner.html","Pinterest: Pet Traffic|pinterest-bot.html"],"$49/mo"),
    ("Accounting & Bookkeeping", "📊", "Trained on GAAP, tax codes, invoicing, payroll, and audit preparation.",
     ["Invoice Bot","Expense Tracker","Tax Preparer","Payroll Agent","Audit Assistant"],
     ["ClickBank: Software|clickbank-analyzer.html","Email: Tax Reminders|email-campaigner.html","Compliance: GAAP/IRS|compliance-scanner.html"],"$79/mo"),
    ("HR & Recruiting", "👔", "Trained on ATS integration, resume parsing, interview scheduling, onboarding, labor law.",
     ["Resume Screener","Interview Scheduler","Onboarding Agent","Compliance Checker","Perf Tracker"],
     ["ClickBank: Career Products|clickbank-analyzer.html","Email: Candidate Nurture|email-campaigner.html","Funnel: Job Board|funnel-builder.html"],"$79/mo"),
    ("Photography & Videography", "📸", "Trained on booking, portfolio management, client proofing, equipment, editing.",
     ["Booking Agent","Gallery Curator","Client Comms Bot","Equipment Advisor","Review Collector"],
     ["ClickBank: Camera Gear|clickbank-analyzer.html","Video: Script Generation|video-script-generator.html","Pinterest: Portfolio|pinterest-bot.html"],"$49/mo"),
    ("Nonprofit & NGOs", "🌍", "Trained on donor management, grant writing, fundraising campaigns, volunteer coordination.",
     ["Donor Engagement","Grant Writer","Volunteer Coordinator","Campaign Analyst","Impact Reporter"],
     ["Email: Donor Nurture|email-campaigner.html","Lead Magnet: Reports|lead-magnet-builder.html","Funnel: Monthly Donor|funnel-builder.html"],"$49/mo"),
    ("Fintech, Crypto & Blockchain", "🪙", "Trained on DeFi, XRPL/XRP, smart contracts, wallets, and crypto compliance.",
     ["Wallet Assistant","Market Analyzer","Smart Contract Tester","DeFi Strategist","Compliance Scanner"],
     ["ClickBank: Crypto Courses|clickbank-analyzer.html","Bridge: Token Reviews|bridge-page-maker.html","Social: XRP/Twitter|social-scheduler.html"],"$79/mo"),
    ("Consulting & Coaching", "🧠", "Trained on engagement frameworks, client intake, proposals, billing, thought leadership.",
     ["Client Intake","Proposal Generator","Engagement Tracker","Billing Bot","Content Publisher"],
     ["ClickBank: Coaching|clickbank-analyzer.html","Email: Discovery Sequence|email-campaigner.html","Funnel: Free Call to Paid|funnel-builder.html"],"$79/mo"),
    ("Holistic Health & Alt Med", "🌿", "Pre-trained on herbal remedies, supplement interactions, holistic protocols, naturopathic.",
     ["Remedy Advisor","Supplement Checker","Protocol Builder","Contraindicator","Content Creator"],
     ["ClickBank: Alt Health|clickbank-analyzer.html","Bridge: Remedy Reviews|bridge-page-maker.html","Email: Wellness Sequence|email-campaigner.html"],"$49/mo"),
    ("Gyms & Fitness Centers", "🏋️", "Trained on memberships, class scheduling, PT booking, equipment, retention.",
     ["Membership Agent","Class Scheduler","PT Booking Bot","Equipment Tracker","Retention Engine"],
     ["ClickBank: Fitness Gear|clickbank-analyzer.html","Email: Class Reminders|email-campaigner.html","Lead Magnet: Free Pass|lead-magnet-builder.html"],"$49/mo"),
    ("Childcare & Daycare", "👶", "Trained on enrollment, parent communication, safety compliance, activity planning, billing.",
     ["Enrollment Agent","Parent Comms Bot","Attendance Tracker","Activity Planner","Billing Manager"],
     ["ClickBank: Parenting|clickbank-analyzer.html","Email: Parent Updates|email-campaigner.html","Lead Magnet: Guide|lead-magnet-builder.html"],"$49/mo"),
    ("Home Services", "🏡", "Trained on scheduling optimization, routing, customer communication, and upsell timing.",
     ["Schedule Optimizer","Service Router","Customer Comms","Upsell Engine","Review Collector"],
     ["Bridge: Local Service|bridge-page-maker.html","Email: Seasonal Reminders|email-campaigner.html","ClickBank: Home Products|clickbank-analyzer.html"],"$49/mo"),
    ("Travel Agencies & Tour Ops", "✈️", "Trained on itinerary planning, booking APIs, destination knowledge, group travel.",
     ["Itinerary Planner","Booking Bot","Destination Advisor","Group Coordinator","Travel Alert Manager"],
     ["ClickBank: Travel Gear|clickbank-analyzer.html","Bridge: Destinations|bridge-page-maker.html","Pinterest: Inspiration|pinterest-bot.html"],"$49/mo"),
    ("Biotech & Pharmaceuticals", "🔬", "Pre-trained on FDA regs, clinical trials, drug interactions, and medical compliance.",
     ["Regulatory Monitor","Trial Data Tracker","Drug Interaction Checker","Compliance Bot","Research Assistant"],
     ["Compliance: FDA/EMA|compliance-checker.html","Trend: Therapies|trend-detector.html","Email: Research Alerts|email-campaigner.html"],"$149/mo"),
    ("Mobile App Development", "📱", "Trained on SDK integration, crash reporting, engagement metrics, ASO, CI/CD.",
     ["Bug Triage Bot","App Store Optimizer","Engagement Analyzer","SDK Integrator","Release Manager"],
     ["Validate App Idea|product-validator.html","Funnel: Free to Paid|funnel-builder.html","Retarget: Inactive|retargeting-bot.html"],"$79/mo"),
    ("Agriculture & Farming", "🌾", "Trained on crop management, weather, supply chain logistics, equipment, subsidies.",
     ["Crop Advisor","Weather Monitor","Supply Chain Bot","Equipment Tracker","Subsidy Navigator"],
     ["ClickBank: Farming Equipment|clickbank-analyzer.html","Email: Market Alerts|email-campaigner.html","Lead Magnet: Subsidy Guide|lead-magnet-builder.html"],"$49/mo"),
    ("Energy & Utilities", "⚡", "Trained on grid management, renewable credits, consumption analytics, and reg compliance.",
     ["Grid Monitor","Consumption Analyzer","Renewable Credit Tracker","Maintenance Scheduler","Compliance Reporter"],
     ["Trend: Renewables|trend-detector.html","Email: Usage Reports|email-campaigner.html","Compliance: Regs|compliance-checker.html"],"$79/mo"),
    ("Logistics & Supply Chain", "🚚", "Trained on route optimization, warehouse management, inventory forecasting, carrier coord.",
     ["Route Optimizer","Warehouse Manager","Inventory Forecaster","Carrier Coordinator","Tracking Agent"],
     ["ClickBank: Logistics Tools|clickbank-analyzer.html","Email: Supply Alerts|email-campaigner.html","Workflow: Fulfillment|workflow-builder.html"],"$79/mo"),
    ("Gaming & Esports", "🎮", "Trained on player engagement, in-game economies, community management, tournaments.",
     ["Player Support","Community Manager","Tournament Scheduler","Economy Tester","Content Curator"],
     ["ClickBank: Gaming Gear|clickbank-analyzer.html","Bridge: Game Reviews|bridge-page-maker.html","Social: Esports Posts|social-scheduler.html"],"$49/mo"),
    ("Film & Media Production", "🎬", "Trained on production scheduling, script coverage, budget management, distribution.",
     ["Production Scheduler","Script Coverage Bot","Budget Tracker","Distribution Coord","Crew Manager"],
     ["ClickBank: Filmmaking|clickbank-analyzer.html","Video: Script Gen|video-script-generator.html","Pinterest: Film Boards|pinterest-bot.html"],"$79/mo"),
    ("E-Com Dropshipping", "📦", "Trained on AliExpress sourcing, supplier verification, order fulfillment, disputes.",
     ["Product Sourcer","Supplier Verifier","Order Fulfiller","Dispute Manager","Profit Calculator"],
     ["ClickBank: Dropship|clickbank-analyzer.html","Validate Product|product-validator.html","Email: Abandoned Cart|email-campaigner.html"],"$49/mo"),
    ("Retail & Brick & Mortar", "🏪", "Trained on POS systems, inventory, foot traffic analytics, local SEO, loyalty.",
     ["POS Assistant","Inventory Manager","Footfall Analyzer","Local SEO Bot","Loyalty Engine"],
     ["Local SEO|seo-optimizer.html","Email: In-Store Promos|email-campaigner.html","Lead Magnet: Coupon|lead-magnet-builder.html"],"$49/mo"),
    ("K-12 & Schools", "🏫", "Trained on student information systems, parent-teacher communication, curriculum, regulations.",
     ["Attendance Bot","Parent Comms Bot","Curriculum Planner","Scheduling Agent","Resource Librarian"],
     ["ClickBank: Educational|clickbank-analyzer.html","Email: Newsletters|email-campaigner.html","FERPA Compliance|compliance-checker.html"],"$49/mo"),
    ("Manufacturing & Industrial", "🔧", "Trained on production monitoring, quality control, safety protocols, supply chain.",
     ["Production Monitor","QC Bot","Safety Auditor","Supply Optimizer","Maint Forecaster"],
     ["Compliance: OSHA/ISO|compliance-checker.html","Trend: Industry 4.0|trend-detector.html","Email: Supply Alerts|email-campaigner.html"],"$79/mo"),
    ("Drone Services & Aerial", "🚁", "Trained on flight planning, airspace regs, payload specs, inspection workflows.",
     ["Flight Planner","Regs Checker","Payload Advisor","Inspection Bot","Data Processor"],
     ["ClickBank: Drone Gear|clickbank-analyzer.html","Bridge: Service Areas|bridge-page-maker.html","FAA Compliance|compliance-checker.html"],"$79/mo"),
    ("Web3 & DAOs", "🌐", "Trained on DAO governance, treasury management, contract audits, tokenomics, voting.",
     ["Governance Tracker","Treasury Bot","Contract Auditor","Tokenomics Designer","Vote Coordinator"],
     ["ClickBank: Web3 Courses|clickbank-analyzer.html","Bridge: Token Analysis|bridge-page-maker.html","Social: Discord/Twitter|social-scheduler.html"],"$79/mo"),
    ("Yoga & Meditation Studios", "🧘", "Trained on class scheduling, teacher management, retreat planning, wellness content.",
     ["Class Scheduler","Teacher Manager","Retreat Planner","Wellness Bot","Student Tracker"],
     ["ClickBank: Wellness|clickbank-analyzer.html","Email: Class Reminders|email-campaigner.html","Pinterest: Yoga|pinterest-bot.html"],"$49/mo"),
    ("Lab & Research Facilities", "🧪", "Trained on lab management, equipment tracking, sample logging, protocol compliance.",
     ["Lab Manager","Equipment Tracker","Sample Logger","Protocol Bot","Results Reporter"],
     ["Compliance: CLIA/ISO|compliance-checker.html","Email: Result Alerts|email-campaigner.html","Workflow: Sample Pipeline|workflow-builder.html"],"$149/mo"),
    ("Wedding & Event Planning", "💒", "Trained on vendor coordination, budget management, timeline planning, guests.",
     ["Vendor Coordinator","Budget Tracker","Timeline Planner","Guest Manager","Day-Of Assistant"],
     ["ClickBank: Wedding Niche|clickbank-analyzer.html","Email: Vendor Follow-up|email-campaigner.html","Pinterest: Wedding Boards|pinterest-bot.html"],"$49/mo"),
    ("Cybersecurity & IT Security", "🔐", "Trained on threat detection, vulnerability scanning, incident response, frameworks.",
     ["Threat Detector","Vuln Scanner","Incident Responder","Compliance Auditor","Security Trainer"],
     ["Compliance: SOC2/NIST|compliance-checker.html","Trend: Threat Intel|trend-detector.html","Email: Security Alerts|email-campaigner.html"],"$149/mo"),
    ("RV, Camping & Outdoor", "🧳", "Trained on RV rental workflows, campground booking, outdoor gear, trip planning.",
     ["Rental Manager","Campground Booking","Gear Advisor","Trip Planner","Maint Reminder"],
     ["ClickBank: Outdoor Gear|clickbank-analyzer.html","Bridge: Trip Reviews|bridge-page-maker.html","Pinterest: Camping|pinterest-bot.html"],"$49/mo"),
    ("Music & Recording Studios", "🎵", "Trained on session booking, equipment inventory, artist management, mixing.",
     ["Session Scheduler","Gear Inventory","Artist Manager","Mixing Assistant","Client CRM"],
     ["ClickBank: Music Gear|clickbank-analyzer.html","Email: Confirmations|email-campaigner.html","Lead Magnet: Studio|lead-magnet-builder.html"],"$49/mo"),
    ("Private Aviation & Charter", "🛩️", "Trained on flight scheduling, crew management, fuel planning, maintenance, profiles.",
     ["Flight Scheduler","Crew Manager","Fuel Planner","Maint Tracker","Client Profile Bot"],
     ["ClickBank: Aviation|clickbank-analyzer.html","Email: Charter Reminders|email-campaigner.html","FAA Compliance|compliance-checker.html"],"$149/mo"),
    ("Coworking & Flex Space", "🏢", "Trained on membership management, desk booking, room scheduling, events, billing.",
     ["Membership Agent","Desk Booker","Room Scheduler","Event Coordinator","Billing Bot"],
     ["ClickBank: Office Supplies|clickbank-analyzer.html","Email: Renewals|email-campaigner.html","Lead Magnet: Free Pass|lead-magnet-builder.html"],"$49/mo"),
]

def card(title, icon, tagline, bots, tools, price):
    b = "".join(f'<span>{x}</span>' for x in bots)
    t = "".join(f'<a href="/products/{u}">{l}</a>' for l,u in (x.split("|") for x in tools))
    return f'''<div class="ic" data-i="{title.lower()}"><div class="ico">{icon}</div><h3>{title}</h3><div class="tg">{tagline}</div><div class="bl">{b}</div><div class="at"><div class="atl">Affiliate Toolkits</div>{t}</div><div class="pr">{price}</div><div class="tb">Manager + 3 Specialists  24/7</div></div>'''

cards = "\n".join(card(*i) for i in industries)

# Read the full template and inject
parts = []
parts.append("""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>Industry Hub - 50 Pre-Trained Quantum Bots | QBA</title><meta name="description" content="50 industries. Pre-trained, deploy-ready AI agents for every sector. Full management team + affiliate toolkits.">
<style>
*{margin:0;padding:0;box-sizing:border-box}body{background:#0a0a12;color:#fff;font-family:Inter,system-ui,sans-serif}a{color:inherit;text-decoration:none}.c{max-width:1200px;margin:0 auto;padding:0 16px}
header{background:linear-gradient(180deg,#0f0f1a,rgba(15,15,26,.8),transparent);position:sticky;top:0;z-index:100;backdrop-filter:blur(10px);border-bottom:1px solid rgba(255,255,255,.05)}
header .c{display:flex;align-items:center;justify-content:space-between;padding:14px 16px}
header h1{font-size:16px;font-weight:700;background:linear-gradient(135deg,#22d3ee,#3b82f6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
nav a{font-size:12px;color:#94a3b8;margin-left:20px;transition:color .2s;letter-spacing:.5px}
nav a:hover{color:#22d3ee}
.hero{text-align:center;padding:60px 16px 40px}
.pill{display:inline-block;font-size:10px;color:#22d3ee;background:rgba(34,211,238,.08);border:1px solid rgba(34,211,238,.15);border-radius:100px;padding:4px 14px;margin-bottom:16px;letter-spacing:1px;text-transform:uppercase}
.hero h2{font-size:36px;font-weight:800;line-height:1.15;margin-bottom:12px;letter-spacing:-1px}
.hero h2 span{background:linear-gradient(135deg,#22d3ee,#f59e0b);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.hero p{color:#94a3b8;font-size:14px;max-width:600px;margin:0 auto 20px;line-height:1.7}
.stats{display:flex;gap:24px;justify-content:center;flex-wrap:wrap;margin-top:24px}
.stat{text-align:center}.stat-num{font-size:28px;font-weight:800;color:#22d3ee}.stat-lbl{font-size:10px;color:#555;letter-spacing:1px;text-transform:uppercase}
.srch{max-width:500px;margin:0 auto 24px}.srch input{width:100%;padding:12px 16px;background:#0f0f1a;border:1px solid #1a1a2e;border-radius:12px;color:#fff;font-size:13px;outline:none}
.srch input:focus{border-color:#22d3ee}.srch input::placeholder{color:#555}
.grd{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px;padding:0 16px 60px;max-width:1200px;margin:0 auto}
.ic{background:linear-gradient(135deg,#0f0f1a,#15152a);border:1px solid #1a1a2e;border-radius:16px;padding:20px;transition:all .3s ease;position:relative;overflow:hidden}
.ic:hover{border-color:#22d3ee44;transform:translateY(-2px);box-shadow:0 8px 32px rgba(34,211,238,.06)}
.ico{font-size:28px;margin-bottom:8px}.ic h3{font-size:15px;font-weight:600;margin-bottom:4px}
.tg{color:#94a3b8;font-size:11px;margin-bottom:12px;line-height:1.5}
.bl{display:flex;flex-wrap:wrap;gap:4px;margin-bottom:12px}
.bl span{font-size:9px;padding:2px 8px;border-radius:100px;background:rgba(34,211,238,.06);border:1px solid rgba(34,211,238,.1);color:#22d3ee;letter-spacing:.3px}
.at{margin-top:8px;padding-top:8px;border-top:1px solid #1a1a2e}
.atl{font-size:9px;color:#f59e0b;text-transform:uppercase;letter-spacing:1px;margin-bottom:4px;font-weight:600}
.at a{display:block;font-size:10px;color:#94a3b8;padding:2px 0;transition:color .2s}.at a:hover{color:#f59e0b}
.pr{position:absolute;top:16px;right:16px;font-size:11px;color:#22d3ee;font-weight:600;background:rgba(34,211,238,.08);border:1px solid rgba(34,211,238,.15);padding:2px 10px;border-radius:100px}
.tb{font-size:8px;color:#555;letter-spacing:.5px;margin-top:6px}
.cta{text-align:center;padding:60px 16px;background:linear-gradient(180deg,transparent,#0a0a12)}
.cta h2{font-size:24px;font-weight:700;margin-bottom:10px}
.cta p{color:#94a3b8;font-size:13px;max-width:500px;margin:0 auto 20px;line-height:1.6}
.cbtn{display:inline-block;background:linear-gradient(135deg,#22d3ee,#3b82f6);color:#000;padding:14px 32px;border-radius:12px;font-weight:700;font-size:14px;transition:transform .2s}
.cbtn:hover{transform:scale(1.02)}
.tgrd{max-width:900px;margin:30px auto;display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px;text-align:left}
.tc{background:#0f0f1a;border:1px solid #1a1a2e;border-radius:12px;padding:16px}
.tc .l{font-size:10px;color:#22d3ee;text-transform:uppercase;letter-spacing:1px;margin-bottom:6px}
.tc .d{font-size:12px;color:#94a3b8;margin-bottom:8px;line-height:1.5}
.tc .lk{font-size:11px;color:#f59e0b}.tc .lk:hover{text-decoration:underline}
footer{text-align:center;padding:30px;color:#333;font-size:10px}
@media(max-width:640px){.hero h2{font-size:26px}.grd{grid-template-columns:1fr}}
</style></head><body>
<header><div class="c"><h1>QBA INDUSTRY HUB</h1><nav><a href="/">Marketplace</a><a href="#affiliates">Affiliate Toolkits</a><a href="/products/affiliate-bot.html">Join</a></nav></div></header>
<section class="hero"><div class="pill">PRE-TRAINED  DEPLOY-READY  50 INDUSTRIES</div><h2>Deploy a <span>Quantum Bot</span> Trained for Your Industry</h2><p>Each bot comes with 200+ hours of industry-specific training, a full management team (manager + 3 specialists), and pre-built affiliate marketing workflows. Deploy in 47 seconds.</p>
<div class="stats"><div class="stat"><div class="stat-num">50</div><div class="stat-lbl">Industries</div></div><div class="stat"><div class="stat-num">200+</div><div class="stat-lbl">Training Hours</div></div><div class="stat"><div class="stat-num">4</div><div class="stat-lbl">Agent Team</div></div><div class="stat"><div class="stat-num">47s</div><div class="stat-lbl">Deploy Time</div></div></div>
<div class="srch"><input type="text" placeholder="Search your industry..." id="s" oninput="f()"></div></section>
<div class="grd" id="g">""")

parts.append(cards)
parts.append("""</div>
<section id="affiliates" class="cta"><div class="pill">AFFILIATE TOOLKITS FOR EVERY NICHE</div><h2>Automated Workflows Built for Affiliate Marketers</h2><p>Each toolkit comes with ClickBank Gravity analysis, bridge page templates, email sequences, and funnel automations pre-configured for your niche.</p>
<div class="tgrd">
<div class="tc"><div class="l">Niche Finder Tool</div><div class="d">Input any category - AI analyzes Gravity scores, competition, avg payout - outputs top 10 blue ocean products.</div><a href="/products/niche-finder.html" class="lk">Deploy Niche Scanner</a></div>
<div class="tc"><div class="l">Bridge Page Automation</div><div class="d">One click - AI generates Top 5 review page, inserts affiliate link, cloaks URL, deploys to your domain. Repeat for next product.</div><a href="/products/bridge-page-maker.html" class="lk">Deploy Bridge Builder</a></div>
<div class="tc"><div class="l">Affiliate Email Sequences</div><div class="d">Pre-written 7-email sequences for every niche. Value First structure - 3 paragraphs of help before product mention. Compliance-checked.</div><a href="/products/email-campaigner.html" class="lk">Deploy Email Engine</a></div>
<div class="tc"><div class="l">Gravity Analyzer</div><div class="d">Scans ClickBank marketplace in real-time. Filters Gravity 50-200 sweet spot. Sorts by commission payout. Outputs ready-to-promote list.</div><a href="/products/clickbank-analyzer.html" class="lk">Deploy Gravity Scanner</a></div>
<div class="tc"><div class="l">Multi-Platform Stealth Distributor</div><div class="d">Takes your bridge page - auto-creates Pinterest pins, Quora answers, YouTube scripts, blog posts. Rotates IPs, value-first content, cloaked links.</div><a href="/products/pinterest-bot.html" class="lk">Deploy Stealth System</a></div>
<div class="tc"><div class="l">Affiliate Funnel Builder</div><div class="d">Complete 3-step funnel: Lead magnet - Email nurture - Bridge page - ClickBank checkout. Pre-tested for every niche. 5 min setup.</div><a href="/products/funnel-builder.html" class="lk">Deploy Funnel Engine</a></div>
</div></section>
<footer>Quantum Bots Agency - Industry Hub - 50 Pre-Trained Bots</footer>
<script>
function f(){const v=document.getElementById('s').value.toLowerCase();document.querySelectorAll('.ic').forEach(c=>{c.style.display=c.dataset.i.includes(v)||!v?'':'none'})}
</script>
</body></html>""")

with open('index.html','w') as f:
    f.write("\n".join(parts))

print(f"Wrote {len(parts)} parts, total {sum(len(p) for p in parts)} bytes")
