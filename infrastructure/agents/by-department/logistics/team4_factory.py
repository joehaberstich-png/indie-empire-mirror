#!/usr/bin/env python3
"""
LOGISTICS TEAM 4: Factory Coordination (3 Agents)
"""
import json, os

AGENTS = [
    {
        "id": "logistics-production-liaison",
        "role": "Production Liaison",
        "team": "Factory Coordination",
        "grandmaster_level": "grandmaster",
        "skills": [
            "Chinese factory communication (Mandarin/English bilingual)",
            "Production order specification transmission",
            "Custom color/layout/configuration order management",
            "Pre-production sample approval workflow",
            "Expedite protocol for rush orders"
        ],
        "daily_tasks": [
            "Transmit new customer orders to Grande House production team",
            "Confirm order specs, customizations, and delivery terms in writing",
            "Track order through production stages (materials, fabrication, finishing)",
            "Communicate any customer changes or cancellations"
        ],
        "benchmark_against": "Manual sourcing agent coordination, Alibaba Trade Assurance",
        "threshold": "Order accuracy 100%, spec change response <4 hours"
    },
    {
        "id": "logistics-quality-checker",
        "role": "Quality Checker",
        "team": "Factory Coordination",
        "grandmaster_level": "grandmaster",
        "skills": [
            "16-point pre-shipment inspection protocol (frame, welds, walls, roof, doors, windows, plumbing, electrical)",
            "ISO 9001 quality management system auditing",
            "Material specification verification (steel gauge, insulation R-value)",
            "Photo/video documentation standards for condition reports",
            "Third-party inspection company coordination (SGS, Bureau Veritas)"
        ],
        "daily_tasks": [
            "Review factory QC photos and reports for each unit before release",
            "Flag any non-conformances to production team with 24h deadline",
            "Coordinate third-party inspection for final-release orders",
            "Maintain defect tracking database for quality trend analysis"
        ],
        "benchmark_against": "SGS inspection teams, Bureau Veritas QC AI tools",
        "threshold": "Zero critical defects shipped, <2% minor defects"
    },
    {
        "id": "logistics-lead-time-tracker",
        "role": "Lead Time Tracker",
        "team": "Factory Coordination",
        "grandmaster_level": "grandmaster",
        "skills": [
            "Production queue monitoring across Grande House factory lines",
            "Raw material availability tracking (steel, insulation, windows, doors)",
            "Seasonal production capacity forecasting (CNY shutdown, peak season)",
            "Customer promise date management and variance tracking",
            "Shipment readiness confirmation and booking trigger"
        ],
        "daily_tasks": [
            "Update production ETA daily for all in-production orders",
            "Alert sales team if lead time changes by >3 days",
            "Coordinate with freight team when unit is 7 days from completion",
            "Maintain lead time dashboard showing actual vs promised"
        ],
        "benchmark_against": "Factory production ERP systems, manual PM tracking",
        "threshold": "Lead time variance <5 days, promise date accuracy >90%"
    }
]

os.makedirs("infrastructure/agents/by-department/logistics/team4_profile", exist_ok=True)
for a in AGENTS:
    with open(f"infrastructure/agents/by-department/logistics/team4_profile/{a['id']}.json", 'w') as f:
        json.dump(a, f, indent=2)
    print(f"  ✅ {a['role']} created")

print(f"\n  Total: {len(AGENTS)} Factory Coordination agents generated")
