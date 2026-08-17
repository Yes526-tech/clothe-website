import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import os
import re

views_dir = os.path.join(BASE_DIR, 'views')
collections = [
    {
        "file": "medieval_view.html",
        "name": "Medieval",
        "images": ["medival1.jpg", "medival2.jpg", "medival3.jpg", "medival4.jpg"]
    },
    {
        "file": "graffiti_view.html",
        "name": "Graffiti",
        "images": ["grafitti1.jpg", "grafitti2.jpg", "grafitti3.jpg", "grafitti4.jpg"]
    },
    {
        "file": "sweatshirt_view.html",
        "name": "Sweatshirt",
        "images": ["sweattshirt1.jpg", "sweattshirt2.jpg", "sweattshirt3.jpg", "sweattshirt4.jpg"]
    }
]

hero_template = """  <!-- HERO SECTION (4-COLUMN SPLIT) -->
  <section class="collection-section is-visible">
    <div class="collection-bg-grid">
      <div class="grid-img-wrap"><img src="/assets/images/collections/{img1}" alt="{name} 1" /></div>
      <div class="grid-img-wrap"><img src="/assets/images/collections/{img2}" alt="{name} 2" /></div>
      <div class="grid-img-wrap"><img src="/assets/images/collections/{img3}" alt="{name} 3" /></div>
      <div class="grid-img-wrap"><img src="/assets/images/collections/{img4}" alt="{name} 4" /></div>
    </div>
    <div class="collection-content">
      <div class="collection-label">Artévia Exclusive</div>
      <h2 class="collection-title">{name}<br/>Collection</h2>
      <a href="#products" class="collection-btn">KEŞFET</a>
    </div>
  </section>"""

for col in collections:
    filepath = os.path.join(views_dir, col["file"])
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Include CSS if missing
    if 'home-collections.css' not in content:
        content = content.replace('</head>', '  <link rel="stylesheet" href="/assets/css/home-collections.css" />\n</head>')

    # 2. Replace old cp-hero with new 4-column hero
    new_hero = hero_template.format(
        name=col["name"],
        img1=col["images"][0],
        img2=col["images"][1],
        img3=col["images"][2],
        img4=col["images"][3]
    )
    
    # Use regex to replace the old cp-hero block
    content = re.sub(r'<!-- HERO SECTION -->\s*<section class="cp-hero">.*?</section>', new_hero, content, flags=re.DOTALL)
    
    # 3. Add id="products" to products section
    content = content.replace('<section class="cp-products-section">', '<section class="cp-products-section" id="products">')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {col['file']}")
