---
title: daily-writing-friends-design
url: https://skills.sh/bumgeunsong/daily-writing-friends/daily-writing-friends-design
---

# daily-writing-friends-design

skills/bumgeunsong/daily-writing-friends/daily-writing-friends-design
daily-writing-friends-design
Installation
$ npx skills add https://github.com/bumgeunsong/daily-writing-friends --skill daily-writing-friends-design
SKILL.md
Daily Writing Friends Design System

Follow these guidelines for ALL UI-related work in this project.

Design Documentation

For detailed reference, see the design docs:

tokens.md - Colors, typography, spacing
buttons.md - Button hierarchy and usage
components.md - Cards, inputs, interactions
theme.md - Dark mode, accessibility, mobile
Quick Reference
Color System (CSS Variables)
/* Light Mode */
--background: hsl(0, 0%, 100%);
--foreground: hsl(0, 0%, 9%);
--accent: hsl(210, 100%, 50%);

/* Dark Mode */
--background: hsl(180, 4%, 12%);
--foreground: hsl(180, 3%, 92%);
--accent: hsl(210, 100%, 70%);

Button Hierarchy (Most to Least Important)
Variant	Use For	Example
cta	Critical conversions	Signup, Join, Main FAB
default	Main interactions	Login, Save, Submit
outline	Supporting actions	Drafts, Cancel
ghost	Subtle actions	Edit, Navigation, Logout
destructive	Dangerous actions	Delete (red ghost style)
// CTA - most important
<Button variant="cta">회원가입</Button>

// Primary - main action
<Button variant="default">글 저장</Button>

// Secondary - supporting
<Button variant="outline">임시 저장 글</Button>

// Ghost - subtle
<Button variant="ghost">수정</Button>

// Destructive - dangerous (ghost style with red text)
<Button variant="destructive">삭제</Button>

Ghost Button Override Pattern

When ghost buttons need consistent styling on hover:

<Button
  variant="ghost"
  className="text-foreground hover:bg-transparent hover:text-foreground"
>

Component Styling
// Card
<div className="bg-card border-border/50 reading-shadow rounded-lg p-4">

// Input
<input className="bg-input border-border reading-focus" />

// Link
<a className="text-ring hover:underline">

Utility Classes
Class	Purpose
reading-shadow	Adaptive shadow (light/dark)
reading-hover	Subtle accent highlight on hover
reading-focus	Focus ring (2px accent)
text-reading	Optimized reading (line-height 1.7)
nav-selected	Navigation selection state
active-scale	Press feedback (scale 0.99)
Dark Mode
Strategy: Tailwind darkMode: 'class'
Toggle: useTheme() hook from @/shared/hooks/useTheme
Persistence: localStorage with OS preference fallback
import { useTheme } from '@/shared/hooks/useTheme';

const { theme, toggleTheme } = useTheme();

Spacing
Major sections: my-6 / py-6
Minor sections: my-3 / py-3
Default: space-y-4, p-4
Mobile: px-3 md:px-4
Accessibility
Touch targets: minimum 44x44px
Color contrast: 4.5:1 for text, 3:1 for large text
Focus visibility: use reading-focus
Screen reader: use sr-only for hidden text
Principles
Premium minimal - Less visual noise, Bear app style
Content-first - Remove decorative wrappers
Consistent hierarchy - Follow button/color hierarchy strictly
Dual-mode - All UI must work in both light and dark modes
Mobile-first - Responsive spacing and touch targets
Weekly Installs
28
Repository
bumgeunsong/dai…-friends
GitHub Stars
9
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass