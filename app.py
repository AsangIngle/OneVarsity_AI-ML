from fastapi import FastAPI, UploadFile, File
import shutil

from services.summarizer import summarize_text
from services.qa_service import qa_from_pdf
from services.learning_path import generate_learning_path

app = FastAPI(title="AI Microservices with LangChain + Ollama")


@app.post("/summarize")
def summarize(text: str):
    return {"summary": summarize_text(text)}


@app.post("/qa")
def question_answer(file: UploadFile = File(...), question: str = ""):

    file_path = file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    answer = qa_from_pdf(file_path, question)

    return {"answer": answer}


@app.get("/learning-path")
def learning_path(goal: str, level: str):
    path = generate_learning_path(goal, level)

    return {"learning_path": path}


@app.get("/")
def home():
    return {"message": "AI Microservices API is running"}
