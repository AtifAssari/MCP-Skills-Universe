---
rating: ⭐⭐
title: powershell-ui-architect
url: https://skills.sh/404kidwiz/claude-supercode-skills/powershell-ui-architect
---

# powershell-ui-architect

skills/404kidwiz/claude-supercode-skills/powershell-ui-architect
powershell-ui-architect
Installation
$ npx skills add https://github.com/404kidwiz/claude-supercode-skills --skill powershell-ui-architect
SKILL.md
PowerShell UI Architect
Purpose

Provides expertise in building graphical user interfaces (GUI) and terminal user interfaces (TUI) with PowerShell. Specializes in WinForms, WPF, and console-based TUI frameworks for creating user-friendly PowerShell tools.

When to Use
Building PowerShell tools with GUI
Creating WinForms applications
Developing WPF interfaces for scripts
Building terminal user interfaces (TUI)
Adding dialogs to automation scripts
Creating interactive admin tools
Building configuration wizards
Implementing progress displays
Quick Start

Invoke this skill when:

Creating GUIs for PowerShell scripts
Building WinForms or WPF interfaces
Developing terminal-based UIs
Adding interactive dialogs to tools
Creating admin tool interfaces

Do NOT invoke when:

Cross-platform CLI tools → use /cli-developer
PowerShell module design → use /powershell-module-architect
Web interfaces → use /frontend-design
Windows app development (non-PS) → use /windows-app-developer
Decision Framework
UI Type Needed?
├── Simple Dialog
│   └── WinForms MessageBox / InputBox
├── Full Windows App
│   ├── Simple layout → WinForms
│   └── Rich UI → WPF with XAML
├── Console/Terminal
│   ├── Simple menu → Write-Host + Read-Host
│   └── Rich TUI → Terminal.Gui / PSReadLine
└── Cross-Platform
    └── Terminal-based only

Core Workflows
1. WinForms Application
Add System.Windows.Forms assembly
Create Form object
Add controls (buttons, text boxes)
Wire up event handlers
Configure layout
Show form with ShowDialog()
2. WPF Interface
Define XAML layout
Load XAML in PowerShell
Get control references
Add event handlers
Implement logic
Display window
3. TUI with Terminal.Gui
Install Terminal.Gui module
Initialize application
Create window and views
Add controls (buttons, lists, text)
Handle events
Run main loop
Best Practices
Keep UI code separate from logic
Use XAML for complex WPF layouts
Handle errors gracefully with user feedback
Provide progress indication for long operations
Test on target Windows versions
Use appropriate UI for audience (GUI vs TUI)
Anti-Patterns
Anti-Pattern	Problem	Correct Approach
UI logic mixed with business logic	Hard to maintain	Separate concerns
Blocking UI thread	Frozen interface	Use runspaces/jobs
No input validation	Crashes, bad data	Validate before use
Hardcoded sizes	Scaling issues	Use anchoring/docking
No error messages	Confused users	Friendly error dialogs
Weekly Installs
109
Repository
404kidwiz/claud…e-skills
GitHub Stars
76
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass