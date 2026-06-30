from google import genai

from app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def ask_ai(medicines, question):

    prompt = f"""
You are an experienced pharmacist.

The user has these medicines:

{medicines}

Question:

{question}

Answer in simple language.

If the answer requires a doctor's advice,
clearly say so.

Keep the answer under 150 words.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text