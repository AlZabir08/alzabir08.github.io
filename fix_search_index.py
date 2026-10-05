import json

with open('search-index.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Filter out the page 2 entry itself
data = [item for item in data if item.get('url') != '/publications/page-2/']

# Update the URLs for the publications that were moved
for item in data:
    if item.get('url', '').startswith('/publications/page-2/#'):
        item['url'] = item['url'].replace('/publications/page-2/#', '/publications/#')

with open('search-index.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, separators=(',', ':'))

