"""
This code is used to retrieve response from RAG
This part of code is used in fa.py file which is also the root file.
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from vectordb.DocSearch import docsearch
from langchain_core.output_parsers import StrOutputParser

from LLM.llms import llm
from langchain_core.runnables import RunnablePassthrough
from utils import format_docs
from prompts.propmt import prompt_character


retriever = docsearch.docsearch.as_retriever(search_kwargs={"k": 4})

# Change the prompt file in case you want to modify the role
address = os.path.join(os.path.dirname(__file__), "prompts/Lallan.txt")

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt_character(prompt_template_address=address)
    | llm
    | StrOutputParser()
)
