---
rating: ⭐⭐⭐
title: browserwing-executor
url: https://skills.sh/memtensor/memos/browserwing-executor
---

# browserwing-executor

skills/memtensor/memos/browserwing-executor
browserwing-executor
Installation
$ npx skills add https://github.com/memtensor/memos --skill browserwing-executor
SKILL.md
BrowserWing Executor API
Overview

BrowserWing Executor provides comprehensive browser automation capabilities through HTTP APIs. You can control browser navigation, interact with page elements, extract data, and analyze page structure.

API Base URL: http://localhost:8080/api/v1/executor

Authentication: Use X-BrowserWing-Key: <api-key> header or Authorization: Bearer <token>

Core Capabilities
Page Navigation: Navigate to URLs, go back/forward, reload
Element Interaction: Click, type, select, hover on page elements
Data Extraction: Extract text, attributes, values from elements
Accessibility Analysis: Get accessibility snapshot to understand page structure
Advanced Operations: Screenshot, JavaScript execution, keyboard input
Batch Processing: Execute multiple operations in sequence
API Endpoints
1. Discover Available Commands

IMPORTANT: Always call this endpoint first to see all available commands and their parameters.

curl -X GET 'http://localhost:8080/api/v1/executor/help'


Response: Returns complete list of all commands with parameters, examples, and usage guidelines.

Query specific command:

curl -X GET 'http://localhost:8080/api/v1/executor/help?command=extract'

2. Get Accessibility Snapshot

CRITICAL: Always call this after navigation to understand page structure and get element RefIDs.

curl -X GET 'http://localhost:8080/api/v1/executor/snapshot'


Response Example:

{
  "success": true,
  "snapshot_text": "Clickable Elements:\n  @e1 Login (role: button)\n  @e2 Sign Up (role: link)\n\nInput Elements:\n  @e3 Email (role: textbox) [placeholder: your@email.com]\n  @e4 Password (role: textbox)"
}


Use Cases:

Understand what interactive elements are on the page
Get element RefIDs (@e1, @e2, etc.) for precise identification
See element labels, roles, and attributes
The accessibility tree is cleaner than raw DOM and better for LLMs
RefIDs are stable references that work reliably across page changes
3. Common Operations
Navigate to URL
curl -X POST 'http://localhost:8080/api/v1/executor/navigate' \
  -H 'Content-Type: application/json' \
  -d '{"url": "https://example.com"}'

Click Element
curl -X POST 'http://localhost:8080/api/v1/executor/click' \
  -H 'Content-Type: application/json' \
  -d '{"identifier": "@e1"}'


Identifier formats:

RefID (Recommended): @e1, @e2 (from snapshot)
CSS Selector: #button-id, .class-name
XPath: //button[@type='submit']
Text: Login (text content)
Type Text
curl -X POST 'http://localhost:8080/api/v1/executor/type' \
  -H 'Content-Type: application/json' \
  -d '{"identifier": "@e3", "text": "user@example.com"}'

Extract Data
curl -X POST 'http://localhost:8080/api/v1/executor/extract' \
  -H 'Content-Type: application/json' \
  -d '{
    "selector": ".product-item",
    "fields": ["text", "href"],
    "multiple": true
  }'

Wait for Element
curl -X POST 'http://localhost:8080/api/v1/executor/wait' \
  -H 'Content-Type: application/json' \
  -d '{"identifier": ".loading", "state": "hidden", "timeout": 10}'

Batch Operations
curl -X POST 'http://localhost:8080/api/v1/executor/batch' \
  -H 'Content-Type: application/json' \
  -d '{
    "operations": [
      {"type": "navigate", "params": {"url": "https://example.com"}, "stop_on_error": true},
      {"type": "click", "params": {"identifier": "@e1"}, "stop_on_error": true},
      {"type": "type", "params": {"identifier": "@e3", "text": "query"}, "stop_on_error": true}
    ]
  }'

Instructions

Step-by-step workflow:

Discover commands: Call GET /help to see all available operations and their parameters (do this first if unsure).

Navigate: Use POST /navigate to open the target webpage.

Analyze page: Call GET /snapshot to understand page structure and get element RefIDs.

Interact: Use element RefIDs (like @e1, @e2) or CSS selectors to:

Click elements: POST /click
Input text: POST /type
Select options: POST /select
Wait for elements: POST /wait

Extract data: Use POST /extract to get information from the page.

Present results: Format and show extracted data to the user.

Complete Example

User Request: "Search for 'laptop' on example.com and get the first 5 results"

Your Actions:

Navigate to search page:
curl -X POST 'http://localhost:8080/api/v1/executor/navigate' \
  -H 'Content-Type: application/json' \
  -d '{"url": "https://example.com/search"}'

Get page structure to find search input:
curl -X GET 'http://localhost:8080/api/v1/executor/snapshot'


Response shows: @e3 Search (role: textbox) [placeholder: Search...]

Type search query:
curl -X POST 'http://localhost:8080/api/v1/executor/type' \
  -H 'Content-Type: application/json' \
  -d '{"identifier": "@e3", "text": "laptop"}'

Press Enter to submit:
curl -X POST 'http://localhost:8080/api/v1/executor/press-key' \
  -H 'Content-Type: application/json' \
  -d '{"key": "Enter"}'

Wait for results to load:
curl -X POST 'http://localhost:8080/api/v1/executor/wait' \
  -H 'Content-Type: application/json' \
  -d '{"identifier": ".search-results", "state": "visible", "timeout": 10}'

Extract search results:
curl -X POST 'http://localhost:8080/api/v1/executor/extract' \
  -H 'Content-Type: application/json' \
  -d '{
    "selector": ".result-item",
    "fields": ["text", "href"],
    "multiple": true
  }'

Present the extracted data:
Found 15 results for 'laptop':
1. Gaming Laptop - $1299 (https://...)
2. Business Laptop - $899 (https://...)
...

Key Commands Reference
Navigation
POST /navigate - Navigate to URL
POST /go-back - Go back in history
POST /go-forward - Go forward in history
POST /reload - Reload current page
Element Interaction
POST /click - Click element (supports: RefID @e1, CSS selector, XPath, text content)
POST /type - Type text into input (supports: RefID @e3, CSS selector, XPath)
POST /select - Select dropdown option
POST /hover - Hover over element
POST /wait - Wait for element state (visible, hidden, enabled)
POST /press-key - Press keyboard key (Enter, Tab, Ctrl+S, etc.)
Data Extraction
POST /extract - Extract data from elements (supports multiple elements, custom fields)
POST /get-text - Get element text content
POST /get-value - Get input element value
GET /page-info - Get page URL and title
GET /page-text - Get all page text
GET /page-content - Get full HTML
Page Analysis
GET /snapshot - Get accessibility snapshot (⭐ ALWAYS call after navigation)
GET /clickable-elements - Get all clickable elements
GET /input-elements - Get all input elements
Advanced
POST /screenshot - Take page screenshot (base64 encoded)
POST /evaluate - Execute JavaScript code
POST /batch - Execute multiple operations in sequence
POST /scroll-to-bottom - Scroll to page bottom
POST /resize - Resize browser window
POST /tabs - Manage browser tabs (list, new, switch, close)
POST /fill-form - Intelligently fill multiple form fields at once
Debug & Monitoring
GET /console-messages - Get browser console messages (logs, warnings, errors)
GET /network-requests - Get network requests made by the page
POST /handle-dialog - Configure JavaScript dialog (alert, confirm, prompt) handling
POST /file-upload - Upload files to input elements
POST /drag - Drag and drop elements
POST /close-page - Close the current page/tab
Element Identification

You can identify elements using:

RefID (Recommended): @e1, @e2, @e3

Most reliable method - stable across page changes
Get RefIDs from /snapshot endpoint
Valid for 5 minutes after snapshot
Example: "identifier": "@e1"
Works with multi-strategy fallback for robustness

CSS Selector: #id, .class, button[type="submit"]

Standard CSS selectors
Example: "identifier": "#login-button"

XPath: //button[@id='login'], //a[contains(text(), 'Submit')]

XPath expressions for complex queries
Example: "identifier": "//button[@id='login']"

Text Content: Login, Sign Up, Submit

Searches buttons and links with matching text
Example: "identifier": "Login"

ARIA Label: Elements with aria-label attribute

Automatically searched
Guidelines

Before starting:

Call GET /help if you're unsure about available commands or their parameters
Ensure browser is started (if not, it will auto-start on first operation)

During automation:

Always call /snapshot after navigation to get page structure and RefIDs
Prefer RefIDs (like @e1) over CSS selectors for reliability and stability
Re-snapshot after page changes to get updated RefIDs
Use /wait for dynamic content that loads asynchronously
Check element states before interaction (visible, enabled)
Use /batch for multiple sequential operations to improve efficiency

Error handling:

If operation fails, check element identifier and try different format
For timeout errors, increase timeout value
If element not found, call /snapshot again to refresh page structure
Explain errors clearly to user with suggested solutions

Data extraction:

Use fields parameter to specify what to extract: ["text", "href", "src"]
Set multiple: true to extract from multiple elements
Format extracted data in a readable way for user
Complete Workflow Example

Scenario: User wants to login to a website

User: "Please log in to example.com with username 'john' and password 'secret123'"


Your Actions:

Step 1: Navigate to login page

POST http://localhost:8080/api/v1/executor/navigate
{"url": "https://example.com/login"}


Step 2: Get page structure

GET http://localhost:8080/api/v1/executor/snapshot


Response:

Clickable Elements:
  @e1 Login (role: button)

Input Elements:
  @e2 Username (role: textbox)
  @e3 Password (role: textbox)


Step 3: Enter username

POST http://localhost:8080/api/v1/executor/type
{"identifier": "@e2", "text": "john"}


Step 4: Enter password

POST http://localhost:8080/api/v1/executor/type
{"identifier": "@e3", "text": "secret123"}


Step 5: Click login button

POST http://localhost:8080/api/v1/executor/click
{"identifier": "@e1"}


Step 6: Wait for login success (optional)

POST http://localhost:8080/api/v1/executor/wait
{"identifier": ".welcome-message", "state": "visible", "timeout": 10}


Step 7: Inform user

"Successfully logged in to example.com!"

Batch Operation Example

Scenario: Fill out a form with multiple fields

Instead of making 5 separate API calls, use one batch operation:

curl -X POST 'http://localhost:8080/api/v1/executor/batch' \
  -H 'Content-Type: application/json' \
  -d '{
    "operations": [
      {
        "type": "navigate",
        "params": {"url": "https://example.com/form"},
        "stop_on_error": true
      },
      {
        "type": "type",
        "params": {"identifier": "#name", "text": "John Doe"},
        "stop_on_error": true
      },
      {
        "type": "type",
        "params": {"identifier": "#email", "text": "john@example.com"},
        "stop_on_error": true
      },
      {
        "type": "select",
        "params": {"identifier": "#country", "value": "United States"},
        "stop_on_error": true
      },
      {
        "type": "click",
        "params": {"identifier": "#submit"},
        "stop_on_error": true
      }
    ]
  }'

Best Practices
Discovery first: If unsure, call /help or /help?command=<name> to learn about commands
Structure first: Always call /snapshot after navigation to understand the page
Use accessibility indices: They're more reliable than CSS selectors (elements might have dynamic classes)
Wait for dynamic content: Use /wait before interacting with elements that load asynchronously
Batch when possible: Use /batch for multiple sequential operations
Handle errors gracefully: Provide clear explanations and suggestions when operations fail
Verify results: After operations, check if desired outcome was achieved
Common Scenarios
Form Filling
Navigate to form page
Get accessibility snapshot to find input elements and their RefIDs
Use /type for each field: @e1, @e2, etc.
Use /select for dropdowns
Click submit button using its RefID
Data Scraping
Navigate to target page
Wait for content to load with /wait
Use /extract with CSS selector and multiple: true
Specify fields to extract: ["text", "href", "src"]
Search Operations
Navigate to search page
Get accessibility snapshot to locate search input
Type search query into input
Press Enter or click search button
Wait for results
Extract results data
Login Automation
Navigate to login page
Get accessibility snapshot to find RefIDs
Type username: @e2
Type password: @e3
Click login button: @e1
Wait for success indicator
Important Notes
Browser must be running (it will auto-start on first operation if needed)
Operations are executed on the currently active browser tab
Accessibility snapshot updates after each navigation and click operation
All timeouts are in seconds
Use wait_visible: true (default) for reliable element interaction
Replace localhost:8080 with actual API host address
Authentication required: use X-BrowserWing-Key header or JWT token
Troubleshooting

Element not found:

Call /snapshot to see available elements
Try different identifier format (accessibility index, CSS selector, text)
Check if page has finished loading

Timeout errors:

Increase timeout value in request
Check if element actually appears on page
Use /wait with appropriate state before interaction

Extraction returns empty:

Verify CSS selector matches target elements
Check if content has loaded (use /wait first)
Try different extraction fields or type
Quick Reference
# Discover commands
GET localhost:8080/api/v1/executor/help

# Navigate
POST localhost:8080/api/v1/executor/navigate {"url": "..."}

# Get page structure
GET localhost:8080/api/v1/executor/snapshot

# Click element
POST localhost:8080/api/v1/executor/click {"identifier": "@e1"}

# Type text
POST localhost:8080/api/v1/executor/type {"identifier": "@e3", "text": "..."}

# Extract data
POST localhost:8080/api/v1/executor/extract {"selector": "...", "fields": [...], "multiple": true}

Response Format

All operations return:

{
  "success": true,
  "message": "Operation description",
  "timestamp": "2026-01-15T10:30:00Z",
  "data": {
    // Operation-specific data
  }
}


Error response:

{
  "error": "error.operationFailed",
  "detail": "Detailed error message"
}

Weekly Installs
100
Repository
memtensor/memos
GitHub Stars
8.9K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail