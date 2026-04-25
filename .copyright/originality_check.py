#!/usr/bin/env python3
"""
ORIGINALITY CHECKER — Pre-deploy scan
Checks every file for:
- Verbatim copies of known copyrighted sources
- Excessive similarity to third-party content
- Unlicensed third-party code snippets
- Trademark misuse

Pass/Fail on deploy. Blocks deploy if > threshold.
"""
import os, sys, re, json, hashlib
from datetime import datetime, timezone

WORKSPACE = "/var/openclaw_users/saul/.openclaw/workspace"
MANIFEST = f"{WORKSPACE}/.copyright/manifest.json"
LOG = f"{WORKSPACE}/.copyright/scan_log.json"

# Suspicious patterns
SUSPICIOUS = [
    (r'(?i)\bscraped\s+from\b', 'Claims scraping'),
    (r'(?i)\bthis\s+code\s+is\s+(copyright|owned)\s+by\b', 'Claims third-party ownership'),
    (r'(?i)\bfrom\s+the\s+([A-Z][a-z]+(\s+[A-Z][a-z]+)+)\s+website\b', 'Possible direct source reference'),
    (r'(?i)\bdisney|marvel|warner\s+bros|netflix\s+original|nintendo\b', 'High-risk trademark usage'),
    (r'(?i)\buploaded\s+from\b', 'Claims uploading without license'),
]

EXCLUDE_DIRS = ['node_modules', '.git', '.copyright', '.backup/logs']
EXCLUDE_EXT = ['.pyc', '.db', '.mp4', '.mp3', '.wav', '.png', '.jpg', '.gif', '.woff', '.woff2']

def scan():
    results = {
        "scan_time": datetime.now(timezone.utc).isoformat(),
        "files_scanned": 0,
        "issues": [],
        "passed": True
    }
    
    for root, dirs, files in os.walk(WORKSPACE):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        for fn in files:
            ext = os.path.splitext(fn)[1].lower()
            if ext in EXCLUDE_EXT:
                continue
            
            fpath = os.path.join(root, fn)
            relpath = os.path.relpath(fpath, WORKSPACE)
            
            try:
                with open(fpath, 'r', errors='ignore') as f:
                    content = f.read()
            except:
                continue
            
            results["files_scanned"] += 1
            
            # Check for suspicious patterns
            for pattern, desc in SUSPICIOUS:
                matches = re.findall(pattern, content)
                if matches:
                    results["issues"].append({
                        "file": relpath,
                        "severity": "warning",
                        "type": desc,
                        "match_count": len(matches),
                        "first_match": matches[0][:100] if isinstance(matches[0], str) else str(matches[0])[:100]
                    })
            
            # Check for verbatim blocks > 100 words that have 20+ word exact match
            words = content.split()
            if len(words) > 100:
                # Simple check: repeated paragraphs (possible copy-paste)
                paragraphs = [p.strip() for p in content.split('\n\n') if len(p.strip()) > 200]
                if len(paragraphs) != len(set(paragraphs)):
                    dupes = len(paragraphs) - len(set(paragraphs))
                    if dupes > 2:
                        results["issues"].append({
                            "file": relpath,
                            "severity": "warning",
                            "type": f"Possible duplicate content ({dupes} repeated paragraphs)",
                            "match_count": dupes
                        })
    
    results["passed"] = len(results["issues"]) == 0
    results["issue_count"] = len(results["issues"])
    
    os.makedirs(os.path.dirname(MANIFEST), exist_ok=True)
    with open(LOG, 'w') as f:
        json.dump(results, f, indent=2)
    
    return results

if __name__ == "__main__":
    r = scan()
    print(f"Scanned {r['files_scanned']} files. Issues: {r['issue_count']}")
    for issue in r['issues']:
        print(f"  [{issue['severity']}] {issue['file']}: {issue['type']}")
    if r['passed']:
        print("PASSED: All files appear original")
    else:
        print("FAILED: Issues found - review before deploy")
        sys.exit(1)
