import os
import re

directory = "seo-pages"
files = os.listdir(directory)
files.sort()

issues = []
stats = {
    "total": 0,
    "missing_cta": 0,
    "missing_keywords": 0,
    "missing_breakdown": 0,
    "gtm_capitalization": 0,
    "short_content": 0
}

for filename in files:
    if not filename.endswith(".md"):
        continue
    
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        content = f.read()
    
    stats["total"] += 1
    file_issues = []

    # Check for CTA
    if "Ready to Scale Your GTM?" not in content:
        file_issues.append("Missing CTA")
        stats["missing_cta"] += 1

    # Check for Related Keywords
    if "## Related Keywords" not in content:
        file_issues.append("Missing Related Keywords")
        stats["missing_keywords"] += 1

    # Check for Detailed Breakdown
    if "## Detailed Breakdown" not in content:
        file_issues.append("Missing Detailed Breakdown")
        stats["missing_breakdown"] += 1
        
    # Check for "Gtm" instead of "GTM" in Headers
    # We look for "# ... Gtm" or "## ... Gtm"
    if re.search(r"^#{1,3} .*Gtm\b", content, re.MULTILINE):
        file_issues.append("Header has 'Gtm' instead of 'GTM'")
        stats["gtm_capitalization"] += 1

    # Check content length (heuristic)
    if len(content.splitlines()) < 20:
        file_issues.append("Content very short (< 20 lines)")
        stats["short_content"] += 1

    if file_issues:
        issues.append(f"{filename}: {', '.join(file_issues)}")

print(f"Reviewed {stats['total']} files.")
print("--- Usage Stats ---")
for k, v in stats.items():
    if k != "total":
        print(f"{k}: {v}")

print("\n--- Issues Found ---")
if issues:
    for issue in issues:
        print(issue)
else:
    print("No major structural issues found.")
