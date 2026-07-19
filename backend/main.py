from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from api.verification import router as verification_router
from api.dashboard import router as dashboard_router
from api.chat import router as chat_router


# -----------------------------
# Create FastAPI App
# -----------------------------

app = FastAPI(
    title="SmartGov AI API",
    version="1.0.0"
)

# -----------------------------
# CORS
# -----------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Routers
# -----------------------------
app.include_router(chat_router)
app.include_router(verification_router)
app.include_router(dashboard_router)

# -----------------------------
# Paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent
FRONTEND_DIR = PROJECT_DIR / "frontend"
REPORTS_DIR = BASE_DIR / "reports"
# -----------------------------
# Static Files
# -----------------------------

app.mount(
    "/assets",
    StaticFiles(directory=FRONTEND_DIR / "assets"),
    name="assets"
)

app.mount(
    "/reports",
    StaticFiles(directory=REPORTS_DIR),
    name="reports"
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
    return FileResponse(FRONTEND_DIR / "ai_assistant.html")


@app.get("/services")
def services():
    return FileResponse(FRONTEND_DIR / "services.html")