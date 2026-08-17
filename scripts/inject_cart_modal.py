import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import os

views_dir = os.path.join(BASE_DIR, 'views')
css_file = os.path.join(BASE_DIR, 'public/assets/css/style.css')
js_file = os.path.join(BASE_DIR, 'public/assets/js/script.js')

files_to_update = [
    'men_view.html',
    'women_view.html',
    'medieval_view.html',
    'graffiti_view.html',
    'sweatshirt_view.html'
]

modal_html = """
  <!-- CUSTOM CART SUCCESS MODAL -->
  <div class="cart-modal-overlay" id="cartModal">
    <div class="cart-modal-box">
      <div class="cart-modal-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
      </div>
      <h3 class="cart-modal-title">Ürün Sepete Eklendi</h3>
      <div class="cart-modal-buttons">
        <button class="cart-modal-btn btn-outline" onclick="closeCartModal()">Alışverişe Devam Et</button>
        <a href="#" class="cart-modal-btn btn-solid">Ödemeye Geç</a>
      </div>
    </div>
  </div>
"""

# 1. Update HTML Files
for filename in files_to_update:
    filepath = os.path.join(views_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace ADD TO CART with SEPETE EKLE
        content = content.replace('ADD TO CART', 'SEPETE EKLE')
        
        # Replace ugly alerts with beautiful ones
        content = content.replace("alert('Added to Cart!');", "showCartModal();")
        content = content.replace("alert('Added to Favorites!');", "this.classList.toggle('active-fav');")
        
        # Inject modal before </body> if not present
        if 'id="cartModal"' not in content:
            content = content.replace('</body>', modal_html + '\n</body>')
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated HTML: {filename}")

# 2. Append CSS
css_to_append = """
/* CART SUCCESS MODAL */
.cart-modal-overlay {
  position: fixed;
  top: 0; left: 0; width: 100%; height: 100%;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  opacity: 0;
  visibility: hidden;
  transition: all 0.4s ease;
}

.cart-modal-overlay.active {
  opacity: 1;
  visibility: visible;
}

.cart-modal-box {
  background-color: #1a3a2a;
  border: 1px solid #c6a87c;
  padding: 40px;
  text-align: center;
  max-width: 400px;
  width: 90%;
  transform: translateY(30px);
  transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.cart-modal-overlay.active .cart-modal-box {
  transform: translateY(0);
}

.cart-modal-icon {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background-color: rgba(198, 168, 124, 0.2);
  color: #c6a87c;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 20px auto;
}
.cart-modal-icon svg {
  width: 30px; height: 30px;
}

.cart-modal-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: 28px;
  color: #c6a87c;
  margin-bottom: 30px;
  font-style: italic;
}

.cart-modal-buttons {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.cart-modal-btn {
  padding: 12px 0;
  font-family: 'Outfit', sans-serif;
  font-size: 12px;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.3s ease;
}

.cart-modal-btn.btn-outline {
  background: transparent;
  border: 1px solid #c6a87c;
  color: #c6a87c;
}
.cart-modal-btn.btn-outline:hover {
  background: rgba(198, 168, 124, 0.1);
}

.cart-modal-btn.btn-solid {
  background: #c6a87c;
  border: 1px solid #c6a87c;
  color: #1a3a2a;
  font-weight: 600;
}
.cart-modal-btn.btn-solid:hover {
  background: #b59565;
}

/* FAV BUTTON TOGGLE */
.cp-fav-btn.active-fav {
  color: #ff4b4b !important;
  border-color: #ff4b4b !important;
}
.cp-fav-btn.active-fav svg {
  fill: #ff4b4b;
}
"""

with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

if 'cart-modal-overlay' not in css_content:
    with open(css_file, 'a', encoding='utf-8') as f:
        f.write(css_to_append)
    print("Appended CSS to style.css")

# 3. Append JS
js_to_append = """
// CART MODAL LOGIC
function showCartModal() {
  const modal = document.getElementById('cartModal');
  if (modal) {
    modal.classList.add('active');
  }
}

function closeCartModal() {
  const modal = document.getElementById('cartModal');
  if (modal) {
    modal.classList.remove('active');
  }
}
"""

with open(js_file, 'r', encoding='utf-8') as f:
    js_content = f.read()

if 'showCartModal' not in js_content:
    with open(js_file, 'a', encoding='utf-8') as f:
        f.write(js_to_append)
    print("Appended JS to script.js")
