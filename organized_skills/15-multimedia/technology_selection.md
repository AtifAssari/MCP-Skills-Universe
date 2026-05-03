---
rating: ⭐⭐
title: technology-selection
url: https://skills.sh/dotnet/skills/technology-selection
---

# technology-selection

skills/dotnet/skills/technology-selection
technology-selection
Installation
$ npx skills add https://github.com/dotnet/skills --skill technology-selection
SKILL.md
.NET AI and Machine Learning
Inputs
Input	Required	Description
Task description	Yes	What the AI/ML feature should accomplish (e.g., "classify support tickets", "summarize documents")
Data description	Yes	Type and shape of input data (structured/tabular, unstructured text, images, mixed)
Deployment constraints	No	Cloud vs. local, latency SLO, cost budget, offline requirements
Existing project context	No	Current .csproj, existing packages, target framework
Workflow
Step 1: Classify the task using the decision tree

Evaluate the developer's task against this decision tree and select the appropriate technology. State which branch applies and why.

Task type	Technology	Rationale
Structured/tabular data: classification, regression, clustering, anomaly detection, recommendation	ML.NET (Microsoft.ML)	Reproducible (given a fixed seed and dataset), no cloud dependency, purpose-built models for these tasks
Natural language understanding, generation, summarization, reasoning over unstructured text (single prompt → response, no tool calling)	LLM via Microsoft.Extensions.AI (IChatClient)	Requires language model capabilities beyond pattern matching; no orchestration needed
Agentic workflows: tool/function calling, multi-step reasoning, agent loops, multi-agent collaboration	Microsoft Agent Framework (Microsoft.Agents.AI) built on top of Microsoft.Extensions.AI	Requires orchestration, tool dispatch, iteration control, and guardrails that IChatClient alone does not provide
Building GitHub Copilot extensions, custom agents, or developer workflow tools	GitHub Copilot SDK (GitHub.Copilot.SDK)	Integrates with the Copilot agent runtime for IDE and CLI extensibility
Running a pre-trained or fine-tuned custom model in production	ONNX Runtime (Microsoft.ML.OnnxRuntime)	Hardware-accelerated inference, model-format agnostic
Local/offline LLM inference with no cloud dependency	OllamaSharp with local AI models supported by Ollama	Privacy-sensitive, air-gapped, or cost-constrained scenarios
Semantic search, RAG, or embedding storage	Microsoft.Extensions.VectorData.Abstractions + a vector database provider (e.g., Azure AI Search, Milvus, MongoDB, pgvector, Pinecone, Qdrant, Redis, SQL)	Provider-agnostic abstractions for vector similarity search; pair with a database-specific connector package (many are moving to community toolkits)
Ingesting, chunking, and loading documents into a vector store	Microsoft.Extensions.AI.DataIngestion (preview) + Microsoft.Extensions.VectorData.Abstractions (MEVD)	Handles document parsing, text chunking, embedding generation, and upserting into a vector database; pairs with Microsoft.Extensions.VectorData.Abstractions
Both structured ML predictions AND natural language reasoning	Hybrid: ML.NET for predictions + LLM for reasoning layer	Keep loosely coupled; ML.NET handles reproducible scoring, LLM adds explanation

Critical rule: Do NOT use an LLM for tasks that ML.NET handles well (classification on tabular data, regression, clustering). LLMs are slower, more expensive, and non-deterministic for these tasks.

Step 1b: Select the correct library layer

After identifying the task type, select the right library layer. These libraries form a stack — each builds on the one below it. Using the wrong layer is a major source of non-deterministic agent behavior.

Layer	Library	NuGet package	Use when
Abstraction	Microsoft.Extensions.AI (MEAI)	Microsoft.Extensions.AI	You need a provider-agnostic interface for chat, embeddings, or tool calling. This is the foundation — always include it. Use IChatClient directly only for simple prompt-in/response-out scenarios with no tool calling or agentic loops. If the task involves tools, agents, or multi-step reasoning, you must add the Orchestration layer above.
Provider SDK	OpenAI, Azure.AI.OpenAI, Azure.AI.Inference, OllamaSharp	OpenAI, Azure.AI.OpenAI, Azure.AI.Inference, OllamaSharp	You need a concrete LLM provider implementation. These wire into MEAI via AddChatClient. Use OpenAI for direct OpenAI access, Azure.AI.OpenAI for Azure OpenAI, Azure.AI.Inference for Azure AI Foundry / GitHub Models, or OllamaSharp for local Ollama. Use directly only if you need provider-specific features not exposed through MEAI.
Orchestration	Microsoft Agent Framework	Microsoft.Agents.AI (prerelease)	The task involves tool/function calling, agentic loops, multi-step reasoning, multi-agent coordination, durable context, or graph-based workflows. This is required whenever the scenario involves agents or tools — do not hand-roll tool dispatch loops with IChatClient. Builds on top of MEAI. Note: This package is currently prerelease — use dotnet add package Microsoft.Agents.AI --prerelease to install it.
Copilot integration	GitHub Copilot SDK	GitHub.Copilot.SDK	You are building extensions or tools that integrate with the GitHub Copilot runtime — custom agents, IDE extensions, or developer workflow automation that leverages the Copilot agent platform.
Decision rules for library selection

Start with MEAI. Every AI integration begins with Microsoft.Extensions.AI for the IChatClient / IEmbeddingGenerator abstractions. This ensures provider-swappability and testability.

Add a provider SDK (OpenAI, Azure.AI.OpenAI) as the concrete implementation behind MEAI. Do not call the provider SDK directly in business logic — always go through the MEAI abstraction.

Use Agent Framework (Microsoft.Agents.AI) for any task that involves tools or agents. If the task is a single prompt → response with no tool calling, MEAI is sufficient. You MUST use Microsoft.Agents.AI when any of these apply:

Tool/function calling (agent decides which tools to invoke)
Multi-step reasoning with state carried across turns
Agentic loops that iterate until a goal is met
Multi-agent collaboration with handoff protocols
Graph-based or durable workflows

Do not implement these patterns by hand with IChatClient — the Agent Framework provides iteration limits, observability, and tool dispatch that are error-prone to reimplement.

Add Copilot SDK only when building Copilot extensions. Use GitHub.Copilot.SDK when the goal is to build a custom agent or tool that runs inside the GitHub Copilot platform (CLI, IDE, or Copilot Chat). This is not a general-purpose LLM orchestration library — it is specifically for Copilot extensibility.

Never skip layers. Do not use Agent Framework without MEAI underneath. Do not call HttpClient to OpenAI alongside MEAI in the same workflow. Each layer depends on the one below it.

Step 2: Select packages and set up the project

Install only the packages needed for the selected technology branch. Do not mix competing abstractions.

Classic ML packages
<PackageReference Include="Microsoft.ML" Version="4.*" />
<PackageReference Include="Microsoft.ML.AutoML" Version="0.*" />
<!-- Only if custom numerical work is needed: -->
PackageReference Include="System.Numerics.Tensors" Version="10.*"
<PackageReference Include="MathNet.Numerics" Version="5.*" />
<!-- Only for data exploration: -->
<PackageReference Include="Microsoft.Data.Analysis" Version="0.*" />


Do NOT use Accord.NET — it is archived and unmaintained.

Modern AI packages
<!-- Always start with the abstraction layer -->
<PackageReference Include="Microsoft.Extensions.AI" Version="9.*" />

<!-- Orchestration (agents, workflows, tools, memory) — prerelease; use dotnet add package Microsoft.Agents.AI --prerelease -->
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />

<!-- Cloud LLM provider (pick one) -->
<PackageReference Include="Azure.AI.OpenAI" Version="2.*" />
<!-- OR -->
<PackageReference Include="OpenAI" Version="2.*" />

