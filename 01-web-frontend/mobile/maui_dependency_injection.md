---
rating: ⭐⭐⭐
title: maui-dependency-injection
url: https://skills.sh/dotnet/skills/maui-dependency-injection
---

# maui-dependency-injection

skills/dotnet/skills/maui-dependency-injection
maui-dependency-injection
Installation
$ npx skills add https://github.com/dotnet/skills --skill maui-dependency-injection
SKILL.md
Dependency Injection in .NET MAUI

.NET MAUI uses the same Microsoft.Extensions.DependencyInjection container as ASP.NET Core. All service registration happens in MauiProgram.CreateMauiApp() on builder.Services. The container is built once at startup and is immutable thereafter.

When to Use
Registering services, ViewModels, and Pages in MauiProgram.cs
Choosing between AddSingleton, AddTransient, and AddScoped
Wiring constructor injection for Pages and ViewModels
Leveraging Shell navigation to auto-resolve DI-registered Pages
Registering platform-specific service implementations with #if directives
Designing interfaces for testable service layers
When Not to Use
XAML data-binding syntax or compiled bindings — use the maui-data-binding skill
Shell route registration and query parameters — use the maui-shell-navigation skill
Mocking frameworks or test runners — use standard .NET testing tools (xUnit, NUnit, MSTest) and mocking libraries (NSubstitute, Moq)
Inputs
A .NET MAUI project with a MauiProgram.cs file
Knowledge of which services, ViewModels, and Pages need registration
Target platforms (Android, iOS, Mac Catalyst, Windows) for conditional registrations
Workflow
Identify all services, ViewModels, and Pages that need to participate in dependency injection.
Choose the correct lifetime for each type — AddSingleton for shared services, AddTransient for Pages and ViewModels.
Register all types in MauiProgram.CreateMauiApp() on builder.Services, grouping by category (services, HTTP, ViewModels, Pages).
Register Pages as Shell routes in AppShell.xaml.cs so Shell navigation auto-resolves the full dependency graph.
Wire each Page to its ViewModel via constructor injection, assigning the ViewModel as BindingContext.
Add platform-specific registrations with #if directives, ensuring every target platform is covered or has a fallback.
Verify resolution works by running the app and confirming no null dependencies or missing-registration exceptions at runtime.
Lifetime Selection
Lifetime	When to Use	Typical Types
AddSingleton<T>()	Shared state, expensive to create, app-wide config	HttpClient factory, settings service, database connection
AddTransient<T>()	Lightweight, stateless, or needs a fresh instance per use	Pages, ViewModels, per-call API wrappers
AddScoped<T>()	Per-scope lifetime with manually created IServiceScope	Scoped unit-of-work (rare in MAUI)

Key rule: Register Pages and ViewModels as Transient. Register shared services as Singleton.

⚠️ Avoid AddScoped unless you manually manage IServiceScope. MAUI has no built-in request scope like ASP.NET Core. A Scoped registration without an explicit scope silently behaves as a Singleton, leading to subtle bugs.

Registration Pattern in MauiProgram.cs
public static MauiApp CreateMauiApp()
{
    var builder = MauiApp.CreateBuilder();
    builder.UseMauiApp<App>();

    // Services — Singleton for shared state
    builder.Services.AddSingleton<IDataService, DataService>();
    builder.Services.AddSingleton<ISettingsService, SettingsService>();

    // HTTP — use typed or named clients via IHttpClientFactory
    // Requires NuGet: Microsoft.Extensions.Http
    builder.Services.AddHttpClient<IApiClient, ApiClient>();

    // ViewModels — Transient for fresh state per navigation
    builder.Services.AddTransient<MainViewModel>();
    builder.Services.AddTransient<DetailViewModel>();

    // Pages — Transient so constructor injection fires each time
    builder.Services.AddTransient<MainPage>();
    builder.Services.AddTransient<DetailPage>();

    return builder.Build();
}

Constructor Injection

Inject dependencies through constructor parameters. The container resolves them automatically when the type is itself resolved from DI.

public class MainViewModel
{
    private readonly IDataService _dataService;

    public MainViewModel(IDataService dataService)
    {
        _dataService = dataService;
    }

    public async Task LoadAsync() => Items = await _dataService.GetItemsAsync();
}

ViewModel → Page Wiring

Register both Page and ViewModel. Inject the ViewModel into the Page and assign it as BindingContext:

public partial class MainPage : ContentPage
{
    public MainPage(MainViewModel viewModel)
    {
        InitializeComponent();
        BindingContext = viewModel;
    }
}

Shell Navigation Auto-Resolution

When a Page is registered in DI and as a Shell route, Shell resolves it (and its full dependency graph) automatically on navigation:

// MauiProgram.cs
builder.Services.AddTransient<DetailPage>();
builder.Services.AddTransient<DetailViewModel>();

// AppShell.xaml.cs
Routing.RegisterRoute(nameof(DetailPage), typeof(DetailPage));

// Navigate — DI resolves DetailPage + DetailViewModel
await Shell.Current.GoToAsync(nameof(DetailPage));

Platform-Specific Registration

Use preprocessor directives to register platform implementations. Always cover every target platform or provide a no-op fallback to avoid runtime null.

#if ANDROID
builder.Services.AddSingleton<INotificationService, AndroidNotificationService>();
#elif IOS || MACCATALYST
builder.Services.AddSingleton<INotificationService, AppleNotificationService>();
#elif WINDOWS
builder.Services.AddSingleton<INotificationService, WindowsNotificationService>();
#else
builder.Services.AddSingleton<INotificationService, NoOpNotificationService>();
#endif

Explicit Resolution (Last Resort)

Prefer constructor injection. Use explicit resolution only where injection is genuinely unavailable (custom handlers, platform callbacks):

// From any Element with a Handler
var service = this.Handler.MauiContext.Services.GetService<IDataService>();


For dynamic resolution, inject IServiceProvider:

public class NavigationService(IServiceProvider serviceProvider)
{
    public T ResolvePage<T>() where T : Page
        => serviceProvider.GetRequiredService<T>();
}

Interface-First Pattern for Testability

Define interfaces for every service so implementations can be swapped in tests:

public interface IDataService
{
    Task<List<Item>> GetItemsAsync();
}

// Production registration
builder.Services.AddSingleton<IDataService, DataService>();

// Test registration — swap without touching production code
var services = new ServiceCollection();
services.AddSingleton<IDataService, FakeDataService>();

Common Pitfalls
1. Singleton ViewModels Cause Stale Data
// ❌ ViewModel keeps stale state across navigations
builder.Services.AddSingleton<DetailViewModel>();

// ✅ Fresh instance each navigation
builder.Services.AddTransient<DetailViewModel>();

2. Unregistered Page Silently Skips Injection

If a Page appears in Shell XAML via <ShellContent ContentTemplate="..."> but is not registered in builder.Services, MAUI creates it with the parameterless constructor. Dependencies are silently null — no exception is thrown.

// ❌ Missing — injection silently skipped
// builder.Services.AddTransient<DetailPage>();

// ✅ Always register pages that need injection
builder.Services.AddTransient<DetailPage>();
builder.Services.AddTransient<DetailViewModel>();

3. XAML Resource Parsing vs. DI Timing

XAML resources in App.xaml are parsed during InitializeComponent() — before the container is fully available. Defer service-dependent work to CreateWindow():

public partial class App : Application
{
    private readonly IServiceProvider _services;

    public App(IServiceProvider services)
    {
        _services = services;
        InitializeComponent();
    }

    protected override Window CreateWindow(IActivationState? activationState)
    {
        // Safe — container is fully built
        // Requires: builder.Services.AddTransient<AppShell>() in MauiProgram.cs
        var appShell = _services.GetRequiredService<AppShell>();
        return new Window(appShell);
    }
}

4. Service Locator Anti-Pattern
// ❌ Hides dependencies, hard to test
var svc = this.Handler.MauiContext.Services.GetService<IDataService>();

// ✅ Constructor injection — explicit and testable
public class MyViewModel(IDataService dataService) { }

5. Missing Platform in Conditional Registration

Forgetting a platform in #if blocks means GetService<T>() returns null at runtime on that platform. Always include an #else fallback or cover every target.

6. AddScoped Without Manual Scope

AddScoped in MAUI without creating IServiceScope manually gives Singleton behavior silently. Use AddTransient or AddSingleton instead unless you explicitly manage scopes.

Checklist
 Every Page and ViewModel that needs injection is registered in MauiProgram.cs
 Pages and ViewModels use AddTransient; shared services use AddSingleton
 Constructor injection used everywhere possible; service locator only as last resort
 Interfaces defined for services that need test substitution
 Platform-specific #if registrations cover all target platforms or include a fallback
 Service-dependent work deferred to CreateWindow(), not run during XAML parse
 AddScoped only used alongside manually created IServiceScope
References
Dependency injection in .NET MAUI
.NET dependency injection fundamentals
Weekly Installs
135
Repository
dotnet/skills
GitHub Stars
1.5K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass