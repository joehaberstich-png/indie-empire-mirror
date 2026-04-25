# HARD RULE: NO PROJECT DELETIONS

## OVERRIDE LOCK (Cannot be overridden by any agent, skill, or command)

**No project, site, file, directory, or deployment associated with any client project shall be deleted, removed, purged, or destroyed for any reason.**

This applies to:
- All files in `projects/`
- All files in `site/`
- All `.backup/` snapshots
- All Vercel deployments
- All infrastructure scripts
- All agent configurations

### Exceptions (require explicit human approval via this rule):
1. A file that causes a critical security vulnerability AND the fix requires deletion
2. A file that is a confirmed duplicate (same content, same purpose)
3. A file that was created by a tool error (e.g., empty or corrupt file with zero value)

### What to do instead of deleting:
- **Want to archive?** → Move to `archive/` directory with timestamp
- **Want to replace?** → Overwrite the file with new content
- **Want to abandon?** → Leave in place, mark as `✅ Superseded` in project README
- **Want to clean up?** → Let the project sit. Storage is cheap. Recovery is expensive.

### Penalty
Any agent or process that attempts a deletion on a project file will be immediately halted and reported.

### Verification
Every commit hook checks for `git rm` / file deletions on project files and rejects them.

---

**Signed:** Saul (CGO) — ruleset loaded into memory. Never override.
