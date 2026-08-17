import glob

html_files = glob.glob('views/*.html')

old_auth_block = """      <!-- NEW: Authentication Buttons -->
      <li>
        <span onclick="window.location.href='/auth?mode=login'" style="cursor: pointer; padding: 6px 14px; color: #c6a87c; transition: color 0.3s; font-family: 'Outfit', sans-serif; letter-spacing: 0.14em; font-size: 11px; text-transform: uppercase; font-weight: 500;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#c6a87c'">LOG IN</span>
      </li>
      <li>
        <span onclick="window.location.href='/auth?mode=signup'" style="cursor: pointer; padding: 6px 14px; color: #c6a87c; transition: color 0.3s; font-family: 'Outfit', sans-serif; letter-spacing: 0.14em; font-size: 11px; text-transform: uppercase; font-weight: 500;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#c6a87c'">SIGN UP</span>
      </li>"""

new_auth_block = """      <!-- NEW: Authentication Buttons -->
      <li id="auth-buttons" style="display: flex; gap: 1rem;">
        <span onclick="window.location.href='/auth?mode=login'" style="cursor: pointer; padding: 6px 14px; color: #c6a87c; transition: color 0.3s; font-family: 'Outfit', sans-serif; letter-spacing: 0.14em; font-size: 11px; text-transform: uppercase; font-weight: 500;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#c6a87c'">LOG IN</span>
        <span onclick="window.location.href='/auth?mode=signup'" style="cursor: pointer; padding: 6px 14px; color: #c6a87c; transition: color 0.3s; font-family: 'Outfit', sans-serif; letter-spacing: 0.14em; font-size: 11px; text-transform: uppercase; font-weight: 500;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#c6a87c'">SIGN UP</span>
      </li>
      <li id="user-profile-menu" class="w-dropdown" style="display: none; position: relative;">
        <span style="cursor: pointer; color: #c6a87c; padding: 6px 14px; display: flex; align-items: center; transition: color 0.3s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#c6a87c'">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
        </span>
        <div class="w-dropdown-content" style="right: 0; left: auto; min-width: 220px; padding-top: 15px; border: 1px solid rgba(198,168,124,0.2); border-top: none; box-shadow: 0 10px 25px rgba(0,0,0,0.5);">
          <a href="#">My Account</a>
          <a href="#">Order Tracking & History</a>
          <a href="#">My Wishlist / Saved Items</a>
          <a href="#">Settings</a>
          <div style="height: 1px; background-color: rgba(198,168,124,0.2); margin: 4px 0;"></div>
          <a href="#" onclick="toggleAuthState(false); return false;" style="color: #ff4d4d !important; display: flex; align-items: center; justify-content: space-between;">Log Out <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg></a>
        </div>
      </li>"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(old_auth_block, new_auth_block)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated auth elements in {len(html_files)} files.")
