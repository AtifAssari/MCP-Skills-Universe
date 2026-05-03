---
rating: ⭐⭐⭐
title: powershell-shell-detection
url: https://skills.sh/josiahsiegel/claude-plugin-marketplace/powershell-shell-detection
---

# powershell-shell-detection

skills/josiahsiegel/claude-plugin-marketplace/powershell-shell-detection
powershell-shell-detection
Installation
$ npx skills add https://github.com/josiahsiegel/claude-plugin-marketplace --skill powershell-shell-detection
SKILL.md
PowerShell Shell Detection & Cross-Shell Compatibility

Critical guidance for distinguishing between PowerShell and Git Bash/MSYS2 shells on Windows, with shell-specific path handling and compatibility notes.

Shell Detection Priority (Windows)

When working on Windows, correctly identifying the shell environment is crucial for proper path handling and command execution.

Detection Order (Most Reliable First)
process.env.PSModulePath (PowerShell specific)
process.env.MSYSTEM (Git Bash/MinGW specific)
process.env.WSL_DISTRO_NAME (WSL specific)
uname -s output (Cross-shell, requires execution)
PowerShell Detection
Primary Indicators

PSModulePath (Most Reliable):

# PowerShell detection
if ($env:PSModulePath) {
    Write-Host "Running in PowerShell"
    # PSModulePath contains 3+ paths separated by semicolons
    $env:PSModulePath -split ';'
}

# Check PowerShell version
$PSVersionTable.PSVersion
# Output: 7.5.4 (PowerShell 7) or 5.1.x (Windows PowerShell)


PowerShell-Specific Variables:

# These only exist in PowerShell
$PSVersionTable    # Version info
$PSScriptRoot      # Script directory
$PSCommandPath     # Script full path
$IsWindows         # Platform detection (PS 7+)
$IsLinux           # Platform detection (PS 7+)
$IsMacOS           # Platform detection (PS 7+)

Shell Type Detection in Scripts
function Get-ShellType {
    if ($PSVersionTable) {
        return "PowerShell $($PSVersionTable.PSVersion)"
    }
    elseif ($env:PSModulePath -and ($env:PSModulePath -split ';').Count -ge 3) {
        return "PowerShell (detected via PSModulePath)"
    }
    else {
        return "Not PowerShell"
    }
}

Get-ShellType

Git Bash / MSYS2 Detection
Primary Indicators

MSYSTEM Environment Variable (Most Reliable):

# Bash detection in Git Bash/MSYS2
if [ -n "$MSYSTEM" ]; then
    echo "Running in Git Bash/MSYS2: $MSYSTEM"
fi

# MSYSTEM values:
# MINGW64 - Native Windows 64-bit environment
# MINGW32 - Native Windows 32-bit environment
# MSYS    - POSIX-compliant build environment


Secondary Detection Methods:

# Using OSTYPE (Bash-specific)
case "$OSTYPE" in
    msys*)   echo "MSYS/Git Bash" ;;
    cygwin*) echo "Cygwin" ;;
    linux*)  echo "Linux" ;;
    darwin*) echo "macOS" ;;
esac

# Using uname (Most portable)
case "$(uname -s)" in
    MINGW64*) echo "Git Bash 64-bit" ;;
    MINGW32*) echo "Git Bash 32-bit" ;;
    MSYS*)    echo "MSYS" ;;
    CYGWIN*)  echo "Cygwin" ;;
    Linux*)   echo "Linux" ;;
    Darwin*)  echo "macOS" ;;
esac

Cross-Shell Compatibility on Windows
Critical Differences
Aspect	PowerShell	Git Bash/MSYS2
Environment Variable	$env:VARIABLE	$VARIABLE
Path Separator	; (semicolon)	: (colon)
Path Style	C:\Windows\System32	/c/Windows/System32
Home Directory	$env:USERPROFILE	$HOME
Temp Directory	$env:TEMP	/tmp
Command Format	Get-ChildItem	ls (native command)
Aliases	PowerShell cmdlet aliases	Unix command aliases
Path Handling: PowerShell vs Git Bash

PowerShell Path Handling:

# Native Windows paths work directly
$path = "C:\Users\John\Documents"
Test-Path $path  # True

# Forward slashes also work in PowerShell 7+
$path = "C:/Users/John/Documents"
Test-Path $path  # True

# Use Join-Path for cross-platform compatibility
$configPath = Join-Path -Path $PSScriptRoot -ChildPath "config.json"

# Use [System.IO.Path] for advanced scenarios
$fullPath = [System.IO.Path]::Combine($home, "documents", "file.txt")


