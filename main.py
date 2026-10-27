from fastapi import FastAPI
from pydantic import BaseModel,Field
import requests

app=FastAPI(title="Agentic knowledge Assistant")
@app.get("/")
def home():
    return{"message":"my ai assitant is running"}

class chat_request(BaseModel):
    question:str = Field(min_length=1)
@app.post("/chat")
def chat(request:chat_request):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen2.5:1.5b",
            "prompt": request.question,
            "stream": False
        }
    )

    answer = response.json()["response"]
    return {
        "question": request.question,
        "answer": answer
    }