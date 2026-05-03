---
title: fluentui-blazor
url: https://skills.sh/github/awesome-copilot/fluentui-blazor
---

# fluentui-blazor

skills/github/awesome-copilot/fluentui-blazor
fluentui-blazor
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill fluentui-blazor
Summary

Comprehensive guide for building Blazor apps with Microsoft Fluent UI components.

Covers setup (service registration, mandatory providers), component patterns (lists, dialogs, forms), and icons via a separate NuGet package with strongly-typed variants and sizes
Explains critical patterns: FluentSelect/FluentAutocomplete use Items, OptionText, and SelectedOption binding (not <option> children), and dialogs use IDialogService with content components, not visibility toggling
Provides service injection examples for toasts, dialogs, and message bars; clarifies ServiceLifetime rules (Scoped for Server/Interactive, Singleton for WebAssembly)
Warns against common mistakes: manual <script>/<link> tags, setting design tokens before render, and using FluentEditForm outside wizard contexts
SKILL.md
Fluent UI Blazor — Consumer Usage Guide

This skill teaches how to correctly use the Microsoft.FluentUI.AspNetCore.Components (version 4) NuGet package in Blazor applications.

Critical Rules
1. No manual <script> or <link> tags needed

The library auto-loads all CSS and JS via Blazor's static web assets and JS initializers. Never tell users to add <script> or <link> tags for the core library.

2. Providers are mandatory for service-based components

These provider components MUST be added to the root layout (e.g. MainLayout.razor) for their corresponding services to work. Without them, service calls fail silently (no error, no UI).

<FluentToastProvider />
<FluentDialogProvider />
<FluentMessageBarProvider />
<FluentTooltipProvider />
<FluentKeyCodeProvider />

3. Service registration in Program.cs
builder.Services.AddFluentUIComponents();

// Or with configuration:
builder.Services.AddFluentUIComponents(options =>
{
    options.UseTooltipServiceProvider = true;  // default: true
    options.ServiceLifetime = ServiceLifetime.Scoped; // default
});


ServiceLifetime rules:

ServiceLifetime.Scoped — for Blazor Server / Interactive (default)
ServiceLifetime.Singleton — for Blazor WebAssembly standalone
ServiceLifetime.Transient — throws NotSupportedException
4. Icons require a separate NuGet package
dotnet add package Microsoft.FluentUI.AspNetCore.Components.Icons


Usage with a @using alias:

@using Icons = Microsoft.FluentUI.AspNetCore.Components.Icons

<FluentIcon Value="@(Icons.Regular.Size24.Save)" />
<FluentIcon Value="@(Icons.Filled.Size20.Delete)" Color="@Color.Error" />


Pattern: Icons.[Variant].[Size].[Name]

Variants: Regular, Filled
Sizes: Size12, Size16, Size20, Size24, Size28, Size32, Size48

Custom image: Icon.FromImageUrl("/path/to/image.png")

Never use string-based icon names — icons are strongly-typed classes.

5. List component binding model

FluentSelect<TOption>, FluentCombobox<TOption>, FluentListbox<TOption>, and FluentAutocomplete<TOption> do NOT work like <InputSelect>. They use:

Items — the data source (IEnumerable<TOption>)
OptionText — Func<TOption, string?> to extract display text
OptionValue — Func<TOption, string?> to extract the value string
SelectedOption / SelectedOptionChanged — for single selection binding
SelectedOptions / SelectedOptionsChanged — for multi-selection binding
<FluentSelect Items="@countries"
              OptionText="@(c => c.Name)"
              OptionValue="@(c => c.Code)"
              @bind-SelectedOption="@selectedCountry"
              Label="Country" />


NOT like this (wrong pattern):

@* WRONG — do not use InputSelect pattern *@
<FluentSelect @bind-Value="@selectedValue">
    <option value="1">One</option>
</FluentSelect>

6. FluentAutocomplete specifics
Use ValueText (NOT Value — it's obsolete) for the search input text
OnOptionsSearch is the required callback to filter options
Default is Multiple="true"
<FluentAutocomplete TOption="Person"
                    OnOptionsSearch="@OnSearch"
                    OptionText="@(p => p.FullName)"
                    @bind-SelectedOptions="@selectedPeople"
                    Label="Search people" />

@code {
    private void OnSearch(OptionsSearchEventArgs<Person> args)
    {
        args.Items = allPeople.Where(p =>
            p.FullName.Contains(args.Text, StringComparison.OrdinalIgnoreCase));
    }
}

7. Dialog service pattern

Do NOT toggle visibility of <FluentDialog> tags. The service pattern is:

Create a content component implementing IDialogContentComponent<TData>:
public partial class EditPersonDialog : IDialogContentComponent<Person>
{
    [Parameter] public Person Content { get; set; } = default!;

    [CascadingParameter] public FluentDialog Dialog { get; set; } = default!;

    private async Task SaveAsync()
    {
        await Dialog.CloseAsync(Content);
    }

    private async Task CancelAsync()
    {
        await Dialog.CancelAsync();
    }
}

Show the dialog via IDialogService:
[Inject] private IDialogService DialogService { get; set; } = default!;

private async Task ShowEditDialog()
{
    var dialog = await DialogService.ShowDialogAsync<EditPersonDialog, Person>(
        person,
        new DialogParameters
        {
            Title = "Edit Person",
            PrimaryAction = "Save",
            SecondaryAction = "Cancel",
            Width = "500px",
            PreventDismissOnOverlayClick = true,
        });

    var result = await dialog.Result;
    if (!result.Cancelled)
    {
        var updatedPerson = result.Data as Person;
    }
}


For convenience dialogs:

await DialogService.ShowConfirmationAsync("Are you sure?", "Yes", "No");
await DialogService.ShowSuccessAsync("Done!");
await DialogService.ShowErrorAsync("Something went wrong.");

8. Toast notifications
[Inject] private IToastService ToastService { get; set; } = default!;

ToastService.ShowSuccess("Item saved successfully");
ToastService.ShowError("Failed to save");
ToastService.ShowWarning("Check your input");
ToastService.ShowInfo("New update available");


FluentToastProvider parameters: Position (default TopRight), Timeout (default 7000ms), MaxToastCount (default 4).

9. Design tokens and themes work only after render

Design tokens rely on JS interop. Never set them in OnInitialized — use OnAfterRenderAsync.

<FluentDesignTheme Mode="DesignThemeModes.System"
                   OfficeColor="OfficeColor.Teams"
                   StorageName="mytheme" />

10. FluentEditForm vs EditForm

FluentEditForm is only needed inside FluentWizard steps (per-step validation). For regular forms, use standard EditForm with Fluent form components:

<EditForm Model="@model" OnValidSubmit="HandleSubmit">
    <DataAnnotationsValidator />
    <FluentTextField @bind-Value="@model.Name" Label="Name" Required />
    <FluentSelect Items="@options"
                  OptionText="@(o => o.Label)"
                  @bind-SelectedOption="@model.Category"
                  Label="Category" />
    <FluentValidationSummary />
    <FluentButton Type="ButtonType.Submit" Appearance="Appearance.Accent">Save</FluentButton>
</EditForm>


Use FluentValidationMessage and FluentValidationSummary instead of standard Blazor validation components for Fluent styling.

Reference files

For detailed guidance on specific topics, see:

Setup and configuration
Layout and navigation
Data grid
Theming
Weekly Installs
8.5K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass