---
rating: ⭐⭐
title: enonic-sandbox-manager
url: https://skills.sh/webmaxru/enonic-agent-skills/enonic-sandbox-manager
---

# enonic-sandbox-manager

skills/webmaxru/enonic-agent-skills/enonic-sandbox-manager
enonic-sandbox-manager
Installation
$ npx skills add https://github.com/webmaxru/enonic-agent-skills --skill enonic-sandbox-manager
SKILL.md
Enonic CLI & Local Dev Environment Helper
Procedures

Step 1: Detect Workspace Context

Execute node scripts/find-enonic-targets.mjs from the skill root to scan the current workspace for Enonic project markers (.enonic, build.gradle with com.enonic.xp plugin, gradle.properties with xpVersion).
If markers are found, note the project name, linked sandbox, and XP version from the output. Use these values as defaults for subsequent commands.
If no markers are found, treat the request as a greenfield setup and proceed to sandbox creation or project scaffolding as appropriate.

Step 2: Ensure CLI is Available

Verify the Enonic CLI is installed by running enonic --version.
If the command fails, read references/cli-reference.md for installation instructions and guide through the appropriate method for the detected OS:
npm (any OS): npm install -g @enonic/cli
macOS: brew tap enonic/cli && brew install --no-quarantine enonic
Linux: wget -qO- https://repo.enonic.com/public/com/enonic/cli/installer/cli-linux/1.0.0/cli-linux-1.0.0.sh | sh
Windows: scoop bucket add enonic https://github.com/enonic/cli-scoop.git && scoop install enonic
After installation, verify with enonic --version.

Step 3: Sandbox Management

Read references/cli-reference.md for the full sandbox command catalog.
Match the request to the correct operation:
Create: enonic sandbox create <name> [-v <version>] [-t <template>] [--skip-template] [-f]
List: enonic sandbox ls
Start: enonic sandbox start <name> [--detach] [--prod] [--debug]
Stop: enonic sandbox stop
Upgrade: enonic sandbox upgrade <name> -v <version>
Delete: enonic sandbox delete <name> -f
Copy: enonic sandbox copy <source> <target>
When creating a sandbox, prompt for the XP version if not specified. Use -f flag for non-interactive execution when the version and name are known.
If the request mentions templates, list available templates or use -t <template> flag. Use --skip-template to create a bare sandbox with no pre-installed apps.

Step 4: Project Scaffolding

For new project creation, use the simplified command: enonic create <name> [-r <starter>] [-s <sandbox>] [-f]
Common starters include starter-vanilla, starter-headless, and starter-nextjs. Read references/cli-reference.md for the full list of options.
To link an existing project to a different sandbox: enonic project sandbox <name>
Ensure the project folder contains build.gradle and .enonic configuration after creation.

Step 5: Development Workflow

Determine the appropriate development command:
Dev mode (hot-reload): enonic dev — starts the sandbox in detached mode and runs the app with file watching. Execute from the project root.
Build only: enonic project build
Deploy to sandbox: enonic project deploy [sandbox-name] [-c] — use -c for continuous deployment.
Install to running XP: enonic project install
Run tests: enonic project test
Clean build artifacts: enonic project clean
Arbitrary Gradle task: enonic project gradle <tasks>
If the sandbox is not running, start it first: enonic sandbox start <name> -d
To terminate dev mode, use Ctrl-C. The CLI will attempt to stop the detached sandbox automatically.

Step 6: App Management on Running XP

For managing applications on a running XP instance, read references/cli-reference.md for the XP app commands.
Match the operation:
Install from URL: enonic app install --url <jar-url>
Install from file: enonic app install --file <path-to-jar>
Start app: enonic app start <app-key>
Stop app: enonic app stop <app-key>
Authentication is required for XP commands. Use --cred-file <path> (XP 7.15+), --client-key <path> + --client-cert <path> for mTLS (XP 7.15+), or set ENONIC_CLI_REMOTE_USER and ENONIC_CLI_REMOTE_PASS environment variables.

Step 7: CI/CD Pipeline Generation

Read assets/enonic-ci.template.yml for the GitHub Actions workflow template.
Customize the template based on the project:
Set the correct XP version in the sandbox creation step.
Set the app name and Gradle build parameters.
Configure deployment targets (sandbox for staging, cloud for production).
Place the generated workflow file at .github/workflows/enonic-ci.yml in the project repository.

Step 8: Troubleshooting

If a sandbox fails to start or a deployment fails, read references/troubleshooting.md for common issues and resolutions.
Key diagnostic commands:
enonic sandbox ls — check sandbox status and XP version.
enonic system info — check running XP instance details.
Check port 8080 (HTTP) and 5005 (debug) availability.
Read references/compatibility.md for CLI-to-XP version compatibility if version mismatch errors occur.
Error Handling
If scripts/find-enonic-targets.mjs returns no results, proceed with greenfield setup instructions rather than failing.
If enonic --version fails, guide through CLI installation per Step 2 before proceeding.
If sandbox creation fails with a version error, read references/compatibility.md and suggest a compatible XP version.
If port conflicts occur during sandbox start, read references/troubleshooting.md for resolution steps.
If enonic dev fails, verify the project has a Gradle dev task (present in all official starters) and that the linked sandbox exists and is not already running in another terminal.
Weekly Installs
80
Repository
webmaxru/enonic…t-skills
First Seen
Mar 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn