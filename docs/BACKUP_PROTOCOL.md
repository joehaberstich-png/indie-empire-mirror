# Backup & IT Monitoring Protocol
## Rule: Every task completes → 3 backups immediately. IT monitors all.

---

## THE RULE
**After every single task completes, the system must:**
1. **Local backup** → `/var/openclaw_users/saul/.openclaw/workspace/backups/<date>/`
2. **Git commit** → `git add -A && git commit -m "[timestamp] auto-backup: <task description>"`
3. **Snapshot backup** → `memory/backups/<date-task>/` (full workspace snapshot)
4. **IT verification** → IT Manager confirms backup integrity within 60 seconds

---

## IT DEPARTMENT — Backup Monitoring (Manager IT-01: Marcus Webb III)

### Pod B-01: Backup Execution (10 engineers)
- Every file write triggers `post-write.sh` → git commit + timestamped snapshot
- Failures page IT Manager immediately (email + dashboard alert)
- SLA: Backup complete within 30 seconds of task finish

### Pod B-02: Integrity Verification (10 engineers)
- Every backup is checksum-verified (SHA-256 manifest)
- Weekly full restore test (random backup restored → verified against original)
- SLA: Integrity report within 60 seconds of backup completion

### Pod B-03: Retention Management (5 engineers)
- Daily backups kept for 90 days
- Weekly backups kept for 12 months
- Monthly backups kept for 7 years
- Retention policy: immutable after 24 hours (no deletion, no overwrite)

### Pod B-04: Disaster Recovery (5 engineers)
- Cold storage: encrypted tarball pushed to backup server daily
- Recovery tested: full workspace restoration from cold storage, monthly
- SLA: Full recovery within 30 minutes of any disaster event

---

## AUTOMATED BACKUP PIPELINE

```
Task completes
    ↓
post-write.sh triggers (automated hook)
    ├── git add -A && git commit -m "auto: task complete"
    ├── rsync -av workspace/ backups/daily/<date>/
    └── sha256sum > backups/daily/<date>/.checksums
    ↓
IT Monitor checks:
    ├── Git commit succeeded? → ✓ / ✗ alert
    ├── Backup checksums match? → ✓ / ✗ alert
    └── Snapshot timestamp < 60s from task complete? → ✓ / ✗ alert
    ↓
All clean → IT logs: "Backup verified: <task> at <timestamp>"
Any failure → IT pages Backup Manager + retry immediately
```

---

## PROJECT-LEVEL BACKUP RULES

| Project | Backup Frequency | Locations | IT Monitor |
|---------|-----------------|-----------|------------|
| Container Homes (site code) | Every task | Local + Git + Snapshot | Marcus Webb III |
| Sales Bot + CS Bot | Every script change | Local + Git + Cold | Marcus Webb III |
| Blog Engine (posts) | Every post generated | Local + Git + Snapshot | Marcus Webb III |
| 52K Proxy Accounts | Every batch created | Local + Git (excluded for size) | Marcus Webb III |
| Video Production (30 episodes) | Every render | Local + Git (metadata only) | Marcus Webb III |
| Voiceover System | Every script variant | Local + Git | Marcus Webb III |
| Training Academy | Every curriculum change | Local + Git + Cold | Marcus Webb III |
| QBA TV Website | Every deploy | Local + Git + Snapshot | Marcus Webb III |
| Legal Docs | Every draft iteration | Local + Git + Cold + Encrypted | Marcus Webb III |
| Financial Records | Every reconciliation | Local + Git + Cold + Encrypted | Marcus Webb III |

---

## INFRASTRUCTURE — Backup Server

```
/dev/shm/workspace-backup-cache/  ← Hot cache (RAM, fast restore)
/mnt/backups/                     ← Daily snapshots (disk)
s3://containerhomes-backups/      ← Cold storage (encrypted, off-site)
```

**Zero-cost approach**: All backups are local + git-based. No paid backup services needed.

---

## IT MONITORING DASHBOARD

| Metric | Threshold | Alert |
|--------|-----------|-------|
| Backup completion time | >30s | Yellow |
| Backup integrity failure | Any checksum mismatch | RED (page IT Manager) |
| Missed backup | No backup in >60s from task end | RED (page IT Manager) |
| Git push failure | >1 failed push | Yellow |
| Cold storage age | >24 hours without sync | Yellow |
| Recovery test failure | Any failed restore | RED (page IT Manager + CTO) |

---

## BACKUP MANAGER (Marcus Webb III — IT-01)

**Role**: Owns the backup pipeline. Every backup goes through him.
**Staff**: 30 engineers across 4 pods (Execution, Verification, Retention, Disaster Recovery)
**Escalation**:
- Yellow alert → Marcus reviews within 5 minutes
- Red alert → Marcus pages Department Heads + CTO within 1 minute
- Recovery drill → Marcus runs full restore test monthly, reports to Megan

**Marcus's rules**:
1. Every backup must have a SHA-256 checksum manifest
2. No backup older than 60 seconds from task completion
3. Git must be clean (no uncommitted changes) at all times
4. Failed backup = immediate retry, no exceptions
5. Monthly recovery test: random restore from cold storage

---

## ENFORCEMENT

Every manager ensures their team follows backup protocol:
- **Sales Manager Aisha**: "Post on Reddit → backup" — agent doesn't advance to next task until backup verified
- **Content Manager Emily**: "Write blog post → backup" — post not published until backup confirmed
- **Video Manager Victor**: "Render episode → backup" — render not uploaded until backup verified
- **All 39 managers**: Same rule, same enforcement

**IT audits weekly**: Random sample of 100 tasks → check backup timestamps. Any task missing backup within 60 seconds = manager flagged.

---

## IMMEDIATE ACTIONS

1. This document is now backed up per the rule it describes
2. Marcus Webb III is designated Backup Manager
3. All 39 managers receive backup training within 24 hours
4. post-write.sh hook is the system-wide enforcement mechanism

---

*Rule established: Every task → 3 backups immediately. IT monitors all. No exceptions.*

— Saul, CGO
