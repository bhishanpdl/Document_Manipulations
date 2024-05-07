# tabula
```python
%%writefile test_tabula.py
import sys
print(sys.executable)

import tabula
print(f"{tabula.__version__=}")

print('\nMake sure JAVA is installed and JAVA_HOME is set to use the module tabula.')
import os
print(os.getenv('JAVA_HOME'))
print()

path_pdf = r"C:\Users\a126291\OneDrive - AmerisourceBergen(ABC)\data\pdf_files\pdf_with_data_tables\non_scan_pdf_with_text_and_table_from_camelot.pdf"

tables = tabula.read_pdf(path_pdf, pages="all", stream=True, silent=True)
num_tables = len(tables)
print(f"Found: {num_tables} tables (tabula gives pandas dataframes)")

table = tables[0]
print(f"{type(table)=}")
print(table.head())
```
