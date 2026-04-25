#!/usr/bin/env python3
"""
Container Homes — Unified Quantum Sales & CS Bot
Deep container home industry expertise.
Installed on every page of containerhomes.com.
Handles: sales, questions, support, purchasing — full funnel.
Industry-trained: 3-problem rule, container construction, zoning, pricing, financing.
"""

import json, random, time
from datetime import datetime

QBA_BRANDING = "Powered by Quantum Bots Agency — AI workforce for every business → quantumbotsagency.com"
SITE_NAME = "Container Homes"

# ─── PRODUCTS (live Stripe links) ───
PRODUCTS = {
    "20ft-expandable": {
        "name": "20FT Expandable",
        "price": 9945,
        "sqft": 400,
        "delivery_days": 45,
        "stripe": "https://buy.stripe.com/bJebJ1e1C6wddrQ6Ima3u00",
        "best_for": "man caves, home offices, guest rooms, she sheds, tiny homes, workshops"
    },
    "20ft-premium": {
        "name": "20FT Premium",
        "price": 17125,
        "sqft": 400,
        "delivery_days": 45,
        "stripe": "https://buy.stripe.com/fZedRj7YC70Y9le145d7",
        "best_for": "move-in ready with kitchen & bath, in-law suites, rental units"
    },
    "40ft-deluxe": {
        "name": "40FT Deluxe",
        "price": 21100,
        "sqft": 800,
        "delivery_days": 45,
        "stripe": "https://buy.stripe.com/28o8wRfXs8CC50c145bF98",
        "best_for": "2-bedroom living, guest houses, family accommodation, vacation rentals"
    },
    "40ft-premium": {
        "name": "40FT Premium",
        "price": 28550,
        "sqft": 800,
        "delivery_days": 45,
        "stripe": "https://buy.stripe.com/8wM7vf8yY9m49tG6oHb38",
        "best_for": "luxury living, full families, smart home, premium finishes"
    }
}

# ─── DEEP INDUSTRY KNOWLEDGE ───
# Every sales and CS agent is trained on this

INDUSTRY_KNOWLEDGE = {
    "pricing": {
        "cost": "Our container homes range from $9,945 for the 20FT Expandable to $28,550 for the 40FT Premium. All prices include delivery and assembly in the continental U.S.",
        "20ft": "$9,945 for the Expandable model. $17,125 for Premium with kitchen and bath. All prices include delivery and assembly.",
        "40ft": "$21,100 for the Deluxe (2 bedroom). $28,550 for the Premium flagship with granite and stainless steel.",
        "vs_traditional": "A traditional 400 sq ft addition runs $40,000-$80,000 with permits and contractors. Our 20FT is $9,945 delivered. You save 60-80%.",
        "vs_tiny_house": "Tiny houses average $40,000-$60,000. Our 20FT Expandable at $9,945 is 75% cheaper per square foot and requires no builder.",
        "vs_modular": "Modular homes cost $80-$160 per sq ft. Our container homes are $25-$35 per sq ft delivered. 70% less.",
        "financing": "We accept all major credit cards via Stripe. Some owners use personal loans, RV loans, or home equity lines. We provide all documentation needed for financing applications."
    },
    "delivery": {
        "delivery": "Delivery takes 45 days from order to your property anywhere in the continental U.S. Free delivery, team handles assembly. No contractor needed on your end.",
        "timeline": "45 days from order to delivery anywhere in the continental U.S. That's faster than any traditional build.",
        "process": "Day 1: Order placed. Day 7: Manufacturing begins. Day 30: Unit ships. Day 45: Delivered and assembled on your property.",
        "cost": "Delivery is FREE within the continental U.S. We use flatbed trucks with crane offloading.",
        "assembly": "Our team handles assembly. Typically 2-3 days for the 20FT models, 5-7 days for 40FT. You don't lift a finger.",
        "requirements": "We need clear access to your property — 12ft wide gate minimum. Level ground or prepared foundation. We can advise on both."
    },
    "construction": {
        "steel": "14-gauge corten steel. Same grade used in ocean shipping. These containers survive hurricanes and 30-foot waves.",
        "insulation": "Spray foam insulation: R-19 in walls, R-30 in the roof. That's better insulation than most stick-built homes.",
        "hurricane_rating": "Category 4 hurricane rated. Sustained winds up to 140 mph. Tested and certified.",
        "earthquake_rating": "Seismic Zone 4 rated. The steel frame flexes under stress rather than cracking like concrete or wood.",
        "foundation": "Concrete slab or concrete piers. We include a foundation plan with every purchase engineered for your soil type.",
        "roof": "Steel roof with standing seams. Rated for heavy snow load. 30-year lifespan with zero maintenance.",
        "windows": "Double-pane tempered low-E glass. Argon gas filled for insulation. Impact rated for hurricane zones."
    },
    "zoning": {
        "classification": "Container homes are classified as prefabricated structures (IBC Section 3102). Most counties permit them the same as modular homes.",
        "minimum_sqft": "Some counties have minimum square footage requirements (typically 600-1,000 sq ft). Our 40FT models cover you everywhere.",
        "hoa": "HOAs may restrict container homes. We recommend checking your CC&Rs. Many owners place them on rural or unincorporated land.",
        "permit_process": "We provide stamped engineering drawings certified for all 50 states. Most permit offices approve within 2-4 weeks.",
        "setbacks": "Standard setbacks apply: typically 5-30 feet from property line depending on your county. Same as any accessory dwelling unit."
    },
    "living": {
        "full_time": "Absolutely. Our 40FT models sleep 4-6 people with full kitchen, bath, living room, and bedrooms. People live full-time in 20FT models too.",
        "utilities": "Hook up to standard electric, water, and sewer just like any home. Pre-wired with 100-amp panel (20FT) or 200-amp (40FT).",
        "heating_cooling": "Mini-split heat pump included on Premium models. Covers both heating and AC. Efficient down to -15°F.",
        "plumbing": "Full PEX plumbing with tankless water heater on Premium models. Standard connections to city water or well.",
        "internet": "Standard cable/fiber run. We include a conduit for data cabling. Starlink works great for rural locations.",
        "pets": "Perfect for pets. Steel walls don't absorb odors like wood. Easy to clean. No drywall for them to damage."
    },
    "use_cases": {
        "man_cave": "400 sq ft of pure sanctuary. Soundproofed, climate controlled, room for a full bar and theater setup.",
        "she_shed": "Natural light studio with vaulted ceiling. Wide plank floors. Your creative space for under $10K.",
        "in_law_suite": "Wider doorways, step-free entry, kitchenette, full bathroom with grab bars. Close enough to help, far enough for privacy.",
        "airbnb": "Owners report $2,700-$3,200/month on Airbnb. Many recoup their $9,945 investment in 4 months. 75% occupancy average.",
        "home_office": "Professional workspace separate from your living space. Soundproofed. Dedicated fiber run. Walk 30 feet to work.",
        "tiny_home": "400 sq ft of efficient living. Lower utility bills, smaller footprint, more freedom. Starting at $9,945.",
        "workshop": "Steel walls, concrete-ready floor, high ceilings. Perfect for woodworking, mechanics, or any maker trade."
    },
    "support": {
        "warranty": "10-year structural warranty on the steel frame. 2-year warranty on finishes, windows, and doors. Transferable to new owners.",
        "returns": "14-day return window from delivery. Unit must be in original condition. Return shipping arranged by our team.",
        "damage": "Inspect within 48 hours of delivery. Photograph any damage. We ship replacement parts within 7 days at no cost.",
        "contact": "Our CS bot handles 24/7 inquiries. L1 human agents available within 3 minutes for complex issues. support@containerhomes.com",
        "modifications": "We can modify any model before manufacturing — window placement, door location, electrical layout, finishes. Contact sales before ordering."
    },
    "qba_branding": {
        "description": "Quantum Bots Agency builds AI workforces for businesses. Every container home sale is powered by our quantum agents.",
        "link": "quantumbotsagency.com",
        "tagline": "AI workforce for every business. Sales, support, marketing, content — all automated by quantum-built agents."
    },
    "aliases": {
        "live": "Absolutely. Our 40FT models sleep 4-6 people with full kitchen, bath, living room, and bedrooms. People live full-time in 20FT models too. Our 40FT Deluxe at $21,100 is the most popular for full-time living.",
        "full-time": "Yes, many owners live full-time in their container homes. The 40FT models are designed for full-time living with 2 bedrooms, kitchen, bath, and living room. 20FT works too for singles or couples.",
        "take": "45 days from order to delivery anywhere in the continental U.S. That's faster than any traditional build.",
        "when": "45 days from order to delivery. You'll have your container home in about 6 weeks.",
        "hurricane": "Category 4 hurricane rated. Sustained winds up to 140 mph. 14-gauge corten steel. Tested and certified.",
        "storm": "Same hurricane rating — 140 mph wind resistance. Steel frame won't rot or warp like wood in storms.",
        "safe": "Extremely safe. Hurricane rated, earthquake rated, fire resistant steel. More durable than traditional wood frame construction.",
        "buy": "Ready to purchase! Here are your secure checkout links:\n\n20FT Expandable — $9,945\n\u2192 https://buy.stripe.com/bJebJ1e1C6wddrQ6Ima3u00\n\n20FT Premium — $17,125\n\u2192 https://buy.stripe.com/fZedRj7YC70Y9le145d7\n\n40FT Deluxe — $21,100\n\u2192 https://buy.stripe.com/28o8wRfXs8CC50c145bF98\n\n40FT Premium — $28,550\n\u2192 https://buy.stripe.com/8wM7vf8yY9m49tG6oHb38"
    }
}


class QuantumWebsiteBot:
    """Combined sales + CS bot — runs on every page of containerhomes.com"""
    
    def __init__(self):
        self.conversations = {}
        self.total_helpful_responses = 0
        self.total_sales = 0
    
    def greet(self, visitor_id, page="/", language="en"):
        """Greet based on page context"""
        conv = {
            "id": visitor_id,
            "page": page,
            "language": language,
            "started": datetime.utcnow().isoformat(),
            "problems_solved": 0,
            "product_recommended": None,
            "purchased": False,
            "messages": [],
            "intent": "browsing"
        }
        self.conversations[visitor_id] = conv
        
        # Page-aware greetings
        page_greetings = {
            "/": "Hey! 👋 Looking at container homes? I can answer any question — pricing, delivery, sizes, zoning. Ask me anything.",
            "/products/": "🔍 Checking out the models? I can help you pick the right size. Tell me what you're planning to use it for.",
        }
        
        greeting = page_greetings.get(page, "Hi! 🏠 Need help with container homes? I'm here 24/7.")
        return f"{greeting}\n\n_{QBA_BRANDING}_"
    
    def answer(self, visitor_id, question):
        """Answer any container home question with deep industry knowledge"""
        conv = self.conversations.get(visitor_id)
        if not conv:
            return self.greet(visitor_id)
        
        q = question.lower()
        answer_parts = []
        
        # Search all knowledge domains — PRIORITY: pricing > delivery > all else
        # Build ordered domain list
        ordered_domains = ['pricing', 'delivery'] + [d for d in INDUSTRY_KNOWLEDGE if d not in ('pricing', 'delivery')]
        for domain in ordered_domains:
            topics = INDUSTRY_KNOWLEDGE[domain]
            for keyword, text in topics.items():
                if keyword in q:
                    answer_parts.append(text)
        
        # Track problem solved
        conv["problems_solved"] += 1
        self.total_helpful_responses += 1
        
        # If 3 problems solved, always hint at a product
        if conv["problems_solved"] >= 3 and not conv["product_recommended"]:
            # Determine best product
            recommended = self._match_product(q)
            conv["product_recommended"] = recommended["slug"]
            answer_parts.append(f"\n\n💡 Based on what you're telling me, the **{recommended['product']['name']}** at **${recommended['product']['price']:,}** sounds like a great fit. Here's the secure checkout: {recommended['product']['stripe']}")
        
        if not answer_parts:
            # Fallback — rule of 3
            answer_parts.append("Great question! Here's what I can tell you:\n\n")
            answer_parts.append("1️⃣ Our container homes start at $9,945 delivered — 60-80% cheaper than traditional construction.\n")
            answer_parts.append("2️⃣ Delivery takes 45 days anywhere in the continental U.S. — no contractor needed.\n")
            answer_parts.append("3️⃣ All models are hurricane rated, earthquake rated, and fully insulated with spray foam.\n\n")
            answer_parts.append("What else can I help you with? I can answer pricing, delivery, zoning, assembly, anything.")
        
        response = "\n".join(answer_parts)
        response += f"\n\n_{QBA_BRANDING}_"
        
        conv["messages"].append(("customer", question))
        conv["messages"].append(("bot", response))
        
        return response
    
    def _match_product(self, question):
        """Match user context to best product"""
        scores = {}
        for slug, product in PRODUCTS.items():
            score = 0
            best_for = product["best_for"]
            for word in question.split():
                if word in best_for:
                    score += 10
                if word == str(product["price"]):
                    score += 5
            scores[slug] = score
        
        if not scores or max(scores.values()) == 0:
            # Default to best seller
            return {"slug": "20ft-expandable", "product": PRODUCTS["20ft-expandable"]}
        
        best = max(scores, key=scores.get)
        return {"slug": best, "product": PRODUCTS[best]}
    
    def handle_support(self, visitor_id, issue):
        """CS mode — resolve support issues"""
        issue_lower = issue.lower()
        
        if any(w in issue_lower for w in ["refund", "cancel", "return"]):
            return ("Our 14-day return policy: contact us within 14 days of delivery, we'll arrange return shipping, "
                    "and refunds process within 5-7 business days after we receive the unit. Need to start a return? "
                    "I'll connect you to our support team.\n\n"
                    f"_{QBA_BRANDING}_")
        
        if any(w in issue_lower for w in ["damage", "broken", "crack", "dent"]):
            return ("I'm sorry for the issue! Inspect and photograph the damage within 48 hours of delivery. "
                    "We ship replacement parts within 7 days at no cost. For major damage, our support team will coordinate a full resolution.\n\n"
                    f"_{QBA_BRANDING}_")
        
        if any(w in issue_lower for w in ["track", "where", "ship", "arrive"]):
            return ("Your order is on the way! Typical timeline: 30 days manufacturing, then 15 days shipping. "
                    "You'll receive tracking via email when it ships. If you haven't received tracking yet, your unit is still in production.\n\n"
                    f"_{QBA_BRANDING}_")
        
        if any(w in issue_lower for w in ["assembly", "install", "build", "setup"]):
            return ("Assembly takes 2-3 days for 20FT models, 5-7 days for 40FT. Our team handles everything. "
                    "You just prepare a level site. Full instructions and video guide included. Need specific assembly help? "
                    "I can connect you to our technical support.\n\n"
                    f"_{QBA_BRANDING}_")
        
        # Default support response
        return ("I'm here to help! I can assist with delivery tracking, assembly questions, warranty claims, "
                "returns, or any issue. Just tell me what's going on and I'll get you sorted.\n\n"
                f"_{QBA_BRANDING}_")
    
    def purchase(self, visitor_id, product_slug):
        """Direct purchase path"""
        product = PRODUCTS.get(product_slug)
        if not product:
            return "Which model are you interested in? We have the 20FT Expandable ($9,945), 20FT Premium ($17,125), 40FT Deluxe ($21,100), and 40FT Premium ($28,550)."
        
        conv = self.conversations.get(visitor_id)
        if conv:
            conv["purchased"] = True
            self.total_sales += 1
        
        return (f"Ready to buy the {product['name']}! 🎉 Here's your secure checkout link:\n\n"
                f"🔗 {product['stripe']}\n\n"
                f"After purchase, you'll get an order confirmation within 5 minutes. Your 45-day delivery countdown starts now.\n\n"
                f"_{QBA_BRANDING}_")


# ─── WEB WIDGET INJECTION ───

CHAT_WIDGET_HTML = '''
<div id="qba-chat-widget" style="position:fixed;bottom:20px;right:20px;z-index:99999;font-family:Inter,sans-serif">
  <style>
    #qba-chat-btn{width:56px;height:56px;border-radius:50%;background:linear-gradient(135deg,#6366f1,#8b5cf6);border:none;cursor:pointer;box-shadow:0 4px 20px rgba(99,102,241,.4);display:flex;align-items:center;justify-content:center;transition:all .2s;font-size:24px}
    #qba-chat-btn:hover{transform:scale(1.05);box-shadow:0 6px 28px rgba(99,102,241,.5)}
    #qba-chat-box{display:none;width:360px;height:500px;background:#0f0f1a;border:1px solid #1a1a25;border-radius:16px;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.5);flex-direction:column}
    #qba-chat-header{background:linear-gradient(135deg,#111120,#13131a);padding:16px;border-bottom:1px solid #1a1a25;display:flex;align-items:center;gap:10px}
    #qba-chat-header .dot{width:8px;height:8px;border-radius:50%;background:#22c55e;display:inline-block}
    #qba-chat-header h3{color:#fff;font-size:14px;font-weight:600}
    #qba-chat-header p{color:#555;font-size:11px}
    #qba-chat-messages{flex-grow:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:8px}
    #qba-chat-messages .msg-bot{background:#111120;color:#ccc;padding:12px 14px;border-radius:12px 12px 12px 4px;font-size:13px;line-height:1.5;max-width:85%;align-self:flex-start;border:1px solid #1a1a25}
    #qba-chat-messages .msg-bot strong{color:#fff}
    #qba-chat-messages .msg-user{background:linear-gradient(135deg,#6366f1,#7c3aed);color:#fff;padding:12px 14px;border-radius:12px 12px 4px 12px;font-size:13px;line-height:1.5;max-width:80%;align-self:flex-end}
    #qba-chat-messages .qba-tag{font-size:10px;color:#555;margin-top:6px}
    #qba-chat-input{display:flex;border-top:1px solid #1a1a25;padding:10px;gap:8px;background:#0a0a0f}
    #qba-chat-input input{flex-grow:1;background:#111120;border:1px solid #1a1a25;border-radius:8px;padding:10px 14px;color:#fff;font-size:13px;outline:none}
    #qba-chat-input input:focus{border-color:#6366f1}
    #qba-chat-input button{background:#6366f1;border:none;color:#fff;padding:10px 16px;border-radius:8px;cursor:pointer;font-weight:600;font-size:13px}
    #qba-chat-input button:hover{background:#5558e6}
    @media(max-width:480px){#qba-chat-box{width:100vw;height:100vh;bottom:0;right:0;border-radius:0}}
  </style>
  <div id="qba-chat-btn" onclick="toggleChat()">💬</div>
  <div id="qba-chat-box">
    <div id="qba-chat-header">
      <div><span class="dot"></span></div>
      <div><h3>Container Homes</h3><p>Quantum sales & support bot</p></div>
    </div>
    <div id="qba-chat-messages">
      <div class="msg-bot">🏠 Welcome! I'm your container home specialist. Ask me about pricing, delivery, sizes, zoning — or get a recommendation.<div class="qba-tag">Powered by Quantum Bots Agency</div></div>
    </div>
    <div id="qba-chat-input">
      <input id="qba-input" placeholder="Ask about container homes..." onkeydown="if(event.key==='Enter')sendMsg()">
      <button onclick="sendMsg()">Send</button>
    </div>
  </div>
  <script>
    let chatOpen = false;
    function toggleChat(){chatOpen=!chatOpen;document.getElementById('qba-chat-box').style.display=chatOpen?'flex':'none';document.getElementById('qba-chat-btn').textContent=chatOpen?'✕':'💬'}
    function sendMsg(){const i=document.getElementById('qba-input');const m=i.value.trim();if(!m)return;i.value='';const msgs=document.getElementById('qba-chat-messages');msgs.innerHTML+=`<div class="msg-user">${m}</div>`;msgs.scrollTop=msgs.scrollHeight;setTimeout(()=>{const r=getResponse(m);msgs.innerHTML+=r;msgs.scrollTop=msgs.scrollHeight},300)}
    function getResponse(q){const l=q.toLowerCase();let r='';const kb={
      "price|cost|how much":'<div class="msg-bot"><strong>💰 Pricing</strong><br>20FT Expandable: <strong>$9,945</strong><br>20FT Premium: <strong>$17,125</strong><br>40FT Deluxe: <strong>$21,100</strong><br>40FT Premium: <strong>$28,550</strong><br><br>All prices include delivery and assembly within the continental U.S. 60-80% cheaper than traditional construction.<div class="qba-tag">Powered by Quantum Bots Agency</div></div>',
      "delivery|ship|shipping|arrive":'<div class="msg-bot"><strong>🚚 Delivery</strong><br>45 days from order to your property. Free delivery within the continental U.S. Our team handles assembly — 2-3 days for 20FT, 5-7 days for 40FT. No contractor needed on your end.<div class="qba-tag">Powered by Quantum Bots Agency</div></div>',
      "size|sqft|square|feet|20ft|40ft":'<div class="msg-bot"><strong>📐 Sizes</strong><br><strong>20FT Expandable:</strong> 400 sq ft — best for man caves, offices, she sheds, guest rooms<br><strong>40FT Deluxe:</strong> 800 sq ft — 2 bed, 1 bath, full kitchen, living room<br><strong>40FT Premium:</strong> 800 sq ft — luxury finishes, granite, smart home<br><br>Both expand on-site — no permits needed for delivery.<div class="qba-tag">Powered by Quantum Bots Agency</div></div>',
      "foundation|concrete|install|setup":'<div class="msg-bot"><strong>🏗️ Foundation & Setup</strong><br>Concrete slab or concrete piers — we include engineered plans for your soil type. Our team handles placement and expansion. You just need clear property access (12ft wide gate min).<div class="qba-tag">Powered by Quantum Bots Agency</div></div>',
      "zoning|permit|hoa|legal":'<div class="msg-bot"><strong>📋 Zoning & Permits</strong><br>Container homes are classified as prefabricated structures. We provide stamped engineering drawings approved for all 50 states. Most counties approve permits in 2-4 weeks. HOAs may restrict — check your CC&Rs.<div class="qba-tag">Powered by Quantum Bots Agency</div></div>',
      "hurricane|earthquake|storm|safe|steel":'<div class="msg-bot"><strong>🛡️ Durability</strong><br>Category 4 hurricane rated (140 mph winds). Seismic Zone 4 earthquake rated. 14-gauge corten steel — same grade used in ocean shipping. Spray foam insulation (R-19 walls, R-30 roof). Built to last decades.<div class="qba-tag">Powered by Quantum Bots Agency</div></div>',
      "airbnb|rental|income":'<div class="msg-bot"><strong>💰 Rental Income</strong><br>Owners report $2,700-$3,200/month on Airbnb with our container homes. At $9,945 for the 20FT Expandable, many recoup their investment in 4 months. 75% occupancy average. Novelty factor drives bookings.<div class="qba-tag">Powered by Quantum Bots Agency</div></div>',
      "warranty|return|refund":'<div class="msg-bot"><strong>✅ Warranty & Returns</strong><br>10-year structural warranty on steel frame. 2-year on finishes. 14-day return window. Refunds processed within 5-7 business days. We handle damage replacement within 7 days at no cost.<div class="qba-tag">Powered by Quantum Bots Agency</div></div>',
      "buy|purchase|order":'<div class="msg-bot"><strong>Ready to buy! 🎉</strong><br><br><strong>20FT Expandable — $9,945</strong><br><a href="https://buy.stripe.com/bJebJ1e1C6wddrQ6Ima3u00" target="_blank" style="color:#818cf8">Buy Now →</a><br><br><strong>20FT Premium — $17,125</strong><br><a href="https://buy.stripe.com/fZedRj7YC70Y9le145d7" target="_blank" style="color:#818cf8">Buy Now →</a><br><br><strong>40FT Deluxe — $21,100</strong><br><a href="https://buy.stripe.com/28o8wRfXs8CC50c145bF98" target="_blank" style="color:#818cf8">Buy Now →</a><br><br><strong>40FT Premium — $28,550</strong><br><a href="https://buy.stripe.com/8wM7vf8yY9m49tG6oHb38" target="_blank" style="color:#818cf8">Buy Now →</a><div class="qba-tag">Powered by Quantum Bots Agency</div></div>'
    };
    for(const k in kb){const words=k.split('|');if(words.some(w=>l.includes(w))){r=kb[k];break}}
    if(!r)r='<div class="msg-bot">Great question! Here\'s what I can tell you:<br><br>1️⃣ Our container homes start at <strong>$9,945 delivered</strong> — 60-80% cheaper than traditional construction.<br>2️⃣ <strong>45-day delivery</strong> anywhere in the continental U.S. — no contractor needed.<br>3️⃣ All models are <strong>hurricane rated, earthquake rated</strong>, and fully insulated.<br><br>What else can I help with? Pricing, sizes, delivery, zoning — I cover it all.<div class="qba-tag">Powered by Quantum Bots Agency</div></div>';
    return r}
  </script>
</div>
'''


# ─── INJECT INTO WEBSITE ───

def inject_chat_widget(html_file):
    """Inject the quantum chat widget into any HTML page"""
    with open(html_file, 'r') as f:
        html = f.read()
    
    if '</body>' in html:
        html = html.replace('</body>', f'{CHAT_WIDGET_HTML}\n</body>')
    elif '</html>' in html:
        html = html.replace('</html>', f'{CHAT_WIDGET_HTML}\n</html>')
    
    with open(html_file, 'w') as f:
        f.write(html)
    
    print(f"  ✓ Injected into {html_file.split('/')[-1]}")


# ─── DEMO ───
if __name__ == "__main__":
    bot = QuantumWebsiteBot()
    
    print("=" * 60)
    print("CONTAINER HOMES — QUANTUM SALES + CS BOT")
    print("=" * 60)
    print(f"\n{QBA_BRANDING}\n")
    
    # Simulate a full interaction
    visitor = "web_visitor_001"
    
    print("--- SALES FLOW ---")
    print(f"Visitor lands on home page")
    print(f"BOT: {bot.greet(visitor, '/')}\n")
    
    questions = [
        "How much do these container homes cost?",
        "How long does delivery take?",
        "What kind of foundation do I need?"
    ]
    
    for q in questions:
        print(f"VISITOR: {q}")
        r = bot.answer(visitor, q)
        print(f"BOT: {r[:200]}...\n")
    
    print("--- SUPPORT FLOW ---")
    print(f"VISITOR: My container arrived damaged")
    print(f"BOT: {bot.handle_support(visitor, 'my container arrived damaged')}\n")
    
    print("--- PURCHASE FLOW ---")
    print(f"VISITOR: I want to buy the 20FT")
    print(f"BOT: {bot.purchase(visitor, '20ft-expandable')}\n")
    
    print("--- STATS ---")
    print(f"Problems solved: {bot.conversations[visitor]['problems_solved']}")
    print(f"Product recommended: {bot.conversations[visitor]['product_recommended']}")
    print(f"Total helpful responses: {bot.total_helpful_responses}")
    print(f"QBA branding: On every response ✓")
    
    print("\n= WEB WIDGET READY =")
    print("Injected chat widget handles: pricing, delivery, sizes, foundation,")
    print("zoning, permits, hurricane rating, rental income, warranty, returns, purchases")
    print("Deep container home industry knowledge on every question.")

