---
rating: ⭐⭐
title: nuget-manager
url: https://skills.sh/github/awesome-copilot/nuget-manager
---

# nuget-manager

skills/github/awesome-copilot/nuget-manager
nuget-manager
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill nuget-manager
Summary

NuGet package management for .NET projects using dotnet CLI with strict workflows for adds, removes, and version updates.

Enforces dotnet add and dotnet remove commands for package operations; direct file edits only allowed for version changes
Requires version verification via dotnet package search before updates, with support for both jq and PowerShell parsing
Supports centralized version management via Directory.Packages.props or per-project .csproj configuration
Mandatory dotnet restore verification after any version change to ensure compatibility
SKILL.md
NuGet Manager
Overview

This skill ensures consistent and safe management of NuGet packages across .NET projects. It prioritizes using the dotnet CLI to maintain project integrity and enforces a strict verification and restoration workflow for version updates.

Prerequisites
.NET SDK installed (typically .NET 8.0 SDK or later, or a version compatible with the target solution).
dotnet CLI available on your PATH.
jq (JSON processor) OR PowerShell (for version verification using dotnet package search).
Core Rules
NEVER directly edit .csproj, .props, or Directory.Packages.props files to add or remove packages. Always use dotnet add package and dotnet remove package commands.
DIRECT EDITING is ONLY permitted for changing versions of existing packages.
VERSION UPDATES must follow the mandatory workflow:
Verify the target version exists on NuGet.
Determine if versions are managed per-project (.csproj) or centrally (Directory.Packages.props).
Update the version string in the appropriate file.
Immediately run dotnet restore to verify compatibility.
Workflows
Adding a Package

Use dotnet add [<PROJECT>] package <PACKAGE_NAME> [--version <VERSION>]. Example: dotnet add src/MyProject/MyProject.csproj package Newtonsoft.Json

Removing a Package

Use dotnet remove [<PROJECT>] package <PACKAGE_NAME>. Example: dotnet remove src/MyProject/MyProject.csproj package Newtonsoft.Json

Updating Package Versions

When updating a version, follow these steps:

Verify Version Existence: Check if the version exists using the dotnet package search command with exact match and JSON formatting. Using jq: dotnet package search <PACKAGE_NAME> --exact-match --format json | jq -e '.searchResult[].packages[] | select(.version == "<VERSION>")' Using PowerShell: (dotnet package search <PACKAGE_NAME> --exact-match --format json | ConvertFrom-Json).searchResult.packages | Where-Object { $_.version -eq "<VERSION>" }

Determine Version Management:

Search for Directory.Packages.props in the solution root. If present, versions should be managed there via <PackageVersion Include="Package.Name" Version="1.2.3" />.
If absent, check individual .csproj files for <PackageReference Include="Package.Name" Version="1.2.3" />.

Apply Changes: Modify the identified file with the new version string.

Verify Stability: Run dotnet restore on the project or solution. If errors occur, revert the change and investigate.

Examples
User: "Add Serilog to the WebApi project"

Action: Execute dotnet add src/WebApi/WebApi.csproj package Serilog.

User: "Update Newtonsoft.Json to 13.0.3 in the whole solution"

Action:

Verify 13.0.3 exists: dotnet package search Newtonsoft.Json --exact-match --format json (and parse output to confirm "13.0.3" is present).
Find where it's defined (e.g., Directory.Packages.props).
Edit the file to update the version.
Run dotnet restore.
Weekly Installs
9.8K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass