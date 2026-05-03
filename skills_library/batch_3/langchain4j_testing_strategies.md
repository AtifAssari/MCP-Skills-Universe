---
title: langchain4j-testing-strategies
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/langchain4j-testing-strategies
---

# langchain4j-testing-strategies

skills/giuseppe-trisciuoglio/developer-kit/langchain4j-testing-strategies
langchain4j-testing-strategies
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill langchain4j-testing-strategies
Summary

Comprehensive testing strategies for LangChain4j applications with mocks, containers, and RAG validation.

Provides unit testing patterns with mock models, integration testing via Testcontainers, and end-to-end workflows for RAG systems, AI Services, and tool execution
Covers testing pyramid approach: 70% unit tests with mocks, 20% integration tests with real services, 10% end-to-end tests
Includes specialized patterns for streaming responses, memory management, guardrail assertions, and error handling scenarios
Requires Docker for Testcontainers-based integration tests; emphasizes test isolation, performance targets (unit tests under 50ms), and avoiding real API calls in unit tests
SKILL.md
LangChain4J Testing Strategies
Overview

Patterns for unit testing with mocks, integration testing with Testcontainers, and end-to-end validation of RAG systems, AI Services, and tool execution.

When to Use
Unit testing AI services: When you need fast, isolated tests for services using LangChain4j AiServices
Integration testing LangChain4j components: When testing real ChatModel, EmbeddingModel, or RAG pipelines with Testcontainers
Mocking AI models: When you need deterministic responses without calling external APIs
Testing LLM-based Java applications: When validating RAG workflows, tool execution, or retrieval chains
Instructions
1. Unit Testing with Mocks

Use mock models for fast, isolated testing. See references/unit-testing.md.

ChatModel mockModel = mock(ChatModel.class);
when(mockModel.generate(any(String.class)))
    .thenReturn(Response.from(AiMessage.from("Mocked response")));

var service = AiServices.builder(AiService.class)
        .chatModel(mockModel)
        .build();

2. Configure Testing Dependencies

Setup Maven/Gradle dependencies. See references/testing-dependencies.md.

langchain4j-test - Guardrail assertions
testcontainers - Containerized testing
mockito - Mock external dependencies
assertj - Fluent assertions
3. Integration Testing with Testcontainers

Test with real services. See references/integration-testing.md.

@Testcontainers
class OllamaIntegrationTest {
    @Container
    static GenericContainer<?> ollama = new GenericContainer<>(
        DockerImageName.parse("ollama/ollama:0.5.4")
    ).withExposedPorts(11434);

    @Test
    void shouldGenerateResponse() {
        // Verify container is healthy
        assertTrue(ollama.isRunning());
        await().atMost(30, TimeUnit.SECONDS)
            .until(() -> ollama.getLogs().contains("API server listening"));

        ChatModel model = OllamaChatModel.builder()
                .baseUrl(ollama.getEndpoint())
                .build();

        // Verify model responds before running tests
        assertDoesNotThrow(() -> model.generate("ping"));

        String response = model.generate("Test query");
        assertNotNull(response);
    }
}

4. Advanced Features

Streaming, memory, error handling patterns in references/advanced-testing.md.

5. Testing Workflow

Follow the testing pyramid from references/workflow-patterns.md:

70% Unit Tests: Fast, isolated with mocks
20% Integration Tests: Real services with health checks
10% End-to-End Tests: Complete workflows
70% Unit Tests ─ Mock ChatModel, guardrails, edge cases
20% Integration Tests ─ Testcontainers, vector stores, RAG
10% End-to-End Tests ─ Complete user journeys

Troubleshooting
Container fails to start: Check Docker daemon is running, verify image exists, increase timeout
Model not responding: Verify baseUrl is correct, check container logs, ensure model is loaded
Test timeout: Increase @Timeout duration for slow models, check container resource limits
Flaky tests: Add retry logic or health checks before assertions
Examples
Unit Test
@Test
void shouldProcessQueryWithMock() {
    ChatModel mockModel = mock(ChatModel.class);
    when(mockModel.generate(any(String.class)))
        .thenReturn(Response.from(AiMessage.from("Test response")));

    var service = AiServices.builder(AiService.class)
            .chatModel(mockModel)
            .build();

    String result = service.chat("What is Java?");
    assertEquals("Test response", result);
}

Integration Test with Testcontainers
@Testcontainers
class RAGIntegrationTest {
    @Container
    static GenericContainer<?> ollama = new GenericContainer<>(
        DockerImageName.parse("ollama/ollama:0.5.4")
    );

    @BeforeAll
    static void waitForContainerReady() {
        await().atMost(60, TimeUnit.SECONDS)
            .until(() -> ollama.getLogs().contains("API server listening"));
    }

    @Test
    void shouldCompleteRAGWorkflow() {
        assertTrue(ollama.isRunning());

        var chatModel = OllamaChatModel.builder()
                .baseUrl(ollama.getEndpoint())
                .build();

        var embeddingModel = OllamaEmbeddingModel.builder()
                .baseUrl(ollama.getEndpoint())
                .build();

        var store = new InMemoryEmbeddingStore<>();
        var retriever = EmbeddingStoreContentRetriever.builder()
                .chatModel(chatModel)
                .embeddingStore(store)
                .embeddingModel(embeddingModel)
                .build();

        var assistant = AiServices.builder(RagAssistant.class)
                .chatLanguageModel(chatModel)
                .contentRetriever(retriever)
                .build();

        String response = assistant.chat("What is Spring Boot?");
        assertNotNull(response);
        assertTrue(response.contains("Spring"));
    }
}

Best Practices
Use @BeforeEach/@AfterEach for test isolation
Never call real APIs in unit tests; use mocks
Include @Timeout for external service calls
Test both success and error handling scenarios
Validate response coherence and edge cases
Common Patterns
Mock Strategy
ChatModel mockModel = mock(ChatModel.class);
when(mockModel.generate(anyString())).thenReturn(Response.from(AiMessage.from("Mocked")));
when(mockModel.generate(eq("Hello"))).thenReturn(Response.from(AiMessage.from("Hi")));
when(mockModel.generate(contains("Java"))).thenReturn(Response.from(AiMessage.from("Java")));

Assertion Helpers
assertThat(response).isNotNull().isNotEmpty();
assertThat(response).containsAll(expectedKeywords);
assertThat(response).doesNotContain("error");

Reference Documentation
Testing Dependencies - Maven/Gradle configuration
Unit Testing - Mock models, guardrails
Integration Testing - Testcontainers, real services
Advanced Testing - Streaming, memory, error handling
Workflow Patterns - Test pyramid, best practices
Constraints and Warnings
AI responses are non-deterministic; use mocks for reliable unit tests
Avoid real API calls in tests to prevent costs and rate limiting
Integration tests require Docker; use container health checks
RAG tests need properly seeded embedding stores
Mock-based tests cannot guarantee actual LLM behavior; supplement with integration tests
Use test-specific configuration profiles; never affect production data
Weekly Installs
695
Repository
giuseppe-trisci…oper-kit
GitHub Stars
233
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass