import streamlit as st
import os

#--- ocr
import pdf2image
import pytesseract
pytesseract.tesseract_cmd = r"C:\Users\a126291\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

#@st.cache_data
def get_ocr_lst_text_from_uploaded_file(uploaded_file, language='eng',pytesseract_path=None):
    import pdf2image
    import pytesseract
    from pathlib import Path

    if pytesseract_path == None:
        pytesseract_path = r"C:\Users\a126291\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
    pytesseract.tesseract_cmd = pytesseract_path

    try: # streamlit uploded file
        data_bytes = uploaded_file.getvalue()
    except:
        try: # regular file path
            path_pdf = Path(uploaded_file)
            if path_pdf.exists():
                with open(path_pdf, 'rb') as file:
                    data_bytes = file.read()
        except:
            pass

    pil_images = pdf2image.convert_from_bytes(data_bytes)
    lst_txt = []
    for pil_image in pil_images:
        text_one_page = pytesseract.image_to_string(pil_image, lang=language)
        lst_txt.append(text_one_page)
    return lst_txt
