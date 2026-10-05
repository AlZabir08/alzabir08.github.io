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
    
    # Remove link like: <a href="../publications/presentations/">Presentations</a>
    # or <a href="../../publications/presentations/">Presentations</a>
    # The actual href could just end with /presentations/"
    content = re.sub(r'<a href="[^"]*presentations/"[^>]*>Presentations</a>', '', content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
