#!/usr/bin/env python3
"""
QA Bug Monitor Daemon — Runs 24/7, scans every 6 hours, alerts on bugs.
Lives forever. Never stops. Trade #10 is permanent.
"""
import os, time, json, subprocess, sys, hashlib
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = "/var/openclaw_users/saul/.openclaw/workspace"
REPORT_DIR = f"{WORKSPACE}/reports/bugs"
SCAN_SCRIPT = f"{WORKSPACE}/infrastructure/agents/by-department/qa/auto_scan.sh"
HEARTBEAT_FILE = f"{WORKSPACE}/reports/bugs/daemon_heartbeat.json"
PID_FILE = f"{WORKSPACE}/reports/bugs/daemon.pid"

PROJECTS = [
    "atv-homes.vercel.app", "quantumbotsagency.vercel.app",
    "jeannienails.vercel.app", "fallofthecabal.vercel.app",
    "flytoaustralia.vercel.app", "thedealwizard.vercel.app",
    "drugdoctors.vercel.app", "allaboutmd.vercel.app",
    "smallbiz-financing.vercel.app", "quanivo.vercel.app"
]

os.makedirs(REPORT_DIR, exist_ok=True)
os.makedirs(f"{WORKSPACE}/reports/qa", exist_ok=True)

def log(msg):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"[{ts}] {msg}")
    with open(f"{WORKSPACE}/reports/qa/monitor.log", "a") as f:
        f.write(f"[{ts}] {msg}\n")

def write_heartbeat(status):
    hb = {
        "last_ping": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "projects_ok": None,
        "bugs_found": None,
        "pid": os.getpid()
    }
    # Check last report for bug count
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    report_path = f"{REPORT_DIR}/{today}.md"
    if os.path.exists(report_path):
        with open(report_path) as f:
            content = f.read()
        if "Bugs:" in content:
            for line in content.split('\n'):
                if 'Bugs:' in line and 'Summary' in line:
                    hb["bugs_found"] = line.strip()
    with open(HEARTBEAT_FILE, "w") as f:
        json.dump(hb, f, indent=2)

def scan():
    log("═══ QA SCAN START ═══")
    bugs = 0
    critical = 0
    results = []
    
    for project in PROJECTS:
        try:
            status = subprocess.run(
                ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "--max-time", "10", f"https://{project}/"],
                capture_output=True, text=True, timeout=15
            )
            http_status = status.stdout.strip()
            
            has_cs = subprocess.run(
                ["curl", "-s", "--max-time", "10", f"https://{project}/"],
                capture_output=True, text=True, timeout=15
            )
            [REDACTED] = "quantum-cs-v2.js" in has_cs.stdout
            
            result = {
                "project": project,
                "http": http_status,
                "[REDACTED]": [REDACTED],
                "issues": []
            }
            
            if http_status != "200":
                result["issues"].append(f"HTTP {http_status}")
                bugs += 1
                critical += 1
            
            if not [REDACTED]:
                result["issues"].append("Missing CS v2")
                bugs += 1
                critical += 1
            
            results.append(result)
            
            status_icon = "✅" if not result["issues"] else "🔴"
            log(f"  {status_icon} {project} — HTTP {http_status} {'+ CS v2' if [REDACTED] else '⚠️ NO CS'}")
        
        except Exception as e:
            log(f"  ❌ {project} — Error: {e}")
            bugs += 1
    
    # Write report
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    ts = datetime.now(timezone.utc).strftime("%H:%M UTC")
    report = f"# 🔍 QA Bug Report — {today}\n\n## Auto-Scan {ts}\n\n"
    
    for r in results:
        report += f"**{r['project']}** — HTTP {r['http']}\n"
        if r["[REDACTED]"]:
            report += "- ✅ Quantum CS v2 injected\n"
        else:
            report += "- 🔴 Missing Quantum CS v2\n"
        if not r["issues"]:
            report += "- ✅ All good\n"
        else:
            for issue in r["issues"]:
                report += f"- 🔴 {issue}\n"
        report += "\n"
    
    report += "---\n"
    severity = f"**Summary:** {bugs} bugs found (🔴{critical} critical)"
    if bugs == 0:
        severity = "**✅ ZERO BUGS — ALL SYSTEMS NOMINAL**"
    report += severity + "\n"
    
    report_path = f"{REPORT_DIR}/{today}.md"
    # Append new scan section
    mode = "a" if os.path.exists(report_path) else "w"
    with open(report_path, mode) as f:
        if mode == "a":
            f.write("\n\n")
        f.write(f"### Auto-Scan {ts}\n\n")
        for r in results:
            f.write(f"**{r['project']}** — HTTP {r['http']}\n")
            if r["[REDACTED]"]:
                f.write("- ✅ CS v2\n")
            else:
                f.write("- 🔴 NO CS v2\n")
            f.write("\n")
        f.write(f"**Result: {severity}**\n\n")
    
    write_heartbeat("ok" if bugs == 0 else "bugs_found")
    log(f"═══ SCAN COMPLETE — {severity} ═══")
    
    # If bugs found, write to alert file
    if bugs > 0:
        with open(f"{WORKSPACE}/reports/qa/latest_alert.md", "w") as f:
            f.write(f"# 🚨 QA ALERT — {today}\n\n")
            f.write(f"**{bugs} bugs found**\n\n")
            for r in results:
                if r["issues"]:
                    f.write(f"- {r['project']}: {', '.join(r['issues'])}\n")
            f.write(f"\nFull report: reports/bugs/{today}.md\n")
        log(f"🚨 ALERT: {bugs} bugs written to reports/qa/latest_alert.md")
    
    return bugs

def run_forever():
    pid = os.getpid()
    with open(PID_FILE, "w") as f:
        f.write(str(pid))
    
    log(f"QA Monitor Daemon started (PID: {pid})")
    log("Scanning all 10 projects every 6 hours — forever.")
    log("Trade #10: QA/Bug Detection — permanent, immutable.")
    
    interval = 6 * 3600  # 6 hours
    scan()  # Run immediately
    
    while True:
        time.sleep(interval)
        try:
            scan()
        except Exception as e:
            log(f"❌ Scan error: {e}")
            write_heartbeat(f"error: {e}")

if __name__ == "__main__":
    run_forever()
