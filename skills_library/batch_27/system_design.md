---
title: system-design
url: https://skills.sh/luongnv89/skills/system-design
---

# system-design

skills/luongnv89/skills/system-design
system-design
Installation
$ npx skills add https://github.com/luongnv89/skills --skill system-design
SKILL.md
System Design

Generate comprehensive Technical Architecture Documents with modular design for startups.

Subagent Architecture

This skill uses parallel research agents with upfront content extraction. Pattern: D (Research+Synthesis) + E (Staged Pipeline).

Agents
Agent	Role	Parallelization
prd-reader	Read PRD + supporting docs, return structured extraction	Sequential (only once)
tech-researcher	Handle one research round (spawned 5x in parallel)	Parallel (5 instances)
tad-writer	Generate complete tad.md from all inputs	Sequential (after all research)
Research Rounds (5 Parallel)
Round 1: Technology Stack validation (React, Node.js, PostgreSQL, Elasticsearch)
Round 2: Infrastructure validation (Vercel, AWS, CDN, cost estimation)
Round 3: Security review (auth, encryption, compliance, API security)
Round 4: Risk assessment (bottlenecks, vendor lock-in, team gaps)
Round 5: Holistic review (PRD alignment, team capability, quick wins)
Parallelization Strategy
PRD Content: Extracted once by prd-reader, stays out of main context
Research Independence: Each round researches conceptually different angle (tech vs. infra vs. security)
Reasoning Isolation: Parallel rounds keep each area's reasoning isolated, prevent groupthink
Note: Research rounds are conceptual reasoning, not data fetching — parallel rounds won't produce fundamentally different info, but isolation improves quality

Result: All 5 rounds complete concurrently, tad-writer synthesizes outputs into unified TAD.

Environment Check

Before executing:

Verify prd.md exists in project directory
Check for supporting docs (idea.md, validate.md) if available
Confirm WebSearch and WebFetch tools available for research
Verify write permissions to project root for tad.md creation
Ensure git access for final commit
Repo Sync Before Edits (mandatory)

Before creating/updating/deleting files in an existing repository, sync the current branch with remote:

branch="$(git rev-parse --abbrev-ref HEAD)"
git fetch origin
git pull --rebase origin "$branch"


If the working tree is not clean, stash first, sync, then restore:

git stash push -u -m "pre-sync"
branch="$(git rev-parse --abbrev-ref HEAD)"
git fetch origin && git pull --rebase origin "$branch"
git stash pop


If origin is missing, pull is unavailable, or rebase/stash conflicts occur, stop and ask the user before continuing.

Input

Project folder path in $ARGUMENTS containing:

prd.md - Product requirements (required)
idea.md, validate.md - Additional context (optional)
Workflow
Phase 1: Setup & Validation
Verify prd.md exists
Read supporting docs if present
Read references/tech-stack.md for technology recommendations
Backup existing tad.md if present
Phase 2: Extract Context

From PRD extract:

Product name and vision
Core features and requirements
User flows
Non-functional requirements
Third-party integrations
Analytics requirements
Phase 3: Clarify Architecture

Ask user (if not clear):

Decision	Options
Deployment	Vercel/Netlify (recommended), AWS, GCP, Self-hosted
Database	PostgreSQL, MongoDB, Supabase/Firebase, Multiple
Auth	Social (OAuth), Email/password, Magic links, Enterprise SSO
Budget	Free tier, <$50/mo, <$200/mo, Flexible
Phase 4: Research & Validation

Conduct 5 research rounds:

Technology Stack: Validate choices against industry standards
Infrastructure: Compare hosting for cost and scalability
Security: Review OWASP guidelines for chosen stack
Risk Assessment: Identify bottlenecks, vendor lock-in
Holistic Review: Ensure PRD alignment and startup feasibility
Phase 5: Generate TAD

Create tad.md with sections:

System Overview - Purpose, scope, PRD alignment
Architecture Diagram - Mermaid diagrams for system and flows
Technology Stack - Frontend, backend, database, infrastructure, DevOps
System Components - Modular design with interfaces and dependencies
Data Architecture - Schema, models, flows, storage
Infrastructure - Hosting, environments, scaling, CI/CD, monitoring
Security - Auth, authorization, data protection, API security
Performance - Targets, optimization strategies, caching
Development - Environment setup, project structure, testing, deployment
Risks - Risk matrix with mitigations
Appendix - Research insights, alternatives, costs, glossary

See references/tad-template.md for full template structure.

Phase 6: README Maintenance (ideas repo)

After writing tad.md, if the project folder is inside an ideas repo, update the repo README ideas table:

Preferred: cd to repo root and run python3 scripts/update_readme_ideas_index.py (if it exists)
Fallback: update README.md manually (ensure TAD status becomes ✅ for that idea)
Phase 7: Commit and push (mandatory)
Commit immediately after updates.
Push immediately to remote.
If push is rejected: git fetch origin && git rebase origin/main && git push.

Do not ask for additional push permission once this skill is invoked.

Phase 8: Output
Write tad.md to project folder
Summarize architecture decisions
Highlight modular design benefits
List cost estimates by phase
Suggest next steps (setup dev environment, create tasks)
Reporting with GitHub links (mandatory)

When reporting completion, include:

GitHub link to tad.md
GitHub link to README.md when it was updated
Commit hash

Link format (derive <owner>/<repo> from git remote get-url origin):

https://github.com/<owner>/<repo>/blob/main/<relative-path>
Step Completion Reports

After completing each major step, output a status report in this format:

◆ [Step Name] ([step N of M] — [context])
··································································
  [Check 1]:          √ pass
  [Check 2]:          √ pass (note if relevant)
  [Check 3]:          × fail — [reason]
  [Check 4]:          √ pass
  [Criteria]:         √ N/M met
  ____________________________
  Result:             PASS | FAIL | PARTIAL


Adapt the check names to match what the step actually validates. Use √ for pass, × for fail, and — to add brief context. The "Criteria" line summarizes how many acceptance criteria were met. The "Result" line gives the overall verdict.

Phase-specific checks

Phase 1 — Setup

◆ Setup (step 1 of 8 — environment validation)
··································································
  PRD found:                    √ pass
  Context extracted:            √ pass (product + features + NFRs read)
  Architecture questions answered: √ pass (deployment, DB, auth, budget confirmed)
  ____________________________
  Result:             PASS | FAIL | PARTIAL


Phase 4 — Research

◆ Research (step 4 of 8 — validation rounds)
··································································
  5 parallel rounds completed:  √ pass
  Best practices gathered:      √ pass (tech, infra, security, risk, holistic)
  Patterns validated:           √ pass (OWASP, vendor lock-in, startup feasibility)
  ____________________________
  Result:             PASS | FAIL | PARTIAL


Phase 5 — Generation

◆ Generation (step 5 of 8 — TAD authoring)
··································································
  11 sections written:          √ pass
  tad.md created:               √ pass
  Diagrams included:            √ pass (mermaid architecture + flow diagrams)
  ____________________________
  Result:             PASS | FAIL | PARTIAL


Phase 8 — Output

◆ Output (step 8 of 8 — delivery)
··································································
  Summary presented:            √ pass (architecture decisions highlighted)
  README updated:               √ pass (TAD status ✅)
  Committed and pushed:         √ pass (commit hash: ...)
  ____________________________
  Result:             PASS | FAIL | PARTIAL

Modification Mode

For existing TAD changes:

Create timestamped backup
Ask what to modify (stack, infrastructure, security, data, scaling)
Apply changes preserving structure
Update revision history
Guidelines
Practical: Implementable solutions for startups
Cost-conscious: Consider budget implications
Modular: Emphasize separation of concerns
Specific: Concrete technology choices
Visual: Include mermaid diagrams
Weekly Installs
59
Repository
luongnv89/skills
GitHub Stars
68
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn