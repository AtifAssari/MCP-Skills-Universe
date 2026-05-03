---
title: implementing-new-features
url: https://skills.sh/streamlit/streamlit/implementing-new-features
---

# implementing-new-features

skills/streamlit/streamlit/implementing-new-features
implementing-new-features
Installation
$ npx skills add https://github.com/streamlit/streamlit --skill implementing-new-features
SKILL.md
New Feature Implementation Guide

For understanding the underlying architecture (backend runtime, frontend rendering, WebSocket communication, element tree), see the understanding-streamlit-architecture skill.

Most features need implementation in three areas:

Backend: lib/streamlit/
Frontend: frontend/
Protobufs: proto/

New features should include:

Python unit tests in lib/tests
Vitest unit tests
E2E Playwright tests in e2e_playwright/
Order of Implementation

Protobuf changes in proto/ then run make protobuf

New elements: add to proto/streamlit/proto/Element.proto

Backend in lib/streamlit/

New elements: add to lib/streamlit/__init__.py

Python unit tests in lib/tests

Run: uv run pytest lib/tests/streamlit/the_test_name.py
New elements: add to lib/tests/streamlit/element_mocks.py

Frontend in frontend/

New elements: add to frontend/lib/src/components/core/Block/ElementNodeRenderer.tsx

Vitest tests in *.test.tsx

Run: cd frontend && yarn vitest lib/src/components/elements/NewElement/NewElement.test.tsx

E2E Playwright tests in e2e_playwright/

Run: make run-e2e-test e2e_playwright/name_of_the_test.py

Autofix formatting and linting: make autofix

Verify the implementation: make check

Weekly Installs
68
Repository
streamlit/streamlit
GitHub Stars
44.4K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass