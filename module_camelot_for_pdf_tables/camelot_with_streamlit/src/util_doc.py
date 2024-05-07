
import os
import sys
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pathlib import Path

# local imports
from src.util_text import get_lst_text_from_uploaded_file

def get_doc_chunks_from_lst_text(lst_text,path_pdf):
    """Convert list of text to list of langchain Documents.

    Note: we have chunks, not the page documents

    from langchain.docstore.document import Document
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    """
    from langchain.docstore.document import Document
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from pathlib import Path

    if isinstance(lst_text, str):
        # Take a single string as one page
        lst_text = [lst_text]

    # get docs
    page_docs = [Document(page_content=page) for page in lst_text]

    # Add page numbers as metadata
    for i, doc in enumerate(page_docs):
        doc.metadata["page"] = i + 1

    # Split pages into chunks
    doc_chunks = []

    for doc in page_docs:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""],
            chunk_overlap=0,
        )
        chunks = text_splitter.split_text(doc.page_content)
        for i, chunk in enumerate(chunks):
            doc = Document(
                page_content=chunk, metadata={"page": doc.metadata["page"], "chunk": i}
            )
            # Add sources a metadata
            doc.metadata["source"] = f"{doc.metadata['page']}-{doc.metadata['chunk']}"
            doc.metadata["path_name"] = Path(path_pdf).name
            doc.metadata["path_name_full"] = str(path_pdf)
            doc_chunks.append(doc)
    return doc_chunks

def get_all_doc_chunks_from_path_pdfs(path_pdfs,ocr=False):
    r'''Get document chunks for all the pdfs.

    Depends:
    ========
    - get_lst_text_from_uploaded_file
    - get_doc_chunks_from_lst_text

    '''
    all_doc_chunks = []
    for i, path_pdf in enumerate(path_pdfs):
        lst_text =  get_lst_text_from_uploaded_file(path_pdf,ocr=ocr)
        doc_chunks = get_doc_chunks_from_lst_text(lst_text,path_pdf)
        for doc in doc_chunks:
            doc.metadata["pdf_number"] = str(i+1)
            all_doc_chunks.append(doc)
    return all_doc_chunks
