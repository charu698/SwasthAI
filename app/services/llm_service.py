import json
from google import genai

from app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def explain_medicines(ocr_text: str):

    prompt = f"""
You are an expert pharmacist.

OCR Text:

{ocr_text}

Tasks:

1. Identify all medicine names.
2. For every medicine provide:
   - medicine
   - purpose
   - dosage
   - side_effects
   - precautions
3. Generate a short AI Health Summary (2-3 sentences) explaining the prescription in simple language.

Return ONLY valid JSON.

Example:

{{
  "summary": "This prescription contains medicines for pain relief...",
  "medicines": [
    {{
      "medicine": "Dolo 650",
      "purpose": "Pain relief",
      "dosage": "As prescribed",
      "side_effects": ["Nausea"],
      "precautions": "Avoid overdose"
    }}
  ]
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()
    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    return json.loads(text)