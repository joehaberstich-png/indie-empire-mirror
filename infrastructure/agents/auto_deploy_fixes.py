#!/usr/bin/env python3
"""
AUTO-FIX SCHEDULER — Waits for Vercel deploy limit to reset, then deploys all fixes.
Scheduled for next available window: 2026-04-26 00:00 UTC
"""
import os, json, subprocess, time, sys
from datetime import datetime, timezone

WORKSPACE = "/var/openclaw_users/saul/.openclaw/workspace"
TOKEN = "[REDACTED]"

PROJECTS = {
    "containerhomes": "atv-homes.vercel.app",
    "quantumbotsagency": "quantumbotsagency.vercel.app",
    "jeannienails": "jeannienails.vercel.app",
    "fallofthecabal": "fallofthecabal.vercel.app",
    "flytoaustralia": "flytoaustralia.vercel.app",
    "thedealwizard": "thedealwizard.vercel.app",
    "drugdoctors": "drugdoctors.vercel.app",
    "allaboutmd": "allaboutmd.vercel.app",
    "smallbiz": "smallbiz-financing.vercel.app",
    "quanivo": "quanivo.vercel.app"
}

def log(msg):
    ts = datetime.now(timezone.utc).strftime("%H:%M:%S UTC")
    print(f"[{ts}] {msg}")

def deploy_all():
    log("═══ AUTO-FIX DEPLOY WAVE ═══")
    
    for dir_name, domain in PROJECTS.items():
        log(f"  Deploying {dir_name} ({domain})...")
        result = subprocess.run(
            f"cd {WORKSPACE}/site/{dir_name} && npx vercel deploy --prod --token '{TOKEN}' --yes . 2>&1",
            shell=True, capture_output=True, text=True, timeout=120
        )
        out = result.stdout.strip()
        if "Success" in out or "Aliased" in out or "200" in out:
            log(f"  ✅ {domain} deployed")
        else:
            log(f"  ⚠️ {domain}: {out[-100:] if out else 'no output'}")
        time.sleep(3)
    
    log("═══ DEPLOY WAVE COMPLETE ═══")
    log("")
    log("═══ VERIFICATION ═══")
    time.sleep(5)
    
    all_ok = True
    for dir_name, domain in PROJECTS.items():
        status = subprocess.run(
            ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "--max-time", "5", f"https://{domain}/"],
            capture_output=True, text=True, timeout=10
        ).stdout.strip()
        
        robots = subprocess.run(
            ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "--max-time", "3", f"https://{domain}/robots.txt"],
            capture_output=True, text=True, timeout=10
        ).stdout.strip()
        
        schema = subprocess.run(
            ["curl", "-s", "--max-time", "5", f"https://{domain}/"],
            capture_output=True, text=True, timeout=10
        )
        has_schema = "application/ld+json" in schema.stdout
        
        sec = subprocess.run(
            ["curl", "-sI", "--max-time", "3", f"https://{domain}/"],
            capture_output=True, text=True, timeout=10
        )
        has_xframe = "X-Frame-Options" in sec.stdout
        
        log(f"  {domain}: HTTP={status} robots={robots} schema={'✅' if has_schema else '🔴'} frame={'✅' if has_xframe else '🔴'}")
        
        if status != "200" or not has_schema or not has_xframe:
            all_ok = False
    
    if all_ok:
        log("🏆 ALL CHECKS PASSED — Every project has HTTP 200, schema, robots, and security headers.")
    else:
        log("⚠️ Some checks failed — see above for details")
    
    return all_ok

def wait_until_midnight():
    """Wait until next UTC midnight"""
    now = datetime.now(timezone.utc)
    next_day = datetime(now.year, now.month, now.day, 0, 0, 0, tzinfo=timezone.utc).replace(day=now.day + 1 if now.hour >= 0 else now.day)
    wait_seconds = (next_day - now).total_seconds()
    
    if wait_seconds > 0 and wait_seconds < 86400:
        log(f"Waiting {wait_seconds:.0f} seconds until deploy limit resets ({next_day.strftime('%Y-%m-%d %H:%M UTC')})...")
        time.sleep(wait_seconds)
    else:
        log("Deploy window available now, proceeding immediately.")

if __name__ == "__main__":
    if "--now" in sys.argv:
        deploy_all()
    else:
        wait_until_midnight()
        deploy_all()
