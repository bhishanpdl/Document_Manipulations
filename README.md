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

# OCR from image PDF
```python
from pdf2image import convert_from_path, convert_from_bytes
import os

# import pytesseract
import pytesseract
pytesseract.tesseract_cmd = r"C:\Users\a126291\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def get_ocr_from_pdf(path_pdf,poppler_path=None):
    path_pdf = str(path_pdf)
    # create temp output folder for pdm2image convert_from_path
    output_folder = 'temp_output_folder'
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)

    if poppler_path is None:
        poppler_path = r"C:\Users\a126291\OneDrive - AmerisourceBergen(ABC)\Softwares\poppler-23.11.0\Library\bin"
    images = convert_from_path(path_pdf,poppler_path=poppler_path,output_folder=output_folder)
    images_gray = [image.convert("L") for image in images]

    # get ocr text from grayscale image
    texts = [pytesseract.image_to_string(image_gray) for image_gray in images_gray]
    out = '\n'.join(texts)
    return out

path_pdf = r"C:\Users\a126291\OneDrive - AmerisourceBergen(ABC)\data\pdf_files\ocr_pdf\Drug Channels.pdf"
path_pdf = 'test.pdf'
text = get_ocr_from_pdf(path_pdf)
print(text)
```
