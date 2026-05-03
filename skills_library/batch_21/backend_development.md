---
title: backend-development
url: https://skills.sh/reynalivan/emmm2/backend-development
---

# backend-development

skills/reynalivan/emmm2/backend-development
backend-development
Installation
$ npx skills add https://github.com/reynalivan/emmm2 --skill backend-development
SKILL.md
Backend Development Skill

Rules for the Rust "Engine" of EMMM2.

1. Core Architecture (The 3-Layer Standard)

Follow Clean Architecture to keep logic testable and decoupled.

Presentation (Commands): src-tauri/src/commands/. Thin wrapper. Deserializes input -> Calls Service -> Serializes Output. NO LOGIC HERE.
Domain (Services): src-tauri/src/services/. Pure Business Logic. Agnostic of Tauri or UI.
Infrastructure (Repositories): src-tauri/src/database/. SQLx queries and OS File I/O.
2. API Design (Tauri Commands)

Treat Commands like REST Endpoints.

Input: Use DTO structs (Data Transfer Objects), not long argument lists.
Output: Always return Result<T, AppError>.
Async: All Commands must be async.
3. Database Patterns (SQLite + SQLx)
Schema: managed via migrations/*.sql.
ID: Use UUID v4 (Text) for universal uniqueness.
Optimization: Use WAL mode and PRAGMA synchronous = NORMAL.
References
Service Pattern
Database & Schema
API Style Guide
Weekly Installs
9
Repository
reynalivan/emmm2
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass