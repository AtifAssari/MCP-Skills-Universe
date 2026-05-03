---
title: n8n-expression-syntax
url: https://skills.sh/czlonkowski/n8n-skills/n8n-expression-syntax
---

# n8n-expression-syntax

skills/czlonkowski/n8n-skills/n8n-expression-syntax
n8n-expression-syntax
Installation
$ npx skills add https://github.com/czlonkowski/n8n-skills --skill n8n-expression-syntax
Summary

Write correct n8n expressions with double braces, proper variable syntax, and webhook data access patterns.

Use {{}} syntax for all dynamic content; access current node data with $json, other nodes with $node["Node Name"], and webhook payloads from $json.body (not root)
Node names are case-sensitive and require quotes; field names with spaces use bracket notation like $json['field name']
Code nodes use direct JavaScript access without {{}} braces; expressions don't work in webhook paths or credential fields
Common mistakes include missing braces, incorrect webhook data paths, and double-wrapping with nested {{}}
SKILL.md
n8n Expression Syntax

Expert guide for writing correct n8n expressions in workflows.

Expression Format

All dynamic content in n8n uses double curly braces:

{{expression}}


Examples:

✅ {{$json.email}}
✅ {{$json.body.name}}
✅ {{$node["HTTP Request"].json.data}}
❌ $json.email  (no braces - treated as literal text)
❌ {$json.email}  (single braces - invalid)

Core Variables
$json - Current Node Output

Access data from the current node:

{{$json.fieldName}}
{{$json['field with spaces']}}
{{$json.nested.property}}
{{$json.items[0].name}}

$node - Reference Other Nodes

Access data from any previous node:

{{$node["Node Name"].json.fieldName}}
{{$node["HTTP Request"].json.data}}
{{$node["Webhook"].json.body.email}}


Important:

Node names must be in quotes
Node names are case-sensitive
Must match exact node name from workflow
$now - Current Timestamp

Access current date/time:

{{$now}}
{{$now.toFormat('yyyy-MM-dd')}}
{{$now.toFormat('HH:mm:ss')}}
{{$now.plus({days: 7})}}

$env - Environment Variables

Access environment variables:

{{$env.API_KEY}}
{{$env.DATABASE_URL}}


Warning: Some n8n instances have N8N_BLOCK_ENV_ACCESS_IN_NODE enabled, which blocks $env access entirely. If $env returns errors, use alternative approaches:

Store values in credentials instead
Use a Set node with manually entered values
Pass values through webhook query parameters
🚨 CRITICAL: Webhook Data Structure

Most Common Mistake: Webhook data is NOT at the root!

Webhook Node Output Structure
{
  "headers": {...},
  "params": {...},
  "query": {...},
  "body": {           // ⚠️ USER DATA IS HERE!
    "name": "John",
    "email": "john@example.com",
    "message": "Hello"
  }
}

Correct Webhook Data Access
❌ WRONG: {{$json.name}}
❌ WRONG: {{$json.email}}

✅ CORRECT: {{$json.body.name}}
✅ CORRECT: {{$json.body.email}}
✅ CORRECT: {{$json.body.message}}


Why: Webhook node wraps incoming data under .body property to preserve headers, params, and query parameters.

Common Patterns
Access Nested Fields
// Simple nesting
{{$json.user.email}}

// Array access
{{$json.data[0].name}}
{{$json.items[0].id}}

// Bracket notation for spaces
{{$json['field name']}}
{{$json['user data']['first name']}}

Reference Other Nodes
// Node without spaces
{{$node["Set"].json.value}}

// Node with spaces (common!)
{{$node["HTTP Request"].json.data}}
{{$node["Respond to Webhook"].json.message}}

// Webhook node
{{$node["Webhook"].json.body.email}}

Combine Variables
// Concatenation (automatic)
Hello {{$json.body.name}}!

// In URLs
https://api.example.com/users/{{$json.body.user_id}}

// In object properties
{
  "name": "={{$json.body.name}}",
  "email": "={{$json.body.email}}"
}

When NOT to Use Expressions
❌ Code Nodes

Code nodes use direct JavaScript access, NOT expressions!

// ❌ WRONG in Code node
const email = '={{$json.email}}';
const name = '{{$json.body.name}}';

// ✅ CORRECT in Code node
const email = $json.email;
const name = $json.body.name;

// Or using Code node API
const email = $input.item.json.email;
const allItems = $input.all();

❌ Webhook Paths
// ❌ WRONG
path: "{{$json.user_id}}/webhook"

// ✅ CORRECT
path: "user-webhook"  // Static paths only

❌ Credential Fields
// ❌ WRONG
apiKey: "={{$env.API_KEY}}"

// ✅ CORRECT
Use n8n credential system, not expressions

Validation Rules
1. Always Use {{}}

Expressions must be wrapped in double curly braces.

❌ $json.field
✅ {{$json.field}}

2. Use Quotes for Spaces and Special Characters

Field or node names with spaces, diacritics, or special characters require bracket notation:

❌ {{$json.field name}}
✅ {{$json['field name']}}

❌ {{$node.HTTP Request.json}}
✅ {{$node["HTTP Request"].json}}

// Bracket notation is mandatory for keys with special characters
✅ {{$json['Gross Price w/o shipment']}}
✅ {{$json['Cena brutto zł']}}

3. Match Exact Node Names

Node references are case-sensitive:

❌ {{$node["http request"].json}}  // lowercase
❌ {{$node["Http Request"].json}}  // wrong case
✅ {{$node["HTTP Request"].json}}  // exact match

4. No Nested {{}}

Don't double-wrap expressions:

❌ {{{$json.field}}}
✅ {{$json.field}}

Common Mistakes

For complete error catalog with fixes, see COMMON_MISTAKES.md

Quick Fixes
Mistake	Fix
$json.field	{{$json.field}}
{{$json.field name}}	{{$json['field name']}}
{{$node.HTTP Request}}	{{$node["HTTP Request"]}}
{{{$json.field}}}	{{$json.field}}
{{$json.name}} (webhook)	{{$json.body.name}}
'={{$json.email}}' (Code node)	$json.email
Working Examples

For real workflow examples, see EXAMPLES.md

Example 1: Webhook to Slack

Webhook receives:

{
  "body": {
    "name": "John Doe",
    "email": "john@example.com",
    "message": "Hello!"
  }
}


In Slack node text field:

New form submission!

Name: {{$json.body.name}}
Email: {{$json.body.email}}
Message: {{$json.body.message}}

Example 2: HTTP Request to Email

HTTP Request returns:

{
  "data": {
    "items": [
      {"name": "Product 1", "price": 29.99}
    ]
  }
}


In Email node (reference HTTP Request):

Product: {{$node["HTTP Request"].json.data.items[0].name}}
Price: ${{$node["HTTP Request"].json.data.items[0].price}}

Example 3: Format Timestamp
// Current date
{{$now.toFormat('yyyy-MM-dd')}}
// Result: 2025-10-20

// Time
{{$now.toFormat('HH:mm:ss')}}
// Result: 14:30:45

// Full datetime
{{$now.toFormat('yyyy-MM-dd HH:mm')}}
// Result: 2025-10-20 14:30

Data Type Handling
Arrays
// First item
{{$json.users[0].email}}

// Array length
{{$json.users.length}}

// Last item
{{$json.users[$json.users.length - 1].name}}

Objects
// Dot notation (no spaces)
{{$json.user.email}}

// Bracket notation (with spaces or dynamic)
{{$json['user data'].email}}

Strings
// Concatenation (automatic)
Hello {{$json.name}}!

// String methods
{{$json.email.toLowerCase()}}
{{$json.name.toUpperCase()}}

Numbers
// Direct use
{{$json.price}}

// Math operations
{{$json.price * 1.1}}  // Add 10%
{{$json.quantity + 5}}

Advanced Patterns
Conditional Content
// Ternary operator
{{$json.status === 'active' ? 'Active User' : 'Inactive User'}}

// Default values
{{$json.email || 'no-email@example.com'}}

Date Manipulation
// Add days
{{$now.plus({days: 7}).toFormat('yyyy-MM-dd')}}

// Subtract hours
{{$now.minus({hours: 24}).toISO()}}

// Set specific date
{{DateTime.fromISO('2025-12-25').toFormat('MMMM dd, yyyy')}}

String Manipulation
// Substring
{{$json.email.substring(0, 5)}}

// Replace
{{$json.message.replace('old', 'new')}}

// Split and join
{{$json.tags.split(',').join(', ')}}

Debugging Expressions
Test in Expression Editor
Click field with expression
Open expression editor (click "fx" icon)
See live preview of result
Check for errors highlighted in red
Common Error Messages

"Cannot read property 'X' of undefined" → Parent object doesn't exist → Check your data path

"X is not a function" → Trying to call method on non-function → Check variable type

Expression shows as literal text → Missing {{ }} → Add curly braces

Expression Helpers
Available Methods

String:

.toLowerCase(), .toUpperCase()
.trim(), .replace(), .substring()
.split(), .includes()

Array:

.length, .map(), .filter()
.find(), .join(), .slice()

DateTime (Luxon):

.toFormat(), .toISO(), .toLocal()
.plus(), .minus(), .set()

Number:

.toFixed(), .toString()
Math operations: +, -, *, /, %
Best Practices
✅ Do
Always use {{ }} for dynamic content
Use bracket notation for field names with spaces
Reference webhook data from .body
Use $node for data from other nodes
Test expressions in expression editor
❌ Don't
Don't use expressions in Code nodes
Don't forget quotes around node names with spaces
Don't double-wrap with extra {{ }}
Don't assume webhook data is at root (it's under .body!)
Don't use expressions in webhook paths or credentials
Related Skills
n8n MCP Tools Expert: Learn how to validate expressions using MCP tools
n8n Workflow Patterns: See expressions in real workflow examples
n8n Node Configuration: Understand when expressions are needed
Summary

Essential Rules:

Wrap expressions in {{ }}
Webhook data is under .body
No {{ }} in Code nodes
Quote node names with spaces
Node names are case-sensitive

Most Common Mistakes:

Missing {{ }} → Add braces
{{$json.name}} in webhooks → Use {{$json.body.name}}
{{$json.email}} in Code → Use $json.email
{{$node.HTTP Request}} → Use {{$node["HTTP Request"]}}

For more details, see:

COMMON_MISTAKES.md - Complete error catalog
EXAMPLES.md - Real workflow examples

Need Help? Reference the n8n expression documentation or use n8n-mcp validation tools to check your expressions.

Weekly Installs
2.6K
Repository
czlonkowski/n8n-skills
GitHub Stars
4.7K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass