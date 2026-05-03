---
rating: ⭐⭐⭐
title: sensei
url: https://skills.sh/microsoft/github-copilot-for-azure/sensei
---

# sensei

skills/microsoft/github-copilot-for-azure/sensei
sensei
Installation
$ npx skills add https://github.com/microsoft/github-copilot-for-azure --skill sensei
Summary

Iteratively improve skill frontmatter compliance and test coverage using the Ralph loop pattern.

Automates a 10-step feedback loop: read skill metadata, score compliance against the agentskills.io spec, scaffold missing tests, improve frontmatter triggers, run tests, validate references, check token budgets, and prompt for commit/issue creation
Targets Medium-High compliance: distinctive WHEN: trigger phrases, descriptions under 60 words, passing tests, and token budgets under 500 lines
Supports single skills, multiple skills, batch operations by adherence level (Low/Medium/Medium-High/High), and all skills at once; includes --skip-integration flag for faster iteration
Validates skill names, description length, trigger keywords, and warns against risky "DO NOT USE FOR:" anti-triggers in multi-skill environments; preserves optional spec fields like license and metadata
SKILL.md
Sensei

"A true master teaches not by telling, but by refining." - The Skill Sensei

Automates skill frontmatter improvement using the Ralph loop pattern - iteratively improving skills until they reach Medium-High compliance with passing tests, then checking token usage and prompting for action.

Help

When user says "sensei help" or asks how to use sensei, show this:

╔══════════════════════════════════════════════════════════════════╗
║  SENSEI - Skill Frontmatter Compliance Improver                  ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  USAGE:                                                          ║
║    Run sensei on <skill-name>              # Single skill        ║
║    Run sensei on <skill-name> --skip-integration  # Fast mode    ║
║    Run sensei on <skill1>, <skill2>, ...   # Multiple skills     ║
║    Run sensei on all Low-adherence skills  # Batch by score      ║
║    Run sensei on all skills                # All skills       ║
║                                                                  ║
║  EXAMPLES:                                                       ║
║    Run sensei on appinsights-instrumentation                     ║
║    Run sensei on azure-security --skip-integration               ║
║    Run sensei on azure-security, azure-observability             ║
║    Run sensei on all Low-adherence skills                        ║
║                                                                  ║
║  WHAT IT DOES:                                                   ║
║    1. READ      - Load skill's SKILL.md, tests, and token count  ║
║    2. SCORE     - Check compliance (Low/Medium/Medium-High/High) ║
║    3. SCAFFOLD  - Create tests from template if missing          ║
║    4. IMPROVE   - Add WHEN: triggers (cross-model optimized)     ║
║    5. TEST      - Run tests, fix if needed                       ║
║    6. REFERENCES- Validate markdown links                        ║
║    7. TOKENS    - Check token budget, gather suggestions         ║
║    8. SUMMARY   - Show before/after with suggestions             ║
║    9. PROMPT    - Ask: Commit, Create Issue, or Skip?            ║
║   10. REPEAT    - Until Medium-High score + tests pass           ║
║                                                                  ║
║  TARGET SCORE: Medium-High                                       ║
║    ✓ Description > 150 chars, ≤ 60 words                         ║
║    ✓ Has "WHEN:" trigger phrases (preferred)                     ║
║    ✓ No "DO NOT USE FOR:" (unless disambiguation-critical)         ║
║    ✓ SKILL.md < 500 tokens (soft limit)                          ║
║                                                                  ║
║  MORE INFO:                                                      ║
║    See .github/skills/sensei/README.md for full documentation    ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

When to Use
Improving a skill's frontmatter compliance score
Adding trigger phrases and anti-triggers to skill descriptions
Batch-improving multiple skills at once
Auditing and fixing Low-adherence skills
Invocation Modes
Single Skill
Run sensei on azure-deploy

Multiple Skills
Run sensei on azure-security, azure-observability

By Adherence Level
Run sensei on all Low-adherence skills

All Skills
Run sensei on all skills

GEPA Mode (Deep Optimization)
Run sensei on my-skill --gepa
Run sensei on my-skill --gepa --skip-integration
Run sensei on all skills --gepa


When --gepa is used, Step 5 (IMPROVE) is replaced with GEPA evolutionary optimization. Instead of template-based improvements, GEPA parses trigger prompt arrays from the existing test harness and combines them with content quality heuristics to build a fitness function. An LLM proposes and evaluates many candidate improvements automatically. Note: GEPA does not execute Jest tests directly — it uses the test data (prompts) as evaluation inputs.

GEPA score-only mode (no LLM calls, just evaluate current quality):

Run sensei score my-skill
Run sensei score all skills

The Ralph Loop

For each skill, execute this loop until score >= Medium-High AND tests pass:

READ - Load plugin/skills/{skill-name}/SKILL.md, tests, and token count
SCORE - Run spec-based compliance check (see SCORING.md):
Validate name per agentskills.io spec (no --, no start/end -, lowercase alphanumeric)
Check description length and word count (≤60 words)
Check triggers (WHEN: preferred, USE FOR: accepted)
Warn on "DO NOT USE FOR:" (risky in multi-skill environments — exception: REQUIRED for skills that share trigger overlap with broader skills like azure-prepare)
Preserve optional spec fields (license, metadata, allowed-tools) if present
CHECK - If score >= Medium-High AND tests pass → go to TOKENS step
SCAFFOLD - If tests/{skill-name}/ doesn't exist, create from tests/_template/
IMPROVE FRONTMATTER - Add WHEN: triggers (stay under 60 words and 1024 chars) 5b. IMPROVE WITH GEPA (when --gepa flag is set) — Replaces step 5 (IMPROVE FRONTMATTER) with automated optimization; step 6 (IMPROVE TESTS) still runs normally:
Auto-discovers tests/{skill-name}/triggers.test.ts and extracts prompt arrays
Builds a GEPA evaluator scoring content quality + trigger accuracy based on those trigger prompt arrays (not Jest test pass/fail results)
Runs python .github/skills/sensei/scripts/gepa/auto_evaluator.py optimize --skill {skill-name} --skills-dir plugin/skills --tests-dir tests
Shows diff of optimized SKILL.md for user approval
GEPA uses existing test trigger definitions as configuration — it does not execute, replace, or modify Jest tests
IMPROVE TESTS - Update shouldTriggerPrompts and shouldNotTriggerPrompts to match the finalized frontmatter (including any GEPA changes)
VERIFY - Run cd tests && npm test -- --testPathPatterns={skill-name}
VALIDATE REFERENCES - Run cd scripts && npm run references {skill-name} to check markdown links
TOKENS - Check token budget and line count (< 500 lines per spec), gather optimization suggestions
SUMMARY - Display before/after comparison with unimplemented suggestions
PROMPT - Ask user: Commit, Create Issue, or Skip?
REPEAT - Go to step 2 (max 5 iterations per skill)
Scoring Criteria (Quick Reference)

Sensei validates skills against the agentskills.io specification. See SCORING.md for full details.

Score	Requirements
Invalid	Name fails spec validation (consecutive hyphens, start/end hyphen, uppercase, etc.)
Low	Basic description, no explicit triggers
Medium	Has trigger keywords/phrases, description > 150 chars, >60 words
Medium-High	Has "WHEN:" (preferred) or "USE FOR:" triggers, ≤60 words
High	Medium-High + compatibility field

Target: Medium-High (distinctive triggers, concise description)

⚠️ "DO NOT USE FOR:" is risky in multi-skill environments (15+ overlapping skills) — causes keyword contamination on fast-pattern-matching models. Safe for small, isolated skill sets. Use positive routing with WHEN: for cross-model safety.

Exception — disambiguation-critical skills: When a skill's USE FOR triggers directly overlap with a broader skill (e.g., azure-prepare owns "deploy to Azure"), DO NOT USE FOR: is REQUIRED to prevent the broader skill from capturing prompts that belong to the specialized skill. Removing it causes routing regressions. Integration tests validate this routing -- run them before removing any DO NOT USE FOR: clause.

Strongly recommended (reported as suggestions if missing):

license — identifies the license applied to the skill
metadata.version — tracks the skill version for consumers
Frontmatter Template

Per the agentskills.io spec, required and optional fields:

---
name: skill-name
description: "[ACTION VERB] [UNIQUE_DOMAIN]. [One clarifying sentence]. WHEN: \"trigger 1\", \"trigger 2\", \"trigger 3\"."
license: MIT
metadata:
  version: "1.0"
# Other optional spec fields — preserve if already present:
# metadata.author: example-org
# allowed-tools: Bash(git:*) Read
---


IMPORTANT: Use inline double-quoted strings for descriptions. Do NOT use >- folded scalars (incompatible with skills.sh). Do NOT use | literal blocks (preserves newlines). Keep total description under 1024 characters and ≤60 words.

⚠️ "DO NOT USE FOR:" carries context-dependent risk. In multi-skill environments (10+ skills with overlapping domains), anti-trigger clauses introduce the very keywords that cause wrong-skill activation on Claude Sonnet and fast-pattern-matching models (evidence). For small, isolated skill sets (1-5 skills), the risk is low. When in doubt, use positive routing with WHEN: and distinctive quoted phrases.

Exception: DO NOT USE FOR: is REQUIRED when a specialized skill's triggers overlap with a broader skill (e.g., azure-hosted-copilot-sdk vs. azure-prepare on "deploy to Azure"). Without the negative discriminator, the broader skill captures prompts that should route to the specialized one. Always run integration tests before removing a DO NOT USE FOR: clause.

Test Scaffolding

When tests don't exist, scaffold from tests/_template/:

cp -r tests/_template tests/{skill-name}


Then update:

SKILL_NAME constant in all test files
shouldTriggerPrompts - 5+ prompts matching new frontmatter triggers
shouldNotTriggerPrompts - 5+ prompts matching anti-triggers

Commit Messages:

sensei: improve {skill-name} frontmatter

Constraints
Only modify plugin/skills/ - these are the Azure skills used by Copilot
.github/skills/ contains meta-skills like sensei for developer tooling
Max 5 iterations per skill before moving on
Description must stay under 1024 characters
SKILL.md should stay under 500 tokens (soft limit)
Tests must pass before prompting for action
User chooses: Commit, Create Issue, or Skip after each skill
Flags
Flag	Description
--skip-integration	Skip integration tests for faster iteration. Only runs unit and trigger tests.
--gepa	Use GEPA evolutionary optimization instead of template-based improvement. Auto-discovers tests and builds evaluator at runtime.

⚠️ Skipping integration tests speeds up the loop but may miss runtime issues. Consider running full tests before final commit.

Reference Documentation
SCORING.md - Detailed scoring criteria
LOOP.md - Ralph loop workflow details
EXAMPLES.md - Before/after examples
TOKEN-INTEGRATION.md - Token budget integration
Related Skills
markdown-token-optimizer - Token analysis and optimization
skill-authoring - Skill writing guidelines
Weekly Installs
1.1K
Repository
microsoft/githu…or-azure
GitHub Stars
202
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass