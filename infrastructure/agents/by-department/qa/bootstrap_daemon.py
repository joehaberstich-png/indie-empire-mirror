#!/usr/bin/env python3
"""
QA Daemon Bootstrap — called by OpenClaw heartbeat & start scripts.
Ensures the daemon is always running. Never dies.
"""
import os, sys, time, subprocess

WORKSPACE = "/var/openclaw_users/saul/.openclaw/workspace"
DAEMON = f"{WORKSPACE}/infrastructure/agents/by-department/qa/qa_daemon.py"
PID_FILE = f"{WORKSPACE}/reports/bugs/daemon.pid"
HEARTBEAT = f"{WORKSPACE}/reports/bugs/daemon_heartbeat.json"
LOG = f"{WORKSPACE}/reports/qa/monitor.log"

def is_running():
    if not os.path.exists(PID_FILE):
        return False
    with open(PID_FILE) as f:
        pid = f.read().strip()
    if not pid:
        return False
    try:
        pid = int(pid)
        os.kill(pid, 0)
        return True
    except (OSError, ValueError):
        return False

def start():
    if is_running():
        print("✅ QA daemon already running")
        return True
    
    print("🚀 Starting QA daemon...")
    subprocess.Popen(
        ["python3", DAEMON],
        stdout=open(LOG, "a"),
        stderr=subprocess.STDOUT,
        cwd=WORKSPACE,
        start_new_session=True
    )
    time.sleep(3)
    
    if is_running():
        print("✅ QA daemon started successfully")
        
        # Set heartbeat
        import json
        hb = {
            "last_ping": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()),
            "status": "started",
            "pid": int(open(PID_FILE).read().strip()),
            "auto_restart": True,
            "interval_hours": 6,
            "permanent": True,
            "immutable_trade": 10
        }
        os.makedirs(os.path.dirname(HEARTBEAT), exist_ok=True)
        with open(HEARTBEAT, "w") as f:
            json.dump(hb, f, indent=2)
        return True
    
    print("❌ Failed to start QA daemon")
    return False

if __name__ == "__main__":
    success = start()
    sys.exit(0 if success else 1)
