from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_service import handle_chat

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest):
    response = handle_chat(request.message)

    return {"response": response}
