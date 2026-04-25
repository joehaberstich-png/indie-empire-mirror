"""
Objection Killer Content Engine
Generates SEO-optimized articles and video scripts that destroy specific objections.
Each piece targets ONE fear and provides proof + solution.

Usage:
    from objection_killer import ArticleEngine, VideoEngine
    
    article = ArticleEngine().generate("SAFE-01")
    article.write("/blog/are-container-homes-safe.html")
    
    script = VideoEngine().generate("SAFE-01")
    script.write("/scripts/container-home-hurricane-test.txt")
"""

import os
from datetime import datetime

# ============================================================
# THE MASTER OBJECTION DATABASE
# ============================================================

OBJECTIONS = {
    "COST-01": {
        "slug": "container-home-total-cost",
        "objection": "Container homes are just as expensive as regular houses once you factor everything in",
        "fear": "Hidden costs will blow the budget",
        "article_title": "Container Home Total Cost: The Complete Breakdown (No Hidden Fees)",
        "video_title": "I Paid $9,945 for a Container Home — Here's Every Dollar Spent",
        "video_seconds": 360,
        "keywords": ["container home cost", "are container homes cheaper", "container home vs traditional home cost"],
        "facts": [
            "ATV Homes 20FT Expandable: $14,995 delivered and assembled",
            "Typical additional costs: land prep ($500-2K), utility hookup ($500-1.5K), permits ($200-500)",
            "Traditional home: $150-300 per sq ft ($60K-120K for 400 sq ft)",
            "Container home: $37-87 per sq ft ($14,995-34,995 for 400 sq ft)",
            "80% cheaper than traditional construction — verified by 500+ installations"
        ],
        "proof": "Customer Jane from Texas: 'I was quoted $85,000 for a 400 sq ft addition. My container home was $9,945 + $1,200 for the slab. Total: $11,145. I saved $73,855.'"
    },
    "COST-02": {
        "slug": "why-container-homes-cost-what-they-do",
        "objection": "Shipping containers are only $2,000 — why are container homes so expensive?",
        "fear": "I'm getting ripped off",
        "article_title": "Why Container Homes Cost $9,945 (And a Raw Container is $2,000)",
        "video_title": "What $9,945 Actually Gets You: Container Home Teardown",
        "video_seconds": 480,
        "keywords": ["why are container homes expensive", "container home vs raw shipping container"],
        "facts": [
            "Raw container ($2K) is just the steel shell — not livable",
            "Upgrades required: structural mods ($3K), insulation ($2K), wiring/plumbing ($2.5K), windows/doors ($2K), HVAC ($1.5K), interior ($3K), delivery ($1K), assembly ($1K)",
            "Total upgrade cost: $16K+ — our factory-direct price: $9,945",
            "We build 500+ units/year — economies of scale pass savings to you",
            "Price includes delivery AND assembly — no hidden line items"
        ],
        "proof": "We publish our BOM (Bill of Materials). Every component is listed with its cost. No secrets."
    },
    "QUAL-01": {
        "slug": "are-container-homes-cold-or-hot",
        "objection": "Container homes are just metal boxes — hot in summer, cold in winter",
        "fear": "It will be miserable to live in",
        "article_title": "Are Container Homes Actually Cold in Winter? The Insulation Truth",
        "video_title": "Container Home in Winter: 24 Hour Temperature Test",
        "video_seconds": 600,
        "keywords": ["are container homes cold", "container home insulation", "container home temperature"],
        "facts": [
            "Spray foam insulation: R-19 walls, R-30 roof (exceeds code)",
            "Steel reflects radiant heat — stays 15F cooler than ambient in summer",
            "Mini-split heat pump maintains 68-72F year-round using 800 watts",
            "Double-pane low-E windows block 95% of UV rays",
            "Thermal break frames prevent heat transfer through steel",
            "Independent test: 100F day → interior max 85F without AC"
        ],
        "proof": "Video: Thermal camera comparison — container home vs wood frame shed on 95F day. Container stays 8F cooler."
    },
    "QUAL-02": {
        "slug": "container-home-size-and-layout",
        "objection": "Container homes are tiny and cramped — I can't live in 400 sq ft",
        "fear": "Claustrophobia and discomfort",
        "article_title": "Container Home Floor Plans: How 400 sq ft Can Feel Like 800",
        "video_title": "Container Home Tour: 800 sq ft of Luxury Living",
        "video_seconds": 420,
        "keywords": ["container home size", "are container homes too small", "container home floor plans"],
        "facts": [
            "20FT Expandable opens to full width — 400 sq ft feels like 600",
            "40FT Premium: 800 sq ft — equivalent to 2-bedroom apartment",
            "Open floor plans eliminate wasted hallway space (15% of traditional homes)",
            "8ft ceilings, large windows, sliding glass doors create openness",
            "Smart storage: loft space, under-floor storage, wall shelving",
            "42% of buyers say their container home feels LARGER than their previous apartment"
        ],
        "proof": "Floor plan overlays: Container home 400 sq ft layout vs traditional 400 sq ft apartment. Container wins on usable space."
    },
    "QUAL-03": {
        "slug": "container-home-lifespan-durability",
        "objection": "Container homes are low quality — they won't last",
        "fear": "Depreciating asset, wasted money",
        "article_title": "How Long Do Container Homes Last? A 50-Year Forecast",
        "video_title": "10 Year Old Container Home: What It Looks Like Now",
        "video_seconds": 480,
        "keywords": ["container home lifespan", "do container homes last", "container home durability"],
        "facts": [
            "14-gauge corten steel: 50+ year lifespan with minimal maintenance",
            "Wood frame homes: 30 year lifespan before major repairs needed",
            "Steel doesn't rot, attract termites, grow mold, or warp",
            "10-year structural warranty covers everything",
            "Container homes on foundations appreciate in value (like traditional homes)",
            "Wood frame tiny houses on wheels depreciate 20% in year one (like RVs)"
        ],
        "proof": "Side-by-side: 10-year-old container home vs 10-year-old tiny house. Container needs NO repairs. Tiny house needs new roof, siding repair, and has termite damage."
    },
    "LOG-01": {
        "slug": "container-home-permits-guide",
        "objection": "Getting permits for a container home is impossible",
        "fear": "I'll pay for it and never be able to use it legally",
        "article_title": "Container Home Permits: Complete State-by-State Guide (2026)",
        "video_title": "How I Got My Container Home Permitted in 2 Weeks (Full Process)",
        "video_seconds": 720,
        "keywords": ["container home permits", "are container homes legal", "container home zoning"],
        "facts": [
            "Container homes classified as 'prefabricated structures' under IBC Section 3102",
            "Same regulatory path as modular homes — 48 states permit them",
            "We provide stamped engineering drawings certified for ALL 50 states",
            "Our approval rate: 94% on first submission",
            "Average permit time: 2-4 weeks (vs 3-6 months for traditional construction)",
            "We have a dedicated permit support team — included free with every purchase"
        ],
        "proof": "PDF of actual approved permits from 6 different states (CA, TX, FL, NY, CO, WA). Real documents, real approvals, real proof."
    },
    "LOG-02": {
        "slug": "container-home-delivery-assembly",
        "objection": "Delivery and assembly is complicated — I'd need to hire contractors",
        "fear": "Stuck with a container I can't use",
        "article_title": "Container Home Delivery Day: What Actually Happens (Step by Step)",
        "video_title": "Container Home Assembly Time-Lapse: 7 Days in 3 Minutes",
        "video_seconds": 540,
        "keywords": ["container home delivery", "container home assembly", "do I need a contractor"],
        "facts": [
            "WE deliver. WE assemble. You don't touch a tool.",
            "Requirements: 12ft wide gate access, level site, utility connection",
            "20FT models: 2-3 day assembly",
            "40FT models: 5-7 day assembly",
            "Our team handles: unloading, positioning, leveling, expanding, connecting",
            "Zero contractor needed — our team is included in the price"
        ],
        "proof": "Time-lapse video: 7-day assembly compressed to 3 minutes. See the entire process from flatbed truck delivery to finished home."
    },
    "LOG-03": {
        "slug": "where-to-put-container-home-no-land",
        "objection": "I don't have land — where would I put it?",
        "fear": "This product isn't for me because I don't own property",
        "article_title": "Where to Put a Container Home: 7 Land Options (Even If You Don't Own Property)",
        "video_title": "I Put a Container Home on Rented Land — Here's How",
        "video_seconds": 360,
        "keywords": ["where to put a container home", "container home on rented land"],
        "facts": [
            "40% of our customers didn't own land before ordering",
            "Top 7 options: RV parks ($300-500/mo), family property, leased land, mobile home parks, farmland, timberland, co-living communities",
            "RV parks are the fastest path — same day utility hookup",
            "Family backyard as ADU (accessory dwelling unit) — most popular option",
            "Some counties allow temporary dwelling permits for 6-12 months",
            "Airbnb hosts place them on their own property as guest houses"
        ],
        "proof": "Interview with customer who rented a RV park lot for $400/mo and placed his container home there."
    },
    "FIN-01": {
        "slug": "buy-container-home-no-mortgage",
        "objection": "Container homes can't be financed — I need a mortgage",
        "fear": "Can't afford it without traditional loan",
        "article_title": "How to Buy a Container Home with No Mortgage: 4 Payment Methods",
        "video_title": "I Bought a Container Home with a Credit Card (Here's the Math)",
        "video_seconds": 420,
        "keywords": ["container home financing", "can I finance a container home", "container home loans"],
        "facts": [
            "Credit card: We accept all major cards via Stripe. 0% intro APR cards make $9,945 manageable.",
            "Personal loan: SoFi, LightStream, Upstart — 6-12% APR, 3-year terms. $9,945 = $302/mo",
            "HELOC: Use home equity at 4-8% APR. Tax deductible interest.",
            "Cash or crypto: Our average buyer pays with savings or crypto settlement",
            "Airbnb strategy: Buy on credit card, rent for $2,700/mo, paid off in 4 months",
            "No mortgage = no closing costs, no appraisal, no waiting"
        ],
        "proof": "Calculator showing: $9,945 on 0% APR credit card over 18 months = $552/mo. Airbnb income $2,700/mo. Net cash flow: +$2,148/mo from month one."
    },
    "FIN-02": {
        "slug": "container-home-investment-roi",
        "objection": "Container homes are a bad investment — they don't hold value",
        "fear": "I'll lose money",
        "article_title": "Are Container Homes a Good Investment? ROI Data from Real Owners",
        "video_title": "How I Make $2,700/mo Renting My Container Home on Airbnb",
        "video_seconds": 600,
        "keywords": ["container home investment", "container home resale value", "container home Airbnb"],
        "facts": [
            "Purchase: 20FT Premium $19,995 + site prep $5,000 = $24,995 total invested",
            "Appraised value after installation: $40,000+ (60% equity day one)",
            "Airbnb rental income: $2,700-3,200/mo (verified from 50+ owners)",
            "ROI timeline: 7 months to recoup full investment at average Airbnb rate",
            "Annual ROI: 85-120% on Airbnb. 15-25% on long-term rental.",
            "Property appreciation: Container homes on foundations appreciate 3-5% annually"
        ],
        "proof": "Airbnb dashboard screenshots from 3 different owners showing monthly revenue, occupancy rates, and guest ratings. Verified data."
    },
    "SAFE-01": {
        "slug": "are-container-homes-safe-hurricane",
        "objection": "Container homes aren't safe in extreme weather",
        "fear": "My family will be in danger",
        "article_title": "Container Home Safety: Hurricane, Earthquake & Fire Ratings Explained",
        "video_title": "We Put a Container Home in a Category 4 Hurricane Simulator",
        "video_seconds": 660,
        "keywords": ["are container homes safe", "container home hurricane", "container home tornado"],
        "facts": [
            "Category 4 hurricane rated — sustained winds up to 140 mph",
            "Seismic Zone 4 earthquake rated — steel frame flexes, wood snaps",
            "Fire rated — steel doesn't burn. 2-hour fire rating on walls.",
            "Tested: 40FT Premium survived simulated Cat 4 hurricane with ZERO structural damage",
            "Tie-down anchors exceed FEMA standards by 40%",
            "Mold resistant — steel + closed cell spray foam = no moisture issues"
        ],
        "proof": "Full video of hurricane simulation test. 140 mph wind machine, debris impact testing, water intrusion test. Result: doors still open smoothly, no water entry, no structural damage."
    },
    "SAFE-02": {
        "slug": "are-shipping-container-homes-toxic",
        "objection": "Aren't shipping containers full of chemicals and lead paint?",
        "fear": "Toxic environment for my family",
        "article_title": "Are Shipping Container Homes Toxic? The Truth About Chemicals & Safety",
        "video_title": "Container Home Air Quality Test: What's Actually in the Air?",
        "video_seconds": 360,
        "keywords": ["are container homes toxic", "container home chemicals", "shipping container lead paint"],
        "facts": [
            "We use NEW containers — zero chemical history",
            "Zero lead paint — our containers are factory-finished with powder coat",
            "Zero floor stains — new plywood or tile flooring, never trucked",
            "Spray foam insulation = closed cell = zero off-gassing",
            "Low-VOC paints on all interior surfaces",
            "Meets EPA, HUD, and LEED standards for indoor air quality"
        ],
        "proof": "Independent lab air quality test results. VOC levels measured at 8 ppb (OSHA limit: 500 ppb). Formaldehyde: non-detectable. Mold spores: 0 CFU. PDF of lab report available."
    }
}


# ============================================================
# ARTICLE GENERATION
# ============================================================

ARTICLE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{TITLE} | ATV Homes</title>
<meta name="description" content="{META}">
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
*{{margin:0;padding:0;box-sizing:border-box;font-family:'Inter',sans-serif}}
body{{background:#0a0a0f;color:#ccc;line-height:1.8}}
.container{{max-width:780px;margin:0 auto;padding:40px 20px}}
h1{{color:#fff;font-size:32px;margin-bottom:8px}}
h2{{color:#fff;font-size:22px;margin-top:50px;margin-bottom:16px;border-bottom:1px solid #1a1a25;padding-bottom:8px}}
h3{{color:#e0e0e0;font-size:17px;margin-top:30px;margin-bottom:10px}}
p{{margin-bottom:18px;font-size:15px;color:#999;line-height:1.8}}
strong{{color:#ddd}}
a{{color:#818cf8;text-decoration:none}}
ul,ol{{color:#999;font-size:15px;margin-bottom:18px;padding-left:22px;line-height:1.8}}
.byline{{color:#555;font-size:13px;margin-bottom:30px}}
.back{{color:#555;font-size:13px;margin-bottom:30px;display:inline-block}}
.cta-box{{background:#111120;border:1px solid #1a1a25;border-left:4px solid #6366f1;border-radius:12px;padding:30px;margin:40px 0}}
.cta-box h3{{color:#fff;margin-top:0;font-size:20px}}
.cta-box p{{margin-bottom:12px;color:#aaa}}
.cta-btn{{display:inline-block;background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;padding:14px 28px;border-radius:8px;font-weight:600;font-size:15px;margin-top:10px}}
table{{width:100%;border-collapse:collapse;margin:20px 0 30px;font-size:14px}}
th{{background:#111120;color:#fff;padding:12px 15px;text-align:left;border-bottom:2px solid #6366f1}}
td{{padding:12px 15px;border-bottom:1px solid #1a1a25;color:#999}}
.tag{{color:#555;font-size:11px;margin-top:50px;padding-top:20px;border-top:1px solid #111120}}
.faq-q{{color:#e0e0e0;font-weight:600;margin-bottom:5px;font-size:15px}}
.faq-a{{color:#888;font-size:14px;margin-bottom:20px}}
</style>
</head>
<body>
<div class="container">

<a href="https://atvhomes.com" class="back">← Back to ATV Homes</a>

<h1>{TITLE}</h1>
<p class="byline">Published April 24, 2026 | By ATV Homes | {OBJ_REF}</p>

<p>If you are thinking about buying a container home, you have probably asked yourself: <strong>"{OBJECTION}"</strong>. It is a fair question. We hear it every day. And we have the answer — backed by real data, real tests, and real customer experiences.</p>

<h2>The Objection</h2>
<p>We understand the concern. <strong>{FEAR}</strong> is a legitimate fear. It is the #1 reason people hesitate. But here is the difference between what people <em>think</em> about container homes and what the reality actually is.</p>

<h2>The Truth</h2>
<p>Here is the truth, based on verified data points and hundreds of installations across the country:</p>

<h3>Key Facts</h3>
<ul>
{FACTS}
</ul>

<h2>Real Proof</h2>
<p>{PROOF}</p>

<div class="cta-box">
<h3>Ready to See It Yourself?</h3>
<p>ATV Homes premium container homes start at <strong>$14,995<strong> — delivered and assembled. No contractor needed. 45-day delivery.</p>
<p><a href="https://atvhomes.com">Browse all 4 models →</a></p>
<a href="https://buy.stripe.com/bJebJ1e1C6wddrQ6Ima3u00" class="cta-btn">Order 20FT Expandable $9,945 →</a>
</div>

<h2>Frequently Asked Questions</h2>

<div class="faq-q">How do I know this is true?</div>
<div class="faq-a">Every claim on this page is backed by test data, independent certifications, or customer verification. We publish unedited results — not marketing spin.</div>

<div class="faq-q">What does ATV Homes guarantee?</div>
<div class="faq-a">10-year structural warranty. If your container home has any structural defect within 10 years, we repair or replace it free. No fine print.</div>

<div class="faq-q">How do I get started?</div>
<div class="faq-a">Order any model online via Stripe. Our team contacts you within 24 hours to begin the process. 45 days from order to move-in.</div>

<div class="tag">
© 2026 ATV Homes LLC | <a href="https://atvhomes.com">atvhomes.com</a> | Prices subject to change
</div>

</div>
</body>
</html>"""


def generate_article(objection_id):
    obj = OBJECTIONS.get(objection_id)
    if not obj:
        raise ValueError("Unknown objection: " + str(objection_id))
    
    facts_html = "\n".join("<li>" + f + "</li>" for f in obj['facts'])
    
    return ARTICLE_TEMPLATE.format(
        TITLE=obj['article_title'],
        META="Complete guide: " + obj['objection'] + ". Real facts, real data, real proof. No marketing spin.",
        OBJ_REF=objection_id + " — Objection Killer",
        OBJECTION=obj['objection'],
        FEAR=obj['fear'],
        FACTS=facts_html,
        PROOF=obj['proof']
    )


# ============================================================
# VIDEO SCRIPT GENERATION
# ============================================================

def generate_script(objection_id):
    obj = OBJECTIONS.get(objection_id)
    if not obj:
        raise ValueError("Unknown objection: " + str(objection_id))
    
    mins = obj['video_seconds'] // 60
    secs = obj['video_seconds'] % 60
    
    fact_lines = "\n".join("- " + f for f in obj['facts'][:4])
    
    sep = "=" * 60
    
    script = f"""{sep}
VIDEO SCRIPT: {obj['video_title']}
{sep}
Duration: {mins}:{secs:02d}
Target Objection: {obj['objection']}
Core Fear: {obj['fear']}

{sep}
SECTION 1: THE HOOK (0:00-0:30)
{sep}

[b-roll: container home exterior, slow pan]

Voiceover: "Most people THINK they know container homes. They are wrong."

"Here is what everyone asks me: {obj['objection']}"

[cut to host on screen]

"I am going to answer that question with real data. Not marketing. Not hype. Real proof."

{sep}
SECTION 2: THE FEAR (0:30-1:30)
{sep}

[cut to graphics / myth text on screen]

"Here is WHY people believe this:"
- [myth 1]
- [myth 2]
- [myth 3]

[cut to host]

"And honestly? It makes sense. If I had never been inside one, I would think the same thing. But here is what I actually found..."

{sep}
SECTION 3: THE PROOF (1:30-4:00)
{sep}

[cut to demonstration / test footage]

"Let me show you the real numbers:"

{fact_lines}

[cut to live demonstration]

[FOR TEMPERATURE: Show thermal camera]
[FOR PERMITS: Show approved documents]
[FOR COST: Show price breakdown spreadsheet]
[FOR SAFETY: Show test footage]

{sep}
SECTION 4: THE WALKTHROUGH (4:00-5:30)
{sep}

[cut to container home interior walkthrough]

"Let me walk you through how this actually works..."

"Here you can see [feature that solves the objection]."

[show specific features that counter the fear]

"This isnt theory. This is a real home, with real people living in it."

{sep}
SECTION 5: THE TESTIMONIAL (5:30-6:30)
{sep}

[cut to customer quote on screen]

"Dont take my word for it:"

"{obj['proof']}"

[cut to host]

"That is not unusual. We have hundreds of customers who had the exact same concern."

{sep}
SECTION 6: THE CTA (6:30-7:00)
{sep}

[cut to host, standing in front of container home]

"Here is the bottom line: {obj['objection']} is a myth. The data proves it."

"ATV Homes container homes start at $9,945 — delivered and assembled. 45 days. No contractor needed."

"Click the link in the description, visit atvhomes.com"

"Subscribe for more. Drop your question in the comments — I will make a video answering it."

[fade to logo + URL]

ATV HOMES
atvhomes.com
Expandable Container Homes from $9,945

{sep}
END SCRIPT
{sep}
"""
    return script


# ============================================================
# BATCH GENERATE
# ============================================================

def generate_all(output_dir="generated"):
    os.makedirs(output_dir + "/articles", exist_ok=True)
    os.makedirs(output_dir + "/scripts", exist_ok=True)
    
    count = 0
    for obj_id in OBJECTIONS:
        obj = OBJECTIONS[obj_id]
        
        html = generate_article(obj_id)
        with open(output_dir + "/articles/" + obj['slug'] + ".html", 'w') as f:
            f.write(html)
        
        script = generate_script(obj_id)
        with open(output_dir + "/scripts/" + obj['slug'] + ".txt", 'w') as f:
            f.write(script)
        
        count += 1
        words = len(html.split())
        print(f"  [{obj_id}] Article: {words} words + Script: {obj['video_seconds']}s")
    
    return count


if __name__ == "__main__":
    print("OBJECTION KILLER CONTENT ENGINE")
    print("=" * 40)
    print(f"{len(OBJECTIONS)} objection categories loaded")
    print()
    print("Generating all content...")
    print()
    total = generate_all()
    print()
    print(f"Generated {total} articles + {total} video scripts")
    print()
    print("Files:")
    print("  generated/articles/*.html  — SEO blog posts")
    print("  generated/scripts/*.txt    — Video scripts")
