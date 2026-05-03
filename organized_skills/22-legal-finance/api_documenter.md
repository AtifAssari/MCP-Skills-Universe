---
rating: ⭐⭐⭐
title: api-documenter
url: https://skills.sh/charon-fan/agent-playbook/api-documenter
---

# api-documenter

skills/charon-fan/agent-playbook/api-documenter
api-documenter
Installation
$ npx skills add https://github.com/charon-fan/agent-playbook --skill api-documenter
SKILL.md
API Documenter

Specialist in creating comprehensive API documentation using OpenAPI/Swagger specifications.

When This Skill Activates

Activates when you:

Ask to document an API
Create OpenAPI/Swagger specs
Need API reference documentation
Mention "API docs"
OpenAPI Specification Structure
openapi: 3.0.3
info:
  title: API Title
  version: 1.0.0
  description: API description
servers:
  - url: https://example.com/api/v1
paths:
  /users:
    get:
      summary: List users
      operationId: listUsers
      tags:
        - users
      parameters: []
      responses:
        '200':
          description: Successful response
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
      properties:
        id:
          type: string
        name:
          type: string

Endpoint Documentation

For each endpoint, document:

Required Fields
summary: Brief description
operationId: Unique identifier
description: Detailed explanation
tags: For grouping
responses: All possible responses
Recommended Fields
parameters: All parameters with details
requestBody: For POST/PUT/PATCH
security: Authentication requirements
deprecated: If applicable
Example
/users/{id}:
  get:
    summary: Get a user by ID
    operationId: getUserById
    description: Retrieves a single user by their unique identifier
    tags:
      - users
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: string
        description: The user ID
    responses:
      '200':
        description: User found
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/User'
      '404':
        description: User not found
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Error'

Schema Documentation
Best Practices
Use references for shared schemas
Add descriptions to all properties
Specify format for strings (email, uuid, date-time)
Add examples for complex schemas
Mark required fields
Example
components:
  schemas:
    User:
      type: object
      required:
        - id
        - email
      properties:
        id:
          type: string
          format: uuid
          description: Unique user identifier
          example: "550e8400-e29b-41d4-a716-446655440000"
        email:
          type: string
          format: email
          description: User's email address
          example: "user@example.com"
        createdAt:
          type: string
          format: date-time
          description: Account creation timestamp

Authentication Documentation

Document auth requirements:

security:
  - bearerAuth: []

components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: Use your JWT token from /auth/login

Error Responses

Standard error format:

components:
  schemas:
    Error:
      type: object
      properties:
        error:
          type: string
          description: Error message
        code:
          type: string
          description: Application-specific error code
        details:
          type: object
          description: Additional error details


Common HTTP status codes:

200: Success
201: Created
204: No Content
400: Bad Request
401: Unauthorized
403: Forbidden
404: Not Found
409: Conflict
422: Unprocessable Entity
500: Internal Server Error
Scripts

Generate OpenAPI spec from code:

python scripts/generate_openapi.py


Validate OpenAPI spec:

python scripts/validate_openapi.py openapi.yaml

References
references/openapi-template.yaml - OpenAPI template
references/examples/ - API documentation examples
OpenAPI Specification
Weekly Installs
446
Repository
charon-fan/agen…playbook
GitHub Stars
49
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass