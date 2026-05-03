---
rating: ⭐⭐
title: muapi-ui-design
url: https://skills.sh/samuraigpt/generative-media-skills/muapi-ui-design
---

# muapi-ui-design

skills/samuraigpt/generative-media-skills/muapi-ui-design
muapi-ui-design
Installation
$ npx skills add https://github.com/samuraigpt/generative-media-skills --skill muapi-ui-design
SKILL.md
🎨 UI/UX Design Mockup Skill

A specialized skill for AI Agents to architect high-fidelity digital interfaces. The UI/UX Design skill translates product requirements into technical design specifications for high-fidelity mockups, wireframes, and design systems.

Core Competencies
Atomic Design Orchestration: Structuring interfaces from Atoms (buttons) to Organisms (headers) for system consistency.
Platform-Specific Layouts: Designing for responsive breakpoints across Mobile (iOS/Android) and Web (SaaS/E-commerce).
Design System Integration: Specifying typography scales, spacing tokens, and color palettes (Hex/HSL).
Heuristic Awareness: Ensuring designs follow established usability principles (Nielsen's 10 Heuristics).
🏗️ Technical Specification
1. Intent Mapping Table
Creative Intent	Style	Layout Pattern	Focus
Enterprise SaaS	Modern/Clean	Dashboard/Grid	Data Density
Consumer App	Glassmorphism	F-Pattern / Cards	Visual Flair
E-commerce	Minimalist	Z-Pattern / Product Grid	Conversion
Portfolio	Brutalist	Asymmetric	Identity
Utility/Tool	Neomorphism	Control Panel	Tactile Feedback
2. Design Tokens & Variables
Typography: Geometric Sans (Inter/Roboto) for tech; Serif (Playfair) for luxury.
Spacing: 8pt grid system for consistent rhythmic spacing.
Color: High-contrast accessible palettes (WCAG 2.1 compliant).
Elevation: Shadow-based depth vs. Flat design layers.
🧠 Prompt Optimization Protocol (Agent Instruction)

Before calling the script, the Agent MUST expand the user's requirements into a Design Specification:

ATOMIC STRUCTURE: Mention specific components (Atoms): Glassmorphic buttons, Input fields with 4px radius, Iconic sidebars.
HIERARCHY: Use layout patterns: F-Pattern for content-heavy sites, Z-Pattern for landing pages, Grid-based Dashboards.
TYPOGRAPHY & TOKENS: Injected design tokens: Inter Sans-serif, 8pt spacing system, WCAG high-contrast colors.
NO SKEUOMORPHISM: Ensure the prompt enforces Flat Design or Glassmorphism to avoid "photograph-of-screen" results.
🚀 Protocol: Using the UI Designer
Step 1: Define the Product Brief

Provide the agent with a feature list and target audience.

Step 2: Invoke the Script

The generate-mockup.sh script expands the brief using internal knowledge of design systems.

# Designing a Fintech Mobile App
bash scripts/generate-mockup.sh \
  --desc "crypto wallet home with price charts" \
  --platform mobile \
  --theme dark \
  --style glassmorphism

⚠️ Constraints & Guardrails
Device Realism: MANDATORY - Do not show hands, physical phones, or desks. Generate pure UI/UX mockups only.
Accessibility: Avoid low-contrast text on bright backgrounds.
Complexity: Keep "Atoms" consistent across a single page generation.
Text Rendering: Use Flux for legible headers; specify placeholder text for smaller body copy.
⚙️ Implementation Details

This skill translates a high-level DESCRIPTION into a UX_BRIEF that specifies layout patterns, design tokens, and aesthetic constraints for the core/media/generate-image.sh primitive.

Weekly Installs
226
Repository
samuraigpt/gene…a-skills
GitHub Stars
3.2K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass