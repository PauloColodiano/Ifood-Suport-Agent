from fastapi import FastAPI
from .agent import run_agent

app = FastAPI()

@app.post("/chat")
async def chat(payload: dict):
    user_message = payload.get("message", "")
    response = await run_agent(user_message)
    return {"response": response}
