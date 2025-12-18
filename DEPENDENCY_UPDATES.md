# Dependency Updates - Backend (FastAPI)

Date: 2025-12-18

Container: delivery_tracker_backend

Package updates (pinned to latest compatible versions):
- fastapi==0.115.5
- starlette==0.41.2
- pydantic==2.9.2
- pydantic-settings==2.6.1
- uvicorn[standard]==0.32.1
- httpx==0.27.2
- python-multipart==0.0.17
- itsdangerous==2.2.0
- asyncpg==0.30.0
- loguru==0.7.3
- pytest==8.3.3
- pytest-asyncio==0.24.0
- mypy==1.12.0
- ruff==0.6.9
- black==24.10.0

Notable changes and considerations:
- Pydantic v2 is used. Code must use pydantic.BaseModel (v2) and avoid `from pydantic import BaseSettings` in favor of `pydantic-settings`.
- Starlette is aligned to FastAPI's upper bound. Route decorators and ResponseModel behavior remain compatible.
- uvicorn updated. Use `uvicorn delivery_tracker_backend.main:app --reload` in development.
- mypy/ruff/black versions updated to recent releases; basic configs added in `pyproject.toml`.

Breaking changes requiring follow-up:
- If existing code relied on Pydantic v1 behaviors (validators, .dict() behavior), migrate to v2 equivalents (validators -> field validators, model_dump()).
- If there is database ORM integration (SQLAlchemy, Tortoise, etc.) or other services not yet present, pin their versions and verify compatibility with Pydantic v2 and FastAPI 0.115.x.

Environment Variables:
- No changes made. Settings read from `.env` via `pydantic-settings`.

How to install (backend):
- python -m venv .venv && source .venv/bin/activate
- pip install --upgrade pip
- pip install -r delivery_tracker_backend/requirements.txt
- Run: uvicorn delivery_tracker_backend.main:app --reload
