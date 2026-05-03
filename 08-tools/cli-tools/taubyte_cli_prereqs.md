---
title: taubyte-cli-prereqs
url: https://skills.sh/taubyte/skills/taubyte-cli-prereqs
---

# taubyte-cli-prereqs

skills/taubyte/skills/taubyte-cli-prereqs
taubyte-cli-prereqs
Installation
$ npx skills add https://github.com/taubyte/skills --skill taubyte-cli-prereqs
SKILL.md
Taubyte CLI prerequisites (hard gate)
Purpose

Run this skill before any other Taubyte skill. It ensures Node.js, Docker (engine running — needed for Dream, inject, and local container workflows), tau / dream, and (when GitHub work is in scope) authenticated tau profile are in place.

Stop conditions (read first)
Situation	Action
Node missing and cannot be installed from this environment	Stop; give OS-specific install instructions; do not run npm i -g without node.
Docker missing, daemon not running, and cannot be fixed from this environment	Stop; give install/start instructions (see Docker section).
GitHub-backed work needed but no tau profile / login incomplete	Stop; follow taubyte-auth-and-profile (browser login hard stop applies there).
tau or dream still broken after install attempts	Stop; log attempts in .taubyte_ai/logs.txt (or project context log per taubyte-context-log).
Workflow order
Node.js — detect; install automatically when possible (see §1).
Docker — detect CLI + daemon; install or start when possible (see §2).
tau / dream — detect; install from @taubyte npm packages when missing (see §3).
tau login / profile — taubyte-auth-and-profile for all login policy; quick tau --json current gate here (see §4).
Verify after any install (see §5).
1. Node.js
Detect
command -v node >/dev/null 2>&1 && node --version
command -v npm >/dev/null 2>&1 && npm --version

If node is missing or node --version fails

Prefer installing Node for the user when the environment supports it (network, permissions, non-interactive package managers):

Windows (e.g. winget available):

winget install -e --id OpenJS.NodeJS.LTS --accept-package-agreements --accept-source-agreements


macOS (brew on PATH):

brew install node


Linux (Debian/Ubuntu family, when apt-get is usable):

sudo apt-get update && sudo apt-get install -y nodejs npm


If automated install fails, is blocked (no sudo, no winget/brew, CI sandbox), or the OS is unclear, stop and ask the user to install Node.js LTS from https://nodejs.org/ (or their distro’s Node LTS packages), then open a new terminal and rerun this skill.

Do not run npm i -g @taubyte/cli or npm i -g @taubyte/dream until node and npm work.

2. Docker

Docker is required for Dream, dream inject, and other local container-backed Taubyte flows (see taubyte-dream-local-operations, taubyte-cloud-selection). You need both the docker CLI and a running daemon (docker info succeeds).

Detect
command -v docker >/dev/null 2>&1 && docker version
docker info

If docker is not in PATH → treat as not installed; try install workflow below.
If docker info fails with connection / daemon errors but docker version shows a client → the engine is stopped or the user lacks permission. Prefer starting Docker Desktop (Windows/macOS) or sudo systemctl start docker (Linux), or sudo usermod -aG docker $USER + re-login when the error is permission-related. Do not assume a fresh install fixes a stopped daemon.
Install when the CLI is missing (automate when possible)

Windows (winget):

winget install -e --id Docker.DockerDesktop --accept-package-agreements --accept-source-agreements


After install, the user may need to start Docker Desktop once (or reboot). Re-run docker info after they confirm it is running.

macOS (brew):

brew install --cask docker


Then start Docker Desktop from Applications and re-check docker info.

Linux (Debian/Ubuntu, when apt-get + sudo work):

sudo apt-get update && sudo apt-get install -y docker.io
sudo systemctl enable --now docker


If builds still fail with permission errors, document sudo usermod -aG docker <user> and logging out/in, or use sudo docker info only to confirm the daemon — long-term, the user should be in the docker group.

If install is not possible (no admin, winget/brew/apt unavailable, headless policy), stop and point the user to https://docs.docker.com/get-docker/ for Docker Engine or Docker Desktop, then rerun this skill once docker info works.

3. Taubyte CLIs on npm (@taubyte scope)

Official tau and Dream packages are published on npm under the @taubyte organization, for example:

@taubyte/cli — provides the tau command (wrapper downloads the platform tau binary as needed).
@taubyte/dream — local cloud / Dream CLI.

Browse or confirm versions: https://www.npmjs.com/search?q=scope%3A%40taubyte.

Detect
command -v tau >/dev/null 2>&1 && tau version
command -v dream >/dev/null 2>&1 && (dream --version || dream --help) || true


If dream fails but Node works, a broken shell alias may point to a missing binary. Try:

node "$(npm root -g)/@taubyte/dream/index.js" --help

Install when missing (Node + npm must work)

Default: global npm:

npm i -g @taubyte/cli
npm i -g @taubyte/dream


Alternative (e.g. npm global path blocked):

curl https://get.tau.link/cli | sh
curl https://get.tau.link/dream | sh


If install fails, stop immediately (see stop conditions).

4. Auth and tau login (defer to taubyte-auth-and-profile)

Any flow that touches GitHub (clone, tau new project, tau push, generated repos) needs a valid Taubyte profile and GitHub auth.

Do not improvise login policy here. Load and follow taubyte-auth-and-profile for:

tau login, tau login --new, --name, --token, --provider github
Browser-based login (tell user, stop until done — see that skill)
Non-interactive patterns with taubyte-execution-modes

Minimal gate check in this skill only:

tau --json current


Inspect Profile (and cloud if needed). If there is no profile and the upcoming work requires GitHub, apply taubyte-auth-and-profile and do not continue to project create, push, import, or website repo operations until auth is resolved.

If the user refuses or cannot complete required login, stop the Taubyte workflow.

5. Verify after installs
node --version
npm --version
docker version
docker info
tau version
dream --version || dream --help || node "$(npm root -g)/@taubyte/dream/index.js" --help

Hard stops (summary)
No Node (and install not possible or failed): stop; no global @taubyte npm installs.
No working Docker (CLI missing and install failed, or daemon not running / no permission after user guidance): stop before Dream / inject / local container work.
GitHub work without completed auth per taubyte-auth-and-profile: stop.
tau / dream still failing after install: stop; log diagnostics to .taubyte_ai/logs.txt.
Do not proceed to cloud / project / resource operations until this gate passes.
Weekly Installs
9
Repository
taubyte/skills
First Seen
10 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn