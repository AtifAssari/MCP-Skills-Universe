---
rating: ⭐⭐
title: ionic-appflow-migration
url: https://skills.sh/cap-go/capgo-skills/ionic-appflow-migration
---

# ionic-appflow-migration

skills/cap-go/capgo-skills/ionic-appflow-migration
ionic-appflow-migration
Installation
$ npx skills add https://github.com/cap-go/capgo-skills --skill ionic-appflow-migration
SKILL.md
Contains Shell Commands

This skill contains shell command directives (!`command`) that may execute system commands. Review carefully before installing.

Ionic Appflow Migration

Migrate an existing Ionic or Capacitor project away from Ionic Appflow.

When to Use This Skill
User is moving off Ionic Appflow
The project uses Appflow Live Updates, cloud builds, or store deployment
The repository still references ionic appflow, @capacitor/live-updates, or cordova-plugin-ionic
Live Project Snapshot

Detected Appflow-related packages and scripts: !node -e "const fs=require('fs');if(!fs.existsSync('package.json'))process.exit(0);const pkg=JSON.parse(fs.readFileSync('package.json','utf8'));const out=[];for(const section of ['dependencies','devDependencies']){for(const [name,version] of Object.entries(pkg[section]||{})){if(name==='@capacitor/live-updates'||name==='cordova-plugin-ionic'||name.includes('appflow'))out.push(section+'.'+name+'='+version)}}for(const [name,cmd] of Object.entries(pkg.scripts||{})){if(/appflow|ionic cloud|ionic package|live-updates/i.test(cmd))out.push('scripts.'+name+'='+cmd)}console.log(out.join('\n'))"

Possible Appflow config and workflow paths: !find . -maxdepth 4 \( -name '.io-config.json' -o -name 'ionic.config.json' -o -name 'capacitor.config.json' -o -name 'capacitor.config.ts' -o -name 'capacitor.config.js' -o -path './.github/workflows' \)

Migration Strategy

Split the Appflow migration by feature instead of treating it as a single package swap.

Live Updates -> capgo-live-updates
Native cloud builds -> capacitor-ci-cd
Store publishing -> capacitor-app-store

Use this skill to detect what Appflow is doing today, then hand off each feature area to the right skill.

Procedures
Step 1: Detect Appflow Usage

Start from the injected snapshot above, then search more broadly if the migration surface is still unclear.

Search the repository for:

ionic appflow
@capacitor/live-updates
cordova-plugin-ionic
dashboard.ionicframework.com
appflow.ionic.io

Record whether the project currently uses:

live updates
cloud/native builds
app store deployment automation
Step 2: Migrate Live Updates

If Appflow live updates are in use:

Remove @capacitor/live-updates or cordova-plugin-ionic.
Install and configure Capgo using the capgo-live-updates skill.
Map Appflow channels and rollout behavior onto Capgo channels.
Verify that notifyAppReady() or the equivalent Capgo startup flow is wired correctly.

Do not delete Appflow configuration until the Capgo update path is validated.

Step 3: Replace Cloud Build Automation

If Appflow was building the app in the cloud:

Inspect the existing CI/CD workflow for ionic appflow build.
Replace it with repository-owned automation using the capacitor-ci-cd skill.
Preserve signing inputs, environment variables, and platform-specific build arguments.

Treat Appflow build settings as migration input, not as a runtime dependency.

Step 4: Replace Store Publishing

If Appflow handled TestFlight or Google Play publishing:

Inspect the current deployment flow.
Move that workflow to the repository's publishing pipeline using the capacitor-app-store skill.
Keep bundle identifiers, track selection, and credential handling unchanged unless the user wants a new release process.
Step 5: Clean Up

After each migrated feature is verified:

remove Appflow packages and scripts
remove obsolete Appflow configuration
remove stale CI secrets that are no longer needed
Error Handling
For live update migrations, validate rollback behavior before deleting the old Appflow setup.
For build migrations, preserve the existing signing path first and only simplify later.
For publishing migrations, move one destination at a time so App Store and Play failures stay isolated.
Weekly Installs
82
Repository
cap-go/capgo-skills
GitHub Stars
31
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass