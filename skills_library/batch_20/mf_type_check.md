---
title: mf-type-check
url: https://skills.sh/module-federation/core/mf-type-check
---

# mf-type-check

skills/module-federation/core/mf-type-check
mf-type-check
Installation
$ npx skills add https://github.com/module-federation/core --skill mf-type-check
SKILL.md

Step 1: Call the mf-context Skill (pass $ARGUMENTS) to collect MFContext.

Step 2: Serialize MFContext to JSON and pass it to the check script via the --context argument:

node scripts/type-check.js --context '<MFContext-JSON>'


Process each item in the output results array and follow the action plan based on the scenario field:

Scenario: TYPE_GENERATION_FAILED (Problem 1 — Producer type files not generated)

The producer failed to generate type files (TYPE-001 error).

If enhancedVersion > 2.0.1 (result field canReadDiagnostics: true):

Read .mf/diagnostics/latest.json to get full error info and the temporary TS config path
Use the temp TS config path with npx tsc --project <tmp-tsconfig> to reproduce errors
Fix the TS errors revealed. Refer to FAQ: https://module-federation.io/guide/troubleshooting/type.md
Offer "skipLibCheck": true as a temporary workaround if errors are complex

If enhancedVersion <= 2.0.1 (result field canReadDiagnostics: false):

Ask the user to run npx mf dts and paste the terminal output (which includes the temp TS config path)
Or ask them to copy the error message that contains the temp TS config path
Once the temp TS config path is known, run npx tsc --project <tmp-tsconfig> to reproduce and fix errors
Offer "skipLibCheck": true as a temporary workaround
Scenario: TYPES_NOT_PULLED (Problem 2 — Consumer not pulling remote types)

The @mf-types folder is missing. Remote types have not been downloaded.

Call mf-module-info skill with the remote module name to retrieve the type file URL (@mf-types.zip)
If no URL returned: the producer has not configured the type file URL or has not generated types. Guide them to enable dts in the @module-federation/enhanced plugin config, then revisit Problem 1
If URL found: attempt to fetch it (or ask the user to verify in browser)
URL inaccessible: try fetching the remoteEntry URL
remoteEntry unreachable: producer deployment is broken or URL is misconfigured; ask user to verify deployment
remoteEntry reachable: type file generation failed or wasn't deployed; ask user to provide local producer path and proceed to Problem 1
URL accessible: types were generated and deployed; the issue is in tsconfig — proceed to Problem 3
Scenario: TSCONFIG_PATHS_MISSING (Problem 3 — tsconfig not configured for remote types)

The @mf-types folder exists but TypeScript cannot find the types because tsconfig.json is missing the paths mapping.

Open tsconfig.json and add the following to compilerOptions.paths:
{
  "compilerOptions": {
    "paths": {
      "*": ["./@mf-types/*"]
    }
  }
}

If paths already exists, merge the new entry without overwriting existing mappings
After updating, run npx tsc --noEmit to verify the type errors are resolved
Scenario: ENV_INCOMPLETE (Missing tsconfig or TypeScript)

TYPE-001 · warning — tsconfig.json missing

tsconfig.json not found in the project root
Advise the user to create tsconfig.json and configure producer type paths in paths

TYPE-001 · warning — typescript dependency missing

typescript not installed in dependencies / devDependencies
Prompt the user to install: pnpm add -D typescript

This Skill performs configuration and dependency-level checks. It runs npx tsc only when guided by a valid temp TS config path. It never runs tsc blindly against the entire project.

Weekly Installs
56
Repository
module-federation/core
GitHub Stars
2.5K
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn