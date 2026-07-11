import os
import re
import sys

def verify_files():
    required_files = ['index.html', 'styles.css', 'impressum.html', 'datenschutz.html']
    missing_files = []
    
    print("=== Step 1: Checking Required Files ===")
    for filename in required_files:
        if os.path.exists(filename):
            print(f"✓ Found: {filename} ({os.path.getsize(filename)} bytes)")
        else:
            print(f"✗ Missing: {filename}")
            missing_files.append(filename)
            
    if missing_files:
        print(f"\nCRITICAL: Missing required files: {missing_files}")
        return False
        
    print("\n=== Step 2: Checking HTML Link Integrity ===")
    html_files = [f for f in required_files if f.endswith('.html')]
    all_links_valid = True
    
    for html_file in html_files:
        print(f"\nScanning: {html_file}")
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Check Stylesheets
        stylesheets = re.findall(r'<link[^>]+href=["\']([^"\']+)["\']', content)
        for ss in stylesheets:
            if not ss.startswith('http') and not ss.startswith('//'):
                # Local reference
                clean_path = ss.split('#')[0].split('?')[0]
                if os.path.exists(clean_path):
                    print(f"  ✓ Stylesheet Link Valid: {ss}")
                else:
                    print(f"  ✗ Stylesheet Link Broken: {ss}")
                    all_links_valid = False
                    
        # 2. Check Local Hyperlinks
        hrefs = re.findall(r'<a[^>]+href=["\']([^"\']+)["\']', content)
        for href in hrefs:
            # Skip external links and hash-only links on the same page
            if href.startswith('http') or href.startswith('mailto:') or href.startswith('tel:') or href == '#' or href.startswith('#'):
                continue
                
            # Local page reference
            # Remove hash segment if any
            clean_href = href.split('#')[0]
            if clean_href:
                if os.path.exists(clean_href):
                    print(f"  ✓ Link Valid: {href}")
                else:
                    print(f"  ✗ Link Broken: {href}")
                    all_links_valid = False
                    
    if not all_links_valid:
        print("\nCRITICAL: Found broken local link references.")
        return False
        
    print("\n=== All checks passed! Landing page is fully verified and consistent! ===")
    return True

if __name__ == '__main__':
    success = verify_files()
    if not success:
        sys.exit(1)
    sys.exit(0)
