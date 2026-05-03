---
rating: ⭐⭐⭐
title: syncfusion-wpf-button
url: https://skills.sh/syncfusion/wpf-ui-components-skills/syncfusion-wpf-button
---

# syncfusion-wpf-button

skills/syncfusion/wpf-ui-components-skills/syncfusion-wpf-button
syncfusion-wpf-button
Installation
$ npx skills add https://github.com/syncfusion/wpf-ui-components-skills --skill syncfusion-wpf-button
SKILL.md
Implementing Syncfusion WPF Button (ButtonAdv)

The ButtonAdv is Syncfusion's enhanced WPF button control. It extends the standard WPF button with rich icon support (SmallIcon, LargeIcon, IconTemplate), predefined size modes, toggle/checkable behavior, multiline text, MVVM command binding, corner radius, and full theme support via SfSkinManager.

Assembly required: Syncfusion.Shared.WPF
Namespace: Syncfusion.Windows.Tools.Controls
XAML schema: http://schemas.syncfusion.com/wpf

When to Use This Skill
Adding a Syncfusion WPF button to an application (designer, XAML, or C#)
Configuring size modes (Small, Normal, Large) and icons
Setting up a toggle/checkable button
Binding commands using MVVM pattern
Customizing label, corner radius, icon size, or multiline text
Applying built-in themes or editing button templates
Handling Click, Checked, or Unchecked events
Navigation Guide
Getting Started

📄 Read: references/getting-started.md

Assembly / NuGet setup
Adding ButtonAdv via designer, XAML, or C#
Setting the Label property
CornerRadius customization
IsDefault and IsCancel modes
Icon priority loading order
Size Modes & Icons

📄 Read: references/size-modes-and-icons.md

SizeMode enum: Small, Normal, Large
SmallIcon vs LargeIcon usage rules
IconWidth / IconHeight sizing
IconTemplate (path data, font icons, DataTemplate)
IconTemplateSelector for dynamic icon switching
IsMultiLine for large-mode multiline labels
Toggle State

📄 Read: references/toggle-state.md

IsCheckable — enable toggle behavior
IsChecked — set initial checked state
Checked / Unchecked events
Click event handler
MVVM & Commands

📄 Read: references/mvvm-and-commands.md

Command property binding (ICommand)
CommandParameter for passing data
DelegateCommand implementation pattern
CanExecute and RaiseCanExecuteChanged
Full ViewModel example
Styling & Themes

📄 Read: references/styling-and-themes.md

Applying built-in themes via SfSkinManager
Creating custom themes with Theme Studio
Editing templates in Expression Blend
Editing templates in Visual Studio
Quick Start
Minimal XAML Setup
<Window xmlns:syncfusion="http://schemas.syncfusion.com/wpf" ...>
    <Grid>
        <syncfusion:ButtonAdv Label="Log in"
                              SizeMode="Normal"
                              SmallIcon="Images/user.png"
                              Width="120" Height="36"/>
    </Grid>
</Window>

Minimal C# Setup
using Syncfusion.Windows.Tools.Controls;

ButtonAdv button = new ButtonAdv();
button.Label = "Log in";
button.SizeMode = SizeMode.Normal;
button.SmallIcon = new BitmapImage(new Uri("Images/user.png", UriKind.RelativeOrAbsolute));
Root.Children.Add(button);

Common Patterns
Button with Large Icon
<syncfusion:ButtonAdv Label="Save"
                      SizeMode="Large"
                      LargeIcon="Images/save-large.png"
                      Width="68" Height="68"/>

Toggle Button
<syncfusion:ButtonAdv Label="Bold"
                      SizeMode="Normal"
                      SmallIcon="Images/bold.png"
                      IsCheckable="True"
                      IsChecked="False"
                      Checked="OnBoldChecked"
                      Unchecked="OnBoldUnchecked"/>

MVVM Command Binding
<syncfusion:ButtonAdv Label="Submit"
                      SizeMode="Normal"
                      Command="{Binding SubmitCommand}"
                      CommandParameter="SubmitAction"/>

Icon Template (Vector/Font Icon)
<syncfusion:ButtonAdv Label="User" SizeMode="Normal">
    <syncfusion:ButtonAdv.IconTemplate>
        <DataTemplate>
            <Grid Width="16" Height="16">
                <Path Data="M16,0 C19.6,0 22.5,2.9 22.5,6.5 ..."
                      Fill="#FF3A3A38" Stretch="Fill"/>
            </Grid>
        </DataTemplate>
    </syncfusion:ButtonAdv.IconTemplate>
</syncfusion:ButtonAdv>

Key Properties
Property	Type	Description
Label	string	Button text displayed to the user
SizeMode	SizeMode	Small (icon only), Normal (icon + label side), Large (icon + label below)
SmallIcon	ImageSource	Icon for Small/Normal size modes
LargeIcon	ImageSource	Icon for Large size mode
IconTemplate	DataTemplate	Vector/font icon template (highest priority)
IconTemplateSelector	DataTemplateSelector	Dynamic icon switching
IconWidth	double	Custom icon width
IconHeight	double	Custom icon height
CornerRadius	CornerRadius	Rounded corners (default: 3)
IsCheckable	bool	Enables toggle button behavior
IsChecked	bool	Initial toggle state
IsMultiLine	bool	Multiline label (Large mode only)
IsDefault	bool	Activated by Enter key
IsCancel	bool	Activated by Escape key
Command	ICommand	MVVM command binding
CommandParameter	object	Data passed to command handler

Icon priority order: IconTemplateSelector → IconTemplate → LargeIcon → SmallIcon

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