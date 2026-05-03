---
rating: ⭐⭐⭐
title: flask-api-development
url: https://skills.sh/aj-geddes/useful-ai-prompts/flask-api-development
---

# flask-api-development

skills/aj-geddes/useful-ai-prompts/flask-api-development
flask-api-development
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill flask-api-development
Summary

Build modular Flask REST APIs with blueprints, SQLAlchemy ORM, JWT authentication, and validation.

Covers application setup, database models, JWT authentication, blueprints for modular design, request validation, and configuration management
Includes error handling middleware, CORS support, request ID tracking, and proper HTTP status code responses
Emphasizes input validation, environment-based configuration, and comprehensive logging for production readiness
Provides reference guides and best practices for structuring microservices and lightweight web services
SKILL.md
Flask API Development
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Create efficient Flask APIs with blueprints for modular organization, SQLAlchemy for ORM, JWT authentication, comprehensive error handling, and proper request validation following REST principles.

When to Use
Building RESTful APIs with Flask
Creating microservices with minimal overhead
Implementing lightweight authentication systems
Designing API endpoints with proper validation
Integrating with relational databases
Building request/response handling systems
Quick Start

Minimal working example:

# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///app.db')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'dev-secret')
app.config['JSON_SORT_KEYS'] = False

db = SQLAlchemy(app)
jwt = JWTManager(app)
CORS(app)

# Request ID middleware
@app.before_request
def assign_request_id():
    import uuid
    request.request_id = str(uuid.uuid4())

# Error handlers
@app.errorhandler(400)
def bad_request(error):
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Flask Application Setup	Flask Application Setup
Database Models with SQLAlchemy	Database Models with SQLAlchemy
Authentication and JWT	Authentication and JWT
Blueprints for Modular API Design	Blueprints for Modular API Design
Request Validation	Request Validation
Application Factory and Configuration	Application Factory and Configuration
Best Practices
✅ DO
Use blueprints for modular organization
Implement proper authentication with JWT
Validate all user input
Use SQLAlchemy ORM for database operations
Implement comprehensive error handling
Use pagination for collection endpoints
Log errors and important events
Return appropriate HTTP status codes
Implement CORS properly
Use environment variables for configuration
❌ DON'T
Store secrets in code
Use global variables for shared state
Ignore database transactions
Trust user input without validation
Return stack traces in production
Use mutable default arguments
Forget to handle database connection errors
Implement authentication in route handlers
Weekly Installs
838
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass