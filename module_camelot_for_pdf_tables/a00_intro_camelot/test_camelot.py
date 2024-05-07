import sys
print(sys.executable)

import camelot
print(f"{camelot.__version__=}")

path_pdf = r"C:\Users\a126291\OneDrive - AmerisourceBergen(ABC)\data\pdf_files\pdf_with_data_tables\non_scan_pdf_with_text_and_table_from_camelot.pdf"

tables = camelot.read_pdf(path_pdf)
num_tables = len(tables)
print(f"Found: {num_tables} tables (pandas dataframes.)")

table = tables[0]
print(f"{type(table)=}")

# save all tables (using export, or single table using .to_csv, .to_json, etc)
tables.export('foo.csv', f='csv', compress=True) # json, excel, html, markdown, sqlite (compress creates .zip)
