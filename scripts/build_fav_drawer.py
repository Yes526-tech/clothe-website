import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import os

views_dir = os.path.join(BASE_DIR, 'views')
js_file = os.path.join(BASE_DIR, 'public/assets/js/script.js')
css_file = os.path.join(BASE_DIR, 'public/assets/css/style.css')

files_to_update = [
    'index_view.html',
    'collections_view.html',
    'men_view.html',
    'women_view.html',
    'medieval_view.html',
    'graffiti_view.html',
    'sweatshirt_view.html'
]

# 1. Update HTML files
fav_drawer_html = """
  <!-- FAVORITES DRAWER -->
  <div class="fav-drawer-overlay" id="favDrawerOverlay" onclick="closeFavDrawer()"></div>
  <div class="fav-drawer" id="favDrawer">
    <div class="cart-drawer-header">
      <h2 class="cart-drawer-title">FAVORİLER</h2>
      <button class="cart-drawer-close" onclick="closeFavDrawer()">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
      </button>
    </div>
    
    <div class="fav-drawer-items">
      <!-- Dynamic Items -->
    </div>
  </div>
"""

for filename in files_to_update:
    filepath = os.path.join(views_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update NAVBAR link
        content = content.replace(
            '<a href="#" style="color: #c6a87c;">FAVORİLER</a>',
            '<a href="#" style="color: #c6a87c;" onclick="event.preventDefault(); openFavDrawer()">FAVORİLER</a>'
        )
        
        # Update heart button onclick
        content = content.replace(
            'onclick="event.preventDefault(); this.classList.toggle(\'active-fav\');"',
            'onclick="event.preventDefault(); toggleFavorite(this);"'
        )
        
        # Inject Drawer HTML
        if 'id="favDrawer"' not in content:
            content = content.replace('</body>', fav_drawer_html + '\n</body>')
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated HTML: {filename}")

# 2. Append CSS
fav_css = """
/* FAVORITES DRAWER */
.fav-drawer-overlay {
  position: fixed; top: 0; left: 0; width: 100%; height: 100%;
  background: rgba(0, 0, 0, 0.5); backdrop-filter: blur(4px);
  z-index: 10000; opacity: 0; visibility: hidden; transition: all 0.4s ease;
}
.fav-drawer-overlay.active { opacity: 1; visibility: visible; }
.fav-drawer {
  position: fixed; top: 0; right: 0; width: 400px; height: 100%;
  background-color: #1a3a2a; border-left: 1px solid #c6a87c;
  z-index: 10001; transform: translateX(100%);
  transition: transform 0.5s cubic-bezier(0.165, 0.84, 0.44, 1);
  display: flex; flex-direction: column;
}
.fav-drawer.active { transform: translateX(0); }
.fav-drawer-items {
  flex: 1; overflow-y: auto; padding: 30px;
}
@media (max-width: 768px) { .fav-drawer { width: 100%; } }
"""
with open(css_file, 'r', encoding='utf-8') as f:
    if 'fav-drawer-overlay' not in f.read():
        with open(css_file, 'a', encoding='utf-8') as f2:
            f2.write(fav_css)
        print("Appended Fav CSS")

# 3. Append JS
fav_js = """
// ─── FAVORITES LOGIC ───────────────────────────────────────────────────────────
let arteviaFavs = JSON.parse(localStorage.getItem('artevia_fav_data')) || [];

function saveFavs() {
  localStorage.setItem('artevia_fav_data', JSON.stringify(arteviaFavs));
  syncFavDrawer();
}

function syncFavDrawer() {
  const container = document.querySelector('.fav-drawer-items');
  if (!container) return;

  container.innerHTML = '';
  
  if (arteviaFavs.length === 0) {
    container.innerHTML = '<div style="color:rgba(255,255,255,0.5); text-align:center; margin-top:50px; font-family:\\'Outfit\\', sans-serif; letter-spacing:0.1em;">FAVORİ LİSTENİZ BOŞ.</div>';
  } else {
    arteviaFavs.forEach((item, index) => {
      const itemHTML = `
        <div class="cart-drawer-item">
          <img src="${item.image}" alt="${item.title}" class="cart-item-img" />
          <div class="cart-item-details">
            <div class="cart-item-title">${item.title}</div>
            <div class="cart-item-price">₺${item.price}</div>
            <div style="display:flex; align-items:center; gap:15px; margin-top:auto;">
              <button onclick="removeFavItem(${index})" style="background:none; border:none; color:rgba(255,255,255,0.5); font-family:'Outfit', sans-serif; font-size:11px; text-decoration:underline; cursor:pointer;">Kaldır</button>
            </div>
          </div>
        </div>
      `;
      container.innerHTML += itemHTML;
    });
  }
  
  // Sync heart icons on current page
  document.querySelectorAll('a.cp-card').forEach(card => {
     const titleEl = card.querySelector('.cp-card-title');
     const favBtn = card.querySelector('.cp-fav-btn');
     if(titleEl && favBtn) {
       const title = titleEl.innerText.trim();
       const isFav = arteviaFavs.find(i => i.title === title);
       if(isFav) favBtn.classList.add('active-fav');
       else favBtn.classList.remove('active-fav');
     }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  syncFavDrawer();
});

function toggleFavorite(btn) {
  if (btn) {
    const card = btn.closest('a.cp-card');
    if (card) {
      const titleEl = card.querySelector('.cp-card-title');
      const priceEl = card.querySelector('.cp-card-price');
      const imgEl = card.querySelector('.cp-card-img');
      
      if (titleEl && priceEl && imgEl) {
        const title = titleEl.innerText.trim();
        const priceStr = priceEl.innerText.replace(/[^0-9]/g, '');
        const price = parseInt(priceStr) || 0;
        const image = imgEl.getAttribute('src');
        
        const existingIndex = arteviaFavs.findIndex(i => i.title === title);
        if (existingIndex > -1) {
          arteviaFavs.splice(existingIndex, 1);
          btn.classList.remove('active-fav');
        } else {
          arteviaFavs.push({ title, price, image });
          btn.classList.add('active-fav');
        }
        
        saveFavs();
      }
    }
  }
}

function removeFavItem(index) {
  arteviaFavs.splice(index, 1);
  saveFavs();
}

function openFavDrawer() {
  const overlay = document.getElementById('favDrawerOverlay');
  const drawer = document.getElementById('favDrawer');
  if(overlay && drawer) {
    overlay.classList.add('active');
    drawer.classList.add('active');
  }
}

function closeFavDrawer() {
  const overlay = document.getElementById('favDrawerOverlay');
  const drawer = document.getElementById('favDrawer');
  if(overlay && drawer) {
    overlay.classList.remove('active');
    drawer.classList.remove('active');
  }
}
"""

with open(js_file, 'r', encoding='utf-8') as f:
    if 'openFavDrawer' not in f.read():
        with open(js_file, 'a', encoding='utf-8') as f2:
            f2.write(fav_js)
        print("Appended Fav JS")
