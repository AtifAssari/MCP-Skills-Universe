---
rating: ⭐⭐⭐
title: reviewing-python-libraries
url: https://skills.sh/wdm0006/python-skills/reviewing-python-libraries
---

# reviewing-python-libraries

skills/wdm0006/python-skills/reviewing-python-libraries
reviewing-python-libraries
Installation
$ npx skills add https://github.com/wdm0006/python-skills --skill reviewing-python-libraries
SKILL.md
Python Library Review
Quick Health Check (5 min)
git clone https://github.com/user/package && cd package
cat pyproject.toml | head -50        # Modern config?
ls tests/ && pytest --collect-only   # Tests exist?
pytest --cov=package | tail -20      # Coverage?
pip install bandit && bandit -r src/ # Security?

Review Dimensions
Area	Check For
Structure	src/ layout, py.typed marker
Packaging	pyproject.toml (not setup.py)
Code	Type hints, docstrings, no anti-patterns
Tests	80%+ coverage, edge cases
Security	No secrets, input validation, pip-audit clean
Docs	README, API docs, changelog
API	Consistent naming, sensible defaults
CI/CD	Tests on PR, multi-Python, security scans
Red Flags 🚩
No tests
No type hints
setup.py only (no pyproject.toml)
Pinned exact versions for all deps
No LICENSE file
Last commit > 1 year ago
Green Flags ✅
Active maintenance (recent commits)
High test coverage (>85%)
Comprehensive CI/CD
Type hints throughout
Clear documentation
Semantic versioning
Report Template
# Library Review: [package]

**Rating:** [Excellent/Good/Needs Work/Significant Issues]

## Strengths
- [Strength 1]

## Areas for Improvement
- [Issue 1] - Severity: High/Medium/Low

## Category Scores
| Category | Score |
|----------|-------|
| Structure | ⭐⭐⭐⭐⭐ |
| Testing | ⭐⭐⭐☆☆ |
| Security | ⭐⭐⭐⭐☆ |

## Recommendations
1. [High priority action]
2. [Medium priority action]


For detailed checklists, see:

CHECKLIST.md - Full review checklist
REPORT_TEMPLATE.md - Complete report template
Best Practices Checklist
Essential:
- [ ] pyproject.toml valid
- [ ] Tests exist and pass
- [ ] README has install/usage
- [ ] LICENSE present
- [ ] No hardcoded secrets

Important:
- [ ] Type hints on public API
- [ ] CI runs tests on PRs
- [ ] Coverage > 70%
- [ ] Changelog maintained

Recommended:
- [ ] src/ layout
- [ ] py.typed marker
- [ ] Security scanning in CI
- [ ] Contributing guide

Learn More

This skill is based on the Guide to Developing High-Quality Python Libraries by Will McGinnis. The review criteria in this skill draw from all posts in the guide — see the full guide for detailed quality criteria across every dimension of library development.

Weekly Installs
16
Repository
wdm0006/python-skills
GitHub Stars
24
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn