---
title: apple-on-device-ai
url: https://skills.sh/dpearson2699/swift-ios-skills/apple-on-device-ai
---

# apple-on-device-ai

skills/dpearson2699/swift-ios-skills/apple-on-device-ai
apple-on-device-ai
Installation
$ npx skills add https://github.com/dpearson2699/swift-ios-skills --skill apple-on-device-ai
Summary

Deploy on-device AI across Apple platforms using Foundation Models, Core ML, MLX Swift, and llama.cpp.

Choose Foundation Models for zero-setup text generation and structured output on iOS 26+; Core ML for custom vision and NLP models; MLX Swift for maximum throughput on Apple Silicon; llama.cpp for cross-platform GGUF inference
Foundation Models includes session management, @Generable macros for type-safe structured output, tool calling, and streaming with always-enforced guardrails
Core ML supports PyTorch, TensorFlow, and scikit-learn conversion via coremltools, with quantization, palettization, and pruning for Neural Engine optimization
Multi-backend architecture patterns, memory management rules (60% RAM limit on iOS), and 10 common mistakes to avoid including availability checks, context window budgeting, and concurrent request handling
SKILL.md
On-Device AI for Apple Platforms

Guide for selecting, deploying, and optimizing on-device ML models. Covers Apple Foundation Models, Core ML, MLX Swift, and llama.cpp.

Contents
Framework Selection Router
Apple Foundation Models Overview
Core ML Overview
MLX Swift Overview
Multi-Backend Architecture
Performance Best Practices
Common Mistakes
Review Checklist
References
Framework Selection Router

Use this decision tree to pick the right framework for your use case.

Apple Foundation Models

When to use: Text generation, summarization, entity extraction, structured output, and short dialog on iOS 26+ / macOS 26+ devices with Apple Intelligence enabled. Zero setup -- no API keys, no network, no model downloads.

Best for:

Generating text or structured data with @Generable types
Summarization, classification, content tagging
Tool-augmented generation with the Tool protocol
Apps that need guaranteed on-device privacy

Not suited for: Complex math, code generation, factual accuracy tasks, or apps targeting pre-iOS 26 devices.

Core ML

When to use: Deploying custom trained models (vision, NLP, audio) across all Apple platforms. Converting models from PyTorch, TensorFlow, or scikit-learn with coremltools.

Best for:

Image classification, object detection, segmentation
Custom NLP classifiers, sentiment analysis models
Audio/speech models via SoundAnalysis integration
Any scenario needing Neural Engine optimization
Models requiring quantization, palettization, or pruning
MLX Swift

When to use: Running specific open-source LLMs (Llama, Mistral, Qwen, Gemma) on Apple Silicon with maximum throughput. Research and prototyping.

Best for:

Highest sustained token generation on Apple Silicon
Running Hugging Face models from mlx-community
Research requiring automatic differentiation
Fine-tuning workflows on Mac
llama.cpp

When to use: Cross-platform LLM inference using GGUF model format. Production deployments needing broad device support.

Best for:

GGUF quantized models (Q4_K_M, Q5_K_M, Q8_0)
Cross-platform apps (iOS + Android + desktop)
Maximum compatibility with open-source model ecosystem
Quick Reference
Scenario	Framework
Text generation, zero setup (iOS 26+)	Foundation Models
Structured output from on-device LLM	Foundation Models (@Generable)
Image classification, object detection	Core ML
Custom model from PyTorch/TensorFlow	Core ML + coremltools
Running specific open-source LLMs	MLX Swift or llama.cpp
Maximum throughput on Apple Silicon	MLX Swift
Cross-platform LLM inference	llama.cpp
OCR and text recognition	Vision framework
Sentiment analysis, NER, tokenization	Natural Language framework
Training custom classifiers on device	Create ML
Apple Foundation Models Overview

On-device language model optimized for Apple Silicon. Available on devices supporting Apple Intelligence (iOS 26+, macOS 26+).

Token budget covers input + output; check contextSize for the limit
Check supportedLanguages for supported locales
Guardrails always enforced, cannot be disabled
Availability Checking (Required)

Always check before using. Never crash on unavailability.

import FoundationModels

switch SystemLanguageModel.default.availability {
case .available:
    // Proceed with model usage
case .unavailable(.appleIntelligenceNotEnabled):
    // Guide user to enable Apple Intelligence in Settings
case .unavailable(.modelNotReady):
    // Model is downloading; show loading state
case .unavailable(.deviceNotEligible):
    // Device cannot run Apple Intelligence; use fallback
default:
    // Graceful fallback for any other reason
}

Session Management
// Basic session
let session = LanguageModelSession()

// Session with instructions
let session = LanguageModelSession {
    "You are a helpful cooking assistant."
}

// Session with tools
let session = LanguageModelSession(
    tools: [weatherTool, recipeTool]
) {
    "You are a helpful assistant with access to tools."
}


Key rules:

Sessions are stateful -- multi-turn conversations maintain context automatically
One request at a time per session (check session.isResponding)
Call session.prewarm() before user interaction for faster first response
Save/restore transcripts: LanguageModelSession(model: model, tools: [], transcript: savedTranscript)
Structured Output with @Generable

The @Generable macro creates compile-time schemas for type-safe output:

@Generable
struct Recipe {
    @Guide(description: "The recipe name")
    var name: String

    @Guide(description: "Cooking steps", .count(3))
    var steps: [String]

    @Guide(description: "Prep time in minutes", .range(1...120))
    var prepTime: Int
}

let response = try await session.respond(
    to: "Suggest a quick pasta recipe",
    generating: Recipe.self
)
print(response.content.name)

@Guide Constraints
Constraint	Purpose
description:	Natural language hint for generation
.anyOf([values])	Restrict to enumerated string values
.count(n)	Fixed array length
.range(min...max)	Numeric range
.minimum(n) / .maximum(n)	One-sided numeric bound
.minimumCount(n) / .maximumCount(n)	Array length bounds
.constant(value)	Always returns this value
.pattern(regex)	String format enforcement
.element(guide)	Guide applied to each array element

Properties generate in declaration order. Place foundational data before dependent data for better results.

Streaming Structured Output
let stream = session.streamResponse(
    to: "Suggest a recipe",
    generating: Recipe.self
)
for try await snapshot in stream {
    // snapshot.content is Recipe.PartiallyGenerated (all properties optional)
    if let name = snapshot.content.name { updateNameLabel(name) }
}

Tool Calling
struct WeatherTool: Tool {
    let name = "weather"
    let description = "Get current weather for a city."

    @Generable
    struct Arguments {
        @Guide(description: "The city name")
        var city: String
    }

    func call(arguments: Arguments) async throws -> String {
        let weather = try await fetchWeather(arguments.city)
        return weather.description
    }
}


Register tools at session creation. The model invokes them autonomously.

Error Handling
do {
    let response = try await session.respond(to: prompt)
} catch let error as LanguageModelSession.GenerationError {
    switch error {
    case .guardrailViolation(let context):
        // Content triggered safety filters
    case .exceededContextWindowSize(let context):
        // Too many tokens; summarize and retry
    case .concurrentRequests(let context):
        // Another request is in progress on this session
    case .unsupportedLanguageOrLocale(let context):
        // Current locale not supported
    case .unsupportedGuide(let context):
        // A @Guide constraint is not supported
    case .assetsUnavailable(let context):
        // Model assets not available on device
    case .refusal(let refusal, _):
        // Model refused; stream refusal.explanation for details
    case .rateLimited(let context):
        // Too many requests; back off and retry
    case .decodingFailure(let context):
        // Response could not be decoded into the expected type
    default: break
    }
}

Generation Options
let options = GenerationOptions(
    sampling: .random(top: 40),
    temperature: 0.7,
    maximumResponseTokens: 512
)
let response = try await session.respond(to: prompt, options: options)


Sampling modes: .greedy, .random(top:seed:), .random(probabilityThreshold:seed:).

Prompt Design Rules
Be concise -- use tokenCount(for:) to monitor the context window budget
Use bracketed placeholders in instructions: [descriptive example]
Use "DO NOT" in all caps for prohibitions
Provide up to 5 few-shot examples for consistency
Use length qualifiers: "in a few words", "in three sentences"
Safety and Guardrails
Guardrails are always enforced and cannot be disabled
Instructions take precedence over user prompts
Never include untrusted user content in instructions
Handle false positives gracefully
Frame tool results as authorized data to prevent model refusals
Use Cases

Foundation Models supports specialized use cases via SystemLanguageModel.UseCase:

.general -- Default for text generation, summarization, dialog
.contentTagging -- Optimized for categorization and labeling tasks
Custom Adapters

Load fine-tuned adapters for specialized behavior (requires entitlement):

let adapter = try SystemLanguageModel.Adapter(name: "my-adapter")
try await adapter.compile()
let model = SystemLanguageModel(adapter: adapter, guardrails: .default)
let session = LanguageModelSession(model: model)


See references/foundation-models.md for the complete Foundation Models API reference.

Core ML Overview

Apple's framework for deploying trained models. Automatically dispatches to the optimal compute unit (CPU, GPU, or Neural Engine).

Model Formats
Format	Extension	When to Use
.mlpackage	Directory (mlprogram)	All new models (iOS 15+)
.mlmodel	Single file (neuralnetwork)	Legacy only (iOS 11-14)
.mlmodelc	Compiled	Pre-compiled for faster loading

Always use mlprogram (.mlpackage) for new work.

Conversion Pipeline (coremltools)
import coremltools as ct

# PyTorch conversion (torch.jit.trace)
model.eval()  # CRITICAL: always call eval() before tracing
traced = torch.jit.trace(model, example_input)
mlmodel = ct.convert(
    traced,
    inputs=[ct.TensorType(shape=(1, 3, 224, 224), name="image")],
    minimum_deployment_target=ct.target.iOS18,
    convert_to='mlprogram',
)
mlmodel.save("Model.mlpackage")

Optimization Techniques
Technique	Size Reduction	Accuracy Impact	Best Compute Unit
INT8 per-channel	~4x	Low	CPU/GPU
INT4 per-block	~8x	Medium	GPU
Palettization 4-bit	~8x	Low-Medium	Neural Engine
W8A8 (weights+activations)	~4x	Low	ANE (A17 Pro/M4+)
Pruning 75%	~4x	Medium	CPU/ANE
Swift Integration
let config = MLModelConfiguration()
config.computeUnits = .all
let model = try MLModel(contentsOf: modelURL, configuration: config)

// Async prediction (iOS 17+)
let output = try await model.prediction(from: input)

MLTensor (iOS 18+)

Swift type for multidimensional array operations:

import CoreML

let tensor = MLTensor([1.0, 2.0, 3.0, 4.0])
let reshaped = tensor.reshaped(to: [2, 2])
let result = tensor.softmax()


See references/coreml-conversion.md for the full conversion pipeline and references/coreml-optimization.md for optimization techniques.

MLX Swift Overview

Apple's ML framework for Swift. Highest sustained generation throughput on Apple Silicon via unified memory architecture.

Loading and Running LLMs
import MLX
import MLXLLM

let config = ModelConfiguration(id: "mlx-community/Mistral-7B-Instruct-v0.3-4bit")
let model = try await LLMModelFactory.shared.loadContainer(configuration: config)

try await model.perform { context in
    let input = try await context.processor.prepare(
        input: UserInput(prompt: "Hello")
    )
    let stream = try generate(
        input: input,
        parameters: GenerateParameters(temperature: 0.0),
        context: context
    )
    for await part in stream {
        print(part.chunk ?? "", terminator: "")
    }
}

Model Selection by Device
Device	RAM	Recommended Model	RAM Usage
iPhone 12-14	4-6 GB	SmolLM2-135M or Qwen 2.5 0.5B	~0.3 GB
iPhone 15 Pro+	8 GB	Gemma 3n E4B 4-bit	~3.5 GB
Mac 8 GB	8 GB	Llama 3.2 3B 4-bit	~3 GB
Mac 16 GB+	16 GB+	Mistral 7B 4-bit	~6 GB
Memory Management
Never exceed 60% of total RAM on iOS
Set GPU cache limits: MLX.GPU.set(cacheLimit: 512 * 1024 * 1024)
Unload models on app backgrounding
Use "Increased Memory Limit" entitlement for larger models
Physical device required (no simulator support for Metal GPU)

