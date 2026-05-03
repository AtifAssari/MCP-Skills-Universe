---
rating: ⭐⭐
title: syncfusion-wpf-integer-textbox
url: https://skills.sh/syncfusion/wpf-ui-components-skills/syncfusion-wpf-integer-textbox
---

# syncfusion-wpf-integer-textbox

skills/syncfusion/wpf-ui-components-skills/syncfusion-wpf-integer-textbox
syncfusion-wpf-integer-textbox
Installation
$ npx skills add https://github.com/syncfusion/wpf-ui-components-skills --skill syncfusion-wpf-integer-textbox
SKILL.md
Implementing IntegerTextBox

Syncfusion WPF IntegerTextBox restricts input to integer (Int64) values with validation, formatting, and customization.

Assembly: Syncfusion.Shared.WPF Namespace: Syncfusion.Windows.Shared

Reference Files
File	Topics
getting-started.md	Installation, XAML/C# setup, MVVM binding
value-management.md	Value property, paste modes, spin buttons, null/watermark
validation-restrictions.md	Min/Max, validation modes, exceed behavior, read-only
formatting-culture.md	Culture, NumberFormat, group separator/sizes
appearance-customization.md	Colors, alignment, selection, corner radius
step-interval-scrolling.md	ScrollInterval, arrow keys, mouse wheel, drag, focus selection
range-adorner.md	EnableRangeAdorner, RangeAdornerBackground
Key Properties Reference
Property	Type	Default	Description
Value	long?	0	Current integer value of the control
MinValue	int	int.MinValue	Minimum allowed value
MaxValue	int	int.MaxValue	Maximum allowed value
ScrollInterval	int	1	Increment/decrement step value
ShowSpinButton	bool	false	Show up/down spinner buttons
EnableRangeAdorner	bool	false	Show progress bar-like visual
GroupSeperatorEnabled	bool	false	Enable number group separators
NumberGroupSeparator	string	Culture-based	Custom group separator character
Culture	CultureInfo	CurrentCulture	Culture for number formatting
UseNullOption	bool	false	Allow null values
NullValue	int?	null	Value to display when null
WatermarkText	string	string.Empty	Placeholder text when empty
PositiveForeground	Brush	Black	Foreground for positive values
NegativeForeground	Brush	Red	Foreground for negative values
ZeroColor	Brush	Green	Foreground for zero value
IsReadOnly	bool	false	Prevent user input
TextAlignment	TextAlignment	Left	Horizontal text alignment
CornerRadius	CornerRadius	1	Border corner rounding
Weekly Installs
51
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