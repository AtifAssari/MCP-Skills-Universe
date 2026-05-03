---
rating: ⭐⭐⭐
title: geb-skill
url: https://skills.sh/lambdatest/agent-skills/geb-skill
---

# geb-skill

skills/lambdatest/agent-skills/geb-skill
geb-skill
Installation
$ npx skills add https://github.com/lambdatest/agent-skills --skill geb-skill
SKILL.md
Geb Automation Skill

For TestMu AI cloud execution, see reference/cloud-integration.md and shared/testmu-cloud-reference.md.

Core Patterns
Basic Test (Spock)
import geb.spock.GebSpec

class LoginSpec extends GebSpec {
    def "login with valid credentials"() {
        when:
        to LoginPage
        emailInput.value("user@test.com")
        passwordInput.value("password123")
        loginButton.click()

        then:
        at DashboardPage
        welcomeMessage.text().contains("Welcome")
    }

    def "login shows error for invalid credentials"() {
        when:
        to LoginPage
        emailInput.value("wrong@test.com")
        passwordInput.value("wrong")
        loginButton.click()

        then:
        at LoginPage
        errorMessage.displayed
        errorMessage.text().contains("Invalid")
    }
}

Page Objects
class LoginPage extends geb.Page {
    static url = "/login"
    static at = { title == "Login" }
    static content = {
        emailInput { $("#email") }
        passwordInput { $("#password") }
        loginButton { $("button[type='submit']") }
        errorMessage(required: false) { $(".error") }
    }
}

class DashboardPage extends geb.Page {
    static url = "/dashboard"
    static at = { $(".dashboard").displayed }
    static content = {
        welcomeMessage { $(".welcome") }
        userName { $(".user-name") }
    }
}

Navigator API
$("css-selector")
$("div", class: "active")
$("input", name: "email")
$("div.items li", 0)        // First match
$("div.items li").size()     // Count

// Actions
element.click()
element.value("text")
element << "text"            // Append text
element.text()
element.displayed
element.@href                // Attribute

Cloud: driver = new RemoteWebDriver(new URL(gridUrl), caps)
Setup: Gradle with geb-spock and selenium-support dependencies
Cloud Execution on TestMu AI

Set environment variables: LT_USERNAME, LT_ACCESS_KEY

// GebConfig.groovy
environments {
    lambdatest {
        driver = {
            def ltOptions = [
                user: System.getenv("LT_USERNAME"),
                accessKey: System.getenv("LT_ACCESS_KEY"),
                build: "Geb Build",
                name: "Geb Test",
                platformName: "Windows 11",
                video: true,
                console: true,
                network: true,
            ]
            def caps = new ChromeOptions()
            caps.setCapability("LT:Options", ltOptions)
            new RemoteWebDriver(
                new URL("https://hub.lambdatest.com/wd/hub"), caps)
        }
    }
}


Run: ./gradlew test -Dgeb.env=lambdatest

Run: ./gradlew test
Deep Patterns

See reference/playbook.md for production-grade patterns:

Section	What You Get
§1 Project Setup	build.gradle, GebConfig.groovy, environments, waiting config
§2 Page Objects	Content DSL, at checks, modules for reusable components
§3 Spec Tests	Spock integration, data-driven with @Unroll, @Stepwise flows
§4 Waiting & Async	Waiting presets, JavaScript interaction, alerts/confirms
§5 Advanced Patterns	File upload/download, windows, frames, custom extensions
§6 API Testing	REST API specs with Groovy JsonSlurper
§7 CI/CD Integration	GitHub Actions with headless Chrome, Gradle caching
§8 Debugging Table	12 common problems with causes and fixes
§9 Best Practices	14-item Geb testing checklist
Weekly Installs
37
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