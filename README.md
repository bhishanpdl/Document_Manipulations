<!-- TOC start (generated with https://github.com/derlin/bitdowntoc) -->

- [PDF_Manipulations](#pdf_manipulations)
- [Download Tesseract Binary](#download-tesseract-binary)
- [Download Poppler for Windows (required by pdf2image)](#download-poppler-for-windows-required-by-pdf2image)
- [pytesseract examples](#pytesseract-examples)
- [OCR from image PDF](#ocr-from-image-pdf)
- [Get PDF Info](#get-pdf-info)

<!-- TOC end -->

<!-- TOC --><a name="pdf_manipulations"></a>
# PDF_Manipulations

- [module: pytesseract](https://github.com/madmaze/pytesseract/tree/master)

# Articles
- [medium: PDF Manipulation with Python: A Comprehensive Guide to Building PDF Tools and Automation](https://medium.com/@meetjethwa3/pdf-manipulation-with-python-a-comprehensive-guide-to-building-pdf-tools-and-automation-c1b4564cdd8c)

<!-- TOC --><a name="download-tesseract-binary"></a>
# Download Tesseract Binary
- https://github.com/UB-Mannheim/tesseract/wiki

<!-- TOC --><a name="download-poppler-for-windows-required-by-pdf2image"></a>
# Download Poppler for Windows (required by pdf2image)
- https://github.com/oschwartz10612/poppler-windows
- Go to Releases and download the **Release.xx.xx.zip** file. (not the source codes).

<!-- TOC --><a name="pytesseract-examples"></a>
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

<!-- TOC --><a name="ocr-from-image-pdf"></a>
# OCR from image PDF
```python
from pdf2image import convert_from_path, convert_from_bytes
import os

# import pytesseract
import pytesseract
pytesseract.tesseract_cmd = r"C:\Users\a126291\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def get_ocr_from_pdf(path_pdf,poppler_path=None):
    r'''Get OCR from image PDF document. Also works for regular PDF.

    Depends:
    =========
    - tesseract (get installer for windows)
    - poppler   (get binary file from github releases for Windows)

    '''
    # path to pdf file
    path_pdf = str(path_pdf)

    # create temp output folder for pdm2image convert_from_path
    output_folder = 'temp_output_folder'
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)

    # poppler path
    if poppler_path is None:
        poppler_path = r"C:\Users\a126291\OneDrive - AmerisourceBergen(ABC)\Softwares\poppler-23.11.0\Library\bin"

    # get images from pdf
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

<!-- TOC --><a name="get-pdf-info"></a>
# Get PDF Info
```python
from pdf2image import pdfinfo_from_path

# Path to the PDF file
path_to_pdf = r"C:\Users\a126291\OneDrive - AmerisourceBergen(ABC)\data\pdf_files\ocr_pdf\ocr_test_small.pdf"

# Get information about the PDF file
pdf_info = pdfinfo_from_path(path_to_pdf)

# Retrieve the page count from the PDF info
page_count = pdf_info["Pages"]

print(f"The PDF file has {page_count} pages.")
```

# Convert pdf to jpg using pdf2image
```python
from pdf2image import convert_from_path

path_pdf = r'"C:\Users\a126291\OneDrive - AmerisourceBergen(ABC)\GPS\aa_Learn\PDF_Manipulation\a01_ocr\dev\data\multi-column-2p.pdf"'
path_pdf = path_pdf[1:-1]
images = convert_from_path(path_pdf)

odir = 'output'
if not os.path.isdir(odir):
    os.makedirs(odir)

for i,img in enumerate(images):
    img.save(f'{odir}/page_{i:03d}.jpg')
```

# Convert pdf to jpg function
```python
def pdf_to_jpg(dpi=200,
               first_page=None,
               last_page=None,
               size=None,
               page_nums=None,
               fmt = 'jpg'):
    r"""Convert all pdfs in given path to images in respective folders.

    We can also choose the size of images:
    size = 400           preserves aspect ratio
    size = (400,None)    preserves aspect ratio
    size = (400,400)     won't preserve aspect ratio

    Note: png conversion is much slower
          and also output png size is much higher than jpg.
    Example:
    ========
    pdf_file = "C:\Users\a126291\OneDrive - AmerisourceBergen(ABC)\GPS\p_994_Patient_Journey\docs\GSK MoRe Patient Journey 2022YTD.pdf"

    pdf_path = C:\Users\a126291\OneDrive - AmerisourceBergen(ABC)\GPS\p_994_Patient_Journey\docs

    References:
    - https://pdf2image.readthedocs.io/en/latest/reference.html

    """
    import time
    import pathlib
    import pyperclip
    import webbrowser
    from pdf2image import convert_from_path

    try:
        path_cwd = pyperclip.paste()
    except:
        path_cwd = ''

    if path_cwd[-5:-1] == '.pdf':
        pdf_paths = [path_cwd[1:-1]]
    else:
        pdf_paths = glob.glob(f"{path_cwd}\*.pdf")

    # if dir is not copied, return pre-maturely
    cond1 = path_cwd[-5:-1] == '.pdf'
    cond2 = os.path.isdir(path_cwd)
    cond = cond1 | cond2
    if not cond:
        return "Clipboard is not path like."

    for pdf_path in  pdf_paths:
        base = os.path.basename(pdf_path)
        name = base.replace('.pdf','')

        odir = fr"{os.path.dirname(pdf_path)}\\images_{name}"
        if not os.path.isdir(odir):
            os.makedirs(odir)

        images = convert_from_path(pdf_path,dpi=dpi,size=size,fmt=fmt)
        first_page = 1 if first_page is None else first_page
        last_page = len(images) if last_page is None else last_page
        page_nums = list(range(first_page, last_page+1)) if page_nums is None else page_nums

        for i in page_nums:
            img = images[i-1]
            img.save(f'{odir}/page_{i:03d}.{fmt}')

    out = f"""Images are created at:
{path_cwd}
    """
    pyperclip.copy(out)

    return out

# Usage
import pyperclip
import glob

path_pdf = r'"C:\Users\a126291\OneDrive - AmerisourceBergen(ABC)\GPS\aa_Learn\PDF_Manipulation\a01_ocr\dev\data\multi-column-2p.pdf"'
pdf_to_jpg(dpi=200,first_page=None,last_page=None,size=None,page_nums=None,fmt = 'jpg')
```
