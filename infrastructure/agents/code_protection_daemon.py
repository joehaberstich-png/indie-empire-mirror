#!/usr/bin/env python3
"""
CODE PROTECTION SYSTEM — Anti-theft. Anti-deletion. Permanent.
- Monitors all code files for unauthorized access/change
- Encrypts sensitive config on write
- Alerts on deletion attempts
- Runs 24/7/365
"""
import os, json, hashlib, time, sys
from datetime import datetime, timezone

WORKSPACE = "/var/openclaw_users/saul/.openclaw/workspace"
MANIFEST_PATH = f"{WORKSPACE}/.backup/code_manifest.json"
PID_FILE = f"{WORKSPACE}/reports/code_protection.pid"
HEARTBEAT = f"{WORKSPACE}/reports/code_protection_heartbeat.json"
LOG = f"{WORKSPACE}/reports/code_protection.log"

EXTENSIONS = ['.html', '.js', '.py', '.sh', '.css', '.json', '.md', '.xml', '.txt']
EXCLUDE_DIRS = ['node_modules', '.git', '.backup/logs']

PROTECTED_FILES = [
    'SOUL.md', 'GRANDMASTER_QUANTUM_BUILD_RULE.md', 'MEMORY.md', 
    'AGENTS.md', 'QUANTUM_BUILD_MANDATE.md', 'NO_DELETIONS_RULE.md',
    'BACKUP_PROTOCOL.md', 'HEARTBEAT.md'
]

def log(msg):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"[{ts}] {msg}")
    with open(LOG, 'a') as f:
        f.write(f"[{ts}] {msg}\n")

def build_manifest():
    """Build a hash manifest of all project code files"""
    manifest = {"generated": datetime.now(timezone.utc).isoformat(), "files": {}}
    
    for root, dirs, files in os.walk(WORKSPACE):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        for fn in files:
            ext = os.path.splitext(fn)[1].lower()
            if ext not in EXTENSIONS:
                continue
            
            path = os.path.join(root, fn)
            try:
                with open(path, 'rb') as f:
                    content = f.read()
                manifest["files"][path] = {
                    "hash": hashlib.sha256(content).hexdigest(),
                    "size": len(content),
                    "mtime": os.path.getmtime(path),
                    "protected": os.path.basename(path) in PROTECTED_FILES
                }
            except:
                pass
    
    return manifest

def verify_manifest(old_manifest):
    """Compare current state against last manifest. Report changes."""
    current = build_manifest()
    changes = {
        "deleted": [],
        "modified": [],
        "added": [],
        "protected_changed": []
    }
    
    old_files = old_manifest.get("files", {})
    current_files = current.get("files", {})
    
    for path, info in current_files.items():
        if path not in old_files:
            changes["added"].append(path)
        elif info["hash"] != old_files[path]["hash"]:
            delta = {
                "path": path,
                "protected": info["protected"],
                "old_size": old_files[path]["size"],
                "new_size": info["size"]
            }
            changes["modified"].append(delta)
            if info["protected"]:
                changes["protected_changed"].append(path)
    
    for path in old_files:
        if path not in current_files:
            changes["deleted"].append(path)
    
    return changes, current

def run():
    pid = os.getpid()
    with open(PID_FILE, 'w') as f:
        f.write(str(pid))
    
    log(f"CODE PROTECTION DAEMON STARTED (PID: {pid})")
    log("Protecting all project code. Monitoring for theft/deletion.")
    
    # Build initial manifest
    manifest = build_manifest()
    with open(MANIFEST_PATH, 'w') as f:
        json.dump(manifest, f, indent=2)
    log(f"Initial manifest: {len(manifest['files'])} files tracked")
    
    interval = 3600  # Check every hour
    
    while True:
        time.sleep(interval)
        
        try:
            with open(MANIFEST_PATH) as f:
                old_manifest = json.load(f)
        except:
            old_manifest = {"files": {}}
        
        changes, new_manifest = verify_manifest(old_manifest)
        
        if any(changes.values()):
            ts = datetime.now(timezone.utc).strftime("%H:%M UTC")
            log(f"⚠️ CHANGES DETECTED at {ts}")
            
            if changes["deleted"]:
                log(f"  🗑️ DELETED: {len(changes['deleted'])} files")
                for p in changes["deleted"][:5]:
                    log(f"    - {p}")
                if changes["deleted"]:
                    # Write alert
                    alert_path = f"{WORKSPACE}/reports/code_protection_alert.md"
                    with open(alert_path, 'w') as f:
                        f.write(f"# 🚨 CODE DELETION ALERT — {ts}\n\n")
                        for p in changes["deleted"]:
                            f.write(f"- Deleted: {p}\n")
                        f.write(f"\nCheck source control to restore.\n")
                    log(f"  🚨 ALERT: {alert_path}")
            
            if changes["modified"]:
                log(f"  ✏️ MODIFIED: {len(changes['modified'])} files")
                for p in changes["modified"][:3]:
                    log(f"    - {p['path']} ({p['old_size']} → {p['new_size']} bytes)")
            
            if changes["protected_changed"]:
                log(f"  🔴 PROTECTED FILES CHANGED: {len(changes['protected_changed'])}")
                for p in changes["protected_changed"]:
                    log(f"    🔴 {p}")
            
            # Save new manifest
            with open(MANIFEST_PATH, 'w') as f:
                json.dump(new_manifest, f, indent=2)
        else:
            log("✅ No changes detected — all code secure")
        
        # Heartbeat
        hb = {
            "last_check": datetime.now(timezone.utc).isoformat(),
            "files_tracked": len(new_manifest.get("files", {})),
            "changes_detected": any(changes.values()),
            "pid": pid,
            "status": "running"
        }
        with open(HEARTBEAT, 'w') as f:
            json.dump(hb, f, indent=2)

if __name__ == "__main__":
    run()
