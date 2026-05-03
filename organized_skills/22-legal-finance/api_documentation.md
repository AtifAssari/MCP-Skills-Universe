---
rating: ⭐⭐
title: api documentation
url: https://skills.sh/danhvb/my-ba-skills/api-documentation
---

# api documentation

skills/danhvb/my-ba-skills/API Documentation
API Documentation
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'API Documentation'
SKILL.md
API Documentation Skill
Purpose

Define integration requirements and document API specifications to ensure smooth communication between systems (e.g., Frontend to Backend, or Service to Service).

When to Use
Designing new API endpoints (e.g., FRS for Backend).
Integrating with 3rd party services (e.g., Stripe, SendGrid).
Documenting public APIs for partners.
Defining payload structures for developers.
Key API Concepts for BAs
1. Protocols
REST (Representational State Transfer): Most common. Resource-based.
SOAP: Older, XML-based. Heavy enterprise use.
GraphQL: Flexible, query-based. Client asks for exactly what it needs.
2. HTTP Methods (Verbs)
GET: Retrieve data (Read).
POST: Create new data (Create).
PUT: Update/Replace full data (Update).
PATCH: Update partial data (Update).
DELETE: Remove data (Delete).
3. Status Codes
200 OK: Success.
201 Created: Success (new resource made).
400 Bad Request: Client error (invalid input).
401 Unauthorized: Authentication missing/failed.
403 Forbidden: Authentication passed, but permission denied.
404 Not Found: Resource doesn't exist.
500 Internal Server Error: Backend crashed.
Documentation Structure (Swagger/OpenAPI Style)
Required Sections per Endpoint
Title & Method: GET /api/v1/users/{userId}
Summary: One-line description of what it does.
Parameters:
Path Params: Required ID in URL (e.g., {userId}).
Query Params: Filter/Sort limits (e.g., ?limit=10&role=admin).
Body: JSON payload (for POST/PUT).
Headers: Auth tokens, Content-Type.
Response Examples:
Success (200) JSON body.
Error (4xx/5xx) JSON body.
Business Rules: Constraints, logic, side effects.
API Specification Template (Simple)
Endpoint: Create New Order

Method: POST URL: /api/v1/orders Description: Creates a new customer order and reserves inventory.

Request Headers:

Authorization: Bearer <token>
Content-Type: application/json

Request Body (JSON):

{
  "customerId": "uuid-string",
  "items": [
    {
      "productId": "uuid-string",
      "quantity": 2
    }
  ],
  "shippingAddress": {
    "street": "123 Main St",
    "city": "Startown"
  }
}


Constraints:

quantity must be > 0.
customerId must be active.
Max 20 items per order.

Success Response (201 Created):

{
  "orderId": "ord-12345",
  "status": "PENDING",
  "totalAmount": 150.00,
  "createdAt": "2026-01-21T10:00:00Z"
}


Error Responses:

400 Bad Request: "Invalid Quantity" or "Product Out of Stock".
401 Unauthorized: Token expired.
Mapping Integrations (Data Mapping)

When connecting System A to System B, create a Mapping Table:

Source Field (System A)	Type	Transformation	Destination Field (System B)	Type	Notes
first_name	Str	Concat	FullName	Str	A.first + " " + A.last
last_name	Str	(above)	-	-	
dob	Date	Format YYYY-MM-DD	BirthDate	Str	B requires string format
status	Enum	Map 'Active'->1	IsActive	Bool	Logic mapping
Tools
Swagger / OpenAPI: Standard for dev docs.
Postman: Testing API calls.
Stoplight: Visual API design.
Lark Docs / Markdown: Writing specs for BRD/FRS.
Best Practices
Be Consistent: Use ISO 8601 for dates (YYYY-MM-DDThh:mm:ssZ).
Authentication: Explicitly state how auth works (API Key vs OAuth).
Pagination: Don't return 1 million records. Specify default limits (limit=20).
Error Messages: Define clear human-readable error messages.
Reference
RESTful API Design Guide.
OpenAPI Specification (OAS).
Weekly Installs
–
Repository
danhvb/my-ba-skills
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass