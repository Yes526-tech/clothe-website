import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import os

views = [
    {
        "file": "medieval_view.html",
        "title": "Medieval",
        "hero_img": "/assets/images/collections/medival1.jpg",
        "products": [
            {"name": "Velvet Corset Dress", "price": "₺2500", "img": "/assets/images/collections/medival2.jpg"},
            {"name": "Knight Wool Coat", "price": "₺3200", "img": "/assets/images/collections/medival3.jpg"},
            {"name": "Royal Silk Blouse", "price": "₺1800", "img": "/assets/images/collections/medival4.jpg"},
            {"name": "Gothic Lace Skirt", "price": "₺1500", "img": "/assets/images/collections/medival1.jpg"}
        ]
    },
    {
        "file": "graffiti_view.html",
        "title": "Graffiti",
        "hero_img": "/assets/images/collections/grafitti1.jpg",
        "products": [
            {"name": "Urban Spray Puffer", "price": "₺4200", "img": "/assets/images/collections/grafitti2.jpg"},
            {"name": "Tag Print Hoodie", "price": "₺1800", "img": "/assets/images/collections/grafitti3.jpg"},
            {"name": "Distressed Denim", "price": "₺2100", "img": "/assets/images/collections/grafitti4.jpg"},
            {"name": "Neon Accent Vest", "price": "₺1950", "img": "/assets/images/collections/grafitti1.jpg"}
        ]
    },
    {
        "file": "sweatshirt_view.html",
        "title": "Sweatshirt",
        "hero_img": "/assets/images/collections/sweattshirt1.jpg",
        "products": [
            {"name": "Heavyweight Crew", "price": "₺1200", "img": "/assets/images/collections/sweattshirt2.jpg"},
            {"name": "Essential Zip Hoodie", "price": "₺1500", "img": "/assets/images/collections/sweattshirt3.jpg"},
            {"name": "Lounge Sweatpants", "price": "₺1100", "img": "/assets/images/collections/sweattshirt4.jpg"},
            {"name": "Fleece Lined Pullover", "price": "₺1350", "img": "/assets/images/collections/sweattshirt1.jpg"}
        ]
    }
]

template = """<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Artévia - {title} Collection</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=Inter:wght@300;400;500;600&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
  
  <link rel="stylesheet" href="/assets/css/style.css" />
  <link rel="stylesheet" href="/assets/css/collection-page.css" />
</head>
<body>

  <!-- NAVBAR -->
  <nav class="w-navbar" style="background-color: #1a3a2a; border-bottom: 1px solid rgba(198,168,124,0.2);">
    <ul class="w-nav-links">
      <li class="w-dropdown">
        <a href="/collections" class="w-dropbtn" style="color: #c6a87c;">KOLEKSİYONLAR</a>
        <div class="w-dropdown-content">
          <a href="/collection/medieval">MEDIEVAL</a>
          <a href="/collection/graffiti">GRAFFITI</a>
          <a href="/collection/sweatshirt">SWEATSHIRT</a>
        </div>
      </li>
      <li><a href="/men" style="color: #c6a87c;">ERKEK</a></li>
      <li><a href="/women" style="color: #c6a87c;">KADIN</a></li>
    </ul>
    <a href="/" class="w-logo" style="color: #c6a87c;">Artévia</a>
    <ul class="w-nav-links">
      <li><a href="#" style="color: #c6a87c;">ARAMA</a></li>
      <li><a href="#" style="color: #c6a87c;" onclick="event.preventDefault(); openFavDrawer()">FAVORİLER</a></li>
      <li><button class="w-cart-btn" id="open-cart-btn" style="color: #c6a87c;" onclick="openCartDrawer()">SEPET (<span id="w-cart-count">0</span>)</button></li>
    </ul>
  </nav>

  <!-- HERO SECTION -->
  <section class="cp-hero">
    <img src="{hero_img}" alt="{title} Collection Hero" />
  </section>

  <!-- FEATURES BAR -->
  <section class="cp-features">
    <div class="cp-feature-item">
      <svg viewBox="0 0 24 24" fill="none" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
      <div class="cp-feature-text">
        <span class="cp-feature-title">WORLDWIDE SHIPPING</span>
        <span class="cp-feature-desc">DELIVERING GLOBALLY</span>
      </div>
    </div>
    <div class="cp-feature-item">
      <svg viewBox="0 0 24 24" fill="none" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
      <div class="cp-feature-text">
        <span class="cp-feature-title">LIMITED DROPS</span>
        <span class="cp-feature-desc">EXCLUSIVE RELEASES</span>
      </div>
    </div>
    <div class="cp-feature-item">
      <svg viewBox="0 0 24 24" fill="none" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
      <div class="cp-feature-text">
        <span class="cp-feature-title">PREMIUM QUALITY</span>
        <span class="cp-feature-desc">BUILT TO LAST</span>
      </div>
    </div>
    <div class="cp-feature-item">
      <svg viewBox="0 0 24 24" fill="none" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
      <div class="cp-feature-text">
        <span class="cp-feature-title">SECURE CHECKOUT</span>
        <span class="cp-feature-desc">100% SAFE & SECURE</span>
      </div>
    </div>
  </section>

  <!-- PRODUCTS GRID -->
  <section class="cp-products-section">
    <div class="cp-grid" id="dynamic-products-grid" data-category="collection" data-collection="{collection_id}">
      <!-- Products will be injected here via Javascript -->
    </div>
  </section>

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
      <!-- Items will be injected dynamically -->
    </div>

    <div class="cart-drawer-footer">
      <div class="cart-drawer-total">
        <span>ARA TOPLAM</span>
        <span>₺<span id="mock-total-price">0</span></span>
      </div>
      <button class="cart-drawer-checkout-btn">ÖDEME YAP</button>
    </div>
  </div>

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

  <script src="/assets/js/script.js?v=3.0"></script>
</body>
</html>"""

for v in views:
    filepath = os.path.join(os.path.join(BASE_DIR, 'views'), v["file"])
    content = template.format(
        title=v["title"],
        hero_img=v["hero_img"],
        collection_id=v["file"].split('_')[0]
    )
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
