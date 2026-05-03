---
title: backend-dev
url: https://skills.sh/srbhr/resume-matcher/backend-dev
---

# backend-dev

skills/srbhr/resume-matcher/backend-dev
backend-dev
Installation
$ npx skills add https://github.com/srbhr/resume-matcher --skill backend-dev
SKILL.md
Backend Development

Use when creating or modifying FastAPI endpoints, Pydantic schemas, database operations, LLM integrations, or Python service logic.

Before Writing Code
Read docs/agent/architecture/backend-guide.md for architecture
Read docs/agent/apis/front-end-apis.md for API contracts
Read docs/agent/llm-integration.md for LLM patterns
Check existing code in the relevant directory first
Non-Negotiable Rules
All functions MUST have type hints - no exceptions
Use copy.deepcopy() for mutable defaults
Log detailed errors server-side, return generic messages to clients
Use asyncio.Lock() for shared resource initialization
Pass API keys directly to litellm via api_key=, never os.environ
Project Structure
apps/backend/app/
├── main.py          # FastAPI app, CORS, lifespan, routers
├── config.py        # Pydantic BaseSettings from env
├── database.py      # TinyDB wrapper (JSON file storage)
├── llm.py           # LiteLLM wrapper (multi-provider)
├── routers/         # API endpoint handlers
├── services/        # Business logic layer
├── schemas/         # Pydantic request/response models
└── prompts/         # LLM prompt templates (Jinja2)

Patterns
New Endpoint
from fastapi import APIRouter, HTTPException
from app.schemas.my_schema import MyRequest, MyResponse
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1", tags=["my-feature"])

@router.post("/my-endpoint", response_model=MyResponse)
async def create_thing(request: MyRequest) -> MyResponse:
    try:
        result = await process_data(request)
        return result
    except Exception as e:
        logger.error(f"Failed to create thing: {e}")
        raise HTTPException(status_code=500, detail="Operation failed. Please try again.")

New Schema
from pydantic import BaseModel, Field

class MyRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    description: str | None = None

class MyResponse(BaseModel):
    id: str
    name: str
    status: str = "created"

Database Operation
import copy
from app.database import get_db

DEFAULT_DATA = {"sections": [], "metadata": {}}

async def get_or_create(doc_id: str) -> dict:
    db = get_db()
    existing = db.get(doc_id)
    if existing:
        return existing
    data = copy.deepcopy(DEFAULT_DATA)  # ALWAYS deepcopy mutable defaults
    db.insert(data)
    return data

LLM Call
from app.llm import get_completion
from app.config import settings

async def improve_text(text: str) -> str:
    prompt = f"Improve this resume text:\n\n{text}"
    result = await get_completion(
        prompt=prompt,
        model=settings.LLM_MODEL,
        api_key=settings.LLM_API_KEY,  # Pass directly, not via env
        json_mode=True,
    )
    return result

Error Handling Pattern
except Exception as e:
    logger.error(f"Operation failed: {e}")  # Detailed for server logs
    raise HTTPException(
        status_code=500,
        detail="Operation failed. Please try again."  # Generic for client
    )

Checklist
 All functions have type hints
 Mutable defaults use copy.deepcopy()
 Error handling logs details, returns generic messages
 New endpoints registered in main.py router includes
 Schemas defined for all request/response bodies
 API keys passed via api_key= parameter
Weekly Installs
52
Repository
srbhr/resume-matcher
GitHub Stars
26.5K
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail