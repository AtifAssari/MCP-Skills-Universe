---
title: python-development
url: https://skills.sh/moizibnyousaf/ai-agent-skills/python-development
---

# python-development

skills/moizibnyousaf/ai-agent-skills/python-development
python-development
Installation
$ npx skills add https://github.com/moizibnyousaf/ai-agent-skills --skill python-development
SKILL.md
Python Development
Project Setup
Modern Python Project Structure
my-project/
├── src/
│   └── my_project/
│       ├── __init__.py
│       ├── main.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── pyproject.toml
├── README.md
└── .gitignore

pyproject.toml
[project]
name = "my-project"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "fastapi>=0.100.0",
    "pydantic>=2.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "ruff>=0.1.0",
    "mypy>=1.0",
]

[tool.ruff]
line-length = 88
select = ["E", "F", "I", "N", "W"]

[tool.mypy]
strict = true

Type Hints
from typing import TypeVar, Generic
from collections.abc import Sequence

T = TypeVar('T')

def process_items(items: Sequence[str]) -> list[str]:
    return [item.upper() for item in items]

class Repository(Generic[T]):
    def get(self, id: int) -> T | None: ...
    def save(self, item: T) -> T: ...

Async Patterns
import asyncio
from collections.abc import AsyncIterator

async def fetch_all(urls: list[str]) -> list[dict]:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_one(session, url) for url in urls]
        return await asyncio.gather(*tasks)

async def stream_data() -> AsyncIterator[bytes]:
    async with aiofiles.open('large_file.txt', 'rb') as f:
        async for chunk in f:
            yield chunk

FastAPI Patterns
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    email: str
    name: str

class UserResponse(BaseModel):
    id: int
    email: str
    name: str

@app.post("/users", response_model=UserResponse)
async def create_user(
    user: UserCreate,
    db: Database = Depends(get_db)
) -> UserResponse:
    result = await db.users.create(user.model_dump())
    return UserResponse(**result)

Testing
import pytest
from unittest.mock import AsyncMock, patch

@pytest.fixture
def mock_db():
    db = AsyncMock()
    db.users.get.return_value = {"id": 1, "name": "Test"}
    return db

@pytest.mark.asyncio
async def test_get_user(mock_db):
    result = await get_user(1, db=mock_db)
    assert result["name"] == "Test"
    mock_db.users.get.assert_called_once_with(1)

Best Practices
Use ruff for linting and formatting
Use mypy with strict mode
Prefer pathlib.Path over os.path
Use dataclasses or Pydantic for data structures
Use asyncio for I/O-bound operations
Use contextlib.asynccontextmanager for async resources
Weekly Installs
8
Repository
moizibnyousaf/a…t-skills
GitHub Stars
1.0K
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass