---
title: form-validation
url: https://skills.sh/aj-geddes/useful-ai-prompts/form-validation
---

# form-validation

skills/aj-geddes/useful-ai-prompts/form-validation
form-validation
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill form-validation
SKILL.md
Form Validation
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement comprehensive form validation including client-side validation, server-side synchronization, and real-time error feedback with TypeScript type safety.

When to Use
User input validation
Form submission handling
Real-time error feedback
Complex validation rules
Multi-step forms
Quick Start

Minimal working example:

// types/form.ts
export interface LoginFormData {
  email: string;
  password: string;
  rememberMe: boolean;
}

export interface RegisterFormData {
  email: string;
  password: string;
  confirmPassword: string;
  name: string;
  terms: boolean;
}

// components/LoginForm.tsx
import { useForm, SubmitHandler } from 'react-hook-form';
import { LoginFormData } from '../types/form';

const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export const LoginForm: React.FC = () => {
  const {
    register,
    handleSubmit,
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
React Hook Form with TypeScript	React Hook Form with TypeScript
Formik with Yup Validation	Formik with Yup Validation
Vue Vee-Validate	Vue Vee-Validate
Custom Validator Hook	Custom Validator Hook
Server-Side Validation Integration	Server-Side Validation Integration
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
289
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