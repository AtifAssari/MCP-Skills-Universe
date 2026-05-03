---
rating: ⭐⭐⭐
title: umbraco-extension-template
url: https://skills.sh/umbraco/umbraco-cms-backoffice-skills/umbraco-extension-template
---

# umbraco-extension-template

skills/umbraco/umbraco-cms-backoffice-skills/umbraco-extension-template
umbraco-extension-template
Installation
$ npx skills add https://github.com/umbraco/umbraco-cms-backoffice-skills --skill umbraco-extension-template
SKILL.md
Umbraco Extension Template
What is it?

The Umbraco Extension Template is the official .NET template for creating backoffice extensions. It provides a pre-configured project structure with TypeScript/Vite tooling, proper folder structure, and all essential files needed for extension development. Every Umbraco backoffice extension should start with this template.

Documentation

Always fetch the latest docs before implementing:

Main docs: https://docs.umbraco.com/umbraco-cms/customizing/development-flow/umbraco-extension-template
Development Flow: https://docs.umbraco.com/umbraco-cms/customizing/development-flow
Foundation: https://docs.umbraco.com/umbraco-cms/customizing/foundation
Prerequisites
.NET SDK 9.0 or later
Node.js 22 or later
Workflow
Install template (one-time): dotnet new install Umbraco.Templates
Create extension: dotnet new umbraco-extension -n MyExtension
Install dependencies: cd MyExtension/Client && npm install
Start development: npm run watch
Build for production: npm run build
Commands
Install the Template
dotnet new install Umbraco.Templates

Create New Extension (Basic)
dotnet new umbraco-extension -n MyExtension

Create New Extension (With Examples)
dotnet new umbraco-extension -n MyExtension -ex


The -ex flag adds example code including:

Sample API controller
Swagger API registration
Example dashboard component
Generated API client
Project Structure
Basic Template
MyExtension/
├── MyExtension.csproj        # .NET project file
├── Constants.cs              # Extension constants
├── README.md                 # Setup instructions
└── Client/                   # TypeScript source
    ├── package.json
    ├── tsconfig.json
    ├── vite.config.ts
    └── src/
        └── ...               # Your extension code

With Examples (-ex flag)
MyExtension/
├── MyExtension.csproj
├── Constants.cs
├── README.md
├── Composers/                # C# composers
│   └── SwaggerComposer.cs    # API documentation setup
├── Controllers/              # C# API controllers
│   └── MyExtensionController.cs
└── Client/
    ├── package.json
    ├── tsconfig.json
    ├── vite.config.ts
    └── src/
        ├── api/              # Generated API client
        ├── dashboards/       # Example dashboard
        └── entrypoints/      # Extension entry point

Development Commands
# Navigate to Client folder
cd MyExtension/Client

# Install dependencies
npm install

# Development with hot reload
npm run watch

# Production build
npm run build

# Type checking
npm run check

Build and Deploy
Publish the Extension
dotnet publish --configuration Release

Create NuGet Package
dotnet pack --configuration Release

Minimal Example

After running the template, add your first manifest in Client/src/:

manifest.ts
export const manifests: Array<UmbExtensionManifest> = [
  {
    name: "My Extension Entrypoint",
    alias: "MyExtension.Entrypoint",
    type: "backofficeEntryPoint",
    js: () => import("./entrypoint.js"),
  },
];

entrypoint.ts
import type { UmbEntryPointOnInit } from "@umbraco-cms/backoffice/extension-api";

export const onInit: UmbEntryPointOnInit = (_host, _extensionRegistry) => {
  console.log("Extension loaded!");
};

IMPORTANT: Add Extension to Umbraco Instance

After creating a new extension, you MUST add it as a project reference to the main Umbraco instance. Without this step, the extension will not load.

Reference skill: umbraco-add-extension-reference

This skill explains how to add the new extension's .csproj file as a <ProjectReference> in the main Umbraco project (e.g., Umbraco-CMS.Skills.csproj).

Related Skills

After creating your extension, use these skills to add functionality:

Sections: Reference skill: umbraco-sections
Dashboards: Reference skill: umbraco-dashboard
Menus: Reference skill: umbraco-menu
Workspaces: Reference skill: umbraco-workspace
Trees: Reference skill: umbraco-tree

For complete extension blueprints with working examples:

Reference skill: umbraco-backoffice

That's it! Always fetch fresh docs, use the template to scaffold, add the project reference, then add extension types as needed.

Weekly Installs
147
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