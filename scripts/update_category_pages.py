import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import os

pages = [
    {
        "file": "men_view.html",
        "title": "Artévia - Men's Collection",
        "hero_img": "/assets/images/hero_model_men.png",
        "hero_title": "Artévia",
        "hero_subtitle": "Creative Clothing",
        "categories": [
            {"name": "Hoodies", "img": "/assets/images/prod_sweatshirt.png"},
            {"name": "Tracksuits", "img": "/assets/images/cat_outerwear_men.png"},
            {"name": "Tees", "img": "/assets/images/prod_tshirt.png"},
            {"name": "Accessories", "img": "/assets/images/prod_hat.png"},
            {"name": "Jackets", "img": "/assets/images/cat_knitwear_men.png"},
            {"name": "Extras", "img": "/assets/images/cat_shirts_men.png"}
        ]
    },
    {
        "file": "women_view.html",
        "title": "Artévia - Women's Collection",
        "hero_img": "/assets/images/hero_model.png",
        "hero_title": "Artévia",
        "hero_subtitle": "Creative Clothing",
        "categories": [
            {"name": "Hoodies", "img": "/assets/images/prod_sweatshirt.png"},
            {"name": "Dresses", "img": "/assets/images/cat_dresses.png"},
            {"name": "Tees", "img": "/assets/images/prod_tshirt.png"},
            {"name": "Accessories", "img": "/assets/images/prod_bag.png"},
            {"name": "Jackets", "img": "/assets/images/cat_outerwear.png"},
            {"name": "Extras", "img": "/assets/images/cat_knitwear.png"}
        ]
    }
]

template = """<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{title}</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=Inter:wght@300;400;500;600&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
  
  <link rel="stylesheet" href="/assets/css/style.css" />
  <link rel="stylesheet" href="/assets/css/collection-page.css" />
  
  <style>
    .w-dropdown {{ position: relative; display: inline-block; }}
    .w-dropdown-content {{
      display: none; position: absolute; background-color: #1a3a2a; min-width: 180px;
      box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.5); z-index: 1000; top: 100%; left: 0;
      padding-top: 15px; border: 1px solid rgba(198, 168, 124, 0.2); border-top: none;
    }}
    .w-dropdown-content a {{
      color: #c6a87c !important; padding: 12px 20px !important; text-decoration: none;
      display: block; font-size: 11px !important; letter-spacing: 0.14em !important;
    }}
    .w-dropdown-content a::after {{ display: none !important; }}
    .w-dropdown-content a:hover {{ background-color: rgba(198, 168, 124, 0.1); color: #fff !important; }}
    .w-dropdown:hover .w-dropdown-content {{ display: block; }}

    .cp-hero-subtitle {{
      position: absolute; z-index: 2; color: #fff; font-family: 'Outfit', sans-serif;
      font-size: 14px; letter-spacing: 0.3em; margin-top: 120px; text-transform: uppercase; text-shadow: 1px 1px 5px rgba(0,0,0,0.5);
    }}
  </style>
</head>
<body>

  <!-- NAVBAR -->
  <nav class="w-navbar" style="background-color: #1a3a2a; border-bottom: 1px solid rgba(198,168,124,0.2);">
    <ul class="w-nav-links">
      <li class="w-dropdown">
        <a href="/" class="w-dropbtn" style="color: #c6a87c;">KOLEKSİYONLAR</a>
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
      <li><a href="#" style="color: #c6a87c;">FAVORİLER</a></li>
      <li><button class="w-cart-btn" id="open-cart-btn" style="color: #c6a87c;">SEPET (<span id="w-cart-count">0</span>)</button></li>
    </ul>
  </nav>

  <!-- HERO SECTION -->
  <section class="cp-hero">
    <h1 class="cp-hero-title">{hero_title}</h1>
    <div class="cp-hero-subtitle">{hero_subtitle}</div>
    <img src="{hero_img}" alt="{title} Hero" />
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
    <div class="cp-grid-6">
      <a href="#" class="cp-card">
        <img src="{cat1_img}" alt="{cat1_name}" class="cp-card-img" />
        <div class="cp-card-info">
          <div class="cp-card-title">{cat1_name}</div>
          <div class="cp-card-arrow">&rarr;</div>
        </div>
      </a>
      <a href="#" class="cp-card">
        <img src="{cat2_img}" alt="{cat2_name}" class="cp-card-img" />
        <div class="cp-card-info">
          <div class="cp-card-title">{cat2_name}</div>
          <div class="cp-card-arrow">&rarr;</div>
        </div>
      </a>
      <a href="#" class="cp-card">
        <img src="{cat3_img}" alt="{cat3_name}" class="cp-card-img" />
        <div class="cp-card-info">
          <div class="cp-card-title">{cat3_name}</div>
          <div class="cp-card-arrow">&rarr;</div>
        </div>
      </a>
      <a href="#" class="cp-card">
        <img src="{cat4_img}" alt="{cat4_name}" class="cp-card-img" />
        <div class="cp-card-info">
          <div class="cp-card-title">{cat4_name}</div>
          <div class="cp-card-arrow">&rarr;</div>
        </div>
      </a>
      <a href="#" class="cp-card">
        <img src="{cat5_img}" alt="{cat5_name}" class="cp-card-img" />
        <div class="cp-card-info">
          <div class="cp-card-title">{cat5_name}</div>
          <div class="cp-card-arrow">&rarr;</div>
        </div>
      </a>
      <a href="#" class="cp-card">
        <img src="{cat6_img}" alt="{cat6_name}" class="cp-card-img" />
        <div class="cp-card-info">
          <div class="cp-card-title">{cat6_name}</div>
          <div class="cp-card-arrow">&rarr;</div>
        </div>
      </a>
    </div>
  </section>

</body>
</html>"""

for p in pages:
    filepath = os.path.join(os.path.join(BASE_DIR, 'views'), p["file"])
    content = template.format(
        title=p["title"],
        hero_img=p["hero_img"],
        hero_title=p["hero_title"],
        hero_subtitle=p["hero_subtitle"],
        cat1_name=p["categories"][0]["name"], cat1_img=p["categories"][0]["img"],
        cat2_name=p["categories"][1]["name"], cat2_img=p["categories"][1]["img"],
        cat3_name=p["categories"][2]["name"], cat3_img=p["categories"][2]["img"],
        cat4_name=p["categories"][3]["name"], cat4_img=p["categories"][3]["img"],
        cat5_name=p["categories"][4]["name"], cat5_img=p["categories"][4]["img"],
        cat6_name=p["categories"][5]["name"], cat6_img=p["categories"][5]["img"]
    )
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
