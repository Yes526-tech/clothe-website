import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import os
import re

views_dir = os.path.join(BASE_DIR, 'views')
css_file = os.path.join(BASE_DIR, 'public/assets/css/collection-page.css')

files_to_update = [
    'men_view.html',
    'women_view.html',
    'medieval_view.html',
    'graffiti_view.html',
    'sweatshirt_view.html'
]

# 1. Update HTML Files
replacement_html = r'''<div class="cp-card-img-wrapper">
          \1
          <div class="cp-card-actions">
            <button class="cp-action-btn cp-fav-btn" onclick="event.preventDefault(); alert('Added to Favorites!');" aria-label="Add to Favorites">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
            </button>
            <button class="cp-action-btn cp-add-btn" onclick="event.preventDefault(); alert('Added to Cart!');" aria-label="Add to Cart">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M9 20a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm7 0a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-9.8-3.4h11.6l2.3-10.4H5.4l-.8-3.7H1v2h2.2l3.4 15.6.8-3.5z"></path></svg>
              ADD TO CART
            </button>
          </div>
        </div>'''

for filename in files_to_update:
    filepath = os.path.join(views_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Only replace if not already wrapped
        if 'cp-card-img-wrapper' not in content:
            # Pattern: <img src="..." alt="..." class="cp-card-img" />
            # Need to capture the exact img tag to preserve src and alt
            pattern = re.compile(r'(<img[^>]+class="cp-card-img"[^>]*>)')
            new_content = pattern.sub(replacement_html, content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated HTML: {filename}")
        else:
            print(f"Already updated: {filename}")

# 2. Append CSS
css_to_append = """
/* QUICK ACTIONS OVERLAY */
.cp-card-img-wrapper {
  position: relative;
  overflow: hidden;
  width: 100%;
}

.cp-card-actions {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 15px;
  display: flex;
  gap: 10px;
  opacity: 0;
  transform: translateY(20px);
  transition: all 0.4s ease;
  z-index: 10;
}

.cp-card:hover .cp-card-actions {
  opacity: 1;
  transform: translateY(0);
}

.cp-action-btn {
  background: rgba(26, 58, 42, 0.9);
  border: 1px solid #c6a87c;
  color: #fff;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  font-family: 'Outfit', sans-serif;
  font-size: 11px;
  letter-spacing: 0.1em;
  transition: all 0.3s;
  backdrop-filter: blur(4px);
}

.cp-action-btn svg {
  width: 16px;
  height: 16px;
}

.cp-action-btn:hover {
  background: #c6a87c;
  color: #1a3a2a;
}

.cp-fav-btn {
  padding: 10px;
  flex-shrink: 0;
}

.cp-add-btn {
  padding: 10px;
  flex-grow: 1;
}
"""

with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

if 'cp-card-img-wrapper' not in css_content:
    with open(css_file, 'a', encoding='utf-8') as f:
        f.write(css_to_append)
    print("Appended CSS to collection-page.css")
else:
    print("CSS already exists.")
