---
title: avalonia-mvvm
url: https://skills.sh/abdssamie/quater/avalonia-mvvm
---

# avalonia-mvvm

skills/abdssamie/quater/avalonia-mvvm
avalonia-mvvm
Installation
$ npx skills add https://github.com/abdssamie/quater --skill avalonia-mvvm
SKILL.md
MVVM Patterns in Avalonia

Complete guide to MVVM patterns using CommunityToolkit.Mvvm in Avalonia applications.

What I do
Guide implementation of ViewModels with ObservableObject base class
Show how to create observable properties with [ObservableProperty] attribute
Demonstrate command patterns with [RelayCommand] including async and CanExecute
Explain View-ViewModel mapping using DataTemplates (critical for navigation)
Show dependency injection patterns for passing services to ViewModels
When to use me

Use this skill when you need to:

Create new ViewModels for Avalonia views
Implement observable properties that notify the UI of changes
Add commands to handle user interactions (button clicks, etc.)
Set up navigation patterns with SukiSideMenu or ContentControl
Pass services (like ISukiToastManager) between ViewModels
Implement validation on ViewModel properties
ViewModel Base Classes
Basic ViewModel
using CommunityToolkit.Mvvm.ComponentModel;

namespace YourApp.ViewModels;

public partial class ViewModelBase : ObservableObject
{
}

Page ViewModel Base
using CommunityToolkit.Mvvm.ComponentModel;

namespace YourApp.ViewModels;

public abstract partial class PageViewModelBase : ViewModelBase
{
    public abstract string DisplayName { get; }
    public abstract string Icon { get; }
}

Observable Properties
Basic Observable Property
[ObservableProperty]
private string _name = "";

With Validation
using System.ComponentModel.DataAnnotations;

[ObservableProperty]
[Required(ErrorMessage = "Name is required")]
[MinLength(3, ErrorMessage = "Name must be at least 3 characters")]
private string _name = "";

With Property Changed Notification
[ObservableProperty]
private string _firstName = "";

[ObservableProperty]
private string _lastName = "";

public string FullName => $"{FirstName} {LastName}";

partial void OnFirstNameChanged(string value)
{
    OnPropertyChanged(nameof(FullName));
}

partial void OnLastNameChanged(string value)
{
    OnPropertyChanged(nameof(FullName));
}

Commands
Basic Command
[RelayCommand]
private void Save()
{
    // Save logic
}

Command with Parameter
[RelayCommand]
private void ButtonClick(string buttonName)
{
    LastButtonClicked = buttonName;
}


View:

<Button Content="Save" 
        Command="{Binding ButtonClickCommand}" 
        CommandParameter="Save Button" />

Async Command
[RelayCommand]
private async Task LoadDataAsync()
{
    IsLoading = true;
    await Task.Delay(1000);
    IsLoading = false;
}

Command with CanExecute
[ObservableProperty]
private bool _isDataLoaded;

[RelayCommand(CanExecute = nameof(CanSave))]
private void Save()
{
    // Save logic
}

private bool CanSave() => IsDataLoaded;

partial void OnIsDataLoadedChanged(bool value)
{
    SaveCommand.NotifyCanExecuteChanged();
}

Critical Pattern: DataTemplates

When using navigation patterns where ViewModels are displayed in a ContentControl (like SukiSideMenu), you MUST define DataTemplates to map ViewModels to their corresponding Views.

In SukiWindow:

<suki:SukiWindow.DataTemplates>
    <DataTemplate DataType="vm:HomePageViewModel">
        <views:HomePage />
    </DataTemplate>
    <DataTemplate DataType="vm:SettingsPageViewModel">
        <views:SettingsPage />
    </DataTemplate>
</suki:SukiWindow.DataTemplates>

Dependency Injection
Passing Services to ViewModels

Parent ViewModel:

public partial class MainWindowViewModel : ViewModelBase
{
    private readonly ISukiToastManager _toastManager;

    public MainWindowViewModel()
    {
        _toastManager = new SukiToastManager();
        Pages = new ObservableCollection<PageViewModelBase>
        {
            new NotificationsPageViewModeler)
        };
    }
}


Child ViewModel:

public partial class NotificationsPageViewModel : PageViewModelBase
{
    private readonly ISukiToastManager _toastManager;

    public NotificationsPageViewModel(ISukiToastManager toastManager)
    {
        _toastManager = toastManager;
    }
}

Common Mistakes to Avoid
Forgetting DataTemplates - Navigation won't work without ViewModel-to-View mapping
Not using partial class - CommunityToolkit.Mvvm requires partial keyword
Missing OnPropertyChanged - Computed properties won't update without manual notification
Not calling NotifyCanEuteChanged - Commands with CanExecute won't re-evaluate automatically
Using wrong field naming - Observable property fields must start with underscore and be private
Best Practices
Always use partial keyword on ViewModels
Use [ObservableProperty] instead of manual INotifyPropertyChanged
Use [RelayCommand] instead of manual ICommand implementation
Define DataTemplates in the root window for navigation scenarios
Pass services through constructor injection
Use computed properties for derived values
Implement validation attributes on properties need validation
Weekly Installs
39
Repository
abdssamie/quater
GitHub Stars
2
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass