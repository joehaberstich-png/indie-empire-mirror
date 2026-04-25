# Agent Heartbeat — Daily Auto-Publish Flow
*"Trending Topic at 9 AM → Link-Embedded Post by 2 PM"*

## Timeline

| Time | Phase | Agent Type | Action |
|------|-------|-----------|--------|
| 09:00 | Scrape | Research Agent | Pull trending topics from niche subreddits, Quora hot questions, Pinterest trending. Cross-reference with assigned product keywords. |
| 09:30 | Select | Research Agent | Score topics (relevance × urgency × comment velocity). Pick top 1–2. |
| 10:00 | Draft | Content Agent | Write 3-paragraph "Value First" response/blog. No link in paragraphs 1–2. Paragraph 3 transitions naturally. |
| 11:00 | Bridge | Content Agent | Insert link to bridge page (cloaked). Add FTC disclosure. |
| 12:00 | Review | Compliance Agent | Quick pass: disclosure present, no direct CB link, no spam patterns. |
| 13:00 | Post | Sales Agent | Deploy to platform. Log URL + timestamp. |
| 14:00 | Monitor | Sales Agent | Check for engagement, replies, or flagging. Alert if removed. |

## Agent Prompt — "Value First" Rule (baked into every Content Agent)
> *"Write 3 paragraphs of genuinely helpful advice or insight before mentioning any product or link. The first two paragraphs must stand alone as useful content even if the product link is removed."*

## Cron Setup (per agent)
```yaml
schedule:
  - time: "09:00 UTC"
    action: scrape_trending
  - time: "10:00 UTC"
    action: draft_value_post
  - time: "13:00 UTC"
    action: deploy_post
```

## Scoring Formula
```
Topic Score = (TrendingVelocity × 0.4) + (KeywordRelevance × 0.4) + (CommentPotential × 0.2)
```
Only topics with Score ≥ 70 proceed to drafting.
