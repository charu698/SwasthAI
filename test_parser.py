from app.services.medicine_parser import extract_medicine_names

text = """
Biotin Tablets USP

H-Vit

Store below 25°C

Schedule H Drug

Take after food
"""

medicines = extract_medicine_names(text)

print(medicines)