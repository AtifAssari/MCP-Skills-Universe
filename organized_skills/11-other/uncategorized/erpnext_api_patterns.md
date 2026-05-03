---
rating: ⭐⭐⭐
title: erpnext-api-patterns
url: https://skills.sh/openaec-foundation/erpnext_anthropic_claude_development_skill_package/erpnext-api-patterns
---

# erpnext-api-patterns

skills/openaec-foundation/erpnext_anthropic_claude_development_skill_package/erpnext-api-patterns
erpnext-api-patterns
Installation
$ npx skills add https://github.com/openaec-foundation/erpnext_anthropic_claude_development_skill_package --skill erpnext-api-patterns
SKILL.md
ERPNext API Patterns
API Type Decision Tree
What do you want to achieve?
│
├─► CRUD operations on documents
│   └─► REST API: /api/resource/{doctype}
│
├─► Call custom business logic
│   └─► RPC API: /api/method/{path}
│
├─► Notify external systems on events
│   └─► Configure Webhooks
│
└─► Client-side server calls (JavaScript)
    └─► frappe.call() or frappe.xcall()

Quick Reference
Authentication Headers
# Token Auth (RECOMMENDED for integrations)
headers = {
    'Authorization': 'token api_key:api_secret',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# Bearer Token (OAuth2)
headers = {'Authorization': 'Bearer {access_token}'}

REST API CRUD
Operation	Method	Endpoint
List	GET	/api/resource/{doctype}
Create	POST	/api/resource/{doctype}
Read	GET	/api/resource/{doctype}/{name}
Update	PUT	/api/resource/{doctype}/{name}
Delete	DELETE	/api/resource/{doctype}/{name}
Filter Operators
# Basic filters
filters = [["status", "=", "Open"]]
filters = [["amount", ">", 1000]]
filters = [["status", "in", ["Open", "Pending"]]]
filters = [["date", "between", ["2024-01-01", "2024-12-31"]]]
filters = [["reference", "is", "set"]]  # NOT NULL

RPC Method Call
# Server-side: mark with decorator
@frappe.whitelist()
def my_function(param1, param2):
    return {"result": "value"}

# API call
POST /api/method/my_app.api.my_function
{"param1": "value1", "param2": "value2"}

Client-Side Calls (JavaScript)
// Async/await pattern (RECOMMENDED)
const result = await frappe.xcall('my_app.api.my_function', {
    param1: 'value'
});

// Promise pattern
frappe.call({
    method: 'my_app.api.my_function',
    args: {param1: 'value'},
    freeze: true,
    freeze_message: __('Processing...')
}).then(r => console.log(r.message));

Response Structure

REST API Success:

{"data": {...}}


RPC API Success:

{"message": "return_value"}


Error Response:

{
    "exc_type": "ValidationError",
    "_server_messages": "[{\"message\": \"Error details\"}]"
}

HTTP Status Codes
Code	Meaning
200	Success
400	Validation error
401	No authentication
403	No permissions
404	Document not found
417	Server exception
429	Rate limit exceeded
Critical Rules
ALWAYS include Accept: application/json header
ALWAYS add permission checks in whitelisted methods
NEVER hardcode credentials - use frappe.conf
NEVER write SQL injection vulnerable queries
GET for read-only, POST for state-changing operations
Reference Files
File	Contents
authentication-methods.md	Token, Session, OAuth2 implementation
rest-api-reference.md	Complete REST API with filters and pagination
rpc-api-reference.md	Whitelisted methods and frappe.call patterns
webhooks-reference.md	Webhook configuration and security
anti-patterns.md	Common mistakes and fixes
Version Notes (v14 vs v15)
Feature	v14	v15
expand_links parameter	❌	✅
Server Script rate limiting	❌	✅
PKCE for OAuth2	Limited	✅
Weekly Installs
47
Repository
openaec-foundat…_package
GitHub Stars
92
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn