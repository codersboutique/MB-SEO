import os
import re

directory = "seo-pages"
files = os.listdir(directory)

def fix_content(content):
    lines = content.splitlines()
    new_lines = []
    in_keywords_section = False
    
    for line in lines:
        # Detect if we are in the Related Keywords section
        if "## Related Keywords" in line:
            in_keywords_section = True
        elif line.startswith("## ") and "Related Keywords" not in line:
            in_keywords_section = False
            
        # Decision logic
        if in_keywords_section:
            # maintain lowercase for keywords if they are list items
            if line.strip().startswith("- "):
                new_lines.append(line)
            else:
                # Still fix prose in this section if there is any (unlikely)
                new_lines.append(line.replace("Gtm", "GTM"))
        else:
            # Fix Headers
            if line.startswith("#"):
                # aggressive fix for headers
                fixed_line = line.replace("Gtm", "GTM")
                new_lines.append(fixed_line)
            else:
                # Fix body text
                # Fix "Gtm" word when it appears as a distinct word or part of a phrase mostly
                # We simply replace "Gtm" with "GTM" but we should be careful about "gtm" (lowercase)
                # The issue is specifically "Gtm" (Title case) appearing where it should be "GTM"
                
                # Replace "Gtm " with "GTM "
                # Replace " Gtm" with " GTM"
                # Replace "**Gtm" with "**GTM"
                # Replace "Gtm**" with "GTM**"
                
                # Simple string replace for "Gtm" -> "GTM" usually is safe for the Title Case version.
                # We rarely see "Gtm" used correctly as Title Case (it's an acronym).
                
                fixed_line = line.replace("Gtm", "GTM")
                
                # Also check for "Full Stack Gtm" -> "Full Stack GTM"
                # "what is gtm" -> "what is GTM" (optional, but finding "gtm" lowercase in prose is rare unless strictly keyword matching)
                # The user's content seems to use "gtm" in bold: "**gtm strategy**".
                # Should we upper case that? "**gtm strategy**" -> "**GTM Strategy**"?
                # "Unlock the potential of **gtm strategy**" -> This looks like a variable insertion.
                # I will focus on "Gtm" -> "GTM" first as that is the clear error.
                
                new_lines.append(fixed_line)

    return "\n".join(new_lines)

count_fixed = 0
for filename in files:
    if not filename.endswith(".md"):
        continue
        
    filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        content = f.read()
        
    new_content = fix_content(content)
    
    if new_content != content:
        with open(filepath, "w") as f:
            f.write(new_content)
        count_fixed += 1

print(f"Fixed {count_fixed} files.")
