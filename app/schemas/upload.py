from fastapi import APIRouter, UploadFile, File, HTTPException
import os

from app.config import UPLOAD_FOLDER
from app.schemas.prescription import PrescriptionResponse
from app.services.pipeline_service import analyze_prescription

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post(
    "/",
    response_model=PrescriptionResponse
)
async def upload_image(file: UploadFile = File(...)):

    try:

        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        file_path = os.path.join(
            UPLOAD_FOLDER,
            file.filename
        )

        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        result = analyze_prescription(file_path)

        return PrescriptionResponse(
            success=True,
            filename=file.filename,
            ocr_text=result["ocr_text"],
            medicines=result["medicines"],
            summary=f"{len(result['medicines'])} medicine(s) detected successfully."
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )