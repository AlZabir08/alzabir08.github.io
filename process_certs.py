import re

with open('certificates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the resource-links div
content = re.sub(r'<div class="resource-links">.*?</div>', '', content)

# Title-case the h2 tags inside article
def title_case_match(match):
    text = match.group(1)
    # capitalize every word
    new_text = " ".join([word.capitalize() for word in text.split()])
    return f'<h2>{new_text}</h2>'

# The h2 tags are only for certificates in this grid? 
# Wait, let's only target h2 tags that are inside article tags or just all h2 inside the main block.
# Actually, the only other h2 in the page might be the search dialog "Search the portfolio" which we should NOT title case.
# Let's target `<p class="eyebrow">.*?</p><h2>(.*?)</h2>`
def replace_h2(match):
    eyebrow = match.group(1)
    h2_text = match.group(2)
    new_h2 = " ".join([w.capitalize() for w in h2_text.split()])
    return f'{eyebrow}<h2>{new_h2}</h2>'

content = re.sub(r'(<p class="eyebrow">.*?</p>)<h2>(.*?)</h2>', replace_h2, content)

with open('certificates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
