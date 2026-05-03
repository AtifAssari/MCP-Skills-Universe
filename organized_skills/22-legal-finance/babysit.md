---
rating: ⭐⭐
title: babysit
url: https://skills.sh/a5c-ai/babysitter/babysit
---

# babysit

skills/a5c-ai/babysitter/babysit
babysit
Installation
$ npx skills add https://github.com/a5c-ai/babysitter --skill babysit
SKILL.md
babysit

Orchestrate .a5c/runs/<runId>/ through iterative execution.

Dependencies
Babysitter SDK and CLI

Read the SDK version from versions.json to ensure version compatibility:

SDK_VERSION=$(node -e "try{console.log(JSON.parse(require('fs').readFileSync('${CLAUDE_PLUGIN_ROOT}/versions.json','utf8')).sdkVersion||'latest')}catch{console.log('latest')}")
sudo npm i -g @a5c-ai/babysitter-sdk@$SDK_VERSION
# sudo is depending on the env and system


then use the CLI alias: CLI="babysitter"

Alternatively, use the CLI alias: CLI="npx -y @a5c-ai/babysitter-sdk@$SDK_VERSION"

jq

make sure you have jq installed and available in the path. if not, install it.

Instructions

Run the following command to get full orchestration instructions:

babysitter instructions:babysit-skill --harness claude-code --interactive


For non-interactive mode (running with -p flag or no AskUserQuestion tool):

babysitter instructions:babysit-skill --harness claude-code --no-interactive


Follow the instructions returned by the command above to orchestrate the run.

Weekly Installs
186
Repository
a5c-ai/babysitter
GitHub Stars
696
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykFail