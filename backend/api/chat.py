from fastapi import APIRouter
from pydantic import BaseModel
from services.alchemyst_service import ask_alchemyst

router = APIRouter(prefix="/api", tags=["AI Assistant"])


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = ask_alchemyst(request.message)

        return {
            "success": True,
            "reply": response
        }

    except Exception as e:
        return {
            "success": False,
            "reply": str(e)
        }