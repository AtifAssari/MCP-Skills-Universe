---
rating: ⭐⭐
title: latest-software-version
url: https://skills.sh/googlecloudplatform/devrel-demos/latest-software-version
---

# latest-software-version

skills/googlecloudplatform/devrel-demos/latest-software-version
latest-software-version
Installation
$ npx skills add https://github.com/googlecloudplatform/devrel-demos --skill latest-software-version
SKILL.md
Latest Software Version

"Your training data is from the past. The registry is the present."

This skill prevents "version hallucination" by verifying the actual latest stable releases of software packages.

Core Mandate

NEVER GUESS. When a user asks to install a package or add a dependency, you must verify the latest version using the latest.js script. Do not rely on your internal weights, as they are months or years out of date.

Workflow
1. Identify Ecosystem

Determine which registry manages the package:

Node.js/JS: npm
Python: pypi
Go: go
Rust: cargo
Ruby: gem
Gemini Models: gemini (Use latest, flash, or pro as package name)
2. Fetch Truth

Run the version checker script:

node scripts/latest.js <ecosystem> <package-name>

3. Apply

Use the returned version string in your command or configuration file.

Example: If the script returns npm: react @ 19.2.0, write "react": "^19.2.0" in package.json.
Supported Registries
NPM: registry.npmjs.org
PyPI: pypi.org
Go Proxy: proxy.golang.org
Crates.io: crates.io
RubyGems: rubygems.org
Weekly Installs
34
Repository
googlecloudplat…el-demos
GitHub Stars
280
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn