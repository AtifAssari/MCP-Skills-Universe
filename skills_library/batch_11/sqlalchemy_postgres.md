---
title: sqlalchemy-postgres
url: https://skills.sh/cfircoo/claude-code-toolkit/sqlalchemy-postgres
---

# sqlalchemy-postgres

skills/cfircoo/claude-code-toolkit/sqlalchemy-postgres
sqlalchemy-postgres
Installation
$ npx skills add https://github.com/cfircoo/claude-code-toolkit --skill sqlalchemy-postgres
SKILL.md

<essential_principles>

SQLAlchemy 2.0 + Pydantic + PostgreSQL Best Practices

This skill provides expert guidance for building production-ready database layers.

Stack
SQLAlchemy 2.0 with async support (asyncpg driver)
Pydantic v2 for validation and serialization
Alembic for migrations
PostgreSQL only
Core Principles

1. Separation of Concerns

models/       # SQLAlchemy ORM models (database layer)
schemas/      # Pydantic schemas (API layer)
repositories/ # Data access patterns
services/     # Business logic


2. Type Safety First Always use SQLAlchemy 2.0 style with Mapped[] type annotations:

from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))


3. Async by Default Use async engine and sessions for FastAPI:

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
engine = create_async_engine("postgresql+asyncpg://...")


4. Pydantic-SQLAlchemy Bridge Keep models and schemas separate but mappable:

# Schema reads from ORM
class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)


5. Repository Pattern Abstract database operations for testability and clean code. </essential_principles>

Setup database layer - Initialize SQLAlchemy + Pydantic + Alembic from scratch
Define models - Create SQLAlchemy models with Pydantic schemas
Create migration - Generate and manage Alembic migrations
Query patterns - Async CRUD, joins, eager loading, optimization
Full implementation - Complete database layer for a feature

Auto-detection triggers (use this skill when user mentions):

database, db, sqlalchemy, postgres, postgresql
model, migration, alembic
repository, crud, query
async session, connection pool

<reference_index>

Domain Knowledge
Reference	Purpose
references/best-practices.md	Production patterns, security, performance
references/patterns.md	Repository, Unit of Work, common queries
references/async-patterns.md	Async session management, FastAPI integration
</reference_index>	

<workflows_index>

Workflow	Purpose
workflows/setup-database.md	Initialize complete database layer
workflows/define-models.md	Create models + schemas + relationships
workflows/create-migration.md	Alembic migration workflow
workflows/query-patterns.md	CRUD operations and optimization
</workflows_index>	

<quick_reference>

File Structure
src/
├── db/
│   ├── __init__.py
│   ├── base.py          # DeclarativeBase
│   ├── session.py       # Engine + async session factory
│   └── dependencies.py  # FastAPI dependency
├── models/
│   ├── __init__.py
│   └── user.py          # SQLAlchemy models
├── schemas/
│   ├── __init__.py
│   └── user.py          # Pydantic schemas
├── repositories/
│   ├── __init__.py
│   ├── base.py          # Generic repository
│   └── user.py          # User repository
└── alembic/
    ├── alembic.ini
    ├── env.py
    └── versions/

Essential Imports
# Models
from sqlalchemy import String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase

# Async
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

# Pydantic
from pydantic import BaseModel, ConfigDict, Field

Connection String
# PostgreSQL async
DATABASE_URL = "postgresql+asyncpg://user:pass@localhost:5432/dbname"


</quick_reference>

<success_criteria> Database layer is complete when:

 Async engine and session factory configured
 Base model with common fields (id, created_at, updated_at)
 Models use Mapped[] type annotations
 Pydantic schemas with from_attributes=True
 Alembic configured for async
 Repository pattern implemented
 FastAPI dependency for session injection
 Connection pooling configured for production </success_criteria>
Weekly Installs
206
Repository
cfircoo/claude-…-toolkit
GitHub Stars
17
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass