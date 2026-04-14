import json

with open('Week3/results.json') as file:
    data = json.load(file)
print(type(data))
