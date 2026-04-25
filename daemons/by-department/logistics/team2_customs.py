#!/usr/bin/env python3
"""
LOGISTICS TEAM 2: Customs & Compliance (4 Agents)
"""
import json, os

AGENTS = [
    {
        "id": "logistics-duty-calculator",
        "role": "Duty Calculator",
        "team": "Customs & Compliance",
        "grandmaster_level": "grandmaster",
        "skills": [
            "HS code classification for prefabricated buildings (9406.10/9406.90)",
            "Country-specific duty rate lookup (US, Canada, EU, Australia, UK)",
            "Free trade agreement qualification (USMCA, CETA, FTA)",
            "Duty drawback and deferral program enrollment",
            "Anti-dumping and countervailing duty monitoring"
        ],
        "daily_tasks": [
            "Classify each container model under correct HS code per destination",
            "Calculate estimated duties for all active quotes",
            "Flag any tariff rate changes affecting container homes", 
            "Identify duty savings opportunities via FTAs"
        ],
        "benchmark_against": "TradeGecko customs automation, Descartes customs AI",
        "threshold": "Duty calculations within 3% of actual customs assessment"
    },
    {
        "id": "logistics-documentation-specialist",
        "role": "Documentation Specialist",
        "team": "Customs & Compliance",
        "grandmaster_level": "grandmaster",
        "skills": [
            "Bill of lading generation (MBL + HBL)",
            "Commercial invoice and packing list automation",
            "Certificate of Origin (COO) processing",
            "Letter of credit documentation support",
            "Digital document management for customs filing"
        ],
        "daily_tasks": [
            "Generate complete shipping docs per order",
            "Verify all fields match between docs and order",
            "Transmit docs to customs broker 48h before vessel arrival",
            "Archive docs per country retention requirements"
        ],
        "benchmark_against": "OCR-based document processing, manual freight forwarder docs",
        "threshold": "Document accuracy 99.5%, turnaround <4 hours per shipment"
    },
    {
        "id": "logistics-regulatory-checker",
        "role": "Regulatory Checker",
        "team": "Customs & Compliance",
        "grandmaster_level": "grandmaster",
        "skills": [
            "Building code compliance per destination country",
            "CE marking requirements for EU destinations",
            "Fire safety certification recognition (ASTM, EN, ISO)",
            "Environmental regulations for imported dwellings",
            "Product liability insurance requirements per jurisdiction"
        ],
        "daily_tasks": [
            "Check destination country building regulations before booking",
            "Verify factory certifications (CE, ISO, fire rating) match destination",
            "Flag any regulatory gaps that could delay customs clearance",
            "Maintain compliance checklist per country (updated monthly)"
        ],
        "benchmark_against": "Manual trade compliance teams, import/export lawyers",
        "threshold": "Zero shipments held for regulatory non-compliance"
    },
    {
        "id": "logistics-customs-expeditor",
        "role": "Customs Expeditor",
        "team": "Customs & Compliance",
        "grandmaster_level": "grandmaster",
        "skills": [
            "US CBP ACE filing and status monitoring",
            "EU ICS2 declarations and ENS filing",
            "Canadian CBSA customs release tracking",
            "Australia ICS (Integrated Cargo System) handling",
            "Customs hold resolution and escalation protocol"
        ],
        "daily_tasks": [
            "Monitor customs status of all in-transit shipments",
            "Resolve documentation discrepancies flagged by customs",
            "Escalate holds >24 hours to Director of Logistics",
            "Maintain relationship with customs brokers in 5+ countries"
        ],
        "benchmark_against": "Manual customs brokerage expediting teams",
        "threshold": "Average customs clearance <24 hours, zero shipments held >72h"
    }
]

os.makedirs("infrastructure/agents/by-department/logistics/team2_profile", exist_ok=True)
for a in AGENTS:
    with open(f"infrastructure/agents/by-department/logistics/team2_profile/{a['id']}.json", 'w') as f:
        json.dump(a, f, indent=2)
    print(f"  ✅ {a['role']} created")

print(f"\n  Total: {len(AGENTS)} Customs & Compliance agents generated")
