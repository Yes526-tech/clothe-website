import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import os
import re

index_path = os.path.join(BASE_DIR, 'views/index_view.html')
style_path = os.path.join(BASE_DIR, 'public/assets/css/style.css')

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the CSS block
match = re.search(r'/\* WOMEN PREMIUM NAVBAR STYLES FOR MAIN PAGE \*/.*?(?=</style>)', content, flags=re.DOTALL)
if match:
    navbar_css = match.group(0)
    
    # Check if it's already in style.css
    with open(style_path, 'r', encoding='utf-8') as f:
        style_content = f.read()
    
    if '.w-navbar' not in style_content:
        # Append to style.css
        with open(style_path, 'a', encoding='utf-8') as f:
            f.write('\n' + navbar_css + '\n')
            print("Successfully appended navbar CSS to style.css")
else:
    print("Could not find navbar CSS block.")
