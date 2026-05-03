---
title: frontend-routing
url: https://skills.sh/aj-geddes/useful-ai-prompts/frontend-routing
---

# frontend-routing

skills/aj-geddes/useful-ai-prompts/frontend-routing
frontend-routing
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill frontend-routing
SKILL.md
Frontend Routing
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement client-side routing with navigation, lazy loading, protected routes, and state management for multi-page single-page applications.

When to Use
Multi-page navigation
URL-based state management
Protected/guarded routes
Lazy loading of components
Query parameter handling
Quick Start

Minimal working example:

// App.tsx
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { Layout } from './components/Layout';
import { Home } from './pages/Home';
import { NotFound } from './pages/NotFound';
import { useAuth } from './hooks/useAuth';
import React from 'react';

// Lazy loaded components
const Dashboard = React.lazy(() => import('./pages/Dashboard'));
const UserProfile = React.lazy(() => import('./pages/UserProfile'));
const Settings = React.lazy(() => import('./pages/Settings'));

// Protected route wrapper
const ProtectedRoute: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const { isAuthenticated } = useAuth();

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  return <>{children}</>;
};

export const App: React.FC = () => {
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
React Router v6	React Router v6
Vue Router 4	Vue Router 4
Angular Routing	Angular Routing
Query Parameter Handling	Query Parameter Handling
Route Transition Effects	Route Transition Effects
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
280
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