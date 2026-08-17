import os
import glob
import re

html_files = glob.glob('views/*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the exact strings. 
    # For LOG IN button:
    content = content.replace('<a href="/auth" style="padding: 6px 14px; border: 1px solid rgba(198,168,124,0.5);', '<a href="/auth?mode=login" style="padding: 6px 14px; border: 1px solid rgba(198,168,124,0.5);')
    
    # For SIGN UP button:
    content = content.replace('<a href="/auth" style="padding: 6px 14px; background-color: #3A0B1A;', '<a href="/auth?mode=signup" style="padding: 6px 14px; background-color: #3A0B1A;')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated links in {len(html_files)} files.")
