import streamlit as st
import pdf2image
from PIL import Image
import pytesseract
from pytesseract import Output, TesseractError
from pathlib import Path

# local imports
from util import (
    convert_pdf_to_list_bytes,
    convert_pdf_to_bytes,
    save_pages,
    display_pdf_bytes_data,
    images_to_txt,
)
st.set_page_config(page_title="PDF to Text")
#======================== settings
hide = """
<style>
footer{
	visibility: hidden;
    	position: relative;
}
.viewerBadge_container__1QSob{
  	visibility: hidden;
}
#MainMenu{
	visibility: hidden;
}
<style>
"""



html_temp = """
            <div style="background-color:{};padding:1px">

            </div>
            """

st.markdown(
    """
    ## Text data extractor: PDF to Text

"""
)
languages = {
    "English": "eng",
    "French": "fra",
    "Arabic": "ara",
    "Spanish": "spa",
}

#============================= sidebar================
with st.sidebar:
    st.title(":outbox_tray: PDF to Text")
    text_output = st.selectbox(
        "How do you want your output text?",
        ("One text file (.txt)", "Text file per page (ZIP)"),
    )
    ocr_box = st.checkbox("Enable OCR (scanned document)",value=False)

    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"), unsafe_allow_html=True)
    st.markdown(
        """
    # Steps
    1. Upload your image or pdf file
    2. Choose one text file output or zipped file output.
    3. Download
    """
    )
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"), unsafe_allow_html=True)

#==================== uploaded file
uploaded_file = st.file_uploader("Load your PDF", type=["pdf", "png", "jpg"])
st.markdown(hide, unsafe_allow_html=True)

if uploaded_file:
    data_bytes = uploaded_file.read()
    file_extension = Path(uploaded_file.name).suffix

    if file_extension == ".pdf":
        # display document
        with st.expander("Display document"):
            display_pdf_bytes_data(data_bytes)
        if ocr_box:
            language_option = st.selectbox(
                "Select the document language", list(languages.keys())
            )
        # pdf to text
        if text_output == "One text file (.txt)":
            if ocr_box:
                texts, n_pages = images_to_txt(data_bytes, languages[language_option])
                total_pages_str = "Pages: " + str(n_pages) + " in total"
                text_data_str = "\n\n".join(texts)
                with st.expander("Display Text"):
                    st.write('\n\n'.join(texts))
            else:
                converted_bytes, n_pages = convert_pdf_to_bytes(uploaded_file)
                total_pages_str = "Pages: " + str(n_pages) + " in total"

            st.info(total_pages_str)
            st.download_button("Download txt file", converted_bytes)
        else:
            if ocr_box:
                text_data, n_pages = images_to_txt(data_bytes, languages[language_option])
                total_pages_str = "Pages: " + str(n_pages) + " in total"
                with st.expander("Display Text"):
                    st.write('\n\n'.join(text_data))
            else:
                lst_bytes, n_pages = convert_pdf_to_list_bytes(uploaded_file)
                total_pages_str = "Pages: " + str(n_pages) + " in total"
            st.info(total_pages_str)

            #==================================================
            path_zip = save_pages(lst_bytes)
            # download text data
            with open(path_zip, "rb") as fh:
                btn = st.download_button(
                    label="Download ZIP (txt)",
                    data=fh,
                    file_name="pdf_to_txt.zip",
                    mime="application/zip",
                )
    else:
        language_option = st.selectbox(
            "What's the language of the text in the image?", list(languages.keys())
        )
        pil_image = Image.open(uploaded_file)
        text = pytesseract.image_to_string(pil_image, lang=languages[language_option])
        col1, col2 = st.columns(2)
        with col1:
            with st.expander("Display Image"):
                st.image(uploaded_file)
        with col2:
            with st.expander("Display Text"):
                st.info(text)
        st.download_button("Download txt file", text)
