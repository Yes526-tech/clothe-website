import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import os
import re

filepath = os.path.join(BASE_DIR, 'views/index_view.html')
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Make hero full screen
content = content.replace('height: 80vh;', 'height: calc(100vh - 81px);')

# Remove scroll section
content = re.sub(r'<!-- SCROLL VIDEO SECTION -->.*?</section>', '', content, flags=re.DOTALL)

# Remove brand story
content = re.sub(r'<!-- BRAND STORY -->.*?</section>', '', content, flags=re.DOTALL)

# Remove category banner
content = re.sub(r'<!-- CATEGORY BANNER -->.*?</section>', '', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
