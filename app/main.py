from fastapi import FastAPI
from app.api import health, chat
from app.core.config import settings
from app.db import init_db

app = FastAPI(title="revolutionary - backend (FastAPI)")

app.include_router(health.router, prefix="/api")
app.include_router(chat.router, prefix="/api")

@app.on_event("startup")
def on_startup():
    # initialize DB (creates tables for SQLModel models)
    init_db()

@app.get("/")
async def root():
    return {"service": "revolutionary-backend", "env": settings.environment}