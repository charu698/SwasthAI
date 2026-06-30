from unittest import result

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import os

from app.config import UPLOAD_FOLDER
from app.services.vision_service import analyze_prescription

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post("/")
async def upload_image(
    file: UploadFile = File(...),
    language: str = Form("English")):

    try:
        # Create uploads folder if it doesn't exist
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        # Save uploaded file
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        # Run the AI pipeline
        result = analyze_prescription(
    file_path,
    language
)
        # Return response
        # Return response
        return {
            "success": True,
            "filename": file.filename,
            "ocr_text": "",   # Vision doesn't produce OCR text
            "summary": result["summary"],
            "medicines":result["medicines"],
}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )