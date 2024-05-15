import pdfplumber
import pandas as pd

# PDFファイルのパス
pdf_path = "../pdf/gakusyoku.pdf" 
# 出力するCSVファイルのパス
csv_path = "../output/output.csv"

# PDFから表を抽出
all_tables = []
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            # テーブルが空でないことを確認
            if table:
                df = pd.DataFrame(table[1:], columns=table[0])
                all_tables.append(df)

# 抽出したデータフレームを1つに結合
if all_tables:  # テーブルが一つ以上存在するか確認
    combined_df = pd.concat(all_tables, ignore_index=True)
    # データフレームをCSVに書き出し（エンコーディングを指定）
    combined_df.to_csv(csv_path, index=False, encoding="utf-8")
    print(f"{csv_path}に書き出しました")
else:
    print("PDFからテーブルが抽出できませんでした")

# CSVファイルを読み込む
df = pd.read_csv(csv_path, encoding="utf-8")

# 指定したセルの値を取得
index_row = int(input("行: "))
index_col = int(input("列: "))
cell_value = df.iloc[index_row, index_col]

# セルの値を出力
print(f"指定したセルの値: {cell_value}")
