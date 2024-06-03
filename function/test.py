import json

with open("../data/lunch.json", "r", encoding = "utf-8") as f:
    lunch = json.load(f)
    print(lunch["Aset"]["Monday"])