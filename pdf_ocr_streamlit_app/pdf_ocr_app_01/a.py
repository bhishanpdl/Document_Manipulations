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

st.set_page_config(page_title="PDF to Text")

@st.cache_data
def get_ocr_text_from_data_bytes(data_bytes, language='eng'):
    pil_images = pdf2image.convert_from_bytes(data_bytes)
    all_text = []
    for pil_image in pil_images:
        text = pytesseract.image_to_string(pil_image, lang=language)
        all_text.append(text)
    return all_text, len(all_text)

#==================== uploaded file
uploaded_file = st.file_uploader("Load your PDF", type=["pdf", "png", "jpg"])


if uploaded_file:
    data_bytes = uploaded_file.read()
    file_extension = Path(uploaded_file.name).suffix

    texts, n_pages = get_ocr_text_from_data_bytes(data_bytes, language='eng')
    total_pages_str = "Pages: " + str(n_pages) + " in total"
    text_data_str = "\n\n".join(texts)
    with st.expander("Display Text"):
        st.write('\n\n'.join(texts))
