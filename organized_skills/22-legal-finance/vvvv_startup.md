---
rating: ⭐⭐⭐
title: vvvv-startup
url: https://skills.sh/tebjan/vvvv-skills/vvvv-startup
---

# vvvv-startup

skills/tebjan/vvvv-skills/vvvv-startup
vvvv-startup
Installation
$ npx skills add https://github.com/tebjan/vvvv-skills --skill vvvv-startup
SKILL.md
Launching vvvv gamma
Filesystem Paths
Location	Path
Install directory	C:\Program Files\vvvv\vvvv_gamma_X.Y-win-x64\
User data (AppData)	%LOCALAPPDATA%\vvvv\gamma\
Documents root	%USERPROFILE%\Documents\vvvv\gamma\
Sketches	%USERPROFILE%\Documents\vvvv\gamma\Sketches
Exports	%USERPROFILE%\Documents\vvvv\gamma\Exports
User packages	%LOCALAPPDATA%\vvvv\gamma\nugets
Log file (when enabled)	%USERPROFILE%\Documents\vvvv\gamma\vvvv.log

Preview builds use gamma-preview instead of gamma in the above paths.

Normal Launch
# Launch vvvv (opens with default empty patch)
"C:\Program Files\vvvv\vvvv_gamma_7.0-win-x64\vvvv.exe"

# Open a specific patch
vvvv.exe MyProject.vl

# Open multiple files
vvvv.exe --open "FileA.vl;FileB.vl"

Package Repositories and Editable Packages

These two arguments work together and are the most important for development:

--package-repositories tells vvvv where to look for packages. Provide the parent folder of each package (the folder containing the package directory, not the package directory itself).
--editable-packages tells vvvv which packages from those repositories to load from source instead of pre-compiled cache (read-only). Glob patterns are supported.

You must use both together when working on a package from source:

# Given this folder structure:
#   D:\Projects\
#     VL.MyLib\           <-- the package
#       VL.MyLib.vl
#     VL.MyOtherLib\      <-- another package
#       VL.MyOtherLib.vl

# The parent folder "D:\Projects" is the package repository
vvvv.exe --package-repositories "D:\Projects" --editable-packages "VL.MyLib*" --debug

# Multiple repositories (semi-colon separated)
vvvv.exe --package-repositories "D:\Projects;D:\SharedLibs" --editable-packages "VL.MyLib*;VL.SharedUtils" --debug

# Open a specific help patch for testing
vvvv.exe --package-repositories "D:\Projects" --editable-packages "VL.MyLib*" -o "D:\Projects\VL.MyLib\help\HowTo Use Feature.vl" --debug


Without --package-repositories, vvvv won't find your local package sources, and --editable-packages will have no effect.

Common Argument Combinations
# Development: debug symbols + allow multiple instances
vvvv.exe MyProject.vl --debug --allowmultiple

# Troubleshooting: skip cache, enable logging
vvvv.exe MyProject.vl --nocache --log

# Minimal startup: no extensions, no backend (fast launch for patch editing)
vvvv.exe --noextensions --disable-backend

# Paused on startup (runtime won't start until you press play)
vvvv.exe MyProject.vl --stoppedonstartup

# Skip splash screen
vvvv.exe --no-splash


For the complete argument reference, see cli-reference.md.

Detecting vvvv Installations

To find vvvv programmatically:

Windows Registry: Enumerate HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall for subkeys starting with vvvv_gamma_. Read the InstallLocation value.
Default path: Scan C:\Program Files\vvvv\ for directories matching vvvv_gamma_*.
Version parsing: Extract version from directory name format vvvv_gamma_MAJOR.MINOR[-PREVIEW-HASH-PLATFORM].
Filtering: Exclude -beta, -alpha, -rc, -test, -dev, etc. variants if not explicitly requested.
Selection: Sort by major DESC, minor DESC, preview number DESC. Pick the latest and ask the user if that or another one should be used.

The executable is at <install-dir>\vvvv.exe.

Weekly Installs
21
Repository
tebjan/vvvv-skills
GitHub Stars
23
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass