---
title: m365-agent-scaffolder
url: https://skills.sh/sebastienlevert/m365-copilot-skills/m365-agent-scaffolder
---

# m365-agent-scaffolder

skills/sebastienlevert/m365-copilot-skills/m365-agent-scaffolder
m365-agent-scaffolder
Installation
$ npx skills add https://github.com/sebastienlevert/m365-copilot-skills --skill m365-agent-scaffolder
SKILL.md
M365 Agent Scaffolder
⛔ STOP - READ THIS FIRST ⛔
THE ONLY VALID COMMAND

Copy this command EXACTLY. Replace <project-name> with the user's project name:

npx -p @microsoft/m365agentstoolkit-cli@latest atk new -n <project-name> -c declarative-agent -with-plugin type-spec -i false

FORBIDDEN COMMANDS - THESE DO NOT EXIST
❌ INVALID COMMAND	WHY IT FAILS
atk init	DOES NOT EXIST - there is no init command
atk init --template	DOES NOT EXIST - there is no init command or --template flag
atk create	DOES NOT EXIST - there is no create command
atk scaffold	DOES NOT EXIST - there is no scaffold command
--template anything	DOES NOT EXIST - there is no --template flag
--template declarative-copilot	DOES NOT EXIST - this is completely made up
--template m365-agent	DOES NOT EXIST - this is completely made up
Any command without npx -p @microsoft/m365agentstoolkit-cli@latest prefix	WILL FAIL - atk might not be installed globally
CORRECT vs WRONG

✅ CORRECT:

npx -p @microsoft/m365agentstoolkit-cli@latest atk new -n my-agent -c declarative-agent -with-plugin type-spec -i false


❌ WRONG (DO NOT USE):

atk init my-agent --template declarative-copilot


❌ WRONG (DO NOT USE):

atk init my-agent --template m365-agent


❌ WRONG (DO NOT USE):

atk create my-agent

Quick Summary

This skill does ONE thing: creates new M365 Copilot agent project structures. It:

Collects minimal required information
Scaffolds the project using ATK CLI
Automatically continues to m365-agent-developer skill for implementation

All architecture, planning, implementation, and deployment is handled by the m365-agent-developer skill.

When to Use This Skill

Use this skill ONLY when:

Creating a brand new empty M365 Copilot agent project from scratch
The user explicitly asks to create a new M365 Copilot project, agent or workspace
Starting a new M365 Copilot agent development initiative that needs initial project structure

Do NOT use this skill when:

Working with existing projects (use m365-agent-developer)
Implementing features or capabilities (use m365-agent-developer)
Deploying or managing agents (use m365-agent-developer)
Troubleshooting issues (use m365-agent-developer)
Designing architecture or planning (use m365-agent-developer)
Instructions

Follow these exact steps when creating a new M365 Copilot agent project:

Step 1: Understand the Request

Action: Verify the user wants to create a NEW M365 Copilot agent project.

Check for:

Keywords: "new project", "create agent", "scaffold", "start from scratch", "M365 Copilot", "M365 agent", "declarative agent"
Confirmation this is NOT an existing project

If existing project: Stop and recommend using m365-agent-developer skill.

Step 2: Verify Empty Directory and Collect Project Name

Action: First, check if the current directory is empty. Then ask for the project name.

Directory Check (CRITICAL):

Use ls -A to check if current directory is empty
Ignore hidden folders (folders starting with .) when evaluating if directory is empty:
Hidden folders like .claude, .copilot, .github are configuration/metadata folders
These folders are used to steer coding agents and should not prevent scaffolding
If ONLY hidden folders exist, treat the directory as empty
If directory is NOT empty (has non-hidden files/folders), ERROR OUT with message:
❌ Error: Current directory is not empty!

This skill requires an empty directory to scaffold a new M365 Copilot agent project.
Please navigate to an empty directory or create a new one first.

Do NOT proceed if directory has non-hidden content

If directory is empty, collect:

Project name (required)
What should the M365 Copilot agent project be named?
Must be valid for directory names (no spaces, special characters)
Example: "customer-support-agent", "sales-assistant"

Example question:

What would you like to name your M365 Copilot agent project?

Step 3: Run ATK CLI Command and Move Files to Current Directory

Action: Execute the scaffolding command, then move files from the ATK-created subfolder to the current directory.

⛔ COMMAND REMINDER - COPY EXACTLY ⛔

Commands to execute sequentially:

Create the project (COPY THIS EXACT COMMAND):
npx -p @microsoft/m365agentstoolkit-cli@latest atk new -n <project-name> -c declarative-agent -with-plugin type-spec -i false


BEFORE YOU RUN ANY COMMAND, VERIFY:

✅ Command starts with npx -p @microsoft/m365agentstoolkit-cli@latest
✅ Command uses atk new (NOT atk init, NOT atk create)
✅ Command has -c declarative-agent (NOT --template)
✅ Command has -with-plugin type-spec
✅ Command has -i false

IF YOUR COMMAND LOOKS LIKE ANY OF THESE, STOP - IT IS WRONG:

❌ atk init ... → WRONG, use atk new
❌ --template ... → WRONG, use -c declarative-agent
❌ Missing npx -p @microsoft/m365agentstoolkit-cli@latest → WRONG

Parameters:

-n <project-name>: The project name provided by the user (ONLY parameter to customize)
-c declarative-agent: Create a declarative agent (REQUIRED - do not change)
-with-plugin type-spec: Include TypeSpec plugin scaffolding (REQUIRED - do not change)
-i false: Non-interactive mode (REQUIRED - do not change)

Note: ATK will create a subfolder named <project-name> with all project files.

Move all files from the subfolder to current directory:
mv <project-name>/* <project-name>/.* . 2>/dev/null || true

Delete the now-empty subfolder:
rmdir <project-name>


Why this is important:

ATK always creates a subfolder, but we want files in the current directory
Moving files ensures the developer's intended directory structure
Deleting the empty subfolder keeps the workspace clean
Step 4: Confirm Creation and Continue to m365-agent-developer Skill

Action: Provide a simple confirmation message and automatically continue to m365-agent-developer skill.

Message template:

✅ Project created in current directory: <absolute-current-directory-path>

Your empty M365 Copilot agent project structure is ready.

🎯 Continuing with the m365-agent-developer skill to help you design and implement your agent...


Then immediately invoke m365-agent-developer skill:

Use the Skill tool to invoke "m365-agent-developer"
Do NOT stop or wait for user confirmation
The flow should be seamless and automatic
Examples

For detailed examples of how to use this skill, see the Examples Reference.

Best Practices

For detailed best practices when scaffolding M365 Copilot agent projects, see the Best Practices Reference.

Weekly Installs
12
Repository
sebastienlevert…t-skills
GitHub Stars
4
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass