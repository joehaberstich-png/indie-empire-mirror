# Backup Portal — Standalone Recovery Console

## Overview
This portal lives independently from all main projects. Used for emergency recovery if primary platforms (Vercel, GitHub) go down.

## Host Locations
| Platform | URL | Status |
|----------|-----|--------|
| Local | `/var/openclaw_users/saul/.openclaw/workspace/backup-portal/` | ✅ Live |
| Vercel (separate project) | Deploy pending — midnight UTC | ⏳ Queued |
| GitHub Pages | Needs repo creation with full-scope token | ⏳ Queued |

## Access
- Username: `indie_empire`
- Password: `Recovery@2026!`

## Credentials Backup
Back Office: `jeannienails.vercel.app/manage/` — `jeannie_admin` / `JN@SheetHbr2026!`
Training: `jeannienails.vercel.app/training/` — `student` / `learn2026`

## Recovery Procedure
1. Open this portal (local or hosted copy)
2. Click "Initiate Recovery" to trigger restore sequence
3. All snapshots stored in 3 locations:
   - `.backup/snapshots/` (local)
   - Git history (local)
   - MEMORY.md hard references (local)

## Independence Guarantee
This portal and its backups are NOT hosted on Vercel or GitHub as primary. Source files are in this workspace. A separate deploy target will be added on midnight UTC when deploy limit resets.
