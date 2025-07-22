from pydantic import BaseModel
from typing import List
from ai_agent import get_response_from_ai_agent

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

from fastapi import FastAPI

ALLOWED_MODEL_NAMES = ["llama-3.3-70b-versatile", "gpt-4o-mini", "llama-3.3-70b-8192", "mixtral-8x7b-32768"]

app = FastAPI(title="AI Agent API")
@app.post("/chat")
def chat_endpoint(request: RequestState):
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid Model"}
    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    provider = request.model_provider
    response = get_response_from_ai_agent(llm_id, query, allow_search, provider)
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)