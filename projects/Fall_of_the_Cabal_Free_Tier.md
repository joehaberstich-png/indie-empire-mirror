## Free Tier — Recruit Access

### Who Gets It
- **Everyone** — signing up with email creates a free Recruit account
- No payment required. No credit card. Just email verification.

### What They Get

| Feature | Free Tier (Recruit) | Paid Membership (Operative+) |
|---------|-------------------|-----------------------------|
| **Map access** | 3 zones unlocked only | Full world map + all DLC zones |
| **Zones** | Tutorial Hub, Safe Zone Alpha, Training Grounds | All 50+ countries + underground networks |
| **Missions** | 5 tutorial missions (intro to lore + mechanics) | Full campaign Act 1-5 + side ops + daily contracts |
| **NFT drops** | 0 (can view NFT store, cannot purchase) | Full NFT marketplace access |
| **Safehouses** | 1 basic safehouse (pre-set, no customization) | Build + customize unlimited safehouses |
| **Weapons** | 1 handgun (standard issue) | Full arsenal: rifles, drones, cyber tools, EMP |
| **Vehicles** | 1 sedan (no upgrades) | Any vehicle + full customization |
| **Intel reports** | None | Weekly classified intel |
| **Multiplayer** | Observe only (spectator mode) | Full PvP + co-op + faction wars |
| **Leaderboard** | View only | Ranked + rewards |
| **Faction alliance** | Cannot join | Join any faction + earn faction NFTs |

### Free Zone Map

```
                    ┌─────────────────────┐
                    │  TUTORIAL HUB        │
                    │  (Free - Learn lore) │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │  SAFE ZONE ALPHA     │
                    │  (Free - Social hub) │
                    │  Browse store only   │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │  TRAINING GROUNDS    │
                    │  (Free - Basic PvE)  │
                    │  5 intro missions    │
                    └─────────────────────┘

                    ╔══════════════════════╗
                    ║   EVERYTHING ELSE    ║
                    ║   (LOCKED - PAYWALL) ║
                    ║   Full world map     ║
                    ║   All campaigns      ║
                    ║   NFT marketplace     ║
                    ║   PvP / factions      ║
                    ╚══════════════════════╝
```

### Conversion Funnel

| Step | Action | Free User Does | Conversion Trigger |
|------|--------|---------------|-------------------|
| 1 | Sign up | Get free account | — |
| 2 | Tutorial 1-3 | Learn controls, witness a conspiracy | Lore teaser cliffhanger |
| 3 | Tutorial 4 | Complete first mission | "Act 1 begins in 24h. Unlock now." |
| 4 | Safe Zone Alpha | Browse NFT store, window shop | See other players' Legendary NFTs |
| 5 | Training Grounds | Fight 5 intro PvE waves | Wave 5 boss is unbeatable without upgrades |
| 6 | **Conversion** | "Your free access expires in 7 days" | **→ Recruit ($99/mo) or higher** |

### Free Tier Time Limit

| Duration | Access | After Expiry |
|----------|--------|-------------|
| **7 days free** | Tutorial Hub + Safe Zone Alpha + Training Grounds | Account paused — all progress saved |
| **After 7 days** | Cannot enter game zones | Can still browse NFT store + chat in lobby |
| **Upgrade anytime** | Unlocks all paid content retroactively | Progress carries over |

### Marketing Hook for Free Tier

> *"The world's secrets are hidden in plain sight. You've seen the first three clues. The real conspiracy starts at the border of Safe Zone Alpha. Your 7-day free pass gives you a taste. What happens next is up to you."*

### Technical Implementation

| Requirement | Implementation |
|-------------|---------------|
| Registration | Email + password. No payment info. |
| Free tier storage | 100MB per account (basic profile + tutorial progress) |
| Timer tracking | Server-side `trial_expires_at` field |
| Expiry enforcement | Game client checks `account.tier` on every zone load |
| Conversion | In-game "Upgrade" button → Stripe checkout (Recruit tier) |
| Data retention | 90 days after trial expiry before account purge (with 3 email warnings) |
| Free tier to subscription | Full progress carry-over. No restart needed. |

### Stripe Checkout Integration

The free tier checkout maps to:
```
Product: fotc-recruit
Type: subscription (recurring)
Price: $99/mo
Success URL: /checkout/membership-success.html?tier=recruit
Metadata: project=fall-of-the-cabal, membership_tier=recruit
```
