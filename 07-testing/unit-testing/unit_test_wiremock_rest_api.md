---
rating: ⭐⭐
title: unit-test-wiremock-rest-api
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/unit-test-wiremock-rest-api
---

# unit-test-wiremock-rest-api

skills/giuseppe-trisciuoglio/developer-kit/unit-test-wiremock-rest-api
unit-test-wiremock-rest-api
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill unit-test-wiremock-rest-api
Summary

Unit test external REST API integrations with WireMock HTTP mocking and request verification.

Stub HTTP responses with configurable status codes, headers, and JSON bodies; verify request details including headers, query parameters, and request bodies
Test error scenarios (4xx/5xx responses, timeouts, malformed responses) without calling real APIs or hitting rate limits
Use dynamic port allocation to avoid conflicts in parallel test execution; automatic cleanup between tests via JUnit 5 extension registration
Supports request matching by URL, HTTP method, headers, and JSON path expressions for precise stub targeting
SKILL.md
Unit Testing REST APIs with WireMock
Overview

Patterns for testing external REST API integrations with WireMock: stubbing responses, verifying requests, error scenarios, and fast tests without network dependencies.

When to Use
Testing services calling external REST APIs
Stubbing HTTP responses for predictable test behavior
Testing error scenarios (timeouts, 5xx errors, malformed responses)
Verifying request details (headers, query params, request body)
Instructions
Add dependency: WireMock in test scope (Maven/Gradle)
Register extension: @RegisterExtension WireMockExtension with dynamicPort()
Configure client: Use wireMock.getRuntimeInfo().getHttpBaseUrl() as base URL
Stub responses: stubFor() with request matching (URL, headers, body)
Execute and assert: Call service methods, validate results with AssertJ
Verify requests: verify() to ensure correct API usage

If stub not matching: Check URL encoding, header names, use urlEqualTo for query params.

If tests hanging: Configure connection timeouts in HTTP client; use withFixedDelay() for timeout simulation.

If port conflicts: Always use wireMockConfig().dynamicPort().

Examples
Maven Dependencies
<dependency>
  <groupId>org.wiremock</groupId>
  <artifactId>wiremock</artifactId>
  <version>3.4.1</version>
  <scope>test</scope>
</dependency>
<dependency>
  <groupId>org.assertj</groupId>
  <artifactId>assertj-core</artifactId>
  <scope>test</scope>
</dependency>

Basic Stubbing and Verification
import com.github.tomakehurst.wiremock.junit5.WireMockExtension;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.RegisterExtension;
import static com.github.tomakehurst.wiremock.client.WireMock.*;
import static org.assertj.core.api.Assertions.assertThat;

class ExternalWeatherServiceTest {

  @RegisterExtension
  static WireMockExtension wireMock = WireMockExtension.newInstance()
    .options(wireMockConfig().dynamicPort())
    .build();

  @Test
  void shouldFetchWeatherDataFromExternalApi() {
    wireMock.stubFor(get(urlEqualTo("/weather?city=London"))
      .withHeader("Accept", containing("application/json"))
      .willReturn(aResponse()
        .withStatus(200)
        .withHeader("Content-Type", "application/json")
        .withBody("{\"city\":\"London\",\"temperature\":15,\"condition\":\"Cloudy\"}")));

    String baseUrl = wireMock.getRuntimeInfo().getHttpBaseUrl();
    WeatherApiClient client = new WeatherApiClient(baseUrl);
    WeatherData weather = client.getWeather("London");

    assertThat(weather.getCity()).isEqualTo("London");
    assertThat(weather.getTemperature()).isEqualTo(15);

    wireMock.verify(getRequestedFor(urlEqualTo("/weather?city=London"))
      .withHeader("Accept", containing("application/json")));
  }
}


See references/advanced-examples.md for error scenarios, body verification, timeout simulation, and stateful testing.

Best Practices
Dynamic port: Prevents conflicts in parallel test execution
Verify requests: Ensures correct API usage by the client
Test errors: Cover timeouts, 4xx, 5xx scenarios
Focused stubs: One concern per test
Auto-reset: @RegisterExtension resets WireMock between tests
Never call real APIs: Always stub third-party endpoints
Constraints and Warnings
Dynamic ports required: Fixed ports cause parallel execution conflicts
HTTPS testing: Configure WireMock TLS settings if testing TLS connections
Stub precedence: More specific stubs take priority over general ones
Performance: WireMock adds overhead; mock at client layer for faster tests
API changes: Keep stubs synchronized with actual API contracts
References
WireMock Documentation
WireMock Stubbing Guide
references/advanced-examples.md - Error scenarios, body verification, timeouts
Weekly Installs
728
Repository
giuseppe-trisci…oper-kit
GitHub Stars
233
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass