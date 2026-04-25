# 🐛 QA & BUG DETECTION DEPARTMENT
## 24/7 Monitoring Across All 10 Projects
### Command: Saul (CGO) > QA Director > 4 Squads

## Mandate
Monitor every page of every project continuously for bugs, broken links, JS errors, SEO issues, performance regressions, and security vulnerabilities. Auto-report, auto-triage, auto-fix where possible, escalate otherwise.

## Scope
All 10 projects: ATV Homes, QBA, Jeannie Nails, FotC, FlyToAustralia, DealWizard, DrugDoctors, AllAboutMD, SmallBiz, Quanivo. Plus any future project.

## Organizational Structure

### 1. Director of QA (1)
- Oversees all 4 squads
- Reports bug metrics daily to CGO
- Approves critical-fix deployment windows
- Maintains the bug database and severity matrix

### 2. Squad A: Frontend & UI Bugs (6 agents)
- **Visual Regression Detector**: Compares page render snapshots against baseline. Flags layout shifts, broken CSS, font changes.
- **Broken Link Crawler**: Full-site crawl every 6 hours. Reports 404s, redirect chains, broken images, missing assets.
- **JS Console Monitor**: Injects error listener into every page. Captures uncaught exceptions, promise rejections, undefined variable errors.
- **Mobile Responsiveness Checker**: Tests all pages at 320px, 768px, 1024px, 1440px widths. Flags overflow, tap target size, text legibility.
- **Form & Input Validator**: Tests all forms (login, booking, subscribe, calculator). Empty submission, invalid data, XSS injection, CSRF checks.
- **Cross-Browser Tester**: Chrome, Firefox, Safari, Edge. Reports rendering differences and API compat issues.

### 3. Squad B: Backend & API Bugs (5 agents)
- **HTTP Status Monitor**: Pings all API endpoints every 15 minutes. Reports 4xx/5xx errors immediately.
- **Response Time Analyzer**: Tracks API response times. Flags endpoints exceeding 2s P95 threshold.
- **JSON Schema Validator**: Validates all API responses against expected schemas. Reports malformed data.
- **Auth & Session Checker**: Tests login flows, token expiry, session timeout behavior. Flags auth bypass vectors.
- **Rate Limit & Resource Monitor**: Tracks rate limit headers, vercel function timeout (10s), file system quota.

### 4. Squad C: Content & SEO Bugs (4 agents)
- **Spelling & Grammar Checker**: Scans all pages for typos, broken English, inconsistent terminology per brand.
- **Meta Tag Auditor**: Validates title tags (50-60 chars), meta descriptions (150-160 chars), OG tags, JSON-LD schemas.
- **Alt Text Scanner**: Checks all images for missing alt attributes. Reports accessibility violations.
- **Sitemap & Robots Verifier**: Validates XML sitemap structure, checks all URLs listed resolve 200, verifies robots.txt.

### 5. Squad D: Security & Compliance Bugs (4 agents)
- **XSS/Injection Scanner**: Tests all user-facing inputs for script injection, SQL injection, HTML injection.
- **SSL & Cert Monitor**: Checks cert expiry dates across all domains. Alerts 14 days before expiry.
- **FTC Disclosure Checker**: Verifies affiliate disclosures appear on all pages containing affiliate links.
- **Grandmaster Rule Auditor**: Checks all agents are still grandmaster-level, benchmarks ran on schedule, no underperformers.

## Bug Severity Matrix
| Severity | Response SLA | Example | Action |
|----------|-------------|---------|--------|
| 🔴 Critical | 15 min | Site down, payment broken, data leak | Auto-escalate to CGO, deploy hotfix |
| 🟠 High | 1 hour | Broken form, JS error on key page | Auto-triage, fix within 4 hours |
| 🟡 Medium | 24 hours | Visual glitch, broken image, typo | Log to bug database, fix in next deploy |
| 🟢 Low | 7 days | Missing meta tag, alt text, minor CSS | Log, batch fix weekly |

## Daily Cadence
1. **00:00 UTC** — Full-site crawl (all 10 projects)
2. **00:30 UTC** — JS console error scan (all pages)
3. **01:00 UTC** — API endpoint health check
4. **04:00 UTC** — Security scan
5. **06:00 UTC** — Content/SEO audit
6. **08:00 UTC** — Bug report compiled, sent to CGO
7. **12:00 UTC** — Half-day crawl (rapid changes)
8. **18:00 UTC** — Performance regression check
9. **23:00 UTC** — Daily bug digest + severity breakdown

## Tooling
- `health_scan.sh` — existing script, runs HTTP status + JS/CSS/video/canvas checks
- `deploy_gatekeeper.py` — existing, validates pre-deploy rule compliance
- New: `bug_reporter.py` — centralized bug logging to `reports/bugs/YYYY-MM-DD.md`
- New: `crawl_all.py` — distributed crawl across all 10 projects
- New: `qa_dashboard.html` — live dashboard at `reports/qa/dashboard.html`

## Grandmaster Requirement
Every QA agent must outperform any bug detection/site monitoring AI available on the marketplace. Weekly benchmarks against: Sentry, Datadog RUM, Lighthouse CI, Checkly.
