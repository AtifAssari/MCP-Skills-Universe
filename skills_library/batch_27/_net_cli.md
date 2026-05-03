---
title: .net cli
url: https://skills.sh/exceptionless/exceptionless/.net-cli
---

# .net cli

skills/exceptionless/exceptionless/.NET CLI
.NET CLI
Installation
$ npx skills add https://github.com/exceptionless/exceptionless --skill '.NET CLI'
SKILL.md
.NET CLI
Prerequisites
.NET SDK 10.0
NuGet feeds defined in NuGet.Config
Common Commands
Restore Packages
dotnet restore

Build Solution
dotnet build

Run Tests
# All tests
dotnet test

# By test name
dotnet test --filter "FullyQualifiedName~CanCreateOrganization"

# By class name
dotnet test --filter "ClassName~OrganizationTests"

# By category/trait
dotnet test --filter "Category=Integration"

Run Project
# Run the AppHost (recommended for full stack)
dotnet run --project src/Exceptionless.AppHost

# Run specific project
dotnet run --project src/Exceptionless.Web

Format Code
# Format all C# files
dotnet format

# Check without making changes
dotnet format --verify-no-changes

NuGet Configuration

Feeds are defined in NuGet.Config — do not add new sources unless explicitly requested.

Directory.Build.props

Shared settings live in src/Directory.Build.props:

Target framework versions
Common package references
Build properties

Keep changes consistent across the solution.

Build Configurations
# Debug build (default)
dotnet build

# Release build
dotnet build -c Release

# Clean and rebuild
dotnet clean && dotnet build

Watch Mode
# Run with hot reload
dotnet watch run --project src/Exceptionless.Web

Package Management
# Add package to project
dotnet add package Foundatio

# Remove package
dotnet remove package OldPackage

# List packages
dotnet list package

# Check for outdated packages
dotnet list package --outdated

Solution Management
# Build specific project
dotnet build src/Exceptionless.Core

# List projects in solution
dotnet sln list

Environment Variables
# Set environment for run
ASPNETCORE_ENVIRONMENT=Development dotnet run --project src/Exceptionless.Web

Troubleshooting
Clean Restore
# Clear NuGet cache and restore
dotnet nuget locals all --clear
dotnet restore

Verbose Build
dotnet build -v detailed

Weekly Installs
–
Repository
exceptionless/e…tionless
GitHub Stars
2.5K
First Seen
–