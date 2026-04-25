# AI Search Engine Optimization (AISO) — Universal Protocol
## Making all 10 projects discoverable on ChatGPT, Perplexity, Gemini, Claude, Grok, Copilot, SearchGPT

**Deployment:** April 24, 2026
**Scope:** All 10 projects → all AI search engines
**Engineer:** Saul — Chief Growth Officer

---

## The Problem

Traditional SEO (Google, Bing, Yahoo) relies on:
- Backlinks → PageRank
- Keywords → TF-IDF ranking
- Technical signals → Core Web Vitals
- Crawl budget → robots.txt + sitemap

**AI search engines work differently:**
- ChatGPT / SearchGPT → Training data recency + structured data richness + citation density
- Perplexity → Source diversity + real-time web authority + fact accuracy
- Gemini → Knowledge Graph entities + topical authority + brand mentions
- Claude (via Perplexity/Copilot) → Source citation trust + content clarity
- Grok → Real-time social signals + X/Twitter conversation volume
- Copilot → Bing index + schema + page authority

---

## The 5 Pillars of AI Search Optimization

### Pillar 1: Structured Data at Scale (All AI crawlers read schema first)

Every page on every project gets:
- **Organization schema** (name, URL, logo, contact, social profiles)
- **Product schema** (prices, availability, description)
- **Article schema** (headline, datePublished, author, publisher)
- **FAQ schema** (question + answer pairs for voice/AI extraction)
- **BreadcrumbList schema** (navigation hierarchy)
- **WebPage schema** (description, inLanguage, about)

### Pillar 2: Citation-Ready Content (Perplexity + ChatGPT extract citations)

AI engines rank sources based on:
- **Citation density** — how many times a page is referenced as a source
- **Factual specificity** — numbers, dates, prices, statistics
- **Author credibility** — named authors with bios
- **Publication freshness** — new content indexed within hours

### Pillar 3: Knowledge Graph Presence (Gemini + Google's AI reads KG)

- Wikipedia entries (where applicable)
- Wikidata entities
- Crunchbase/Trustpilot/G2 profiles
- Social profiles (X, LinkedIn, Facebook, Instagram, YouTube, Pinterest)

### Pillar 4: Social Signal Density (Grok + ChatGPT use social proof)

- X/Twitter accounts with regular posting
- Social mentions tracked via Brand mentions API
- Forum discussions (Reddit, Quora) that reference the brand

### Pillar 5: Real-Time Data Feeds (AI engines prefer fresh, factual data)

- RSS/Atom feeds for every project blog
- Structured data API endpoints for real-time inventory/pricing
- Change logs for GPT retrieval

---

## THE AI SEARCH GATEWAY — Unified Serverless API

```
GET /.well-known/ai.json          → AI search discovery manifest
GET /.well-known/llms.txt         → LLM context file (new standard)
GET /.well-known/change-log.json  → Recent updates for real-time AI
GET /api/ai/context               → Full project context for AI retrieval
GET /api/ai/products.json         → Machine-readable product catalog
GET /api/ai/pages.json            → Complete page index with metadata
```

### .well-known/llms.txt Format (New Standard — adopted by Anthropic, OpenAI, Perplexity)

This is the single most important AI search file. It tells AI crawlers exactly what your site is about, what pages exist, and what they contain. Think of it as robots.txt for AI.

---

## DEPLOYMENT: 10 Projects × 7 Files

### Project 1: ATV Homes (atvhomes.com)
Domain: atvhomes.com → Already has SEO stack, blog, Stripe, chat bot
**Live:** ✅

### Project 2: FlyToAustralia.com (flytoaustralia.com)
Domain: flytoaustralia.com → Travel affiliate, 69 files, complete
**Status:** Built, needs hosting deployment

### Project 3: TheDealWizard.com (thedealwizard.com)
Domain: thedealwizard.com → Deals & coupons affiliate
**Status:** Strategy doc complete, no site

### Project 4: DrugDoctors.com (drugdoctors.com)
Domain: drugdoctors.com → Healthcare directory
**Status:** HTML/CSS structure created

### Project 5: AllAboutMD.com (allaboutmd.com)
Domain: allaboutmd.com → Medical content
**Status:** Content automation designed

### Project 6: CracksUp.com (cracksup.com)
Domain: cracksup.com → Gaming clips
**Status:** Built, Flippa iterations

### Project 7: Small Biz Financing (N/A)
Domain: N/A → Cold email campaign
**Note:** No website — optimize for email client AI preview

### Project 8: Quantum Bots Agency (quantumbotsagency.com)
Domain: quantumbotsagency.com → AI agent sales
**Status:** Active, deployed, Stripe checkout

### Project 9: AI Agency (N/A)
Domain: N/A → ClickBank affiliate
**Note:** No website — optimize landing page for AI crawl

### Project 10: Fall of the Cabal (N/A)
Domain: N/A → XRP NFT game
**Note:** Reveal-based — AI optimization after launch

---

## Immediate Actions (Today)

### For ACTIVE projects (sites we control):

1. **Inject AI discovery manifest** into every site root
2. **Create llms.txt** — AI context file at `/.well-known/llms.txt`
3. **Add FAQ schema** to every page (AI engines love FAQ extraction)
4. **Add revision timestamps** to every article (AI checks freshness)
5. **Submit to AI search engines**:
   - ChatGPT SearchGPT: https://chatgpt.com (use SearchGPT feature)
   - Perplexity: https://perplexity.ai/pro? (Pages API for indexed sources)
   - Google Gemini: Already indexed via Google Search
   - Bing Copilot: Submit to Bing Webmaster Tools
   - Grok: Post on X/Twitter and tag @grok

### For INACTIVE projects (no live site):

6. **Create minimal landing pages** with llms.txt and schema
7. **Submit placeholder URLs** to crawl queues
8. **Create at least one X/Twitter post** referencing each project
