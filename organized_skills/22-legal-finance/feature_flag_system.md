---
rating: ⭐⭐
title: feature-flag-system
url: https://skills.sh/aj-geddes/useful-ai-prompts/feature-flag-system
---

# feature-flag-system

skills/aj-geddes/useful-ai-prompts/feature-flag-system
feature-flag-system
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill feature-flag-system
SKILL.md
Feature Flag System
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement feature flags to decouple deployment from release, enable gradual rollouts, A/B testing, and provide emergency kill switches.

When to Use
Gradual feature rollouts
A/B testing and experiments
Canary deployments
Beta features for specific users
Emergency kill switches
Trunk-based development
Dark launching
Operational flags (maintenance mode)
User-specific features
Quick Start

Minimal working example:

interface FlagConfig {
  key: string;
  enabled: boolean;
  description: string;
  rules?: FlagRule[];
  variants?: FlagVariant[];
  createdAt: Date;
  updatedAt: Date;
}

interface FlagRule {
  type: "user" | "percentage" | "attribute" | "datetime";
  operator: "in" | "equals" | "contains" | "gt" | "lt" | "between";
  attribute?: string;
  values: any[];
}

interface FlagVariant {
  key: string;
  weight: number;
  value: any;
}

interface EvaluationContext {
  userId?: string;
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Feature Flag Service (TypeScript)	Feature Flag Service (TypeScript)
React Hook for Feature Flags	React Hook for Feature Flags
Feature Flag with Analytics	Feature Flag with Analytics
LaunchDarkly-Style SDK	LaunchDarkly-Style SDK
Admin UI for Feature Flags	Admin UI for Feature Flags
Best Practices
✅ DO
Use descriptive flag names
Document flag purpose and lifecycle
Implement gradual rollouts
Track flag evaluations
Clean up old flags regularly
Use feature flags for experiments
Implement kill switches for critical features
Test both enabled and disabled states
Use consistent hashing for stable rollouts
Provide admin UI for non-technical users
❌ DON'T
Use flags for permanent configuration
Accumulate technical debt with old flags
Skip flag cleanup
Make flags too granular
Hard-code flag checks everywhere
Skip analytics and monitoring
Weekly Installs
278
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