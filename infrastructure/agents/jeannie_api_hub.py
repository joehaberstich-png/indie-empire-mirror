#!/usr/bin/env python3
"""
Jeannie Boutiler Nails — API & Integration Hub v1.0
Quantum Bot API + Scheduling + Plugin & Integration Layer
Deployable as standalone server or Vercel serverless function.
"""

import json, os, hashlib, time, random
from datetime import datetime, timedelta
from http.server import HTTPServer, BaseHTTPRequestHandler

# ─── CONFIG ───
API_VERSION = "1.0"
SITE_URL = "https://jeannie-nails.vercel.app"
PHONE = "(902) 885-7896"
EMAIL = ""  # TBD
TIMEZONE = "Atlantic Canada"

# ─── SCHEDULE LOGIC ───
WEEKLY_SCHEDULE = {
    1: {"day": "Monday", "status": "closed"},
    2: {"day": "Tuesday", "status": "open", "hours": "10:00 AM – 5:00 PM", "open_h": 10, "close_h": 17},
    3: {"day": "Wednesday", "status": "open", "hours": "10:00 AM – 6:00 PM", "open_h": 10, "close_h": 18},
    4: {"day": "Thursday", "status": "open", "hours": "10:00 AM – 6:00 PM", "open_h": 10, "close_h": 18},
    5: {"day": "Friday", "status": "open", "hours": "10:00 AM – 4:00 PM", "open_h": 10, "close_h": 16},
    6: {"day": "Saturday", "status": "closed"},
    7: {"day": "Sunday", "status": "closed"},
}

SERVICES = {
    "ingrown_toenail": {
        "name": "Ingrown Toenail Correction",
        "desc": "Professional Onyx treatment for ingrown toenails — fast relief & lasting results",
        "category": "specialty", "duration_min": 30, "price_call": True
    },
    "manicure": {"name": "Manicure", "desc": "Classic and spa manicure options", "category": "nails", "duration_min": 30, "price_call": True},
    "pedicure": {"name": "Pedicure", "desc": "Relaxing foot care — classic, spa, or deluxe", "category": "nails", "duration_min": 45, "price_call": True},
    "gel_nails": {"name": "Gel Nails", "desc": "Long-lasting high-gloss color, lasts 2-3 weeks", "category": "nails", "duration_min": 45, "price_call": True},
    "nail_extensions": {"name": "Nail Extensions", "desc": "Custom length, shape & design", "category": "nails", "duration_min": 60, "price_call": True},
    "waxing": {"name": "Waxing", "desc": "Professional hair removal — brows, lip, face, body", "category": "waxing", "duration_min": 15, "price_call": True},
    "ear_piercings": {"name": "Ear Piercings", "desc": "Safe, sterile, professional ear piercing", "category": "piercing", "duration_min": 15, "price_call": True},
    "nail_art": {"name": "Nail Art", "desc": "Custom designs for any occasion", "category": "nails", "duration_min": 30, "price_call": True},
}

# ─── BOOKING STORE (in-memory, replace with DB in prod) ───
bookings = []

def get_available_slots(days_ahead=14):
    slots = []
    now = datetime.now()
    for d in range(days_ahead):
        date = now + timedelta(days=d)
        wd = date.isoweekday()
        s = WEEKLY_SCHEDULE.get(wd)
        if s and s["status"] == "open":
            for hour in range(s["open_h"], s["close_h"]):
                for minute in [0, 30]:
                    slot_time = f"{hour:02d}:{minute:02d}"
                    slots.append({
                        "date": date.strftime("%Y-%m-%d"),
                        "day": s["day"],
                        "display_date": date.strftime("%A, %B %d"),
                        "time": f"{hour % 12 or 12}:{minute:02d} {'AM' if hour < 12 else 'PM'}",
                        "slot": slot_time
                    })
    return slots

# ─── PLUGIN & INTEGRATION CONFIG ───
PLUGINS = {
    "booking_form": {
        "name": "Online Booking Form",
        "status": "active",
        "endpoint": "/api/book",
        "description": "Appointment booking & scheduling"
    },
    "chatbot": {
        "name": "Quantum Sales Bot",
        "status": "active",
        "endpoint": "/api/bot/chat",
        "description": "AI sales & customer service chatbot"
    },
    "calendar_sync": {
        "name": "Calendar Sync",
        "status": "inactive",
        "endpoint": None,
        "description": "Sync bookings with Google Calendar / iCal"
    },
    "sms_reminders": {
        "name": "SMS Reminders",
        "status": "inactive",
        "endpoint": None,
        "description": "Automated appointment reminders via SMS"
    },
    "facebook_messenger": {
        "name": "Facebook Messenger Integration",
        "status": "inactive",
        "endpoint": None,
        "description": "Connect chatbot to Facebook page messenger"
    },
    "google_business": {
        "name": "Google Business Profile",
        "status": "inactive",
        "endpoint": None,
        "description": "Sync hours, services & booking to Google"
    },
    "reviews_collector": {
        "name": "Review Collector",
        "status": "inactive",
        "endpoint": None,
        "description": "Auto-collect Google & Facebook reviews"
    },
    "analytics": {
        "name": "Visitor Analytics",
        "status": "active",
        "endpoint": "/api/analytics",
        "description": "Site traffic & booking conversion tracking"
    },
    "whatsapp": {
        "name": "WhatsApp Business API",
        "status": "inactive",
        "endpoint": None,
        "description": "WhatsApp booking & customer communication"
    },
    "inventory": {
        "name": "Supply Inventory",
        "status": "inactive",
        "endpoint": None,
        "description": "Track nail polish, supplies & equipment"
    }
}

# ─── BOT ENGINE ───
def chat_response(message):
    msg = message.lower().strip()
    
    if any(w in msg for w in ["book", "appointment", "schedule", "available"]):
        slots = get_available_slots()
        return {
            "type": "booking",
            "text": f"📅 Available appointments (next 2 weeks):\n\nCall {PHONE} to book any of these slots:",
            "slots": slots[:14]
        }
    elif any(w in msg for w in ["ingrown", "toenail", "onyx"]):
        return {"type": "specialty", "text": "🦶 Ingrown toenail correction is our specialty! Onyx treatment — fast relief. Walk-ins welcome. Call (902) 885-7896."}
    elif any(w in msg for w in ["hours", "open", "time"]):
        hours = "\n".join([f"{v['day']}: {'Closed' if v['status']=='closed' else v['hours']}" for v in WEEKLY_SCHEDULE.values()])
        return {"type": "info", "text": f"🕐 Hours ({TIMEZONE}):\n{hours}\n\nCall {PHONE}"}
    elif any(w in msg for w in ["service", "price", "cost"]):
        svcs = "\n".join([f"• {v['name']}" for v in SERVICES.values()])
        return {"type": "info", "text": f"💅 Services:\n{svcs}\n\n📞 Call {PHONE} for pricing"}
    else:
        return {"type": "general", "text": f"✨ Welcome to Jeannie Boutiler Nails! I specialize in ingrown toenail correction, manicures, pedicures, gel nails, extensions, waxing & ear piercings.\n\n📞 Call {PHONE} to book or ask anything!"}

# ─── HTTP HANDLER ───
class APIHandler(BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def do_OPTIONS(self):
        self._send_json({})
    
    def do_GET(self):
        if self.path == "/api/health":
            self._send_json({"status": "ok", "version": API_VERSION, "site": SITE_URL, "phone": PHONE})
        elif self.path == "/api/services":
            self._send_json({"services": SERVICES})
        elif self.path == "/api/schedule":
            self._send_json({"schedule": WEEKLY_SCHEDULE, "timezone": TIMEZONE})
        elif self.path == "/api/book/slots":
            self._send_json({"slots": get_available_slots()})
        elif self.path == "/api/plugins":
            self._send_json({"plugins": PLUGINS})
        elif self.path == "/api/bot/health":
            self._send_json({"status": "ok", "bot": "Jeannie Nails Bot v1.0"})
        else:
            self._send_json({"error": "Not found"}, 404)
    
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length).decode()) if length else {}
        
        if self.path == "/api/bot/chat":
            msg = body.get("message", "")
            result = chat_response(msg)
            self._send_json(result)
        elif self.path == "/api/book":
            booking = {
                "id": hashlib.md5(str(time.time()).encode()).hexdigest()[:8],
                "name": body.get("name", ""),
                "phone": body.get("phone", ""),
                "service": body.get("service", ""),
                "date": body.get("date", ""),
                "time": body.get("time", ""),
                "notes": body.get("notes", ""),
                "created": datetime.now().isoformat()
            }
            bookings.append(booking)
            self._send_json({"status": "booked", "booking": booking})
        else:
            self._send_json({"error": "Not found"}, 404)

def run_server(port=8080):
    server = HTTPServer(("0.0.0.0", port), APIHandler)
    print(f"🚀 Jeannie Nails API running on port {port}")
    print(f"📋 Endpoints:")
    for p in ["/api/health", "/api/services", "/api/schedule", "/api/book/slots", "/api/plugins", "/api/bot/chat", "/api/bot/health", "/api/book"]:
        print(f"   {p}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        server.shutdown()

if __name__ == "__main__":
    run_server()
