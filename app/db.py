from sqlmodel import SQLModel, create_engine, Session
from app.core.config import settings
from app import models

# Using SQLModel synchronous engine for simplicity in scaffold.
# For production with async DB drivers use SQLAlchemy Async or another async ORM.
engine = create_engine(settings.DATABASE_URL, echo=False, connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {})

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session