import streamlit as st
from zipfile import ZipFile
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import base64
from pathlib import Path

# ------- OCR ------------
import pdf2image
import pytesseract
from pytesseract import Output, TesseractError

import os
import pytesseract
pytesseract.tesseract_cmd = r"C:\Users\a126291\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

st.set_page_config(page_title="Parse OCR PDF")

@st.cache_data
def get_ocr_lst_text_from_uploaded_file(uploaded_file, language='eng'):
    data_bytes = uploaded_file.getvalue()
    pil_images = pdf2image.convert_from_bytes(data_bytes)
    lst_txt = []
    for pil_image in pil_images:
        text_one_page = pytesseract.image_to_string(pil_image, lang=language)
        lst_txt.append(text_one_page)
    return lst_txt

#==================== uploaded file
uploaded_file = st.file_uploader("Load your PDF", type=["pdf", "png", "jpg"])

if uploaded_file:
    lst_txt = get_ocr_lst_text_from_uploaded_file(uploaded_file, language='eng')
    total_pages_str = "Pages: " + str(len(lst_txt)) + " in total"
    text_data_str = "\n\n".join(lst_txt)
    with st.expander("Display Text"):
        st.write(text_data_str)
