import streamlit as st
from zipfile import ZipFile
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import base64

# ------- OCR ------------
import pdf2image
import pytesseract
from pytesseract import Output, TesseractError

import os
import pytesseract
pytesseract.tesseract_cmd = r"C:\Users\a126291\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

@st.cache_data
def images_to_txt(path, language):
    pil_images = pdf2image.convert_from_bytes(path)
    all_text = []
    for pil_image in pil_images:
        text = pytesseract.image_to_string(pil_image, lang=language)
        all_text.append(text)
    return all_text, len(all_text)

@st.cache_data
def convert_pdf_to_list_bytes(uploaded_file):
    r'''Convert pdf to a list of bytes.

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
    '''

    lst_bytes = []
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    interpreter = PDFPageInterpreter(rsrcmgr, device)
    size = 0
    c = 0
    file_pages = PDFPage.get_pages(uploaded_file)
    n_pages = len(list(file_pages))
    for page in PDFPage.get_pages(uploaded_file):
        interpreter.process_page(page)
        byte_data = retstr.getvalue()
        if c == 0:
            lst_bytes.append(byte_data)
        else:
            lst_bytes.append(byte_data[size:])
        c = c + 1
        size = len(byte_data)

    device.close()
    retstr.close()
    return lst_bytes, n_pages

@st.cache_data
def convert_pdf_to_bytes(uploaded_file):
    texts = []
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    interpreter = PDFPageInterpreter(rsrcmgr, device)

    file_pages = PDFPage.get_pages(uploaded_file)
    n_pages = len(list(file_pages))
    for page in PDFPage.get_pages(uploaded_file):
        interpreter.process_page(page)
        data_bytes = retstr.getvalue()

    device.close()
    retstr.close()
    return data_bytes, n_pages

@st.cache_data
def save_pages(pages,output_dir='output'):
    # create output dir
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    path_files = []
    for page in range(len(pages)):
        filename = "page_" + str(page) + ".txt"
        with open(f"{output_dir}/" + filename, "w", encoding="utf-8") as fh:
            fh.write(pages[page])
            path_files.append(fh.name)

    # create zipfile object
    path_zip = f"{output_dir}/pdf_to_txt.zip"
    with ZipFile(path_zip, "w") as zip_obj:
        for path_file in path_files:
            zip_obj.write(path_file)

    return path_zip

def display_pdf_bytes_data(pdf_data_bytes):
    base64_pdf = base64.b64encode(pdf_data_bytes).decode("utf-8")
    raw_html = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(raw_html, unsafe_allow_html=True)
