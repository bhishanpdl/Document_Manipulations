
import os
import sys
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain.chat_models import AzureChatOpenAI

# get config
import sys
sys.path.append(os.path.expanduser("~/.utils"))
from util_openai import get_config_dict
config = get_config_dict(env='openai')

# Azure Chat example
template = """
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Question: {question}
"""
prompt = PromptTemplate(input_variables=["question"], template=template)

llm = AzureChatOpenAI(**config['kw_azure_chat_openai'],temperature=0)

chain = LLMChain(llm=llm, prompt=prompt)
query = "What are the competitors of AmerisourceBergen?"
response = chain.run(query)
print(response)
