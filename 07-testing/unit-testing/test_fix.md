---
title: test-fix
url: https://skills.sh/pv-udpv/pplx-sdk/test-fix
---

# test-fix

skills/pv-udpv/pplx-sdk/test-fix
test-fix
Installation
$ npx skills add https://github.com/pv-udpv/pplx-sdk --skill test-fix
SKILL.md
test-fix

Diagnose and fix failing tests following pplx-sdk testing conventions.

When to use

Use this skill when pytest tests fail and you need to identify the root cause and apply the correct fix.

Instructions
Read the failure output carefully — identify the root cause (assertion error, import error, missing mock, timeout, etc.).
Locate the source code the test exercises — the fix may be in the source, not the test itself.
Follow existing patterns: Look at passing tests in the same file for mock setup and assertion style.
Preserve test intent: Never weaken assertions to make tests pass. Fix the underlying issue.
Run the fix: Execute pytest tests/<file> -v to confirm the fix works.
Project Testing Conventions
Framework: pytest with pytest-asyncio and pytest-httpx
HTTP mocking: Use HTTPXMock from pytest-httpx for transport tests
Fixtures: Common fixtures in tests/conftest.py — mock_auth_token, mock_context_uuid, mock_frontend_uuid, mock_backend_uuid
Test naming: test_<what>_<behavior> (e.g., test_http_transport_auth_error)
Structure: Arrange-Act-Assert pattern
No docstrings needed in test files (per ruff config)
Exception Testing

Verify the exception hierarchy when testing error cases:

# AuthenticationError is a TransportError which is a PerplexitySDKError
with pytest.raises(AuthenticationError) as exc_info:
    transport.request("GET", "/api/test")
assert exc_info.value.status_code == 401

Common Issues
Symptom	Likely Cause	Fix
ImportError	Module restructured	Update import path
AttributeError	Model field renamed	Check domain/models.py
HTTPXMock not matching	URL or method mismatch	Verify mock URL matches request
TransportError vs RuntimeError	Exception type changed	Use pplx_sdk.core.exceptions types
Weekly Installs
17
Repository
pv-udpv/pplx-sdk
First Seen
Feb 8, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass