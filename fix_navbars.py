import os
import glob
import re

html_files = glob.glob('views/*.html')

new_right_nav = """    <ul class="w-nav-links">
      <li><a href="#" style="color: #c6a87c;">ARAMA</a></li>
      <li><a href="#" style="color: #c6a87c;" onclick="event.preventDefault(); openFavDrawer()">FAVORİLER</a></li>
      <li><button class="w-cart-btn" id="open-cart-btn" style="color: #c6a87c;" onclick="openCartDrawer()">SEPET (<span id="w-cart-count">0</span>)</button></li>

      <!-- NEW: Authentication Buttons -->
      <li id="auth-buttons" style="display: flex; gap: 1rem;">
        <span onclick="window.location.href='/auth?mode=login'" style="cursor: pointer; padding: 6px 14px; color: #c6a87c; transition: color 0.3s; font-family: 'Outfit', sans-serif; letter-spacing: 0.14em; font-size: 11px; text-transform: uppercase; font-weight: 500;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#c6a87c'">LOG IN</span>
        <span onclick="window.location.href='/auth?mode=signup'" style="cursor: pointer; padding: 6px 14px; color: #c6a87c; transition: color 0.3s; font-family: 'Outfit', sans-serif; letter-spacing: 0.14em; font-size: 11px; text-transform: uppercase; font-weight: 500;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#c6a87c'">SIGN UP</span>
      </li>

      <li id="user-profile-menu" class="w-dropdown" style="display: none; position: relative;">
        <span style="cursor: pointer; color: #c6a87c; padding: 6px 14px; display: flex; align-items: center; transition: color 0.3s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#c6a87c'">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
            <circle cx="12" cy="7" r="4"></circle>
          </svg>
        </span>
        <div class="w-dropdown-content" style="right: 0; left: auto; min-width: 220px; padding-top: 15px; border: 1px solid rgba(198,168,124,0.2); border-top: none; box-shadow: 0 10px 25px rgba(0,0,0,0.5);">
          <a href="#">My Account</a>
          <a href="#">Order Tracking & History</a>
          <a href="#">My Wishlist / Saved Items</a>
          <a href="#">Settings</a>
          <div style="height: 1px; background-color: rgba(198,168,124,0.2); margin: 4px 0;"></div>
          <a href="#" onclick="toggleAuthState(false); return false;" style="color: #ff4d4d !important; display: flex; align-items: center; justify-content: space-between;">Log Out 
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
              <polyline points="16 17 21 12 16 7"></polyline>
              <line x1="21" y1="12" x2="9" y2="12"></line>
            </svg>
          </a>
        </div>
      </li>
    </ul>"""

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The right nav always starts after the logo: class="w-logo"
    # So we can search for the first <ul class="w-nav-links"> AFTER <a href="/" class="w-logo"...>
    
    parts = re.split(r'(<a[^>]*class="w-logo"[^>]*>.*?</a>)', content, flags=re.IGNORECASE)
    
    if len(parts) >= 3:
        # parts[0] is everything before logo (including left nav)
        # parts[1] is the logo
        # parts[2] is everything after logo (including right nav)
        
        # Now we find the first <ul class="w-nav-links"> ... </ul> in parts[2] and replace it.
        # We need a regex that matches from <ul class="w-nav-links"> to its matching </ul>.
        # Since HTML isn't regular, but the structure here is simple, we can use a non-greedy match.
        # BUT there are inner <ul> elements? No, the right nav doesn't have nested <ul>.
        
        new_after_logo = re.sub(r'<ul class="w-nav-links">.*?</ul>', new_right_nav, parts[2], count=1, flags=re.DOTALL)
        
        final_content = parts[0] + parts[1] + new_after_logo
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f"Updated {filepath}")
    else:
        print(f"Skipped {filepath} (could not parse layout)")

for f in html_files:
    update_file(f)

