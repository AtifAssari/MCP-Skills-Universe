---
title: umbraco-add-extension-reference
url: https://skills.sh/umbraco/umbraco-cms-backoffice-skills/umbraco-add-extension-reference
---

# umbraco-add-extension-reference

skills/umbraco/umbraco-cms-backoffice-skills/umbraco-add-extension-reference
umbraco-add-extension-reference
Installation
$ npx skills add https://github.com/umbraco/umbraco-cms-backoffice-skills --skill umbraco-add-extension-reference
SKILL.md
Add Extension Reference to Umbraco Instance
What is it?

After creating a new Umbraco backoffice extension project, it must be added as a project reference in the main Umbraco instance's .csproj file. Without this reference, the extension will not be loaded when running the Umbraco site.

If a solution file (.sln) exists, the extension should also be added to it for proper IDE support (Visual Studio, Rider). This is optional - the extension will work without being in the solution.

When to Use

Use this skill after:

Creating a new extension with dotnet new umbraco-extension
Moving or copying an extension project to your solution
Setting up a new extension from the umbraco-backoffice blueprints
Workflow
Step 1: Find the Main Umbraco Project

The main Umbraco instance .csproj file must be discovered dynamically. Search for it using these criteria:

# Find all .csproj files
Glob: **/*.csproj

# Then search for the one containing Umbraco.Cms package reference
Grep: Umbraco\.Cms" Version  (in *.csproj files)


The main Umbraco project will have:

A <PackageReference Include="Umbraco.Cms" ...> entry
SDK of Microsoft.NET.Sdk.Web
Usually located at the solution root or in a dedicated folder
Step 2: Read the Project File

Once found, read the .csproj file to understand its structure and find where <ProjectReference> entries are located.

Step 3: Calculate Relative Path

Calculate the relative path from the main project's directory to the new extension's .csproj file:

Use forward slashes / (cross-platform compatible)
Path is relative to the main .csproj file's directory

Example paths:

Extension Location	Example Relative Path
Sibling folder	../MyExtension/MyExtension.csproj
Subfolder	./extensions/MyExtension/MyExtension.csproj
Skills folder	../.claude/skills/.../MyExtension.csproj
Step 4: Add the ProjectReference

Add a <ProjectReference> entry in an <ItemGroup>:

<ItemGroup>
  <!-- Existing references -->
  <ProjectReference Include="../ExistingExtension/ExistingExtension.csproj" />
  <!-- Add new extension here -->
  <ProjectReference Include="../NewExtension/NewExtension.csproj" />
</ItemGroup>


If there's already an <ItemGroup> with <ProjectReference> entries, add to that one. Otherwise, create a new <ItemGroup>.

Step 5: Add Extension to Solution File (Optional)

If a solution file (.sln) exists, the extension project should be added to it for proper IDE support. This step is optional - not all projects use solution files.

Find the solution file:

# Find any .sln files in the workspace
Glob: **/*.sln


Scenarios to handle:

Scenario	Action
No .sln file found	Skip this step - it's not required
One .sln file found	Add the extension to it
Multiple .sln files found	Ask the user which solution to use
Extension already in solution	dotnet sln add will report this - safe to ignore

Add the extension project to the solution:

dotnet sln <path-to-solution.sln> add <path-to-extension.csproj>


Example:

# If solution is at ./MySite/MySite.sln and extension is at ./MyExtension/MyExtension.csproj
dotnet sln ./MySite/MySite.sln add ./MyExtension/MyExtension.csproj


When a solution file exists, adding the extension ensures:

The extension appears in Visual Studio/Rider solution explorer
Building the solution builds the extension
IDE features like "Go to Definition" work across projects
Example
Before
<Project Sdk="Microsoft.NET.Sdk.Web">
  <PropertyGroup>
    <TargetFramework>net9.0</TargetFramework>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Umbraco.Cms" Version="16.0.0" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="../BlankExtension/BlankExtension.csproj" />
  </ItemGroup>
</Project>

After Adding "MyNewExtension"
<Project Sdk="Microsoft.NET.Sdk.Web">
  <PropertyGroup>
    <TargetFramework>net9.0</TargetFramework>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Umbraco.Cms" Version="16.0.0" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="../BlankExtension/BlankExtension.csproj" />
    <ProjectReference Include="../MyNewExtension/MyNewExtension.csproj" />
  </ItemGroup>
</Project>

Implementation Checklist
 Discover the main Umbraco project using Glob + Grep for Umbraco.Cms
 Read the main project file to understand structure
 Calculate relative path from main project to new extension
 Verify the extension .csproj file exists at the calculated path
 Edit the main project file to add <ProjectReference>
 Check for a solution file (.sln) using Glob
 If found, add the extension to the solution using dotnet sln add
 Ask user to verify with dotnet build
Verification

After adding the reference, the user should verify by:

Building the solution: dotnet build
Running the Umbraco instance: dotnet run
Checking the backoffice loads the extension
Troubleshooting

Build error: Project not found

Check the relative path is correct
Verify the extension .csproj file exists
Ensure forward slashes are used in the path

Extension not loading

Verify the extension has been built: cd ExtensionName/Client && npm run build
Check the umbraco-package.json exists in the extension's wwwroot folder
Look for errors in the browser console

Multiple Umbraco projects found

If there are multiple .csproj files with Umbraco.Cms, ask the user which one is the main instance
The main instance is typically the one with Microsoft.NET.Sdk.Web SDK and a Program.cs or Startup.cs

No solution file found

This is fine - solution files are optional
The <ProjectReference> in the .csproj is sufficient for the extension to work
Skip the solution step and proceed with verification

Multiple solution files found

Ask the user which solution they want the extension added to
Common scenarios: separate solutions for different IDEs, test solutions, etc.

Extension already in solution

dotnet sln add will report the project is already added - this is safe to ignore
The command is idempotent and won't create duplicates
Weekly Installs
138
Repository
umbraco/umbraco…e-skills
GitHub Stars
23
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass