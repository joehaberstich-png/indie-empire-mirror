# Fall of the Cabal — NFT Store & Marketplace Operations v4

---

## 🏪 Primary NFT Store (Stripe Checkout → XRPL Mint)

The initial sale. Players buy NFTs with fiat (credit card/Apple Pay) via Stripe Checkout. Backend mints on XRPL and delivers to their wallet.

### Payment Flow
```
Player → NFT Store (Stripe Checkout) 
    → Payment Confirmed (Stripe Webhook)
    → Mint Queue
    → XRPL NFTokenMint (Mainnet/Testnet)
    → Wallet Delivery (XUMM / Crossmark)
    → Receipt + In-Game Notification
```

### Store Categories

| Category | Content | Price Range | Commission on Sale |
|----------|---------|-------------|-------------------|
| **Normal** | Base intel docs, generic identities, starter weapons | $1-$5 | — |
| **Uncommon** | Wiretaps, diplomatic passports, SMGs, sports cars | $5-$20 | 15% |
| **Rare** | Classified files, military ID, assault rifles, helicopters | $20-$50 | 15% |
| **Epic** | Operation dossiers, deep cover IDs, prototype weapons, private jets | $50-$150 | 20% |
| **Legendary** | Complete intel sets, ghost identities, golden weapons, stealth fighters | $150-$500 | 25% |
| **Mythic** | One-of-a-kind assets — only 10 minted per item | Auction | 30% |
| **Mystic** | The rarest — 1-3 minted per item in the entire game lifecycle | Auction | 35% |

### Founders Token — First 1,000 Paid Subscribers

| Detail | Value |
|--------|-------|
| **Who gets it** | First 1,000 players who subscribe to any paid membership tier |
| **How** | Auto-minted to wallet within 24h of first subscription payment |
| **Cost** | **Free** with membership — not a separate purchase |
| **Supply** | 1,000 max — numbered FP-001 to FP-1000 |
| **Binding** | Soulbound — cannot be traded or sold |
| **Benefit** | Quarterly royalty split, Founder Channel, credits, permanent +25% Intel bonus |
| **Mint trigger** | Stripe webhook `checkout.session.completed` → `subscription.created` → queue mint |

> The Founders Token is a thank-you to the first 1,000 believers. It's not for sale. You subscribe, you get it. No other way.

---

## 🧭 Hunted Founders Token — 100 Hidden In-Game

| Detail | Value |
|--------|-------|
| **Supply** | 100 max — numbered FH-001 to FH-100 |
| **How to get** | **Cannot be bought.** Found by exploring the paid world map. |
| **Rarity** | <0.0001% per zone — rarer than Mystic |
| **Requirement** | Active paid membership |
| **Announcement** | Global server broadcast when each one is found |
| **Binding** | Soulbound — cannot be traded or sold |
| **Perks** | +50% Intel bonus, "The Unseen" title, Phantom gear skin, permanent top leaderboard slot |

---

## 🔄 Secondary Marketplace (P2P Trading)

Players can buy, sell, and auction their NFTs with each other. **We take commission on every transaction.**

### Marketplace Fee Structure

| Fee Type | Rate | Who Pays | Purpose |
|----------|------|----------|---------|
| **Sale Commission** | 5% | Seller | Platform fee on every P2P sale |
| **Artwork Commission** | 3% | Seller | Paid to original NFT artist (split from sale) |
| **Creation Commission** | 2% | Seller | Paid to the game studio (minting + infrastructure) |
| **Auction Reserve** | 10% | Seller | When listing via auction (covers gas + platform) |
| **Resale Royalty** | 10% | Buyer | On every subsequent resale of an NFT |
| **Listing Fee** | $0.50 | Seller | Flat fee per listing (prevents spam) |
| **Buyout Fee** | 1% | Buyer | Instant buyout premium |
| **Total per sale** | **~18-30%** | Both sides | Varies by sale type |

### Example Transaction

```
Player A sells a Rare "Wiretap" NFT to Player B for $50

$50.00  → Sale price
 - $2.50  → Sale Commission (5%)
 - $1.50  → Artwork Commission (3%)   → paid to the original artist
 - $1.00  → Creation Commission (2%)  → game studio revenue
 - $0.50  → Listing Fee
───────
$44.50  → Player A receives
$5.50   → Platform retains (11% net)

Plus: $5.00  → Resale Royalty from Buyer B (10%) → platform retains
Total platform revenue from this sale: $10.50 (21%)
```

### Marketplace Revenue Projection

| Month | Estimated Volume | Commission (avg 20%) | Monthly Revenue |
|-------|-----------------|---------------------|-----------------|
| Month 1-3 (closed alpha) | $5,000 | $1,000 | Minimal testing |
| Month 4-6 (beta) | $50,000 | $10,000 | Early adopters |
| Month 7-9 (post-launch) | $250,000 | $50,000 | Growing |
| Month 10-12 | $1,000,000 | $200,000 | Volume + new players |
| Year 2 (mature) | $5,000,000 | $1,000,000 | Established economy |

### Smart Contract: P2P Marketplace

The marketplace runs on XRP Ledger with trust lines and escrow:

```
XRPL Smart Contract (escrow):
├── Seller lists NFT with price
├── Buyer sends funds to escrow
├── Smart contract holds 20% commission
├── NFT transfers from Seller wallet → Buyer wallet
├── 80% of funds released to Seller
├── 12% released to platform wallet (sale + creation commission)
├── 5% released to original artist wallet
└── 3% released to creation fund (infrastructure/development)
```

### Commission Distribution

```
Commission Pool ($100 total on a $500 sale)
├── 10% ($50) → Platform (Fall of the Cabal Treasury)
│   ├── 40% → Development fund
│   ├── 30% → Marketing/user acquisition
│   ├── 20% → Operations & support
│   └── 10% → Founder distribution pool
├── 5% ($25) → Original Artist (artwork commission)
├── 3% ($15) → Creation Fund (new NFT design + minting costs)
└── 2% ($10) → Infrastructure (XRPL fees, server costs, gas subsidies)

Total retained by platform: 20% ($100)
Total distributed to creators: 5% ($25)
Total operational overhead: 5% ($25)
```

---

## 💎 Artwork & Creation Commissions

### Artwork Commission (3%)
- **Paid to:** The original digital artist who created the NFT artwork
- **Trigger:** Every time their NFT is sold on the secondary market
- **Lifetime:** Forever — even if the NFT changes hands 100x
- **Payment:** Auto-paid to artist's XRP wallet via smart contract
- **Minimum payout:** $5 (accumulates until threshold)

### Creation Commission (2%)
- **Paid to:** The game studio (us)
- **Covers:** Minting costs, design costs, infrastructure, tooling
- **Trigger:** Every secondary market sale
- **Vesting:** Available immediately, no lockup

### Artist Registration
1. Artist submits portfolio for review
2. Approved artists get XRP wallet registered in marketplace
3. Artist creates NFT designs → submits to curation team
4. Approved designs minted and listed in Primary Store
5. Artist receives 3% of every future resale. Forever.

---

## 🔗 Stripe Integration (Updated)

### Product Map for Stripe Checkout

| Product ID | Type | Price | Success Page |
|-----------|------|-------|-------------|
| `fotc-normal-nft` | One-time payment | $99 | /checkout/nft-success.html |
| `fotc-uncommon-nft` | One-time payment | $249 | /checkout/nft-success.html |
| `fotc-rare-nft` | One-time payment | $499 | /checkout/nft-success.html |
| `fotc-epic-nft` | One-time payment | $999 | /checkout/nft-success.html |
| `fotc-legendary-nft` | One-time payment | $2,499 | /checkout/nft-success.html |
| `fotc-mystic-nft` | One-time payment | $4,999 | /checkout/nft-success.html |
| `fotc-founder-token` | One-time payment | $9,999 | /checkout/nft-success.html |
| `fotc-whale-pack` | One-time payment | $9,999 | /checkout/nft-success.html |
| `fotc-act1-pass` | One-time payment | $499 | /checkout/nft-success.html |
| `fotc-full-campaign` | One-time payment | $2,499 | /checkout/nft-success.html |
| `fotc-mantle-tier` | One-time payment | $9,999 | /checkout/nft-success.html |
| `fotc-recruit` | Subscription | $99/mo | /checkout/membership-success.html |
| `fotc-operative` | Subscription | $249/mo | /checkout/membership-success.html |
| `fotc-strategist` | Subscription | $499/mo | /checkout/membership-success.html |
| `fotc-architect-mantle` | Subscription | $999/mo | /checkout/membership-success.html |
| `fotc-cabal-insider` | Subscription | $1,999/mo | /checkout/membership-success.html |
| `fotc-free-recruit` | Setup (no charge) | $0 | /checkout/trial-activated.html |
| `fotc-hunted-founder` | **BLOCKED (403)** | N/A | Must be found in-game |

### Memberships Include Free Founder Token

When `fotc-recruit` (or higher) subscription payment succeeds → webhook checks:
1. Total minted Founder Tokens < 1,000?
2. If yes → queue auto-mint to subscriber's wallet
3. If no (all 1,000 claimed) → no token, but subscriber gets a "Close but missed it" consolation item

Auto-mint metadata: `token_type=founders_pledge`, `reason=first_1000_subscribers`

---

## 🛡️ Soulbound Enforcement

| Token | Tradable? | Why |
|-------|-----------|-----|
| Founder's Pledge | ❌ Soulbound | First 1,000 reward — prestige, not profit |
| Hunted Founder | ❌ Soulbound | Bragging rights — finding it is the reward |
| All other NFTs | ✅ Tradable | Marketplace economy |

Soulbound is enforced via XRPL `lsfOnlyXRP` flag on the mint transaction + a burned trust line.

---

## 📦 Complete Revenue Model (Per Player)

| Revenue Source | When | Amount | Commission |
|---------------|------|--------|-----------|
| **Membership** | Monthly | $99-$1,999/mo | 100% (direct Stripe) |
| **Primary NFT Sale** | One-time | $99-$9,999 | 100% (direct Stripe) |
| **Secondary Sale** | Per trade | Variable | ~20% (platform cut) |
| **Artwork Royalty** | Per trade | 3% | Paid to artist |
| **Creation Commission** | Per trade | 2% | Paid to studio |
| **Listing Fee** | Per listing | $0.50 | 100% platform |
| **Auction Premium** | Per auction | 10% reserve | 100% platform |

**Projected Revenue at Maturity (Year 2):**
- 50,000 active members @ avg $200/mo = $10M/mo membership
- $5M/mo marketplace volume @ 20% = $1M/mo marketplace
- $3M/mo primary NFT sales = $3M/mo direct
- **Total: ~$14M/mo at maturity**

---

## 🔧 Technical Implementation

### Smart Contract Addresses (To Be Deployed)

| Contract | XRPL Network | Purpose |
|----------|-------------|---------|
| `NFTokenMint` | Mainnet | Mint all game NFTs |
| `MarketplaceEscrow` | Mainnet | Hold funds during P2P trades |
| `FounderTokenMint` | Testnet → Mainnet | Limit 1,000 Founder's Pledge tokens |
| `ArtistRoyaltySplit` | Mainnet | Auto-distribute 3% to artists |
| `CreationCommissionPool` | Mainnet | Auto-distribute 2% to studio |

### Marketplace UI Components (To Build)

- [ ] NFT listing page (set price, auction, or instant buy)
- [ ] Wallet connect (XUMM + Crossmark)
- [ ] Trade history per NFT
- [ ] Artist portfolio pages
- [ ] Commission dashboard for artists
- [ ] Soulbound badge display
- [ ] Auction timer + bid tracking
- [ ] Fee breakdown shown at checkout
