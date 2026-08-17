import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import os
import re

with open(os.path.join(BASE_DIR, 'views/index_view.html'), 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract from <!-- MAIN NAVIGATION --> down to </nav>
match = re.search(r'<!-- MAIN NAVIGATION -->.*?</nav>', index_html, flags=re.DOTALL)
if match:
    navbar_html = match.group(0)

    for view in ['medieval_view.html', 'graffiti_view.html', 'sweatshirt_view.html']:
        path = os.path.join(os.path.join(BASE_DIR, 'views'), view)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the current navbar in the collection page with navbar_html
        content = re.sub(r'<!-- NAVBAR -->.*?</nav>', navbar_html, content, flags=re.DOTALL)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
