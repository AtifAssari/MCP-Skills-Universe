---
rating: ⭐⭐
title: flags
url: https://skills.sh/facebook/react/flags
---

# flags

skills/facebook/react/flags
flags
Installation
$ npx skills add https://github.com/facebook/react --skill flags
Summary

Inspect and compare feature flag states across React release channels.

View all flags across channels (www, www-modern, canary, next, experimental, rn variants) or compare specific channels with --diff
Output formats include default table view, CSV export, and cleanup status grouping
Flag states indicated by symbols: enabled (✅), disabled (❌), variant testing (🧪), profiling-only (📊)
Common pitfall: __VARIANT__ flags are tested in both states on www; use --diff to spot meaningful differences between channels
SKILL.md
Feature Flags

Arguments:

$ARGUMENTS: Optional flags
Options
Option	Purpose
(none)	Show all flags across all channels
--diff <ch1> <ch2>	Compare flags between channels
--cleanup	Show flags grouped by cleanup status
--csv	Output in CSV format
Channels
www, www-modern - Meta internal
canary, next, experimental - OSS channels
rn, rn-fb, rn-next - React Native
Legend

✅ enabled, ❌ disabled, 🧪 __VARIANT__, 📊 profiling-only

Instructions
Run yarn flags $ARGUMENTS
Explain the output to the user
For --diff, highlight meaningful differences
Common Mistakes
Forgetting __VARIANT__ flags - These are tested both ways in www; check both variants
Comparing wrong channels - Use --diff to see exact differences
Weekly Installs
765
Repository
facebook/react
GitHub Stars
244.8K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass