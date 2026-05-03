---
title: metronic-module
url: https://skills.sh/harishafeez1/providr-react/metronic-module
---

# metronic-module

skills/harishafeez1/providr-react/metronic-module
metronic-module
Installation
$ npx skills add https://github.com/harishafeez1/providr-react --skill metronic-module
SKILL.md
Metronic Provider Portal Module Creator

This skill helps you create production-ready modules for the Providr Provider Portal using the Metronic Tailwind React theme with established patterns and conventions.

Quick Start

When creating a new module, you will:

Follow the established file structure patterns
Use Metronic theme components and layouts
Integrate with Shadcn UI component library
Apply consistent naming conventions
Implement responsive design with dark mode support
Documentation Structure

This skill is organized into focused reference documents:

📁 Patterns & Structure
File structure patterns
Directory organization
Naming conventions
Barrel exports
Module creation checklist
🎨 Components & UI
Layout components (Container, Toolbar, etc.)
Common component patterns (Cards, Buttons, Badges)
Data tables with DataGrid
Forms with Formik + Yup validation
Dialogs and modals
Dropdown menus
KeenIcons usage
🎨 Styling Conventions
Tailwind CSS patterns
Metronic-specific classes
Dark mode implementation
Responsive design breakpoints
Color system and theming
🔌 API Integration
React Query patterns
Data layer components
Error handling
Loading states
🛣️ Routing & Menu
Route configuration
Protected routes
Sidebar menu setup
Permission-based access
📦 Templates

Ready-to-use component templates:

page-template.tsx - Main page component
content-template.tsx - Content wrapper
form-template.tsx - Form with validation
table-template.tsx - Data table component
📚 Examples

Complete working examples:

Full module implementation
Real-world use cases
Tech Stack
Core Technologies
Theme: Metronic (Tailwind CSS version)
CSS Framework: Tailwind CSS v3.4.14
Component Library: Shadcn UI (Radix UI primitives)
Icons: KeenIcons (ki-filled, ki-outline, ki-duotone, ki-solid)
Layout: Demo1 (sidebar + fixed header)
TypeScript: Fully typed components
Libraries & Tools
UI Components: Shadcn UI in src/components/ui/
Charts: ApexCharts
Forms: Formik + Yup validation
Notifications: Sonner + Notistack
Data Tables: TanStack React Table (DataGrid)
State Management: React Query (server state) + Context API (UI state)
Best Practices
TypeScript First - Always use TypeScript with proper type definitions
Component Reuse - Use existing Shadcn UI components, don't create custom ones
Follow Patterns - Reference similar modules (incidents, service-offerings) in the codebase
Dark Mode - Always implement dark mode with Tailwind dark: classes
Responsive Design - Test on mobile, tablet, and desktop viewports
Loading & Error States - Handle all data states properly
Accessibility - Use semantic HTML and ARIA attributes
Icons - Use only KeenIcons, not other icon libraries
Absolute Imports - Use @/ for project-relative imports
Permissions - Implement role-based access control where needed
Quick Reference: Component Imports
// Layout
import { Container } from '@/components/Container';
import { Toolbar, ToolbarHeading, ToolbarActions } from '@/layouts/demo1';

// UI Components
import { Button } from '@/components/ui/button';
import { Card, CardHeader, CardBody } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Input } from '@/components/ui/input';
import { Dialog, DialogContent } from '@/components/ui/dialog';

// Icons
import { KeenIcon } from '@/components/keenicons';

// Data & Forms
import { DataGrid } from '@/components/data-grid';
import { Formik, Form, Field } from 'formik';
import { useQuery, useMutation } from '@tanstack/react-query';

Workflow

When asked to create a new module:

Understand Requirements

What is the module's purpose?
What data does it handle?
What permissions are needed?

Review Patterns

Check patterns.md for structure
Look at existing similar modules in the codebase

Build Components

Use templates from templates/
Follow examples in components.md
Apply styling from styling.md

Add Integration

Implement data layer per api-integration.md
Configure routes per routing-menu.md

Finalize

Test responsive design
Verify dark mode
Check permissions
Add to navigation menu
Getting Help
For file structure questions → See patterns.md
For UI component usage → See components.md
For styling help → See styling.md
For data fetching → See api-integration.md
For routing setup → See routing-menu.md
For ready-to-use code → See templates/
For complete examples → See examples/

Remember: Always check existing modules in the codebase for real-world reference implementations before creating new patterns.

Weekly Installs
21
Repository
harishafeez1/pr…dr-react
GitHub Stars
1
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass