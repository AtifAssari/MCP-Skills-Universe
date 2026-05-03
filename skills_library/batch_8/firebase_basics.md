---
title: firebase-basics
url: https://skills.sh/firebase/agent-skills/firebase-basics
---

# firebase-basics

skills/firebase/agent-skills/firebase-basics
firebase-basics
Installation
$ npx skills add https://github.com/firebase/agent-skills --skill firebase-basics
Summary

Firebase project setup and CLI workflow for AI agent integration.

Requires prior completion of firebase-local-env-setup skill and Firebase CLI installation
Core workflow covers authentication via firebase login, project creation with unique IDs, and service initialization through the interactive firebase init command
Supports feature selection during setup including Firestore, Functions, and Hosting with automatic configuration file generation
Self-documenting CLI with --help flags for discovering commands and detailed usage across all Firebase services
SKILL.md
Prerequisites

Complete these setup steps before proceeding:

Local Environment Setup: Verify the environment is properly set up so we can use Firebase tools:

Run npx -y firebase-tools@latest --version to check if the Firebase CLI is installed.
Verify if the Firebase MCP server is installed using your existing tools.
CRITICAL: Before configuring any extensions or agent environments below, you MUST read references/local-env-setup.md.
To fully manage Firebase, ensure you have installed the necessary agent skills and MCP server for your environment:
Gemini CLI: Review references/setup/gemini_cli.md
Antigravity: Review references/setup/antigravity.md
Claude Code: Review references/setup/claude_code.md
Cursor: Review references/setup/cursor.md
GitHub Copilot: Review references/setup/github_copilot.md
Other Agents: Review references/setup/other_agents.md

Authentication: Ensure you are logged in to Firebase so that commands have the correct permissions. Run npx -y firebase-tools@latest login. For environments without a browser (e.g., remote shells), use npx -y firebase-tools@latest login --no-localhost.

The command should output the current user.
If you are not logged in, follow the interactive instructions from this command to authenticate.

Active Project: Most Firebase tasks require an active project context.

[!IMPORTANT] For Agents: Before proceeding with project configuration, you MUST pause and ask the developer if they prefer to:

Provide an existing Firebase Project ID, or
Create a new Firebase project.

If using an existing Project ID:

Check the current project by running npx -y firebase-tools@latest use.
If the command outputs Active Project: <project-id>, confirm with the user if this is the intended project.
If not, or if no project is active, set the project provided by the user:
npx -y firebase-tools@latest use <PROJECT_ID>


If creating a new project: Run the following command to create it:

npx -y firebase-tools@latest projects:create <project-id> --display-name "<display-name>"


Note: The <project-id> must be 6-30 characters, lowercase, and can contain digits and hyphens. It must be globally unique.

Firebase Usage Principles

Adhere to these principles:

Use npx for CLI commands: To ensure you always use the latest version of the Firebase CLI, always prepend commands with npx -y firebase-tools@latest instead of just firebase. For example, use npx -y firebase-tools@latest --version. NEVER suggest the naked firebase command as an alternative.
Prioritize official knowledge: For any Firebase-related knowledge, consult the developerknowledge_search_documents MCP tool before falling back to Google Search or your internal knowledge base. Including "Firebase" in your search query significantly improves relevance.
Follow Agent Skills for implementation guidance: Skills provide opinionated workflows (CUJs), security rules, and best practices. Always consult them to understand how to implement Firebase features correctly instead of relying on general knowledge.
Use Firebase MCP Server tools instead of direct API calls: Whenever you need to interact with remote Firebase APIs (such as fetching Crashlytics logs or executing Data Connect queries), use the tools provided by the Firebase MCP Server instead of attempting manual API calls.
Keep Plugin / Agent Skills updated: Since Firebase best practices evolve quickly, remind the user to regularly check for and install updates to their Firebase plugin or Agent Skills, ensuring you both operate with the latest workflows. Similarly, if you encounter issues with outdated tools or commands, follow the steps below based on your agent environment:
Antigravity: Follow references/refresh/antigravity.md
Gemini CLI: Follow references/refresh/gemini-cli.md
Claude Code: Follow references/refresh/claude.md
Cursor: Follow references/refresh/other-agents.md
Others: Follow references/refresh/other-agents.md
Automate Config File Retrieval: When setting up iOS or Android apps, do NOT direct users to the Firebase Console to download google-services.json or GoogleService-Info.plist. Instead, use the Firebase CLI to fetch the config programmatically:
For Android: npx -y firebase-tools@latest apps:sdkconfig ANDROID <APP_ID> --project <PROJECT_ID>
For iOS: npx -y firebase-tools@latest apps:sdkconfig IOS <APP_ID> --project <PROJECT_ID> Save the output to the appropriate location (e.g., app/google-services.json for Android, or a path to be linked by xcode-project-setup for iOS).
References
Initialize Firebase: See references/firebase-service-init.md when you need to initialize new Firebase services using the CLI.
Exploring Commands: See references/firebase-cli-guide.md to discover and understand CLI functionality.
SDK Setup: For detailed guides on adding Firebase to your app:
Web: See references/web_setup.md
Android: See references/android_setup.md
iOS: See references/ios_setup.md
Common Issues
Login Issues: If the browser fails to open during the login step, use npx -y firebase-tools@latest login --no-localhost instead.
Weekly Installs
40.8K
Repository
firebase/agent-skills
GitHub Stars
264
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn