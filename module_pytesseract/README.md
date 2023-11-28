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
