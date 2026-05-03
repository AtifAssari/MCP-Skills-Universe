---
title: audit-dead-code
url: https://skills.sh/sebkay/skills/audit-dead-code
---

# audit-dead-code

skills/sebkay/skills/audit-dead-code
audit-dead-code
Installation
$ npx skills add https://github.com/sebkay/skills --skill audit-dead-code
SKILL.md
Audit Dead Code

Audit reachability before deleting anything. Build a proof chain from live entrypoint to candidate, then apply the smallest safe removal.

Follow this workflow
Map the codebase entrypoints, public surfaces, and dynamic loading surfaces in scope.
Search for references from public surfaces inward, not just from the candidate itself.
Classify each candidate as unused export, unreachable code, orphaned file, stale feature flag, dead registration, or legacy compatibility path.
Build a proof chain with code search, config or registry checks, framework conventions, and typecheck, build, or tests where available.
Prioritize findings as P1 through P4.
Auto-fix only local, low-risk removals. Leave broader deletions as findings with a concrete removal plan.
Map live entrypoints first

Do not start deleting from leaf files without understanding how code can be reached.

Inspect the relevant equivalents of:

routes, controllers, pages, and API handlers
package exports, workspace boundaries, and public modules
CLI commands and scheduled jobs
queues, workers, and event subscribers
dependency-injection or service-container registration
framework auto-discovery and naming conventions
plugin manifests, registries, and config-driven loading
dynamic imports, reflection, and string-based dispatch
tests, fixtures, storybook stories, and demo apps
build scripts, codegen inputs, and release tooling

Dead code claims are weak until these entrypoints are checked.

Search for dead-code signals

Start with the language-appropriate equivalents of:

import
require
export
public
function
class
interface
type
const
enum
if (false)
if (FLAG)
else
switch
default
return
throw
break
continue
deprecated
legacy
TODO remove
unused
feature flag
register
route
command

Also inspect:

files with no inbound imports
modules imported only by other suspected-dead modules
modules re-exported but never consumed
path aliases, barrels, or registries that may hide the last live reference
duplicate implementations behind old/new paths
branches gated by flags that are permanently on or off
code after unconditional return, throw, or exhaustive matches
adapters kept only for migrations that already finished
Build a proof chain

Treat "no references found" as a starting signal, not proof.

Prefer at least two independent pieces of evidence when possible:

repo search shows no live callers after checking aliases, barrels, generated paths, and test-only consumers
no route, command, registry, manifest, config, or package export points at the candidate
framework conventions and auto-discovery rules do not require it by name or location
removing it keeps typecheck, build, and targeted tests green when those checks exist
feature-flag source of truth shows the branch is permanently on or off
public-surface review finds no external or cross-workspace consumers you can verify

If evidence depends on a system you cannot inspect locally, downgrade the claim to a finding with missing proof instead of deleting.

Detect these dead-code patterns
Unused exports

Flag exported values that have no live consumers.

Common signals:

exported helper, component, hook, class, or constant with zero references outside its file
barrel exports that expose symbols never imported anywhere
public methods required by no interface, subclass, or framework hook
package exports left behind after an internal refactor

Verify framework conventions before deleting. Some exports are consumed by reflection, auto-registration, templates, external packages, or sibling workspaces.

Unreachable code

Flag code paths that normal execution cannot enter.

Common signals:

statements after return, throw, break, or continue
if or switch branches guarded by impossible conditions
fallback branches after exhaustive enum or union handling
code behind version checks or environment gates that can no longer occur

Prefer proving why the branch is impossible, not just that it looks suspicious.

Orphaned files

Flag files, directories, or modules with no live entrypoint.

Common signals:

module not imported, registered, routed, or referenced by config
page, component, job, or worker replaced by a new implementation but never removed
fixture, test helper, or mock file not referenced by any tests
scripts that are no longer invoked by package scripts, CI, cron, or docs

Check for out-of-repo or cross-workspace consumers before deleting shared packages or public artifacts.

Stale feature flags

Flag flags whose rollout is finished but both paths still remain.

Common signals:

flag is always on or always off in current config
old branch is still present long after migration or launch
flag name includes a completed rollout, migration, or temporary workaround
kill switch exists but no owner, expiry, or current use remains

Confirm the source of truth for the flag. Code search alone is not enough if flags are managed remotely.

Dead registrations and compatibility layers

Flag code kept only to support paths that no longer exist.

Common signals:

event listeners subscribed to events no producer emits
adapters for old payload shapes after all producers migrated
deprecated routes, commands, or aliases with no callers
serializer fields kept for clients that no longer exist

These often survive because the registration site looks live even though the upstream caller is gone.

Guard against false positives

Dead-code audits are easy to get wrong where usage is indirect.

Be careful around:

reflection and runtime method lookup
DI container resolution by string or class name
framework auto-discovery by filename or folder
dynamic imports and lazy loading
package exports, CLI bin entries, or monorepo workspace consumers
generated registries, manifests, or codegen that recreate the reference chain
templates that reference symbols indirectly
code generation inputs and generated outputs
public SDK or package APIs consumed outside the repo
migrations, backfills, and historical one-off scripts that are intentionally retained
feature flags controlled in remote dashboards or environment management

If reachability depends on conventions or external systems, report the finding with the missing proof instead of deleting speculatively.

Classify findings
P1

Use for dead paths that actively create risk: stale flags masking security, billing, or data-integrity behavior, duplicate write paths that can diverge, or unreachable rollback logic that operators may believe still works.

P2

Use for dead code in active boundaries: orphaned routes, handlers, jobs, or compatibility layers that increase maintenance cost or hide which path is truly live.

P3

Use for routine cleanup: unused exports, unreachable local branches, dead helpers, unreferenced tests, or unused files with low behavioral risk.

P4

Use for cosmetic leftovers: comments referencing removed flags, empty barrels, deprecated aliases with obvious replacements, or cleanup that does not materially affect maintenance risk.

Auto-fix only when safe

Auto-fix local removals when proof is strong and the blast radius is contained.

Safe examples:

remove statements after unconditional return or throw
delete a private helper or local constant with zero references in one module
remove an import/export pair that is unused and not part of a public surface
collapse a stale flag branch when the live branch is unambiguous and locally verified
delete an orphaned test helper or fixture with no references

Do not auto-fix without explicit approval when the change affects:

public APIs, SDKs, or package exports
framework conventions or auto-discovery
dynamic loading or reflection
remote feature-flag systems
database migrations, backfills, or compliance artifacts
shared build, CI, release, or deployment scripts
cross-repo consumers you cannot verify locally

For those, report the finding and recommend the smallest removal plan.

Choose the smallest defensible fix

Prefer this order:

Remove the dead leaf code.
Remove imports, exports, and registrations that only existed for it.
Remove stale tests or fixtures tied only to the deleted path.
Remove the flag or compatibility shim if both sides are now gone.
Stop once the live path is simpler and still verified.

Avoid broad "cleanup passes" that mix proven dead code with speculative simplification.

Report findings in this format

List findings first, highest severity first.

For each finding, include:

priority: P1 to P4
dead-code type: unused export, unreachable code, orphaned file, stale feature flag, dead registration, or compatibility layer
location: file and line or the smallest concrete scope available
proof chain: what references, registries, conventions, and validation checks were used
false-positive risk: dynamic loading, external consumers, or unknowns
recommended fix
whether it is safe to auto-fix now

If no issues are found, say so explicitly and mention which entrypoints and dynamic-loading surfaces were checked plus any remaining blind spots.

Default review stance
Prefer proof over suspicion
Prefer deletion over deprecation once reachability is disproven
Prefer contained removals over broad cleanups
Prefer preserving live entrypoints over chasing local neatness
Prefer findings with concrete reference evidence over style commentary
Weekly Installs
18
Repository
sebkay/skills
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass