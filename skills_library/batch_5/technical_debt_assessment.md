---
title: technical-debt-assessment
url: https://skills.sh/aj-geddes/useful-ai-prompts/technical-debt-assessment
---

# technical-debt-assessment

skills/aj-geddes/useful-ai-prompts/technical-debt-assessment
technical-debt-assessment
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill technical-debt-assessment
SKILL.md
Technical Debt Assessment
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Systematically identify, measure, and manage technical debt to make informed decisions about code quality investments.

When to Use
Legacy code evaluation
Refactoring prioritization
Sprint planning
Code quality initiatives
Acquisition due diligence
Architectural decisions
Quick Start

Minimal working example:

interface DebtItem {
  id: string;
  title: string;
  description: string;
  category: "code" | "architecture" | "test" | "documentation" | "security";
  severity: "low" | "medium" | "high" | "critical";
  effort: number; // hours
  impact: number; // 1-10 scale
  interest: number; // cost per sprint if not fixed
}

class TechnicalDebtAssessment {
  private items: DebtItem[] = [];

  addDebtItem(item: DebtItem): void {
    this.items.push(item);
  }

  calculatePriority(item: DebtItem): number {
    const severityWeight = {
      low: 1,
      medium: 2,
      high: 3,
      critical: 4,
    };
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Technical Debt Calculator	Technical Debt Calculator
Code Quality Scanner	Code Quality Scanner
Best Practices
✅ DO
Quantify debt impact
Prioritize by ROI
Track debt over time
Include debt in sprints
Document debt decisions
Set quality gates
❌ DON'T
Ignore technical debt
Fix everything at once
Skip impact analysis
Make emotional decisions
Weekly Installs
333
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass