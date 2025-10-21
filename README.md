# revolutionary — FastAPI backend scaffold

This is a minimal FastAPI backend scaffold for the "revolutionary" project. It includes:
- FastAPI app structure
- health and simple chat endpoints (OpenAI-compatible wrapper)
- config via environment variables
- PostgreSQL service via docker-compose
- Dockerfile for the web service

Quickstart (local, no remote push required)
1. Create a repository and add these files (or copy them into your existing repo).
2. Create a .env file from .env.example and fill in values:
   - DATABASE_URL (postgresql://postgres:postgres@db:5432/revolutionary)
   - OPENAI_API_KEY (your OpenAI key)
   - SECRET_KEY (random secret for app)
3. Start services:
   docker-compose up -d
4. (Local dev) Install dependencies:
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
5. Run the app:
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
6. Visit http://localhost:8000/docs for automatic API docs.

Notes & next steps
- This scaffold uses a simple OpenAI HTTP client. Swap in your preferred LLM provider/client as needed.
- For production, add migrations (Alembic), more robust connection pooling, authentication (OAuth / JWT / FastAPI Users), rate limits, logging, and secrets management.
- If you'd like, after you make an initial commit on the repo I can push these files and open a PR with a checklist (auth, migrations, vector DB integration, tests).