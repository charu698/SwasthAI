# 🩺 SwasthAI – AI Health Companion for Bharat

**An AI-powered healthcare assistant for understanding handwritten and printed medical prescriptions.**

🚀 **[Live Demo](https://swasth-ai-sigma.vercel.app)** | **[GitHub Repository](https://github.com/charu698/SwasthAI)** | **[Backend API](https://swasthai-api.onrender.com)**

## 📌 Overview

SwasthAI is an AI-powered healthcare assistant that helps users understand handwritten and printed prescriptions using Google Gemini Vision.

It extracts medicine information, explains their purpose, dosage, side effects, and precautions in simple language, and supports multiple Indian languages.

## ✨ Features

- 📷 Upload handwritten or printed prescriptions
- 🤖 AI-powered medicine extraction using Gemini Vision
- 💊 Medicine explanations
- 🧠 AI-generated health summaries
- 🌍 Multilingual support
- 💬 AI chat assistant for medicine-related questions
- ⚡ FastAPI backend
- ⚛️ React frontend

## 🛠 Tech Stack

**Frontend**
- React
- Vite
- Axios

**Backend**
- Python
- FastAPI

**AI**
- Google Gemini Vision API

**OCR**
- EasyOCR (legacy pipeline)

## 📂 Project Structure

```text
SwasthAI/
│
├── app/
│   ├── api/
│   ├── services/
│   └── main.py
│
├── frontend/
│   ├── src/
│   └── package.json
│
├── requirements.txt
├── render.yaml
└── README.md
```

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/charu698/SwasthAI.git
cd SwasthAI
```

### 2. Backend Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure your Gemini API key in a root `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

Start the backend:

```bash
uvicorn app.main:app --reload
```

### 3. Frontend Setup

Open another terminal:

```bash
cd frontend
npm install
```

Configure the frontend API URL in `frontend/.env.local`:

```env
VITE_API_URL=http://127.0.0.1:8000
```

Start the frontend:

```bash
npm run dev
```

The application will be available at:

```text
http://localhost:5173
```

## 🌐 Deployment

- **Frontend:** Vercel
- **Backend:** Render
- **AI Integration:** Google Gemini Vision API

## 🔐 Environment Variables

Keep API keys and other secrets private. Never commit `.env` files or expose your Gemini API key in frontend code or GitHub.

## 👩‍💻 Developed By

**Charu Arora**# 🩺 SwasthAI – AI Health Companion for Bharat

**An AI-powered healthcare assistant for understanding handwritten and printed medical prescriptions.**

🚀 **[Live Demo](https://swasth-ai-sigma.vercel.app)** | **[GitHub Repository](https://github.com/charu698/SwasthAI)** | **[Backend API](https://swasthai-api.onrender.com)**

## 📌 Overview

SwasthAI is an AI-powered healthcare assistant that helps users understand handwritten and printed prescriptions using Google Gemini Vision.

It extracts medicine information, explains their purpose, dosage, side effects, and precautions in simple language, and supports multiple Indian languages.

## ✨ Features

- 📷 Upload handwritten or printed prescriptions
- 🤖 AI-powered medicine extraction using Gemini Vision
- 💊 Medicine explanations
- 🧠 AI-generated health summaries
- 🌍 Multilingual support
- 💬 AI chat assistant for medicine-related questions
- ⚡ FastAPI backend
- ⚛️ React frontend

## 🛠 Tech Stack

**Frontend**
- React
- Vite
- Axios

**Backend**
- Python
- FastAPI

**AI**
- Google Gemini Vision API

**OCR**
- EasyOCR (legacy pipeline)

## 📂 Project Structure

```text
SwasthAI/
│
├── app/
│   ├── api/
│   ├── services/
│   └── main.py
│
├── frontend/
│   ├── src/
│   └── package.json
│
├── requirements.txt
├── render.yaml
└── README.md
```

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/charu698/SwasthAI.git
cd SwasthAI
```

### 2. Backend Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure your Gemini API key in a root `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

Start the backend:

```bash
uvicorn app.main:app --reload
```

### 3. Frontend Setup

Open another terminal:

```bash
cd frontend
npm install
```

Configure the frontend API URL in `frontend/.env.local`:

```env
VITE_API_URL=http://127.0.0.1:8000
```

Start the frontend:

```bash
npm run dev
```

The application will be available at:

```text
http://localhost:5173
```

## 🌐 Deployment

- **Frontend:** Vercel
- **Backend:** Render
- **AI Integration:** Google Gemini Vision API

## 🔐 Environment Variables

Keep API keys and other secrets private. Never commit `.env` files or expose your Gemini API key in frontend code or GitHub.

## 👩‍💻 Developed By

**Charu Arora**
