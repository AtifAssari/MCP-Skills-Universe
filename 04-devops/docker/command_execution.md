---
rating: ⭐⭐⭐
title: command-execution
url: https://skills.sh/loxosceles/ai-dev/command-execution
---

# command-execution

skills/loxosceles/ai-dev/command-execution
command-execution
Installation
$ npx skills add https://github.com/loxosceles/ai-dev --skill command-execution
SKILL.md
Command Execution Guidelines

This is a strict guideline. Follow these rules exactly.

Guidelines for AI agents when executing commands and running scripts.

Core Rules
1. Never Run Project Tools on the Host Machine

The host machine stays pristine. All project tools (pnpm, npm, python, pip, pytest, cargo, etc.) live inside devcontainers. Never install packages, run builds, or execute project commands directly on the host.

If you need to run something in a project, use the devcontainer:

# ✅ Correct: execute inside the container
docker exec -it <container_name> pnpm install
docker exec -it <container_name> pnpm build
docker exec -it <container_name> pytest

# ❌ NEVER: run project tools on the host
pnpm install          # installs to host, pollutes system
pip install requests  # modifies host Python
npm run build         # uses host Node version, may differ from container


Exceptions (tools that are OK on the host):

git — version control is host-level
docker / docker compose — managing containers
gh — GitHub CLI for repo operations
npx skills — skill installation (doesn't modify project deps)
File operations (cat, ls, grep, find, etc.)

When working across multiple projects from outside containers, limit yourself to reading files, git operations, and docker commands. If you need to build/test/install, exec into the container.

2. Use Project's Developer API

Always use root package.json scripts:

# ✅ Correct
pnpm lint
pnpm provision:dev
pnpm build:frontend

# ❌ Wrong
cd infrastructure && npx cdk deploy
cd frontend && npm run build


Why: Root scripts are the developer API. Bypassing them means the API can break without anyone noticing.

2. Never Use cd
# ❌ Wrong
cd infrastructure && pnpm synth

# ✅ Correct
pnpm synth:dev

# ✅ Or use working_dir parameter
execute_bash(command="pnpm synth", working_dir="infrastructure")


Why: cd doesn't persist. Use root scripts or working_dir parameter.

3. Discover Scripts First
# Check available scripts
cat package.json | grep -A 50 '"scripts"'


Look for: lint, test, build, provision:*, deploy:*

Installation
# ✅ Workspace root (shared)
pnpm add -D -w eslint

# ✅ Specific workspace
pnpm add -D eslint --filter frontend

# ❌ Wrong
cd frontend && pnpm add eslint

When Direct Execution is Necessary
Check if root script exists first
Use working_dir parameter if available
Document why you're not using root scripts
Summary

Golden Rules:

✅ Use root package.json scripts (the developer API)
✅ Never use cd in commands
✅ Check available scripts first
✅ Use working_dir parameter for direct execution

Remember: Root scripts are the project's public API. Bypassing them breaks the contract.

Progressive Improvement

If the developer corrects a behavior that this skill should have prevented, suggest a specific amendment to this skill to prevent the same correction in the future.

Weekly Installs
40
Repository
loxosceles/ai-dev
First Seen
Mar 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass