---
title: a2ui
url: https://skills.sh/kobe4cn/a2ui_skills/a2ui
---

# a2ui

skills/kobe4cn/a2ui_skills/a2ui
a2ui
Installation
$ npx skills add https://github.com/kobe4cn/a2ui_skills --skill a2ui
SKILL.md
A2UI Development Skill

This skill helps you generate A2UI (Agent to UI) protocol compliant code for building rich, interactive user interfaces that AI agents can stream to clients.

Protocol Version

This skill targets A2UI Protocol v0.8 (Stable Release).

Standard Catalog ID: https://github.com/google/A2UI/blob/main/specification/0.8/json/standard_catalog_definition.json

Core Concepts
1. Message Types

A2UI uses four message types in a JSONL stream:

Message	Purpose
surfaceUpdate	Define or update UI components
dataModelUpdate	Populate or update application state
beginRendering	Signal client to start rendering
deleteSurface	Remove a UI surface
2. Adjacency List Model

Components are defined as a flat list with ID references, not nested trees:

{"surfaceUpdate": {"surfaceId": "main", "components": [
  {"id": "root", "component": {"Column": {"children": {"explicitList": ["header", "content"]}}}},
  {"id": "header", "component": {"Text": {"text": {"literalString": "Welcome"}, "usageHint": "h1"}}},
  {"id": "content", "component": {"Text": {"text": {"path": "/user/name"}}}}
]}}

3. Data Binding (BoundValue)

Three patterns for binding values:

// Literal only - static value
{"literalString": "Hello"}

// Path only - dynamic from data model
{"path": "/user/name"}

// Both - initialization shorthand (sets default AND binds)
{"path": "/form/email", "literalString": "user@example.com"}

4. Styles Configuration

Customize appearance in beginRendering:

{"beginRendering": {
  "surfaceId": "main",
  "root": "root",
  "styles": {
    "font": "Roboto",
    "primaryColor": "#1976D2"
  }
}}

Property	Description
font	Primary font family
primaryColor	Theme color (hex format #RRGGBB)
Standard Catalog Components
Layout Components
Row - Horizontal container with distribution and alignment
Column - Vertical container with distribution and alignment
List - Scrollable list with direction (vertical/horizontal)
Card - Material card wrapper with single child
Tabs - Tab navigation with tabItems array
Modal - Dialog with entryPointChild and contentChild
Divider - Separator with axis (horizontal/vertical)
Display Components
Text - Text display with usageHint (h1-h5, caption, body). Supports simple Markdown.
Image - Image with url, fit, usageHint
Icon - Icon from standard set (see components reference)
Video - Video player with url
AudioPlayer - Audio with url and description
Input Components
Button - Clickable with child and action
TextField - Text input with label, textFieldType
CheckBox - Toggle with label and value
DateTimeInput - Date/time picker with enableDate/enableTime
MultipleChoice - Selection with options and maxAllowedSelections
Slider - Range input with minValue/maxValue
Component Weight

Use weight on components inside Row/Column for flex layout:

{"id": "sidebar", "weight": 1, "component": {"Column": {...}}},
{"id": "main", "weight": 3, "component": {"Column": {...}}}

Generating A2UI Messages
Basic Flow
Define components via surfaceUpdate
Populate data via dataModelUpdate
Trigger render via beginRendering
Complete Example: Simple Form
{"surfaceUpdate": {"surfaceId": "booking", "components": [
  {"id": "root", "component": {"Column": {"children": {"explicitList": ["title", "name_field", "date_field", "submit_btn"]}}}},
  {"id": "title", "component": {"Text": {"text": {"literalString": "Book a Table"}, "usageHint": "h2"}}},
  {"id": "name_field", "component": {"TextField": {"label": {"literalString": "Your Name"}, "text": {"path": "/form/name"}}}},
  {"id": "date_field", "component": {"DateTimeInput": {"value": {"path": "/form/date"}, "enableDate": true}}},
  {"id": "submit_btn", "component": {"Button": {"child": "submit_text", "action": {"name": "submit_booking", "context": [{"key": "name", "value": {"path": "/form/name"}}, {"key": "date", "value": {"path": "/form/date"}}]}}}},
  {"id": "submit_text", "component": {"Text": {"text": {"literalString": "Confirm Booking"}}}}
]}}
{"dataModelUpdate": {"surfaceId": "booking", "contents": [{"key": "form", "valueMap": [{"key": "name", "valueString": ""}, {"key": "date", "valueString": ""}]}]}}
{"beginRendering": {"surfaceId": "booking", "root": "root"}}

Event Handling
User Actions

When a user interacts (e.g., clicks a button), the client sends userAction:

{
  "userAction": {
    "name": "submit_booking",
    "surfaceId": "booking",
    "sourceComponentId": "submit_btn",
    "timestamp": "2025-01-01T10:00:00Z",
    "context": {"name": "John Doe", "date": "2025-01-15"}
  }
}

Error Reporting

Clients report errors via error message:

{
  "error": {
    "type": "RENDER_ERROR",
    "message": "Component 'user_card' references missing child",
    "surfaceId": "main",
    "componentId": "user_card",
    "timestamp": "2025-01-01T10:30:05Z"
  }
}

Best Practices
Unique IDs: Every component needs a unique id within its surface
Flat Structure: Use ID references for parent-child relationships
Data Separation: Keep UI structure in surfaceUpdate, dynamic values in dataModelUpdate
Path Convention: Use JSON Pointer format for paths (e.g., /user/profile/name)
Progressive Rendering: Send beginRendering after essential components are defined
Clean up surfaces: Use deleteSurface when flows complete
Reference Documentation
Core References
Component Reference - All 16 components with properties
Data Binding Guide - BoundValue patterns and templates
API Integration - Event handling and backend connection
Schema Reference - JSON Schema for validation
Advanced Topics
Catalog Negotiation - Multi-catalog support
Surface Management - Multiple UI regions
Streaming & Performance - Progressive rendering
Agent Prompting - LLM integration
Examples
Basic Patterns
Form Example - Registration and booking forms
List Example - Dynamic lists with templates
Modal Example - Dialog and popup patterns
Advanced Patterns
Booking Flow - End-to-end business flow
Multi-Surface - Multiple UI regions
Streaming - Progressive rendering
Weekly Installs
65
Repository
kobe4cn/a2ui_skills
GitHub Stars
6
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn