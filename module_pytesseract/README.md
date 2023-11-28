# Get OCR from a jpg file

```python
from PIL import Image
import pytesseract

# binary path
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\a126291\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# ocr
print(pytesseract.image_to_string(Image.open('test_good.jpg')))
```

# Get OCR from text file with image paths
```python
with open('images.txt','w') as fh:
    fh.write(r"C:\Users\a126291\OneDrive - AmerisourceBergen(ABC)\GPS\a00_AI_POC_Projects\pdf_ocr_example\test_good.jpg")

print(pytesseract.image_to_string('images.txt'))
```

# Create Searchable PDF
```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\a126291\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

pdf = pytesseract.image_to_pdf_or_hocr('test_good.jpg', extension='pdf')
with open('test_good_searchable.pdf', 'w+b') as fh:
    fh.write(pdf) # pdf type is bytes by default
```

# OCR from image pdf
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
