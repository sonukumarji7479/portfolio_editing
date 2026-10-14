import json

data = json.load(open('all_replacements.json'))
for d in data:
    print(f"{d['time']} - {d['file']} - {d['instruction']}")
