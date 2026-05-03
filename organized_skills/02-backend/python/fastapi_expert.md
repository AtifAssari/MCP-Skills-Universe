---
rating: ⭐⭐⭐
title: fastapi-expert
url: https://skills.sh/bilalmk/todo_correct/fastapi-expert
---

# fastapi-expert

skills/bilalmk/todo_correct/fastapi-expert
fastapi-expert
Installation
$ npx skills add https://github.com/bilalmk/todo_correct --skill fastapi-expert
SKILL.md
FastAPI Expert

Production-ready FastAPI knowledge covering basic API development to planet-scale deployment.

Quick Start

Create a basic FastAPI application:

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Run with: uvicorn main:app --reload

Core Topics
1. Database Operations

See: references/database.md

SQLModel integration (recommended ORM)
CRUD operations with dependency injection
Async database operations
Connection pooling
Migrations with Alembic
Neon Serverless PostgreSQL setup
2. Security & Authentication

See: references/security.md

OAuth2 with password flow
JWT token-based authentication
Password hashing with Argon2
OAuth2 scopes for permissions
CORS configuration
Rate limiting
API key authentication
Security best practices
3. Deployment & Scalability

See: references/deployment.md

Docker containerization
Kubernetes deployment
Production server configuration (Uvicorn + Gunicorn)
Horizontal pod autoscaling
Performance monitoring with Prometheus
Caching strategies with Redis
Platform-specific guides (Vercel, AWS, GCP)
4. Advanced Features

See: references/advanced.md

Dependency injection patterns
Custom middleware
WebSocket support
Background tasks
Request/response models with validation
Streaming responses
File uploads
Testing strategies
Event handlers
Project Templates

Use the provided production-ready templates in assets/:

FastAPI Project Structure
assets/project-template/
├── main.py           # Application entry point
├── config.py         # Settings management
├── database.py       # Database setup
├── models.py         # SQLModel models
└── auth.py           # Authentication logic


Copy the template to start a new project:

cp -r assets/project-template/* your-project/

Docker Deployment

Use assets/Dockerfile for containerizing your application with multi-stage builds and security best practices.

Kubernetes Deployment

Use assets/kubernetes-deployment.yaml for deploying to Kubernetes with:

Deployment with 3 replicas
Service with LoadBalancer
Horizontal Pod Autoscaler
Health and readiness probes
Common Patterns
Database CRUD with Session Dependency
from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, select

SessionDep = Annotated[Session, Depends(get_session)]

@app.get("/users/{user_id}")
def get_user(user_id: int, session: SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

Protected Routes with Authentication
from typing import Annotated
from fastapi import Depends

CurrentUser = Annotated[User, Depends(get_current_active_user)]

@app.get("/users/me")
async def read_users_me(current_user: CurrentUser):
    return current_user

Background Tasks
from fastapi import BackgroundTasks

@app.post("/send-email/")
async def send_email(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email_task, email)
    return {"message": "Email queued"}

Best Practices Checklist
Development
 Use type hints everywhere
 Implement request/response models with Pydantic
 Use dependency injection for shared logic
 Add proper error handling with HTTPException
 Use async/await for I/O operations
Security
 Hash passwords with Argon2
 Use JWT for authentication
 Implement OAuth2 scopes for authorization
 Configure CORS properly
 Store secrets in environment variables
 Enable HTTPS in production
Database
 Use SQLModel for ORM
 Implement connection pooling
 Use migrations (Alembic)
 Leverage dependency injection for sessions
 Add database indexes for performance
Deployment
 Multi-stage Dockerfile
 Non-root container user
 Health check endpoints
 Resource limits in Kubernetes
 Horizontal pod autoscaling
 Prometheus metrics
 Structured logging
Scalability Strategies
Async Operations

Always use async def for endpoints that perform I/O:

@app.get("/users/")
async def get_users():
    users = await fetch_from_db()
    return users

Caching

Implement Redis caching for frequently accessed data:

@cache(expire=600)
async def expensive_operation():
    # Heavy computation
    return result

Background Processing

Offload long-running tasks:

background_tasks.add_task(process_data, data)

Connection Pooling

Configure database connection pools:

engine = create_engine(
    DATABASE_URL,
    pool_size=20,
    max_overflow=10,
    pool_timeout=30
)

Troubleshooting
Performance Issues
Enable Prometheus metrics to identify bottlenecks
Use async operations for all I/O
Implement caching with Redis
Optimize database queries (indexes, eager loading)
Enable GZip compression
Authentication Errors
Verify JWT secret key matches
Check token expiration time
Ensure password hashing is consistent
Validate CORS configuration
Database Connection Issues
Check connection string format
Verify connection pool settings
Test database reachability
Review firewall rules
Production Deployment Flow
Develop locally with auto-reload
Test with TestClient and pytest
Build Docker image
Push to container registry
Deploy to Kubernetes cluster
Monitor with Prometheus/Grafana
Scale with HPA based on metrics
Example: Complete CRUD API
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Annotated

# Database setup
engine = create_engine("sqlite:///database.db")

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

# Model
class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str | None = None

# App
app = FastAPI()

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

# CRUD endpoints
@app.post("/items/", response_model=Item)
def create_item(item: Item, session: SessionDep):
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@app.get("/items/", response_model=list[Item])
def read_items(session: SessionDep, skip: int = 0, limit: int = 100):
    items = session.exec(select(Item).offset(skip).limit(limit)).all()
    return items

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, session: SessionDep):
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.patch("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item_update: Item, session: SessionDep):
    db_item = session.get(Item, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    item_data = item_update.model_dump(exclude_unset=True)
    for key, value in item_data.items():
        setattr(db_item, key, value)

    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item

@app.delete("/items/{item_id}")
def delete_item(item_id: int, session: SessionDep):
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    session.delete(item)
    session.commit()
    return {"ok": True}


This skill provides everything needed to build production-ready FastAPI applications from basic CRUD to planet-scale deployments.

Weekly Installs
15
Repository
bilalmk/todo_correct
GitHub Stars
1
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass