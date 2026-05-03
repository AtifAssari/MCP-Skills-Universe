---
title: 1k-date-formatting
url: https://skills.sh/onekeyhq/app-monorepo/1k-date-formatting
---

# 1k-date-formatting

skills/onekeyhq/app-monorepo/1k-date-formatting
1k-date-formatting
Installation
$ npx skills add https://github.com/onekeyhq/app-monorepo --skill 1k-date-formatting
SKILL.md
Date Formatting

Guidelines for consistent date and time formatting across OneKey applications.

Critical Rule

NEVER use native JavaScript date methods:

// ❌ FORBIDDEN
date.toLocaleDateString()
date.toLocaleString()
date.toISOString()
new Intl.DateTimeFormat().format(date)

// ✅ CORRECT
import { formatDate } from '@onekeyhq/shared/src/utils/dateUtils';
formatDate(date, { hideSeconds: true });

Quick Reference
Function	Use Case	Example Output
formatDate(date, options?)	Full date and time	2024/01/15, 14:30
formatTime(date, options?)	Time only	14:30:45
formatRelativeDate(date)	Relative display	Today, Yesterday
formatDistanceToNow(date)	Time distance	2 hours ago
formatDateFns(date, format?)	Custom format	Based on template
Common Patterns
Transaction History
import { formatDate } from '@onekeyhq/shared/src/utils/dateUtils';

// Hide year if current year, hide seconds
<SizableText>
  {formatDate(item.createdAt, { hideTheYear: true, hideSeconds: true })}
</SizableText>

Custom Format
// Use format template
{formatDate(item.timestamp, { formatTemplate: 'yyyy-LL-dd HH:mm' })}

React Hook (for dynamic updates)
import useFormatDate from '@onekeyhq/kit/src/hooks/useFormatDate';

function MyComponent() {
  const { formatDate } = useFormatDate();
  return <SizableText>{formatDate(date, { hideSeconds: true })}</SizableText>;
}

Format Options
interface IFormatDateOptions {
  hideYear?: boolean;        // Always hide year
  hideMonth?: boolean;       // Always hide month
  hideTheYear?: boolean;     // Hide year if current year
  hideTheMonth?: boolean;    // Hide month if current month
  hideTimeForever?: boolean; // Hide time portion
  hideSeconds?: boolean;     // Hide seconds (HH:mm)
  formatTemplate?: string;   // Custom date-fns format
}

Detailed Guide

For comprehensive date formatting rules and examples, see date-formatting.md.

Topics covered:

Core utilities from @onekeyhq/shared/src/utils/dateUtils
Available formatting functions
Options reference and format templates
Common patterns for transactions, history, and relative time
React hooks for dynamic updates
Locale-aware formatting
Real-world examples
Troubleshooting
Key Files
Purpose	File Path
Core utilities	packages/shared/src/utils/dateUtils.ts
React hook	packages/kit/src/hooks/useFormatDate.ts
Locale mapping	packages/shared/src/locale/dateLocaleMap.ts
Related Skills
/1k-i18n - Internationalization and locale handling
/1k-coding-patterns - General coding patterns
Weekly Installs
68
Repository
onekeyhq/app-monorepo
GitHub Stars
2.4K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass