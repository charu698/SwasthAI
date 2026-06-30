from app.services.llm_service import explain_medicines

ocr_text = """
Dolo 650
Azithromycin 500
Pantoprazole
"""

result = explain_medicines(ocr_text)

print(result)