<!-- Client-side token counting for cost management -->
    <PackageReference Include="Microsoft.ML.Tokenizers" Version="2.*" 

<!-- Local LLM inference -->
<PackageReference Include="OllamaSharp" Version="5.*" />

<!-- Custom model inference -->
<PackageReference Include="Microsoft.ML.OnnxRuntime" Version="1.*" />

<!-- Vector store abstraction -->
<PackageReference Include="Microsoft.Extensions.VectorData.Abstractions" Version="9.*" />

<!-- Document ingestion, chunking, and vector store loading (preview) -->
<PackageReference Include="Microsoft.Extensions.AI.DataIngestion" Version="9.*-*" />

<!-- Copilot platform extensibility -->
<PackageReference Include="GitHub.Copilot.SDK" Version="1.*" />


Stack coherence rule: Never mix raw SDK calls (HttpClient to OpenAI) with Microsoft.Extensions.AI, Microsoft Agent Framework, or Copilot SDK in the same workflow. Pick one abstraction layer per workflow boundary and commit to it. See Step 1b for the layering rules.

Register services with dependency injection

All AI/ML services must be registered via DI. Never instantiate clients directly in business logic.

// Configuration via IOptions<T>
services.Configure<AiOptions>(configuration.GetSection("AI"));

// Register the AI client through the abstraction
services.AddChatClient(builder => builder
    .UseOpenAIChatClient("gpt-4o-mini-2024-07-18"));

Step 3: Implement with guardrails

Apply the guardrails for the selected technology branch. Every generated implementation must follow these rules.

Classic ML guardrails

Reproducibility: Always set a random seed in the ML context:

var mlContext = new MLContext(seed: 42);


Data splitting: Always split into train/test (and optionally validation). Never evaluate on training data:

var split = mlContext.Data.TrainTestSplit(data, testFraction: 0.2);


Metrics logging: Always compute and log evaluation metrics appropriate to the task:

var metrics = mlContext.BinaryClassification.Evaluate(predictions);
logger.LogInformation("AUC: {Auc:F4}, F1: {F1:F4}", metrics.AreaUnderRocCurve, metrics.F1Score);


AutoML first: Prefer mlContext.Auto() for initial model selection, then refine manually.

PredictionEngine pooling: In ASP.NET Core, always use the pooled prediction engine — never a singleton:

services.AddPredictionEnginePool<ModelInput, ModelOutput>()
    .FromFile(modelPath);

LLM integration guardrails

Temperature: Always set explicitly. Use 0 for factual/deterministic tasks:

var options = new ChatOptions
{
    Temperature = 0f,
    MaxOutputTokens = 1024,
};


Structured output: Always parse LLM output into strongly-typed objects with fallback handling:

var result = await chatClient.GetResponseAsync<MySchema>(prompt, options, cancellationToken);


Retry logic: Always implement retry with exponential backoff:

services.AddChatClient(builder => builder
    .UseOpenAIChatClient(modelId)
    .Use(new RetryingChatClient(maxRetries: 3)));


Cost control: Always estimate and log token usage. Use Microsoft.ML.Tokenizers to count tokens client-side before sending requests so you can enforce budgets proactively. Choose the smallest model tier that meets quality requirements (e.g., gpt-4o-mini before gpt-4o).

Secret management: Never hardcode API keys. Use Azure Key Vault, user-secrets, or environment variables:

var apiKey = configuration["AI:ApiKey"]
    ?? throw new InvalidOperationException("AI:ApiKey not configured");


Model version pinning: Specify exact model versions to reduce behavioral drift:

// Pin to a specific dated version, not just "gpt-4o"
var modelId = "gpt-4o-2024-08-06";

Agentic workflow guardrails

Use Microsoft.Agents.AI for all agentic workflows. Do not implement tool dispatch loops or multi-step agent reasoning by hand with IChatClient. The Agent Framework provides ChatClientAgent (or AgentWorker) which handles the tool call → result → re-prompt cycle with built-in guardrails. All rules below assume you are using Microsoft.Agents.AI.

Iteration limits: Always cap agentic loops to prevent runaway execution:

var settings = new AgentInvokeOptions
{
    MaximumIterations = 10,
};


Cost ceiling: Implement a token budget per execution and terminate when reached. Use Microsoft.ML.Tokenizers to count prompt and completion tokens locally and compare against the budget before each iteration.

Observability: Log non-sensitive metadata for every agent step. Never log raw message.Content — it may contain user prompts, tool outputs, secrets, or PII that persist in plaintext in central logging systems:

await foreach (var message in agent.InvokeStreamingAsync(history, settings))
{
    logger.LogDebug("Agent step: Role={Role}, ContentLength={Length}",
        message.Role, message.Content?.Length ?? 0);
}


Tool schemas: Define explicit tool/function schemas with descriptions. Never rely on implicit tool discovery.

Simplicity preference: Prefer single-agent with tools over multi-agent unless the task genuinely requires agent collaboration.

RAG guardrails

Embedding caching: Never re-embed the same content on every query. Cache embeddings in the vector store.

Chunking strategy: Use semantic chunking (split on paragraph/section boundaries) over fixed-size chunking. Ensure chunks have enough context to be useful on their own.

Relevance thresholds: Do not inject low-relevance chunks into context. Set a minimum similarity score:

var results = await vectorStore.SearchAsync(query, new VectorSearchOptions
{
    Top = 5,
    MinimumScore = 0.75f,
});


Source attribution: Track which chunks contributed to the final response. Include source references in the output.

Batch embeddings: Batch embedding API calls where possible to reduce latency and cost.

Step 4: Handle non-determinism

When the solution involves LLM calls or agentic workflows, explicitly address non-determinism:

Acknowledge it: Inform the developer that LLM outputs are non-deterministic even at temperature 0 (due to batching, quantization, and model updates).

Validate outputs: Implement schema validation and content assertion checks on every LLM response.

Graceful degradation: Design a fallback path for when the LLM returns unexpected, malformed, or empty output:

var response = await chatClient.GetResponseAsync<ClassificationResult>(prompt, options);
if (response is null || !response.IsValid())
{
    logger.LogWarning("LLM returned invalid response, falling back to rule-based classifier");
    return ruleBasedClassifier.Classify(input);
}


Evaluation harness: For any prompt that will be iterated on, recommend creating a golden dataset and evaluation scaffold to measure prompt quality over time.

Model version pinning: Pin to specific dated model versions (e.g., gpt-4o-2024-08-06) to reduce drift between deployments.

Step 5: Apply performance and cost controls

Connection pooling: Use IHttpClientFactory and DI-managed clients for all external services.

Response caching: Cache repeated or similar queries. Consider semantic caching for LLM responses where appropriate.

Streaming: Use IAsyncEnumerable for LLM responses in user-facing scenarios to reduce time-to-first-token:

await foreach (var update in chatClient.GetStreamingResponseAsync(prompt, options))
{
    yield return update.Text;
}


Health checks: Implement health checks for external AI service dependencies:

services.AddHealthChecks()
    .AddCheck<OpenAIHealthCheck>("openai");


ML.NET prediction pooling: In web applications, always use PredictionEnginePool<TIn, TOut>, never a single PredictionEngine instance (it is not thread-safe).

Step 6: Validate the implementation

Build the project and verify no warnings:

dotnet build -c Release -warnaserror


Run tests, including integration tests that validate AI/ML behavior:

dotnet test -c Release


For ML.NET pipelines, verify that evaluation metrics meet the project's quality bar and that the model can be serialized and loaded correctly.

For LLM integrations, verify that structured output parsing handles both valid and malformed responses.

For RAG pipelines, verify that retrieval returns relevant results and that irrelevant chunks are filtered out.

Validation
 Technology selection follows the decision tree — LLMs are not used for tasks ML.NET handles
 All AI/ML services are registered via dependency injection
 Configuration uses IOptions<T> pattern — no hardcoded values
 API keys are loaded from secure sources — not in source code or committed config files
 ML.NET pipelines set a random seed and split data for evaluation
 LLM calls set temperature, max tokens, and retry logic explicitly
 Agentic workflows have iteration limits and cost ceilings
 RAG pipelines implement chunking, relevance thresholds, and source attribution
 Non-deterministic outputs have validation and fallback paths
 dotnet build -c Release -warnaserror completes cleanly
Anti-Patterns to Reject

When reviewing or generating code, flag and redirect the developer if any of these patterns are detected:

Anti-pattern	Redirect
Using an LLM for classification on structured/tabular data	Use ML.NET instead — it is faster, cheaper, and deterministic
Calling LLM APIs without retry or timeout logic	Add RetryingChatClient or Polly-based retry with exponential backoff
Storing API keys in appsettings.json committed to source control	Use user-secrets (dev), environment variables, or Azure Key Vault (prod)
Using Accord.NET for new projects	Migrate to ML.NET — Accord.NET is archived and unmaintained
Building custom neural networks in .NET from scratch	Use a pre-trained model via ONNX Runtime or call an LLM API
RAG without chunking strategy or relevance filtering	Implement semantic chunking and set a minimum similarity score threshold
Agentic loops without iteration limits or cost ceilings	Add MaximumIterations and a token budget ceiling
Using MEAI IChatClient with raw HttpClient calls to the same provider	Pick one abstraction layer and commit to it
Implementing tool calling or agentic loops manually with IChatClient instead of using Microsoft.Agents.AI	Use Microsoft.Agents.AI — it provides iteration limits (MaximumIterations), built-in tool dispatch, observability hooks, and cost controls. Hand-rolled loops lack these guardrails.
Using Agent Framework for a single prompt→response call	Use MEAI IChatClient directly — Agent Framework is for multi-step orchestration
Using Copilot SDK for general-purpose LLM apps	Copilot SDK is for Copilot platform extensions only — use MEAI + Agent Framework for standalone apps
Calling OpenAI SDK directly in business logic instead of through MEAI	Register the provider via AddChatClient and depend on IChatClient in business code
Using PredictionEngine as a singleton in ASP.NET Core	Use PredictionEnginePool<TIn, TOut> — PredictionEngine is not thread-safe
Using Func<ReadOnlySpan<T>> for delegates with ref struct parameters	Define a custom delegate type — ref structs cannot be generic type arguments
Using Microsoft.SemanticKernel for new projects	Use Microsoft.Extensions.AI + Microsoft.Agents.AI — Semantic Kernel is superseded by these newer abstractions for LLM orchestration and tool calling
Common Pitfalls
Pitfall	Solution
Over-engineering with LLMs	Start with the simplest approach (rules, ML.NET) and add LLM capability only when simpler methods fall short
Evaluating ML models on training data	Always use TrainTestSplit and report metrics on the held-out test set
LLM output drift between deployments	Pin to specific dated model versions (e.g., gpt-4o-2024-08-06)
Token cost surprises	Set MaxOutputTokens, use Microsoft.ML.Tokenizers for accurate client-side token counting, log token counts per request, and alert on budget thresholds
Non-reproducible ML training	Set MLContext(seed: N) and version your training data alongside the code
RAG returning irrelevant context	Set a minimum similarity score and limit the number of injected chunks
Cold start latency on ML.NET models	Pre-warm the PredictionEnginePool during application startup
Microsoft Agent Framework + raw OpenAI SDK in same class	Choose one orchestration layer per workflow boundary
Weekly Installs
237
Repository
dotnet/skills
GitHub Stars
1.5K
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass