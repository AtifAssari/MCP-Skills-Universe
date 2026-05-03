---
rating: ⭐⭐⭐
title: product-ux-expert
url: https://skills.sh/majiayu000/claude-arsenal/product-ux-expert
---

# product-ux-expert

skills/majiayu000/claude-arsenal/product-ux-expert
product-ux-expert
Installation
$ npx skills add https://github.com/majiayu000/claude-arsenal --skill product-ux-expert
SKILL.md
Product UX Expert
Core Principles
Reduce Cognitive Load — Minimize mental effort required for every interaction
Accessibility First — WCAG 2.2 AA is the baseline, not an afterthought
Evidence-Based — Decisions backed by user research, not assumptions
Anticipatory Design — Predict user needs before they ask
Ethical Design — No dark patterns, transparent data practices
Mobile First — Design for smallest screens, enhance for larger
Quick Reference
Nielsen's 10 Heuristics
#	Heuristic	Key Question
1	Visibility of System Status	Does the user always know what's happening?
2	Match System & Real World	Does it use familiar language and concepts?
3	User Control & Freedom	Can users easily undo or exit?
4	Consistency & Standards	Does it follow platform conventions?
5	Error Prevention	Does it prevent errors before they occur?
6	Recognition over Recall	Is information visible, not memorized?
7	Flexibility & Efficiency	Are there shortcuts for experts?
8	Aesthetic & Minimalist Design	Is every element necessary?
9	Help Users with Errors	Are error messages helpful and actionable?
10	Help & Documentation	Is help available when needed?
Cognitive Psychology
Cognitive Load Types
Intrinsic Load     — Complexity inherent to the task itself
Extraneous Load    — Unnecessary complexity from poor design (eliminate this!)
Germane Load       — Mental effort for learning/understanding (support this)

Key Laws
Hick's Law         — More choices = longer decision time
                   → Limit options to 5-7, use progressive disclosure

Miller's Law       — Working memory holds 7±2 items
                   → Chunk information, use visual grouping

Fitts's Law        — Larger, closer targets are easier to click
                   → Make primary actions big and accessible

Jakob's Law        — Users expect your site to work like others
                   → Follow established patterns

Von Restorff       — Different items are more memorable
                   → Highlight CTAs with contrast

Serial Position    — First and last items remembered best
                   → Put key info at start/end of lists

Gestalt Principles
Proximity          — Close elements are perceived as groups
Similarity         — Similar elements are perceived as related
Continuity         — Eyes follow smooth lines and curves
Closure            — Mind completes incomplete shapes
Figure-Ground      — Elements seen as foreground or background
Common Region      — Elements in same area are grouped

Heuristic Evaluation
Process
1. Define scope         — What screens/flows to evaluate
2. Select evaluators    — 3-5 UX experts (80%+ issues found)
3. Independent review   — Each expert reviews alone
4. Apply heuristics     — Rate severity for each issue
5. Consolidate          — Merge findings, remove duplicates
6. Prioritize           — Rank by severity × frequency
7. Report               — Actionable recommendations

Severity Rating
Level	Severity	Description
0	Not a problem	Evaluator disagrees it's an issue
1	Cosmetic	Fix only if extra time available
2	Minor	Low priority, causes friction
3	Major	High priority, significant impact
4	Catastrophic	Must fix before release
Issue Template
## Issue: [Brief Description]

**Heuristic:** #N - Name
**Severity:** 0-4
**Location:** Screen / Component / Flow

**Problem:**
What's wrong and why it matters to users.

**Evidence:**
Screenshot or recording link.

**Recommendation:**
Specific fix with before/after comparison.

User Journey Mapping
Journey Map Structure
┌─────────────────────────────────────────────────────────────────┐
│  PERSONA: [Name, Goals, Context]                                │
├─────────┬─────────┬─────────┬─────────┬─────────┬──────────────┤
│ Stage   │ Aware   │ Consider│ Purchase│ Use     │ Advocate     │
├─────────┼─────────┼─────────┼─────────┼─────────┼──────────────┤
│ Actions │ Search  │ Compare │ Signup  │ Onboard │ Share/Review │
├─────────┼─────────┼─────────┼─────────┼─────────┼──────────────┤
│ Touch-  │ Search  │ Website │ Checkout│ App     │ Social       │
│ points  │ Ads     │ Reviews │ Email   │ Support │ Email        │
├─────────┼─────────┼─────────┼─────────┼─────────┼──────────────┤
│ Emotions│   😐    │   🤔    │   😟    │   😊    │    😍        │
│         │ curious │ hopeful │ anxious │ relieved│  delighted   │
├─────────┼─────────┼─────────┼─────────┼─────────┼──────────────┤
│ Pain    │ Too many│ Info    │ Complex │ Unclear │ No referral  │
│ Points  │ options │ overload│ forms   │ next    │ program      │
├─────────┼─────────┼─────────┼─────────┼─────────┼──────────────┤
│ Opportu-│ Clear   │ Compare │ 1-click │ Progress│ Share        │
│ nities  │ tagline │ table   │ signup  │ tracker │ incentive    │
└─────────┴─────────┴─────────┴─────────┴─────────┴──────────────┘

Touchpoint Analysis
For each touchpoint, evaluate:

1. Entry Point      — How do users arrive?
2. User Goal        — What are they trying to accomplish?
3. Friction         — What slows them down?
4. Emotion          — How do they feel?
5. Drop-off Risk    — Where might they abandon?
6. Opportunity      — How can we improve?

Accessibility (WCAG 2.2 AA)
POUR Principles
Perceivable     — Can users perceive the content?
                  ✓ Text alternatives for images
                  ✓ Captions for video
                  ✓ 4.5:1 color contrast
                  ✓ Resizable text (up to 200%)

Operable        — Can users operate the interface?
                  ✓ Keyboard accessible
                  ✓ No keyboard traps
                  ✓ Skip navigation links
                  ✓ Sufficient time limits
                  ✓ Focus visible (new in 2.2!)

Understandable  — Can users understand the content?
                  ✓ Language declared
                  ✓ Consistent navigation
                  ✓ Error identification
                  ✓ Labels and instructions

Robust          — Works with assistive technology?
                  ✓ Valid HTML
                  ✓ ARIA landmarks
                  ✓ Status messages announced

New in WCAG 2.2 (2023-2025)
Focus Not Obscured (AA)      — Focused element not fully hidden
Focus Appearance (AA)        — Visible focus indicator (2px outline)
Dragging Movements (AA)      — Alternatives to drag-and-drop
Target Size (AA)             — Minimum 24×24 CSS pixels
Consistent Help (A)          — Help mechanisms in consistent locations
Redundant Entry (A)          — Don't ask for same info twice
Accessible Authentication (A) — No cognitive function tests for login

Quick Checklist
## Accessibility Check

### Perceivable
- [ ] All images have meaningful alt text
- [ ] Videos have captions and transcripts
- [ ] Color contrast ratio ≥ 4.5:1 (text), ≥ 3:1 (large text)
- [ ] Information not conveyed by color alone
- [ ] Text can be resized to 200% without loss

### Operable
- [ ] All functionality available via keyboard
- [ ] Focus order is logical
- [ ] Focus indicator is visible (2px outline minimum)
- [ ] No keyboard traps
- [ ] Skip links provided
- [ ] Touch targets ≥ 24×24px

### Understandable
- [ ] Page language declared
- [ ] Consistent navigation across pages
- [ ] Form errors clearly identified
- [ ] Labels associated with inputs

### Robust
- [ ] Valid HTML (no duplicate IDs)
- [ ] ARIA roles used correctly
- [ ] Works with screen readers (NVDA/VoiceOver)

Interaction Patterns
Micro-interactions
Purpose of micro-interactions:
1. Feedback      — Confirm user action (button click, form submit)
2. Status        — Show current state (loading, progress)
3. Guidance      — Direct attention (onboarding tooltips)
4. Delight       — Create emotional connection (subtle animations)

Best Practices:
✓ Keep animations under 300ms
✓ Use easing (ease-out for exits, ease-in for entries)
✓ Respect prefers-reduced-motion
✓ Animate properties that don't trigger layout (transform, opacity)

Motion Design Principles
Duration Scale:
- Micro (fade, state change)     →  100-200ms
- Small (dropdown, tooltip)      →  200-300ms
- Medium (modal, sidebar)        →  300-400ms
- Large (page transition)        →  400-500ms

Easing:
- ease-out    → Elements entering (decelerate into view)
- ease-in     → Elements exiting (accelerate out of view)
- ease-in-out → Elements moving (natural feel)

Form Design
✓ One column layout (no side-by-side inputs)
✓ Labels above inputs (not placeholder-only)
✓ Group related fields visually
✓ Inline validation (after field blur)
✓ Clear error messages with solutions
✓ Show password option
✓ Autofill support (autocomplete attributes)
✓ Smart defaults based on context

Design System Integration
Component States
Every interactive component needs:

Default         — Normal resting state
Hover           — Mouse over (desktop)
Focus           — Keyboard focus (visible ring)
Active          — Being pressed/clicked
Disabled        — Not currently available
Loading         — Processing action
Error           — Validation failed
Success         — Action completed

Design Tokens
{
  "color": {
    "text": {
      "primary": "#1a1a1a",
      "secondary": "#6b6b6b",
      "disabled": "#a3a3a3",
      "inverse": "#ffffff"
    },
    "interactive": {
      "default": "#0066cc",
      "hover": "#0052a3",
      "active": "#003d7a",
      "focus": "#0066cc"
    },
    "feedback": {
      "error": "#d32f2f",
      "warning": "#f57c00",
      "success": "#388e3c",
      "info": "#1976d2"
    }
  },
  "spacing": {
    "xs": "4px",
    "sm": "8px",
    "md": "16px",
    "lg": "24px",
    "xl": "32px"
  },
  "radius": {
    "sm": "4px",
    "md": "8px",
    "lg": "16px",
    "full": "9999px"
  }
}

2025 UX Trends
AI-Driven Personalization
✓ Adaptive interfaces based on user behavior
✓ Predictive content suggestions
✓ Context-aware personalization
✓ Real-time UI adjustments

⚠️ Always provide transparency and user control
⚠️ Respect privacy, use on-device processing when possible

Anticipatory Design
Design that:
- Predicts user needs before they ask
- Reduces decision fatigue with smart defaults
- Automates repetitive tasks
- Surfaces relevant information proactively

Example: Pre-filling shipping address based on previous orders

Ethical Design Practices
DO:
✓ Clear consent for data collection
✓ Easy-to-find privacy settings
✓ Honest product representations
✓ Sustainable design (reduce digital carbon)

DON'T (Dark Patterns):
✗ Confirmshaming ("No, I don't want to save money")
✗ Hidden costs
✗ Trick questions
✗ Forced continuity (hard-to-cancel subscriptions)
✗ Misdirection
✗ Roach motels (easy in, hard out)

Evaluation Template
# UX Evaluation Report

## Overview
- **Product:** [Name]
- **Scope:** [Screens/Flows evaluated]
- **Date:** [Date]
- **Evaluators:** [Names]

## Executive Summary
[2-3 sentences on overall UX health and critical findings]

## Methodology
- Nielsen's 10 Heuristics
- WCAG 2.2 AA Compliance Check
- Cognitive Load Analysis

## Findings by Severity

### Catastrophic (Severity 4)
[Issues that must be fixed immediately]

### Major (Severity 3)
[High priority issues]

### Minor (Severity 2)
[Low priority improvements]

## Accessibility Status
- [ ] WCAG 2.2 A Compliance
- [ ] WCAG 2.2 AA Compliance
- [ ] Screen Reader Compatible
- [ ] Keyboard Navigation Complete

## Recommendations
[Prioritized action items with effort estimates]

## Appendix
- Screenshot evidence
- User testing video clips
- Competitive analysis

See Also
reference/heuristics.md — Detailed heuristic examples
reference/accessibility.md — Full WCAG 2.2 checklist
reference/psychology.md — Cognitive psychology deep dive
reference/journey-mapping.md — Journey mapping templates
Weekly Installs
115
Repository
majiayu000/clau…-arsenal
GitHub Stars
30
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass