import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import os
import re

filepath = os.path.join(BASE_DIR, 'views/index_view.html')
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add script to head
if 'video-scroll.js' not in content:
    content = content.replace('</head>', '  <script src="/assets/js/video-scroll.js" defer></script>\n</head>')

# 2. Add styles
css = """
    /* SCROLL VIDEO STYLES */
    .brand-hero video {
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      object-fit: cover;
      opacity: 0.6;
    }
    .scroll-video-section {
        height: 400vh; /* scrollable distance */
        position: relative;
        background-color: #1a3a2a;
    }
    .scroll-video-sticky {
        position: sticky;
        top: 0;
        height: 100vh;
        width: 100%;
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .scroll-video-sticky video {
        width: 100%;
        height: 100%;
        object-fit: cover;
        opacity: 0.7;
    }
    .scroll-video-overlay {
        position: absolute;
        z-index: 2;
        text-align: center;
        color: #fff;
        pointer-events: none;
    }
    .scroll-video-overlay h2 {
        font-family: 'Cormorant Garamond', serif;
        font-size: 80px;
        font-style: italic;
        color: #c6a87c;
        margin: 0;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.5);
    }
    .scroll-video-overlay p {
        font-family: 'Outfit', sans-serif;
        font-size: 14px;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        text-shadow: 1px 1px 5px rgba(0,0,0,0.5);
    }
"""
if '.scroll-video-section' not in content:
    content = content.replace('</style>', css + '</style>')

# 3. Update Hero
hero_old = '<img src="/assets/images/hero_model.png" alt="Artévia Fashion" />'
hero_new = '<video src="/assets/videos/Cinematic_K_video_seconds.mp4" autoplay loop muted playsinline></video>'
content = content.replace(hero_old, hero_new)

# 4. Add scroll video section after Brand Hero
scroll_section = """
  <!-- SCROLL VIDEO SECTION -->
  <section class="scroll-video-section">
    <div class="scroll-video-sticky">
      <video src="/assets/videos/Create_D_model_advertising_vi.mp4" id="scrollVideo" muted playsinline></video>
      <div class="scroll-video-overlay">
        <h2>Experience Luxury</h2>
        <p>Scroll to Explore</p>
      </div>
    </div>
  </section>
"""

if 'class="scroll-video-section"' not in content:
    # Insert after closing </section> of brand-hero
    content = re.sub(r'(</section>\s*)(?=<!-- BRAND STORY -->)', r'\1' + scroll_section + '\n', content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
