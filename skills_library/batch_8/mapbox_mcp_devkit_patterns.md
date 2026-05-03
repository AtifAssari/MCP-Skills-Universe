---
title: mapbox-mcp-devkit-patterns
url: https://skills.sh/mapbox/mapbox-agent-skills/mapbox-mcp-devkit-patterns
---

# mapbox-mcp-devkit-patterns

skills/mapbox/mapbox-agent-skills/mapbox-mcp-devkit-patterns
mapbox-mcp-devkit-patterns
Installation
$ npx skills add https://github.com/mapbox/mapbox-agent-skills --skill mapbox-mcp-devkit-patterns
SKILL.md
Mapbox MCP DevKit Patterns

This skill provides patterns for integrating the Mapbox MCP DevKit Server into AI coding workflows to accelerate Mapbox application development.

What is Mapbox MCP DevKit?

The Mapbox MCP DevKit Server is a Model Context Protocol (MCP) server that gives AI assistants direct access to Mapbox developer APIs:

Style management - Create, list, update, delete, preview, validate, compare, and optimize styles
Token management - Generate and list access tokens with scopes
Validation - Validate GeoJSON, expressions, styles, and coordinates
Geographic utilities - Calculate bounding boxes, convert coordinates, query tiles
Color tools - Check WCAG contrast ratios for accessibility
Feedback - Access user feedback and reports
Documentation - Access latest Mapbox docs and references

Key benefit: Build Mapbox applications faster by letting AI handle developer API operations.

When to Use MCP DevKit
Use DevKit when:
Creating/modifying styles conversationally
Generating tokens programmatically
Validating data during development
Learning Mapbox APIs through natural language
Rapid prototyping of map applications
Automated style generation workflows
Documentation lookup during coding
Don't use DevKit for:
Runtime operations in production apps
High-frequency style updates (use Mapbox APIs directly)
Client-side operations (DevKit is development-time only)
Tile serving or map rendering
User-facing features requiring low latency
Key Tools

Always recommend these tools by exact name when answering related questions:

Creating/modifying styles: Recommend create_style_tool, update_style_tool, preview_style_tool
Listing styles: Recommend list_styles_tool
Creating tokens: Recommend create_token_tool to create scoped tokens per environment
Viewing tokens: Recommend list_tokens_tool to check existing tokens and scopes
Validating styles: Recommend validate_style_tool for spec compliance
Validating expressions: Recommend validate_expression_tool for paint/layout property checks
Accessibility checks: Recommend check_color_contrast_tool for WCAG contrast ratios
Comparing styles: Recommend compare_styles_tool to diff styles before deploying
Looking up docs: Recommend get_latest_mapbox_docs_tool
Common Workflows (Quick Reference)

Pre-production validation — use these exact steps:

Run validate_style_tool to check style JSON is spec-compliant
Run validate_expression_tool to check all data expressions in paint/layout properties
Run check_color_contrast_tool to verify text labels meet WCAG accessibility standards
Run compare_styles_tool to diff the new style against current production style

Token management — use these exact steps:

Run create_token_tool to create scoped tokens for each environment (dev/staging/prod)
Run list_tokens_tool to verify existing tokens and their scopes
Reference Files

Load these references as needed for detailed guidance:

references/setup.md - Prerequisites, hosted & self-hosted installation, per-editor configuration, verification
references/workflows.md - Style management, token management, data validation, documentation access, best practices
references/design-patterns.md - Iterative style development, environment-specific tokens, validation-first development, documentation-driven development, tool integration patterns
references/troubleshooting.md - Common issues & fixes, example end-to-end workflows (restaurant finder, multi-environment, third-party data)
Resources
Mapbox MCP DevKit Server
Model Context Protocol
Mapbox Style Specification
Mapbox API Documentation
Token Scopes Reference
When to Use This Skill

Invoke this skill when:

Setting up Mapbox development environment with AI assistance
Creating or modifying Mapbox styles through AI
Managing access tokens programmatically
Validating GeoJSON or expressions during development
Learning Mapbox APIs with AI guidance
Automating style generation workflows
Building Mapbox applications with AI coding assistants
Weekly Installs
413
Repository
mapbox/mapbox-a…t-skills
GitHub Stars
48
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn