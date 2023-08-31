import json

with open('ss1.json', encoding='utf-8') as f:
    dd = f.read()

sss = json.loads(dd)
print(sss)