Git Bash Path Handling:

# Git Bash uses Unix-style paths
path="/c/Users/John/Documents"
test -d "$path" && echo "Directory exists"

# Automatic path conversion (CAUTION)
# Git Bash converts Unix-style paths to Windows-style
# /c/Users → C:\Users (automatic)
# Arguments starting with / may be converted unexpectedly

# Use cygpath for manual conversion
cygpath -u "C:\path"      # → /c/path (Unix format)
cygpath -w "/c/path"      # → C:\path (Windows format)
cygpath -m "/c/path"      # → C:/path (Mixed format)

Automatic Path Conversion in Git Bash (CRITICAL)

Git Bash/MSYS2 automatically converts paths in certain scenarios, which can cause issues:

What Triggers Conversion
# Leading forward slash triggers conversion
command /foo         # Converts to C:\msys64\foo

# Path lists with colons
export PATH=/foo:/bar  # Converts to C:\msys64\foo;C:\msys64\bar

# Arguments after dashes
command --path=/foo    # Converts to --path=C:\msys64\foo

What's Exempt from Conversion
# Arguments with equals sign (variable assignments)
VAR=/foo command      # NOT converted

# Drive specifiers
command C:/path       # NOT converted

# Arguments with semicolons (already Windows format)
command "C:\foo;D:\bar"  # NOT converted

# Double slashes (Windows switches)
command //e //s       # NOT converted

Disabling Path Conversion
# Disable ALL conversion (Git Bash)
export MSYS_NO_PATHCONV=1
command /foo  # Stays as /foo

# Exclude specific patterns (MSYS2)
export MSYS2_ARG_CONV_EXCL="*"           # Exclude everything
export MSYS2_ARG_CONV_EXCL="--dir=;/test"  # Specific prefixes

When to Use PowerShell vs Git Bash on Windows
Use PowerShell When:
✅ Windows-specific tasks - Registry, WMI, Windows services
✅ Azure/Microsoft 365 automation - Az, Microsoft.Graph modules
✅ Module ecosystem - Leverage PSGallery modules
✅ Object-oriented pipelines - Rich object manipulation
✅ Native Windows integration - Built into Windows
✅ CI/CD with pwsh - GitHub Actions, Azure DevOps
✅ Cross-platform scripting - PowerShell 7 works on Linux/macOS

Example PowerShell Scenario:

# Azure VM management with Az module
Connect-AzAccount
Get-AzVM -ResourceGroupName "Production" |
    Where-Object {$_.PowerState -eq "VM running"} |
    Stop-AzVM -Force

Use Git Bash When:
✅ Unix tool compatibility - sed, awk, grep, find
✅ Git operations - Native Git command-line experience
✅ POSIX script execution - Running Linux shell scripts
✅ Cross-platform shell scripts - Bash scripts from Linux/macOS
✅ Text processing - Unix text utilities (sed, awk, cut)
✅ Development workflows - Node.js, Python, Ruby with Unix tools

Example Git Bash Scenario:

# Git workflow with Unix tools
git log --oneline | grep -i "feature" | awk '{print $1}' |
    xargs git show --stat

Shell-Aware Script Design
Detect and Adapt (PowerShell)
# Detect if running in PowerShell or Git Bash context
function Test-PowerShellContext {
    return ($null -ne $PSVersionTable)
}

# Adapt path handling based on context
function Get-CrossPlatformPath {
    param([string]$Path)

    if (Test-PowerShellContext) {
        # PowerShell: Use Join-Path
        return (Resolve-Path $Path -ErrorAction SilentlyContinue).Path
    }
    else {
        # Non-PowerShell context
        Write-Warning "Not running in PowerShell. Path operations may differ."
        return $Path
    }
}

Detect and Adapt (Bash)
# Detect shell environment
detect_shell() {
    if [ -n "$MSYSTEM" ]; then
        echo "git-bash"
    elif [ -n "$PSModulePath" ]; then
        echo "powershell"
    elif [ -n "$WSL_DISTRO_NAME" ]; then
        echo "wsl"
    else
        echo "unix"
    fi
}

# Adapt path handling
convert_path() {
    local path="$1"
    local shell_type=$(detect_shell)

    case "$shell_type" in
        git-bash)
            # Convert Windows path to Unix style
            echo "$path" | sed 's|\\|/|g' | sed 's|^\([A-Z]\):|/\L\1|'
            ;;
        *)
            echo "$path"
            ;;
    esac
}

# Usage
shell_type=$(detect_shell)
echo "Running in: $shell_type"

Environment Variable Comparison
Common Environment Variables
Variable	PowerShell	Git Bash	Purpose
Username	$env:USERNAME	$USER	Current user
Home Directory	$env:USERPROFILE	$HOME	User home
Temp Directory	$env:TEMP	/tmp	Temporary files
Path List	$env:Path (; sep)	$PATH (: sep)	Executable paths
Shell Detection	$env:PSModulePath	$MSYSTEM	Shell identifier
Cross-Shell Variable Access

PowerShell accessing environment variables:

$env:PATH              # Current PATH
$env:PSModulePath      # PowerShell module paths
$env:MSYSTEM           # Would be empty in PowerShell
[Environment]::GetEnvironmentVariable("PATH", "Machine")  # System PATH


Git Bash accessing environment variables:

echo $PATH             # Current PATH
echo $MSYSTEM          # Git Bash: MINGW64, MINGW32, or MSYS
echo $PSModulePath     # Would be empty in pure Bash

Practical Examples
Example 1: Cross-Shell File Finding

PowerShell:

# Find files modified in last 7 days
Get-ChildItem -Path "C:\Projects" -Recurse -File |
    Where-Object { $_.LastWriteTime -gt (Get-Date).AddDays(-7) } |
    Select-Object FullName, LastWriteTime


Git Bash:

# Same operation in Git Bash
find /c/Projects -type f -mtime -7 -exec ls -lh {} \;

Example 2: Process Management

PowerShell:

# Stop all Chrome processes
Get-Process chrome -ErrorAction SilentlyContinue | Stop-Process -Force


Git Bash:

# Same operation in Git Bash
ps aux | grep chrome | awk '{print $2}' | xargs kill -9 2>/dev/null

Example 3: Text File Processing

PowerShell:

# Extract unique email addresses from logs
Get-Content "logs.txt" |
    Select-String -Pattern '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' |
    ForEach-Object { $_.Matches.Value } |
    Sort-Object -Unique


Git Bash:

# Same operation in Git Bash
grep -oE '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' logs.txt |
    sort -u

Troubleshooting Cross-Shell Issues
Issue 1: Command Not Found

Problem: Command works in one shell but not another

# PowerShell
Get-Process  # Works

# Git Bash
Get-Process  # Command not found


Solution: Understand that PowerShell cmdlets don't exist in Bash. Use native commands or install PowerShell Core (pwsh) in Git Bash:

# Run PowerShell from Git Bash
pwsh -Command "Get-Process"

Issue 2: Path Format Mismatches

Problem: Paths don't work across shells

# Git Bash path
/c/Users/John/file.txt  # Works in Bash

# PowerShell
Test-Path "/c/Users/John/file.txt"  # May fail


Solution: Use cygpath for conversion or normalize paths:

# Convert to Windows format for PowerShell
win_path=$(cygpath -w "/c/Users/John/file.txt")
pwsh -Command "Test-Path '$win_path'"

Issue 3: Alias Conflicts

Problem: ls, cd, cat behave differently

# PowerShell
ls  # Actually runs Get-ChildItem

# Git Bash
ls  # Runs native Unix ls command


Solution: Use full cmdlet names in PowerShell scripts:

# Instead of: ls
Get-ChildItem  # Explicit cmdlet name

Best Practices Summary
PowerShell Scripts
✅ Use $PSScriptRoot for script-relative paths
✅ Use Join-Path or [IO.Path]::Combine() for paths
✅ Avoid hardcoded backslashes
✅ Use full cmdlet names (no aliases)
✅ Test on all target platforms
✅ Use $IsWindows, $IsLinux, $IsMacOS for platform detection
Git Bash Scripts
✅ Check $MSYSTEM for Git Bash detection
✅ Use cygpath for path conversion when needed
✅ Set MSYS_NO_PATHCONV=1 to disable auto-conversion if needed
✅ Quote paths with spaces
✅ Use Unix-style paths (/c/...) within Bash
✅ Convert to Windows paths when calling Windows tools
Cross-Shell Development
✅ Document which shell your script requires
✅ Add shell detection at script start
✅ Provide clear error messages for wrong shell
✅ Consider creating wrapper scripts for cross-shell compatibility
✅ Test in both PowerShell and Git Bash if supporting both
Resources
PowerShell Documentation
Git for Windows Documentation
MSYS2 Documentation
Cygpath Documentation

Last Updated: October 2025

Weekly Installs
108
Repository
josiahsiegel/cl…ketplace
GitHub Stars
33
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass