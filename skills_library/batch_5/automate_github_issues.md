---
title: automate-github-issues
url: https://skills.sh/google-labs-code/jules-skills/automate-github-issues
---

# automate-github-issues

skills/google-labs-code/jules-skills/automate-github-issues
automate-github-issues
Installation
$ npx skills add https://github.com/google-labs-code/jules-skills --skill automate-github-issues
SKILL.md
Automate GitHub Issues with Jules

You are setting up a repository to automatically analyze open GitHub issues, plan implementation tasks, and dispatch parallel Jules coding agents to fix them.

What You're Setting Up

A 5-phase automated pipeline that runs via GitHub Actions (or locally):

Analyze — Fetch open issues and format as structured markdown
Plan — A Jules session performs deep code-level triage and produces self-contained task prompts
Validate — Verify no two tasks modify the same file (prevents merge conflicts)
Dispatch — Spawn parallel Jules sessions, one per task
Merge — Sequential PR merge with CI validation
Setup Steps
Step 1: Copy fleet scripts to the repository

Copy the entire scripts/ directory from this skill into the target repository at scripts/fleet/:

Target structure:
scripts/fleet/
├── fleet-analyze.ts
├── fleet-plan.ts
├── fleet-dispatch.ts
├── fleet-merge.ts
├── types.ts
├── prompts/
│   ├── analyze-issues.ts
│   └── bootstrap.ts
└── github/
    ├── git.ts
    ├── issues.ts
    ├── markdown.ts
    └── cache-plugin.ts


Important: Preserve the directory structure exactly. The scripts use relative imports between files.

Step 2: Copy workflow templates

Copy the workflow files from assets/ to the repository's .github/workflows/ directory:

assets/fleet-dispatch.yml → .github/workflows/fleet-dispatch.yml
assets/fleet-merge.yml → .github/workflows/fleet-merge.yml
Step 3: Create a package.json for the fleet scripts

Create scripts/fleet/package.json with the required dependencies:

{
  "name": "fleet-scripts",
  "private": true,
  "type": "module",
  "dependencies": {
    "@google/jules-sdk": "^0.1.0",
    "octokit": "^4.1.0",
    "find-up": "^7.0.0"
  },
  "devDependencies": {
    "@types/bun": "^1.2.0"
  }
}

Step 4: Create environment template

Copy assets/.env.example to the repository root.

Step 5: Install dependencies
cd scripts/fleet && bun install

Step 6: Print next steps for the user

Tell the user they need to:

Add JULES_API_KEY as a GitHub repository secret (Settings → Secrets → Actions)
GITHUB_TOKEN is provided automatically by GitHub Actions
Customize the cron schedule in .github/workflows/fleet-dispatch.yml (default: daily 6am UTC)
Commit all generated files
Manual Usage

After setup, the user can run the pipeline locally:

cd scripts/fleet

# Fetch open issues
bun fleet-analyze.ts

# Plan tasks (creates a Jules planning session)
JULES_API_KEY=<key> bun fleet-plan.ts

# Dispatch parallel agents
JULES_API_KEY=<key> bun fleet-dispatch.ts

# Merge PRs sequentially
GITHUB_TOKEN=<token> bun fleet-merge.ts

Customization
Prompt Tuning

The analysis prompt in scripts/fleet/prompts/analyze-issues.ts controls how deeply issues are investigated. Users can adjust:

Root cause analysis depth
Solution implementation detail level
Merge conflict avoidance rules
File ownership constraints
Issue Filtering

Edit scripts/fleet/github/issues.ts to filter issues by label, milestone, or state.

Resource References
Architecture Overview — Detailed explanation of the 5-phase pipeline
Troubleshooting
"Unable to parse git remote URL": Ensure the repo has a valid GitHub remote (git remote get-url origin)
Ownership conflict errors: Two tasks claim the same file. Adjust the task JSON or merge them manually.
CI timeout during merge: Increase maxWaitMs in fleet-merge.ts (default: 10 minutes)
Bun not found: Install Bun: curl -fsSL https://bun.sh/install | bash
Weekly Installs
320
Repository
google-labs-cod…s-skills
GitHub Stars
50
First Seen
1 day ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail