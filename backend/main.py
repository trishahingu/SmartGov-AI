from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.verification import router as verification_router

app = FastAPI(
    title="SmartGov AI API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    verification_router,
    prefix="/api",
    tags=["Verification"]
)


@app.get("/")
def home():
    return {
        "message": "SmartGov AI Backend Running",
        "status": "success"
    }