import os
from fastapi import FastAPI, Request
from question_answerer import QuestionAnswerer

qa = QuestionAnswerer()
api = FastAPI()

@api.get("/")
def hello():
    return "Welcome, I'm dbt's question answering bot."

@api.get("/answer")
def get_answer(question: str = "What is dbt?"):
    return {"answer": qa.answer_question(question)}

@api.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    question = data.get("question", "")
    answer = qa.answer_question(question)
    return {"answer": answer}
