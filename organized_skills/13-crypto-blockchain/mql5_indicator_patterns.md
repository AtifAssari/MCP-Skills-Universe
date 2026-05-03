---
rating: ⭐⭐
title: mql5-indicator-patterns
url: https://skills.sh/terrylica/cc-skills/mql5-indicator-patterns
---

# mql5-indicator-patterns

skills/terrylica/cc-skills/mql5-indicator-patterns
mql5-indicator-patterns
Installation
$ npx skills add https://github.com/terrylica/cc-skills --skill mql5-indicator-patterns
SKILL.md
MQL5 Visual Indicator Patterns

Battle-tested patterns for creating custom MQL5 indicators with proper display, buffer management, and real-time updates.

Self-Evolving Skill: This skill improves through use. If instructions are wrong, parameters drifted, or a workaround was needed — fix this file immediately, don't defer. Only update for real, reproducible issues.

When to Use This Skill

Use this skill when:

Creating custom MQL5 indicators for MetaTrader 5
Debugging indicator display or buffer issues
Setting up OnCalculate with proper warmup handling
Implementing new bar detection patterns
Quick Reference
Essential Patterns

Display Scale (for small values < 1.0):

IndicatorSetDouble(INDICATOR_MINIMUM, 0.0);
IndicatorSetDouble(INDICATOR_MAXIMUM, 0.1);


Buffer Setup (visible + hidden):

SetIndexBuffer(0, BufVisible, INDICATOR_DATA);        // Visible
SetIndexBuffer(1, BufHidden, INDICATOR_CALCULATIONS); // Hidden


New Bar Detection (prevents drift):

static int last_processed_bar = -1;
bool is_new_bar = (i > last_processed_bar);


Warmup Calculation:

int StartCalcPosition = underlying_warmup + own_warmup;
PlotIndexSetInteger(0, PLOT_DRAW_BEGIN, StartCalcPosition);

Common Pitfalls

Blank Display: Set explicit scale (see Display Scale reference)

Rolling Window Drift: Use new bar detection with hidden buffer (see Recalculation reference)

Misaligned Plots: Calculate correct PLOT_DRAW_BEGIN (see Complete Template reference)

Forward-Indexed Arrays: Always set ArraySetAsSeries(buffer, false)

Key Patterns

For production MQL5 indicators:

Explicit scale for small values (< 1.0 range)
Hidden buffers for recalculation tracking
New bar detection prevents rolling window drift
Static variables maintain state efficiently
Proper warmup calculation prevents misalignment
Forward indexing for code clarity

These patterns solve the most common indicator development issues encountered in real-world MT5 development.

Troubleshooting
Issue	Cause	Solution
Blank indicator window	Scale not set for small values	Set INDICATOR_MINIMUM/MAXIMUM explicitly
Values drifting over time	Rolling window not reset	Use new bar detection with hidden buffer
Misaligned plot start	Wrong PLOT_DRAW_BEGIN	Calculate: underlying_warmup + own_warmup
Reversed array indexing	Series mode enabled	Call ArraySetAsSeries(buffer, false)
Buffer values incorrect	Wrong INDICATOR_DATA type	Use INDICATOR_CALCULATIONS for hidden buffers
Compile error on buffer	Buffer count mismatch	Match #property indicator_buffers with SetIndexBuffer
Indicator not updating	OnCalculate return wrong	Return rates_total to signal successful calculation
Performance issues	Recalculating all bars	Only recalculate from prev_calculated onwards
Reference Documentation

For detailed information, see:

Display Scale - Fix blank indicator windows for small values
Buffer Patterns - Visible and hidden buffer architecture
Recalculation - Bar detection and rolling window state management
Complete Template - Full working example with all patterns
Debugging - Checklist for troubleshooting display issues
Post-Execution Reflection

After this skill completes, check before closing:

Did the command succeed? — If not, fix the instruction or error table that caused the failure.
Did parameters or output change? — If the underlying tool's interface drifted, update Usage examples and Parameters table to match.
Was a workaround needed? — If you had to improvise (different flags, extra steps), update this SKILL.md so the next invocation doesn't need the same workaround.

Only update if the issue is real and reproducible — not speculative.

Weekly Installs
282
Repository
terrylica/cc-skills
GitHub Stars
39
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass