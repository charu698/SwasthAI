from app.services.ocr_service import extract_text

image_path = "uploads/strip.png"

text = extract_text(image_path)

print("=" * 40)
print("Extracted Text")
print("=" * 40)
print(text)