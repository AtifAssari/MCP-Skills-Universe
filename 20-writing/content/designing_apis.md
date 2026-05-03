---
title: designing-apis
url: https://skills.sh/nguyenhuuca/assessment/designing-apis
---

# designing-apis

skills/nguyenhuuca/assessment/designing-apis
designing-apis
Installation
$ npx skills add https://github.com/nguyenhuuca/assessment --skill designing-apis
SKILL.md
Designing APIs
Workflows
 Resources: Identify resources and relationships
 Endpoints: Define URL structure and methods
 Request/Response: Define payloads and schemas
 Errors: Define error responses
 Document: Create OpenAPI spec
REST Principles
Resource Naming
Use nouns, not verbs: /users not /getUsers
Use plural: /users not /user
Use kebab-case: /user-profiles not /userProfiles
Nest for relationships: /users/{id}/orders
HTTP Methods
Method	Purpose	Idempotent
GET	Read	Yes
POST	Create	No
PUT	Replace	Yes
PATCH	Update	Yes
DELETE	Remove	Yes
Status Codes
Code	Meaning
200	Success
201	Created
204	No Content
400	Bad Request
401	Unauthorized
403	Forbidden
404	Not Found
409	Conflict
422	Unprocessable Entity
500	Internal Server Error
Error Response Format
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Request validation failed",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ]
  }
}

Versioning
URL Versioning (Recommended)
GET /api/v1/users
GET /api/v2/users

Header Versioning
GET /api/users
Accept: application/vnd.api+json;version=1

Pagination
{
  "data": [...],
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total": 100,
    "total_pages": 5
  }
}

OpenAPI Example
openapi: 3.0.0
info:
  title: Users API
  version: 1.0.0
paths:
  /users:
    get:
      summary: List users
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/User'

Weekly Installs
11
Repository
nguyenhuuca/assessment
GitHub Stars
24
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass