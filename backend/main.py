from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from api.verification import router as verification_router
from api.dashboard import router as dashboard_router

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

app.include_router(verification_router)
app.include_router(dashboard_router)

# -----------------------------
# Frontend Folder
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR.parent / "frontend"

app.mount(
    "/assets",
    StaticFiles(directory=FRONTEND_DIR / "assets"),
    name="assets"
)

# -----------------------------
# HTML Pages
# -----------------------------

@app.get("/")
def index():
    return FileResponse(FRONTEND_DIR / "index.html")

@app.get("/verification")
def verification():
    return FileResponse(FRONTEND_DIR / "verification.html")

@app.get("/officer")
def officer():
    return FileResponse(FRONTEND_DIR / "officer.html")

@app.get("/analytics")
def analytics():
    return FileResponse(FRONTEND_DIR / "analytics.html")

@app.get("/assistant")
def assistant():
    return FileResponse(FRONTEND_DIR / "ai-assistant.html")
@app.get("/services")
def services():
    return FileResponse(FRONTEND_DIR / "services.html")