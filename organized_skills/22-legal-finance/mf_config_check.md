---
rating: ⭐⭐
title: mf-config-check
url: https://skills.sh/module-federation/core/mf-config-check
---

# mf-config-check

skills/module-federation/core/mf-config-check
mf-config-check
Installation
$ npx skills add https://github.com/module-federation/core --skill mf-config-check
SKILL.md

Step 1: Call the mf-context Skill (pass $ARGUMENTS) to collect MFContext.

Step 2: Serialize MFContext to JSON and pass it to the check script via the --context argument:

node scripts/config-exposes-check.js --context '<MFContext-JSON>'


Process each item in the output results array:

CONFIG-PLUGIN · warning — incorrect or missing MF plugin

Based on the detected bundler and installed packages, the recommended plugin is:
Webpack only: @module-federation/enhanced or @module-federation/enhanced/webpack
Rspack only: @module-federation/enhanced/rspack (recommended) or @module-federation/rspack
Rsbuild: @module-federation/rsbuild-plugin (recommended), or the Rspack plugin
Modern.js: @module-federation/modern-js-v3 for @modern-js/app-tools ≥ 3.0.0, otherwise @module-federation/modern-js; falls back to Rspack/Webpack plugin based on the underlying bundler
Next.js: @module-federation/nextjs-mf
Show the detected bundler, installed MF-related packages, and the recommended plugin

CONFIG-ASYNC-ENTRY · warning — async entry not configured (maps to RUNTIME-006)

experiments.asyncStartup = true is not set in the bundler config
This setting is required by most bundler setups to avoid runtime initialization errors
Exception: not required when using @module-federation/modern-js-v3 or @module-federation/modern-js
Note: Rspack requires version > 1.7.4 to support this option
Reference: https://module-federation.io/blog/hoisted-runtime.md
To check: read bundler.configFile from MFContext and look for experiments.asyncStartup

CONFIG-EXPOSES-KEY · warning — key does not start with ./

MF spec requires exposes keys to start with ./ (e.g., "./Button" not "Button")
Inform the user of the specific key name and guide them to correct the format

CONFIG-EXPOSES-PATH · warning — path does not exist

The file referenced by the exposes value does not exist in the project. Show the specific key and incorrect path.
The check must match the exact file extension (e.g., .tsx ≠ .ts)
Common causes:
Typo in file path
Wrong file extension
Incorrect relative path base (should be relative to project root)

When results is empty

Inform the user that plugin selection, async entry config, and exposes passed all checks
Weekly Installs
56
Repository
module-federation/core
GitHub Stars
2.5K
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass