#!/usr/bin/env python3
"""
Container Homes Quantum Customer Service Bot
Deployed by Pod Gamma — Engineer 11 (Bot Architect)
Footer: "Powered by Quantum Bots Agency" on every interaction
Handles pre-sale + post-sale. 24/7. 9 languages. L0→L1 escalation.
"""

import json, random, time, re
from datetime import datetime, timedelta

# ─── CONFIG ───
QBA_BRANDING = "Powered by Quantum Bots Agency — AI for every business"
SLA_RESPONSE_SECONDS = 30  # L0 target
ESCALATION_THRESHOLD = 3   # Escalate to human after 3 unresolved issues

# ─── KNOWLEDGE BASE ───
KNOWLEDGE_BASE = {
    "en": {
        "delivery": "Delivery takes 45-75 days depending on the model. Free shipping to your port city.",
        "tracking": "You'll receive tracking info via email once your container ships. Average transit: 30-45 days.",
        "assembly": "2-7 days with 2-3 people. Full instructions and video guide included.",
        "return": "Returns accepted within 14 days of delivery. Return shipping is customer's responsibility.",
        "refund": "Refunds processed within 5-7 business days after we receive the returned unit.",
        "warranty": "10-year structural warranty. 2-year finish warranty. Both transferable.",
        "damage": "Inspect within 48 hours of delivery. Photos of damage → we ship replacement parts within 7 days.",
        "customize": "Contact sales for customization requests. We can modify layout, finishes, windows, and doors.",
        "payment": "We accept Visa, Mastercard, Amex, and Discover via secure Stripe checkout.",
        "shipping": "Ocean freight to your nearest port. We coordinate customs clearance for you.",
        "permit": "We provide engineering certifications. Most municipalities approve container homes as prefab structures.",
        "foundation": "Concrete slab or piers. Foundation plan included with every order.",
        "sizes": "Available sizes: 20FT Expandable ($9,945), 40FT Expandable Deluxe ($21,100), 40FT Premium ($28,550).",
        "contact": "For urgent issues, you can reach our team at support@containerhomes.com or call +1-555-0170.",
    },
    "es": {
        "delivery": "Entrega en 45-75 días. Envío gratuito a su puerto más cercano.",
        "tracking": "Recibirá información de seguimiento por correo electrónico cuando su contenedor se embarque.",
        "warranty": "Garantía estructural de 10 años. Garantía de acabados de 2 años.",
        "payment": "Aceptamos Visa, Mastercard, Amex y Discover.",
        "contact": "Para asuntos urgentes: support@containerhomes.com o +1-555-0170.",
    },
    "fr": {
        "delivery": "Livraison sous 45 à 75 jours. Expédition gratuite vers votre port.",
        "warranty": "Garantie structurelle de 10 ans. Garantie de finition de 2 ans.",
        "contact": "Urgences : support@containerhomes.com ou +1-555-0170.",
    },
    "de": {
        "delivery": "Lieferung in 45-75 Tagen. Kostenloser Versand zu Ihrem Hafen.",
        "warranty": "10 Jahre strukturelle Garantie. 2 Jahre Oberflächengarantie.",
        "contact": "Bei dringenden Anliegen: support@containerhomes.com oder +1-555-0170.",
    },
    "pt": {
        "delivery": "Entrega em 45-75 dias. Frete grátis para seu porto.",
        "warranty": "Garantia estrutural de 10 anos. Garantia de acabamento de 2 anos.",
        "contact": "Urgências: support@containerhomes.com ou +1-555-0170.",
    },
    "ar": {
        "delivery": "التسليم خلال 45-75 يومًا. شحن مجاني إلى مينائك.",
        "warranty": "ضمان هيكلي لمدة 10 سنوات. ضمان التشطيب لمدة سنتين.",
    },
    "zh": {
        "delivery": "交货时间45-75天。免费送货到您所在港口城市。",
        "warranty": "10年结构保修。2年装修保修。",
    },
    "ja": {
        "delivery": "納期は45〜75日。お近くの港まで送料無料。",
        "warranty": "10年間の構造保証。2年間の仕上げ保証。",
    },
    "it": {
        "delivery": "Consegna in 45-75 giorni. Spedizione gratuita al tuo porto.",
        "warranty": "Garanzia strutturale di 10 anni. Garanzia di finitura di 2 anni.",
    }
}

# ─── ESCALATION RULES ───
ESCALATION_KEYWORDS = {
    "angry": ["refund", "cancel", "complaint", "unacceptable", "lawyer", "sue"],
    "urgent": ["urgent", "emergency", "broken", "flood", "fire", "damage"],
    "complex": ["custom", "modification", "structural change", "engineering"],
}

class QuantumCSBot:
    def __init__(self):
        self.tickets = {}
        self.stats = {
            "total_conversations": 0,
            "resolved_l0": 0,
            "escalated_to_l1": 0,
            "sla_met": 0,
            "sla_missed": 0,
        }
    
    def start_ticket(self, customer_id, language="en", platform="webchat"):
        """Open a support ticket"""
        self.tickets[customer_id] = {
            "created": datetime.utcnow().isoformat(),
            "language": language,
            "platform": platform,
            "issues_count": 0,
            "escalated": False,
            "resolved": False,
            "messages": [],
        }
        self.stats["total_conversations"] += 1
        
        greetings = {
            "en": f"👋 Welcome to {SITE_NAME} support! I'm here to help with orders, delivery, assembly, or any questions. What can I help you with?",
            "es": f"👋 ¡Bienvenido al soporte de {SITE_NAME}! ¿En qué puedo ayudarle?",
            "fr": f"👋 Bienvenue au support {SITE_NAME}! Comment puis-je vous aider?",
            "de": f"👋 Willkommen beim {SITE_NAME} Support! Wie kann ich Ihnen helfen?",
            "pt": f"👋 Bem-vindo ao suporte {SITE_NAME}! Como posso ajudá-lo?",
        }
        
        greeting = greetings.get(language, greetings["en"])
        return f"{greeting}\n\n_{QBA_BRANDING}_"
    
    def handle_inquiry(self, customer_id, message, language="en"):
        """Resolve customer inquiry — L0 automation"""
        ticket = self.tickets.get(customer_id)
        if not ticket:
            return self.start_ticket(customer_id, language)
        
        start_time = time.time()
        message_lower = message.lower()
        
        # Check for escalation triggers
        for category, keywords in ESCALATION_KEYWORDS.items():
            if any(kw in message_lower for kw in keywords):
                ticket["escalated"] = True
                break
        
        # Find answer in knowledge base
        response = None
        kb = KNOWLEDGE_BASE.get(language, KNOWLEDGE_BASE["en"])
        
        for keyword, answer in kb.items():
            if keyword in message_lower:
                response = answer
                break
        
        if not response:
            # Fallback: use English KB
            for keyword, answer in KNOWLEDGE_BASE["en"].items():
                if keyword in message_lower:
                    response = answer
                    break
        
        if not response:
            response = "I want to make sure I help you correctly. Could you give me a bit more detail? I can help with delivery, assembly, warranty, returns, and more."
        
        # Track SLA
        elapsed = time.time() - start_time
        if elapsed < SLA_RESPONSE_SECONDS:
            self.stats["sla_met"] += 1
        else:
            self.stats["sla_missed"] += 1
        
        # Track issue
        ticket["issues_count"] += 1
        
        # Escalate if threshold reached
        if ticket["issues_count"] >= ESCALATION_THRESHOLD + 1 and not ticket["escalated"]:
            return self.escalate_to_human(customer_id)
        
        # Add QBA branding
        response += f"\n\n_{QBA_BRANDING}_"
        
        ticket["messages"].append(("customer", message))
        ticket["messages"].append(("bot", response))
        
        return response
    
    def escalate_to_human(self, customer_id):
        """Escalate to L1 human agent"""
        ticket = self.tickets.get(customer_id)
        if not ticket:
            return "Let me connect you to a team member."
        
        ticket["escalated"] = True
        self.stats["escalated_to_l1"] += 1
        ticket["resolved"] = False
        
        l1_response = (
            f"🔄 I'm connecting you to our support team. A real person will be with you within 3 minutes.\n\n"
            f"Your ticket ID: CS-{customer_id[:8]}-{datetime.utcnow().strftime('%H%M')}\n\n"
            f"While you wait, here's a summary of what we discussed:\n"
            f"• Issues raised: {ticket['issues_count']}\n"
            f"• Time in queue: {(datetime.utcnow() - datetime.fromisoformat(ticket['created'])).seconds // 60} minutes\n\n"
            f"_{QBA_BRANDING}_"
        )
        
        return l1_response
    
    def resolve_ticket(self, customer_id):
        """Mark ticket as resolved"""
        ticket = self.tickets.get(customer_id)
        if ticket:
            ticket["resolved"] = True
            self.stats["resolved_l0"] += 1
        
        resolutions = [
            f"✅ Your issue is resolved! If anything else comes up, I'm here 24/7.\n\n_{QBA_BRANDING}_",
            f"👍 All taken care of! Feel free to come back anytime.\n\n_{QBA_BRANDING}_",
            f"🎉 Done! Thanks for your patience.\n\n_{QBA_BRANDING}_",
        ]
        
        return random.choice(resolutions)
    
    def get_stats(self):
        """Return bot performance stats"""
        total = self.stats["total_conversations"]
        resolved = self.stats["resolved_l0"]
        escalated = self.stats["escalated_to_l1"]
        sla_rate = (self.stats["sla_met"] / (self.stats["sla_met"] + self.stats["sla_missed"])) * 100 if (self.stats["sla_met"] + self.stats["sla_missed"]) > 0 else 100
        
        return {
            "total_tickets": total,
            "resolved_l0": resolved,
            "escalated_l1": escalated,
            "auto_resolution_rate": f"{(resolved / total * 100) if total else 0:.1f}%",
            "sla_compliance": f"{sla_rate:.1f}%",
            "qba_branding": "✅ Present on every response"
        }


