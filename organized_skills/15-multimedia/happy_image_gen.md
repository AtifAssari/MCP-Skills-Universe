---
rating: ⭐⭐
title: happy-image-gen
url: https://skills.sh/iamzhihuix/happy-claude-skills/happy-image-gen
---

# happy-image-gen

skills/iamzhihuix/happy-claude-skills/happy-image-gen
happy-image-gen
Installation
$ npx skills add https://github.com/iamzhihuix/happy-claude-skills --skill happy-image-gen
SKILL.md
happy-image-gen

Generates still images across 8 providers through one CLI: bun scripts/main.ts .... The same CLI handles text-to-image and image-to-image (reference-driven) edits.

Quick usage
bun scripts/main.ts --prompt "A calico cat on green grass, cinematic light" --ar 16:9 --image ./out.png

When to invoke this skill

Invoke this skill whenever the user:

Asks to generate, create, draw, render, illustrate, or synthesize an image from text.
Asks to restyle or transform an existing image they provide a path to.
Names any image-generation model (DALL·E, gpt-image, Flux, SDXL, Gemini Image, Imagen, Seedream, Kolors, Wanx, Stable Diffusion) without specifying 即梦/Dreamina/Jimeng.

Route to happy-dreamina instead when the user explicitly names 即梦, Jimeng, or the dreamina CLI.

Step 0: Preflight (BLOCKING — run before any generation)

Run these checks:

Locate EXTEND.md config. Check in order:

./.happy-skills/happy-image-gen/EXTEND.md (project)
$XDG_CONFIG_HOME/happy-skills/happy-image-gen/EXTEND.md
~/.happy-skills/happy-image-gen/EXTEND.md (user)

If none exist, run bun scripts/main.ts --setup and follow references/config/first-time-setup.md to create one. Do not proceed to generation until the user has at least one provider configured.

Verify a provider is usable. Confirm either an env var is set (e.g., OPENAI_API_KEY) or EXTEND.md references an api_key_env / api_key_source that resolves. If nothing resolves, loop back to setup.

Verify Bun is available. Run command -v bun. If missing, fall back to npx -y bun scripts/main.ts ....

Step 1: Choose a provider

Pick in this order of preference:

--provider <id> explicitly passed by the user.
The default_provider in EXTEND.md.
The first provider whose API key is present in the environment. Priority when auto-detecting: openai → google → replicate → stability → fal → ark → bailian → siliconflow.

See references/providers.md for each provider's required env vars, default models, and strengths (e.g., prefer google for text-in-image, replicate for Flux-family photorealism, ark for Chinese text fidelity).

Step 2: Fill in parameters
--prompt: the user's full request, trimmed. Always double-quote.
--ar: aspect ratio — 1:1 / 16:9 / 9:16 / 3:4 / 4:3. See references/aspect_ratio_map.md for how each provider interprets this.
--quality: draft (fastest + cheapest), hd (default), or ultra (4K-class, slower).
--ref <path>: repeat for multiple reference images. Not every provider supports this — see providers.md.
--model: override the default model for the chosen provider. Omit unless the user asked for a specific one.
--image <path>: REQUIRED — output file path. Use a descriptive name (e.g., ./out/hero-landscape.png).
Step 3: Run
bun scripts/main.ts \
  --prompt "..." \
  --image ./out.png \
  --provider openai \
  --ar 1:1 \
  --quality hd


On success the CLI prints the resolved absolute path and byte count. In --json mode it emits:

{ "success": true, "provider": "openai", "model": "gpt-image-1", "image": "/abs/path.png", "size_bytes": 1416341, "format": "png" }


Echo the path back to the user.

Step 4: Handle errors
config: No provider selected ... — no API key in env and no EXTEND.md. Loop back to Step 0.
[openai] OpenAI images API 401 ... — key invalid or expired. Ask the user to refresh it.
[openai] ... 400 ... content_policy_violation — prompt blocked. Show the raw error to the user; do not paraphrase.
Timeouts / network errors — retry once. If still failing, surface the raw message and provider so the user knows what to check.

See references/error_codes.md for a per-provider error table.

References

Read on demand:

references/providers.md — all 8 providers, required env vars, default models, strengths.
references/aspect_ratio_map.md — how each provider interprets --ar.
references/error_codes.md — common errors per provider and fixes.
references/config/first-time-setup.md — step-by-step for --setup.
references/config/extend-schema.md — EXTEND.md schema reference.

Template for EXTEND.md: assets/EXTEND.template.md.

Weekly Installs
9
Repository
iamzhihuix/happ…e-skills
GitHub Stars
284
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass