from fastapi import APIRouter, Depends, HTTPException
from app.schemas import ChatRequest, ChatResponse
from app.utils.openai_client import get_chat_completion
from app.core.config import settings

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest):
    if not settings.OPENAI_API_KEY:
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY not configured")
    # Basic usage: pass single user message and optional history
    messages = []
    for turn in req.history or []:
        # history items expected as {"role":"user"/"assistant","content": "..."}
        messages.append(turn)
    messages.append({"role": "user", "content": req.message})
    resp = await get_chat_completion(messages)
    return {"reply": resp.get("text", ""), "raw": resp}