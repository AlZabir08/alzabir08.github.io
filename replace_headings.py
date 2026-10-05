import re

pages = {
    'education/index.html': ('Education.jpeg', 'Education'),
    'projects/index.html': ('Projects.jpeg', 'Projects'),
    'research/index.html': ('Research.jpeg', 'Research'),
    'publications/index.html': ('Publications.jpeg', 'Publications'),
    'certificates/index.html': ('Certificates.jpeg', 'Certificates'),
    'skills/index.html': ('Skills.jpeg', 'Skills'),
    'experience/index.html': ('Experience.jpeg', 'Experience'),
    'achievements/index.html': ('Achievements.jpeg', 'Achievements')
}

for filepath, (img, title) in pages.items():
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # regex to match the <header class="page-heading">...</header> completely
        # Note: it might contain an eyebrow <p> and an <h1>
        replacement = f'<header class="page-banner" style="background-image: url(\'../assets/banners/{img}\');"><h1>{title}</h1></header>'
        
        # Replace the header
        new_content = re.sub(r'<header class="page-heading">.*?</header>', replacement, content, flags=re.DOTALL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Updated {filepath}")
    except Exception as e:
        print(f"Error on {filepath}: {e}")
