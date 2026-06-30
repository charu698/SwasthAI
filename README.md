# 🩺 SwasthAI – AI Health Companion for Bharat

SwasthAI is an AI-powered healthcare assistant that helps users understand handwritten and printed prescriptions using Google Gemini Vision.

It extracts medicines, explains their purpose, dosage, side effects, and precautions in simple language and supports multiple Indian languages.

---

## ✨ Features

- 📷 Upload handwritten or printed prescriptions
- 🤖 AI-powered medicine extraction using Gemini Vision
- 💊 Medicine explanation
- 🧠 AI-generated health summary
- 🌍 Multilingual support
- 💬 AI Chat Assistant for medicine-related questions
- ⚡ FastAPI Backend
- ⚛️ React Frontend

---

## 🛠 Tech Stack

### Frontend
- React
- Vite
- Axios

### Backend
- FastAPI
- Python

### AI
- Google Gemini Vision API

### OCR
- EasyOCR (legacy pipeline)

---

## 📂 Project Structure

```
SwasthAI
│
├── app/
├── frontend/
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### Backend

```bash
pip install -r requirements.txt

uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## 👩‍💻 Developed By

**Charu Arora**