from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from utils.vector_store import create_vector_store

llm = Ollama(model="llama3")

def qa_from_pdf(file_path, question):

    db = create_vector_store(file_path)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=db.as_retriever(),
        chain_type="stuff"
    )

    result = qa_chain.run(question)

    return result
