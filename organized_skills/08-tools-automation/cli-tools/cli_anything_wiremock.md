---
rating: ⭐⭐⭐
title: cli-anything-wiremock
url: https://skills.sh/hkuds/cli-anything/cli-anything-wiremock
---

# cli-anything-wiremock

skills/hkuds/cli-anything/cli-anything-wiremock
cli-anything-wiremock
Installation
$ npx skills add https://github.com/hkuds/cli-anything --skill cli-anything-wiremock
SKILL.md
Overview

cli-anything-wiremock is a command-line interface that wraps the WireMock Admin REST API (/__admin/). It allows agents and developers to manage HTTP stub mappings, inspect served requests, control stateful scenarios, and record real backend traffic — all from the terminal or from agent tool calls.

WireMock is commonly used in integration testing environments to replace real HTTP backends with controllable mock responses.

Command Groups
stub — Manage HTTP stub mappings
Command	Description
stub list	List all registered stubs
stub get <id>	Get details of a specific stub by UUID
stub create <json>	Create a stub from a JSON string
stub quick M URL S	Quickly create a stub: METHOD URL STATUS_CODE
stub delete <id>	Delete a stub by UUID
stub reset	Reset all stubs to the defaults on disk
stub save	Persist in-memory stubs to disk
stub import <file>	Import stubs from a JSON file
request — Inspect served requests
Command	Description
request list	List recent served requests
request find <pattern>	Find requests matching a JSON pattern
request count <pattern>	Count requests matching a JSON pattern
request unmatched	List requests that matched no stub (404s)
request reset	Clear the request journal
scenario — Stateful scenario management
Command	Description
scenario list	List all scenarios and current states
scenario set N S	Set scenario NAME to STATE
scenario reset	Reset all scenarios to their initial state
record — Record traffic from a real backend
Command	Description
record start <url>	Start proxying + recording to TARGET_URL
record stop	Stop recording, return captured stubs
record status	Check if currently recording
record snapshot	Snapshot in-memory requests as stubs
settings — Global server settings
Command	Description
settings get	Get current global WireMock settings
settings version	Show WireMock server version
Top-level commands
Command	Description
status	Check if WireMock is running
reset	Full reset: stubs + requests + scenarios
shutdown	Gracefully shut down the WireMock server
Key Examples
# Check connectivity
cli-anything-wiremock status

# Create a stub using quick form
cli-anything-wiremock stub quick GET /api/users 200 --body '[{"id":1}]'

# Create a stub using full JSON
cli-anything-wiremock stub create '{
  "request": {"method": "POST", "url": "/api/orders"},
  "response": {"status": 201, "body": "{\"id\":99}"}
}'

# Verify a POST was made exactly once
cli-anything-wiremock --json request count '{"method":"POST","url":"/api/orders"}'
# → {"count": 1}

# Scenario: advance state
cli-anything-wiremock scenario set "cart-flow" "item-added"

# Record a real backend
cli-anything-wiremock record start https://api.example.com
# ... make requests ...
cli-anything-wiremock record stop

Agent Guidance
Always use --json in agent contexts

Use --json for all invocations in scripts or agent tool calls. JSON output varies by command type (these are distinct response types, not an envelope wrapping all responses):

# Data commands return raw WireMock API JSON directly:
cli-anything-wiremock --json stub quick GET /api/hello 200 --body '{"hello":"world"}'
# → {"id": "abc-123", "request": {...}, "response": {...}, ...}

cli-anything-wiremock --json stub list
# → {"mappings": [...], "total": N}

# Void commands (delete, reset, save) return:
# → {"status": "ok"}

# Errors return:
# → {"status": "error", "message": "Connection refused"}

Connection via environment

Set connection params via environment variables before calling any command:

export WIREMOCK_HOST=localhost
export WIREMOCK_PORT=8080

Workflow pattern for test verification
Set up stubs before running the system under test:
cli-anything-wiremock --json stub quick POST /api/payment 200 --body '{"success":true}'

Run the system under test.
Verify interactions:
cli-anything-wiremock --json request count '{"method":"POST","url":"/api/payment"}'

Clean up:
cli-anything-wiremock reset

Error handling

Non-zero exit code on all errors. In --json mode, errors return {"status": "error", "message": "..."}. Success returns the raw WireMock API response.

Weekly Installs
86
Repository
hkuds/cli-anything
GitHub Stars
33.2K
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn