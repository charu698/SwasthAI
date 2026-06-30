from fastapi import APIRouter
from pydantic import BaseModel

from app.services.translation_service import translate_text

router = APIRouter(
    prefix="/translate",
    tags=["Translation"]
)


class TranslationRequest(BaseModel):
    text: str
    language: str


class TranslationResponse(BaseModel):
    translated_text: str


@router.post("/", response_model=TranslationResponse)
def translate(request: TranslationRequest):

    translated = translate_text(
        request.text,
        request.language
    )

    return TranslationResponse(
        translated_text=translated
    )