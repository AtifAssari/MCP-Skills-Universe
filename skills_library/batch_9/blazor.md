---
title: blazor
url: https://skills.sh/mindrally/skills/blazor
---

# blazor

skills/mindrally/skills/blazor
blazor
Installation
$ npx skills add https://github.com/mindrally/skills --skill blazor
SKILL.md
Blazor Development Guidelines

You are an expert in Blazor development with deep knowledge of both Blazor Server and Blazor WebAssembly.

Component Architecture
Component Design
Create small, focused components
Use component parameters for input
Use EventCallback for output/events
Implement IDisposable for cleanup
Use cascading parameters sparingly
Component Structure
@page "/users/{Id:int}"
@inject IUserService UserService

<h1>@User?.Name</h1>

@code {
    [Parameter]
    public int Id { get; set; }

    private User? User { get; set; }

    protected override async Task OnInitializedAsync()
    {
        User = await UserService.GetUserAsync(Id);
    }
}

Component Lifecycle
Lifecycle Methods
OnInitialized/OnInitializedAsync: Initial setup
OnParametersSet/OnParametersSetAsync: When parameters change
OnAfterRender/OnAfterRenderAsync: After DOM updates
Dispose: Cleanup resources
Best Practices
Use OnInitializedAsync for data loading
Check firstRender in OnAfterRenderAsync
Dispose subscriptions and timers
Avoid long-running synchronous code
Data Binding
One-Way Binding
<p>@message</p>
<input value="@inputValue" />

Two-Way Binding
<input @bind="inputValue" />
<input @bind="inputValue" @bind:event="oninput" />

Event Handling
<button @onclick="HandleClick">Click</button>
<button @onclick="() => HandleClickWithParam(id)">Click</button>
<button @onclick="HandleClickAsync">Async Click</button>

Render Optimization
Prevent Unnecessary Renders
Use @key for list items
Implement ShouldRender() when appropriate
Use StateHasChanged() judiciously
Avoid inline handlers in loops
Virtualization
<Virtualize Items="@items" Context="item">
    <ItemContent>
        <div>@item.Name</div>
    </ItemContent>
</Virtualize>

State Management
Component State
Use private fields for component state
Call StateHasChanged() when state changes externally
Use InvokeAsync for thread-safe updates
Cascading Parameters
<CascadingValue Value="@currentTheme">
    <ChildComponent />
</CascadingValue>

<!-- In child component -->
[CascadingParameter]
public Theme CurrentTheme { get; set; }

State Containers
Create injectable state services
Use events for state change notifications
Consider Fluxor for complex state management
Blazor Server vs WebAssembly
Blazor Server
State lives on server
Real-time connection via SignalR
Faster initial load
Requires stable connection
Better for internal apps
Blazor WebAssembly
Runs entirely in browser
Larger initial download
Works offline (PWA capable)
No server resources per user
Better for public apps
API Integration
HTTP Client
@inject HttpClient Http

private async Task LoadData()
{
    users = await Http.GetFromJsonAsync<List<User>>("api/users");
}

Error Handling
try
{
    users = await Http.GetFromJsonAsync<List<User>>("api/users");
}
catch (HttpRequestException ex)
{
    errorMessage = "Failed to load users";
}

Error Handling
Error Boundaries
<ErrorBoundary>
    <ChildContent>
        <RiskyComponent />
    </ChildContent>
    <ErrorContent Context="ex">
        <p>An error occurred: @ex.Message</p>
    </ErrorContent>
</ErrorBoundary>

Global Error Handling
Implement IErrorBoundary for custom handling
Log errors to server
Show user-friendly messages
Testing
bUnit Testing
[Fact]
public void ComponentRendersCorrectly()
{
    using var ctx = new TestContext();
    var cut = ctx.RenderComponent<Counter>();

    cut.Find("p").MarkupMatches("<p>Current count: 0</p>");
    cut.Find("button").Click();
    cut.Find("p").MarkupMatches("<p>Current count: 1</p>");
}

Authentication
Setup
Use AuthenticationStateProvider
Use AuthorizeView for conditional UI
Use [Authorize] attribute on pages
Implement custom auth state provider for JWT
AuthorizeView
<AuthorizeView>
    <Authorized>
        <p>Welcome, @context.User.Identity?.Name!</p>
    </Authorized>
    <NotAuthorized>
        <p>Please log in.</p>
    </NotAuthorized>
</AuthorizeView>

Performance Tips
Use @key for dynamic lists
Implement virtualization for large lists
Lazy load components with @if
Minimize JavaScript interop calls
Use streaming rendering in .NET 8+
Weekly Installs
281
Repository
mindrally/skills
GitHub Stars
88
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass