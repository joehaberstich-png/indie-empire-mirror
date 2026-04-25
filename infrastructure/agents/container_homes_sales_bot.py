#!/usr/bin/env python3
"""
Container Homes Quantum Sales Bot
Deployed by Pod Beta — Engineer 6 (Bot Architect)
Footer: "Powered by Quantum Bots Agency" on every interaction
"""

import json, random, time, re, hashlib
from datetime import datetime, timedelta

# ─── CONFIG ───
SITE_NAME = "Container Homes"
QBA_BRANDING = "Powered by Quantum Bots Agency — AI for every business"
QBA_LINK = "https://quantumbotsagency.com"

# Products
PRODUCTS = {
    "20ft_expandable": {
        "name": "20FT Expandable Container House",
        "price": 9945,
        "sizes": "20ft x 20ft (expandable to 40ft x 20ft)",
        "delivery": "45-60 days from order",
        "payment_link": "https://buy.stripe.com/bJebJ1e1C6wddrQ6Ima3u00",
        "features": ["Expandable design", "Pre-assembled panels", "Fully insulated", "Ready for utilities"],
        "assembly": "2-3 days with 2 people",
        "foundation": "Concrete slab or piers",
    },
    "40ft_deluxe": {
        "name": "40FT Expandable Container House (Deluxe)",
        "price": 21100,
        "sizes": "40ft x 20ft (expandable to 60ft x 30ft)",
        "delivery": "60-75 days from order",
        "payment_link": "https://buy.stripe.com/eVq8wPcXy6wd87w1o2a3u03",
        "features": ["Premium finish", "Master suite included", "Full kitchen", "Custom layout options"],
        "assembly": "5-7 days with 2-3 people",
        "foundation": "Concrete slab recommended",
    },
    "40ft_premium": {
        "name": "40FT Expandable Container House",
        "price": 28550,
        "sizes": "40ft x 20ft (expandable to 60ft x 40ft)",
        "delivery": "60-75 days from order",
        "payment_link": "https://buy.stripe.com/8x2aEXg9K9IpafEfeSa3u01",
        "features": ["Luxury finishes", "3 bedroom layout", "Full bathroom", "Open plan living", "Premium insulation"],
        "assembly": "5-7 days with 3 people",
        "foundation": "Concrete slab required",
    },
}

# ─── SALES KNOWLEDGE ───
KNOWLEDGE_BASE = {
    "delivery": "Delivery takes 45-75 days depending on the model. Shipping is free within your country's port city.",
    "foundation": "Most container homes work with a concrete slab or concrete piers. We include foundation specs with every order.",
    "customization": "Yes! All our container homes can be customized. Layout, finishes, windows, doors — you tell us what you need.",
    "assembly": "Assembly takes 2-7 days with 2-3 people. Every unit comes with detailed assembly instructions and video guides.",
    "permit": "Container homes are classified as prefabricated structures in most countries. We provide engineering certifications for permit applications.",
    "warranty": "All units come with a 10-year structural warranty and 2-year finish warranty.",
    "shipping": "We ship worldwide via ocean freight. Shipping time depends on your country but averages 30-45 days transit.",
    "price": "Our container homes range from $9,945 for the 20FT Expandable to $28,550 for the 40FT Luxury Villa.",
    "payment": "We accept all major credit cards via secure Stripe checkout. Full payment is due at order.",
}

# ─── PROBLEM SOLVING ───
THREE_PROBLEM_RULE = True  # Required: solve 3 problems before any sale

class QuantumSalesBot:
    def __init__(self):
        self.conversations = {}
        self.problems_solved = {"total": 0}
    
    def start_conversation(self, visitor_id, platform="webchat", language="en"):
        """Initialize a sales conversation"""
        self.conversations[visitor_id] = {
            "started": datetime.utcnow().isoformat(),
            "platform": platform,
            "language": language,
            "problems_solved": 0,
            "mentioned_product": False,
            "recommended_product": None,
            "buyer_intent": 0,
            "messages": [],
        }
        
        # Greeting — 3 variants for human fingerprint
        greetings = [
            f"👋 Hey! Looking for a container home? I answer questions here 24/7.",
            f"🏠 Welcome to {SITE_NAME}! Not sure which container home fits your needs? Ask me anything.",
            f"Hi there! 🚢 I'm the {SITE_NAME} sales guide. Thinking about a container home? Let's talk."
        ]
        
        return random.choice(greetings) + f"\n\n_{QBA_BRANDING}_"
    
    def solve_problem(self, visitor_id, question):
        """Solve customer's problem — must reach 3 before any sale"""
        conv = self.conversations.get(visitor_id)
        if not conv:
            return "Let me start fresh with you. What can I help you with?"
        
        question_lower = question.lower()
        
        # Detect question category
        answer = None
        for keyword, response in KNOWLEDGE_BASE.items():
            if keyword in question_lower:
                answer = response
                break
        
        if not answer:
            # Generic helpful response
            answer = f"That's a great question! Here's what I can tell you: all our container homes are built to international standards and ship to any country. Our most popular model is the 20FT Expandable at $9,945 — a complete home for under $10K.\n\nWhat else would you like to know?"
        
        # Track problem solved
        conv["problems_solved"] += 1
        self.problems_solved["total"] += 1
        
        # Add QBA branding
        answer += f"\n\n_{QBA_BRANDING}_"
        
        conv["messages"].append(("customer", question))
        conv["messages"].append(("bot", answer))
        
        return answer
    
    def recommend_product(self, visitor_id, context=None):
        """Only called after 3 problems solved"""
        conv = self.conversations.get(visitor_id)
        if not conv:
            return None
        
        if conv["problems_solved"] < 3 and THREE_PROBLEM_RULE:
            return None  # Not ready
        
        # Determine best product based on context
        if context:
            if "budget" in context.lower() and any(w in context.lower() for w in ["low", "small", "cheap", "under"]):
                recommended = "20ft_expandable"
            elif "luxury" in context.lower() or "large" in context.lower() or "family" in context.lower():
                recommended = "40ft_premium"
            else:
                recommended = "40ft_deluxe"
        else:
            # Most popular
            recommended = "20ft_expandable"
        
        product = PRODUCTS[recommended]
        conv["recommended_product"] = recommended
        conv["mentioned_product"] = True
        conv["buyer_intent"] = min(conv["buyer_intent"] + 40, 100)
        
        pitch = (
            f"Based on what you've told me, I'd recommend the **{product['name']}** "
            f"at **${product['price']:,}**. Here's why:\n\n"
            f"• {product['features'][0]}\n"
            f"• {product['features'][1]}\n"
            f"• {product['features'][2]}\n\n"
            f"Ready to see the full details? Here's your secure checkout link:\n"
            f"🔗 {product['payment_link']}\n\n"
            f"_{QBA_BRANDING}_"
        )
        
        conv["messages"].append(("bot", pitch))
        return pitch
    
    def handle_post_purchase(self, visitor_id):
        """After purchase, transition to CS bot context"""
        conv = self.conversations.get(visitor_id)
        if conv:
            conv["buyer_intent"] = 100
            
        return (
            f"🎉 Congratulations on your {SITE_NAME} container home! "
            f"Your order is being processed. Here's what happens next:\n\n"
            f"1. 📋 Order confirmation in your email\n"
            f"2. 🏭 Manufacturing begins (2-3 weeks)\n"
            f"3. 🚢 Shipping (30-45 days)\n"
            f"4. 🏠 Delivery to your port city\n\n"
            f"For shipping updates and support, our customer service bot is standing by.\n\n"
            f"_{QBA_BRANDING}_"
        )


# ─── DEPLOYMENT ENTRY POINT ───
if __name__ == "__main__":
    bot = QuantumSalesBot()
    
    # Simulate a conversation
    visitor = "demo_user_001"
    
    print("=== CONTAINER HOMES QUANTUM SALES BOT ===\n")
    print(f"_{QBA_BRANDING}_\n")
    
    # Step 1: Greeting
    print(f"BOT: {bot.start_conversation(visitor)}\n")
    
    # Step 2-4: Solve 3 problems
    problems = [
        "How long does delivery take to the US?",
        "What kind of foundation do I need?",
        "Can I customize the floor plan?"
    ]
    
    for problem in problems:
        print(f"CUSTOMER: {problem}")
        response = bot.solve_problem(visitor, problem)
        print(f"BOT: {response}\n")
    
    # Step 5: Product recommendation (after 3 problems)
    print(f"CUSTOMER: What do you recommend for me?")
    recommendation = bot.recommend_product(visitor, context="mid-range home for family")
    print(f"BOT: {recommendation}\n")
    
    # Step 6: Post-purchase
    print(f"CUSTOMER: I'd like to buy")
    print(f"BOT: {bot.handle_post_purchase(visitor)}\n")
    
    print(f"=== STATS ===")
    print(f"Problems solved: {bot.conversations[visitor]['problems_solved']}")
    print(f"Product recommended: {bot.conversations[visitor]['recommended_product']}")
    print(f"Buyer intent at close: {bot.conversations[visitor]['buyer_intent']}%")
    print(f"QBA branding in every response: ✅")
