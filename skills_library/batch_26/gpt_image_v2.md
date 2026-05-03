---
title: gpt-image-v2
url: https://skills.sh/eachlabs/skills/gpt-image-v2
---

# gpt-image-v2

skills/eachlabs/skills/gpt-image-v2
gpt-image-v2
Installation
$ npx skills add https://github.com/eachlabs/skills --skill gpt-image-v2
SKILL.md
GPT Image v2

OpenAI's GPT Image v2 on the EachLabs Predictions API. GPT Image v2 delivers higher-fidelity images than v1.5 with stronger prompt understanding, improved compositional consistency, physically accurate lighting, and enhanced fine-detail rendering — including reliable in-image text.

Two model slugs:

Slug	Category	Use
gpt-image-v2-text-to-image	Text to Image	Generate new images from a prompt
gpt-image-v2-edit	Image to Image	Edit an existing image with natural-language instructions
When to use
User asks for "GPT Image", "OpenAI image", "gpt-image-2", or the image model behind ChatGPT.
High-fidelity photorealism with accurate in-image text (posters, infographics, packaging, signage).
Brand-consistent product photography with legible labels and logos.
Instruction-following edits that must preserve the subject and layout of a reference image.

For a wider model comparison (Flux, Seedream, Imagen, etc.) see eachlabs-image-generation. For other edit models see eachlabs-image-edit.

Authentication
Header: X-API-Key: <your-api-key>


Set the EACHLABS_API_KEY environment variable. Get your key at eachlabs.ai/dashboard/api-keys.

Prediction Flow
(Recommended) Check schema — GET https://api.eachlabs.ai/v1/model?slug=gpt-image-v2-text-to-image to see the current request_schema. Do the same for gpt-image-v2-edit.
POST https://api.eachlabs.ai/v1/prediction with model, version: "0.0.1", and input.
Poll GET https://api.eachlabs.ai/v1/prediction/{id} until status is "success" or "error", or use a webhook.
Extract the output URLs from output (array).
Quick Start — Text to Image
curl -X POST https://api.eachlabs.ai/v1/prediction \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -d '{
    "model": "gpt-image-v2-text-to-image",
    "version": "0.0.1",
    "input": {
      "prompt": "A minimalist poster reading \"BREW LAB\" in bold serif, steam rising from a ceramic mug, warm paper texture, editorial photography"
    }
  }'


Typical processing time: ~40 seconds.

Quick Start — Edit
curl -X POST https://api.eachlabs.ai/v1/prediction \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -d '{
    "model": "gpt-image-v2-edit",
    "version": "0.0.1",
    "input": {
      "prompt": "Replace the background with a sunlit loft interior while keeping the product label and angle identical",
      "image_url": "https://your-cdn.example.com/product.jpg"
    }
  }'


Typical processing time: ~100 seconds. Reference images are always processed at high fidelity, so input image tokens (and cost) are higher than other GPT Image models.

Polling
curl https://api.eachlabs.ai/v1/prediction/{PREDICTION_ID} \
  -H "X-API-Key: $EACHLABS_API_KEY"

Status	Meaning
processing	Still running — poll again
success	Done — read output (array of URLs)
error	Failed — read message / details
Webhook (alternative to polling)

Pass "webhook_url": "https://your.host/path" in the create body. EachLabs POSTs:

{
  "exec_id": "prediction-uuid",
  "status": "succeeded",
  "output": "https://...",
  "error": ""
}


status is "succeeded" or "failed". Return 2xx within 30 seconds.

Pricing

Both models use dynamic token-based pricing:

Token type	Rate
Text input	$5 / 1M tokens
Image input	$10 / 1M tokens
Text output	$40 / 1M tokens
Image output	$30 / 1M tokens

If the token breakdown is unavailable, EachLabs falls back to a "medium 1024×1024 equivalent" rate.

gpt-image-v2-edit always processes reference images at high fidelity, so image-input tokens (and cost) run noticeably higher than with gpt-image-v1-5-edit or Nano Banana. Prefer downscaling references to 1024px on the long edge before upload unless you need high detail.

Prompt Tips
In-image text: wrap the exact copy in double quotes ("BREW LAB") and specify typography ("bold serif", "sans-serif headline"). v2 renders dense paragraphs and multilingual layouts reliably.
Composition: describe subject, framing, lens, and lighting separately. v2 respects compositional directives better than v1.5.
Edits: be specific about what must stay unchanged ("keep the label, angle, and lighting identical; only replace the background").
Photorealism: add concrete physical cues ("raking 45° sunlight, soft falloff, subtle skin SSS") rather than generic adjectives.
Rate Limits & Limits
Limit	Value
Create requests	100 / minute per key
Concurrent predictions	10 per key
File inputs	Publicly reachable HTTPS URLs only — no data-URIs, no localhost
Errors

Error body: { "status": "error", "message": "...", "details": "..." }

Code	Meaning
400	Invalid input
401	Missing / invalid X-API-Key
404	Unknown model or prediction id
429	Rate limited — back off
5xx	Retry with exponential backoff
Security Constraints
No arbitrary URL loading: image_url must point to your own HTTPS-reachable storage (S3, GCS, CDN). Do not forward user-pasted URLs without validation.
No third-party API tokens: never forward OpenAI / Anthropic / HF tokens through input — authentication is exclusively via the EachLabs API key.
Validate before calling: always resolve the live request_schema via GET /v1/model?slug=<slug> before constructing input. The schema is the source of truth.
Parameter Reference

See references/MODELS.md for the full per-slug parameter table.

Weekly Installs
18
Repository
eachlabs/skills
GitHub Stars
12
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass