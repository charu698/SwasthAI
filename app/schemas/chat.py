from pydantic import BaseModel


class ChatRequest(BaseModel):
    medicines: list
    question: str


class ChatResponse(BaseModel):
    answer: str