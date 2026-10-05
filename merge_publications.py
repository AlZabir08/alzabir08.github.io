import re
import os
import shutil

with open('publications/page-2/index.html', 'r', encoding='utf-8') as f:
    page2_content = f.read()

# Extract all articles
articles = re.findall(r'<article class="project-row publication-row".*?</article>', page2_content, flags=re.DOTALL)

# Fix paths
articles_fixed = [a.replace('../../', '../') for a in articles]

with open('publications/index.html', 'r', encoding='utf-8') as f:
    page1_content = f.read()

# Find the end of publication-list
# It's <div class="project-list publication-list"> ... </article></div>
# Let's just replace '</div><nav class="pagination"' with the new articles + '</div>'
# Or just find the last </article> before pagination

# We can insert them before the closing </div> of publication-list
# The easiest way is to find the pagination block and replace it, but we need to insert the articles INSIDE the list.
# Let's find the pagination block:
pagination_pattern = r'</div><nav class="pagination".*?</nav>'
match = re.search(pagination_pattern, page1_content, flags=re.DOTALL)
if match:
    # Insert articles before the closing </div>
    joined_articles = "".join(articles_fixed)
    new_content = page1_content[:match.start()] + joined_articles + '</div>' + page1_content[match.end():]
else:
    # try another way
    pass

with open('publications/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

# Remove page-2 directory
shutil.rmtree('publications/page-2')

