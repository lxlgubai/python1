import json


def ind():
    with open('ind5.json', mode='r', encoding='utf-8') as f:
        f1 = json.load(f)
        kd = json.dumps(f1,ensure_ascii=False)
        return kd

print(ind())