# imports
import os
import json
import yaml
import numpy as np
import pandas as pd

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import AzureOpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import AzureChatOpenAI
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chains import ConversationalRetrievalChain

# config
def get_config_dict():
    import os
    import yaml

    with open(os.path.expanduser('~/.config/config.yaml')) as fh:
        config = yaml.safe_load(fh)

    # openai
    keys = ["OPENAI_API_KEY","OPENAI_API_TYPE","OPENAI_API_BASE","OPENAI_API_VERSION"]
    for key in keys:
        os.environ[key] = config.get(key)

    return config

config = get_config_dict()

# variables
path_pdf = r"C:\Users\a126291\OneDrive - AmerisourceBergen(ABC)\data\pdf_files\cencora_earning_reports\AmerisourceBergen-Reports-Fiscal-2023-Second-Quarter-Results-2023.pdf"

embed_model= "text-embedding-ada-002"
vectore_store_persist_directory = 'vector_store'

# load documents
loader = PyPDFLoader(path_pdf)
documents = loader.load()

# create embeddings
embed_model= "text-embedding-ada-002"
embeddings = AzureOpenAIEmbeddings(model=embed_model, chunk_size=1)

# create vector store
pages = loader.load_and_split()
vector_store = FAISS.from_documents(documents=pages, embedding=embeddings)
vector_store.save_local(vectore_store_persist_directory)

# llm
llm = AzureChatOpenAI(**config['kw_azure_llm'],temperature=0.4)

# load vector store from local file
vector_store = FAISS.load_local(vectore_store_persist_directory, embeddings)
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k":2},
    return_source_documents=True
)

# question answer
qa = ConversationalRetrievalChain.from_llm(llm, retriever)
chat_history = []
query = "Is there gain or loss of revenue in this quarter?"
result = qa({'question': query, 'chat_history': chat_history})
print(result['answer'])

# another chat
print()
chat_history = [(query,result['answer'])]
query = "Is there gain in revenue for U.S. Healthcare Solutions this quarter?"

result = qa({'question': query, 'chat_history': chat_history})
print(result['answer'])
