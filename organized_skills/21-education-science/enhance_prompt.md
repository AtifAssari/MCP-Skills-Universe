---
rating: ⭐⭐⭐
title: enhance-prompt
url: https://skills.sh/jkappers/agent-skills/enhance-prompt
---

# enhance-prompt

skills/jkappers/agent-skills/enhance-prompt
enhance-prompt
Installation
$ npx skills add https://github.com/jkappers/agent-skills --skill enhance-prompt
SKILL.md
Prompt Enhancement

Analyze, write, and improve LLM prompts and agent instructions. Apply these principles to system prompts, agent instructions, skills, CLAUDE.md files, rules, slash commands, and any LLM prompt.

Workflow

When invoked with input:

Classify the request: Determine if the input is a prompt to review, a description of a prompt to write, or a general prompt engineering question
Analyze: For existing prompts, identify violations of the principles below. For new prompts, gather requirements
Apply principles: Apply Token Economics, Determinism, Imperative Language, Formatting, and Anti-Pattern checks
Produce output: Return the enhanced prompt only
Output Format

Return the enhanced prompt only. No preamble, no violation notes, no commentary, no explanations. The entire response is the improved prompt, ready to copy and paste.

When invoked without input, serve as a reference guide for the principles below.

Token Economics

The context window is a shared resource. Challenge each piece of information: "Does the model already know this?" Only add context the model lacks. Assume high baseline capability.

Remove decorative language. No "please", "remember", "make sure", "it's important".

Use examples over explanations. One concrete before/after pair teaches more than three paragraphs of description.

Prefer tables for structured data. Compress related information into scannable format.

Determinism and Specificity
Degrees of Freedom

Match specificity to task requirements.

High freedom (text instructions): Use when multiple approaches are valid. Medium freedom (pseudocode, parameterized scripts): Use when a preferred pattern exists. Low freedom (exact scripts, no parameters): Use when operations are fragile or consistency is critical.

Zero Ambiguity

Every instruction must have exactly one interpretation.

Use explicit constraints, not suggestions. "Run pytest tests/ --strict-markers" not "Run tests with strict markers when appropriate."

Specify conditions completely. "Validate input at API boundaries" not "Validate input."

Eliminate hedge words: "consider", "try to", "when possible", "generally", "often".

Deterministic Commands

Include all flags and arguments. dotnet test --logger "console;verbosity=detailed" not dotnet test.

Use absolute paths or precisely scoped paths. /src/api/, src/**/*.ts, not "the API code."

Specify tool versions when behavior differs. "Node.js 20+: use native fetch" not "Use fetch."

Imperative Language Patterns

Use imperative form only. "Validate at boundaries" not "You should validate at boundaries."

Write direct commands in imperative mood.

Good: "Validate input at API boundaries" Avoid: "You should consider validating input"

Prefer positive instructions over negations. "Let exceptions propagate" rather than "Do not catch exceptions unnecessarily."

Specificity in Constraints

Be specific in prohibitions and requirements.

Good: "Do not implement retry logic in background jobs" Avoid: "Avoid defensive patterns"

Formatting for LLM Parsing

Use markdown structure that aids LLM understanding.

Format	Purpose
Headings	Establish context and scope boundaries
Lists	Discrete, parallel, independent items only
Code blocks	Exact values, commands, identifiers, patterns
Tables	Structured comparisons, reference data, decision matrices
Bold	Hard constraints where violation causes failure (max 10% of content)
Prose	Relationships between ideas, conditional logic, rationale
White space	Blank lines between paragraphs and sections for parsing clarity
Emphasis and Terminology
Emphasis Modifiers

Use MUST, MUST NOT, REQUIRED only for hard constraints where violation causes failure.

Do not use modifiers for preferences or defaults. If every instruction uses MUST, none stand out.

Terminology Consistency

Choose one term per concept and use it throughout.

Good: Always "API endpoint" Avoid: Alternating "API endpoint", "URL", "route", "path"

Structural Optimization

Place critical constraints first. Most important information at top of file.

Use progressive specificity. Global rules first, then domain-specific, then file-specific.

Separate concerns cleanly. One section per topic. Do not mix testing rules with deployment procedures.

End sections decisively. No trailing "etc." or "and more."

Common Anti-Patterns
Language Anti-Patterns

Suggestion language:

Avoid: "Consider using async/await"
Good: "Use async/await for I/O operations"

Vague quantifiers:

Avoid: "Usually validate input"
Good: "Validate input at API boundaries"

Ambiguous conditionals:

Avoid: "Add logging when appropriate"
Good: "Log errors with stack traces. Omit logging for expected control flow."

Multiple options without default:

Avoid: "Use Jest, Vitest, or Mocha for testing"
Good: "Use Vitest for tests. Jest acceptable for legacy files."
Structural Anti-Patterns

Burying critical constraints:

Avoid: Long preamble, then critical requirement in middle
Good: Critical requirement first, context after if needed

Over-emphasis:

Avoid: Every other word bold
Good: Bold only for hard constraints where violation causes failure

Lists as default:

Avoid: Everything formatted as bulleted list
Good: Lists for discrete items, prose for relationships
Content Anti-Patterns

Repeating framework documentation:

Avoid: "React hooks let you use state and lifecycle in function components..."
Good: "Store form state in URL params, not local state"

Generic best practices:

Avoid: "Functions should be small and focused"
Good: "Limit API handlers to routing only. Move logic to services/"

Time-sensitive information:

Avoid: "Before August 2025, use legacy API"
Good: "Use v2 API at api.example.com/v2/"

Decorative content: Welcome messages, motivational statements, background history.

Hypothetical scenarios: "If we ever migrate to Postgres..." Address when actual, not hypothetical.

Optimization Techniques
Sentence Compression

Remove filler:

Before: "You should make sure to always run the test suite before committing your changes"
After: "Run pytest before committing"

Combine related instructions:

Before: "Use TypeScript. Add type annotations. Enable strict mode."
After: "Use TypeScript strict mode with explicit type annotations"
Command Specification

Full specification:

## Commands
- `pytest tests/ --strict-markers --cov=src --cov-report=html`: Run tests with coverage
- `dotnet build --configuration Release --no-restore`: Production build
- `npm run lint -- --fix`: Auto-fix linting issues


Not:

## Commands
Run pytest to test. Use dotnet build for building. Lint with npm.

Weekly Installs
32
Repository
jkappers/agent-skills
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass