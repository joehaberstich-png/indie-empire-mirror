# jeannienails.ca — Registration in Owner's Name

## Why NOT Vercel
Vercel registers domains in their own account as the registrant. The domain stays in Vercel's name, not the owner's. For .ca domains, this is problematic because:
- CIRA requires Canadian presence — Vercel (US company) doesn't qualify
- The actual business owner has NO control over the domain if they leave Vercel
- Transferring away from Vercel later requires Vercel to release it (painful)

## Recommended Path: Namecheap (Registrant = Jeannie Boutiler)

### Pricing
| Item | Cost |
|------|------|
| jeannienails.ca (1 year) | $8.88 CAD (first year promo) |
| Premium DNS (free tier) | $0 |
| WHOIS privacy (.ca excludes by default) | $0 |
| **Total first year** | **~$8.88-$12.88 CAD** |

### Registration Details — ENTER THESE EXACTLY

**Registrant Contact (THE OWNER):**
```
First Name: Jeannie
Last Name: Boutiler
Organization: Jeannie Boutiler Nails
Email: jeanniesnails17@gmail.com
Phone: +1.9028857896
Address: [TOWN, PROVINCE, POSTAL CODE]
```

**Canadian Presence Requirement — Select one:**
- [ ] Canadian citizen
- [ ] Permanent resident
- [x] Canadian business (sole proprietorship)
- [ ] Canadian organization

### After Purchase — DNS Setup (5 minutes)
1. Buy jeannienails.ca at Namecheap
2. In Namecheap dashboard → Domain List → jeannienails.ca
3. Click "Manage" → "Custom DNS"
4. Change nameservers to:
   ```
   ns1.vercel-dns.com
   ns2.vercel-dns.com
   ```
5. OR keep Namecheap DNS and add these records:
   ```
   Type: A      Host: @     Value: 76.76.21.21
   Type: CNAME  Host: www   Value: jeannienails.vercel.app
   ```
6. Done. Site starts resolving within 15-60 minutes.

### Vercel Configuration (already done)
The domain `jeannienails.ca` is ALREADY added to the Jeannie Nails Vercel project with:
- SSL certificate being generated
- Alias already pointing to latest deployment
- Once DNS propagates → https://jeannienails.ca works immediately

### Alternative Registrars

| Registrar | Cost/yr | Notes |
|-----------|---------|-------|
| Namecheap.ca | $8.88-$12.88 | Best balance of price + features |
| Hover | $14.99 | Canadian-owned, excellent support |
| Rebel.ca  | $14.99 | Canadian, supports CIRA CMP |
| GoDaddy.ca | $11.99-$14.99 | Most features, aggressive upsells |
| Vercel | $16.99 | Simplest but NOT in owner's name |

## ⚡ Alternative: Proxy Registration via QBA

Since you said "purchase from our AI agency at zero cost":
- **QBA purchases** jeannienails.ca at Namecheap with Jeannie as the registrant
- QBA pays and configures DNS
- Cost billed to QBA's operational budget ($8.88 CAD)
- Jeannie retains 100% ownership — domain registered in HER name

## Domain Ownership Rules
- .ca domains CANNOT use WHOIS privacy — the registrant details are PUBLIC
- The registrant IS the legal owner. Changing registrant later requires:
  1. Email confirmation from old owner
  2. CIRA approval
  3. 60-day transfer lock if recently changed
- **Best practice**: Register in owner's name from day 1
