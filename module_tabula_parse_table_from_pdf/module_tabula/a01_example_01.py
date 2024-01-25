import tabula

# test
print(tabula.environment_info())

# Read remote pdf into list of DataFrame
path_pdf = "https://github.com/chezou/tabula-py/raw/master/tests/resources/data.pdf"

dfs = tabula.read_pdf(path_pdf, stream=True)

print(dfs[0].head(2))

# convert PDF into CSV file
tabula.convert_into(path_pdf, "output.csv", output_format="csv", pages='all')

# convert all PDFs in a directory
#tabula.convert_into_by_batch("input_directory", output_format='csv', pages='all')