# ─── SIMULATION ───
if __name__ == "__main__":
    SITE_NAME = "Container Homes"
    bot = QuantumCSBot()
    
    print("=== CONTAINER HOMES QUANTUM CS BOT ===\n")
    print(f"SLA target: {SLA_RESPONSE_SECONDS}s | Escalate after {ESCALATION_THRESHOLD} unresolved\n")
    print("=" * 60)
    
    # Demo: Standard inquiry flow
    customer = "demo_001"
    print(f"\nCUSTOMER (EN): When will my order arrive?")
    print(f"BOT: {bot.handle_inquiry(customer, 'when will my container arrive?', 'en')}")
    
    print(f"\nCUSTOMER (EN): How do I assemble it?")
    print(f"BOT: {bot.handle_inquiry(customer, 'assembly instructions', 'en')}")
    
    # Demo: Escalation flow
    print(f"\nCUSTOMER (EN): This is unacceptable I want a refund")
    print(f"BOT: {bot.handle_inquiry(customer, 'this is unacceptable I want a refund', 'en')}")
    
    # Demo: Spanish inquiry
    print(f"\nCUSTOMER (ES): ¿Cuándo llegará mi pedido?")
    print(f"BOT: {bot.handle_inquiry('demo_es', 'cuando llegara mi pedido', 'es')}")
    
    # Resolve
    print(f"\nCUSTOMER (EN): Everything is good now")
    print(f"BOT: {bot.resolve_ticket(customer)}")
    
    print("\n" + "=" * 60)
    print("\n=== BOT PERFORMANCE STATS ===")
    for k, v in bot.get_stats().items():
        print(f"  {k}: {v}")

PYEOF