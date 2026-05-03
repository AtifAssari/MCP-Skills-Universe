---
title: semantic-kernel
url: https://skills.sh/github/awesome-copilot/semantic-kernel
---

# semantic-kernel

skills/github/awesome-copilot/semantic-kernel
semantic-kernel
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill semantic-kernel
SKILL.md
Semantic Kernel

Use this skill when working with applications, plugins, function-calling flows, or AI integrations built on Semantic Kernel.

Always ground implementation advice in the latest Semantic Kernel documentation and samples rather than memory alone.

Determine the target language first

Choose the language workflow before making recommendations or code changes:

Use the .NET workflow when the repository contains .cs, .csproj, .sln, or other .NET project files, or when the user explicitly asks for C# or .NET guidance. Follow references/dotnet.md.
Use the Python workflow when the repository contains .py, pyproject.toml, requirements.txt, or the user explicitly asks for Python guidance. Follow references/python.md.
If the repository contains both ecosystems, match the language used by the files being edited or the user's stated target.
If the language is ambiguous, inspect the current workspace first and then choose the closest language-specific reference.
Always consult live documentation
Read the Semantic Kernel overview first: https://learn.microsoft.com/semantic-kernel/overview/
Prefer official docs and samples for the current API surface.
Use the Microsoft Docs MCP tooling when available to fetch up-to-date framework guidance and examples.
Shared guidance

When working with Semantic Kernel in any language:

Use async patterns for kernel operations.
Follow official plugin and function-calling patterns.
Implement explicit error handling and logging.
Prefer strong typing, clear abstractions, and maintainable composition patterns.
Use built-in connectors for Azure AI Foundry, Azure OpenAI, OpenAI, and other AI services, while preferring Azure AI Foundry services for new projects when that fits the task.
Use the kernel's memory and context-management capabilities when they simplify the solution.
Use DefaultAzureCredential when Azure authentication is appropriate.
Workflow
Determine the target language and read the matching reference file.
Fetch the latest official docs and samples before making implementation choices.
Apply the shared Semantic Kernel guidance from this skill.
Use the language-specific package, repository, sample paths, and coding practices from the chosen reference.
When examples in the repo differ from current docs, explain the difference and follow the current supported pattern.
References
.NET reference
Python reference
Completion criteria
Recommendations match the target language.
Package names, repository paths, and sample locations match the selected ecosystem.
Guidance reflects current Semantic Kernel documentation rather than stale assumptions.
Weekly Installs
1.3K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass