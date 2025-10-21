import os
import httpx
from typing import List, Dict
from app.core.config import settings

OPENAI_URL = "https://api.openai.com/v1/chat/completions"
DEFAULT_MODEL = "gpt-3.5-turbo"

async def get_chat_completion(messages: List[Dict]) -> Dict:
    headers = {
        "Authorization": f"Bearer {settings.OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": DEFAULT_MODEL,
        "messages": messages,
        "temperature": 0.2,
        "max_tokens": 800
    }
    async with httpx.AsyncClient(timeout=30.0) as client:
        r = await client.post(OPENAI_URL, json=payload, headers=headers)
        r.raise_for_status()
        data = r.json()
        # extract assistant content if available
        try:
            content = data["choices"][0]["message"]["content"]
        except Exception:
            content = ""
        return {"text": content, "raw": data}