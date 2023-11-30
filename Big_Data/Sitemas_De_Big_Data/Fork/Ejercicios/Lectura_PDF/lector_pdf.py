import tabula as tb
import os

data_dir = os.path.dirname(os.path.abspath(__file__)) + "/"

df = tb.read_pdf(data_dir+"Tablas.pdf")

print(df)