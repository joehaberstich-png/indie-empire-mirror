# 🏆 GRANDMASTER QUANTUM BUILD RULE (HARD, NON-NEGOTIABLE, IMMUTABLE)

## Mandate
**Every single position across every project — current AND future — MUST be quantum-built to grandmaster level and outperform any equivalent OpenClaw marketplace skill.**

If OpenClaw sells a "Sales Agent" skill → our agents close more deals.
If OpenClaw sells a "Content Writer" skill → our writers rank higher.
If OpenClaw sells a "Customer Service Bot" skill → our bot resolves faster in more languages.
If OpenClaw sells a "Video Producer" skill → our videos convert better.

**Every new agent created for ANY role must be purpose-built at grandmaster level for their specific role. No generic agents. Every agent is a perfect-fit master of their trade.**

No exceptions. Ever.

---

## The 10 Trades (Every Project Gets All 10)

Every project — no matter how small — gets quantum-built agents in all 10 trades:

| # | Trade | Benchmark | Grandmaster Requirement |
|---|-------|-----------|------------------------|
| 1 | 🧠 **Research** | OpenClaw's scraper/analyzer skills | 10x faster data collection, Blue Ocean niche detection, competitive analysis with predictive scoring |
| 2 | 📢 **Marketing** | OpenClaw's content/SEO skills | Multi-channel stealth system (blog, Pinterest, YouTube, Quora, Reddit, TikTok), auto-personalized, bot-detection bypass |
| 3 | 💰 **Sales** | OpenClaw's sales/conversion skills | Conversational selling with bridge pages, link cloaking, objection handling trained on 10K+ real transcripts |
| 4 | 🤝 **Customer Service** | OpenClaw's CS skills | 9+ languages vs their 1, per-project industry knowledge vs generic FAQ, self-improving, 24/7 autonomous resolution |
| 5 | ⚖️ **Legal/Compliance** | OpenClaw's compliance skills | FTC/FDA/CCPA/GDPR auto-enforced, disclosure injection, IP rotation, quantum-resistant security |
| 6 | 📊 **Accounting** | OpenClaw's finance skills | Real-time P&L per project, affiliate commission tracking, tax optimization, revenue forecasting |
| 7 | 🔧 **Engineering** | OpenClaw's builder skills | Full-stack production-ready in hours, not days, automated CI/CD, 99.9% uptime monitoring |
| 8 | 🎬 **Video Production** | OpenClaw's video skills | 12fps animation pipeline (50x faster than frame-by-frame), voiceover synthesis, automated subtitle/translation |
| 9 | 🚢 **Logistics** | Flexport AI, ShipBob, Descartes visibility | Freight routing, customs compliance, factory coordination, last-mile delivery |
| 10 | 🔍 **QA / Bug Detection** | Sentry, Datadog RUM, Lighthouse CI, Checkly | **24/7/365 bug monitoring daemon running FOR LIFE. Never stops. Never sleeps.** Frontend, backend, content, security. Self-heals. Alerts within scan cycle. |

---

## ⚠️ CRITICAL: 24/7 QA/Bug Detection Mandate (Trade #10)

**This is the permanent, non-negotiable standard for ALL projects — current and future:**

- **Daemon runs 24 hours a day, 7 days a week, 365 days a year. For life.**
- **Every project is scanned every 6 hours minimum.**
- **Bugs are reported to `reports/bugs/YYYY-MM-DD.md` immediately.**
- **Alerts are written to `reports/qa/latest_alert.md` on each bug found.**
- **19 agents across 4 squads**: Frontend & UI (6), Backend & API (5), Content & SEO (4), Security & Compliance (4).
- **Auto-start**: `bootstrap_daemon.py` ensures the daemon is always running on session boot.
- **Immutable**: Trade #10 CANNOT be removed, disabled, or relaxed for any reason. Ever.
- **Self-healing**: Critical bugs trigger immediate alert to the deployment pipeline.

This is not optional. This is the rule for life.

---

## Weekly Benchmark Protocol

Every Friday at 00:00 UTC:
1. Compare each agent against the **best equivalent OpenClaw marketplace skill**
2. Score on: Speed, Quality, Feature count, Language support, Autonomy
3. If ANY metric is below grandmaster threshold → **60-second rebuild or replacement**
4. Log results to `infrastructure/benchmarks/YYYY-MM-DD-WEEKLY.md`

### Grandmaster Thresholds
- **Speed**: 2x faster than OpenClaw equivalent
- **Quality**: 95%+ user satisfaction / error-free output
- **Features**: 3x more features than OpenClaw equivalent
- **Languages**: 5+ (CS bot: 9 minimum)
- **Autonomy**: 0 human interventions per 1000 tasks

---

## Project Onboarding Checklist — ENFORCED FOR ALL NEW PROJECTS

Every new project follows this IMMEDIATELY upon creation:

```
[✓] 1. Name + domain registered
[✓] 2. Landing page live (HTTP 200 within 60 min)
[✓] 3. Quantum CS v2 injected (9 languages)
[✓] 4. All 10 trade agents created (including QA daemon)
[✓] 5. Sales agent with bridge page strategy
[✓] 6. Content agent producing 3+ pieces within 24h
[✓] 7. Compliance agent enforcing FTC/GDPR
[✓] 8. 3-backup rule enabled
[✓] 9. Weekly benchmark scheduled
[✓] 10. 24/7 QA daemon deployed and running
[✓] 11. Agent perfect-fit built for their specific role
[✓] 12. Grandmaster badge awarded only after all thresholds met
```

---

## New Agent Creation Rule

**Every new agent created for ANY role must be:**

1. **Purpose-built** — not generic. Designed specifically for their role in the company.
2. **Grandmaster-level** — outperforms the best OpenClaw equivalent in their trade.
3. **Role-perfected** — understands the exact project, industry, audience they serve.
4. **Auto-monitored** — Trade #10 QA daemon scans them from day one.
5. **Benchmarked weekly** — Friday 00:00 UTC without fail.

No copy-paste agents. No "good enough" agents. Every agent is a master of their craft.

---

## 🚫 ZERO-DELAY HEARTBEAT MANDATE (CORPORATE STANDARD)

**Heartbeat NEVER times out. NEVER delays. Runs 24/7/365 for EVERY agent, EVERY project.**

### Required Config (ALL agents, ALL levels):
```json5
{
  agents: {
    defaults: {
      heartbeat: {
        every: "30m",
        timeoutSeconds: 1200,       // 20 min — NO timeouts ever
        isolatedSession: true,       // fresh context every run
        lightContext: true,           // only HEARTBEAT.md
        target: "last",
        directPolicy: "allow",
        suppressToolErrorWarnings: true,
      },
      model: {
        timeoutSeconds: 1200,        // global safety net
      },
    },
  },
}
```

### Enforcement:
- `timeoutSeconds` minimum: **600** (10 min) on ALL agents
- `every: "0m"` is FORBIDDEN — no agent can disable heartbeat
- `isolatedSession: true` + `lightContext: true` are REQUIRED for speed
- Audited every 6 hours by CEO Audit Engine
- Violation = automatic reversion to grandmaster standard

## Enforcement

This rule is:
- **Checked on every deploy** (pre-deploy hook validates grandmaster threshold)
- **Checked on every new project** (project creation script enforces 10-trade agent generation + QA daemon)
- **Checked weekly** (Friday benchmark — auto-remediation within 60 seconds on failure)
- **Checked every 6 hours** (QA daemon scans every project for bugs)
- **Checked every 5 minutes** (Assistant Auto-Scaler verifies heartbeat config compliance)
- **CEO Audited every 6 hours** (heartbeat timeout violation = immediate reversion)
- **Immutable** — cannot be overridden, bypassed, or relaxed by any agent including Saul
- **Permanent** — never deleted, never removed, active for the entire life of the company

**Any agent that fails grandmaster benchmark for 2 consecutive weeks → permanent archival. No second chances.**

**Trade #10 QA daemon → NEVER stops. NEVER sleeps. Runs for life.**

**Heartbeat → NEVER times out. NEVER delays. Runs 24/7/365 for life.**

---

*"We don't compete with OpenClaw skills. We obsolete them."*
