---
rating: ⭐⭐⭐
title: llm-boost
url: https://skills.sh/ven0m0/claude-config/llm-boost
---

# llm-boost

skills/ven0m0/claude-config/llm-boost
llm-boost
Installation
$ npx skills add https://github.com/ven0m0/claude-config --skill llm-boost
SKILL.md
LLM Boost Skill

Optimize all LLM-facing content: documentation, skills, prompts, and parameters.

Quick Reference
Area	Key Metric	Target
c7score	Question-Snippet Match	80% weight
Skills	SKILL.md size	<=500 lines
LLM Tuning	Task-appropriate settings	See tuning table
Documentation Optimization (c7score)
Analyze: Read README.md, docs/*.md
Generate questions: Create 15-20 "How do I..." questions covering setup, auth, basic usage, errors, advanced features, integrations
Map questions to snippets: Mark complete, partial, or missing (prioritize missing)
Optimize by priority:
Priority	Weight	Action
P1: Question coverage	80%	Add complete code for unanswered questions
P2: Remove duplicates	5%	Consolidate similar snippets
P3: Fix formatting	5%	Proper language tags, TITLE/DESCRIPTION/CODE
P4: Remove metadata	5%	Strip licensing, directory trees, citations
P5: Enhance init	5%	Combine import-only with usage examples
Validate each snippet: runs standalone, answers specific question, proper format, includes imports
Score before vs after across all 5 metrics
Snippet Transformation Patterns
API ref to usage example: Replace method signatures with complete working code including imports, setup, and expected output
Import-only to complete setup: Combine from lib import X with actual usage showing real output
Multiple fragments to one comprehensive: Merge related 1-2 line snippets into one complete workflow
Remove metadata: Strip directory trees, license text, BibTeX citations entirely

For detailed patterns: references/optimization_patterns.md

llms.txt Generation

<format_rules>

H1 title required, H2 sections only (no H3+)
Full URLs with protocol, prefer .md files
- [Title](url): description link format
"Optional" section = skippable for shorter context
No code blocks, images, or complex formatting
Place at repo root as /llms.txt </format_rules>
Project Type	Must Have	Should Have
Library	Documentation, API Reference, Examples	Getting Started, Development
CLI Tool	Getting Started, Commands, Examples	Configuration, Development
Framework	Documentation, Guides, API Reference, Examples	Integrations

For templates: examples/sample_llmstxt.md

Skill Optimization
500-Line Rule

Keep in SKILL.md: purpose, quick start, critical practices, brief examples (5-10 lines), cross-references. Move to reference files: API docs, extensive examples (>20 lines), troubleshooting, pattern libraries, schemas.

Optimization Modes
Mode	Size	Action
Light	<3K tokens	Tighten wording, add YAML if missing
Standard	3K-6K	Consolidate, tables over prose, one example
Aggressive	6K-10K	Table everything, strip filler
Split	>=10K	Propose 3-4 files + index
YAML Frontmatter

Description field (max 1024 chars) must include: what the skill does, when to use it, key technologies, action verbs. Write in third person.

Progressive Disclosure Pattern
## Topic Overview
Brief explanation (2-3 sentences).

**Quick Example:**
(5-10 line code block)

**For detailed docs**: [REFERENCE.md](REFERENCE.md#topic)

XML Tag Structuring

<design_principles>

Principle	Guideline
Semantic naming	Tag names describe content: <contract>, <rubric>
Consistency	Same tag names throughout; reference by name in instructions
Nesting	<outer><inner></inner></outer> for hierarchy
No canonical tags	No "best" tags - name for your use case
Combine techniques	Pair with CoT (<thinking>/<answer>) and multishot (<examples>)

</design_principles>

Core Patterns

Multi-document: <documents><document index="1"><source>...</source><content>...</content></document></documents>

Structured evaluation: <rubric> + <submission> -> <evaluation><score> + <feedback>

CoT separation: <thinking> for reasoning, <answer> for final output

Multishot examples: <examples><example><input>...</input><output>...</output></example></examples>

Guard rails: <instructions><task>...</task><formatting>...</formatting><constraints>...</constraints></instructions>

Output Extraction
import re

def extract_tag(text, tag):
    match = re.search(f'<{tag}>(.*?)</{tag}>', text, re.DOTALL)
    return match.group(1).strip() if match else None


For comprehensive tag catalog: references/xml_tags.md

LLM Parameter Tuning
Task	max_tokens	temperature	top_p	Rationale
Theorem proving	4096	0.6	0.95	CoT needs space; higher temp explores tactics
Code generation	2048	0.2-0.4	-	Deterministic preferred
Creative/exploration	4096	0.8-1.0	-	Maximum diversity
Classification	256	0.0-0.1	-	Consistency over creativity
Summarization	1024	0.3	-	Faithful to source
CLAUDE.md Audit Checklist
Check	How
Tech stack claims	Read("package.json|Cargo.toml")
File path references	Glob("claimed/path")
Command references	Grep("script", glob="package.json")
Testing framework	Glob("**/*.test.*")
Linting config	Glob("**/biome.json|**/.eslintrc*")
Line count	wc -l CLAUDE.md - target <300
No code duplication	Uses file:line pointers
WHAT/WHY/HOW structure	Manual review
Reference Materials
c7score Metrics - scoring rubrics and weights
Optimization Patterns - snippet transformation patterns
llms.txt Format - complete format specification
XML Tag Patterns - comprehensive tag catalog
Skill Optimization - 3-level loading, migration workflow
Weekly Installs
20
Repository
ven0m0/claude-config
GitHub Stars
1
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass