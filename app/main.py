from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.upload import router as upload_router
from app.api.medicine import router as medicine_router
from app.api.health import router as health_router
from app.api.chat import router as chat_router


app = FastAPI(
    title="SwasthAI API",
    description="AI Health Companion for Bharat",
    version="1.0.0"
)

# Allow React frontend to access FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(upload_router)
app.include_router(medicine_router)
app.include_router(health_router)
app.include_router(chat_router)


@app.get("/")
def root():
    return {
        "status": "running",
        "message": "Welcome to SwasthAI 🚀"
    }