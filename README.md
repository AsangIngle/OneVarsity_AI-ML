# OneVarsity_AI-ML

# AI Microservices with LangChain + Ollama

A modular AI microservices project built using **FastAPI, LangChain, and Ollama**.  
This system exposes REST APIs for common GenAI use cases including text summarization, document-based question answering (RAG), and dynamic learning path generation.

The goal of this project is to demonstrate **production-style backend design** while working entirely with open-source LLMs.

---

## Features

✅ **Text Summarization**  
Generate concise summaries from large text inputs using a map-reduce strategy.

✅ **Q&A over Documents (RAG)**  
Upload a PDF and ask questions. The system retrieves relevant chunks using FAISS and produces contextual answers.

✅ **Dynamic Learning Path Generator**  
Creates structured learning roadmaps based on a user's goal and experience level.

---

## Tech Stack

- **FastAPI** → High-performance API framework  
- **LangChain** → LLM orchestration  
- **Ollama (Llama3)** → Local open-source language model  
- **FAISS** → Vector similarity search  
- **SentenceTransformers** → Embeddings  
- **PyPDF** → Document loading  

---



## Project Structure

