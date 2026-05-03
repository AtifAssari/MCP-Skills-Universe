---
title: capacitor-app-upgrade-v5-to-v6
url: https://skills.sh/cap-go/capgo-skills/capacitor-app-upgrade-v5-to-v6
---

# capacitor-app-upgrade-v5-to-v6

skills/cap-go/capgo-skills/capacitor-app-upgrade-v5-to-v6
capacitor-app-upgrade-v5-to-v6
Installation
$ npx skills add https://github.com/cap-go/capgo-skills --skill capacitor-app-upgrade-v5-to-v6
SKILL.md
Contains Shell Commands

This skill contains shell command directives (!`command`) that may execute system commands. Review carefully before installing.

Capacitor App Upgrade v5 to v6

Upgrade a Capacitor app from version 5 to version 6.

When to Use This Skill
User says the app is on Capacitor 5 and must move to v6
User wants the exact v5 to v6 migration path
User needs v6-specific native and package updates
Live Project Snapshot

Current Capacitor packages from package.json: !node -e "const fs=require('fs');if(!fs.existsSync('package.json'))process.exit(0);const pkg=JSON.parse(fs.readFileSync('package.json','utf8'));const out=[];for(const section of ['dependencies','devDependencies']){for(const [name,version] of Object.entries(pkg[section]||{})){if(name.startsWith('@capacitor/'))out.push(section+'.'+name+'='+version)}}console.log(out.sort().join('\n'))"

Procedure
Start from the injected package snapshot and confirm the current @capacitor/core version.
Update all @capacitor/* packages to the v6-compatible range.
Review the v5 to v6 migration notes before editing native files.
Run npm install.
Sync with npx cap sync.
Verify the iOS and Android builds.
Error Handling
If the automated migration misses a package, update it manually before syncing again.
If iOS fails, check the deployment target and Xcode compatibility for Capacitor 6.
If Android fails, check the Gradle and Java requirements for Capacitor 6.
Weekly Installs
79
Repository
cap-go/capgo-skills
GitHub Stars
32
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass