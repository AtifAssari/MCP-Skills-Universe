---
rating: ⭐⭐
title: capacitor-app-upgrades
url: https://skills.sh/cap-go/capgo-skills/capacitor-app-upgrades
---

# capacitor-app-upgrades

skills/cap-go/capgo-skills/capacitor-app-upgrades
capacitor-app-upgrades
Installation
$ npx skills add https://github.com/cap-go/capgo-skills --skill capacitor-app-upgrades
SKILL.md
Contains Shell Commands

This skill contains shell command directives (!`command`) that may execute system commands. Review carefully before installing.

Capacitor App Upgrade

Upgrade a Capacitor app project to a newer major version.

When to Use This Skill
User wants to move a Capacitor app from one major version to another
User is preparing for a multi-version jump
User needs a safe fallback when automated migration does not complete cleanly
Live Project Snapshot

Current Capacitor packages from package.json: !node -e "const fs=require('fs');if(!fs.existsSync('package.json'))process.exit(0);const pkg=JSON.parse(fs.readFileSync('package.json','utf8'));const out=[];for(const section of ['dependencies','devDependencies']){for(const [name,version] of Object.entries(pkg[section]||{})){if(name.startsWith('@capacitor/'))out.push(section+'.'+name+'='+version)}}console.log(out.sort().join('\n'))"

Native and Capacitor config paths: !find . -maxdepth 3 \( -name 'capacitor.config.json' -o -name 'capacitor.config.ts' -o -name 'capacitor.config.js' -o -path './ios' -o -path './android' \)

Procedures
Step 1: Detect the Current Version

Start from the injected snapshot above, then confirm @capacitor/core in package.json if anything looks inconsistent.

If the target version is not specified, ask the user to confirm an explicit major version before proceeding.

Step 2: Upgrade One Major Version at a Time

Do not skip intermediate major versions.

For each version jump:

Update the @capacitor/* package versions in package.json.
Run npm install.
Run the Capacitor migration flow if available for that version.
Sync native projects with npx cap sync.
Verify iOS and Android build cleanly before continuing.

If the automated migration step fails, apply the generated changes manually and continue with the same major version before moving to the next one.

Step 3: Check Native Projects

Review the platform projects for version-specific requirements:

iOS deployment target
Xcode compatibility
Android Gradle Plugin and Java version
Any plugin-specific native changes introduced by the new Capacitor major version
Step 4: Final Verification

Run the project checks that matter for the app:

npm install
npx cap sync
npx cap run ios
npx cap run android


If the app has a custom test or build pipeline, run that as well.

Error Handling
If the automated migration step only partially completes, finish the current major version manually before trying the next one.
If iOS fails, verify the deployment target and Xcode version match the target Capacitor major version.
If Android fails, verify the Gradle and Java requirements for the target version.
If the app uses plugins with their own upgrade constraints, handle those plugins separately after the app version is stable.
Weekly Installs
99
Repository
cap-go/capgo-skills
GitHub Stars
32
First Seen
Mar 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass