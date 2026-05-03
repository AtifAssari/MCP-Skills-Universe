---
rating: ⭐⭐
title: organize-elixir-functions
url: https://skills.sh/jasonharmongit/jh-skills/organize-elixir-functions
---

# organize-elixir-functions

skills/jasonharmongit/jh-skills/organize-elixir-functions
organize-elixir-functions
Installation
$ npx skills add https://github.com/jasonharmongit/jh-skills --skill organize-elixir-functions
SKILL.md
Scope Mode
File mode: if a file path is provided, only organize that file.
Branch mode: if no file path is provided, inspect changed files on the current branch and organize files that need updates.
To see ALL changes made on the branch, always check:
committed branch-only changes: git diff --name-status "$(git merge-base HEAD main)"...HEAD
all working tree changes: git status --short
Selection Mode
Changed-only mode (default):
only organize candidate functions touched on the current branch
candidate functions are newly added, renamed, or changed visibility (def <-> defp)
place candidate functions using this skill's ordering rules (see Ordering Rules below), not ad hoc file habits
do not keep candidate functions anchored near the edit area if that conflicts with proper placement
do not move untouched function definitions, even if out of order
Override mode (explicit request only):
organize all functions in the selected scope, including unchanged definitions
Precedence over file conventions
These rules outrank local or file-specific habits. If the file clusters related helpers together, keeps private functions near their call sites, or otherwise departs from the ordering below, still place candidate (changed) functions according to this skill.
Do not preserve a one-off layout for edited code when it conflicts with Ordering Rules (for example, grouping related functions out of typical order). Correct placement for touched definitions takes priority over "staying consistent" with a non-standard arrangement elsewhere in the file.
In changed-only mode, leave untouched definitions where they are even when the file mixes styles; only moved candidates must follow this skill end-to-end.
Ordering Rules
LiveView modules:
use this default callback order: mount/3, handle_params/3, handle_event/3, handle_info/2, handle_async/3 (and other handlers), then render/1
keep callback groups contiguous, especially handle_event/3, handle_info/2, and handle_async/3
order handle_event/3 clauses alphabetically by event name
if render/1 is not defined in the module (for example, template-backed LiveViews), skip render-ordering rules
private functions last (defp), sorted alphabetically by function name
LiveComponent modules:
use this default callback order: mount/1, update/2, handle_event/3, handle_info/2, handle_async/3 (and other handlers), then render/1
keep callback groups contiguous, especially update/2 and handle_event/3
order handle_event/3 clauses alphabetically by event name
private functions last (defp), sorted alphabetically by function name
Non-LiveView modules:
public functions first (def), sorted alphabetically by function name
private functions last (defp), sorted alphabetically by function name
Test modules:
order test blocks so the happy path (success) case comes first for a given behavior; place related error-path tests immediately after that happy path (not interleaved with other features)
when reordering, keep describe / test groupings consistent with this: success scenario first, then its failure/edge cases in the same cluster
private functions last (defp), sorted alphabetically by function name
Structural Safety Rules
Treat all clauses of the same function name and arity as one unit.
Preserve existing pattern-match clause order unless explicitly asked to change behavior.
Keep callback clause groups contiguous (for example, all handle_params/3 clauses together).
Keep each moved function body unchanged except for location.
Preserve module structure, comments, spacing conventions, and non-function code.
Output Expectations
Move each candidate function to its correct ordered position in the file, even when that means crossing the original change area.
In changed-only mode:
file mode: if the target file has no candidate functions, make no reordering changes
branch mode: skip files with no candidate functions and only modify files that need reordering
In override mode, organize all functions in the selected scope, even if definitions are unchanged.
Preserve behavior: do not make ordering changes that alter pattern matching outcomes.
In LiveView and LiveComponent modules, callback lifecycle order wins over alphabetical order.
Weekly Installs
27
Repository
jasonharmongit/jh-skills
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass