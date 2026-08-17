import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import os

views_dir = os.path.join(BASE_DIR, 'views')
js_file = os.path.join(BASE_DIR, 'public/assets/js/script.js')

files_to_update = [
    'men_view.html',
    'women_view.html',
    'medieval_view.html',
    'graffiti_view.html',
    'sweatshirt_view.html'
]

# 1. Update HTML buttons
for filename in files_to_update:
    filepath = os.path.join(views_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace(
            'onclick="event.preventDefault(); showCartModal();"',
            'onclick="event.preventDefault(); showCartModal(this);"'
        )
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated HTML: {filename}")

# 2. Rewrite JS logic
with open(js_file, 'r', encoding='utf-8') as f:
    js_content = f.read()

# We need to replace everything from "// ─── FULLY SYNCHRONIZED CART LOGIC" to the end of the file.
start_marker = "// ─── FULLY SYNCHRONIZED CART LOGIC ─────────────────────────────────────────────"
if start_marker in js_content:
    parts = js_content.split(start_marker)
    base_js = parts[0]
else:
    print("Marker not found, something is wrong!")
    base_js = js_content

new_js = """// ─── FULLY SYNCHRONIZED REAL CART LOGIC ──────────────────────────────────────

let arteviaCart = JSON.parse(localStorage.getItem('artevia_cart_data')) || [];

function saveCart() {
  localStorage.setItem('artevia_cart_data', JSON.stringify(arteviaCart));
  syncCartDrawer();
}

function syncCartDrawer() {
  const container = document.querySelector('.cart-drawer-items');
  const countSpan = document.getElementById('w-cart-count');
  const totalSpan = document.getElementById('mock-total-price');
  
  if (!container) return;

  // Clear drawer items
  container.innerHTML = '';
  
  let totalQty = 0;
  let totalPrice = 0;

  if (arteviaCart.length === 0) {
    container.innerHTML = '<div style="color:rgba(255,255,255,0.5); text-align:center; margin-top:50px; font-family:\\'Outfit\\', sans-serif; letter-spacing:0.1em;">SEPETİNİZ BOŞ.</div>';
  } else {
    arteviaCart.forEach((item, index) => {
      totalQty += item.qty;
      totalPrice += item.price * item.qty;
      
      const itemHTML = `
        <div class="cart-drawer-item">
          <img src="${item.image}" alt="${item.title}" class="cart-item-img" />
          <div class="cart-item-details">
            <div class="cart-item-title">${item.title}</div>
            <div class="cart-item-variant">Beden: L | Renk: Standart</div>
            <div class="cart-item-price">₺${item.price}</div>
            <div style="display:flex; align-items:center; gap:15px;">
              <div class="cart-item-qty">
                <button class="qty-btn" onclick="updateCartItem(${index}, -1)">-</button>
                <span>${item.qty}</span>
                <button class="qty-btn" onclick="updateCartItem(${index}, 1)">+</button>
              </div>
              <button onclick="removeCartItem(${index})" style="background:none; border:none; color:rgba(255,255,255,0.5); font-family:'Outfit', sans-serif; font-size:11px; text-decoration:underline; cursor:pointer;">Sil</button>
            </div>
          </div>
        </div>
      `;
      container.innerHTML += itemHTML;
    });
  }

  // Update navbar counter
  if (countSpan) countSpan.innerText = totalQty;
  // Update total price
  if (totalSpan) totalSpan.innerText = totalPrice;
}

// Initial sync on page load
document.addEventListener("DOMContentLoaded", () => {
  syncCartDrawer();
});

function showCartModal(btn) {
  // DOM Traversal to extract product info
  if (btn) {
    const card = btn.closest('a.cp-card');
    if (card) {
      const titleEl = card.querySelector('.cp-card-title');
      const priceEl = card.querySelector('.cp-card-price');
      const imgEl = card.querySelector('.cp-card-img');
      
      if (titleEl && priceEl && imgEl) {
        const title = titleEl.innerText.trim();
        // Extract numbers from price string like "₺2500" or "2.500"
        const priceStr = priceEl.innerText.replace(/[^0-9]/g, '');
        const price = parseInt(priceStr) || 0;
        const image = imgEl.getAttribute('src');
        
        // Check if item already in cart
        const existingItem = arteviaCart.find(i => i.title === title);
        if (existingItem) {
          existingItem.qty += 1;
        } else {
          arteviaCart.push({ title, price, image, qty: 1 });
        }
        
        saveCart();
      }
    }
  }

  // Show modal
  const modal = document.getElementById('cartModal');
  if (modal) modal.classList.add('active');
}

function closeCartModal() {
  const modal = document.getElementById('cartModal');
  if (modal) modal.classList.remove('active');
}

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

function updateCartItem(index, change) {
  if (arteviaCart[index]) {
    arteviaCart[index].qty += change;
    if (arteviaCart[index].qty < 1) {
      removeCartItem(index);
    } else {
      saveCart();
    }
  }
}

function removeCartItem(index) {
  arteviaCart.splice(index, 1);
  saveCart();
}
"""

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(base_js + new_js)
print("Updated script.js with Real Cart Logic")
