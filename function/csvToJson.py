from createCsv import df
import json
import pandas as pd

menus = ["Aset", "Bset", "curry", "dailySpecialUdonSoba", "UdonSoba", "dailySpecialRamenPasta", "ramenPasta"]
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

with open("../data/lunch.json", "r") as f:
    lunch = json.load(f)

col: int = 2
row: int = 3
#日替わりうどん・そばまでのデータを取得
for i in range(4):
    col = 2
    for j in week:
        if pd.isna(df.iloc[row][col]):
            (lunch[menus[i]][j]) = "None"
            col += 5
        else:
            (lunch[menus[i]][j]) = df.iloc[row][col]
            col += 5
    row += 3

row = 16
for i in range(2):
    col = 2
    for j in week:
        if pd.isna(df.iloc[row][col]):
            (lunch[menus[i+4]][j]) = "None"
            col += 5
        else:
            (lunch[menus[i+4]][j]) = df.iloc[row][col]
            col += 5
    row += 4

col = 2
row = 23
for i in week:
    if pd.isna(df.iloc[row][col]):
        (lunch["ramenPasta"][i]) = "None"
    else:
        (lunch["ramenPasta"][i]) = df.iloc[row][col]
    col += 5

with open("../data/lunch.json", "w") as f:
    json.dump(lunch, f,indent = 4 , ensure_ascii=False)