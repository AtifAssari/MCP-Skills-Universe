---
rating: ⭐⭐⭐
title: python-backend
url: https://skills.sh/jiatastic/open-python-skills/python-backend
---

# python-backend

skills/jiatastic/open-python-skills/python-backend
python-backend
Installation
$ npx skills add https://github.com/jiatastic/open-python-skills --skill python-backend
Summary

Production-ready Python backend patterns for FastAPI, SQLAlchemy, and Upstash integrations.

Covers async-first REST API development with FastAPI, including dependency injection, Pydantic validation, and structured project organization
Implements authentication patterns for JWT/OAuth2, password hashing, CORS, and API key management
Provides SQLAlchemy async database setup with transactions, eager loading, and migration strategies
Includes Redis/Upstash caching, rate limiting with sliding windows, and QStash background job patterns
Offers code quality guidance for refactoring AI-generated Python and optimizing backend performance
SKILL.md
python-backend

Production-ready Python backend patterns for FastAPI, SQLAlchemy, and Upstash.

When to Use This Skill
Building REST APIs with FastAPI
Implementing JWT/OAuth2 authentication
Setting up SQLAlchemy async databases
Integrating Redis/Upstash caching and rate limiting
Refactoring AI-generated Python code
Designing API patterns and project structure
Core Principles
Async-first - Use async/await for I/O operations
Type everything - Pydantic models for validation
Dependency injection - Use FastAPI's Depends()
Fail fast - Validate early, use HTTPException
Security by default - Never trust user input
Quick Patterns
Project Structure
src/
├── auth/
│   ├── router.py      # endpoints
│   ├── schemas.py     # pydantic models
│   ├── models.py      # db models
│   ├── service.py     # business logic
│   └── dependencies.py
├── posts/
│   └── ...
├── config.py
├── database.py
└── main.py

Async Routes
# BAD - blocks event loop
@router.get("/")
async def bad():
    time.sleep(10)  # Blocking!

# GOOD - runs in threadpool
@router.get("/")
def good():
    time.sleep(10)  # OK in sync function

# BEST - non-blocking
@router.get("/")
async def best():
    await asyncio.sleep(10)  # Non-blocking

Pydantic Validation
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr
    username: str = Field(min_length=3, max_length=50, pattern="^[a-zA-Z0-9_]+$")
    age: int = Field(ge=18)

Dependency Injection
async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    payload = decode_token(token)
    user = await get_user(payload["sub"])
    if not user:
        raise HTTPException(401, "User not found")
    return user

@router.get("/me")
async def get_me(user: User = Depends(get_current_user)):
    return user

SQLAlchemy Async
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

engine = create_async_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session

Redis Caching
from upstash_redis import Redis

redis = Redis.from_env()

@app.get("/data/{id}")
def get_data(id: str):
    cached = redis.get(f"data:{id}")
    if cached:
        return cached
    data = fetch_from_db(id)
    redis.setex(f"data:{id}", 600, data)
    return data

Rate Limiting
from upstash_ratelimit import Ratelimit, SlidingWindow

ratelimit = Ratelimit(
    redis=Redis.from_env(),
    limiter=SlidingWindow(max_requests=10, window=60),
)

@app.get("/api/resource")
def protected(request: Request):
    result = ratelimit.limit(request.client.host)
    if not result.allowed:
        raise HTTPException(429, "Rate limit exceeded")
    return {"data": "..."}

Reference Documents

For detailed patterns, see:

Document	Content
references/fastapi_patterns.md	Project structure, async, Pydantic, dependencies, testing
references/security_patterns.md	JWT, OAuth2, password hashing, CORS, API keys
references/database_patterns.md	SQLAlchemy async, transactions, eager loading, migrations
references/upstash_patterns.md	Redis, rate limiting, QStash background jobs
Resources
FastAPI Documentation
SQLAlchemy 2.0 Documentation
Upstash Documentation
Pydantic Documentation
Weekly Installs
1.3K
Repository
jiatastic/open-…n-skills
GitHub Stars
4
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass