---
rating: ⭐⭐
title: vue-creater
url: https://skills.sh/helloggx/skill/vue-creater
---

# vue-creater

skills/helloggx/skill/vue-creater
vue-creater
Installation
$ npx skills add https://github.com/helloggx/skill --skill vue-creater
SKILL.md
Vue Web Artifacts Builder
Data Flow & Context Management (CRITICAL)

You must maintain a Session Context to store file paths. Do not proceed to subsequent steps until you have populated the required variables.

$SKILL_DIR: The absolute path to this skill's directory (where the vue-creater/SKILL.md is located).
$PROJECT_ROOT: The absolute path to the project created in Step 1.
$DSL_PATH: The absolute path to the dsl.json file generated in Step 2 (only for Default template workflow).

IMPORTANT: All script paths mentioned in this document are relative to $SKILL_DIR. When executing scripts, always use the full path: $SKILL_DIR/scripts/script-name.py

Quick Start
Step 0: Select Project Type

FIRST STEP - MANDATORY: You must ask the user to select a project type:

Please select the project type:

    1. **Default** (shadcn + tailwindcss + vite)
    2. **Nuxt Admin Dashboard** (shadcn + tailwindcss + nuxt)
    3. **Electron** (shadcn + tailwindcss + electron + vite)

    Choice [1/2/3]:


STOP and WAIT for user input - do NOT execute menu items automatically - accept number or cmd trigger or fuzzy command match

Action based on user input:

If Choice "1" (Default):

Proceed to Step 1 and follow the default workflow (Steps 1-4).

If Choice "2" (Nuxt Admin Dashboard):

Execute the script: python3 $SKILL_DIR/scripts/setup_nuxt_dashboard.py [project-name]
Condition: If a project name is specified in the context, pass it as an argument. Otherwise, omit it to use the default name.
CAPTURE OUTPUT: Look for the directory path in the script's output (last line before success message).
ASSIGN: Set this path to variable $PROJECT_ROOT.
SKIP ALL REMAINING STEPS - The Nuxt dashboard is fully configured and ready to use.
Inform the user to run: cd $PROJECT_ROOT && bun run dev
END WORKFLOW - Do not proceed to Steps 1-4.

If Choice "3" (Electron):

Execute the script: python3 $SKILL_DIR/scripts/electron_vue_init.py [project-name]
Condition: If a project name is specified in the context, pass it as an argument. Otherwise, omit it to use the default name.
CAPTURE OUTPUT: Look for the directory path in the script's output (last line before success message).
ASSIGN: Set this path to variable $PROJECT_ROOT.
SKIP Step 1 and Step 4 - Project scaffolding is complete.
Proceed to Step 2 to sync design data (DSL).
Default Template Workflow (Choice 1)

To build powerful frontend claude.ai artifacts using the Vue ecosystem, follow these steps:

Initialize the project scaffold using script: $SKILL_DIR/scripts/shadcn_vue_init.py
Retrieve design data using tool: get_dsl
Apply design tokens and styles using tool: get_token
Start development server

Stack:

Core: Vue 3 (Script Setup) + TypeScript + Vite v8.0.0
Styling: Tailwind CSS v4 + shadcn-vue (Radix-vue based)
State & Logic: Pinia (Store) + Vue Router + TanStack Query (vue-query)
Step 1: Initialize Project Scaffolding

Instruction:

Execute the script: python3 $SKILL_DIR/scripts/shadcn_vue_init.py [project-name]
Condition: If a project name is specified in the context, pass it as an argument. Otherwise, omit it to use the default name.
CAPTURE OUTPUT: Look for the directory path in the script's output (last line before success message).
ASSIGN: Set this path to variable $PROJECT_ROOT.
Validation: If $PROJECT_ROOT is empty, stop and ask the user to verify the installation.

What this script does:

✅ Sets up Vue 3 + Vite 8.0.0
✅ Configures Tailwind CSS 4 (CSS-first configuration, no generic config js)
✅ Installs shadcn-vue and configures components.json
✅ Sets up Pinia, Vue Router, and Vue Query plugins
Step 2: Sync Design Data (DSL)

you must ask question: Please select the design source configuration:

1. **Custom Design DSL** (Provide a URL or file path for the design tokens)
2. **Use TOKEN_URL_LIGHT** (Read DSL URL from .env TOKEN_URL_LIGHT variable)
3. **Use Default** (Skip design tokens, use default theme)

Choice [1/2/3]:


STOP and WAIT for user input - do NOT execute menu items automatically - accept number or cmd trigger or fuzzy command match Fetch the design structure and layout data from the source:

Action based on user input:

If Choice "1" (Custom):

Ask for URL (if missing).
Execute get_dsl with the URL.
CAPTURE OUTPUT: Look for the file path of the saved JSON (e.g., .../dsl.json).
ASSIGN: Set this path to variable $DSL_PATH.

If Choice "2" (TOKEN_URL_LIGHT):

Check for .env file existence:
Look for .env file in the current working directory or project root.
If .env file does NOT exist:
STOP and WAIT for user input
Prompt user to create .env file with the following content:
TOKEN_URL_LIGHT=https://your-token-url.com/dsl.json

Explain to user where to place the .env file and the required parameter.
WAIT until user confirms they have created and configured the .env file.
After .env file is confirmed to exist, read the TOKEN_URL_LIGHT variable from .env file.
If TOKEN_URL_LIGHT is not defined in .env:
STOP and WAIT for user input
Prompt user to add TOKEN_URL_LIGHT=https://your-token-url.com/dsl.json to the .env file.
WAIT until user confirms they have added the variable.
If TOKEN_URL_LIGHT is defined: Execute get_dsl with the URL from TOKEN_URL_LIGHT.
CAPTURE OUTPUT: Look for the file path of the saved JSON (e.g., .../dsl.json).
ASSIGN: Set this path to variable $DSL_PATH.

If Choice "3" (Use Default):

Log "Using default theme, skipping DSL fetch."
ASSIGN: Set $DSL_PATH to empty or null to indicate no custom design tokens.
Step 3: Apply Design Tokens

Prerequisites:

Ensure $PROJECT_ROOT is defined (from Step 1).
Ensure $DSL_PATH is defined (from Step 2).

Instruction: You must now call the get_token tool using the exact paths captured previously.

Strict Execution Logic:

IF $DSL_PATH is valid (User chose Custom): Execute: get_token(project_path=$PROJECT_ROOT, dsl_path=$DSL_PATH)

ELSE (User chose Default): Log "Skipping token application for default theme."

Goal: Extract design tokens from the DSL file at $DSL_PATH and inject them into the Tailwind 4 configuration located inside $PROJECT_ROOT.

Step 4: Start Development Server

Instruction:

Execute the command below immediately.
CRITICAL: You MUST use the chained command format (&&) to ensure the directory context is preserved.
cd "$PROJECT_ROOT" && bun run dev


Note: The project uses bun as the package manager for faster dependency installation and development server startup.

Scripts Reference
shadcn_vue_init.py

Location: $SKILL_DIR/scripts/shadcn_vue_init.py

Usage:

python3 $SKILL_DIR/scripts/shadcn_vue_init.py [project-name]


Features:

Creates Vue 3 + Vite 8.0.0 project
Configures Tailwind CSS 4 with CSS-first configuration
Installs and configures shadcn-vue components
Sets up Pinia, Vue Router, and TanStack Query
Installs Zod for schema validation
Installs VueUse for composition utilities
Creates utility files (lib/utils.ts, composables/useApi.ts)
Generates comprehensive README.md
Cleans up unnecessary template files
setup_nuxt_dashboard.py

Location: $SKILL_DIR/scripts/setup_nuxt_dashboard.py

Usage:

python3 $SKILL_DIR/scripts/setup_nuxt_dashboard.py [project-name]


Features:

Extracts a pre-configured Nuxt 3 admin dashboard template from zip file
Includes Shadcn UI components and Tailwind CSS configuration
Installs all necessary dependencies using bun
Provides a ready-to-use admin dashboard structure
Reference
shadcn-vue: https://www.shadcn-vue.com/
Tailwind CSS v4: https://tailwindcss.com/docs/v4-beta (CSS-centric config)
Vite: https://vitejs.dev/
Weekly Installs
46
Repository
helloggx/skill
GitHub Stars
1
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn