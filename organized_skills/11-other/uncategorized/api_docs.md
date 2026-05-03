---
rating: ⭐⭐
title: api-docs
url: https://skills.sh/langchain-ai/skills-benchmarks/api-docs
---

# api-docs

skills/langchain-ai/skills-benchmarks/api-docs
api-docs
Installation
$ npx skills add https://github.com/langchain-ai/skills-benchmarks --skill api-docs
SKILL.md
API Documentation Standards

Design and document RESTful APIs following industry standards.

OpenAPI Specification

Always document APIs using OpenAPI 3.0+:

openapi: 3.0.3
info:
  title: User API
  version: 1.0.0

paths:
  /users:
    get:
      summary: List users
      parameters:
        - name: limit
          in: query
          schema:
            type: integer
            default: 20
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/User'

components:
  schemas:
    User:
      type: object
      required: [id, email]
      properties:
        id:
          type: string
          format: uuid
        email:
          type: string
          format: email

REST Conventions
Use nouns for resources: /users, /orders
Use HTTP methods correctly: GET, POST, PUT, PATCH, DELETE
Return appropriate status codes: 200, 201, 400, 404, 500
Use pagination for lists: ?page=1&limit=20
Version your API: /v1/users
Error Responses
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input",
    "details": [
      {"field": "email", "message": "Invalid email format"}
    ]
  }
}

Weekly Installs
20
Repository
langchain-ai/sk…nchmarks
GitHub Stars
95
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass