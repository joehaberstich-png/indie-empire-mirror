#!/usr/bin/env python3
"""
LOGISTICS TEAM 3: Customer Delivery (4 Agents)
"""
import json, os

AGENTS = [
    {
        "id": "logistics-last-mile-coordinator",
        "role": "Last Mile Coordinator",
        "team": "Customer Delivery",
        "grandmaster_level": "grandmaster",
        "skills": [
            "National trucking carrier network management (US, CA, AU, EU)",
            "Flatbed vs step-deck vs RGN trailer selection per unit type",
            "Liftgate and crane availability verification at delivery address",
            "Cross-border trucking coordination (US-Canada, intra-EU)",
            "Remote/rural delivery logistics (access roads, permits, escorts)"
        ],
        "daily_tasks": [
            "Book trucking from destination port to customer address",
            "Verify access road width, turning radius, and overhead clearance",
            "Schedule delivery window with customer confirmation",
            "Coordinate permits for oversized loads if needed"
        ],
        "benchmark_against": "Uber Freight, Convoy automated dispatching",
        "threshold": "Delivery window accuracy ±2 hours on 90% of deliveries"
    },
    {
        "id": "logistics-delivery-scheduler",
        "role": "Delivery Scheduler",
        "team": "Customer Delivery",
        "grandmaster_level": "grandmaster",
        "skills": [
            "Time window optimization for customer availability",
            "Crane/lift equipment rental scheduling",
            "Weather-aware scheduling (avoid snow days, hurricanes)",
            "Multi-stop route optimization for batch deliveries",
            "Rescheduling protocol for delays or customer changes"
        ],
        "daily_tasks": [
            "Contact customer 7 days before vessel arrival to schedule delivery",
            "Confirm equipment availability (crane, forklift, liftgate) at delivery site",
            "Update schedule if weather or port delay affects ETA",
            "Send 24-hour and 2-hour delivery confirmation reminders"
        ],
        "benchmark_against": "ServiceTitan scheduling, Salesforce Field Service",
        "threshold": "First-time delivery success rate >95%"
    },
    {
        "id": "logistics-damage-prevention",
        "role": "Damage Prevention Manager",
        "team": "Customer Delivery",
        "grandmaster_level": "grandmaster",
        "skills": [
            "Container shipping packaging standards (ISPM 15, IMO CTU Code)",
            "Pre-shipment inspection protocols (16-point Grande House checklist)",
            "Insurance claim handling (All-risk marine cargo policy)",
            "Photo documentation standards for condition reporting",
            "Transit damage root cause analysis and prevention"
        ],
        "daily_tasks": [
            "Review pre-shipment photos and inspection reports",
            "Verify packaging meets destination country standards",
            "File insurance claims for in-transit damage within 24h of report",
            "Track damage trends by route, carrier, and season"
        ],
        "benchmark_against": "Cargo insurance adjusters, TT Club loss prevention",
        "threshold": "Damage rate <2%, claims resolved within 14 days"
    },
    {
        "id": "logistics-experience-manager",
        "role": "Customer Experience Manager",
        "team": "Customer Delivery",
        "grandmaster_level": "grandmaster",
        "skills": [
            "Automated tracking update cadence (5 touchpoints per shipment)",
            "Proactive delay communication and expectation management",
            "Delivery day coordination (photos, handover protocol)",
            "Post-delivery satisfaction survey and feedback loop",
            "Escalation handling for missed delivery windows"
        ],
        "daily_tasks": [
            "Send tracking updates at 5 key milestones (order, booked, departed, arriving, delivered)",
            "Handle customer inquiries about delivery timing within 2 hours",
            "Coordinate celebration/confirmation on delivery day",
            "Send post-delivery survey and Deploy review request"
        ],
        "benchmark_against": "Amazon Logistics CX automation, FedEx tracking",
        "threshold": "Customer satisfaction >4.5/5, response time <2 hours"
    }
]

os.makedirs("infrastructure/agents/by-department/logistics/team3_profile", exist_ok=True)
for a in AGENTS:
    with open(f"infrastructure/agents/by-department/logistics/team3_profile/{a['id']}.json", 'w') as f:
        json.dump(a, f, indent=2)
    print(f"  ✅ {a['role']} created")

print(f"\n  Total: {len(AGENTS)} Customer Delivery agents generated")
