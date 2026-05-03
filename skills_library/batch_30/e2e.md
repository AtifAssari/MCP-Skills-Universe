---
title: e2e
url: https://skills.sh/helderberto/skills/e2e
---

# e2e

skills/helderberto/skills/e2e
e2e
Installation
$ npx skills add https://github.com/helderberto/skills --skill e2e
SKILL.md
End-to-End Tests (Cypress)
Detection

Run in parallel:

Check package.json for cypress version
Read cypress.config.ts for baseUrl and test file patterns
Read 1-2 existing test files in cypress/e2e/ to match conventions
Workflow
Read existing tests and config to match project style
Understand the user flow — ask if unclear
Identify selectors (see selectors.md)
Write tests in cypress/e2e/ — one file per flow or feature
Format
describe('login flow', () => {
  beforeEach(() => {
    cy.visit('/login')
  })

  it('logs in with valid credentials', () => {
    cy.findByLabelText('Email').type('user@example.com')
    cy.findByLabelText('Password').type('password')
    cy.findByRole('button', { name: 'Sign in' }).click()
    cy.url().should('include', '/dashboard')
    cy.findByRole('heading', { name: 'Dashboard' }).should('be.visible')
  })

  it('shows error with invalid credentials', () => {
    cy.findByLabelText('Email').type('wrong@example.com')
    cy.findByLabelText('Password').type('wrong')
    cy.findByRole('button', { name: 'Sign in' }).click()
    cy.findByRole('alert').should('contain.text', 'Invalid credentials')
  })
})

Selector priority

Prefer @testing-library/cypress commands when installed:

cy.findByRole('button', { name: 'Submit' }) — best
cy.findByLabelText('Email') — forms
cy.findByText('Welcome') — text content
cy.get('[data-testid="submit"]') — last resort

See selectors.md for full guide.

Rules
Use @testing-library/cypress selectors when available, else cy.get
Use data-testid only as last resort
One logical outcome per it block
Test behavior, not implementation details
Never use cy.wait(<number>) — use cy.findBy* auto-retry instead
Error Handling
If cypress is not in package.json → stop and ask user to install Cypress first
If cypress.config.ts is missing → ask user to run npx cypress open to initialize config
If baseUrl is unreachable → verify the dev server is running before writing tests that require it
Weekly Installs
28
Repository
helderberto/skills
GitHub Stars
8
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass