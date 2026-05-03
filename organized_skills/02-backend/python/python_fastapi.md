---
rating: ⭐⭐⭐
title: python:fastapi
url: https://skills.sh/martinffx/claude-code-atelier/python:fastapi
---

# python:fastapi

skills/martinffx/claude-code-atelier/python:fastapi
python:fastapi
Installation
$ npx skills add https://github.com/martinffx/claude-code-atelier --skill python:fastapi
SKILL.md
FastAPI - Modern Python Web APIs

FastAPI is a modern, fast web framework for building APIs with Python, using standard Python type hints. FastAPI automatically validates requests, generates OpenAPI documentation, and provides excellent developer experience.

Quick Start
Basic Application
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="My API",
    description="API for my application",
    version="1.0.0",
)

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/items", response_model=Item)
def create_item(item: Item):
    return item


Run with:

uvicorn main:app --reload

Core Concepts
Request & Response Models

Use Pydantic models for automatic validation and serialization:

from pydantic import BaseModel, EmailStr, Field

class CreateUserRequest(BaseModel):
    email: EmailStr
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(ge=18, le=120)

class UserResponse(BaseModel):
    id: int
    email: str
    name: str
    model_config = {"from_attributes": True}  # Enable ORM mode

@app.post("/users", response_model=UserResponse)
def create_user(user: CreateUserRequest):
    """Request validated, response serialized automatically"""
    return user


See references/validation.md for detailed validation patterns including custom validators and field constraints.

Routers for Organization

Split routes across routers for clean organization:

# routers/users.py
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def list_users():
    ...

@router.post("/")
def create_user(user: CreateUserRequest):
    ...

# main.py
app.include_router(users.router)

Dependency Injection

FastAPI's core feature for managing dependencies like database sessions and authentication:

from fastapi import Depends
from sqlalchemy.orm import Session

def get_db() -> Session:
    """Database session dependency"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
def list_users(db: Session = Depends(get_db)):
    """db automatically injected"""
    return db.query(User).all()


See references/dependencies.md for advanced patterns including auth services, scoped dependencies, and dependency classes.

Error Handling
HTTP Exceptions
from fastapi import HTTPException

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

Custom Exception Handlers
from fastapi import Request
from fastapi.responses import JSONResponse

class BusinessError(Exception):
    def __init__(self, message: str):
        self.message = message

@app.exception_handler(BusinessError)
async def business_error_handler(request: Request, exc: BusinessError):
    return JSONResponse(
        status_code=400,
        content={"error": exc.message},
    )

Project Structure
my-api/
├── main.py                   # FastAPI app
├── routers/                  # Route handlers
│   ├── users.py
│   └── products.py
├── schemas/                  # Pydantic models
│   ├── users.py
│   └── products.py
├── services/                 # Business logic
│   └── users.py
├── repositories/             # Data access
│   └── users.py
└── dependencies.py           # Dependency injection

Reference Materials

Detailed patterns for common scenarios:

Validation: references/validation.md - Field constraints, custom validators, model validation
Dependencies: references/dependencies.md - Auth services, scoped dependencies, advanced injection patterns
Middleware: references/middleware.md - CORS, custom middleware, request/response processing
API Design: references/api-design.md - REST naming, pagination, OpenAPI customization, status codes
Best Practices
Use response_model - Always define explicit response schemas
Validate inputs - Use Pydantic models with constraints
Dependency injection - Manage sessions, auth, and cross-cutting concerns
Router organization - Split routes by resource/domain
Error handling - Use HTTP exceptions and custom handlers appropriately
Type hints - FastAPI uses them for both validation and documentation
Weekly Installs
11
Repository
martinffx/claud…-atelier
GitHub Stars
20
First Seen
Feb 16, 2026