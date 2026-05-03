---
title: setup-windows-dev
url: https://skills.sh/fwfutures/vibe-a-thon/setup-windows-dev
---

# setup-windows-dev

skills/fwfutures/vibe-a-thon/setup-windows-dev
setup-windows-dev
Installation
$ npx skills add https://github.com/fwfutures/vibe-a-thon --skill setup-windows-dev
SKILL.md
Windows Node Dev Environment Setup

You are performing the setup — not instructing the user to do it. Run every command yourself using your tools. Before starting, tell the user:

"Setting up your Windows machine for Node development now. This will take a few minutes. If you see any permission popups (UAC prompts), please accept them." Then work through each step silently and report progress as you go (e.g. "✓ Node.js already installed", "Installing Git..."). At the end, print a summary of what was installed and what was already present.

Step 1: Detect architecture

Run this first — it determines which VC++ redistributable to download later.

$env:PROCESSOR_ARCHITECTURE

Result will be ARM64 or AMD64 (x64). Remember this for Step 5.
Step 2: Install Node.js (if not already installed)

Check first:

$nodePath = "C:\Program Files\nodejs\node.exe"
Test-Path $nodePath


If True — skip, report "✓ Node.js already installed", note the version:

& "C:\Program Files\nodejs\node.exe" --version


If False — install:

winget install --id OpenJS.NodeJS.LTS -e --source winget --accept-package-agreements --accept-source-agreements


After installing, update PATH for the current session so subsequent commands can find node:

$env:PATH = "C:\Program Files\nodejs;" + $env:PATH

Step 3: Fix PowerShell Execution Policy

This prevents "scripts disabled" errors when running npm/npx. No admin required. Check first:

(Get-ExecutionPolicy -Scope CurrentUser)


If result is RemoteSigned or Unrestricted — skip, report "✓ PowerShell execution policy already set". Otherwise — fix it:

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force

Step 4: Install Git (if not already installed)

Check first:

$gitPath = "C:\Program Files\Git\cmd\git.exe"
Test-Path $gitPath


Also try where.exe git in case it's installed elsewhere. If found — skip, report "✓ Git already installed". If not found — install:

winget install --id Git.Git -e --source winget --accept-package-agreements --accept-source-agreements


After installing, update PATH for the current session:

$env:PATH = "C:\Program Files\Git\cmd;" + $env:PATH

Step 5: Install Python (if not already installed)

Python is needed by many JS toolchains, skill frameworks, and build scripts. Check first:

where.exe python 2>$null


If found — skip, report "✓ Python already installed". If not found — install:

winget install --id Python.Python.3.12 -e --source winget --accept-package-agreements --accept-source-agreements


Python adds itself to the user PATH. Update for the current session — check which path was created:

$arm64 = "$env:LOCALAPPDATA\Programs\Python\Python312-arm64"
$x64   = "$env:LOCALAPPDATA\Programs\Python\Python312"
if (Test-Path $arm64) { $env:PATH = "$arm64;$arm64\Scripts;" + $env:PATH }
elseif (Test-Path $x64) { $env:PATH = "$x64;$x64\Scripts;" + $env:PATH }

Step 6: Install Visual C++ Redistributable (if not already installed)

Required on both ARM64 and x64 for native Node addons (Rollup, etc.). Without it you'll see Required DLL was not found errors. Check first — look for the registry key that the VC++ redist install leaves:

$vcKey = "HKLM:\SOFTWARE\Microsoft\VisualStudio\14.0\VC\Runtimes"
# ARM64
$arm64Installed = Test-Path "$vcKey\arm64"
# x64
$x64Installed   = Test-Path "$vcKey\x64"


If already installed for the correct architecture — skip, report "✓ VC++ Redistributable already installed". If not installed — download and install silently (this triggers a UAC prompt — the user was warned at the start): For ARM64:

Invoke-WebRequest -Uri "https://aka.ms/vs/17/release/vc_redist.arm64.exe" -OutFile "$env:TEMP\vc_redist.arm64.exe"
Start-Process -FilePath "$env:TEMP\vc_redist.arm64.exe" -ArgumentList '/install','/quiet','/norestart' -Wait


For x64:

Invoke-WebRequest -Uri "https://aka.ms/vs/17/release/vc_redist.x64.exe" -OutFile "$env:TEMP\vc_redist.x64.exe"
Start-Process -FilePath "$env:TEMP\vc_redist.x64.exe" -ArgumentList '/install','/quiet','/norestart' -Wait

Step 7: Verify everything works

Run these and capture output to include in the final summary:

$nodePath = "C:\Program Files\nodejs\node.exe"
if (Test-Path $nodePath) { & $nodePath --version }
$npmPath = "C:\Program Files\nodejs\npm.cmd"
if (Test-Path $npmPath) { & $npmPath --version }
$gitPath = "C:\Program Files\Git\cmd\git.exe"
if (Test-Path $gitPath) { & $gitPath --version }
python --version 2>$null

Step 8: Print final summary

After all steps complete, print a clear summary like:

Setup complete! Here's what happened:
✓ Node.js v24.x.x  (already installed)
✓ npm 11.x.x       (already installed)
✓ PowerShell policy set to RemoteSigned
✓ Git 2.x.x        (newly installed)
✓ Python 3.12.x    (newly installed)
✓ VC++ Redistributable ARM64  (newly installed)
Open a new terminal and you're ready to go.
To start a React project: npm create vite@latest my-app -- --template react

Adjust based on what was actually installed vs. already present.
Important notes
Always run commands yourself — never ask the user to run them.
Always check before installing. If something is already installed, skip it and say so.
Use npm.cmd instead of npm when invoking npm from within a shell that may not have the .ps1 execution policy fixed yet.
The session PATH must be updated after each install ($env:PATH = ...) so that subsequent steps can find the newly installed tools — the system PATH change only takes effect in new terminals, not the current one.
If a winget install fails (e.g. already installed via a different mechanism), check with where.exe or Test-Path before treating it as an error.
Weekly Installs
12
Repository
fwfutures/vibe-a-thon
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn