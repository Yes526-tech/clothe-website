import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import os
import re

views_dir = os.path.join(BASE_DIR, 'views')
js_file = os.path.join(BASE_DIR, 'public/assets/js/script.js')

files_to_update = [
    'index_view.html',
    'collections_view.html',
    'men_view.html',
    'women_view.html',
    'medieval_view.html',
    'graffiti_view.html',
    'sweatshirt_view.html'
]

old_item_html = """      <!-- MOCK ITEM -->
      <div class="cart-drawer-item">
        <img src="/assets/images/prod_sweatshirt.png" alt="Hoodies" class="cart-item-img" />
        <div class="cart-item-details">
          <div class="cart-item-title">Artévia Premium Hoodie</div>
          <div class="cart-item-variant">Beden: L | Renk: Siyah</div>
          <div class="cart-item-price">₺2500</div>
          <div class="cart-item-qty">
            <button class="qty-btn">-</button>
            <span>1</span>
            <button class="qty-btn">+</button>
          </div>
        </div>
      </div>"""

new_item_html = """      <!-- MOCK ITEM -->
      <div class="cart-drawer-item" id="mock-cart-item">
        <img src="/assets/images/prod_sweatshirt.png" alt="Hoodies" class="cart-item-img" />
        <div class="cart-item-details">
          <div class="cart-item-title">Artévia Premium Hoodie</div>
          <div class="cart-item-variant">Beden: L | Renk: Siyah</div>
          <div class="cart-item-price">₺2500</div>
          <div style="display:flex; align-items:center; gap:15px;">
            <div class="cart-item-qty">
              <button class="qty-btn" onclick="updateMockCart(-1)">-</button>
              <span id="mock-cart-qty">1</span>
              <button class="qty-btn" onclick="updateMockCart(1)">+</button>
            </div>
            <button onclick="removeMockCart()" style="background:none; border:none; color:rgba(255,255,255,0.5); font-family:'Outfit', sans-serif; font-size:11px; text-decoration:underline; cursor:pointer;">Sil</button>
          </div>
        </div>
      </div>"""

old_total_html = """      <div class="cart-drawer-total">
        <span>ARA TOPLAM</span>
        <span>₺2500</span>
      </div>"""

new_total_html = """      <div class="cart-drawer-total">
        <span>ARA TOPLAM</span>
        <span>₺<span id="mock-total-price">2500</span></span>
      </div>"""

for filename in files_to_update:
    filepath = os.path.join(views_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the HTML chunks
        content = content.replace(old_item_html, new_item_html)
        content = content.replace(old_total_html, new_total_html)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated HTML: {filename}")

# APPEND JS
js_logic = """
// CART DRAWER DYNAMIC LOGIC
function updateMockCart(change) {
  const qtyEl = document.getElementById('mock-cart-qty');
  const priceEl = document.getElementById('mock-total-price');
  if(!qtyEl) return;
  
  let currentQty = parseInt(qtyEl.innerText);
  currentQty += change;
  if(currentQty < 1) currentQty = 1; // Minimum 1, use 'Sil' to remove
  
  qtyEl.innerText = currentQty;
  if(priceEl) priceEl.innerText = currentQty * 2500;
}

function removeMockCart() {
  const itemEl = document.getElementById('mock-cart-item');
  const priceEl = document.getElementById('mock-total-price');
  if(itemEl) itemEl.style.display = 'none';
  if(priceEl) priceEl.innerText = '0';
  
  // Also empty the cart counter
  const countSpan = document.getElementById('w-cart-count');
  if (countSpan) {
    countSpan.innerText = '0';
    localStorage.setItem('artevia_cart_count', 0);
  }
}
"""

with open(js_file, 'r', encoding='utf-8') as f:
    if 'updateMockCart' not in f.read():
        with open(js_file, 'a', encoding='utf-8') as f2:
            f2.write(js_logic)
        print("Appended dynamic cart JS")
