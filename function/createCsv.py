import pdfplumber
import pandas as pd

pdf_path = "../data/gakusyoku3.pdf" 
csv_path = "../data/output.csv"

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

combined_df = pd.concat(all_tables, ignore_index = True)
combined_df.to_csv(csv_path, index = False, encoding = "utf-8")
print(f"{csv_path}に書き出しました")

# CSVファイルを読み込む
df = pd.read_csv(csv_path, encoding="utf-8", header=None)