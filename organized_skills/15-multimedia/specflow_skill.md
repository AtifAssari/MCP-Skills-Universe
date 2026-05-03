---
rating: ⭐⭐
title: specflow-skill
url: https://skills.sh/lambdatest/agent-skills/specflow-skill
---

# specflow-skill

skills/lambdatest/agent-skills/specflow-skill
specflow-skill
Installation
$ npx skills add https://github.com/lambdatest/agent-skills --skill specflow-skill
SKILL.md
SpecFlow BDD Skill
Core Patterns
Feature File (Features/Login.feature)
Feature: User Login

  Scenario: Successful login
    Given I am on the login page
    When I enter "user@test.com" as email
    And I enter "password123" as password
    And I click the login button
    Then I should see the dashboard
    And the welcome message should contain "Welcome"

  Scenario: Invalid credentials
    Given I am on the login page
    When I enter "wrong@test.com" as email
    And I enter "wrong" as password
    And I click the login button
    Then I should see error "Invalid credentials"

  Scenario Outline: Login with various users
    Given I am on the login page
    When I enter "<email>" as email
    And I enter "<password>" as password
    And I click the login button
    Then I should see "<result>"

    Examples:
      | email          | password | result    |
      | admin@test.com | admin123 | Dashboard |
      | user@test.com  | pass123  | Dashboard |
      | bad@test.com   | wrong    | Error     |

Step Bindings
using TechTalk.SpecFlow;
using NUnit.Framework;

[Binding]
public class LoginSteps
{
    private readonly ScenarioContext _context;
    private IWebDriver _driver;

    public LoginSteps(ScenarioContext context)
    {
        _context = context;
        _driver = (IWebDriver)_context["driver"];
    }

    [Given(@"I am on the login page")]
    public void GivenIAmOnTheLoginPage()
    {
        _driver.Navigate().GoTo("http://localhost:3000/login");
    }

    [When(@"I enter ""(.*)"" as email")]
    public void WhenIEnterEmail(string email)
    {
        _driver.FindElement(By.Id("email")).SendKeys(email);
    }

    [When(@"I enter ""(.*)"" as password")]
    public void WhenIEnterPassword(string password)
    {
        _driver.FindElement(By.Id("password")).SendKeys(password);
    }

    [When(@"I click the login button")]
    public void WhenIClickLogin()
    {
        _driver.FindElement(By.CssSelector("button[type='submit']")).Click();
    }

    [Then(@"I should see the dashboard")]
    public void ThenIShouldSeeDashboard()
    {
        Assert.That(_driver.Url, Does.Contain("/dashboard"));
    }

    [Then(@"I should see error ""(.*)""")]
    public void ThenIShouldSeeError(string error)
    {
        var element = _driver.FindElement(By.CssSelector(".error"));
        Assert.That(element.Text, Does.Contain(error));
    }
}

Hooks
[Binding]
public class Hooks
{
    private readonly ScenarioContext _context;

    public Hooks(ScenarioContext context) { _context = context; }

    [BeforeScenario]
    public void BeforeScenario()
    {
        var driver = new ChromeDriver();
        _context["driver"] = driver;
    }

    [AfterScenario]
    public void AfterScenario()
    {
        ((IWebDriver)_context["driver"]).Quit();
    }
}

Dependency Injection (Context Injection)
// SpecFlow auto-injects ScenarioContext, FeatureContext, and custom POCOs
public class LoginSteps
{
    private readonly LoginPage _loginPage;
    public LoginSteps(LoginPage loginPage) { _loginPage = loginPage; }
}

Setup: dotnet add package SpecFlow.NUnit or SpecFlow.xUnit
Run: dotnet test
Cloud Execution on TestMu AI

Set environment variables: LT_USERNAME, LT_ACCESS_KEY

// Hooks.cs
[BeforeScenario]
public void Setup()
{
    var ltOptions = new Dictionary<string, object>
    {
        { "user", Environment.GetEnvironmentVariable("LT_USERNAME") },
        { "accessKey", Environment.GetEnvironmentVariable("LT_ACCESS_KEY") },
        { "build", "SpecFlow Build" },
        { "name", ScenarioContext.Current.ScenarioInfo.Title },
        { "platformName", "Windows 11" },
        { "video", true },
        { "console", true },
    };
    var options = new ChromeOptions();
    options.AddAdditionalOption("LT:Options", ltOptions);
    _driver = new RemoteWebDriver(
        new Uri("https://hub.lambdatest.com/wd/hub"), options);
}

Report: SpecFlow+ LivingDoc extension for rich HTML reports
Deep Patterns

For advanced patterns, debugging guides, CI/CD integration, and best practices, see reference/playbook.md.

Weekly Installs
44
Repository
lambdatest/agent-skills
GitHub Stars
247
First Seen
Feb 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass