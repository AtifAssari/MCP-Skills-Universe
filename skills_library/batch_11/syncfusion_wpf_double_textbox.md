---
title: syncfusion-wpf-double-textbox
url: https://skills.sh/syncfusion/wpf-ui-components-skills/syncfusion-wpf-double-textbox
---

# syncfusion-wpf-double-textbox

skills/syncfusion/wpf-ui-components-skills/syncfusion-wpf-double-textbox
syncfusion-wpf-double-textbox
Installation
$ npx skills add https://github.com/syncfusion/wpf-ui-components-skills --skill syncfusion-wpf-double-textbox
SKILL.md
Implementing DoubleTextBox

This skill collects guidance and examples for the Syncfusion WPF DoubleTextBox control. Use this skill to find usage patterns, configuration options, and common gotchas when building WPF apps that accept double values.

When to Use This Skill
When adding or configuring a WPF numeric input bound to doubles
When restricting values using MinValue / MaxValue
When formatting values for different cultures or customizing group/decimal separators
When enabling step/scroll intervals, spin buttons, or range adorner
When you need examples for XAML or C# usage patterns
Navigation Guide
Getting Started

📄 Read: references/getting-started.md

Installing and adding the control via XAML/C#; basic properties and value binding
Overview

📄 Read: references/overview.md

Short feature list and control summary
Appearance & Styling

📄 Read: references/appearance-and-styling.md

Foreground for positive/negative/zero, background, corner radius, selection brush
Validation & Restrictions

📄 Read: references/restriction-or-validation.md

Min/Max validation modes, decimal digit limits, read-only mode
Step Interval & Scrolling

📄 Read: references/step-interval.md

ScrollInterval, mouse wheel, click-and-drag, selection-on-focus
Culture & Number Formatting

📄 Read: references/culture-and-number-formats.md

Culture, NumberFormat, dedicated formatting properties
Range Adorner

📄 Read: references/range-adorner.md

Visual range indicator based on MinValue/MaxValue
Changing Value & Advanced Behavior

📄 Read: references/changing-double-value.md

Paste behavior, spin buttons, null value handling, watermarks
Quick Start (XAML)
<syncfusion:DoubleTextBox x:Name="doubleTextBox" Width="150" Height="25"
                          MinValue="0" MaxValue="100" Value="10"
                          ScrollInterval="1" />

Common Patterns
Bind Value to a ViewModel property and use UpdateSourceTrigger=PropertyChanged for immediate updates.
Use MinValidation/MaxValidation to choose between strict-on-keypress and permissive-on-lost-focus behaviors.
For globalization, set Culture or NumberFormat and prefer NumberFormat when exact control is required.
Weekly Installs
49
Repository
syncfusion/wpf-…s-skills
GitHub Stars
2
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass