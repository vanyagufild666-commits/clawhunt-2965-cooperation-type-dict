"""Generate JSON deliverable for task 2965 (合作方式, xlsx + JSON)."""
import json

content = json.load(open('content.json', encoding='utf-8'))
sheet = content['sheets'][0]

rows = []
for r in sheet['rows']:
    item = dict(zip(sheet['headers'], r))
    rows.append(item)

with open('合作方式字典.json', 'w', encoding='utf-8') as f:
    json.dump(rows, f, ensure_ascii=False, indent=1)

codes = [i['编码'] for i in rows]
assert len(codes) == len(set(codes)), 'duplicate codes'
over40 = [i['编码'] for i in rows if len(i['定义']) > 40]
print('json written |', len(rows), 'items | codes unique | defs over 40 chars:', over40 or 'none')
