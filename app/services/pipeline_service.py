from app.services.ocr_service import extract_text
from app.services.llm_service import explain_medicines


def analyze_prescription(image_path: str):

    # Step 1: OCR
    ocr_text = extract_text(image_path)

    # Step 2: Gemini
    medicines = explain_medicines(ocr_text)

    analysis = explain_medicines(ocr_text)

    return {
    "ocr_text": ocr_text,
    "summary": analysis["summary"],
    "medicines": analysis["medicines"]
}