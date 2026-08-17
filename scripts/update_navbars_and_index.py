import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import os
import re

css_addition = """
    .w-dropdown {
      position: relative;
      display: inline-block;
    }
    .w-dropdown-content {
      display: none;
      position: absolute;
      background-color: #1a3a2a;
      min-width: 180px;
      box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.5);
      z-index: 1000;
      top: 100%;
      left: 0;
      padding-top: 15px;
      border: 1px solid rgba(198, 168, 124, 0.2);
      border-top: none;
    }
    .w-dropdown-content a {
      color: #c6a87c !important;
      padding: 12px 20px !important;
      text-decoration: none;
      display: block;
      font-size: 11px !important;
      letter-spacing: 0.14em !important;
    }
    .w-dropdown-content a::after {
      display: none !important;
    }
    .w-dropdown-content a:hover {
      background-color: rgba(198, 168, 124, 0.1);
      color: #fff !important;
    }
    .w-dropdown:hover .w-dropdown-content {
      display: block;
    }
"""

old_nav = """    <ul class="w-nav-links">
      <li><a href="/">KOLEKSİYONLAR</a></li>
      <li><a href="/men">ERKEK</a></li>
      <li><a href="/women">KADIN</a></li>
    </ul>"""

new_nav = """    <ul class="w-nav-links">
      <li class="w-dropdown">
        <a href="/" class="w-dropbtn">KOLEKSİYONLAR</a>
        <div class="w-dropdown-content">
          <a href="/collection/medieval">MEDIEVAL</a>
          <a href="/collection/graffiti">GRAFFITI</a>
          <a href="/collection/sweatshirt">SWEATSHIRT</a>
        </div>
      </li>
      <li><a href="/men">ERKEK</a></li>
      <li><a href="/women">KADIN</a></li>
    </ul>"""

views_dir = os.path.join(BASE_DIR, 'views')
all_views = [
    'index_view.html',
    'women_view.html',
    'men_view.html',
    'medieval_view.html',
    'graffiti_view.html',
    'sweatshirt_view.html'
]

# 1. Update all navbars and add CSS
for view in all_views:
    path = os.path.join(views_dir, view)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if we already added it
    if '.w-dropdown' not in content:
        # Add CSS before </style>
        content = content.replace('</style>', css_addition + '</style>')
    
    # Replace HTML
    content = content.replace(old_nav, new_nav)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Rewrite index_view.html to be brand centric
with open(os.path.join(views_dir, 'index_view.html'), 'r', encoding='utf-8') as f:
    index_html = f.read()

# We keep everything up to </nav> and replace everything below it up to <!-- FOOTER -->
# Let's extract head + navbar
match_top = re.search(r'<!DOCTYPE html>.*?</nav>', index_html, flags=re.DOTALL)
match_footer = re.search(r'<!-- FOOTER -->.*</html>', index_html, flags=re.DOTALL)

if match_top and match_footer:
    top_html = match_top.group(0)
    footer_html = match_footer.group(0)

    brand_content = """

  <style>
    /* BRAND HOMEPAGE SPECIFIC STYLES */
    .brand-hero {
      position: relative;
      width: 100%;
      height: 80vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background-color: #1a3a2a;
      overflow: hidden;
    }
    .brand-hero img {
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      object-fit: cover;
      opacity: 0.6;
    }
    .brand-hero-content {
      position: relative;
      z-index: 2;
      text-align: center;
      color: #fff;
    }
    .brand-hero-title {
      font-family: 'Cormorant Garamond', serif;
      font-size: 100px;
      font-weight: 300;
      font-style: italic;
      margin: 0;
      color: #c6a87c;
      letter-spacing: 0.05em;
    }
    .brand-hero-subtitle {
      font-family: 'Outfit', sans-serif;
      font-size: 14px;
      letter-spacing: 0.3em;
      margin-top: 20px;
      text-transform: uppercase;
    }
    .brand-story {
      padding: 100px 20px;
      background-color: #f7f7f7;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .brand-story-title {
      font-family: 'Cormorant Garamond', serif;
      font-size: 40px;
      font-style: italic;
      color: #1a3a2a;
      margin-bottom: 30px;
    }
    .brand-story-text {
      font-family: 'Inter', sans-serif;
      font-size: 16px;
      line-height: 1.8;
      max-width: 700px;
      color: #555;
    }
    .brand-banner {
      display: flex;
      width: 100%;
      height: 60vh;
    }
    .brand-banner-half {
      flex: 1;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      text-decoration: none;
    }
    .brand-banner-half img {
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      object-fit: cover;
      transition: transform 0.8s ease;
      filter: brightness(0.7);
    }
    .brand-banner-half:hover img {
      transform: scale(1.05);
      filter: brightness(0.5);
    }
    .brand-banner-text {
      position: relative;
      z-index: 2;
      font-family: 'Outfit', sans-serif;
      font-size: 24px;
      color: #fff;
      letter-spacing: 0.2em;
      border: 1px solid #fff;
      padding: 15px 40px;
      transition: background 0.3s, color 0.3s;
    }
    .brand-banner-half:hover .brand-banner-text {
      background: #fff;
      color: #1a3a2a;
    }
  </style>

  <!-- BRAND HERO -->
  <section class="brand-hero">
    <img src="/assets/images/hero_model.png" alt="Artévia Fashion" />
    <div class="brand-hero-content">
      <h1 class="brand-hero-title">Artévia</h1>
      <div class="brand-hero-subtitle">Fashion That Moves With You</div>
    </div>
  </section>

  <!-- BRAND STORY -->
  <section class="brand-story">
    <h2 class="brand-story-title">The Artévia Vision</h2>
    <p class="brand-story-text">
      Born from a desire to merge avant-garde design with everyday wearability, Artévia represents the pinnacle of modern luxury. We believe clothing is more than just fabric—it is an expression of identity, an armor for the contemporary world. Explore our curated collections that bridge the gap between high-end editorial and accessible street fashion.
    </p>
  </section>

  <!-- CATEGORY BANNER -->
  <section class="brand-banner">
    <a href="/women" class="brand-banner-half">
      <img src="/assets/images/women_category.png" alt="Women" />
      <span class="brand-banner-text">WOMEN</span>
    </a>
    <a href="/men" class="brand-banner-half">
      <img src="/assets/images/men_category.png" alt="Men" />
      <span class="brand-banner-text">MEN</span>
    </a>
  </section>

"""

    final_html = top_html + brand_content + footer_html
    with open(os.path.join(views_dir, 'index_view.html'), 'w', encoding='utf-8') as f:
        f.write(final_html)
