from langchain_community.llms import Ollama
from langchain_core.documents import Document
from langchain.chains.summarize import load_summarize_chain

llm = Ollama(model="llama3")

def summarize_text(text: str):

    docs = [Document(page_content=text)]

    chain = load_summarize_chain(
        llm,
        chain_type="map_reduce"
    )

    return chain.run(docs)
