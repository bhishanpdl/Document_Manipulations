
#========================== util: text
from langchain.text_splitter import CharacterTextSplitter
from PyPDF2 import PdfReader
from pypdf import PdfWriter
from pdf2image import convert_from_path, convert_from_bytes
import os
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

# local imports
from src.util_ocr import get_ocr_lst_text_from_uploaded_file

# import pytesseract
import pytesseract
pytesseract.tesseract_cmd = r"C:\Users\a126291\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# Single PDF No OCR
def get_lst_text_from_single_pdf_no_ocr(path_pdf):
    r'Get list of text for each pages of pdf document'
    from PyPDF2 import PdfReader

    pdf_reader = PdfReader(path_pdf)
    lst_text = []
    for page in pdf_reader.pages:
        text = page.extract_text()
        lst_text.append(text)
    return lst_text


def get_lst_text_from_uploaded_file(uploaded_file,ocr=False,pytesseract_path=None):
    r'''Get list of text from a single pdf (works for both ocr and non-ocr pdf).

    '''
    lst_text = []
    if ocr:
        lst_text = get_ocr_lst_text_from_uploaded_file(uploaded_file, language='eng',pytesseract_path=None)
    else:
        lst_text = get_lst_text_from_single_pdf_no_ocr(uploaded_file)
    return lst_text
