---
title: learn
url: https://skills.sh/boshu2/agentops/learn
---

# learn

skills/boshu2/agentops/learn
learn
Installation
$ npx skills add https://github.com/boshu2/agentops --skill learn
SKILL.md
Learn Skill

YOU MUST EXECUTE THIS WORKFLOW. Do not just describe it.

Capture knowledge manually for future sessions. Fast path to feed the knowledge flywheel without running a full retrospective.

Flags
Flag	Default	Description
--global	off	Write to ~/.agents/learnings/ instead of .agents/knowledge/pending/. Use for knowledge that applies across all projects.
--promote	off	Promote a local learning to global. Reads local file, abstracts repo context, writes to ~/.agents/learnings/, marks local with promoted_to:.

When to use --global: Use for knowledge that applies across all your projects (e.g., language patterns, tooling preferences, debugging techniques). Use default (no flag) for repo-specific knowledge (e.g., architecture decisions, local conventions).

When to use --promote: Use when an existing local learning turns out to be transferable. The skill reads the local file, rewrites it to remove repo-specific references, writes the abstracted version to ~/.agents/learnings/, and marks the local copy with promoted_to: frontmatter so ao inject skips it.

Execution Steps

Given /learn [content]:

Step 1: Get the Learning Content

If content provided as argument: Use it directly.

If no argument: Ask the user via AskUserQuestion: "What did you learn or want to remember?" Then collect the content in free text.

Step 2: Classify the Knowledge Type

Use AskUserQuestion to ask which type:

Tool: AskUserQuestion
Parameters:
  questions:
    - question: "What type of knowledge is this?"
      header: "Type"
      multiSelect: false
      options:
        - label: "decision"
          description: "A choice that was made and why"
        - label: "pattern"
          description: "A reusable approach or technique"
        - label: "learning"
          description: "Something new discovered (default)"
        - label: "constraint"
          description: "A rule or limitation to remember"
        - label: "gotcha"
          description: "A pitfall or trap to avoid"


Default to "learning" if user doesn't choose.

Step 3: Generate Slug

Create a slug from the content:

Take the first meaningful words (skip common words like "use", "the", "a")
Lowercase
Replace spaces with hyphens
Max 50 characters
Remove special characters except hyphens

Check for collisions:

# If file exists, append -2, -3, etc.
slug="<generated-slug>"
counter=2
if [[ "$GLOBAL" == "true" ]]; then
  base_dir="$HOME/.agents/learnings"
else
  base_dir=".agents/knowledge/pending"
fi
while [ -f "${base_dir}/$(date +%Y-%m-%d)-${slug}.md" ]; do
  slug="<generated-slug>-${counter}"
  ((counter++))
done

Step 4: Create Knowledge Directory
# If --global: write to global patterns (cross-repo)
# Otherwise: write to local knowledge (repo-specific)
if [[ "$GLOBAL" == "true" ]]; then
  mkdir -p ~/.agents/learnings
else
  mkdir -p .agents/knowledge/pending
fi

Step 5: Write Knowledge File

Path:

Default: .agents/knowledge/pending/YYYY-MM-DD-<slug>.md
With --global: ~/.agents/learnings/YYYY-MM-DD-<slug>.md

Format:

---
type: <classification>
source: manual
date: YYYY-MM-DD
---

# Learning: <short title>

**ID**: L1
**Category**: <classification>
**Confidence**: medium

## What We Learned

<content>

## Source

Manual capture via /learn


Example:

---
type: pattern
source: manual
date: 2026-02-16
---

# Learning: Token Bucket Rate Limiting
**ID**: L1
**Category**: pattern
**Confidence**: high

## What We Learned

Use token bucket pattern for rate limiting instead of fixed windows. Allows burst traffic while maintaining average rate limit. Implementation: bucket refills at constant rate, requests consume tokens, reject when empty.

Key advantage: smoother user experience during brief bursts.

## Source

Manual capture via /learn

Step 5.5: Abstraction Lint Check (global writes only)

If --global or --promote: After writing the file, grep for repo-specific indicators:

file="<path-to-written-file>"
leaks=""
leaks+=$(grep -iEn '(internal/|cmd/|\.go:|/pkg/|/src/|AGENTS\.md|CLAUDE\.md)' "$file" 2>/dev/null)
leaks+=$(grep -En '[A-Z][a-z]+[A-Z][a-z]+\.(go|py|ts|rs)' "$file" 2>/dev/null)
leaks+=$(grep -En '\./[a-z]+/' "$file" 2>/dev/null)


If any matches found: WARN the user by showing the matched lines and asking whether to proceed or revise. This does NOT block — it catches obvious repo-specific references like athena/internal/validate/audit.go:32.

If no matches: proceed silently.

Step 5.6: Promote Flow (--promote only)

Given /learn --promote <path-to-local-learning>:

Read the local learning file
Rewrite content to remove repo-specific references (file paths, function names, package names, internal architecture). Preserve the core insight.
Generate slug from the abstracted content
Write abstracted version to ~/.agents/learnings/YYYY-MM-DD-<slug>.md
Run abstraction lint check (Step 5.5)
Add promoted_to: frontmatter to the local file:
---
promoted_to: ~/.agents/learnings/YYYY-MM-DD-<slug>.md
---

ao inject skips learnings with promoted_to: set, preventing double-counting.
Confirm: "Promoted to global: ~/.agents/learnings/YYYY-MM-DD-<slug>.md"
Step 6: Integrate with ao CLI (if available)

Check if ao is installed:

if command -v ao &>/dev/null; then
  echo "✓ Knowledge saved to <path>"
  echo ""
  echo "To move this into cached memory now:"
  echo "  ao pool ingest <path>"
  echo "  ao pool list --status pending"
  echo "  ao pool stage <candidate-id>"
  echo "  ao pool promote <candidate-id>"
  echo ""
  echo "Or let hooks run close-loop automation."
else
  echo "✓ Knowledge saved to <path>"
  echo ""
  echo "Note: Install ao CLI to enable automatic knowledge flywheel."
fi


Do NOT auto-run promotion commands. The user should decide when to stage/promote.

Note: If --global or --promote is set, skip ao CLI integration. Global learnings are discovered directly by ao inject from ~/.agents/learnings/.

Step 7: Confirm to User

Tell the user:

Learned: <one-line summary from content>

Saved to: .agents/knowledge/pending/YYYY-MM-DD-<slug>.md
Type: <classification>

This capture is queued for flywheel ingestion; once promoted it is available via /research and /inject.

Key Rules
Be concise - This is for quick captures, not full retrospectives
Preserve user's words - Don't rephrase unless they ask
Use simple slugs - Clear, descriptive, lowercase-hyphenated
Ingest-compatible format - Include # Learning: block with category/confidence
No auto-promotion - User controls quality pool workflow
Examples
Quick Pattern Capture

User says: /learn "use token bucket for rate limiting"

What happens:

Agent has content from argument
Agent asks for classification via AskUserQuestion
User selects "pattern"
Agent generates slug: token-bucket-rate-limiting
Agent creates .agents/knowledge/pending/2026-02-16-token-bucket-rate-limiting.md
Agent writes frontmatter + content
Agent checks for ao CLI, informs user about ao pool ingest + stage/promote options
Agent confirms: "Learned: Use token bucket for rate limiting. Saved to .agents/knowledge/pending/2026-02-16-token-bucket-rate-limiting.md"
Interactive Capture

User says: /learn

Agent asks for content and type, generates slug never-eval-hooks, creates .agents/knowledge/pending/2026-02-16-never-eval-hooks.md, confirms save.

Gotcha Capture

User says: /learn "bd dep add A B means A depends on B, not A blocks B"

Agent classifies as "gotcha", generates slug bd-dep-direction, creates file in pending, confirms save.

Troubleshooting
Problem	Cause	Solution
Slug collision	Same topic on same day	Append -2, -3 counter automatically
Content too long	User pasted large block	Accept it. /learn has no length limit. Suggest /retro for structured extraction if very large.
ao pool ingest/stage fails	Candidate ID mismatch or ao not installed	Show exact next commands (ingest, list, stage, promote) and confirm file was saved
Duplicate knowledge	Same insight already captured	Check existing files with grep before writing. If duplicate, tell user and show existing path.
The Flywheel

Manual captures feed the same flywheel as automatic extraction:

/learn → .agents/knowledge/pending/ → ao pool ingest → .agents/learnings/ → /inject


This skill is for quick wins. For deeper reflection, use /retro.

Weekly Installs
125
Repository
boshu2/agentops
GitHub Stars
323
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass