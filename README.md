# PDF_Manipulations

- https://github.com/madmaze/pytesseract/tree/master

# Download Tesseract Binary
- https://github.com/UB-Mannheim/tesseract/wiki

# Download Poppler for Windows (required by pdf2image)
- https://github.com/oschwartz10612/poppler-windows
- Go to Releases and download the **Release.xx.xx.zip** file. (not the source codes).

# pytesseract examples
```python
from pdf2image import convert_from_path, convert_from_bytes
import os

# import pytesseract locally
import sys
sys.path.append(r"C:\Users\a126291\OneDrive - AmerisourceBergen(ABC)\Softwares\pytesseract")

# import pytesseract
import pytesseract
pytesseract.tesseract_cmd = r"C:\Users\a126291\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# create temp output folder for pdm2image convert_from_path
output_folder = 'output_folder'
if not os.path.isdir(output_folder):
    os.makedirs(output_folder)

poppler_path = r"C:\Users\a126291\OneDrive - AmerisourceBergen(ABC)\Softwares\poppler-23.11.0\Library\bin"
images = convert_from_path('test.pdf',poppler_path=poppler_path,output_folder=output_folder)
image = images[0]
image_gray = image.convert("L")

# get ocr text from grayscale image
text = pytesseract.image_to_string(image_gray)
print(text)
```
