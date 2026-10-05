import json

with open('search-index.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Filter out the presentations page
new_data = [item for item in data if item.get('url') != '/publications/presentations/']

with open('search-index.json', 'w', encoding='utf-8') as f:
    json.dump(new_data, f, separators=(',', ':'))
