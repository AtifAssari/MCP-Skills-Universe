---
title: syncfusion-wpf-radial-slider
url: https://skills.sh/syncfusion/wpf-ui-components-skills/syncfusion-wpf-radial-slider
---

# syncfusion-wpf-radial-slider

skills/syncfusion/wpf-ui-components-skills/syncfusion-wpf-radial-slider
syncfusion-wpf-radial-slider
Installation
$ npx skills add https://github.com/syncfusion/wpf-ui-components-skills --skill syncfusion-wpf-radial-slider
SKILL.md
Implementing SfRadialSlider (WPF)
When to Use This Skill

Use this skill when the user needs to:

Add a circular/radial numeric value selector to a WPF application
Configure value range (Minimum, Maximum), step intervals (SmallChange), or tick spacing (TickFrequency)
Customize the start/end angle and sweep direction of the circular track
Display the selected value inside the inner rim using Content or ContentTemplate
Customize tick marks, tick labels, pointer, or preview pointer with DataTemplates
Format tick label text dynamically via the DrawLabel event
Style the inner rim, outer rim, foreground, and background
Component Overview
SfRadialSlider
├── Outer rim      — circular track background (Background, OuterRimStroke)
├── Ticks          — tick marks on the track (TickRadiusFactor, TickTemplate)
├── Labels         — tick value labels (LabelRadiusFactor, LabelTemplate, DrawLabel)
├── Pointer        — selection indicator (PointerRadiusFactor, PointerStyle)
├── Preview pointer — hover indicator (PreviewPointerStyle)
└── Inner rim      — center circle content area (InnerRimRadiusFactor, InnerRimFill, Content)


Assemblies:

Syncfusion.SfRadialMenu.WPF
Syncfusion.SfShared.WPF

Namespace: Syncfusion.Windows.Controls.Navigation
XAML Schema: http://schemas.syncfusion.com/wpf

Documentation and Navigation Guide
Getting Started

📄 Read: references/getting-started.md

Assembly references and namespace
XAML and C# control creation
Selecting a value by drag or click
Programmatic Value assignment
ValueChanged event
Themes with SfSkinManager
Value and Range Configuration

📄 Read: references/value-and-range.md

Value / Minimum / Maximum
Displaying value in content area (Content + ContentTemplate)
SmallChange — step interval
TickFrequency — tick spacing
ShowMaximumValue — show max when not a multiple
StartAngle / EndAngle — arc extent
SweepDirection — clockwise or counterclockwise
Ticks, Labels, and Templates

📄 Read: references/ticks-and-templates.md

TickRadiusFactor / TickVisibility / TickTemplate
LabelRadiusFactor / LabelVisibility / LabelTemplate
InnerRimRadiusFactor / OuterRimRadiusFactor
PointerRadiusFactor / PointerStyle
PreviewPointerStyle
DrawLabel event — per-label text, color, font
Appearance and Styling

📄 Read: references/appearance.md

Foreground / Background
InnerRimFill / InnerRimStroke / InnerRimStrokeThickness
OuterRimStroke / OuterRimStrokeThickness
FlowDirection (RTL)
SfSkinManager themes
Quick Start
xmlns:syncfusion="http://schemas.syncfusion.com/wpf"

<syncfusion:SfRadialSlider Name="radialSlider"
                           Height="200" Width="200"/>

using Syncfusion.Windows.Controls.Navigation;

SfRadialSlider radialSlider = new SfRadialSlider();
radialSlider.Height = 200;
radialSlider.Width  = 200;
this.Content = radialSlider;


Display selected value inside the inner rim:

<syncfusion:SfRadialSlider Value="{Binding SelectedValue, Mode=TwoWay}"
                           Content="{Binding SelectedValue, Mode=TwoWay}"
                           Height="200" Width="200">
    <syncfusion:SfRadialSlider.DataContext>
        <local:ViewModel/>
    </syncfusion:SfRadialSlider.DataContext>
</syncfusion:SfRadialSlider>

Common Patterns
Scenario	Approach
Temperature selector 0–100	Minimum="0" Maximum="100"
Full circle vs arc	StartAngle="0" EndAngle="360" vs StartAngle="90" EndAngle="330"
Snap to multiples of 5	SmallChange="5"
Reduce tick count	TickFrequency="20"
Counterclockwise arc	SweepDirection="Counterclockwise"
Show max label	ShowMaximumValue="True"
Color-code labels by value	Handle DrawLabel event
Custom pointer style	PointerStyle with TargetType="syncfusion:RadialPointer"
Display formatted value in center	ContentTemplate with bound TextBlock
Key Properties
Property	Default	Description
Value	0	Currently selected value
Minimum	0	Minimum tick value
Maximum	100	Maximum tick value
SmallChange	0.1	Smallest selectable increment
TickFrequency	10	Spacing between displayed ticks
ShowMaximumValue	false	Show max when not a TickFrequency multiple
StartAngle	0	Start angle of the circular arc
EndAngle	360	End angle of the circular arc
SweepDirection	Clockwise	Tick direction
Content	null	Content shown inside inner rim
ContentTemplate	null	DataTemplate for inner rim content
InnerRimRadiusFactor	0.2	Inner circle radius (0–1)
OuterRimRadiusFactor	0.7	Outer rim radius (0–1)
TickRadiusFactor	0.72	Tick mark position radius
LabelRadiusFactor	0.87	Label position radius
PointerRadiusFactor	0.75	Pointer position radius
TickVisibility	Visible	Show/hide tick marks
LabelVisibility	Visible	Show/hide tick labels
Weekly Installs
47
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