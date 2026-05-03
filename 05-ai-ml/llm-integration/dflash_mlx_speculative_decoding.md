---
title: dflash-mlx-speculative-decoding
url: https://skills.sh/aradotso/trending-skills/dflash-mlx-speculative-decoding
---

# dflash-mlx-speculative-decoding

skills/aradotso/trending-skills/dflash-mlx-speculative-decoding
dflash-mlx-speculative-decoding
Installation
$ npx skills add https://github.com/aradotso/trending-skills --skill dflash-mlx-speculative-decoding
SKILL.md
dflash-mlx Speculative Decoding

Skill by ara.so — Daily 2026 Skills collection.

DFlash implements lossless speculative decoding for MLX on Apple Silicon. A small draft model (~1B params) generates 16 tokens in parallel using block diffusion; the target model verifies all 16 in a single forward pass. Tokens are only emitted after target verification — output is lossless (every token is the target model's greedy argmax).

Typical speedups: 1.7x–4.1x over baseline mlx_lm depending on model size and context length. Acceptance rates hover around 87–90% for Qwen3.5 models.

Installation
pip install dflash-mlx

# or isolated install
pipx install dflash-mlx


Requires Python 3.10+, MLX 0.31.1+, Apple Silicon Mac.

Key CLI Commands
Generate text
# Auto-resolve draft model from registry
dflash --model Qwen/Qwen3.5-9B --prompt "Explain backpropagation"

# Explicit draft model
dflash --model Qwen/Qwen3.5-9B \
       --draft z-lab/Qwen3.5-9B-DFlash \
       --prompt "Explain backpropagation"

# Disable EOS (useful for benchmarking fixed token counts)
dflash --model Qwen/Qwen3.5-9B --prompt "..." --max-tokens 1024 --no-eos

OpenAI-compatible server
# Basic server
dflash-serve --model Qwen/Qwen3.5-9B --port 8000

# With explicit draft
dflash-serve --model Qwen/Qwen3.5-9B \
             --draft z-lab/Qwen3.5-9B-DFlash \
             --port 8000

# Disable thinking/reasoning tokens (Qwen3.5 thinking models)
dflash-serve --model Qwen/Qwen3.5-9B --port 8000 \
  --chat-template-args '{"enable_thinking": false}'

# Raise fallback threshold for longer prompts (large models)
dflash-serve --model mlx-community/Qwen3.5-35B-A3B-4bit --port 8000 \
  --chat-template-args '{"enable_thinking": false}' \
  --dflash-max-ctx 16384

Benchmark
dflash-benchmark \
  --model Qwen/Qwen3.5-9B \
  --draft z-lab/Qwen3.5-9B-DFlash \
  --prompt "The function f satisfies..." \
  --max-tokens 1024 \
  --repeat 3 \
  --no-eos


Outputs per-run JSON reports with tok/s, acceptance rate, and speedup vs baseline.

Supported Model Pairs
Target Model	Draft Model
Qwen/Qwen3.5-4B	z-lab/Qwen3.5-4B-DFlash
Qwen/Qwen3.5-9B	z-lab/Qwen3.5-9B-DFlash
mlx-community/Qwen3.5-27B-4bit	z-lab/Qwen3.5-27B-DFlash
mlx-community/Qwen3.5-35B-A3B-4bit	z-lab/Qwen3.5-35B-A3B-DFlash

Draft models are auto-resolved from a registry — no --draft flag needed for listed pairs. Models without a matching draft are rejected at startup.

Python API Usage
Streaming generation
from dflash_mlx import DFlashRuntime

runtime = DFlashRuntime.from_pretrained(
    model="Qwen/Qwen3.5-9B",
    draft="z-lab/Qwen3.5-9B-DFlash",  # optional, auto-resolved
)

prompt = "Explain the Pythagorean theorem step by step."

for token_text in runtime.stream_generate(
    prompt=prompt,
    max_tokens=512,
    use_chat_template=True,
):
    print(token_text, end="", flush=True)
print()

Full generation with stats
from dflash_mlx import DFlashRuntime

runtime = DFlashRuntime.from_pretrained(model="Qwen/Qwen3.5-9B")

result = runtime.generate(
    prompt="What is speculative decoding?",
    max_tokens=256,
    use_chat_template=True,
)

print(result.text)
print(f"Tokens/sec: {result.tokens_per_second:.2f}")
print(f"Acceptance rate: {result.acceptance_rate:.2%}")
print(f"Total tokens: {result.total_tokens}")

Custom draft block size and context
from dflash_mlx import DFlashRuntime, DFlashConfig

config = DFlashConfig(
    draft_block_size=16,      # tokens drafted per speculative step
    max_ctx=8192,             # max context length before fallback
    enable_tape_replay=True,  # GatedDeltaNet recurrent rollback
    jit_sdpa=True,            # custom Metal SDPA for long contexts
)

runtime = DFlashRuntime.from_pretrained(
    model="mlx-community/Qwen3.5-27B-4bit",
    config=config,
)

OpenAI client against dflash-serve
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="not-needed",  # dflash-serve does not require auth by default
)

# Non-streaming
response = client.chat.completions.create(
    model="Qwen/Qwen3.5-9B",
    messages=[
        {"role": "user", "content": "Explain gradient descent."}
    ],
    max_tokens=512,
)
print(response.choices[0].message.content)

# Streaming
stream = client.chat.completions.create(
    model="Qwen/Qwen3.5-9B",
    messages=[{"role": "user", "content": "Write a haiku about silicon."}],
    max_tokens=128,
    stream=True,
)
for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
print()

Tool calling (via dflash-serve)
import json
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="not-needed")

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name"},
                },
                "required": ["city"],
            },
        },
    }
]

response = client.chat.completions.create(
    model="Qwen/Qwen3.5-9B",
    messages=[{"role": "user", "content": "What's the weather in Tokyo?"}],
    tools=tools,
    tool_choice="auto",
)

tool_call = response.choices[0].message.tool_calls[0]
print(f"Function: {tool_call.function.name}")
print(f"Args: {json.loads(tool_call.function.arguments)}")

Common Patterns
Side-by-side demo (baseline vs DFlash)
PYTHONPATH=. python3 -m examples.demo --mode dflash \
  --target-model Qwen/Qwen3.5-9B \
  --draft-model z-lab/Qwen3.5-9B-DFlash \
  --prompt "Solve: f(x) + f(y) = f(x+y) - xy - 1" \
  --max-tokens 2048 \
  --no-eos

Integrating with Open WebUI
Start dflash-serve --model Qwen/Qwen3.5-9B --port 8000
In Open WebUI settings → Connections → add OpenAI API with URL http://localhost:8000/v1
Select model Qwen/Qwen3.5-9B in the chat UI

Works the same for Continue, aider, OpenCode, and any OpenAI-compatible client.

Override draft for unsupported models
# Force a custom draft — bypasses registry check
dflash --model my-org/MyCustomModel \
       --draft my-org/MyCustomModel-DFlash \
       --prompt "Hello"

Disable thinking tokens for Qwen3.5
# CLI
dflash --model Qwen/Qwen3.5-9B \
       --chat-template-args '{"enable_thinking": false}' \
       --prompt "What is 2+2?"

# Server
dflash-serve --model Qwen/Qwen3.5-9B \
             --chat-template-args '{"enable_thinking": false}' \
             --port 8000

Architecture Notes
Tape-replay rollback: For hybrid GatedDeltaNet + attention models (Qwen3.5), dflash records an innovation tape during verify and replays only accepted steps via a custom Metal kernel — avoids full state snapshots.
JIT SDPA 2-pass: For contexts ≥ 1024 tokens, a custom Metal attention kernel maintains numerical alignment with stock MLX attention.
Greedy acceptance: Keeps the longest correct prefix from the 16 drafted tokens, rejects the rest. No temperature/sampling on verification — strictly lossless.
Qwen3 (pure attention) models work but don't benefit from tape-replay rollback (that's GatedDeltaNet-specific).
Troubleshooting

Model rejected at startup

Error: No DFlash draft found for model 'org/ModelName'


→ Pass --draft org/ModelName-DFlash explicitly, or use a model from the supported pairs table.

Low acceptance rate (< 80%)

Usually caused by very long context (4096+). Try --dflash-max-ctx 8192 to extend the fallback threshold.
Qwen3 (non-3.5) models have lower acceptance than Qwen3.5 hybrid models.

Numerical divergence / output differs from pure AR

Expected behavior: "Output can still differ from pure AR because of MLX dispatch divergence, but no unverified token is ever emitted."
If outputs seem wrong (not just different), ensure MLX 0.31.1+ is installed: python -c "import mlx; print(mlx.__version__)"

Server not accepting connections

# Check port is not in use
lsof -i :8000

# Bind to all interfaces for network access
dflash-serve --model Qwen/Qwen3.5-9B --port 8000 --host 0.0.0.0


Out of memory with large models

Use 4-bit quantized variants: mlx-community/Qwen3.5-27B-4bit instead of the full model.
The draft model loads alongside the target — budget ~1–2GB extra for the draft.

Benchmark results JSON location

ls benchmark/results/
# Per-run JSON with tok/s, acceptance rate, repeat measurements

Weekly Installs
225
Repository
aradotso/trending-skills
GitHub Stars
42
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass