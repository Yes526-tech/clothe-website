import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import os

views_dir = os.path.join(BASE_DIR, 'views')
files_to_update = [
    'men_view.html',
    'women_view.html',
    'medieval_view.html',
    'graffiti_view.html',
    'sweatshirt_view.html'
]

for filename in files_to_update:
    filepath = os.path.join(views_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Inject script before </body> if not present
        if 'script.js' not in content:
            content = content.replace('</body>', '  <script src="/assets/js/script.js"></script>\n</body>')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added script.js to {filename}")
