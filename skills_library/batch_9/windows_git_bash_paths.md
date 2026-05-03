---
title: windows-git-bash-paths
url: https://skills.sh/josiahsiegel/claude-plugin-marketplace/windows-git-bash-paths
---

# windows-git-bash-paths

skills/josiahsiegel/claude-plugin-marketplace/windows-git-bash-paths
windows-git-bash-paths
Installation
$ npx skills add https://github.com/josiahsiegel/claude-plugin-marketplace --skill windows-git-bash-paths
SKILL.md
🚨 CRITICAL GUIDELINES
Windows File Path Requirements

MANDATORY: Always Use Backslashes on Windows for File Paths

When using Edit or Write tools on Windows, you MUST use backslashes (\) in file paths, NOT forward slashes (/).

Examples:

❌ WRONG: D:/repos/project/file.tsx
✅ CORRECT: D:\repos\project\file.tsx

This applies to:

Edit tool file_path parameter
Write tool file_path parameter
All file operations on Windows systems
Documentation Guidelines

NEVER create new documentation files unless explicitly requested by the user.

Priority: Update existing README.md files rather than creating new documentation
Repository cleanliness: Keep repository root clean - only README.md unless user requests otherwise
Style: Documentation should be concise, direct, and professional - avoid AI-generated tone
User preference: Only create additional .md files when user specifically asks for documentation
Windows and Git Bash Path Handling for SSDT
Overview

SQL Server development is Windows-heavy, and many developers use Git Bash (MINGW/MSYS2) as their preferred shell on Windows. This creates unique path conversion challenges when working with Windows-native tools like SqlPackage, MSBuild, and Visual Studio that expect Windows-style paths.

This skill provides comprehensive guidance on handling path conversion issues, shell detection, and best practices for SSDT workflows on Windows with Git Bash.

The Path Conversion Problem
What Happens in Git Bash/MINGW

Git Bash automatically converts POSIX-style paths to Windows paths, but this can cause issues with command-line arguments:

Automatic Conversions:

/foo → C:/Program Files/Git/usr/foo
/foo:/bar → C:\msys64\foo;C:\msys64\bar
--dir=/foo → --dir=C:/msys64/foo

Problematic for SqlPackage:

# Git Bash converts /Action to a path!
sqlpackage /Action:Publish /SourceFile:MyDB.dacpac
# Becomes: sqlpackage C:/Program Files/Git/usr/Action:Publish ...

What Triggers Conversion

✓ Leading forward slash (/) in arguments ✓ Colon-separated path lists ✓ Arguments after - or , with path components

What's Exempt

✓ Arguments containing = (variable assignments) ✓ Drive specifiers (C:) ✓ Arguments with ; (already Windows format) ✓ Arguments starting with // (Windows switches)

Solutions for SqlPackage in Git Bash
Method 1: MSYS_NO_PATHCONV (Recommended)

Disable path conversion for specific commands:

# Temporarily disable path conversion
MSYS_NO_PATHCONV=1 sqlpackage /Action:Publish \
  /SourceFile:"MyDatabase.dacpac" \
  /TargetServerName:"localhost" \
  /TargetDatabaseName:"MyDB"

# Works for all SqlPackage actions
MSYS_NO_PATHCONV=1 sqlpackage /Action:Extract \
  /SourceConnectionString:"Server=localhost;Database=MyDB;Integrated Security=True;" \
  /TargetFile:"MyDB_backup.dacpac"


Important Notes:

The VALUE doesn't matter - setting to 0, false, or empty still disables conversion
Only matters that variable is DEFINED
To re-enable: env -u MSYS_NO_PATHCONV
Method 2: Double Slash // (Alternative)

Use double slashes for SqlPackage parameters:

# Works in Git Bash and CMD
sqlpackage //Action:Publish \
  //SourceFile:MyDatabase.dacpac \
  //TargetServerName:localhost \
  //TargetDatabaseName:MyDB

# Extract with double slashes
sqlpackage //Action:Extract \
  //SourceConnectionString:"Server=localhost;Database=MyDB;Integrated Security=True;" \
  //TargetFile:output.dacpac


Advantages:

No environment variable needed
Works across shells
Shell-agnostic scripts
Method 3: Use Windows-Style Paths with Quotes

Always quote paths with backslashes:

# Quoted Windows paths work in Git Bash
MSYS_NO_PATHCONV=1 sqlpackage /Action:Publish \
  /SourceFile:"D:\Projects\MyDB\bin\Release\MyDB.dacpac" \
  /TargetConnectionString:"Server=localhost;Database=MyDB;Integrated Security=True;"

# Or with forward slashes (Windows accepts both)
MSYS_NO_PATHCONV=1 sqlpackage /Action:Publish \
  /SourceFile:"D:/Projects/MyDB/bin/Release/MyDB.dacpac" \
  /TargetConnectionString:"Server=localhost;Database=MyDB;Integrated Security=True;"

Method 4: Switch to PowerShell or CMD

For Windows-native tools, consider using native shells:

# PowerShell (recommended for Windows SSDT workflows)
sqlpackage /Action:Publish `
  /SourceFile:"MyDatabase.dacpac" `
  /TargetServerName:"localhost" `
  /TargetDatabaseName:"MyDB"

:: CMD
sqlpackage /Action:Publish ^
  /SourceFile:"MyDatabase.dacpac" ^
  /TargetServerName:"localhost" ^
  /TargetDatabaseName:"MyDB"

Shell Detection for Scripts
Bash Script Detection
#!/bin/bash

# Method 1: Check $OSTYPE
case "$OSTYPE" in
  msys*)       # MSYS/Git Bash/MinGW
    export MSYS_NO_PATHCONV=1
    SQLPACKAGE_ARGS="/Action:Publish /SourceFile:MyDB.dacpac"
    ;;
  cygwin*)     # Cygwin
    export MSYS_NO_PATHCONV=1
    SQLPACKAGE_ARGS="/Action:Publish /SourceFile:MyDB.dacpac"
    ;;
  linux-gnu*)  # Linux
    SQLPACKAGE_ARGS="/Action:Publish /SourceFile:MyDB.dacpac"
    ;;
  darwin*)     # macOS
    SQLPACKAGE_ARGS="/Action:Publish /SourceFile:MyDB.dacpac"
    ;;
esac

sqlpackage $SQLPACKAGE_ARGS

# Method 2: Check uname -s (most portable)
case "$(uname -s)" in
  MINGW64*|MINGW32*)
    # Git Bash
    export MSYS_NO_PATHCONV=1
    echo "Git Bash detected - path conversion disabled"
    ;;
  MSYS_NT*)
    # MSYS
    export MSYS_NO_PATHCONV=1
    echo "MSYS detected - path conversion disabled"
    ;;
  CYGWIN*)
    # Cygwin
    export MSYS_NO_PATHCONV=1
    echo "Cygwin detected - path conversion disabled"
    ;;
  Linux*)
    # Linux or WSL
    echo "Linux detected"
    ;;
  Darwin*)
    # macOS
    echo "macOS detected"
    ;;
esac

# Method 3: Check $MSYSTEM (Git Bash specific)
if [ -n "$MSYSTEM" ]; then
  # Running in Git Bash/MSYS2
  export MSYS_NO_PATHCONV=1
  echo "MSYS environment detected: $MSYSTEM"
  case "$MSYSTEM" in
    MINGW64) echo "64-bit native Windows environment" ;;
    MINGW32) echo "32-bit native Windows environment" ;;
    MSYS)    echo "POSIX-compliant environment" ;;
  esac
fi

Complete Build Script Example
#!/bin/bash
# build-and-deploy.sh - Cross-platform SSDT build script

set -e  # Exit on error

# Detect shell and set path conversion
if [ -n "$MSYSTEM" ]; then
  echo "Git Bash/MSYS2 detected - disabling path conversion"
  export MSYS_NO_PATHCONV=1
fi

# Variables
PROJECT_NAME="MyDatabase"
BUILD_CONFIG="Release"
DACPAC_PATH="bin/${BUILD_CONFIG}/${PROJECT_NAME}.dacpac"
TARGET_SERVER="${SQL_SERVER:-localhost}"
TARGET_DB="${SQL_DATABASE:-MyDB}"

# Build
echo "Building ${PROJECT_NAME}..."
dotnet build "${PROJECT_NAME}.sqlproj" -c "$BUILD_CONFIG"

# Verify DACPAC exists
if [ ! -f "$DACPAC_PATH" ]; then
  echo "ERROR: DACPAC not found at $DACPAC_PATH"
  exit 1
fi

echo "DACPAC built successfully: $DACPAC_PATH"

# Deploy
echo "Deploying to ${TARGET_SERVER}/${TARGET_DB}..."

# Use double-slash method for maximum compatibility
sqlpackage //Action:Publish \
  //SourceFile:"$DACPAC_PATH" \
  //TargetServerName:"$TARGET_SERVER" \
  //TargetDatabaseName:"$TARGET_DB" \
  //p:BlockOnPossibleDataLoss=False

echo "Deployment complete!"

Common SSDT Path Issues in Git Bash
Issue 1: DACPAC File Paths

Problem:

# Git Bash mangles the path
sqlpackage /Action:Publish /SourceFile:./bin/Release/MyDB.dacpac
# Error: Cannot find file


Solution:

# Use MSYS_NO_PATHCONV
MSYS_NO_PATHCONV=1 sqlpackage /Action:Publish \
  /SourceFile:"./bin/Release/MyDB.dacpac"

# OR use absolute Windows path
MSYS_NO_PATHCONV=1 sqlpackage /Action:Publish \
  /SourceFile:"D:/Projects/MyDB/bin/Release/MyDB.dacpac"

# OR use double slashes
sqlpackage //Action:Publish //SourceFile:./bin/Release/MyDB.dacpac

Issue 2: SQL Project File Paths

Problem:

# Path with spaces causes issues
dotnet build "D:/Program Files/MyProject/Database.sqlproj"
# Works in Git Bash (dotnet handles paths correctly)

# But MSBuild paths may fail
msbuild "D:/Program Files/MyProject/Database.sqlproj"
# May fail if not quoted properly


Solution:

# Always quote paths with spaces
dotnet build "D:/Program Files/MyProject/Database.sqlproj"

# Use backslashes for MSBuild on Windows
msbuild "D:\Program Files\MyProject\Database.sqlproj"

# Or use 8.3 short names (no spaces)
msbuild "D:/PROGRA~1/MyProject/Database.sqlproj"

Issue 3: Publish Profile Paths

Problem:

# Publish profile not found
sqlpackage /Action:Publish \
  /SourceFile:MyDB.dacpac \
  /Profile:./Profiles/Production.publish.xml


Solution:

# Use MSYS_NO_PATHCONV with quoted paths
MSYS_NO_PATHCONV=1 sqlpackage /Action:Publish \
  /SourceFile:"MyDB.dacpac" \
  /Profile:"./Profiles/Production.publish.xml"

# Or absolute Windows path
MSYS_NO_PATHCONV=1 sqlpackage /Action:Publish \
  /SourceFile:"D:/Projects/MyDB.dacpac" \
  /Profile:"D:/Projects/Profiles/Production.publish.xml"

Issue 4: Connection Strings

Problem:

# File paths in connection strings
/SourceConnectionString:"Server=localhost;Database=MyDB;Integrated Security=True;AttachDbFilename=D:/Data/MyDB.mdf"
# Path gets mangled


Solution:

# Quote entire connection string
MSYS_NO_PATHCONV=1 sqlpackage /Action:Extract \
  /SourceConnectionString:"Server=localhost;Database=MyDB;Integrated Security=True;AttachDbFilename=D:\Data\MyDB.mdf" \
  /TargetFile:"output.dacpac"

# Or use double backslashes in connection string
/SourceConnectionString:"Server=localhost;Database=MyDB;Integrated Security=True;AttachDbFilename=D:\\Data\\MyDB.mdf"

CI/CD Considerations
GitHub Actions with Git Bash
name: SSDT Build and Deploy

on: [push]

jobs:
  build:
    runs-on: windows-latest
    defaults:
      run:
        shell: bash  # Use Git Bash

    steps:
      - uses: actions/checkout@v4

      - name: Setup .NET
        uses: actions/setup-dotnet@v4
        with:
          dotnet-version: '8.0.x'

      - name: Install SqlPackage
        run: dotnet tool install -g Microsoft.SqlPackage

      - name: Build Database Project
        run: dotnet build Database.sqlproj -c Release

      - name: Deploy with Path Conversion Disabled
        env:
          MSYS_NO_PATHCONV: 1
        run: |
          sqlpackage /Action:Publish \
            /SourceFile:"bin/Release/MyDatabase.dacpac" \
            /TargetServerName:"localhost" \
            /TargetDatabaseName:"MyDB"

PowerShell Alternative (Recommended for Windows)
jobs:
  build:
    runs-on: windows-latest
    defaults:
      run:
        shell: pwsh  # Use PowerShell - no path issues

    steps:
      - name: Deploy Database
        run: |
          sqlpackage /Action:Publish `
            /SourceFile:"bin/Release/MyDatabase.dacpac" `
            /TargetServerName:"localhost" `
            /TargetDatabaseName:"MyDB"

Best Practices Summary
For Interactive Development
Use PowerShell or CMD for SSDT on Windows - avoids path conversion issues entirely
If using Git Bash, set MSYS_NO_PATHCONV=1 in your shell profile for SSDT work
Always quote paths containing spaces or special characters
Use absolute paths when possible to avoid ambiguity
For Scripts
Detect shell environment and set MSYS_NO_PATHCONV=1 conditionally
Use double-slash // syntax for SqlPackage arguments (most portable)
Prefer PowerShell for Windows-specific workflows (build scripts, CI/CD)
Test scripts on all target platforms (Windows PowerShell, Git Bash, Linux)
For CI/CD
Use PowerShell shell in GitHub Actions for Windows runners (shell: pwsh)
Self-hosted Windows agents - use native Windows paths and shells
Set MSYS_NO_PATHCONV=1 as environment variable if Git Bash required
Prefer dotnet CLI over MSBuild for cross-platform compatibility
For Teams
Document shell requirements in repository README
Provide scripts for all shells (bash, PowerShell, CMD)
Standardize on PowerShell for Windows SSDT workflows when possible
Use containerized builds to avoid shell-specific issues
Quick Reference
Environment Variables
# Disable path conversion (Git Bash/MSYS2/Cygwin)
export MSYS_NO_PATHCONV=1

# Re-enable path conversion
env -u MSYS_NO_PATHCONV

SqlPackage Command Templates
# Git Bash - Method 1 (MSYS_NO_PATHCONV)
MSYS_NO_PATHCONV=1 sqlpackage /Action:Publish /SourceFile:"MyDB.dacpac" /TargetServerName:"localhost" /TargetDatabaseName:"MyDB"

# Git Bash - Method 2 (Double Slash)
sqlpackage //Action:Publish //SourceFile:MyDB.dacpac //TargetServerName:localhost //TargetDatabaseName:MyDB

# PowerShell (Recommended for Windows)
sqlpackage /Action:Publish /SourceFile:"MyDB.dacpac" /TargetServerName:"localhost" /TargetDatabaseName:"MyDB"

# CMD
sqlpackage /Action:Publish /SourceFile:"MyDB.dacpac" /TargetServerName:"localhost" /TargetDatabaseName:"MyDB"

Shell Detection One-Liners
# Check if Git Bash/MSYS
[ -n "$MSYSTEM" ] && echo "Git Bash/MSYS2 detected"

# Check uname
[[ "$(uname -s)" =~ ^MINGW ]] && echo "Git Bash detected"

# Set path conversion conditionally
[ -n "$MSYSTEM" ] && export MSYS_NO_PATHCONV=1

Resources
Git Bash Path Conversion Guide
MSYS2 Path Conversion Documentation
SqlPackage Documentation
Microsoft.Build.Sql SDK
Git for Windows
Troubleshooting
"Invalid parameter" errors

Symptom: SqlPackage reports "Invalid parameter" or "Unknown action" Cause: Git Bash converting /Action to a file path Fix: Use MSYS_NO_PATHCONV=1 or double-slash //Action

"File not found" with valid paths

Symptom: DACPAC or project file not found despite correct path Cause: Path conversion mangling the file path Fix: Quote paths and use MSYS_NO_PATHCONV=1

Build succeeds but publish fails

Symptom: dotnet build works but sqlpackage fails Cause: dotnet CLI handles paths correctly, but SqlPackage uses / parameters Fix: Use MSYS_NO_PATHCONV=1 for SqlPackage commands only

Spaces in paths cause errors

Symptom: Paths with "Program Files" or other spaces fail Cause: Unquoted paths split into multiple arguments Fix: Always quote paths: /SourceFile:"D:/Program Files/MyDB.dacpac"

Weekly Installs
86
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