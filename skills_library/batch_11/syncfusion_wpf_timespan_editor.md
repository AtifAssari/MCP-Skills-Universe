---
title: syncfusion-wpf-timespan-editor
url: https://skills.sh/syncfusion/wpf-ui-components-skills/syncfusion-wpf-timespan-editor
---

# syncfusion-wpf-timespan-editor

skills/syncfusion/wpf-ui-components-skills/syncfusion-wpf-timespan-editor
syncfusion-wpf-timespan-editor
Installation
$ npx skills add https://github.com/syncfusion/wpf-ui-components-skills --skill syncfusion-wpf-timespan-editor
SKILL.md
Implementing Syncfusion WPF TimeSpanEdit

The TimeSpanEdit control allows users to set or display time as Days:Hours:Minutes:Seconds (d.h:m:s) format with support for keyboard and mouse interactions, custom formatting, and theming.

When to Use This Skill

Use the TimeSpanEdit control when you need to:

Capture or display time durations/intervals in your WPF application
Provide Days:Hours:Minutes:Seconds input with a user-friendly interface
Enable users to increment/decrement time values using keyboard, mouse wheel, or buttons
Display time with custom formats and labels (e.g., "5 days, 3 hours, 15 minutes, 30 sec")
Apply min/max constraints to limit allowed time ranges
Support null values with watermark text for empty states
Style the control with colors, themes, and RTL support
Component Overview

Key Capabilities:

✓ Display time as Days:Hours:Minutes:Seconds (with milliseconds support)
✓ Programmatic and user-based value changes
✓ Keyboard navigation between fields (arrow keys)
✓ Mouse wheel and click-drag interactions
✓ Custom format strings with field labels
✓ Min/Max value constraints
✓ ValueChanged event notifications
✓ ReadOnly mode for display-only scenarios
✓ Null value support with watermarks
✓ Theme integration (SfSkinManager, ThemeStudio)
✓ RTL (Right-to-Left) flow direction support
Documentation Guide
Topic	File	Focus
Setup	getting-started.md	Install NuGet, add via Designer/XAML/C#
Formats	value-and-formats.md	Custom format strings, labels, milliseconds
Interactions	user-interactions.md	Keyboard, mouse, buttons, drag, arrow keys
Constraints & Events	constraints-and-events.md	Min/Max, ValueChanged event, validation
Appearance	appearance-and-theming.md	Colors, themes, RTL, SfSkinManager
Quick Start Example

XAML:

<Window xmlns:syncfusion="http://schemas.syncfusion.com/wpf">
    <Grid>
        <!-- Basic TimeSpanEdit -->
        <syncfusion:TimeSpanEdit 
            x:Name="timeSpanEdit"
            Value="5.12:30:45"
            Width="150"
            Height="30" />
    </Grid>
</Window>


C# Code-Behind:

using Syncfusion.Windows.Shared;

public partial class MainWindow : Window {
    public MainWindow() {
        InitializeComponent();
        
        // Create and configure TimeSpanEdit
        TimeSpanEdit editor = new TimeSpanEdit();
        editor.Value = new TimeSpan(5, 12, 30, 45);
        editor.Width = 150;
        editor.Height = 30;
        
        this.Content = editor;
    }
}


Assembly Reference: Add this to your WPF project:

Syncfusion.Shared.WPF
Common Patterns
Use Case	XAML Setup
With Constraints	MinValue="2.00:00:00" MaxValue="10.00:00:00"
Custom Format	Format="d 'days' h 'hours' m 'minutes' s 'seconds'"
Precise Intervals	StepInterval="1.00:15:30" IncrementOnScrolling="True"
Read-Only	IsReadOnly="True" ShowArrowButtons="False"
Nullable	AllowNull="True" NullString="Enter duration..."

Quick Example:

<!-- Constrained input with custom format -->
<syncfusion:TimeSpanEdit 
    Value="5.08:30:00"
    MinValue="2.00:00:00"
    MaxValue="10.00:00:00"
    Format="d 'days' h 'hours'" />

Key Props Reference
Property	Type	Default	Purpose
Value	TimeSpan?	0.0:0:0	The time duration to display/edit
Format	string	d.h:m:s	Custom format string (d=days, h=hours, m=minutes, s=seconds, z=milliseconds)
MinValue	TimeSpan	—	Minimum allowed time duration
MaxValue	TimeSpan	—	Maximum allowed time duration
StepInterval	TimeSpan	1.01:01:01	Increment/decrement interval for buttons/wheel/keyboard
AllowNull	bool	false	Allow null/empty values
NullString	string	""	Watermark text when value is null
ShowArrowButtons	bool	true	Show up/down spinner buttons
IncrementOnScrolling	bool	true	Allow mouse wheel to change values
EnableExtendedScrolling	bool	false	Allow click & drag to change values
IsReadOnly	bool	false	Prevent user edits (read-only mode)
Background	Brush	White	Control background color
Foreground	Brush	Black	Text color
SelectionBrush	Brush	RoyalBlue	Selection highlight color
FlowDirection	FlowDirection	LeftToRight	RTL support (RightToLeft)
Common Use Cases
Scenario	Key Settings
Duration Input	Enable buttons, wheel, keyboard; set Min/Max; use labels
Display Only	IsReadOnly="True" ShowArrowButtons="False"; use clear format
Precise Control	Set StepInterval (e.g., 15-min); field-by-field keyboard entry
Flexible Entry	All interactions enabled; logical step intervals; visual feedback
Next Steps
Start with Getting Started: Read getting-started.md to set up the control
Format Your Display: Check value-and-formats.md for custom formats
Enable Interactions: Review user-interactions.md for optimal UX
Add Logic: Use constraints-and-events.md for events and limits
Style It: Apply colors and themes with appearance-and-theming.md
Weekly Installs
50
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