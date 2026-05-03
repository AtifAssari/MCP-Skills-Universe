---
rating: ⭐⭐
title: capacitor-plugin-upgrade-v4-to-v5
url: https://skills.sh/cap-go/capgo-skills/capacitor-plugin-upgrade-v4-to-v5
---

# capacitor-plugin-upgrade-v4-to-v5

skills/cap-go/capgo-skills/capacitor-plugin-upgrade-v4-to-v5
capacitor-plugin-upgrade-v4-to-v5
Installation
$ npx skills add https://github.com/cap-go/capgo-skills --skill capacitor-plugin-upgrade-v4-to-v5
SKILL.md
Contains Shell Commands

This skill contains shell command directives (!`command`) that may execute system commands. Review carefully before installing.

Capacitor Plugin Upgrade v4 to v5

Upgrade a Capacitor plugin from version 4 to version 5.

When to Use This Skill
User says the plugin targets Capacitor 4 and must move to v5
User wants the exact v4 to v5 migration path
User needs v5-specific native and package updates
Live Project Snapshot

Plugin and Capacitor package snapshot: !node -e "const fs=require('fs');if(!fs.existsSync('package.json'))process.exit(0);const pkg=JSON.parse(fs.readFileSync('package.json','utf8'));const out=['package.name='+(pkg.name||''),'package.version='+(pkg.version||'')];for(const section of ['peerDependencies','dependencies','devDependencies']){for(const [name,version] of Object.entries(pkg[section]||{})){if(name.startsWith('@capacitor/'))out.push(section+'.'+name+'='+version)}}console.log(out.join('\n'))"

Example and native project paths: !find . -maxdepth 3 \( -path './example-app' -o -path './ios' -o -path './android' \)

Procedure
Start from the injected snapshot and confirm the current Capacitor peer dependency range in package.json.
Update the peer dependency range to Capacitor 5.
Review the v4 to v5 migration notes before editing native files.
Update the example app if it exists.
Run npm install.
Sync and verify the example or test app.
Error Handling
If the example app breaks, fix the plugin API or native bridge before moving on.
If iOS fails, verify the deployment target for Capacitor 5.
If Android fails, verify the Gradle and Java requirements for Capacitor 5.
Weekly Installs
78
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