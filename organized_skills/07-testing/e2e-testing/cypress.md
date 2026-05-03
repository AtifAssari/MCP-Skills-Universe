---
rating: ⭐⭐
title: cypress
url: https://skills.sh/bobmatnyc/claude-mpm-skills/cypress
---

# cypress

skills/bobmatnyc/claude-mpm-skills/cypress
cypress
Installation
$ npx skills add https://github.com/bobmatnyc/claude-mpm-skills --skill cypress
SKILL.md
Cypress (E2E + Component Testing)
Overview

Cypress runs browser automation with first-class network control, time-travel debugging, and a strong local dev workflow. Use it for critical path E2E tests and for component tests when browser-level rendering matters.

Quick Start
Install and open
npm i -D cypress
npx cypress open

Minimal spec
// cypress/e2e/health.cy.ts
describe("health", () => {
  it("loads", () => {
    cy.visit("/");
    cy.contains("Hello").should("be.visible");
  });
});

Core Patterns
1) Stable selectors

Prefer data-testid (or data-cy) attributes for selectors. Avoid brittle CSS chains and text-only selectors for critical interactions.

<button data-testid="save-user">Save</button>

cy.get('[data-testid="save-user"]').click();

2) Deterministic waiting (avoid fixed sleeps)

Wait on app-visible conditions or network aliases rather than cy.wait(1000).

cy.intercept("GET", "/api/users/*").as("getUser");
cy.visit("/users/1");
cy.wait("@getUser");
cy.get('[data-testid="user-email"]').should("not.be.empty");

3) Network control with cy.intercept

Stub responses for deterministic tests and speed. Keep a small set of “real backend” smoke tests separate.

cy.intercept("GET", "/api/users/1", {
  statusCode: 200,
  body: { id: "1", email: "a@example.com" },
}).as("getUser");

4) Authentication strategies

Prefer cy.session to cache login for speed and stability.

// cypress/support/commands.ts
Cypress.Commands.add("login", () => {
  cy.session("user", () => {
    cy.request("POST", "/api/auth/login", {
      email: "test@example.com",
      password: "password",
    });
  });
});

// e2e spec
beforeEach(() => {
  cy.login();
});

Component Testing

Run component tests to validate UI behavior in isolation while keeping browser rendering.

npx cypress open --component

// cypress/component/Button.cy.tsx
import React from "react";
import Button from "../../src/Button";

describe("<Button />", () => {
  it("clicks", () => {
    cy.mount(<Button onClick={cy.stub().as("onClick")}>Save</Button>);
    cy.contains("Save").click();
    cy.get("@onClick").should("have.been.calledOnce");
  });
});

CI Patterns
Artifacts (videos/screenshots)

Store artifacts for failed runs and keep videos optional to reduce storage.

// cypress.config.ts
import { defineConfig } from "cypress";

export default defineConfig({
  video: false,
  screenshotOnRunFailure: true,
  retries: { runMode: 2, openMode: 0 },
});

Parallelization (Cypress Cloud)

Parallelize long E2E suites via Cypress Cloud when runtime dominates feedback loops.

Anti-Patterns
Use cy.wait(1000) as a synchronization mechanism.
Select elements via deep CSS paths.
Mix heavy network stubbing with “real backend” assertions in the same spec.
Depend on test order; isolate state with cy.session and per-test setup.
Troubleshooting
Symptom: flaky click or element not found

Actions:

Add a data-testid hook for the element.
Assert visibility before interaction (should("be.visible")).
Wait on network alias for the data that renders the element.
Symptom: tests fail only in CI

Actions:

Increase run-mode retries and record screenshots on failure.
Verify viewport and baseUrl config match CI environment.
Eliminate reliance on local-only seed data; create data via API calls.
Resources
Cypress docs: https://docs.cypress.io/
Best practices: https://docs.cypress.io/guides/references/best-practices
Weekly Installs
457
Repository
bobmatnyc/claud…m-skills
GitHub Stars
40
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass