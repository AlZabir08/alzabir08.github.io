import os
import re

pub_dir = 'publications'
html_files = []
for root, dirs, files in os.walk(pub_dir):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove div class="publication-supporting-link" that contains "presentation certificate"
    content = re.sub(r'<div class="publication-supporting-link"><a class="text-link"[^>]*>View presentation certificate.*?</a></div>', '', content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
