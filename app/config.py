import os
from dotenv import load_dotenv

load_dotenv()

UPLOAD_FOLDER = "uploads"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")