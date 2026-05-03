---
rating: ⭐⭐⭐
title: syncfusion-wpf-range-slider
url: https://skills.sh/syncfusion/wpf-ui-components-skills/syncfusion-wpf-range-slider
---

# syncfusion-wpf-range-slider

skills/syncfusion/wpf-ui-components-skills/syncfusion-wpf-range-slider
syncfusion-wpf-range-slider
Installation
$ npx skills add https://github.com/syncfusion/wpf-ui-components-skills --skill syncfusion-wpf-range-slider
SKILL.md
Implementing Syncfusion WPF Range Slider

The Syncfusion WPF Range Slider (SfRangeSlider) is a versatile control that allows users to select a value or range of values within a defined minimum and maximum limit. It supports dual thumb selection, tick marks, labels, tooltips, customization, touch/gesture support, and various orientation options.

When to Use This Skill

Use this skill when users need to:

Implement a range slider control in WPF applications
Allow users to select a value range with dual thumbs
Create sliders with tick marks and snapping behavior
Display value labels or custom labels on sliders
Show tooltips with formatted values
Customize slider appearance (thumbs, tracks, ticks)
Handle range selection with validation (ThumbInterval)
Support touch and gesture-based interactions
Implement vertical or reversed-direction sliders
Respond to range value changes with
Component Overview

The SfRangeSlider provides:

Single or Dual Thumb Selection - Select a single value or a range with two thumbs
Tick Marks - Major and minor ticks with snapping behavior
Custom Labels - Value labels and custom label support
Tooltips - Customizable tooltips showing current values
Orientation - Horizontal or vertical layout with direction reversal
Touch & Gestures - Full touch support and keyboard/mouse gestures
Customization - Complete styling control for all visual elements
Events - Range change notifications and label customization hooks
Documentation and Navigation Guide
Getting Started

📄 Read: references/getting-started.md

Package installation and setup
Basic range slider implementation
Setting minimum and maximum values
Initial range configuration
Theme and CSS integration
Range Selection Features

📄 Read: references/range-selection.md

RangeStart and RangeEnd properties
ShowRange property for dual thumb mode
AllowRangeDrag for dragging entire range
ThumbInterval for minimum thumb spacing
Single vs dual thumb selection modes
Range value data binding
Ticks and Snapping Behavior

📄 Read: references/ticks-and-snapping.md

TickFrequency and MinorTickFrequency
TickPlacement options (TopLeft, BottomRight, None)
SnapsTo behavior (Ticks, StepFrequency, None)
StepFrequency for incremental values
Tick visualization and customization
Snapping behavior examples
Labels and Value Display

📄 Read: references/labels.md

ShowValueLabels and ShowCustomLabels
LabelPlacement options
LabelOrientation (horizontal/vertical)
ValuePlacement for value positioning
CustomLabels collection
LabelLoaded event for dynamic customization
Label formatting examples
Tooltips and Value Display

📄 Read: references/tooltips.md

ThumbToolTipPlacement (TopLeft, BottomRight, None)
ThumbToolTipPrecision for decimal places
ToolTipFormat for value formatting
ToolTipDisplayMode (Always, OnFocus)
ToolTipStyle for custom appearance
Advanced tooltip customization
Intermediate Values

📄 Read: references/intermediate-values.md

IntermediateValue property
IntermediateRangeStart and IntermediateRangeEnd
Use cases for intermediate indicators
Visual representation examples
Customization and Styling

📄 Read: references/customization.md

ThumbStyle customization
ActiveTrackStyle and InactiveTrackStyle
Tick styling (stroke, length, thickness)
Minor tick customization
Complete visual styling examples
Theme integration
Orientation and Direction

📄 Read: references/orientation-and-direction.md

Orientation property (Horizontal, Vertical)
IsDirectionReversed property
Visual behavior differences
Layout considerations
RTL support
Gestures and Interaction

📄 Read: references/gestures-and-interaction.md

MoveToPoint for tap/click navigation
Touch support capabilities
Keyboard gestures (arrow keys, page up/down, home/end)
Mouse gestures
Accessibility features
Events and Event Handlers

📄 Read: references/events.md

RangeChanged event
RangeStartChanged event
RangeEndChanged event
LabelLoaded event
Event handler examples (XAML and C#)
Quick Start Example
Basic Range Slider
<Window x:Class="RangeSliderDemo.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:editors="clr-namespace:Syncfusion.Windows.Controls.Input;assembly=Syncfusion.SfInput.Wpf">
    
    <Grid>
        <!-- Basic Range Slider -->
        <editors:SfRangeSlider
            Width="400"
            Minimum="0"
            Maximum="100"
            RangeStart="20"
            RangeEnd="80"
            ShowRange="True"
            TickPlacement="BottomRight"
            TickFrequency="10"
            ShowValueLabels="True" />
    </Grid>
</Window>

using Syncfusion.Windows.Controls.Input;
using System.Windows;

namespace RangeSliderDemo
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();

            // Create range slider programmatically
            SfRangeSlider rangeSlider = new SfRangeSlider()
            {
                Width = 400,
                Minimum = 0,
                Maximum = 100,
                RangeStart = 20,
                RangeEnd = 80,
                ShowRange = true,
                TickPlacement = TickPlacement.BottomRight,
                TickFrequency = 10,
                ShowValueLabels = true
            };

            // Add to container
            this.Content = rangeSlider;
        }
    }
}

Common Patterns
Pattern 1: Price Range Filter
<!-- Price range selector with currency formatting -->
<editors:SfRangeSlider
    Width="350"
    Minimum="0"
    Maximum="1000"
    RangeStart="100"
    RangeEnd="500"
    ShowRange="True"
    TickFrequency="100"
    TickPlacement="BottomRight"
    ShowValueLabels="True"
    ToolTipFormat="C0"
    ThumbToolTipPlacement="TopLeft"
    SnapsTo="Ticks"
    RangeChanged="PriceRangeSlider_RangeChanged" />

Pattern 2: Volume Control with Fine Adjustment
<!-- Volume slider with minor ticks and snapping -->
<editors:SfRangeSlider
    Width="300"
    Minimum="0"
    Maximum="100"
    Value="50"
    TickFrequency="10"
    MinorTickFrequency="2"
    TickPlacement="BottomRight"
    SnapsTo="StepFrequency"
    StepFrequency="5"
    ShowValueLabels="True"
    ThumbToolTipPlacement="TopLeft"
    ToolTipFormat="N0" />

Pattern 3: Date Range Selector
<!-- Custom labels for date ranges -->
<editors:SfRangeSlider
    Width="450"
    Minimum="0"
    Maximum="11"
    RangeStart="2"
    RangeEnd="8"
    ShowRange="True"
    ShowCustomLabels="True"
    TickFrequency="1"
    TickPlacement="BottomRight"
    SnapsTo="Ticks">
    <editors:SfRangeSlider.CustomLabels>
        <editors:LabelItem Content="Jan" Position="0"/>
        <editors:LabelItem Content="Feb" Position="1"/>
        <editors:LabelItem Content="Mar" Position="2"/>
        <editors:LabelItem Content="Apr" Position="3"/>
        <editors:LabelItem Content="May" Position="4"/>
        <editors:LabelItem Content="Jun" Position="5"/>
        <editors:LabelItem Content="Jul" Position="6"/>
        <editors:LabelItem Content="Aug" Position="7"/>
        <editors:LabelItem Content="Sep" Position="8"/>
        <editors:LabelItem Content="Oct" Position="9"/>
        <editors:LabelItem Content="Nov" Position="10"/>
        <editors:LabelItem Content="Dec" Position="11"/>
    </editors:SfRangeSlider.CustomLabels>
</editors:SfRangeSlider>

Pattern 4: Vertical Temperature Slider
<!-- Vertical orientation with reversed direction -->
<editors:SfRangeSlider
    Height="300"
    Minimum="-10"
    Maximum="50"
    Value="22"
    Orientation="Vertical"
    TickFrequency="10"
    TickPlacement="TopLeft"
    ShowValueLabels="True"
    ThumbToolTipPlacement="TopLeft"
    ToolTipFormat="N0"
    IsDirectionReversed="False" />

Pattern 5: Styled Range Slider with Custom Colors
<Window.Resources>
    <!-- Custom thumb style -->
    <Style x:Key="CustomThumbStyle" TargetType="Thumb">
        <Setter Property="Width" Value="20"/>
        <Setter Property="Height" Value="20"/>
        <Setter Property="Template">
            <Setter.Value>
                <ControlTemplate TargetType="Thumb">
                    <Ellipse Fill="#FF4CAF50" 
                             Stroke="#FF2E7D32" 
                             StrokeThickness="2"/>
                </ControlTemplate>
            </Setter.Value>
        </Setter>
    </Style>
</Window.Resources>

<editors:SfRangeSlider
    Width="400"
    Minimum="0"
    Maximum="100"
    RangeStart="30"
    RangeEnd="70"
    ShowRange="True"
    ThumbStyle="{StaticResource CustomThumbStyle}"
    ActiveTickStroke="#FF4CAF50"
    TickStroke="#FFBDBDBD"
    TickPlacement="BottomRight"
    TickFrequency="10" />

Key Properties
Range and Values
Minimum - Minimum value of the slider (default: 0)
Maximum - Maximum value of the slider (default: 100)
RangeStart - Start value of the selected range
RangeEnd - End value of the selected range
ShowRange - Enable dual thumb mode for range selection
AllowRangeDrag - Allow dragging the entire selected range
ThumbInterval - Minimum spacing between thumbs
Ticks
TickFrequency - Interval between major ticks
MinorTickFrequency - Interval between minor ticks
TickPlacement - Position of ticks (TopLeft, BottomRight, None)
SnapsTo - Snap behavior (Ticks, StepFrequency, None)
StepFrequency - Increment value for snapping
Labels
ShowValueLabels - Display numeric value labels
ShowCustomLabels - Display custom labels
CustomLabels - Collection of custom label items
LabelPlacement - Position of labels
LabelOrientation - Orientation of label text
ValuePlacement - Position of value display
Tooltips
ThumbToolTipPlacement - Tooltip position (TopLeft, BottomRight, None)
ThumbToolTipPrecision - Decimal places in tooltip
ToolTipFormat - Format string for tooltip values
ToolTipDisplayMode - When to show tooltip (Always, OnFocus)
ToolTipStyle - Custom style for tooltips
Layout
Orientation - Horizontal or Vertical
IsDirectionReversed - Reverse the direction of values
Interaction
MoveToPoint - Move thumb to clicked/tapped position
Styling
ThumbStyle - Custom style for thumb controls
ActiveTrackStyle - Style for active track region
InactiveTrackStyle - Style for inactive track region
ActiveTickStroke - Color for active ticks
TickStroke - Color for ticks
Events
RangeChanged

Triggered when RangeStart or RangeEnd values change. Provides old and new values for both start and end.

RangeStartChanged

Triggered when RangeStart value changes. Provides old and new start values.

RangeEndChanged

Triggered when RangeEnd value changes. Provides old and new end values.

LabelLoaded

Triggered when slider labels are created. Allows dynamic label content customization.

Common Use Cases
Price Range Filters - E-commerce product filtering with min/max price selection
Date Range Selection - Calendar or timeline range selection with custom labels
Volume/Brightness Controls - Media players or system settings
Temperature Controls - HVAC or scientific applications with vertical sliders
Data Filtering - Analytics dashboards for data range selection
Age Range Filters - Demographics or user profile filtering
Zoom Level Controls - Map or image zoom with precise increments
Budget Allocation - Financial applications with range constraints
Time Range Selection - Scheduling or timeline applications
Measurement Ranges - Scientific or industrial applications
Best Practices
Set appropriate TickFrequency - Match tick intervals to your data granularity
Use SnapsTo for discrete values - Enable snapping for better UX with discrete data
Format tooltips appropriately - Use ToolTipFormat to match your data type (currency, percentage, etc.)
Consider ThumbInterval - Prevent invalid ranges by setting minimum thumb spacing
Use CustomLabels for non-numeric data - Better UX for categorical or date-based ranges
Handle RangeChanged events - Update dependent UI or validate range selections
Choose appropriate orientation - Vertical sliders work well for height, temperature, volume
Style consistently - Match thumb and track colors to your application theme
Provide visual feedback - Use ShowRange and tooltips to show current selection
Consider accessibility - Ensure keyboard navigation and screen reader support
Related Components
SfDateTimeRangeNavigator - For date/time range selection with charts
SfSlider - Single value slider (if dual thumb not needed)
NumericUpDown - For precise numeric input
DatePicker - For date selection without range
Installation
# Install via NuGet Package Manager
Install-Package Syncfusion.SfInput.WPF

# Or via .NET CLI
dotnet add package Syncfusion.SfInput.WPF


Add XML namespace in XAML:

xmlns:editors="clr-namespace:Syncfusion.Windows.Controls.Input;assembly=Syncfusion.SfInput.Wpf"

Additional Resources
Syncfusion WPF Range Slider Documentation
API Reference
License Information
Weekly Installs
46
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