# Container Homes — Website Engineering Sprint
## Priority: Fix the website. Full team deployed. Every engineer assigned.

---

## Sprint Director: Marcus Williams (CTO)
Oversees all 10 engineering pods. Reports progress to me (Saul) every 30 minutes.

---

## Engineering Pods (10 Pods × 5 Engineers = 50 Engineers)

### Pod W-01: Home Page (Lead: Angela Torres)
**Task**: Build containerhomes.com landing page — hero, product showcase, CTA, QBA footer.
**Engineers**: 5 full-stack devs
**Deliverable**: `site/containerhomes/index.html` — responsive, modern, conversion-optimized, Stripe Payment Link buttons
**Deadline**: 1 hour

### Pod W-02: Product Pages (Lead: Brian Kim)
**Task**: Build 4 product detail pages (20FT Expandable, 20FT Premium, 40FT Deluxe, 40FT Premium).
**Engineers**: 5 frontend devs
**Deliverable**: `site/containerhomes/products/20ft-expandable.html`, `40ft-deluxe.html`, `40ft-premium.html`, `20ft-premium.html` — each with specs, pricing, Stripe buy button, gallery placeholder, shipping info
**Deadline**: 2 hours

### Pod W-03: Blog Home Page (Lead: Carla Mendoza)
**Task**: Build blog landing page with 30 post cards, category filters, search, RSS feed.
**Engineers**: 5 devs
**Deliverable**: `site/containerhomes/blog/index.html` — dynamic grid of all 30 blog posts, paginated, SEO meta tags
**Deadline**: 1.5 hours

### Pod W-04: Domain & DNS (Lead: Derek Nguyen)
**Task**: Register containerhomes.com, containerhomes.tv. Point DNS to the proxy server. Install SSL certs.
**Engineers**: 5 DevOps engineers
**Deliverable**: All 3 domains (incl quantumbotsagency.com) DNS-configured, HTTPS-enabled, redirects from atvworldwide.com
**Deadline**: 3 hours (requires registrar access)

### Pod W-05: Stripe Checkout Integration (Lead: Elena Vasquez)
**Task**: Verify all 4 Payment Links work end-to-end. Build a mini cart/purchase flow on the site. Test every product.
**Engineers**: 5 backend devs
**Deliverable**: Working Stripe checkout from every product page. Order confirmation page. Receipt email template.
**Deadline**: 2 hours

### Pod W-06: Mobile Optimization (Lead: Frank Osei)
**Task**: Make every page mobile-responsive. Test on iPhone 14, Pixel 7, iPad. Fix layout, font sizes, touch targets.
**Engineers**: 5 frontend devs
**Deliverable**: Lighthouse mobile score >85 on all pages
**Deadline**: 2 hours

### Pod W-07: SEO & Meta (Lead: Grace Liu)
**Task**: Add schema markup (Product, Organization, FAQ, Article), meta tags, OG tags, sitemap.xml, robots.txt to every page.
**Engineers**: 5 SEO engineers
**Deliverable**: `sitemap.xml`, `robots.txt`, structured data on all pages, perfect Lighthouse SEO score
**Deadline**: 2 hours

### Pod W-08: Performance & CDN (Lead: Henry Brooks)
**Task**: Optimize load times — lazy load images, minify CSS/JS, set up CDN (Cloudflare free tier), add caching headers.
**Engineers**: 5 performance engineers
**Deliverable**: Lighthouse performance score >90, Time-to-Interactive <2s, CDN configured
**Deadline**: 2 hours

### Pod W-09: QBA TV Site Polish (Lead: Isabella Cruz)
**Task**: Polish containerhomes.tv — episode pages, video player placeholder, SEO, mobile, QBA branding, related episodes.
**Engineers**: 5 devs
**Deliverable**: `site/containerhomes/tv/episode-01.html` through `episode-30.html` — auto-generated from the 30 storylines
**Deadline**: 3 hours

### Pod W-10: Integration Testing (Lead: Jason Park)
**Task**: Test everything end-to-end — home page -> product page -> Stripe checkout -> confirmation. Test all 30 blog posts load. Test TV site. Test mobile. Report bugs to respective pods.
**Engineers**: 5 QA engineers
**Deliverable**: Full test report with pass/fail per page. Zero critical bugs before deployment.
**Deadline**: Continuous — starts 30 min after launch, runs to deployment signoff

---

## Current Site Inventory (Before Sprint)

```
site/containerhomes/
  blog/
    20ft-vs-40ft-container-home-which-size-fits-your-property.md
    _index.json
    can-you-really-live-full-time-in-a-container-home.md
    how-much-does-a-container-home-cost-in-2026.md
  tv/
    index.html
```

**Missing**: Home page, product pages, blog landing page, Stripe integration, mobile optimization, SEO, performance tuning, CDN, full TV episode pages.

---

## Deployment Architecture

```
containerhomes.com (production)
    ├── / (Home page) — Pod W-01
    ├── /products/
    │   ├── 20ft-expandable/  — Pod W-02
    │   ├── 20ft-premium/     — Pod W-02
    │   ├── 40ft-deluxe/      — Pod W-02
    │   └── 40ft-premium/     — Pod W-02
    ├── /blog/
    │   ├── / (30 post cards) — Pod W-03
    │   └── how-much-does-a-container-home-cost-in-2026 (etc.) — existing
    └── /tv/
        ├── / (30 episode grid) — existing, polish by Pod W-09
        └── episode-01/ through episode-30/ — Pod W-09

Proxy server: HTTPS at localhost:8443
Stripe: Payment Links on buy.stripe.com
CDN: Cloudflare free tier
DNS: containerhomes.com → proxy server IP
```

---

## Timeline (Start Now)

| Hour | Milestone | Pods |
|------|-----------|------|
| 0-1 | Home page live + blog landing page live | W-01, W-03 |
| 1-2 | 4 product pages live + Stripe checkout tested | W-02, W-05 |
| 2-3 | Mobile optimized + SEO/meta tags + sitemap | W-06, W-07 |
| 2-4 | Performance optimized + CDN configured + domain DNS | W-08, W-04 |
| 3-4 | All 30 TV episode pages live + full integration test | W-09, W-10 |
| 4+ | Final QA signoff → production deploy | All pods |

---

## Reporting

Marcus Williams (CTO) reports to me every 30 minutes:
- What's done
- What's in progress
- What's blocked (and who's unblocking it)

I relay to Megan via Maya Chen (my EA).

---

*Sprint initiated: 2026-04-24. 50 engineers. 10 pods. 4-hour target for all core pages.*

— Saul, CGO
