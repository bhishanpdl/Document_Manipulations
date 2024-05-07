import camelot
tables = camelot.read_pdf('foo.pdf')

#tables.export('foo.csv', f='csv', compress=True) # json, excel, html, markdown, sqlite
print(tables[0])
print(tables[0].parsing_report)

#tables[0].to_csv('foo.csv') # to_json, to_excel, to_html, to_markdown, to_sqlite

df = tables[0].df # get a pandas DataFrame!
print(df)
