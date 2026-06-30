from google import genai

from app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def translate_text(text: str, language: str):

    prompt = f"""
Translate the following medical text into {language}.

Rules:

- Keep medicine names in English.
- Translate only explanations.
- Use simple language understandable by patients.
- Return only translated text.

Text:

{text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text