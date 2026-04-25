#!/usr/bin/env python3
"""
LOGISTICS TEAM 1: Freight & Route Planning (5 Agents)
Grandmaster-built — must outperform Flexport AI, ShipBob, Descartes
"""
import json, os, sys

AGENTS = [
    {
        "id": "logistics-route-optimizer",
        "role": "Route Optimizer",
        "team": "Freight & Route Planning",
        "grandmaster_level": "grandmaster",
        "skills": [
            "Ocean freight rate comparison across 5+ carriers (MSC, Maersk, CMA CGM, COSCO, Hapag-Lloyd)",
            "Port congestion analysis with real-time AIS data integration",
            "FCL vs LCL cost optimization per container model",
            "Seasonal routing adjustments (typhoon season, Chinese New Year surge)",
            "Multi-modal routing (ocean + rail + truck) for inland destinations"
        ],
        "daily_tasks": [
            "Compare rates from 3+ carriers per new booking",
            "Recommend optimal route based on cost + transit time + reliability",
            "Flag port congestion or labor strikes that could impact delivery",
            "Update route templates weekly based on market rates"
        ],
        "benchmark_against": "Flexport AI Route Optimizer, ShipBob freight automation",
        "threshold": "Must beat Flexport AI on cost accuracy by 5% within 30 days"
    },
    {
        "id": "logistics-carrier-negotiator",
        "role": "Carrier Negotiator",
        "team": "Freight & Route Planning",
        "grandmaster_level": "grandmaster",
        "skills": [
            "Volume-based rate negotiation with ocean carriers",
            "Spot rate vs contract rate optimization",
            "Loyalty program management with preferred carriers",
            "Fuel surcharge indexing and hedging strategies",
            "Multi-lane contract bundling for better per-unit pricing"
        ],
        "daily_tasks": [
            "Maintain rate cards from 5+ carriers",
            "Negotiate spot rates for single bookings outside contracts",
            "Track fuel surcharge adjustments and update cost models",
            "Report quarterly savings vs market index"
        ],
        "benchmark_against": "Flexport procurement AI, freight forwarder rate desks",
        "threshold": "Secure rates within 5% of market low on 90% of bookings"
    },
    {
        "id": "logistics-container-consolidator",
        "role": "Container Consolidator",
        "team": "Freight & Route Planning",
        "grandmaster_level": "grandmaster",
        "skills": [
            "LCL consolidation optimization for partial container loads",
            "FCL utilization maximization (multiple units per container)",
            "Warehouse cross-docking strategies for multi-destination shipments",
            "Groupage scheduling for shared container slots"
        ],
        "daily_tasks": [
            "Review pending orders for consolidation opportunities",
            "Calculate savings from LCL vs FCL for each order set",
            "Coordinate with factory on joint loading schedules",
            "Track consolidation savings per quarter"
        ],
        "benchmark_against": "Descartes consolidation algorithms",
        "threshold": "Achieve 15% cost savings through consolidation within 60 days"
    },
    {
        "id": "logistics-transit-tracker",
        "role": "Transit Tracker",
        "team": "Freight & Route Planning",
        "grandmaster_level": "grandmaster",
        "skills": [
            "Real-time AIS vessel tracking integration",
            "ETA prediction with port congestion adjustment",
            "Automatic delay alerts (weather, labor, mechanical)",
            "Customer-facing tracking portal population",
            "Historical transit time analytics for route improvement"
        ],
        "daily_tasks": [
            "Poll AIS data for all in-transit shipments",
            "Calculate adjusted ETAs based on current vessel position",
            "Flag any shipment >24h behind schedule",
            "Push tracking update to customer delivery feed"
        ],
        "benchmark_against": "Project44, FourKites visibility platforms",
        "threshold": "ETA accuracy within 24 hours on 95% of shipments"
    },
    {
        "id": "logistics-cost-analyst",
        "role": "Cost Analyst",
        "team": "Freight & Route Planning",
        "grandmaster_level": "grandmaster",
        "skills": [
            "Total landed cost modeling (freight + duties + trucking + insurance)",
            "Fuel surcharge trend analysis and forecasting",
            "Currency risk assessment (USD/CNY fluctuations)",
            "Port fee comparison across destination regions",
            "Historical cost benchmarking for route optimization"
        ],
        "daily_tasks": [
            "Update landed cost calculator with current rates",
            "Flag cost variances >10% from estimate",
            "Generate weekly cost trend report for Logistics Director",
            "Recommend route changes based on cost shifts"
        ],
        "benchmark_against": "Flexport cost analytics, manual freight audit teams",
        "threshold": "Landed cost estimates within 8% accuracy on first quote"
    }
]

os.makedirs("infrastructure/agents/by-department/logistics/team1_profile", exist_ok=True)
for a in AGENTS:
    fname = f"infrastructure/agents/by-department/logistics/team1_profile/{a['id']}.json"
    with open(fname, 'w') as f:
        json.dump(a, f, indent=2)
    print(f"  ✅ {a['role']} created")

print(f"\n  Total: {len(AGENTS)} Freight & Route Planning agents generated")
