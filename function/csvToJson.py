from createCsv import df
import string
import json
import pandas as pd

menus = ["Aset", "Bset", "curry", "dailySpecialUdonSoba", "UdonSoba", "dailySpecialRamenPasta", "ramenPasta"]
idenMenus = ["Aセット", "Bセット", "カレー", "日替り", "かけ", "日替り", "ラーメン"]
week = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekIndex = []
menusIndex = []

with open("../data/lunch.json", "r") as f:
    lunch = json.load(f)

col: int = 2
row: int = 2

#曜日からインデックスを取得
for i in week:
    while True:
        data: string = df.iloc[row][col]
        if pd.isna(data):
            data = "None"
        
        if i in data:
            weekIndex.append(col)
            break
        else:
            col += 1

col = 0
row = 0
#メニューの行のインデックスを取得
for i in idenMenus:
    while True:
        data: string = df.iloc[row][col]
        if pd.isna(data):
            data = "None"

        if i in data:
            menusIndex.append(row)
            row += 2
            break
        else:
            row += 1

for i in range(len(menus)):
    for j in range(len(week)): 
        if pd.isna(df.iloc[menusIndex[i]][weekIndex[j]]):
            (lunch[menus[i]][week[j]]) = "None"
        else:
            (lunch[menus[i]][week[j]]) = df.iloc[menusIndex[i]][weekIndex[j]]
        
        
with open("../data/lunch.json", "w") as f:
    json.dump(lunch, f,indent = 4 , ensure_ascii=False)

"""
#日替わりうどん・そばまでのデータを取得
for i in range(4):
    for j in range(len(week)): 
        if pd.isna(df.iloc[row][weekIndex[j]]):
            (lunch[menus[i]][week[j]]) = "None"
        else:
            (lunch[menus[i]][week[j]]) = df.iloc[row][weekIndex[j]]
    row += 3

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
"""