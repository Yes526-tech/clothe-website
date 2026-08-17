import os
import glob
import re

html_files = glob.glob('views/*.html')

old_auth_block = """      <!-- NEW: Authentication Buttons -->
      <li>
        <a href="/auth?mode=login" style="padding: 6px 14px; border: 1px solid rgba(198,168,124,0.5); color: #c6a87c; text-decoration: none; border-radius: 4px; transition: all 0.3s; font-family: 'Outfit', sans-serif; letter-spacing: 0.1em; font-size: 13px;" onmouseover="this.style.backgroundColor='rgba(198,168,124,0.1)'; this.style.borderColor='#c6a87c'" onmouseout="this.style.backgroundColor='transparent'; this.style.borderColor='rgba(198,168,124,0.5)'">LOG IN</a>
      </li>
      <li>
        <a href="/auth?mode=signup" style="padding: 6px 14px; background-color: #3A0B1A; border: 1px solid #c6a87c; color: #FDF5E6; text-decoration: none; border-radius: 4px; box-shadow: 0 4px 10px rgba(0,0,0,0.3); transition: all 0.3s; font-family: 'Outfit', sans-serif; letter-spacing: 0.1em; font-size: 13px;" onmouseover="this.style.backgroundColor='#5A122A'" onmouseout="this.style.backgroundColor='#3A0B1A'">SIGN UP</a>
      </li>"""

new_auth_block = """      <!-- NEW: Authentication Buttons -->
      <li>
        <span onclick="window.location.href='/auth?mode=login'" style="cursor: pointer; padding: 6px 14px; color: #c6a87c; transition: color 0.3s; font-family: 'Outfit', sans-serif; letter-spacing: 0.14em; font-size: 11px; text-transform: uppercase; font-weight: 500;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#c6a87c'">LOG IN</span>
      </li>
      <li>
        <span onclick="window.location.href='/auth?mode=signup'" style="cursor: pointer; padding: 6px 14px; color: #c6a87c; transition: color 0.3s; font-family: 'Outfit', sans-serif; letter-spacing: 0.14em; font-size: 11px; text-transform: uppercase; font-weight: 500;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#c6a87c'">SIGN UP</span>
      </li>"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We replace the exact old block
    content = content.replace(old_auth_block, new_auth_block)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated buttons in {len(html_files)} files.")