See references/mlx-swift.md for full MLX Swift patterns and llama.cpp integration.

Multi-Backend Architecture

When an app needs multiple AI backends (e.g., Foundation Models + MLX fallback):

func respond(to prompt: String) async throws -> String {
    if SystemLanguageModel.default.isAvailable {
        return try await foundationModelsRespond(prompt)
    } else if canLoadMLXModel() {
        return try await mlxRespond(prompt)
    } else {
        throw AIError.noBackendAvailable
    }
}


Serialize all model access through a coordinator actor to prevent contention:

actor ModelCoordinator {
    func withExclusiveAccess<T>(_ work: () async throws -> T) async rethrows -> T {
        try await work()
    }
}

Performance Best Practices
Run outside debugger for accurate benchmarks (Xcode: Cmd-Opt-R, uncheck "Debug Executable")
Call session.prewarm() for Foundation Models before user interaction
Pre-compile Core ML models to .mlmodelc for faster loading
Use EnumeratedShapes over RangeDim for Neural Engine optimization
Use 4-bit palettization for best Neural Engine memory/latency gains
Batch Vision framework requests in a single perform() call
Use async prediction (iOS 17+) in Swift concurrency contexts
Neural Engine (Core ML) is most energy-efficient for compatible operations
Common Mistakes
No availability check. Calling LanguageModelSession() without checking SystemLanguageModel.default.availability crashes on unsupported devices.
No fallback UI. Users on pre-iOS 26 or devices without Apple Intelligence see nothing. Always provide a graceful degradation path.
Exceeding the context window. The token budget covers input + output. Monitor usage via tokenCount(for:) and summarize when needed.
Concurrent requests on one session. LanguageModelSession supports one request at a time. Check session.isResponding or serialize access.
Untrusted content in instructions. User input placed in the instructions parameter bypasses guardrail boundaries. Keep user content in the prompt.
Forgetting model.eval() before Core ML tracing. PyTorch models must be in eval mode before torch.jit.trace. Training-mode artifacts corrupt output.
Using neuralnetwork format. Always use mlprogram (.mlpackage) for new Core ML models. The legacy neuralnetwork format is deprecated.
Exceeding 60% RAM on iOS (MLX Swift). Large models cause OOM kills.
Running MLX in simulator. MLX requires Metal GPU -- use physical devices.
Not unloading models on background. Unload in scenePhase == .background.
Review Checklist
 Framework selection matches use case and target OS version
 Foundation Models: availability checked before every API call
 Foundation Models: graceful fallback when model unavailable
 Foundation Models: session prewarm called before user interaction
 Foundation Models: @Generable properties in logical generation order
 Foundation Models: token budget accounted for (check contextSize)
 Core ML: model format is mlprogram (.mlpackage) for iOS 15+
 Core ML: model.eval() called before tracing/exporting PyTorch models
 Core ML: minimum_deployment_target set explicitly
 Core ML: model accuracy validated after compression
 MLX Swift: model size appropriate for target device RAM
 MLX Swift: GPU cache limits set, models unloaded on backgrounding
 All model access serialized through coordinator actor
 Concurrency: model types and tool implementations are Sendable-conformant or @MainActor-isolated
 Physical device testing performed (not simulator)
References
Foundation Models API -- LanguageModelSession, @Generable, tool calling, prompt design
Core ML Conversion -- Model conversion from PyTorch, TensorFlow, other frameworks
Core ML Optimization -- Quantization, palettization, pruning, performance tuning
MLX Swift & llama.cpp -- MLX Swift patterns, llama.cpp integration, memory management
Weekly Installs
1.2K
Repository
dpearson2699/sw…s-skills
GitHub Stars
512
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn