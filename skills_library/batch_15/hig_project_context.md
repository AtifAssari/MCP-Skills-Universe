---
title: hig-project-context
url: https://skills.sh/raintree-technology/apple-hig-skills/hig-project-context
---

# hig-project-context

skills/raintree-technology/apple-hig-skills/hig-project-context
hig-project-context
Installation
$ npx skills add https://github.com/raintree-technology/apple-hig-skills --skill hig-project-context
SKILL.md
Apple HIG: Project Context

Create and maintain .claude/apple-design-context.md so other HIG skills can skip redundant questions.

Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered.

Gathering Context

Before asking questions, auto-discover context from:

README.md -- Product description, platform targets
Package.swift / .xcodeproj -- Supported platforms, minimum OS versions, dependencies
Info.plist -- App category, required capabilities, supported orientations
Existing code -- Import statements reveal frameworks (SwiftUI vs UIKit, HealthKit, etc.)
Assets.xcassets -- Color assets, icon sets, dark mode variants
Accessibility audit -- Grep for accessibility modifiers/attributes

Present findings and ask the user to confirm or correct. Then gather anything still missing:

1. Product Overview
What does the app do? (one sentence)
Category (productivity, social, health, game, utility, etc.)
Stage (concept, development, shipped, redesign)
2. Target Platforms
Which Apple platforms? (iOS, iPadOS, macOS, tvOS, watchOS, visionOS)
Minimum OS versions
Universal or platform-specific?
3. Technology Stack
UI framework: SwiftUI, UIKit, AppKit, or mixed?
Architecture: single-window, multi-window, document-based?
Apple technologies in use? (HealthKit, CloudKit, ARKit, etc.)
4. Design System
System defaults or custom design system?
Brand colors, fonts, icon style?
Dark mode and Dynamic Type support status
5. Accessibility Requirements
Target level (baseline, enhanced, comprehensive)
Specific considerations (VoiceOver, Switch Control, etc.)
Regulatory requirements (WCAG, Section 508)
6. User Context
Primary personas (1-3)
Key use cases and environments (desk, on-the-go, glanceable, immersive)
Known pain points or design challenges
7. Existing Design Assets
Figma/Sketch files?
Apple Design Resources in use?
Existing component library?
Context Document Template

Generate .claude/apple-design-context.md using this structure:

# Apple Design Context

## Product
- **Name**: [App name]
- **Description**: [One sentence]
- **Category**: [Category]
- **Stage**: [Concept / Development / Shipped / Redesign]

## Platforms
| Platform | Supported | Min OS | Notes |
|----------|-----------|--------|-------|
| iOS      | Yes/No    |        |       |
| iPadOS   | Yes/No    |        |       |
| macOS    | Yes/No    |        |       |
| tvOS     | Yes/No    |        |       |
| watchOS  | Yes/No    |        |       |
| visionOS | Yes/No    |        |       |

## Technology
- **UI Framework**: [SwiftUI / UIKit / AppKit / Mixed]
- **Architecture**: [Single-window / Multi-window / Document-based]
- **Apple Technologies**: [List any: HealthKit, CloudKit, ARKit, etc.]

## Design System
- **Base**: [System defaults / Custom design system]
- **Brand Colors**: [List or reference]
- **Typography**: [System fonts / Custom fonts]
- **Dark Mode**: [Supported / Not yet / N/A]
- **Dynamic Type**: [Supported / Not yet / N/A]

## Accessibility
- **Target Level**: [Baseline / Enhanced / Comprehensive]
- **Key Considerations**: [List any specific needs]

## Users
- **Primary Persona**: [Description]
- **Key Use Cases**: [List]
- **Known Challenges**: [List]

Updating Context

When updating an existing context document:

Read the current .claude/apple-design-context.md
Ask what has changed
Update only the changed sections
Preserve all unchanged information
Related Skills
hig-platforms -- Platform-specific guidance
hig-foundations -- Color, typography, layout decisions
hig-patterns -- UX pattern recommendations
hig-components-* -- Component recommendations
hig-inputs -- Input method coverage
hig-technologies -- Apple technology relevance

Built by Raintree Technology · More developer tools

Weekly Installs
149
Repository
raintree-techno…g-skills
GitHub Stars
45
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass