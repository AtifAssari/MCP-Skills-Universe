---
rating: ⭐⭐⭐
title: firebase-cli
url: https://skills.sh/supercent-io/skills-template/firebase-cli
---

# firebase-cli

skills/supercent-io/skills-template/firebase-cli
firebase-cli
Installation
$ npx skills add https://github.com/supercent-io/skills-template --skill firebase-cli
SKILL.md
firebase-cli — Firebase Command Line Interface

Keyword: firebase · firebase deploy · firebase init · firebase emulators

The Firebase CLI (firebase-tools) manages your Firebase project from the terminal: deploy, emulate, import/export data, manage users, configure services, and automate CI/CD.

When to use this skill
Deploy Firebase Hosting, Cloud Functions, Firestore rules/indexes, Realtime Database rules, Cloud Storage rules, Remote Config, or Extensions
Set up a new Firebase project with firebase init
Run the Firebase Emulator Suite locally for development and testing
Manage preview/staging channels for Hosting
Import or export Firebase Authentication users in bulk
Distribute app builds to testers via App Distribution
Manage Firebase Extensions (install, configure, update, uninstall)
Deploy Next.js / Angular apps via Firebase App Hosting
Use Firebase CLI in CI/CD pipelines with service account credentials
Instructions
Install the Firebase CLI: npm install -g firebase-tools
Authenticate: firebase login (browser OAuth) or GOOGLE_APPLICATION_CREDENTIALS for CI
Initialize project: firebase init (creates firebase.json and .firebaserc)
Deploy: firebase deploy or firebase deploy --only hosting,functions
Run emulators: firebase emulators:start
For detailed command reference, see references/commands.md
For installation and setup scripts, see scripts/install.sh

CI/CD: Use GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json firebase deploy instead of the deprecated --token / FIREBASE_TOKEN method.

Examples
Deploy everything
firebase deploy

Deploy only Hosting and Functions
firebase deploy --only hosting,functions

Run all emulators with data persistence
firebase emulators:start --import ./emulator-data --export-on-exit

Create a preview channel and deploy
firebase hosting:channel:create staging --expires 7d
firebase hosting:channel:deploy staging

Import users from JSON
firebase auth:import users.json --hash-algo=BCRYPT

Distribute Android build to testers
firebase appdistribution:distribute app-release.apk \
  --app "1:1234567890:android:abcd1234" \
  --release-notes "Sprint 42 build" \
  --groups "qa-team"

Quick Start
# Install
npm install -g firebase-tools

# Authenticate
firebase login

# Initialize project (interactive)
firebase init

# Deploy
firebase deploy

# Run emulators
firebase emulators:start

Installation
npm (recommended — all platforms)
npm install -g firebase-tools
firebase --version

Standalone binary (macOS/Linux — no Node.js required)
curl -sL firebase.tools | bash

CI/CD — service account authentication (recommended)
# Set environment variable pointing to service account JSON key
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-key.json"
firebase deploy --non-interactive

Via skill script
bash scripts/install.sh

Core Usage
Authentication
firebase login                          # OAuth browser login
firebase login --no-localhost           # Copy-paste code flow
firebase login:ci                       # Generate CI token (deprecated — use service account)
firebase login:list                     # List all authorized accounts
firebase login:use user@example.com     # Set default account
firebase logout                         # Sign out

Project Management
firebase init                    # Set up Firebase features in current directory
firebase use <project_id>        # Set active project
firebase use --add               # Add a project alias
firebase projects:list           # List all Firebase projects
firebase open hosting:site       # Open Firebase console in browser

Deployment
# Deploy everything
firebase deploy

# Deploy specific targets
firebase deploy --only hosting
firebase deploy --only functions
firebase deploy --only firestore
firebase deploy --only hosting,functions

# Deploy sub-targets
firebase deploy --only functions:myFunction
firebase deploy --only hosting:my-site
firebase deploy --only firestore:rules
firebase deploy --only firestore:indexes

# Exclude targets
firebase deploy --except functions

# With message
firebase deploy --message "v2.3.1 release"

Firebase Emulator Suite
# Start all configured emulators
firebase emulators:start

# Start specific emulators
firebase emulators:start --only auth,firestore,functions

# With data import/export
firebase emulators:start --import ./emulator-data --export-on-exit

# Run tests against emulators then shut down
firebase emulators:exec "npm test" --only firestore,auth

# Enable Functions debugger (Node.js inspector on port 9229)
firebase emulators:start --inspect-functions

Local Development Server
firebase serve                        # Hosting + HTTPS Functions
firebase serve --only hosting
firebase serve --port 5000

Hosting Commands
# Preview channels
firebase hosting:channel:create staging --expires 7d
firebase hosting:channel:deploy staging
firebase hosting:channel:list
firebase hosting:channel:open staging
firebase hosting:channel:delete staging --force
firebase hosting:clone my-app:live my-app-staging:staging

# Multi-site management
firebase hosting:sites:list
firebase hosting:sites:create new-site-id
firebase hosting:disable --site my-old-site

Cloud Functions Commands
firebase functions:list                           # List deployed functions
firebase functions:log                            # View logs
firebase functions:log --only myFunction          # Filter by function name
firebase functions:delete myFunction              # Delete a function
firebase functions:shell                          # Local interactive shell

# Secrets (2nd gen — replaces functions:config)
firebase functions:secrets:set MY_SECRET
firebase functions:secrets:get MY_SECRET
firebase functions:secrets:prune

# Config (1st gen only)
firebase functions:config:set api.key="VALUE"
firebase functions:config:get

Firestore Commands
firebase firestore:delete /collection/doc --recursive
firebase firestore:indexes
firebase firestore:rules:get

Realtime Database Commands
firebase database:get /path --pretty
firebase database:set /path data.json
firebase database:push /messages --data '{"text":"Hello"}'
firebase database:update /users/uid --data '{"name":"New Name"}'
firebase database:remove /path --confirm
firebase database:profile --duration 30

Auth Import / Export
# Export all users
firebase auth:export users.json

# Import users (BCRYPT hashes)
firebase auth:import users.json --hash-algo=BCRYPT

# Import users (SCRYPT hashes — Firebase default)
firebase auth:import users.json \
  --hash-algo=SCRYPT \
  --hash-key=<base64-key> \
  --salt-separator=<base64-separator> \
  --rounds=8 \
  --mem-cost=8

Remote Config
firebase remoteconfig:get
firebase remoteconfig:get --output config.json
firebase remoteconfig:versions:list --limit 20
firebase remoteconfig:rollback --version-number 5

App Distribution
# Distribute Android APK
firebase appdistribution:distribute app.apk \
  --app APP_ID \
  --release-notes "Bug fixes and improvements" \
  --testers "qa@example.com" \
  --groups "qa-team,beta-users"

# Manage testers
firebase appdistribution:testers:add alice@example.com --group-alias qa-team
firebase appdistribution:testers:remove alice@example.com
firebase appdistribution:groups:list

Extensions
firebase ext:list
firebase ext:info firebase/delete-user-data
firebase ext:install firebase/delete-user-data
firebase ext:configure delete-user-data
firebase ext:update delete-user-data
firebase ext:uninstall delete-user-data
firebase ext:export

App Hosting (Next.js / Angular)
firebase init apphosting
firebase apphosting:backends:create --location us-central1
firebase apphosting:backends:list
firebase deploy --only apphosting
firebase apphosting:rollouts:create BACKEND_ID --git-branch main

Deploy Targets (multi-site / multi-instance)
# Apply target name to a resource
firebase target:apply hosting prod-site my-app-prod
firebase target:apply storage prod-bucket my-app-bucket
firebase target:apply database default my-app-db

# Use target in deploy
firebase deploy --only hosting:prod-site

# Clear targets
firebase target:clear hosting prod-site

Best practices
Use service accounts for CI/CD: Set GOOGLE_APPLICATION_CREDENTIALS instead of --token (deprecated).
Use --only in deploy: Never deploy everything blindly in production — always scope with --only.
Emulators for development: Always run emulators:start locally before deploying; use --import/--export-on-exit for persistence.
Preview channels before production: Use hosting:channel:deploy for staging reviews before firebase deploy --only hosting.
Secrets over functions:config: For Cloud Functions 2nd gen, use functions:secrets:set (Secret Manager) instead of deprecated functions:config:set.
--non-interactive in scripts: Always add --non-interactive in automated scripts to avoid hanging on prompts.
.firebaserc in VCS: Commit .firebaserc (project aliases) but add secrets and service account keys to .gitignore.
--debug for troubleshooting: Run any failing command with --debug for verbose output.
Troubleshooting
Issue	Solution
command not found: firebase	Run npm install -g firebase-tools; check npm bin -g is in PATH
Authentication error in CI	Set GOOGLE_APPLICATION_CREDENTIALS to service account JSON path
FIREBASE_TOKEN warning	Migrate from token-based auth to service accounts
Deploy fails with permission error	Verify service account has required IAM roles (Firebase Admin, Cloud Functions Admin, etc.)
Emulators not starting	Check ports 4000/5000/5001/8080/9000/9099/9199 are available; run lsof -i :<port>
Functions deploy timeout	Use --only functions:specificFunction to deploy one at a time
Hosting deploy not reflecting changes	Check firebase.json public directory and ignore patterns
ext:install fails	Check extension ID format: publisher/extension-id; try --debug
Database permission denied	Verify database rules and that CLI auth account has access
References
Firebase CLI Reference — official full command reference
Full Command Reference — complete options and flags for all commands
Install Scripts — install.sh (setup) · deploy.sh (deployment helper) · emulators.sh (emulator management)
firebase-tools GitHub — source code and changelog
Firebase CLI Release Notes — version history
Auth Import/Export Reference — hash algorithm details
Hosting Preview Channels — staging workflow
Emulator Suite Configuration — emulator setup
Weekly Installs
326
Repository
supercent-io/sk…template
GitHub Stars
88
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn