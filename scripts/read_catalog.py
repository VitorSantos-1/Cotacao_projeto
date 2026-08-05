import json
import re

with open('index copy.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'(<script id="catalogo-data" type="application/json">\s*)(.*?)(\s*</script>)', content, re.DOTALL)
if match:
    prefix = match.group(1)
    data_str = match.group(2)
    suffix = match.group(3)
    
    data = json.loads(data_str)
    print(f'Total items: {len(data)}')
    print(json.dumps(data[:2], indent=2, ensure_ascii=False))
else:
    print("Not found")
