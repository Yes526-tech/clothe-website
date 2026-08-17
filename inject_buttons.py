import os
import glob

html_files = glob.glob('views/*.html')

buttons_html = """
      <!-- NEW: Authentication Buttons -->
      <li>
        <a href="/auth" style="padding: 6px 14px; border: 1px solid rgba(198,168,124,0.5); color: #c6a87c; text-decoration: none; border-radius: 4px; transition: all 0.3s; font-family: 'Outfit', sans-serif; letter-spacing: 0.1em; font-size: 13px;" onmouseover="this.style.backgroundColor='rgba(198,168,124,0.1)'; this.style.borderColor='#c6a87c'" onmouseout="this.style.backgroundColor='transparent'; this.style.borderColor='rgba(198,168,124,0.5)'">LOG IN</a>
      </li>
      <li>
        <a href="/auth" style="padding: 6px 14px; background-color: #3A0B1A; border: 1px solid #c6a87c; color: #FDF5E6; text-decoration: none; border-radius: 4px; box-shadow: 0 4px 10px rgba(0,0,0,0.3); transition: all 0.3s; font-family: 'Outfit', sans-serif; letter-spacing: 0.1em; font-size: 13px;" onmouseover="this.style.backgroundColor='#5A122A'" onmouseout="this.style.backgroundColor='#3A0B1A'">SIGN UP</a>
      </li>
"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to inject before the cart button.
    # The cart button line usually contains `class="w-cart-btn"`
    lines = content.split('\n')
    new_lines = []
    
    # Since there's a mobile nav cart button too, we only want to inject in the top navbar.
    # We can flag when we are in the main navbar.
    in_nav = False
    injected = False
    
    for line in lines:
        if '<nav class="w-navbar"' in line:
            in_nav = True
        
        if in_nav and not injected and 'class="w-cart-btn"' in line:
            new_lines.append(buttons_html)
            injected = True
        
        if '</nav>' in line:
            in_nav = False
            
        new_lines.append(line)
        
        # Also need to modify <ul class="w-nav-links"> to have align-items: center if it's the second one (the one with the cart).
        # Actually it's easier to just inject the style into the second w-nav-links.
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))

print(f"Processed {len(html_files)} files.")
