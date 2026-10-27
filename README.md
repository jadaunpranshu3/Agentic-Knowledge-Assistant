# Agentic Knowledge Assistant

## Project Overview
A backend AI assistant built using FastAPI and Ollama.
It accepts user questions through a REST API and generates responses using a locally running language model.

## Technologies Used
- Python
- FastAPI
- REST API
- Ollama
- Qwen 2.5 (1.5B)
- Requests

## Features
- API endpoint for submitting questions
- Local LLM integration through Ollama
- JSON request and response handling

## Run Locally
1. Install dependencies:
   pip install -r requirements.txt

2. Start Ollama and ensure the model is available:
   ollama run qwen2.5:1.5b

3. Start the FastAPI server:
   uvicorn main:app --reload

4. Open the API documentation:
   http://127.0.0.1:8000/docs
