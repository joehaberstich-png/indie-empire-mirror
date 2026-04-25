#!/usr/bin/env python3
"""
VERIFY ALL ANCHORS - TOC Links, Section Headings, Navigation
MUST PASS BEFORE DEPLOYMENT
"""

import os
import re
import sys

def verify_anchors():
    """Verify ALL anchors in ALL HTML files"""
    print("=" * 80)
    print("VERIFYING ALL ANCHORS - PRE-DEPLOYMENT CHECK")
    print("=" * 80)
    
    base_dir = "/var/openclaw_users/bb/.openclaw/workspace/flytoaustralia.com"
    articles_dir = os.path.join(base_dir, "articles")
    
    all_passed = True
    total_issues = 0
    
    # 1. Check all articles with TOC
    print("\n1. CHECKING ARTICLES WITH TABLE OF CONTENTS:")
    print("-" * 60)
    
    articles_with_toc = [
        'sydney-guide.html',
        'australia-budget-guide.html', 
        'working-holiday-visa-guide.html',
        'relocation-guide.html'
    ]
    
    for article in articles_with_toc:
        article_path = os.path.join(articles_dir, article)
        if not os.path.exists(article_path):
            print(f"❌ {article}: File not found")
            all_passed = False
            total_issues += 1
            continue
        
        with open(article_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"\n📄 {article}:")
        
        # Find TOC
        toc_pattern = r'<!-- Table of Contents -->.*?</ul>'
        toc_match = re.search(toc_pattern, content, re.DOTALL)
        
        if not toc_match:
            print(f"  ❌ No Table of Contents found")
            all_passed = False
            total_issues += 1
            continue
        
        toc_content = toc_match.group(0)
        toc_links = re.findall(r'<a href=\"#([^\"]+)\">([^<]+)</a>', toc_content)
        
        if not toc_links:
            print(f"  ❌ No TOC links found")
            all_passed = False
            total_issues += 1
            continue
        
        print(f"  Found {len(toc_links)} TOC links")
        
        article_issues = 0
        for anchor, text in toc_links:
            # Check if anchor exists
            if f'id="{anchor}"' not in content:
                print(f"    ❌ #{anchor}: \"{text}\" - ANCHOR MISSING!")
                all_passed = False
                article_issues += 1
                total_issues += 1
            else:
                # Check if it's on an h2 heading
                h2_pattern = f'<h2[^>]*id=\"{anchor}\"[^>]*>([^<]+)</h2>'
                h2_match = re.search(h2_pattern, content)
                
                if not h2_match:
                    print(f"    ⚠️  #{anchor}: \"{text}\" - Anchor exists but not on h2")
                    # Not fatal, but should be fixed
                else:
                    # Check section content length
                    section_start = h2_match.start()
                    # Find next h2 or end of section
                    next_h2 = content.find('<h2', section_start + 10)
                    if next_h2 == -1:
                        next_h2 = content.find('</section>', section_start)
                    if next_h2 == -1:
                        next_h2 = len(content)
                    
                    section = content[section_start:next_h2]
                    # Remove HTML tags for word count
                    text_only = re.sub(r'<[^>]*>', ' ', section)
                    words = len(text_only.split())
                    
                    if words < 100:
                        print(f"    ⚠️  #{anchor}: \"{text}\" - Only {words} words (min: 100)")
                        # Warning, not error
                    else:
                        print(f"    ✅ #{anchor}: \"{text}\" - {words} words")
        
        if article_issues == 0:
            print(f"  ✅ All TOC anchors verified")
    
    # 2. Check main navigation links
    print("\n2. CHECKING MAIN NAVIGATION LINKS:")
    print("-" * 60)
    
    main_pages = [
        'index.html',
        'destinations.html',
        'visa-guide.html',
        'itineraries.html',
        'blog.html',
        'resources.html',
        'contact.html'
    ]
    
    for page in main_pages:
        page_path = os.path.join(base_dir, page)
        if not os.path.exists(page_path):
            print(f"❌ {page}: File not found")
            all_passed = False
            total_issues += 1
            continue
        
        print(f"✅ {page}: Exists")
    
    # 3. Check all internal links for validity
    print("\n3. CHECKING INTERNAL LINK PATTERNS:")
    print("-" * 60)
    
    html_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    internal_link_issues = 0
    
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all internal links
        internal_links = re.findall(r'href=["\']([^"\']*\.html[^"\']*)["\']', content)
        
        for link in internal_links:
            # Skip external links
            if link.startswith('http'):
                continue
            
            # Resolve relative path
            if link.startswith('/'):
                target_path = os.path.join(base_dir, link[1:])
            else:
                # Relative to current file
                current_dir = os.path.dirname(html_file)
                target_path = os.path.join(current_dir, link)
            
            # Clean up anchor part
            if '#' in target_path:
                target_path = target_path.split('#')[0]
            
            if not os.path.exists(target_path):
                rel_file = os.path.relpath(html_file, base_dir)
                print(f"❌ {rel_file}: Broken link to {link}")
                all_passed = False
                internal_link_issues += 1
                total_issues += 1
    
    if internal_link_issues == 0:
        print("✅ All internal links valid")
    
    print("\n" + "=" * 80)
    print("VERIFICATION COMPLETE")
    print("=" * 80)
    
    if all_passed:
        print("🎉 ALL ANCHORS VERIFIED - READY FOR DEPLOYMENT")
        print(f"Total issues: {total_issues}")
        return True
    else:
        print(f"❌ VERIFICATION FAILED - {total_issues} ISSUES FOUND")
        print("\nFIX ALL ISSUES BEFORE DEPLOYMENT:")
        print("1. Missing anchors in TOC")
        print("2. Broken internal links")
        print("3. Missing HTML files")
        return False

if __name__ == "__main__":
    success = verify_anchors()
    sys.exit(0 if success else 1)