---
title: format numbers
url: https://skills.sh/tryghost/ghost/format-numbers
---

# format numbers

skills/tryghost/ghost/Format numbers
Format numbers
Installation
$ npx skills add https://github.com/tryghost/ghost --skill 'Format numbers'
SKILL.md
Format Numbers

When editing .tsx files, ensure all user-facing numbers are formatted using the formatNumber utility from @tryghost/shade.

Import
import {formatNumber} from '@tryghost/shade';

When to use formatNumber

Use formatNumber() when rendering any numeric value that is displayed to the user, including:

Member counts, visitor counts, subscriber counts
Email engagement metrics (opens, clicks, bounces)
Revenue amounts (combine with centsToDollars() for monetary values)
Post analytics (views, link clicks)
Any count or quantity shown in UI
Correct usage
<span>{formatNumber(totalMembers)}</span>
<span>{formatNumber(link.count || 0)}</span>
<span>{`${currencySymbol}${formatNumber(centsToDollars(mrr))}`}</span>
<span>{post.members > 0 ? `+${formatNumber(post.members)}` : '0'}</span>

Antipatterns to avoid

Do NOT use any of these patterns for formatting numbers in TSX files:

// BAD: raw .toLocaleString()
<span>{count.toLocaleString()}</span>

// BAD: manual Intl.NumberFormat
<span>{new Intl.NumberFormat('en-US').format(count)}</span>

// BAD: raw number without formatting
<span>{memberCount}</span>

// BAD: manual regex formatting
<span>{count.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')}</span>

Related utilities
formatPercentage() - for percentages (e.g., open rates, click rates)
abbreviateNumber() - for compact notation (e.g., 1.2M, 50k)
centsToDollars() - convert cents to dollars before passing to formatNumber

All are imported from @tryghost/shade.

Weekly Installs
–
Repository
tryghost/ghost
GitHub Stars
52.7K
First Seen
–
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass