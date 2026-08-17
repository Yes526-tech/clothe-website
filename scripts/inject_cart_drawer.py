import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import os

views_dir = os.path.join(BASE_DIR, 'views')
css_file = os.path.join(BASE_DIR, 'public/assets/css/style.css')
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

drawer_html = """
  <!-- CART DRAWER -->
  <div class="cart-drawer-overlay" id="cartDrawerOverlay" onclick="closeCartDrawer()"></div>
  <div class="cart-drawer" id="cartDrawer">
    <div class="cart-drawer-header">
      <h2 class="cart-drawer-title">SEPETİNİZ</h2>
      <button class="cart-drawer-close" onclick="closeCartDrawer()">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
      </button>
    </div>
    
    <div class="cart-drawer-items">
      <!-- MOCK ITEM -->
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
      </div>
    </div>

    <div class="cart-drawer-footer">
      <div class="cart-drawer-total">
        <span>ARA TOPLAM</span>
        <span>₺2500</span>
      </div>
      <button class="cart-drawer-checkout-btn">ÖDEME YAP</button>
    </div>
  </div>
"""

for filename in files_to_update:
    filepath = os.path.join(views_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace Proceed to Checkout link with open drawer button
        content = content.replace(
            '<a href="#" class="cart-modal-btn btn-solid">Ödemeye Geç</a>',
            '<button class="cart-modal-btn btn-solid" onclick="closeCartModal(); openCartDrawer();">Ödemeye Geç</button>'
        )
        
        # Add onclick to top navbar cart btn
        content = content.replace(
            '<button class="w-cart-btn" id="open-cart-btn" style="color: #c6a87c;">SEPET (<span id="w-cart-count">0</span>)</button>',
            '<button class="w-cart-btn" id="open-cart-btn" style="color: #c6a87c;" onclick="openCartDrawer()">SEPET (<span id="w-cart-count">0</span>)</button>'
        )
        # Handle index_view.html which has a slightly different top cart btn possibly
        content = content.replace(
            '<button class="w-cart-btn" id="open-cart-btn">SEPET (<span id="w-cart-count">0</span>)</button>',
            '<button class="w-cart-btn" id="open-cart-btn" onclick="openCartDrawer()">SEPET (<span id="w-cart-count">0</span>)</button>'
        )
        
        # Inject drawer before </body>
        if 'id="cartDrawer"' not in content:
            content = content.replace('</body>', drawer_html + '\n</body>')
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated HTML: {filename}")

# APPEND CSS
drawer_css = """
/* CART DRAWER */
.cart-drawer-overlay {
  position: fixed;
  top: 0; left: 0; width: 100%; height: 100%;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
  z-index: 10000;
  opacity: 0;
  visibility: hidden;
  transition: all 0.4s ease;
}
.cart-drawer-overlay.active {
  opacity: 1;
  visibility: visible;
}
.cart-drawer {
  position: fixed;
  top: 0; right: 0; width: 400px; height: 100%;
  background-color: #1a3a2a;
  border-left: 1px solid #c6a87c;
  z-index: 10001;
  transform: translateX(100%);
  transition: transform 0.5s cubic-bezier(0.165, 0.84, 0.44, 1);
  display: flex;
  flex-direction: column;
}
.cart-drawer.active {
  transform: translateX(0);
}
.cart-drawer-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 30px;
  border-bottom: 1px solid rgba(198, 168, 124, 0.2);
}
.cart-drawer-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: 24px;
  color: #c6a87c;
  margin: 0;
  font-style: italic;
}
.cart-drawer-close {
  background: none; border: none; color: #c6a87c; cursor: pointer; padding: 0;
}
.cart-drawer-close svg { width: 24px; height: 24px; }
.cart-drawer-items {
  flex: 1; overflow-y: auto; padding: 30px;
}
.cart-drawer-item {
  display: flex; gap: 20px; margin-bottom: 30px;
}
.cart-item-img {
  width: 100px; height: 120px; object-fit: cover; border: 1px solid rgba(198, 168, 124, 0.2);
}
.cart-item-details {
  display: flex; flex-direction: column; justify-content: space-between;
}
.cart-item-title {
  font-family: 'Outfit', sans-serif; color: #fff; font-size: 14px; text-transform: uppercase; letter-spacing: 0.1em;
}
.cart-item-variant {
  font-family: 'Outfit', sans-serif; color: rgba(255,255,255,0.6); font-size: 11px;
}
.cart-item-price {
  font-family: 'Outfit', sans-serif; color: #c6a87c; font-size: 14px; font-weight: 500;
}
.cart-item-qty {
  display: flex; align-items: center; gap: 15px; border: 1px solid rgba(198, 168, 124, 0.5); padding: 5px 10px; width: fit-content; color: #fff; font-family: 'Outfit', sans-serif; font-size: 12px;
}
.qty-btn {
  background: none; border: none; color: #fff; cursor: pointer; padding: 0;
}
.cart-drawer-footer {
  padding: 30px; border-top: 1px solid rgba(198, 168, 124, 0.2);
}
.cart-drawer-total {
  display: flex; justify-content: space-between; color: #fff; font-family: 'Outfit', sans-serif; font-size: 14px; letter-spacing: 0.1em; margin-bottom: 20px;
}
.cart-drawer-checkout-btn {
  width: 100%; background: #c6a87c; color: #1a3a2a; border: none; padding: 15px; font-family: 'Outfit', sans-serif; font-size: 12px; font-weight: 600; letter-spacing: 0.2em; text-transform: uppercase; cursor: pointer; transition: background 0.3s ease;
}
.cart-drawer-checkout-btn:hover { background: #b59565; }
@media (max-width: 768px) { .cart-drawer { width: 100%; } }
"""
with open(css_file, 'r', encoding='utf-8') as f:
    if 'cart-drawer-overlay' not in f.read():
        with open(css_file, 'a', encoding='utf-8') as f2:
            f2.write(drawer_css)
        print("Appended Drawer CSS")

# APPEND JS
drawer_js = """
// CART DRAWER LOGIC
function openCartDrawer() {
  const overlay = document.getElementById('cartDrawerOverlay');
  const drawer = document.getElementById('cartDrawer');
  if(overlay && drawer) {
    overlay.classList.add('active');
    drawer.classList.add('active');
  }
}
function closeCartDrawer() {
  const overlay = document.getElementById('cartDrawerOverlay');
  const drawer = document.getElementById('cartDrawer');
  if(overlay && drawer) {
    overlay.classList.remove('active');
    drawer.classList.remove('active');
  }
}
"""
with open(js_file, 'r', encoding='utf-8') as f:
    if 'openCartDrawer' not in f.read():
        with open(js_file, 'a', encoding='utf-8') as f2:
            f2.write(drawer_js)
        print("Appended Drawer JS")
