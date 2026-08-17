import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
import os
import glob

views_dir = os.path.join(BASE_DIR, 'views')
files = glob.glob(os.path.join(views_dir, '*.html'))

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace js
    content = content.replace('src="assets/js/script.js"', 'src="/assets/js/script.js?v=3.0"')
    content = content.replace('src="/assets/js/script.js"', 'src="/assets/js/script.js?v=3.0"')
    content = content.replace('src="/assets/js/script.js?v=3.0?v=3.0"', 'src="/assets/js/script.js?v=3.0"') # in case of double replace
    
    # Replace css
    content = content.replace('href="/assets/css/style.css"', 'href="/assets/css/style.css?v=3.0"')
    content = content.replace('href="/assets/css/collection-page.css"', 'href="/assets/css/collection-page.css?v=3.0"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Cache-busted: {os.path.basename(filepath)}")
