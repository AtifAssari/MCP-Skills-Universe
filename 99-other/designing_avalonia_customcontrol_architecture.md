---
rating: ⭐⭐
title: designing-avalonia-customcontrol-architecture
url: https://skills.sh/christian289/dotnet-with-claudecode/designing-avalonia-customcontrol-architecture
---

# designing-avalonia-customcontrol-architecture

skills/christian289/dotnet-with-claudecode/designing-avalonia-customcontrol-architecture
designing-avalonia-customcontrol-architecture
Installation
$ npx skills add https://github.com/christian289/dotnet-with-claudecode --skill designing-avalonia-customcontrol-architecture
SKILL.md
6.5 Writing AXAML Code
When generating AXAML code, use CustomControl with ControlTheme for Stand-Alone Control Style
Purpose: Theme separation and minimizing style dependencies
6.5.1 AvaloniaUI Custom Control Library Project Structure

Recommended Project Structure:

YourAvaloniaSolution
├── YourCustomControlProject1/
│    ├── Properties/
│    │   ├── AssemblyInfo.cs            ← AssemblyInfo.cs definition
│    ├── Themes/
│    │   ├── Generic.axaml            ← ControlTheme definition
│    │   ├── CustomButton1.axaml       ← Individual control theme
│    │   └── CustomTextBox1.axaml      ← Individual control theme
│    ├── CustomButton1.cs
│    └── CustomTextBox1.cs
└── YourCustomControlProject2/
    ├── Properties/
    │   ├── AssemblyInfo.cs            ← AssemblyInfo.cs definition
    ├── Themes/
    │   ├── Generic.axaml            ← ControlTheme definition
    │   ├── CustomButton2.axaml       ← Individual control theme
    │   └── CustomTextBox2.axaml      ← Individual control theme
    ├── CustomButton2.cs
    └── CustomTextBox2.cs

6.6 ⚠️ Distinguishing ResourceInclude vs MergeResourceInclude
ResourceInclude: Used in regular ResourceDictionary files (Generic.axaml, Styles, etc.)
MergeResourceInclude: Used only in Application.Resources (App.axaml)

Advantages:

Complete separation of theme and logic based on ControlTheme
Flexible style variations through CSS Classes
State management via Pseudo Classes (:pointerover, :pressed, etc.)
Theme modularization through ResourceInclude
Work can be split by file for team collaboration
6.5.2 Key Differences Between WPF and AvaloniaUI
Item	WPF	AvaloniaUI
File Extension	.xaml	.axaml
Style Definition	Style + ControlTemplate	ControlTheme
State Management	Trigger, DataTrigger	Pseudo Classes, Style Selector
CSS Support	❌	✅ (Classes attribute)
Resource Merging	MergedDictionaries + ResourceDictionary	MergedDictionaries + ResourceInclude
Dependency Props	DependencyProperty	StyledProperty, DirectProperty
Weekly Installs
9
Repository
christian289/do…audecode
GitHub Stars
28
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass