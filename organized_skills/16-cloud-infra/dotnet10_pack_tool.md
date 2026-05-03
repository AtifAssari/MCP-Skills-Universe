---
rating: ⭐⭐⭐
title: dotnet10-pack-tool
url: https://skills.sh/rysweet/amplihack/dotnet10-pack-tool
---

# dotnet10-pack-tool

skills/rysweet/amplihack/dotnet10-pack-tool
dotnet10-pack-tool
Installation
$ npx skills add https://github.com/rysweet/amplihack --skill dotnet10-pack-tool
SKILL.md
.NET 10 Hybrid Pack Tool
Purpose

Guides you through creating hybrid .NET 10 tool packages that combine Native AOT for maximum performance on select platforms with CoreCLR fallback for universal compatibility.

When I Activate

I automatically load when you mention:

"pack .NET tool" or "dotnet pack AOT"
"Native AOT tool" or "hybrid .NET tool"
"ToolPackageRuntimeIdentifiers"
".NET 10 tool packaging"
"cross-platform .NET tool with AOT"
What I Do
Configure your .csproj with ToolPackageRuntimeIdentifiers and PublishAot=true
Generate the pointer package (metapackage)
Build Native AOT packages for each target RID
Create CoreCLR fallback with -r any
Validate package structure
Quick Start
Step 1: Configure .csproj
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net10.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>

    <!-- Package as .NET Tool -->
    <PackAsTool>true</PackAsTool>
    <ToolCommandName>your-tool-name</ToolCommandName>

    <!-- RIDs: CoreCLR fallback + Native AOT targets -->
    <ToolPackageRuntimeIdentifiers>any;osx-arm64;linux-arm64;linux-x64</ToolPackageRuntimeIdentifiers>

    <!-- Enable Native AOT -->
    <PublishAot>true</PublishAot>
  </PropertyGroup>

  <!-- Native AOT optimizations -->
  <PropertyGroup Condition="'$(PublishAot)' == 'true'">
    <InvariantGlobalization>true</InvariantGlobalization>
    <OptimizationPreference>Size</OptimizationPreference>
    <StripSymbols>true</StripSymbols>
  </PropertyGroup>
</Project>

Step 2: Build Packages
# 1. Create pointer package (no binaries, just metadata)
dotnet pack -o ./packages

# 2. Build Native AOT for each target platform
dotnet pack -r osx-arm64 -o ./packages      # On macOS
dotnet pack -r linux-arm64 -o ./packages    # On Linux ARM or container
dotnet pack -r linux-x64 -o ./packages      # On Linux x64 or container

# 3. Create CoreCLR fallback for all other platforms
dotnet pack -r any -p:PublishAot=false -o ./packages

Step 3: Install & Run
dotnet tool install -g your-tool-name
your-tool-name  # Auto-selects best package for platform

Key Concepts
Concept	Description
Pointer Package	Metapackage that references RID-specific packages
ToolPackageRuntimeIdentifiers	Lists RIDs, creates pointer structure (no auto-build)
-r any	CoreCLR fallback for unlisted platforms
-p:PublishAot=false	Disables AOT for CoreCLR fallback
Why This Pattern Works
PublishAot=true disables automatic RID package generation (AOT can't cross-compile OSes)
ToolPackageRuntimeIdentifiers creates the pointer package structure
Manual -r <RID> builds produce AOT binaries per platform
-r any -p:PublishAot=false creates portable CoreCLR fallback
Documentation
reference.md: Complete build script, container builds, CI/CD patterns
examples.md: Real-world examples and troubleshooting
Requirements
.NET 10 SDK installed
Docker (for cross-platform Linux builds from macOS/Windows)
AOT-compatible container: mcr.microsoft.com/dotnet/sdk:10.0-noble-aot
Weekly Installs
98
Repository
rysweet/amplihack
GitHub Stars
55
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn