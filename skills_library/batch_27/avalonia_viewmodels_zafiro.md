---
title: avalonia-viewmodels-zafiro
url: https://skills.sh/sickn33/antigravity-awesome-skills/avalonia-viewmodels-zafiro
---

# avalonia-viewmodels-zafiro

skills/sickn33/antigravity-awesome-skills/avalonia-viewmodels-zafiro
avalonia-viewmodels-zafiro
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill avalonia-viewmodels-zafiro
SKILL.md
Avalonia ViewModels with Zafiro

This skill provides a set of best practices and patterns for creating ViewModels, Wizards, and managing navigation in Avalonia applications, leveraging the power of ReactiveUI and the Zafiro toolkit.

Core Principles
Functional-Reactive Approach: Use ReactiveUI (ReactiveObject, WhenAnyValue, etc.) to handle state and logic.
Enhanced Commands: Utilize IEnhancedCommand for better command management, including progress reporting and name/text attributes.
Wizard Pattern: Implement complex flows using SlimWizard and WizardBuilder for a declarative and maintainable approach.
Automatic Section Discovery: Use the [Section] attribute to register and discover UI sections automatically.
Clean Composition: map ViewModels to Views using DataTypeViewLocator and manage dependencies in the CompositionRoot.
Guides
ViewModels & Commands: Creating robust ViewModels and handling commands.
Wizards & Flows: Building multi-step wizards with SlimWizard.
Navigation & Sections: Managing navigation and section-based UIs.
Composition & Mapping: Best practices for View-ViewModel wiring and DI.
Example Reference

For real-world implementations, refer to the Angor project:

CreateProjectFlowV2.cs: Excellent example of complex Wizard building.
HomeViewModel.cs: Simple section ViewModel using functional-reactive commands.
When to Use

This skill is applicable to execute the workflow or actions described in the overview.

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
394
Repository
sickn33/antigra…e-skills
GitHub Stars
36.1K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass