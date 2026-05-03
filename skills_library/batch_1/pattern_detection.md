---
title: pattern-detection
url: https://skills.sh/supercent-io/skills-template/pattern-detection
---

# pattern-detection

skills/supercent-io/skills-template/pattern-detection
pattern-detection
Installation
$ npx skills add https://github.com/supercent-io/skills-template --skill pattern-detection
Summary

Detect code smells, security vulnerabilities, anomalies, and trends across codebases using regex, AST analysis, and statistical methods.

Identifies problematic patterns including long functions, duplicate code, magic numbers, empty catch blocks, and TODO/FIXME markers
Scans for security risks such as SQL injection, hard-coded secrets, dangerous function usage (eval, innerHTML), and credential exposure patterns
Performs statistical anomaly detection using Z-score and IQR methods to flag outliers in numerical data
Includes regex-based sensitive data detection for emails, phone numbers, credit cards, and SSNs, plus time-series trend analysis with moving averages and growth rate calculation
Generates structured reports with severity levels and actionable recommendations; read-only operation with built-in false-positive awareness
SKILL.md
Pattern Detection
When to use this skill
Code review: Proactively detect problematic patterns
Security review: Scan for vulnerability patterns
Refactoring: Identify duplicate code
Monitoring: Alert on anomalies
Instructions
Step 1: Detect code smell patterns

Detect long functions:

# Find functions with 50+ lines
grep -n "function\|def\|func " **/*.{js,ts,py,go} | \
  while read line; do
    file=$(echo $line | cut -d: -f1)
    linenum=$(echo $line | cut -d: -f2)
    # Function length calculation logic
  done


Duplicate code patterns:

# Search for similar code blocks
grep -rn "if.*==.*null" --include="*.ts" .
grep -rn "try\s*{" --include="*.java" . | wc -l


Magic numbers:

# Search for hard-coded numbers
grep -rn "[^a-zA-Z][0-9]{2,}[^a-zA-Z]" --include="*.{js,ts}" .

Step 2: Security vulnerability patterns

SQL Injection risks:

# SQL query built via string concatenation
grep -rn "query.*+.*\$\|execute.*%s\|query.*f\"" --include="*.py" .
grep -rn "SELECT.*\+.*\|\|" --include="*.{js,ts}" .


Hard-coded secrets:

# Password, API key patterns
grep -riE "(password|secret|api_key|apikey)\s*=\s*['\"][^'\"]+['\"]" --include="*.{js,ts,py,java}" .

# AWS key patterns
grep -rE "AKIA[0-9A-Z]{16}" .


Dangerous function usage:

# eval, exec usage
grep -rn "eval\(.*\)\|exec\(.*\)" --include="*.{py,js}" .

# innerHTML usage
grep -rn "innerHTML\s*=" --include="*.{js,ts}" .

Step 3: Code structure patterns

Import analysis:

# Candidates for unused imports
grep -rn "^import\|^from.*import" --include="*.py" . | \
  awk -F: '{print $3}' | sort | uniq -c | sort -rn


TODO/FIXME patterns:

# Find unfinished code
grep -rn "TODO\|FIXME\|HACK\|XXX" --include="*.{js,ts,py}" .


Error handling patterns:

# Empty catch blocks
grep -rn "catch.*{[\s]*}" --include="*.{js,ts,java}" .

# Ignored errors
grep -rn "except:\s*pass" --include="*.py" .

Step 4: Data anomaly patterns

Regex patterns:

import re

patterns = {
    'email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    'phone': r'\d{3}[-.\s]?\d{4}[-.\s]?\d{4}',
    'ip_address': r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',
    'credit_card': r'\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}',
    'ssn': r'\d{3}-\d{2}-\d{4}',
}

def detect_sensitive_data(text):
    found = {}
    for name, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            found[name] = len(matches)
    return found


Statistical anomaly detection:

import numpy as np
from scipy import stats

def detect_anomalies_zscore(data, threshold=3):
    """Z-score-based outlier detection"""
    z_scores = np.abs(stats.zscore(data))
    return np.where(z_scores > threshold)[0]

def detect_anomalies_iqr(data, k=1.5):
    """IQR-based outlier detection"""
    q1, q3 = np.percentile(data, [25, 75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return np.where((data < lower) | (data > upper))[0]

Step 5: Trend analysis
import pandas as pd

def analyze_trend(df, date_col, value_col):
    """Time-series trend analysis"""
    df[date_col] = pd.to_datetime(df[date_col])
    df = df.sort_values(date_col)

    # Moving averages
    df['ma_7'] = df[value_col].rolling(window=7).mean()
    df['ma_30'] = df[value_col].rolling(window=30).mean()

    # Growth rate
    df['growth'] = df[value_col].pct_change() * 100

    # Trend direction
    recent_trend = df['ma_7'].iloc[-1] > df['ma_30'].iloc[-1]

    return {
        'trend_direction': 'up' if recent_trend else 'down',
        'avg_growth': df['growth'].mean(),
        'volatility': df[value_col].std()
    }

Output format
Pattern detection report
# Pattern Detection Report

## Summary
- Files scanned: XXX
- Patterns detected: XX
- High severity: X
- Medium severity: X
- Low severity: X

## Detected patterns

### Security vulnerabilities (HIGH)
| File | Line | Pattern | Description |
|------|------|------|------|
| file.js | 42 | hardcoded-secret | Hard-coded API key |

### Code smells (MEDIUM)
| File | Line | Pattern | Description |
|------|------|------|------|
| util.py | 100 | long-function | Function length: 150 lines |

## Recommended actions
1. [Action 1]
2. [Action 2]

Best practices
Incremental analysis: Start with simple patterns
Minimize false positives: Use precise regex
Check context: Understand the context around a match
Prioritize: Sort by severity
Constraints
Required rules (MUST)
Read-only operation
Perform result verification
State the possibility of false positives
Prohibited (MUST NOT)
Do not auto-modify code
Do not log sensitive information
References
Regex101
OWASP Cheat Sheet
Code Smell Catalog
Examples
Example 1: Basic usage
Example 2: Advanced usage
Weekly Installs
10.5K
Repository
supercent-io/sk…template
GitHub Stars
88
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass