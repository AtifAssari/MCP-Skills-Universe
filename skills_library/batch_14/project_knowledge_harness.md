---
title: project-knowledge-harness
url: https://skills.sh/daviddwlee84/agent-skills/project-knowledge-harness
---

# project-knowledge-harness

skills/daviddwlee84/agent-skills/project-knowledge-harness
project-knowledge-harness
Installation
$ npx skills add https://github.com/daviddwlee84/agent-skills --skill project-knowledge-harness
SKILL.md
project-knowledge-harness

A lightweight, file-based memory harness for any software project.

Three surfaces, sharply separated by time direction and access pattern:

Surface	Time	Question it answers	Access pattern
TODO.md	Future	"What might we do later?"	Read top to bottom (priority lanes)
backlog/<slug>.md	Future	"What was the analysis behind this idea?"	Indexed from TODO.md
pitfalls/<slug>.md	Past	"I see error X — has this happened before?"	Grep symptom keywords

Plus, in projects that already have agent contracts, AGENTS.md Hard invariants answer "What rules MUST agents follow?". Pitfalls graduate to Hard invariants when serious enough — see references/when-to-add-docs.md.

When to use this skill

Use this skill when the user surfaces any of:

A long-term TODO list with no home, or a messy TODO.md that needs structure (signals: "where should ideas go?", "maybe later", "工程量太大需要再評估")
A debugging session worth saving (signals: "keep solving the same problem twice", "save this troubleshooting", "踩過的坑", "TROUBLESHOOTING.md scattered across docs/")
A request to consolidate IDEAS.md / ROADMAP.md / WISHLIST.md / LESSONS.md files

Do NOT use this skill for active sprint planning (use issue trackers), ephemeral agent scratchpads (use .claude/plans/), or current feature documentation (use docs/).

How to apply this skill (default workflow)

The skill bundles five scripts and several templates. Default to the init script for setup, and default to add-todo.sh / sweep-inbox.sh for capture rather than asking the agent to edit TODO.md by hand.

scripts/
  init.sh         # one-shot setup of TODO.md + backlog/ + pitfalls/
                  # + agent guidance + README snippet
  todo-kanban.sh  # validate TODO.md format and render kanban-style board
  add-todo.sh     # insert a structured entry into the right ## P* lane
  promote-todo.sh # move an active TODO item to ## Done with the right syntax
  sweep-inbox.sh  # triage backlog/inbox.md into TODO.md via add-todo.sh

1. Run scripts/init.sh against the target repo
scripts/init.sh \
  --target /path/to/project \
  --project-name "My Project" \
  --deployment chezmoi   # or npm | pip | docker | none


The script:

Creates TODO.md, backlog/README.md, pitfalls/README.md from assets/*.template, substituting placeholders.
Appends an agent-guidance snippet to AGENTS.md / CLAUDE.md (auto-detected, override with --agent-contract).
Appends a "Roadmap & lessons learned" section to README.md.
Runs scripts/todo-kanban.sh --validate-only TODO.md so any drift is caught immediately.
Prints the deployment-exclusion lines you should add manually (it does not edit ignore files — see references/deployment-exclusion.md).

init.sh is idempotent: existing files are skipped unless --force is given, and snippets append only if a sentinel marker is missing.

2. Mid-conversation, when the user surfaces a "maybe later" idea

Signals: "maybe later", "nice to have", "if I'm interested", "工程量太大需要再評估", "先記下來", "not now but…".

If TODO.md doesn't exist yet, run scripts/init.sh first.

Default path — call scripts/add-todo.sh with the priority, effort, title, and description. This inserts the canonical line into the right ## P* lane and re-validates. Add --backlog if the conversation produced enough investigation that a backlog/<slug>.md doc is worth scaffolding.

scripts/add-todo.sh --priority "P?" --effort M \
  --title "Try Rspress for docs" \
  --description "Evaluate AI-native docs framework alternative"


Quick-capture path — append to backlog/inbox.md when the user isn't sure of priority/effort yet, or is mid-thought:

echo "- $UNSTRUCTURED_THOUGHT" >> backlog/inbox.md


Later (this session or next), run scripts/sweep-inbox.sh to formalize the loose lines into TODO.md one at a time. The sweeper prompts for missing fields per line; in --batch mode it only processes lines that already have priority=… effort=… title="…" description="…" pairs and leaves ambiguous ones in place.

Manual edit path — only when scripts can't help. Use the syntax from references/tag-schema.md and run scripts/todo-kanban.sh --validate-only afterwards.

If you wrote a backlog/<slug>.md (either via --backlog or by hand), make sure the TODO line ends with → [research](backlog/<slug>.md) so the index points to the doc.

3. Mid-conversation, when you finish debugging something tricky

Signals: "phew, that took a while", "weird, the error didn't say anything about X", "this is the third time we've hit this", or you find yourself reconstructing context that isn't in any doc.

Create pitfalls/<symptom-slug>.md immediately from assets/pitfall-doc.md.template, while the trace is fresh. Title the doc by the symptom, not the root cause — you'll search by what you're seeing, not by what you eventually learned.
Copy verbatim error messages — never paraphrase, it kills grep-ability.
If the trap is severe (silent corruption / cross-machine recurrence / non-obvious workaround), surface it: "should this graduate to a Hard invariant in AGENTS.md?" — see references/when-to-add-docs.md.
4. When implementing a TODO.md item

In the same commit:

Run scripts/promote-todo.sh --title "<substring>" --summary "<what shipped>". It removes the active line and inserts the dated Done entry, then re-validates. It refuses to run if the substring matches zero or more than one active item.
If a backlog/<slug>.md exists, set its Status: shipped (don't delete — historical record may inform adjacent decisions).
If shipping uncovered a trap, write a pitfalls/<slug>.md for it.
When a TODO entry needs a backlog/ doc, when a debug needs a pitfalls/ doc

Decision rules and the upgrade path to AGENTS.md invariants live in references/when-to-add-docs.md. Read it the first time you set up the harness; consult it again whenever you're unsure which surface a piece of knowledge belongs in.

Tag schema

Two orthogonal axes, validated by scripts/todo-kanban.sh. See references/tag-schema.md for the full schema, useful tag combinations, and the exact validator-checked syntax.

Anti-patterns

Common mistakes to avoid (e.g., spawning IDEAS.md alongside TODO.md, titling pitfalls by root cause, paraphrasing errors). Full list in references/anti-patterns.md.

Deployment exclusion

TODO.md, backlog/, and pitfalls/ are maintainer-facing repo metadata, not files to ship. Cheatsheet for chezmoi / npm / pip / Docker in references/deployment-exclusion.md. scripts/init.sh --deployment ... prints the exact lines to add.

Templates and bundled assets
assets/TODO.md.template — TODO.md skeleton with example items per lane
assets/backlog-README.md.template — backlog/ index + when-to-add rules
assets/backlog-doc.md.template — single backlog doc (context-first)
assets/pitfalls-README.md.template — pitfalls/ index + cross-reference table for traps documented elsewhere
assets/pitfall-doc.md.template — single pitfall doc (symptom-first)
assets/agent-guidance.md.template — snippet for AGENTS.md / CLAUDE.md
assets/readme-roadmap.md.template — snippet for project README.md
scripts/init.sh — one-shot setup
scripts/todo-kanban.sh — validator + Markdown kanban renderer (also supports --json and --validate-only)
scripts/add-todo.sh — structured insert into ## P* lane; --backlog also scaffolds backlog/<slug>.md
scripts/promote-todo.sh — atomic active-→-Done move with re-validation
scripts/sweep-inbox.sh — triage backlog/inbox.md → add-todo.sh
Reference implementation

A live example of this harness is at daviddwlee84/dotfiles:

TODO.md, backlog/, pitfalls/ directories at repo root
AGENTS.md ### Long-term backlog → TODO.md + backlog/ and ### Past pitfalls → pitfalls/ sections
README.md ## Roadmap & lessons learned section
Weekly Installs
11
Repository
daviddwlee84/ag…t-skills
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass