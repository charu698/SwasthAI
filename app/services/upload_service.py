import os

from fastapi import UploadFile

from app.config import UPLOAD_FOLDER
from app.services.ocr_service import extract_text

ALLOWED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png"
}


async def save_uploaded_file(file: UploadFile):

    extension = os.path.splitext(file.filename)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise ValueError(
            "Only JPG, JPEG and PNG files are allowed."
        )

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    extracted_text = extract_text(file_path)

    return {
        "filename": file.filename,
        "text": extracted_text
    }