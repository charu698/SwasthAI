from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ask_ai

router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"]
)


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer = ask_ai(
        request.medicines,
        request.question
    )

    return ChatResponse(answer=answer)