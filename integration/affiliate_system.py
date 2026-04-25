#!/usr/bin/env python3
"""
ATV HOMES AFFILIATE SYSTEM — Stripe Connect Powered
====================================================
Full affiliate management with:
- Stripe Connect for payouts
- Unique referral link generation
- Commission tracking with retroactive tier upgrades
- Real-time dashboard data
- Two-tier referral (refer other affiliates = 1% of their sales)
"""

import json
import time
import os
import re
import secrets
import hashlib
import stripe
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

# Config
AFFILIATE_DATA_FILE = os.path.join(os.path.dirname(__file__), "affiliates.json")
COMMISSION_LOG_FILE = os.path.join(os.path.dirname(__file__), "commissions.json")
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "")

# Commission tiers (retroactive!)
TIERS = [
    {"min_sales": 0,  "rate": 0.05, "label": "Entry (5%)"},
    {"min_sales": 10, "rate": 0.07, "label": "Accelerated (7%)"},
    {"min_sales": 25, "rate": 0.10, "label": "Elite (10%)"},
]

# Two-tier: 1% on referred affiliates' sales
REFERRAL_COMMISSION_RATE = 0.01

# Prices by model slug
MODEL_PRICES = {
    "expandable": 1499500,    # $14,995
    "premium-20": 1999500,    # $19,995
    "deluxe-40": 2499500,     # $24,995
    "premium-40": 3499500,    # $34,995
}

class AffiliateManager:
    def __init__(self):
        self.affiliates = self._load(AFFILIATE_DATA_FILE, {})
        self.commissions = self._load(COMMISSION_LOG_FILE, {"transactions": [], "payouts": []})
    
    def _load(self, path, default):
        try:
            with open(path) as f:
                return json.load(f)
        except:
            return default
    
    def _save(self, path, data):
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def _save_all(self):
        self._save(AFFILIATE_DATA_FILE, self.affiliates)
        self._save(COMMISSION_LOG_FILE, self.commissions)
    
    def _generate_ref_code(self, name: str) -> str:
        """Generate a unique referral code from the affiliate's name."""
        base = re.sub(r'[^a-z0-9]', '', name.lower().replace(' ', ''))[:15]
        if not base:
            base = secrets.token_hex(4)
        # Make unique
        code = base
        counter = 0
        while code in self.affiliates:
            counter += 1
            code = f"{base}{counter}"
        return code
    
    def create_affiliate(self, name: str, email: str, platform: str = "",
                         referred_by: str = None, 
                         stripe_account_id: str = "") -> Dict:
        """Register a new affiliate."""
        code = self._generate_ref_code(name)
        
        affiliate = {
            "code": code,
            "name": name,
            "email": email,
            "platform": platform,
            "ref_link": f"https://atvhomes.com/?ref={code}",
            "stripe_account_id": stripe_account_id,
            "referred_by": referred_by or "",
            "total_sales": 0,
            "total_commission_cents": 0,
            "paid_commission_cents": 0,
            "pending_commission_cents": 0,
            "current_commission_rate": 0.05,
            "created_at": datetime.utcnow().isoformat(),
            "status": "active",  # active, suspended, paid_out
            "referrals": [],  # other affiliates they referred
            "sales_log": [],
        }
        
        self.affiliates[code] = affiliate
        
        # Add to referrer's list
        if referred_by and referred_by in self.affiliates:
            self.affiliates[referred_by]["referrals"].append(code)
        
        self._save_all()
        return affiliate
    
    def get_effective_rate(self, total_sales: int) -> Tuple[float, str]:
        """Get the commission rate for a given number of sales (retroactive)."""
        rate = TIERS[0]["rate"]
        label = TIERS[0]["label"]
        for tier in reversed(TIERS):  # Check highest first
            if total_sales >= tier["min_sales"]:
                rate = tier["rate"]
                label = tier["label"]
                break
        return rate, label
    
    def record_sale(self, ref_code: str, model_id: str, 
                    amount_cents: int = 0,
                    stripe_charge_id: str = "",
                    customer_email: str = "") -> Optional[Dict]:
        """
        Record a sale from an affiliate link.
        Automatically recalculates commission with retroactive tier upgrade.
        """
        if ref_code not in self.affiliates:
            return None
        
        aff = self.affiliates[ref_code]
        
        # Determine price from model or use provided amount
        price_cents = amount_cents or MODEL_PRICES.get(model_id, 14995)
        
        # Calculate commission (at CURRENT rate, not the rate at time of sale)
        commission_cents = int(price_cents * aff["current_commission_rate"])
        
        # Record the sale
        sale = {
            "ref_code": ref_code,
            "model_id": model_id,
            "price_cents": price_cents,
            "commission_cents": commission_cents,
            "stripe_charge_id": stripe_charge_id,
            "customer_email": customer_email,
            "timestamp": datetime.utcnow().isoformat(),
            "recalculated": False,
        }
        
        self.commissions["transactions"].append(sale)
        aff["sales_log"].append(sale)
        aff["total_sales"] += 1
        aff["total_commission_cents"] += commission_cents
        aff["pending_commission_cents"] += commission_cents
        
        # Check if this sale triggers a tier upgrade (retroactive!)
        new_rate, new_label = self.get_effective_rate(aff["total_sales"])
        if new_rate != aff["current_commission_rate"]:
            self._apply_retroactive_upgrade(ref_code, new_rate, new_label)
        
        self._save_all()
        return sale
    
    def _apply_retroactive_upgrade(self, ref_code: str, 
                                    new_rate: float, new_label: str):
        """
        Retroactively recalculate ALL past commissions at the new rate.
        This is the key competitive feature.
        """
        aff = self.affiliates[ref_code]
        old_rate = aff["current_commission_rate"]
        
        if new_rate <= old_rate:
            return
        
        # Recalculate all past sales
        retroactive_adjustment = 0
        for sale in aff["sales_log"]:
            if not sale.get("recalculated", False):
                old_commission = sale["commission_cents"]
                new_commission = int(sale["price_cents"] * new_rate)
                difference = new_commission - old_commission
                sale["commission_cents"] = new_commission
                sale["recalculated"] = True
                retroactive_adjustment += difference
        
        # Apply adjustment
        aff["total_commission_cents"] += retroactive_adjustment
        aff["pending_commission_cents"] += retroactive_adjustment
        aff["current_commission_rate"] = new_rate
        
        # Log the upgrade
        upgrade_log = {
            "type": "retroactive_upgrade",
            "ref_code": ref_code,
            "old_rate": old_rate,
            "new_rate": new_rate,
            "adjustment_cents": retroactive_adjustment,
            "total_sales_at_upgrade": aff["total_sales"],
            "timestamp": datetime.utcnow().isoformat(),
        }
        self.commissions["transactions"].append(upgrade_log)
    
    def process_payout(self, ref_code: str) -> Optional[Dict]:
        """
        Process a payout to an affiliate via Stripe Connect.
        Requires the affiliate to have a Stripe account connected.
        """
        aff = self.affiliates.get(ref_code)
        if not aff or aff["pending_commission_cents"] < 10000:  # $100 minimum
            return None
        
        payout_cents = aff["pending_commission_cents"]
        
        # If Stripe Connect is configured, process the transfer
        payout_stripe_id = ""
        try:
            if STRIPE_SECRET_KEY and aff.get("stripe_account_id"):
                stripe.api_key = STRIPE_SECRET_KEY
                transfer = stripe.Transfer.create(
                    amount=payout_cents,
                    currency="usd",
                    destination=aff["stripe_account_id"],
                    description=f"ATV Homes affiliate payout — {aff['name']}",
                )
                payout_stripe_id = transfer.get("id", "")
        except Exception as e:
            print(f"Stripe payout failed for {ref_code}: {e}")
            # Still record the payout, mark as manual
            pass
        
        payout = {
            "ref_code": ref_code,
            "amount_cents": payout_cents,
            "stripe_transfer_id": payout_stripe_id,
            "timestamp": datetime.utcnow().isoformat(),
            "status": "processed" if payout_stripe_id else "pending_manual",
        }
        
        self.commissions["payouts"].append(payout)
        aff["paid_commission_cents"] += payout_cents
        aff["pending_commission_cents"] = 0
        aff["status"] = "paid_out"
        
        self._save_all()
        return payout
    
    def get_affiliate_dashboard(self, ref_code: str) -> Optional[Dict]:
        """Get full dashboard data for an affiliate."""
        aff = self.affiliates.get(ref_code)
        if not aff:
            return None
        
        # Calculate next tier
        current_tier_idx = 0
        for i, tier in enumerate(TIERS):
            if aff["total_sales"] >= tier["min_sales"]:
                current_tier_idx = i
        
        next_tier = None
        sales_to_next = 0
        if current_tier_idx < len(TIERS) - 1:
            next_tier = TIERS[current_tier_idx + 1]
            sales_to_next = next_tier["min_sales"] - aff["total_sales"]
        
        # Calculate if retroactive upgrade would apply
        projected_rate, projected_label = self.get_effective_rate(aff["total_sales"])
        retroactive_bump = 0
        if projected_rate > aff["current_commission_rate"]:
            retroactive_bump = int(aff["total_commission_cents"] * 
                                   (projected_rate / aff["current_commission_rate"] - 1))
        
        # Referral commissions
        referral_earnings = 0
        for ref in aff["referrals"]:
            if ref in self.affiliates:
                referral_earnings += int(
                    self.affiliates[ref]["total_commission_cents"] * REFERRAL_COMMISSION_RATE
                )
        
        return {
            "affiliate": {
                "name": aff["name"],
                "code": aff["code"],
                "email": aff["email"],
                "ref_link": aff["ref_link"],
                "status": aff["status"],
                "created_at": aff["created_at"],
            },
            "stats": {
                "total_sales": aff["total_sales"],
                "current_rate": aff["current_commission_rate"],
                "current_label": f"{int(aff['current_commission_rate'] * 100)}%",
                "total_commission": f"${aff['total_commission_cents'] / 100:.2f}",
                "paid": f"${aff['paid_commission_cents'] / 100:.2f}",
                "pending": f"${aff['pending_commission_cents'] / 100:.2f}",
                "referral_earnings": f"${referral_earnings:.2f}",
            },
            "next_tier": {
                "tier": next_tier["label"] if next_tier else None,
                "sales_needed": sales_to_next if next_tier else 0,
                "rate": f"{int(next_tier['rate'] * 100)}%" if next_tier else None,
                "retroactive_bump": f"${retroactive_bump / 100:.2f}" if retroactive_bump else "$0.00",
            } if next_tier else None,
            "recent_sales": aff["sales_log"][-5:] if aff["sales_log"] else [],
        }
    
    def generate_dashboard_api_response(self) -> Dict:
        """Generate the /api/v1/affiliate/dashboard endpoint response."""
        total_affiliates = len(self.affiliates)
        total_sales = sum(a["total_sales"] for a in self.affiliates.values())
        total_commission = sum(a["total_commission_cents"] for a in self.affiliates.values())
        total_paid = sum(a["paid_commission_cents"] for a in self.affiliates.values())
        
        return {
            "stats": {
                "total_affiliates": total_affiliates,
                "total_sales": total_sales,
                "total_commission_cents": total_commission,
                "total_paid_cents": total_paid,
                "total_pending_cents": total_commission - total_paid,
            },
            "tiers": [
                {"label": t["label"], "rate": f"{int(t['rate']*100)}%", 
                 "min_sales": t["min_sales"]}
                for t in TIERS
            ],
            "affiliates": [
                {"name": a["name"], "code": a["code"], "email": a["email"],
                 "total_sales": a["total_sales"], 
                 "commission_cents": a["total_commission_cents"],
                 "pending_cents": a["pending_commission_cents"]}
                for a in self.affiliates.values()
                if a["status"] == "active"
            ],
        }


# Example usage
if __name__ == "__main__":
    am = AffiliateManager()
    
    print("ATV HOMES AFFILIATE SYSTEM")
    print("=" * 50)
    print()
    
    # Demo: Create affiliates and simulate sales
    print("1. Creating affiliate: Sarah (YouTube reviewer)")
    sarah = am.create_affiliate("Sarah Johnson", "sarah@example.com", "YouTube")
    print(f"   Ref code: {sarah['code']}")
    print(f"   Link: {sarah['ref_link']}")
    print()
    
    print("2. Recording 11 sales for Sarah (triggers retroactive upgrade at 10)")
    for i in range(11):
        model = list(MODEL_PRICES.keys())[i % 4]
        am.record_sale(sarah['code'], model)
    
    s_dash = am.get_affiliate_dashboard(sarah['code'])
    print(f"   Total sales: {s_dash['stats']['total_sales']}")
    print(f"   Current rate: {s_dash['stats']['current_label']}")
    print(f"   Total commission: {s_dash['stats']['total_commission']}")
    print(f"   Next tier: {s_dash['next_tier']['tier']} "
          f"({s_dash['next_tier']['sales_needed']} sales away)")
    print()
    
    print("3. Creating referral affiliate: Mike (referred by Sarah)")
    mike = am.create_affiliate("Mike Chen", "mike@example.com", "Blog", 
                                referred_by=sarah['code'])
    print(f"   Mike's ref code: {mike['code']}")
    print(f"   Sarah's referrals: {am.affiliates[sarah['code']]['referrals']}")
    print()
    
    print("4. Recording 5 sales for Mike")
    for i in range(5):
        am.record_sale(mike['code'], 'expandable')
    
    m_dash = am.get_affiliate_dashboard(mike['code'])
    print(f"   Mike's commission: {m_dash['stats']['total_commission']}")
    print(f"   Mike's pending: {m_dash['stats']['pending']}")
    
    # Sarah gets 1% of Mike's sales as referral bonus
    print(f"   Sarah's referral earnings: {s_dash['stats']['referral_earnings']}")
