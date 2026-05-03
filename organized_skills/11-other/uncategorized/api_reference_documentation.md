---
rating: ⭐⭐
title: api-reference-documentation
url: https://skills.sh/secondsky/claude-skills/api-reference-documentation
---

# api-reference-documentation

skills/secondsky/claude-skills/api-reference-documentation
api-reference-documentation
Installation
$ npx skills add https://github.com/secondsky/claude-skills --skill api-reference-documentation
SKILL.md
API Reference Documentation

Create comprehensive API documentation for developer integration.

OpenAPI 3.0 Specification
openapi: 3.0.3
info:
  title: E-Commerce API
  version: 1.0.0
  description: API for managing products and orders
  contact:
    email: api@example.com

servers:
  - url: https://api.example.com/v1
    description: Production
  - url: https://staging-api.example.com/v1
    description: Staging

security:
  - bearerAuth: []

paths:
  /products:
    get:
      summary: List products
      tags: [Products]
      parameters:
        - name: limit
          in: query
          schema: { type: integer, default: 20 }
        - name: category
          in: query
          schema: { type: string }
      responses:
        '200':
          description: Product list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ProductList'

components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

  schemas:
    Product:
      type: object
      required: [id, name, price]
      properties:
        id: { type: string, format: uuid }
        name: { type: string, maxLength: 200 }
        price: { type: number, minimum: 0 }
        description: { type: string }

Documentation Checklist
 All endpoints documented with examples
 Authentication methods explained
 Error responses specified
 Rate limits documented
 Pagination explained
 Webhooks documented (if applicable)
 SDK examples in multiple languages
Best Practices
Use OpenAPI 3.0+ specification
Include request/response examples
Document all parameters and headers
Provide authentication examples
Enable interactive API exploration
Maintain version documentation
Include migration guides for breaking changes
Tools
Swagger Editor / Swagger UI
Redoc
Postman Documentation
Stoplight
Weekly Installs
173
Repository
secondsky/claude-skills
GitHub Stars
129
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass