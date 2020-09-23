import json

x = [1, 'simple', 'list']

with open('dummyFile4', 'w') as f:
    json.dump(x, f)

with open('dummyFile4', 'r') as g:
    y = json.load(g)

print(y)