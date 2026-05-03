---
title: ado-windows-git-bash-compatibility
url: https://skills.sh/josiahsiegel/claude-plugin-marketplace/ado-windows-git-bash-compatibility
---

# ado-windows-git-bash-compatibility

skills/josiahsiegel/claude-plugin-marketplace/ado-windows-git-bash-compatibility
ado-windows-git-bash-compatibility
Installation
$ npx skills add https://github.com/josiahsiegel/claude-plugin-marketplace --skill ado-windows-git-bash-compatibility
SKILL.md
Azure Pipelines: Windows & Git Bash Compatibility
Overview

Azure Pipelines frequently run on Windows agents, and teams often use Git Bash for scripting. This creates path conversion and shell compatibility challenges that can cause pipeline failures. This guide provides comprehensive solutions for Windows/Git Bash integration in Azure DevOps pipelines.

Critical Windows Agent Facts
Git Bash Integration

Microsoft's Official Position:

Microsoft advises avoiding mintty-based shells (like git-bash) for agent configuration
mintty is not fully compatible with native Windows Input/Output API
However, Git Bash tasks in pipelines are widely used and supported

Git Version Management:

Windows agents use Git bundled with agent software by default
Microsoft recommends using bundled Git version
Override available via System.PreferGitFromPath=true

Git Bash Location on Windows Agents:

C:\Program Files (x86)\Git\usr\bin\bash.exe
C:\Program Files\Git\usr\bin\bash.exe

Path Conversion Issues in Pipelines
The Core Problem

When using Bash tasks on Windows agents, Azure DevOps variables return Windows-style paths, but Git Bash (MINGW) performs automatic path conversion that can cause issues.

Common Failure Patterns
Issue 1: Backslash Escape in Bash
# ❌ FAILS - Backslashes treated as escape characters
- bash: |
    cd $(System.DefaultWorkingDirectory)  # d:\a\s\1 becomes d:as1


Solution:

# ✅ CORRECT - Use forward slashes or variable properly
- bash: |
    cd "$BUILD_SOURCESDIRECTORY"
    # Or use PWD variable which is already set correctly
    echo "Working in: $PWD"

Issue 2: Path Variables in Arguments
# ❌ FAILS - MINGW converts /d /s style arguments
- bash: |
    my-tool /d $(Build.SourcesDirectory)


Solution:

# ✅ CORRECT - Use double slashes or environment variable
- bash: |
    export MSYS_NO_PATHCONV=1
    my-tool /d $(Build.SourcesDirectory)
    unset MSYS_NO_PATHCONV

Issue 3: Colon-Separated Path Lists
# ❌ FAILS - MINGW converts colon-separated Windows paths
- bash: |
    export PATH="/usr/bin:$(Agent.ToolsDirectory)"


Solution:

# ✅ CORRECT - Use semicolon for Windows or convert properly
- bash: |
    # For Windows-style paths
    export PATH="/usr/bin;$(Agent.ToolsDirectory)"

Shell Detection in Pipeline Scripts
Method 1: Using $OSTYPE (Bash-Specific)
- bash: |
    case "$OSTYPE" in
      linux-gnu*)
        echo "Running on Linux agent"
        BUILD_PATH="$(Build.SourcesDirectory)"
        ;;
      darwin*)
        echo "Running on macOS agent"
        BUILD_PATH="$(Build.SourcesDirectory)"
        ;;
      msys*|mingw*|cygwin*)
        echo "Running on Windows agent with Git Bash"
        # Windows paths already work in MINGW, but may need conversion
        BUILD_PATH="$(Build.SourcesDirectory)"
        export MSYS_NO_PATHCONV=1
        ;;
      *)
        echo "Unknown OS: $OSTYPE"
        BUILD_PATH="$(Build.SourcesDirectory)"
        ;;
    esac

    echo "Build path: $BUILD_PATH"
    cd "$BUILD_PATH"
  displayName: 'Cross-platform path handling'

Method 2: Using uname (Most Portable)
- bash: |
    OS_TYPE=$(uname -s)

    case "$OS_TYPE" in
      Darwin*)
        echo "macOS agent detected"
        ;;
      Linux*)
        echo "Linux agent detected"
        # Check if WSL
        if grep -qi microsoft /proc/version 2>/dev/null; then
          echo "Running in WSL"
        fi
        ;;
      MINGW64*|MINGW32*)
        echo "Git Bash on Windows detected"
        export MSYS_NO_PATHCONV=1
        ;;
      CYGWIN*)
        echo "Cygwin on Windows detected"
        ;;
      MSYS_NT*)
        echo "MSYS on Windows detected"
        export MSYS_NO_PATHCONV=1
        ;;
      *)
        echo "Unknown OS: $OS_TYPE"
        ;;
    esac
  displayName: 'Detect shell environment'

Method 3: Using Agent.OS (Azure Pipelines Variable)
- bash: |
    if [ "$(Agent.OS)" = "Windows_NT" ]; then
      echo "Windows agent - applying MINGW path handling"
      export MSYS_NO_PATHCONV=1
    elif [ "$(Agent.OS)" = "Linux" ]; then
      echo "Linux agent"
    elif [ "$(Agent.OS)" = "Darwin" ]; then
      echo "macOS agent"
    fi
  displayName: 'Agent-specific configuration'

Path Conversion Control
MSYS_NO_PATHCONV (Primary Method)

Disables ALL automatic path conversion in MINGW/Git Bash:

- bash: |
    # Disable path conversion for this script
    export MSYS_NO_PATHCONV=1

    # Now Windows paths work as-is
    dotnet build /p:Configuration=Release
    docker run -v "$(Build.SourcesDirectory):/workspace" myimage

    # Optionally re-enable
    unset MSYS_NO_PATHCONV
  displayName: 'Build with path conversion disabled'

MSYS2_ARG_CONV_EXCL (Selective Exclusion)

Exclude specific argument patterns from conversion:

- bash: |
    # Exclude specific prefixes from conversion
    export MSYS2_ARG_CONV_EXCL="--config=;/p:"

    dotnet build /p:Configuration=Release --config=$(Build.SourcesDirectory)/app.config
  displayName: 'Selective path conversion'

Manual Conversion with cygpath

Convert between Windows and Unix paths explicitly:

- bash: |
    # Convert Windows path to Unix
    UNIX_PATH=$(cygpath -u "$(Build.SourcesDirectory)")
    echo "Unix path: $UNIX_PATH"

    # Convert Unix path to Windows
    WINDOWS_PATH=$(cygpath -w "$PWD")
    echo "Windows path: $WINDOWS_PATH"

    # Mixed format (forward slashes with drive letter)
    MIXED_PATH=$(cygpath -m "$(Build.SourcesDirectory)")
    echo "Mixed path: $MIXED_PATH"
  displayName: 'Path conversion examples'

Cross-Platform Pipeline Patterns
Pattern 1: Platform-Specific Steps with Conditions
jobs:
  - job: CrossPlatformBuild
    strategy:
      matrix:
        Linux:
          imageName: 'ubuntu-24.04'
          osType: 'Linux'
        Windows:
          imageName: 'windows-2025'
          osType: 'Windows_NT'
        macOS:
          imageName: 'macOS-15'
          osType: 'Darwin'
    pool:
      vmImage: $(imageName)

    steps:
      # Windows-specific setup
      - bash: |
          export MSYS_NO_PATHCONV=1
          echo "Windows Git Bash configuration applied"
        condition: eq(variables['Agent.OS'], 'Windows_NT')
        displayName: 'Windows Git Bash setup'

      # Cross-platform build
      - bash: |
          echo "Building on: $(Agent.OS)"
          cd "$(Build.SourcesDirectory)"
          npm install
          npm run build
        displayName: 'Cross-platform build'

Pattern 2: Reusable Template with Platform Detection
# File: templates/cross-platform-script.yml
parameters:
  - name: script
    type: string

steps:
  - bash: |
      # Auto-detect Windows and apply MSYS configuration
      if [ "$(Agent.OS)" = "Windows_NT" ]; then
        export MSYS_NO_PATHCONV=1
      fi

      # Run provided script
      ${{ parameters.script }}
    displayName: 'Cross-platform script execution'

# Usage in main pipeline:
steps:
  - template: templates/cross-platform-script.yml
    parameters:
      script: |
        dotnet build /p:Configuration=Release
        dotnet test --no-build

Pattern 3: PowerShell for Windows, Bash for Unix
- pwsh: |
    Write-Host "Building on Windows with PowerShell"
    dotnet build /p:Configuration=Release
  condition: eq(variables['Agent.OS'], 'Windows_NT')
  displayName: 'Windows build (PowerShell)'

- bash: |
    echo "Building on Unix with Bash"
    dotnet build -p:Configuration=Release
  condition: ne(variables['Agent.OS'], 'Windows_NT')
  displayName: 'Unix build (Bash)'

Azure DevOps CLI on Windows Agents
Common CLI Path Issues
# ❌ FAILS - Windows paths in bash arguments
- bash: |
    az pipelines run --id 123 --variables sourceDir=$(Build.SourcesDirectory)


Solution:

# ✅ CORRECT - Use MSYS_NO_PATHCONV or proper quoting
- bash: |
    export MSYS_NO_PATHCONV=1
    az pipelines run --id 123 --variables sourceDir="$(Build.SourcesDirectory)"

Repository Operations with Paths
- bash: |
    # Configure Git to handle Windows paths correctly
    git config --global core.autocrlf true
    git config --global core.safecrlf false

    # Clone with proper path handling
    export MSYS_NO_PATHCONV=1
    az repos pr create \
      --repository myrepo \
      --source-branch feature/new \
      --target-branch main
  displayName: 'Git operations on Windows agent'
  condition: eq(variables['Agent.OS'], 'Windows_NT')

Agent Configuration Best Practices
Configure Git for Windows Agents
- bash: |
    # Recommended Git configuration for Windows agents
    git config --global core.autocrlf true
    git config --global core.longpaths true
    git config --global core.symlinks false

    # Show configuration
    git config --list | grep core
  displayName: 'Configure Git for Windows'
  condition: eq(variables['Agent.OS'], 'Windows_NT')

Use System.PreferGitFromPath
# Use system Git instead of agent-bundled Git
variables:
  System.PreferGitFromPath: true

steps:
  - bash: |
      git --version
      which git
    displayName: 'Check Git version'

Agent .env Configuration

For self-hosted Windows agents, create .env file in agent root:

# File: agent/.env
System.PreferGitFromPath=true
MSYS_NO_PATHCONV=1

Troubleshooting Windows Pipeline Failures
Diagnostic Script
- bash: |
    echo "=== Environment Diagnostics ==="
    echo "Agent.OS: $(Agent.OS)"
    echo "Agent.OSArchitecture: $(Agent.OSArchitecture)"
    echo "System.DefaultWorkingDirectory: $(System.DefaultWorkingDirectory)"
    echo "Build.SourcesDirectory: $(Build.SourcesDirectory)"
    echo ""

    echo "=== Shell Detection ==="
    echo "OSTYPE: $OSTYPE"
    echo "MSYSTEM: $MSYSTEM"
    uname -a
    echo ""

    echo "=== Path Information ==="
    echo "PWD: $PWD"
    echo "HOME: $HOME"
    echo "PATH: $PATH"
    echo ""

    echo "=== Git Configuration ==="
    git --version
    which git
    git config --list | grep core
    echo ""

    echo "=== Path Conversion Test ==="
    echo "Windows-style: $(Build.SourcesDirectory)"
    if command -v cygpath &> /dev/null; then
      echo "Unix-style: $(cygpath -u "$(Build.SourcesDirectory)")"
      echo "Mixed-style: $(cygpath -m "$(Build.SourcesDirectory)")"
    fi
  displayName: 'Windows agent diagnostics'
  condition: eq(variables['Agent.OS'], 'Windows_NT')

Common Error Patterns and Fixes
Error: "No such file or directory"
# Error: bash: line 1: d:as1: No such file or directory

# ❌ Problem: Backslashes removed
- bash: cd $(System.DefaultWorkingDirectory)

# ✅ Solution: Quote the variable
- bash: cd "$(System.DefaultWorkingDirectory)"

Error: "Invalid switch"
# Error: Invalid switch - "/d"

# ❌ Problem: MINGW converts /d to Windows path
- bash: dotnet test /d:SonarQubeAnalysisPath=.

# ✅ Solution: Disable path conversion
- bash: |
    export MSYS_NO_PATHCONV=1
    dotnet test /d:SonarQubeAnalysisPath=.

Error: "Access denied" with spaces in path
# Error: Access to path 'C:\Program' is denied

# ❌ Problem: Unquoted path with spaces
- bash: my-tool $(Agent.ToolsDirectory)/mytool

# ✅ Solution: Always quote paths
- bash: my-tool "$(Agent.ToolsDirectory)/mytool"

Best Practices Summary
Always Do
Quote all path variables: "$(Build.SourcesDirectory)"
Use MSYS_NO_PATHCONV for Windows-specific commands
Detect platform using $(Agent.OS) or uname
Test on Windows agents if targeting Windows deployments
Use forward slashes in paths when possible (Git Bash compatible)
Never Do
❌ Use unquoted paths: cd $(Build.SourcesDirectory)
❌ Assume Bash = Linux (Windows has Git Bash)
❌ Hardcode platform-specific paths
❌ Mix PowerShell and Bash syntax in same script
❌ Ignore MINGW path conversion in arguments
Platform Detection Template

Use this at the start of complex cross-platform scripts:

- bash: |
    #!/bin/bash
    set -euo pipefail

    # Detect platform and configure
    if [ "$(Agent.OS)" = "Windows_NT" ]; then
      echo "Windows agent detected"
      export MSYS_NO_PATHCONV=1
      PATH_SEP=";"
    else
      echo "Unix-like agent detected"
      PATH_SEP=":"
    fi

    # Your script logic here
    echo "Build directory: $(Build.SourcesDirectory)"
    cd "$(Build.SourcesDirectory)"

    # Platform-agnostic operations
    npm install
    npm run build
  displayName: 'Cross-platform build script'

Additional Resources
Azure Pipelines Windows Agents
Git for Windows Documentation
MINGW Path Conversion
Azure Pipelines Variables
Quick Reference Card
Scenario	Solution
Bash script on Windows	Use export MSYS_NO_PATHCONV=1
Detect Windows agent	Check $(Agent.OS) = Windows_NT
Detect Git Bash	Check uname -s starts with MINGW
Convert Windows → Unix	cygpath -u "C:\path"
Convert Unix → Windows	cygpath -w "/c/path"
Quote paths with spaces	Always use "$(variable)"
Disable conversion for arg	export MSYS2_ARG_CONV_EXCL="pattern"
Check Git version	git --version && which git
Use system Git	Set System.PreferGitFromPath: true
Test path handling	Run diagnostic script above

When in doubt, use MSYS_NO_PATHCONV=1 for Windows agents running Bash tasks.

Weekly Installs
85
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