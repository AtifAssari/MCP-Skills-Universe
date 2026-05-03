---
rating: ⭐⭐
title: sdk-install
url: https://skills.sh/launchdarkly/agent-skills/sdk-install
---

# sdk-install

skills/launchdarkly/agent-skills/sdk-install
sdk-install
Installation
$ npx skills add https://github.com/launchdarkly/agent-skills --skill sdk-install
SKILL.md
LaunchDarkly SDK Install (onboarding)

Installs and initializes the right LaunchDarkly SDK for the user’s project by following three nested skills in order. Do not skip ahead to feature flags here—the parent LaunchDarkly onboarding continues with Step 6: First feature flag using Create first feature flag.

Prerequisites
Project context from parent Step 1: Explore the Project (reuse it; only re-run deep detection if something is unclear)
SDK key / client-side ID / mobile key: Needed when you reach Apply code changes (env wiring). Do not ask the user for these during detect or plan solely because you opened this skill—follow parent onboarding: account status is inferred via MCP OAuth (Step 4) or surfaced at D7 in apply; key material is collected at apply (see parent Prerequisites).
Key types (summary)
SDK Type	Variable (logical)	Source in LaunchDarkly
Server-side	LAUNCHDARKLY_SDK_KEY	Environments → SDK key
Client-side	Client-side ID (bundler-prefixed env names)	Environments → Client-side ID
Mobile	LAUNCHDARKLY_MOBILE_KEY	Environments → Mobile key

Never hardcode keys. Full env rules, consent, and bundler tables: Apply code changes Step 2.

Workflow — run these nested skills in order

Execute all three unless the detect decision tree short-circuits (e.g. skip to apply only). Each nested skill may contain decision points — some blocking (marked D<N> -- BLOCKING, where you must call your structured question tool and wait for the user's response before continuing) and some non-blocking (where you present information and continue unless the user objects). Do NOT batch tool calls across blocking boundaries.

Order	Nested skill	Role
1	Detect repository stack	Language, package manager, monorepo target, entrypoint, existing LD usage
2	Generate integration plan	SDK choice, files to change, env plan -- presented to user (non-blocking; see plan SKILL.md D6)
3	Apply code changes	Install package(s), .env / secrets with consent, init code, compile check (both tracks when dual-SDK plan)

Shared references for all steps: SDK recipes, SDK snippets.

After Step 3 completes

Continue with the parent skill:

Step 6: Create first feature flag

Do not add standalone “sample flag” evaluation in this skill unless the user explicitly needs a throwaway check; the parent flow creates the first flag in order.

Guidelines
Match existing codebase conventions for imports, config, and style.
Prefer TypeScript in TypeScript projects.
If the project uses a shared config layer, initialize LaunchDarkly there.
Add .env.example entries when the project uses dotenv.
Dependency scope: Add only LaunchDarkly SDK package(s) from the recipe unless the user explicitly approves upgrading or adding other packages (Apply — Permission before changing other dependencies).
Edge cases
Multiple environments (e.g. Next.js server + client) or user asked for frontend + backend: Use a dual-SDK plan and apply both packages and both inits—never summarize the second SDK as done without lockfile + entrypoint evidence.
Monorepo: Integrate the package the user chose in parent onboarding; stay within that subtree.
SDK already installed and initialized: Parent may skip this handoff—see parent Edge Cases and detect decision tree.
Unsupported or uncommon stack: Use SDK recipes and the full SDK catalog.
References
Detect repository stack
Generate integration plan
Apply code changes
SDK recipes
SDK snippets
LaunchDarkly onboarding (parent)
Weekly Installs
75
Repository
launchdarkly/ag…t-skills
GitHub Stars
7
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass