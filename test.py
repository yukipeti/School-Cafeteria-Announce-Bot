import tabula
import pandas as pd

# PDFファイルから表を抽出し、DataFrameとして取得
tables = tabula.read_pdf("./pdf/gakusyoku.pdf", pages="all")

# DataFrameをCSVに書き出す
for i, table in enumerate(tables):
    table.to_csv(f"./output/output_table_{i}.csv", index=False)
