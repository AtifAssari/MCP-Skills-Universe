---
title: frontend-testing
url: https://skills.sh/aj-geddes/useful-ai-prompts/frontend-testing
---

# frontend-testing

skills/aj-geddes/useful-ai-prompts/frontend-testing
frontend-testing
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill frontend-testing
SKILL.md
Frontend Testing
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Build comprehensive test suites for frontend applications including unit tests, integration tests, and end-to-end tests with proper coverage and assertions.

When to Use
Component testing
Integration testing
End-to-end testing
Regression prevention
Quality assurance
Test-driven development
Quick Start

Minimal working example:

// Button.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { Button } from './Button';

describe('Button Component', () => {
  it('renders button with text', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByRole('button')).toHaveTextContent('Click me');
  });

  it('calls onClick handler when clicked', () => {
    const handleClick = jest.fn();
    render(<Button onClick={handleClick}>Click</Button>);

    fireEvent.click(screen.getByRole('button'));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('disables button when disabled prop is true', () => {
    render(<Button disabled>Click me</Button>);
    expect(screen.getByRole('button')).toBeDisabled();
  });

  it('applies variant styles correctly', () => {
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Jest Unit Testing (React)	Jest Unit Testing (React)
React Testing Library Integration Tests	React Testing Library Integration Tests
Vitest for Vue Testing	Vitest for Vue Testing
Cypress E2E Testing	Cypress E2E Testing
Test Coverage Configuration	Test Coverage Configuration
Best Practices
✅ DO
Follow established patterns and conventions
Write clean, maintainable code
Add appropriate documentation
Test thoroughly before deploying
❌ DON'T
Skip testing or validation
Ignore error handling
Hard-code configuration values
Weekly Installs
293
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass