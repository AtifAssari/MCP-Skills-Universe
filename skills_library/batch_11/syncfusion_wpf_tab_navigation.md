---
title: syncfusion-wpf-tab-navigation
url: https://skills.sh/syncfusion/wpf-ui-components-skills/syncfusion-wpf-tab-navigation
---

# syncfusion-wpf-tab-navigation

skills/syncfusion/wpf-ui-components-skills/syncfusion-wpf-tab-navigation
syncfusion-wpf-tab-navigation
Installation
$ npx skills add https://github.com/syncfusion/wpf-ui-components-skills --skill syncfusion-wpf-tab-navigation
SKILL.md
Implementing TabNavigationControl (WPF)
When to Use This Skill

Use this skill when the user needs to:

Display pages or items with animated transition effects (slide, fade, zoom, blur, etc.)
Build an ad-rotator or banner-style content switcher in WPF
Create tab-based navigation with visual transition between content areas
Bind a collection of items to an animated tab navigator
Control visibility of the header strip, navigation buttons, or tab strip
Switch between pages programmatically with transition animations
Component Overview
TabNavigationControl                    (root container)
└── TabNavigationItem  (×N)            (each page/item)
    ├── Header                          — tab label text
    └── Content                         — page content (any UIElement)


Assemblies: Syncfusion.Tools.WPF + Syncfusion.Shared.WPF
Namespace: Syncfusion.Windows.Tools.Controls
XAML schema: http://schemas.syncfusion.com/wpf

Documentation and Navigation Guide
Getting Started

📄 Read: references/getting-started.md

Assembly references and NuGet package
XAML namespace (syncfusion schema)
Declarative control setup
Adding TabNavigationItem in XAML and C#
Themes with SfSkinManager
Data Binding

📄 Read: references/data-binding.md

Binding ObservableCollection via ItemsSource
Binding from XML data source
Model + ViewModel + MainWindow wiring
XAML ItemsSource binding pattern
Transition Effects

📄 Read: references/transition-effects.md

All 7 TransitionEffect values: Slide, Fade, Zoom, Blur, Push, PushIn, Wipe
XAML example per effect
When to choose each effect
Decision guide
Appearance

📄 Read: references/appearance.md

HeaderVisibility — show/hide the header tab strip
NavigationButtonVisibility — show/hide prev/next arrows
TabStripVisibility — show/hide the tab strip panel
XAML and C# examples
Quick Start
xmlns:syncfusion="http://schemas.syncfusion.com/wpf"

<syncfusion:TabNavigationControl x:Name="tabNavigation"
                                  TransitionEffect="Slide"
                                  Width="400" Height="300">
    <syncfusion:TabNavigationItem Header="Page 1">
        <syncfusion:TabNavigationItem.Content>
            <TextBlock Text="Welcome to Page 1" FontSize="18" HorizontalAlignment="Center"/>
        </syncfusion:TabNavigationItem.Content>
    </syncfusion:TabNavigationItem>
    <syncfusion:TabNavigationItem Header="Page 2">
        <syncfusion:TabNavigationItem.Content>
            <TextBlock Text="Welcome to Page 2" FontSize="18" HorizontalAlignment="Center"/>
        </syncfusion:TabNavigationItem.Content>
    </syncfusion:TabNavigationItem>
    <syncfusion:TabNavigationItem Header="Page 3">
        <syncfusion:TabNavigationItem.Content>
            <TextBlock Text="Welcome to Page 3" FontSize="18" HorizontalAlignment="Center"/>
        </syncfusion:TabNavigationItem.Content>
    </syncfusion:TabNavigationItem>
</syncfusion:TabNavigationControl>

using Syncfusion.Windows.Tools.Controls;

TabNavigationControl tabNavigation = new TabNavigationControl();
tabNavigation.TransitionEffect = TransitionEffect.Slide;

TabNavigationItem item1 = new TabNavigationItem { Header = "Page 1", Content = "Content 1" };
TabNavigationItem item2 = new TabNavigationItem { Header = "Page 2", Content = "Content 2" };
tabNavigation.Items.Add(item1);
tabNavigation.Items.Add(item2);
this.Content = tabNavigation;

Common Patterns
Scenario	Approach
Static page set	Declarative TabNavigationItem in XAML
Dynamic data-driven tabs	ItemsSource + ObservableCollection<TabNavigationItem>
Smooth slide transition	TransitionEffect="Slide"
Fade between content	TransitionEffect="Fade"
Hide all chrome (full-screen content)	HeaderVisibility="Collapsed" + TabStripVisibility="Collapsed" + NavigationButtonVisibility="Collapsed"
Auto-rotating banner	Bind ItemsSource + control SelectedIndex via timer
Key Properties
Property	Type	Description
TransitionEffect	TransitionEffect enum	Animation when switching items
ItemsSource	IEnumerable	Data collection for data-bound population
HeaderVisibility	Visibility	Show/hide the header tab strip
NavigationButtonVisibility	Visibility	Show/hide prev/next arrow buttons
TabStripVisibility	Visibility	Show/hide the tab strip panel

TabNavigationItem properties:

Property	Description
Header	Tab label text
Content	Page content (string or UIElement)
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