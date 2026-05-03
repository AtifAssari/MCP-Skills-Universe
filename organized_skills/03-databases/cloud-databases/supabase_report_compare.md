---
rating: ⭐⭐⭐
title: supabase-report-compare
url: https://skills.sh/yoanbernabeu/supabase-pentest-skills/supabase-report-compare
---

# supabase-report-compare

skills/yoanbernabeu/supabase-pentest-skills/supabase-report-compare
supabase-report-compare
Installation
$ npx skills add https://github.com/yoanbernabeu/supabase-pentest-skills --skill supabase-report-compare
SKILL.md
Report Comparison

This skill compares two security audit reports to track progress over time.

When to Use This Skill
After fixing vulnerabilities, to verify remediation
For periodic security reviews
To track security posture over time
To identify regression (new vulnerabilities)
Prerequisites
Two audit reports in Markdown format
Reports should be from the same project
Usage
Basic Comparison
Compare security reports old-report.md and new-report.md

With Specific Paths
Compare reports/audit-v1.md with reports/audit-v2.md

Output Format
═══════════════════════════════════════════════════════════
 SECURITY AUDIT COMPARISON
═══════════════════════════════════════════════════════════

 Previous Audit: January 15, 2025
 Current Audit:  January 31, 2025
 Days Between:   16 days

 ─────────────────────────────────────────────────────────
 Score Comparison
 ─────────────────────────────────────────────────────────

 Previous Score: 35/100 (Grade: D)
 Current Score:  72/100 (Grade: C)
 Improvement:    +37 points ⬆️

 ┌────────────────────────────────────────────────────────┐
 │ Score Progress                                         │
 │                                                        │
 │  100 ┤                                                 │
 │   80 ┤                              ████████ 72       │
 │   60 ┤                              ████████          │
 │   40 ┤ ████████ 35                  ████████          │
 │   20 ┤ ████████                     ████████          │
 │    0 ┴─────────────────────────────────────────────── │
 │        Jan 15                       Jan 31            │
 └────────────────────────────────────────────────────────┘

 ─────────────────────────────────────────────────────────
 Findings Summary
 ─────────────────────────────────────────────────────────

 | Status      | P0  | P1  | P2  | Total |
 |-------------|-----|-----|-----|-------|
 | Previous    | 3   | 4   | 5   | 12    |
 | Current     | 0   | 2   | 4   | 6     |
 | Fixed       | 3   | 2   | 2   | 7     |
 | New         | 0   | 0   | 1   | 1     |

 ─────────────────────────────────────────────────────────
 Fixed Vulnerabilities ✅
 ─────────────────────────────────────────────────────────

 P0 (Critical) - ALL FIXED! 🎉

 ✅ P0-001: Service Role Key Exposed
    Status: FIXED
    Resolution: Key rotated, removed from client code
    Fixed on: January 16, 2025

 ✅ P0-002: Database Backups Publicly Accessible
    Status: FIXED
    Resolution: Bucket made private, files deleted
    Fixed on: January 16, 2025

 ✅ P0-003: Admin Function Privilege Escalation
    Status: FIXED
    Resolution: Added admin role verification
    Fixed on: January 17, 2025

 P1 (High) - 2 of 4 Fixed

 ✅ P1-001: Email Confirmation Disabled
    Status: FIXED
    Resolution: Email confirmation now required
    Fixed on: January 20, 2025

 ✅ P1-002: IDOR in get-user-data Function
    Status: FIXED
    Resolution: Added user ownership verification
    Fixed on: January 18, 2025

 P2 (Medium) - 2 of 5 Fixed

 ✅ P2-001: Weak Password Policy
    Status: FIXED
    Resolution: Minimum length increased to 10
    Fixed on: January 22, 2025

 ✅ P2-003: Disposable Emails Accepted
    Status: FIXED
    Resolution: Email validation added
    Fixed on: January 25, 2025

 ─────────────────────────────────────────────────────────
 Remaining Vulnerabilities ⚠️
 ─────────────────────────────────────────────────────────

 P1 (High) - 2 Remaining

 🟠 P1-003: User Enumeration via Timing Attack
    Status: OPEN (16 days)
    Priority: Address this week
    Note: Was in previous report, not yet fixed

 🟠 P1-004: Admin Channel Publicly Accessible
    Status: OPEN (16 days)
    Priority: Address this week

 P2 (Medium) - 3 Remaining

 🟡 P2-002: Wildcard CORS Origin
    Status: OPEN (16 days)

 🟡 P2-004: Verbose Error Messages
    Status: OPEN (16 days)

 🟡 P2-005: Rate Limiting Not Enforced on Functions
    Status: OPEN (16 days)

 ─────────────────────────────────────────────────────────
 New Vulnerabilities 🆕
 ─────────────────────────────────────────────────────────

 P2 (Medium) - 1 New Issue

 🆕 P2-006: New Storage Bucket Without RLS
    Severity: 🟡 P2
    Component: Storage
    Description: New bucket 'user-uploads' created without
                 RLS policies. Currently empty but will
                 need policies before production use.
    First Seen: January 31, 2025

 ─────────────────────────────────────────────────────────
 Progress Analysis
 ─────────────────────────────────────────────────────────

 Remediation Rate: 58% (7 of 12 fixed)

 By Severity:
 ├── P0 (Critical): 100% fixed ✅
 ├── P1 (High): 50% fixed
 └── P2 (Medium): 40% fixed

 Time to Fix (Average):
 ├── P0: 1.3 days (excellent)
 ├── P1: 3.5 days (good)
 └── P2: 5.5 days (acceptable)

 Regression: 1 new issue introduced
             (lower severity, acceptable)

 ─────────────────────────────────────────────────────────
 Recommendations
 ─────────────────────────────────────────────────────────

 1. CONTINUE PROGRESS
    Great work fixing all P0 issues! Focus now on
    remaining P1 issues:
    - User enumeration timing attack
    - Admin broadcast channel

 2. ADDRESS NEW ISSUE
    Configure RLS on 'user-uploads' bucket before
    it's used in production.

 3. SCHEDULE FOLLOW-UP
    Recommend another audit in 14 days to verify
    remaining fixes.

 ─────────────────────────────────────────────────────────
 Trend Analysis
 ─────────────────────────────────────────────────────────

 If you have 3+ reports, trend analysis is available:

 | Date       | Score | P0 | P1 | P2 | Total |
 |------------|-------|----|----|----| ------|
 | 2024-12-01 | 28    | 4  | 5  | 6  | 15    |
 | 2025-01-15 | 35    | 3  | 4  | 5  | 12    |
 | 2025-01-31 | 72    | 0  | 2  | 4  | 6     |

 Trend: Improving ⬆️

═══════════════════════════════════════════════════════════

Comparison Logic
Finding Matching

Findings are matched between reports using:

ID match — Same P0-001, P1-002, etc.
Component + Title match — Same issue description
Location match — Same file/line/endpoint
Status Determination
Previous	Current	Status
Present	Absent	Fixed ✅
Present	Present	Remaining ⚠️
Absent	Present	New 🆕
Absent	Absent	N/A
Score Calculation
Change = Current Score - Previous Score

Positive change = Improvement ⬆️
Negative change = Regression ⬇️
No change = Stable ➡️

Context Output
{
  "comparison": {
    "previous_date": "2025-01-15",
    "current_date": "2025-01-31",
    "previous_score": 35,
    "current_score": 72,
    "score_change": 37,
    "findings": {
      "previous_total": 12,
      "current_total": 6,
      "fixed": 7,
      "remaining": 5,
      "new": 1
    },
    "by_severity": {
      "P0": { "previous": 3, "current": 0, "fixed": 3, "new": 0 },
      "P1": { "previous": 4, "current": 2, "fixed": 2, "new": 0 },
      "P2": { "previous": 5, "current": 4, "fixed": 2, "new": 1 }
    },
    "remediation_rate": 0.58,
    "trend": "improving"
  }
}

Report Output

The comparison generates supabase-audit-comparison.md:

# Security Audit Comparison Report

## Summary

| Metric | Previous | Current | Change |
|--------|----------|---------|--------|
| Score | 35/100 | 72/100 | +37 ⬆️ |
| P0 Issues | 3 | 0 | -3 ✅ |
| P1 Issues | 4 | 2 | -2 ✅ |
| P2 Issues | 5 | 4 | -1 ✅ |
| Total | 12 | 6 | -6 ✅ |

## Fixed Issues (7)

[Detailed list of fixed issues...]

## Remaining Issues (5)

[Detailed list of remaining issues...]

## New Issues (1)

[Detailed list of new issues...]

## Recommendations

[Action items based on comparison...]

Multiple Report Comparison

For trend analysis across 3+ reports:

Compare trend across reports/audit-*.md


Output includes:

Score trend graph
Issue count over time
Average time to fix
Recurring issues identification
Best Practices
Naming Convention
reports/
├── supabase-audit-2024-12-01.md
├── supabase-audit-2025-01-15.md
├── supabase-audit-2025-01-31.md
└── supabase-audit-comparison-2025-01-31.md

Regular Audits
Frequency	Purpose
After fixes	Verify remediation
Monthly	Catch regressions
Before releases	Pre-production check
After incidents	Post-incident review
Tracking Progress
Keep all reports in version control
Link to issue tracker (GitHub, Jira)
Include in sprint planning
Report to stakeholders
Related Skills
supabase-report — Generate the reports to compare
supabase-pentest — Run full audit
supabase-help — Quick reference
Weekly Installs
143
Repository
yoanbernabeu/su…t-skills
GitHub Stars
37
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass