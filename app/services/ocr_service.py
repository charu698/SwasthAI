import easyocr

# Create OCR Reader only once
reader = easyocr.Reader(['en'])


def extract_text(image_path: str):

    result = reader.readtext(image_path)

    extracted_text = ""

    for detection in result:
        extracted_text += detection[1] + "\n"

    return extracted_text