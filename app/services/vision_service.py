import json
from google import genai
from PIL import Image

from app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def analyze_prescription(image_path: str, language: str):
    """
    Analyze a prescription image using Gemini Vision.
    """

    image = Image.open(image_path)

    prompt = f"""
You are an experienced pharmacist.

Analyze this prescription image carefully.

The user's preferred language is: {language}

Tasks:

1. Identify all medicines visible in the prescription.
2. For every medicine provide:
   - medicine
   - purpose
   - dosage
   - side_effects
   - precautions
3. Generate a short AI Health Summary (2–3 sentences).

IMPORTANT RULES:

- Generate ALL explanations in {language}.
- Keep ALL medicine names in English.
- Do NOT translate medicine names.
- If dosage is not visible, write "Consult Doctor" in {language}.
- Use simple language suitable for patients.
- If you are unsure about a medicine name, mention that it is your best interpretation.

Return ONLY valid JSON in this format:

{{
  "summary": "...",
  "medicines": [
    {{
      "medicine": "Dolo 650",
      "purpose": "...",
      "dosage": "...",
      "side_effects": ["...", "..."],
      "precautions": "..."
    }}
  ]
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[prompt, image],
    )

    print("========== GEMINI RESPONSE ==========")
    print(response.text)

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()
    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    return json.loads(text)