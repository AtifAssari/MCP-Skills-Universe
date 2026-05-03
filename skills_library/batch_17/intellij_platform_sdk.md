---
title: intellij-platform-sdk
url: https://skills.sh/gadfly3173/intellij-platform-sdk-skills/intellij-platform-sdk
---

# intellij-platform-sdk

skills/gadfly3173/intellij-platform-sdk-skills/intellij-platform-sdk
intellij-platform-sdk
Installation
$ npx skills add https://github.com/gadfly3173/intellij-platform-sdk-skills --skill intellij-platform-sdk
SKILL.md
IntelliJ Platform SDK Skill

Use this skill for IntelliJ Platform plugin development based on the modern v2 SDK.

This skill is intentionally split into focused references so the main file stays small and the model can load only the material relevant to the task.

What this skill helps with
creating or updating IntelliJ Platform plugins
configuring build.gradle.kts, settings.gradle.kts, and plugin.xml
implementing actions, services, tool windows, settings, and notifications
working with PSI, references, indexing, VFS, and dumb mode
building custom language support
implementing inspections, intentions, quick fixes, completion, formatting, and documentation
implementing run configurations, program runners, and execution consoles
providing live templates, file templates, and postfix completion
creating or extending IDE themes and color schemes
integrating Language Servers (LSP) in plugin-development context
contributing MCP tools and toolsets
testing plugins and preparing Marketplace publication
handling version compatibility and Gradle plugin migration
How to use this skill

First, identify the user’s real task. Then read only the relevant reference files.

Read references/getting-started.md when the task is about
creating a new IntelliJ Platform plugin project
setting up IntelliJ Platform Gradle Plugin 2.x for a plugin project
choosing target IDEs or bundled plugins for plugin development
adding optional plugin/module dependencies in plugin.xml
writing or fixing plugin-project plugin.xml metadata
Read references/platform-basics.md when the task is about
AnAction, action groups, menus, toolbars
services (@Service, project/application/module services)
logging (Logger, logger<T>(), thisLogger())
background tasks (Task.Backgroundable, ProgressManager, ProgressIndicator)
Virtual File System (VirtualFile, VFS listeners)
threading, read/write actions, dumb mode, modality
Kotlin coroutine patterns in plugins (readAction, writeAction, CoroutineScope)
dynamic plugin loading/unloading
disposable lifecycle management
messaging infrastructure (MessageBus, Topic)
general plugin architecture decisions
Read references/psi-and-indexing.md when the task is about
PSI traversal or modification
references, resolve, rename, find usages, safe delete
code generation using PSI factories
file-based indexes, stub indexes, gists
file view providers (multi-language PSI trees in a single file)
IndexNotReadyException, dumb mode, PSI performance
PSI cookbook (Java-specific common operations)
caching with CachedValuesManager
Read references/language-support-and-analysis.md when the task is about
custom language plugins
lexer, parser, ParserDefinition
syntax highlighting, annotators, completion
inspections, intentions, quick fixes
rename refactoring, rename validation, safe delete
formatter, folding, structure view, documentation provider
parameter info, spell checking, navigation bar integration
inlay hints, code vision
language injection
Symbols API and declarations/references model
Poly Symbols and Web Types for web-framework metadata
DocumentationTarget API
OptPane, declarative inspection options, OptionController
element patterns (PlatformPatterns, PsiElementPattern) for completion/reference contributors
color scheme management, TextAttributesKey dependency chaining
Read references/ui-settings-and-toolwindows.md when the task is about
Kotlin UI DSL v2 (panel { row { } }, BoundConfigurable)
dialogs and IntelliJ UI components
tool windows
settings/configurables (including parentId/settings groups hierarchy)
persistent state
notifications
popups (JBPopup, ListPopup, chooser popups)
new project wizard, module type, project view integration
status bar widgets
editor notification banners
persisting sensitive data (PasswordSafe)
embedded editor components (EditorTextField)
internationalization (i18n) and localization
accessibility (keyboard navigation, screen readers)
plugin UX principles
Read references/testing-and-publishing.md when the task is about
test fixtures and plugin tests
integration tests or UI tests
Starter/Driver-based test setup
parser/completion/inspection tests
plugin verifier
verifyPluginProjectConfiguration / verifyPluginStructure
signing and publishing to Marketplace
Read references/compatibility.md when the task is about
build compatibility
sinceBuild / untilBuild
migrating from legacy Gradle plugin 1.x to 2.x
API changes across platform versions
Java/Kotlin version expectations
Workspace Model migration or newer platform API transitions
Read references/extension_points.md when the task is about
exact plugin.xml registration syntax
locating the right extension point
action group IDs and XML patterns
MCP extension points such as com.intellij.mcpServer.*
Read references/code_samples.md when the task is about
finding the closest official SDK sample
copying an official implementation pattern
understanding what each JetBrains sample demonstrates
Read references/lsp.md when the task is about
integrating a Language Server into an IntelliJ Platform plugin
LspServerSupportProvider, LspServerDescriptor, or LSP-specific plugin.xml dependencies
LSP setup for supported JetBrains IDE products and platform versions in plugin-development context
LSP feature support timeline inside the IntelliJ Platform
deciding between LSP integration and native IntelliJ language support for a plugin
Read references/mcp-and-ai-integration.md when the task is about
MCP-related plugin integration in an IntelliJ Platform plugin
contributing MCP tools or defining MCP toolsets
understanding MCP-related extension points such as com.intellij.mcpServer.*
MCP guidance in areas where the official SDK docs are still sparse
Read references/execution-and-run-configs.md when the task is about
implementing custom run configurations (ConfigurationType, RunConfigurationBase)
run configuration producers (auto-detecting configurations from context)
program runners and execution environments
execution consoles and console filters
run configuration macros
before/after launch tasks
Read references/templates.md when the task is about
providing live templates bundled in a plugin
custom live template macros/functions
file and code templates (Velocity-based)
postfix completion templates
surround-with descriptors
Read references/themes.md when the task is about
creating or extending IDE UI themes
theme JSON descriptor format
editor color scheme integration
icon customization in themes
Islands theme compatibility
deploying and publishing theme plugins
Read references/icons.md when the task is about
adding or organizing icons in a plugin
icon file naming conventions (dark variants, HiDPI)
icon holder classes (by-path vs by-class referencing)
New UI (expui) icon requirements and icon mappings
animated icons (AnimatedIcon, AsyncProcessIcon)
icon tooltips via resource bundles
Read references/patterns.md when the task is about
reusable implementation patterns
editor/document helpers (caret position, selection, scrolling)
editor coordinate system (offsets, logical/visual positions)
editor FAQ (get active editor, listen for events, custom tab title/color)
progress handling
dialog/tool-window patterns
PSI/editor/VFS utilities
icon loading and rendering patterns
Read references/troubleshooting.md when the task is about
you are not yet sure which troubleshooting bucket the issue belongs to
actions not appearing
threading assertions
service initialization failures
PSI write-action errors
verifier warnings
test setup failures
Read references/troubleshooting-build-runtime.md when the task is about
Gradle or repository resolution failures
plugin.xml wiring or class loading issues
action registration/runtime visibility issues
verifier/signing/release failures
Read references/troubleshooting-psi-ui-testing.md when the task is about
PSI validity or write-action assertions
IndexNotReadyException
editor/document synchronization
UI refresh or EDT access errors
fixture/test-data/debugging problems
Working principles

When solving IntelliJ Platform tasks:

Prefer official platform concepts over ad-hoc hacks.
Put reusable logic in services, not in actions.
Keep AnAction.update() extremely fast.
Respect threading and dumb mode before optimizing behavior.
Use PSI-aware approaches for structural code tasks.
Use platform UI components and conventions for user-facing surfaces.
Keep plugin dependencies and target IDE scope as small as practical.
High-value reminders
AnAction implementations should not store request-specific state in fields.
When targeting IntelliJ Platform 2022.3 or later, actions must implement getActionUpdateThread().
PSI modifications must run on EDT inside a write action and command; coordinate document changes with the PSI/document APIs used by the platform.
Not every feature is safe in dumb mode; do not mark things DumbAware casually.
For Kotlin plugins targeting 2024.1+ or newer platform baselines, prefer coroutine-based read/write APIs when appropriate.
Light services must be final; constructor injection of dependency services is unsupported, and services should not be looked up in constructors only to cache them in fields.
Avoid internal APIs unless there is no viable public alternative and the tradeoff is explicit.
Typical response strategy

When a user asks for implementation help:

Determine the feature surface: action, service, PSI, UI, language support, test, or publishing.
Read the matching reference files.
Follow the closest official sample or extension-point pattern.
Implement the smallest correct solution that matches IntelliJ Platform rules.
If publishing or compatibility matters, also review verifier/signing/build-range concerns.
Reference map
references/getting-started.md
references/platform-basics.md
references/psi-and-indexing.md
references/language-support-and-analysis.md
references/ui-settings-and-toolwindows.md
references/testing-and-publishing.md
references/compatibility.md
references/extension_points.md
references/code_samples.md
references/lsp.md
references/mcp-and-ai-integration.md
references/execution-and-run-configs.md
references/templates.md
references/themes.md
references/icons.md
references/patterns.md
references/troubleshooting.md
references/troubleshooting-build-runtime.md
references/troubleshooting-psi-ui-testing.md
Weekly Installs
24
Repository
gadfly3173/inte…k-skills
GitHub Stars
2
First Seen
Mar 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass