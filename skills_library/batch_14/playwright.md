---
title: playwright
url: https://skills.sh/stuartf303/sorcha/playwright
---

# playwright

skills/stuartf303/sorcha/playwright
playwright
Installation
$ npx skills add https://github.com/stuartf303/sorcha --skill playwright
SKILL.md
Playwright Skill

E2E testing for Blazor WebAssembly using Playwright .NET with NUnit and .NET Aspire integration. Tests run against the full Aspire application stack with all services.

Quick Start
Basic Page Test
[Parallelizable(ParallelScope.Self)]
[TestFixture]
public class BlazorUITests : PageTest
{
    private DistributedApplication? _app;
    private string? _blazorUrl;

    [OneTimeSetUp]
    public async Task OneTimeSetUp()
    {
        var appHost = await DistributedApplicationTestingBuilder
            .CreateAsync<Projects.Sorcha_AppHost>();
        _app = await appHost.BuildAsync();
        await _app.StartAsync();
        _blazorUrl = _app.GetEndpoint("blazor-client").ToString();
    }

    [Test]
    public async Task HomePage_LoadsSuccessfully()
    {
        await Page.GotoAsync(_blazorUrl!);
        await Page.WaitForLoadStateAsync();
        await Expect(Page).ToHaveTitleAsync(new Regex("Sorcha|Blueprint"));
    }
}

Locator Patterns
// Role-based (preferred)
await Page.GetByRole(AriaRole.Button, new() { Name = "Submit" }).ClickAsync();

// Text-based
Page.Locator("a:has-text('Designer')")

// MudBlazor components
Page.Locator(".mud-button")
Page.Locator(".mud-table")

// Test IDs (most stable)
Page.Locator("[data-testid='my-element']")

Key Concepts
Concept	Usage	Example
PageTest	Base class providing Page object	class MyTests : PageTest
Locator	Lazy element reference	Page.Locator("button")
Expect	Assertion API	await Expect(Page).ToHaveURLAsync(...)
Aspire Testing	Full stack integration	DistributedApplicationTestingBuilder
Auto-wait	Built-in waiting	Actions wait for actionability
Common Patterns
JavaScript Error Detection
[Test]
public async Task NoJavaScriptErrors()
{
    var errors = new List<string>();
    Page.Console += (_, msg) =>
    {
        if (msg.Type == "error") errors.Add(msg.Text);
    };

    await Page.GotoAsync(_blazorUrl!);
    await Page.WaitForLoadStateAsync();
    
    var criticalErrors = errors.Where(e =>
        !e.Contains("WASM") && !e.Contains("Blazor")).ToList();
    Assert.That(criticalErrors, Is.Empty);
}

Responsive Design Testing
[Test]
public async Task ResponsiveDesign_Works()
{
    await Page.SetViewportSizeAsync(375, 667); // Mobile
    await Page.GotoAsync(_blazorUrl!);
    Assert.That(await Page.TextContentAsync("body"), Is.Not.Empty);

    await Page.SetViewportSizeAsync(1920, 1080); // Desktop
    await Page.ReloadAsync();
    Assert.That(await Page.TextContentAsync("body"), Is.Not.Empty);
}

See Also
patterns - Locator strategies and assertions
workflows - Test setup and CI integration
Related Skills
See the xunit skill for unit testing patterns
See the fluent-assertions skill for SignalR integration tests
See the blazor skill for component architecture
See the signalr skill for real-time notification testing
See the docker skill for container-based test environments
Documentation Resources

Fetch latest Playwright .NET documentation with Context7.

How to use Context7:

Use mcp__context7__resolve-library-id to search for "playwright"
Prefer website documentation (/websites/playwright_dev_dotnet) over source code
Query with mcp__context7__query-docs using the resolved library ID

Library ID: /websites/playwright_dev_dotnet

Recommended Queries:

"Locators selectors best practices"
"NUnit test fixtures setup teardown"
"Wait for element network idle auto-waiting"
"Assertions expect API"
"Trace viewer debugging"
Weekly Installs
23
Repository
stuartf303/sorcha
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn