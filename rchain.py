from vectodb import docsearch
from langchain_core.output_parsers import StrOutputParser
from llms import llm
from langchain_core.runnables import RunnablePassthrough
from utils import format_docs
from propmt import lallan_prompt


retriever = docsearch.docsearch.as_retriever(search_kwargs={"k": 4})


rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | lallan_prompt
    | llm
    | StrOutputParser()
)
