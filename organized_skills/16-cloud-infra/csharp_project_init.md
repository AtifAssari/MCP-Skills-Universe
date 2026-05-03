---
rating: ⭐⭐⭐
title: csharp-project-init
url: https://skills.sh/jim60105/copilot-prompt/csharp-project-init
---

# csharp-project-init

skills/jim60105/copilot-prompt/csharp-project-init
csharp-project-init
Installation
$ npx skills add https://github.com/jim60105/copilot-prompt --skill csharp-project-init
SKILL.md
C# Project Init

Set up a C# ASP.NET Core Web API project with proper tooling and configuration.

Git commit after each step that modifies or creates files. Skip commit if nothing to commit.

Steps

Ensure the Git working tree is clean:

git status


If the working directory is not clean, stop execution.

Check .NET SDK version (must be >= 10.0.103):

dotnet --version


Create the project using the webapi template without -n argument:

dotnet new webapi -controllers


Add Entity Framework Core 10 and related SQL Server NuGet packages. Don't use prerelease versions.

Check for EF Core Power Tools CLI:

efcpt --version


If not installed or version is lower than 10, reinstall:

dotnet tool install ErikEJ.EFCorePowerTools.Cli -g --version 10.*


Set up C# Global Usings in GlobalUsings.cs with common namespaces.

Add .gitignore file — refer to the gitignore-generator skill.

Add .gitattributes file:

# Set default behavior to automatically normalize line endings.
* text=auto

# Force batch scripts to always use CRLF line endings.
*.{cmd,[cC][mM][dD]} text eol=crlf
*.{bat,[bB][aA][tT]} text eol=crlf

# Force bash scripts to always use LF line endings.
*.sh text eol=lf

.env text eol=lf
Dockerfile text eol=lf

# Denote all files that are truly binary and should not be modified.
*.mp3 binary
*.wav binary
*.bmp binary
*.png binary
*.jpg binary
*.gif binary


Download the .editorconfig:

curl -sL https://gist.github.com/jim60105/ae6ba63978a2dc3ffb3ebb77344cc7f7/raw/47f342c4b793a32697af6d62022692c26f849c07/.editorconfig > .editorconfig


Let's do this step by step.

Weekly Installs
11
Repository
jim60105/copilot-prompt
GitHub Stars
18
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass