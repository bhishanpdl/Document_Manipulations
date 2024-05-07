from langchain.embeddings import OpenAIEmbeddings,AzureOpenAIEmbeddings
from langchain.vectorstores import FAISS

from langchain.chat_models import AzureChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

#======================= llm functions
def get_vectorstore_from_doc_chunks(doc_chunks):
    # new versions of openai needs AzureOpenAIEmbeddings
    embeddings = AzureOpenAIEmbeddings(model="text-embedding-ada-002", chunk_size=1)
    # embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", chunk_size=1)
    vectorstore = FAISS.from_documents(documents=doc_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore, temp, config):
    # llm
    llm = AzureChatOpenAI(
        openai_api_base=config['openai_api_base'],
        openai_api_version=config['openai_api_version'],
        deployment_name=config['deployment_name'],
        model_name=config['model_name'],
        openai_api_key=config['openai_api_key'],
        openai_api_type=config['openai_api_type'],
        temperature=temp)

    # memory
    memory = ConversationBufferMemory(
                memory_key="chat_history",
                input_key='question',
                output_key='answer',
                return_messages=True)

    # conversation chain
    conv_chain = ConversationalRetrievalChain.from_llm(
                llm=llm,
                retriever=vectorstore.as_retriever(),
                memory=memory,
                return_source_documents=True,
                return_generated_question=True,
                #combine_docs_chain_kwargs={"prompt": chat_prompt_template}
        )

    return conv_chain
