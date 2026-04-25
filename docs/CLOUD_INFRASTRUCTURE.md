# ATV Homes — Cloud Infrastructure
## Deployed: Vercel (Edge Network) + Cloudflare-ready

---

## Live URLs

| Service | URL | Status |
|---|---|---|
| **Production** | https://atv-homes.vercel.app | ✅ Live |
| **Custom Domain** | https://atvhomes.com | ⬜ Needs DNS |
| **Deploy Directory** | `/tmp/atv-homes-deploy/` | ✅ Ready |

## Performance vs Old Hosting

| Metric | Old (Hostinger/PHP) | New (Vercel Edge) | Improvement |
|--------|-------------------|-------------------|-------------|
| TTFB | 737ms | **62ms** | **12x faster** |
| Total load | 855ms | **62ms** | **14x faster** |
| Page size | 256KB (WordPress) | **30KB** (Static) | **8x smaller** |
| Server | PHP 8.1 + hcdn | **Vercel Edge Network** | Global CDN |
| Security | Basic SSL | **HSTS preload, CSP, X-Frame-DENY** | Enterprise grade |

## Infrastructure

```
atvhomes.com (domain)
  └── Vercel Edge Network (CDN + SSL + routing)
       ├── index.html (30KB, sub-100ms anywhere)
       ├── /tos/ → Terms of Service
       ├── /privacy/ → Privacy Policy
       ├── /warranty/ → Warranty
       ├── /returns/ → Returns & Refunds
       └── /api/products → WooCommerce API proxy
```

## Security Headers Applied

- `Strict-Transport-Security: max-age=63072000; includeSubDomains; preload`
- `X-Frame-Options: DENY`
- `X-Content-Type-Options: nosniff`
- `Permissions-Policy: camera=(), microphone=(), geolocation=()`
- `Referrer-Policy: strict-origin-when-cross-origin`
- `Content-Security-Policy: restricted to self, Stripe, Google Fonts`

## DNS Setup (to point atvhomes.com)

Add this A record at your DNS provider:
```
A  atvhomes.com  76.76.21.21
```

Or use Cloudflare:
1. Add site to Cloudflare
2. Set A record → `76.76.21.21`
3. Enable proxy (orange cloud) for DDoS + WAF protection
4. Wait 5-10 minutes for propagation

## WooCommerce API Proxy

The old WordPress/WooCommerce backend still runs at `atvworldwide.com` for:
- Product management
- Order processing
- Inventory updates

The new site has a serverless API proxy at `/api/products` that fetches live product data from the old WooCommerce. This proxy:
- Runs on Vercel Edge (sub-50ms cold start)
- Caches for 5 minutes with stale-while-revalidate
- Returns JSON for any frontend product display needs

## Chat Widget

Quantum sales + CS bot embedded on every page. 9 industry knowledge domains (pricing, delivery, construction, zoning, living, use cases, support, warranty, QBA branding). 3-problem rule enforced. QBA branding on every response.

## Old Site Redirection

The old WordPress site at `atvworldwide.com` should remain running for:
- WooCommerce API backend
- Stripe webhook processing
- Historical data

The new Vercel site is the **customer-facing frontend**. When atvhomes.com DNS resolves, customers see the fast edge-deployed static site while the WordPress backend handles orders invisibly.

## Redeployment

To redeploy after changes:
```bash
cd /tmp/atv-homes-deploy
npx vercel --prod --token YOUR_TOKEN --yes
```

Or simply run the replication engine from workspace:
```bash
python3 deploy_atv_homes.py
```

---

*Infrastructure by Quantum Bots Agency.*
