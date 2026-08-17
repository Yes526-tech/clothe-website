import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import os

views_dir = os.path.join(BASE_DIR, 'views')
files_to_update = [
    'index_view.html',
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
        
        # Replace the specific KOLEKSİYONLAR link
        # It might have style attribute or not
        content = content.replace('<a href="/" class="w-dropbtn">KOLEKSİYONLAR</a>', '<a href="/collections" class="w-dropbtn">KOLEKSİYONLAR</a>')
        content = content.replace('<a href="/" class="w-dropbtn" style="color: #c6a87c;">KOLEKSİYONLAR</a>', '<a href="/collections" class="w-dropbtn" style="color: #c6a87c;">KOLEKSİYONLAR</a>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
