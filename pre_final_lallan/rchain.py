"""
This code is used to retrieve response from RAG
This part of code is used in fa.py file which is also the root file.
"""

from pre_final_lallan.vectordb.DocSearch import docsearch
from langchain_core.output_parsers import StrOutputParser
from pre_final_lallan.LLM.llms import llm
from langchain_core.runnables import RunnablePassthrough
from utils import format_docs
from pre_final_lallan.prompts.propmt import prompt_character


retriever = docsearch.docsearch.as_retriever(search_kwargs={"k": 4})

# Change the prompt file in case you want to modify the role
address = r"pre_final_lallan/prompts/Lallan.txt"

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt_character(prompt_template_address=address)
    | llm
    | StrOutputParser()
)
