---
title: react-component-architecture
url: https://skills.sh/aj-geddes/useful-ai-prompts/react-component-architecture
---

# react-component-architecture

skills/aj-geddes/useful-ai-prompts/react-component-architecture
react-component-architecture
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill react-component-architecture
SKILL.md
React Component Architecture
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Build scalable, maintainable React components using modern patterns including functional components, hooks, composition, and TypeScript for type safety.

When to Use
Component library design
Large-scale React applications
Reusable UI patterns
Custom hooks development
Performance optimization
Quick Start

Minimal working example:

// Button.tsx
import React, { useState, useCallback } from 'react';

interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  onClick?: () => void;
  children: React.ReactNode;
}

export const Button: React.FC<ButtonProps> = ({
  variant = 'primary',
  size = 'md',
  disabled = false,
  onClick,
  children
}) => {
  const variantStyles = {
    primary: 'bg-blue-500 hover:bg-blue-600',
    secondary: 'bg-gray-500 hover:bg-gray-600',
    danger: 'bg-red-500 hover:bg-red-600'
  };

  const sizeStyles = {
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Functional Component with Hooks	Functional Component with Hooks
Custom Hooks Pattern	Custom Hooks Pattern
Composition Pattern	Composition Pattern
Higher-Order Component (HOC)	Higher-Order Component (HOC)
Render Props Pattern	Render Props Pattern
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
401
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