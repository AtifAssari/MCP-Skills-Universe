---
title: setup-mac-dev
url: https://skills.sh/fwfutures/vibe-a-thon/setup-mac-dev
---

# setup-mac-dev

skills/fwfutures/vibe-a-thon/setup-mac-dev
setup-mac-dev
Installation
$ npx skills add https://github.com/fwfutures/vibe-a-thon --skill setup-mac-dev
SKILL.md
macOS Development Setup

Perform setup directly with tools. Do not offload commands to the user unless a GUI prompt or privileged approval is required.

Use non-interactive flags wherever supported (-y, --yes, NONINTERACTIVE=1).

Before starting, tell the user:

"Setting up this Mac for development now. This may require command-line tools installation and admin approval prompts."

Then execute each step and report concise progress updates.

Step 1: Preflight checks

Run checks first and record results.

uname -sm
which brew || true
which node || true
which npm || true
which npx || true
which uv || true
xcode-select -p || true


Interpretation:

If required tools already exist, skip reinstallation and keep going.
If xcode-select -p fails, treat missing Command Line Tools (CLT) as a likely blocker for git and Homebrew.
Step 2: Ensure Xcode Command Line Tools (mandatory)

If CLT is missing:

xcode-select --install


Immediately trigger the installer when missing. Do not defer this step.

If the goal is to avoid GUI approval prompts and sudo access is available, prefer a non-GUI install path:

CLT_LABEL="$(softwareupdate -l | awk -F'* ' '/Command Line Tools/ {print $2}' | sed 's/^ *//' | tail -n 1)"
if [ -n "$CLT_LABEL" ]; then
  sudo softwareupdate -i "$CLT_LABEL" --verbose
fi


Notes:

This may open a system dialog and require user acceptance.
xcode-select --install does not support a --yes auto-approve flag.
Re-check with xcode-select -p after the install prompt is accepted.
Continue with user-local installs when CLT remains unavailable.
Step 3: Install Homebrew when possible

Check whether Homebrew already exists:

which brew


If missing, attempt install:

NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"


If Homebrew install fails due missing admin privileges or CLT, continue with no-admin fallback in Step 4.

Step 4: Install Node.js (preferred: Homebrew, fallback: user-local)

Preferred path when Homebrew is available:

brew install node


Fallback path without Homebrew:

mkdir -p "$HOME/.local" "$HOME/.local/bin"
curl -fsSL "https://nodejs.org/dist/v22.22.0/node-v22.22.0-darwin-arm64.tar.gz" -o "$HOME/.local/node-v22.22.0-darwin-arm64.tar.gz"
tar -xzf "$HOME/.local/node-v22.22.0-darwin-arm64.tar.gz" -C "$HOME/.local"
ln -sfn "$HOME/.local/node-v22.22.0-darwin-arm64" "$HOME/.local/node"
ln -sfn "$HOME/.local/node/bin/node" "$HOME/.local/bin/node"
ln -sfn "$HOME/.local/node/bin/npm" "$HOME/.local/bin/npm"
ln -sfn "$HOME/.local/node/bin/npx" "$HOME/.local/bin/npx"


Add local bin to current shell session when using fallback:

export PATH="$HOME/.local/bin:$PATH"

Step 5: Install uv and Python

Install uv:

curl -LsSf https://astral.sh/uv/install.sh | sh


Ensure uv is on PATH for the current session:

export PATH="$HOME/.local/bin:$PATH"


Install a managed Python:

uv python install

Step 6: Install skills packages

Use npx skills add with global scope when not inside a project repository:

GH_TOKEN=<token> npx skills add fwfutures/rome2rio-skills fwfutures/vibe-a-thon -g -y


If clone fails (often due CLT/git or auth issues), fallback to zipball workflow:

Download each repository zipball from GitHub API with GH_TOKEN.
Unzip into a temp folder.
Install from local extracted path:
npx skills add /path/to/extracted/repo -g -y


Security note:

Keep tokens in environment variables.
Do not echo tokens into logs or summaries.
Step 7: Verify tooling and skills

Run final verification commands:

export PATH="$HOME/.local/bin:$PATH"
which brew || true
node -v
npm -v
npx -v
uv --version
uv python list
npx skills list -g

Step 8: Report completion

Provide a concise final report including:

Installed vs already-present tools (brew, node, npm, npx, uv, python)
Skills installed successfully
Any blockers that remain (for example, CLT still pending)
Exact next command if one manual action is still needed
Troubleshooting quick guide
npx: command not found: ensure Node is installed and ~/.local/bin is on PATH.
Failed to clone repository with xcode-select message: complete CLT install or use zipball fallback.
Homebrew installer asks for sudo/admin: switch to user-local Node path when admin access is unavailable.
Agents: not linked in npx skills list -g: installation succeeded; linking depends on host agent runtime.
Weekly Installs
9
Repository
fwfutures/vibe-a-thon
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn