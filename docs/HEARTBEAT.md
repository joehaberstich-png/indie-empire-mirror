# Heartbeat Tasks
- Check pending follow-ups for your department
- If nothing pending, reply HEARTBEAT_OK

# 🔐 BACKUP RULE — ENFORCED ON EVERY TASK
## The 3-Backup Mandate (60-second SLA)
## Number one rule: After EVERY task → 3 backups within 60 seconds
## Covers all 10 projects. Hot-reload daemon runs 24/7.

# Backup Status (auto-updated by daemon)
# Last backup: See .backup/daemon_status.json
# Daemon PID: See .backup/daemon.pid
# Logs: .backup/logs/
# Reports: reports/
# Meetings: meetings/

# ⚡ CEO PERMANENT RULES (see PERMANENT_INFRASTRUCTURE_RULES.md)
# - Audit every 6 hours → ceo_audit_engine.py
# - QA scan every 6 hours → qa_daemon.py
# - Code protection every 1 hour → code_protection_daemon.py
# - Assistant auto-scaler every 5 min → assistant_auto_scaler.py
# - All daemons running 24/7/365. Forever.

# 🚫 ZERO-DELAY MANDATE
# Heartbeat NEVER times out. NEVER delays. Runs 24/7/365.
# Config: timeoutSeconds: 1200, isolatedSession: true, lightContext: true
# Every agent. Every project. Every heartbeat.
# Violation = automatic reversion. CEO-audited every 6 hours.
