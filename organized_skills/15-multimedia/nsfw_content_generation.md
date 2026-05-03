---
rating: ⭐⭐⭐
title: nsfw-content-generation
url: https://skills.sh/eachlabs/skills/nsfw-content-generation
---

# nsfw-content-generation

skills/eachlabs/skills/nsfw-content-generation
nsfw-content-generation
Installation
$ npx skills add https://github.com/eachlabs/skills --skill nsfw-content-generation
SKILL.md
NSFW Content Generation with each::sense

Generate adult and mature content using each::sense API with the safety checker disabled. This skill enables creation of artistic nude, glamour photography, boudoir, fantasy art, and other adult-themed visual content.

Features:

Artistic nude and figure photography
Glamour and boudoir photography
Fantasy and pin-up art
Mature-themed character generation
Consistent character across multiple generations via session_id
Full creative control with no content filtering
Authentication
Header: X-API-Key: <your-api-key>


Get your API key at eachlabs.ai -> API Keys.

Set the EACHLABS_API_KEY environment variable.

Base URL
https://eachsense-agent.core.eachlabs.run

Quick Start
curl -X POST https://eachsense-agent.core.eachlabs.run/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Generate an artistic nude portrait with renaissance painting style, soft dramatic lighting"}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "max",
    "enable_safety_checker": false
  }'


The endpoint returns Server-Sent Events (SSE) with real-time progress and the final generated output.

Content Types
Type	Description	Example Prompt Keywords
Artistic Nude	Fine art style nude photography/paintings	classical, renaissance, figure study, artistic
Glamour	Sophisticated adult modeling	glamour, elegant, sensual, fashion
Boudoir	Intimate bedroom photography style	boudoir, intimate, romantic, soft light
Pin-Up	Retro/vintage style pin-up art	pin-up, retro, vintage, playful
Fantasy	Fantasy-themed adult art	fantasy, ethereal, mythological, magical
Cinematic	Movie/film style mature scenes	cinematic, dramatic, moody, film still
Fine Art	Museum-quality artistic compositions	fine art, gallery, sculptural, classical
Editorial	Magazine/editorial style content	editorial, fashion, high-end, professional
Request Schema
{
  "messages": [{"role": "user", "content": "string (required) - Content description"}],
  "model": "eachsense/beta",
  "session_id": "string (optional) - Session ID for consistent characters",
  "mode": "string (optional, default: 'max') - Quality mode: 'max' or 'eco'",
  "image_urls": "array[string] (optional) - Reference images",
  "enable_safety_checker": "boolean (required for NSFW) - Set to false"
}

Key Parameters
Parameter	Type	Default	Description
message	string	required	Natural language content description
session_id	string	null	Use for consistent characters across generations
mode	string	"max"	max = best quality, eco = faster/cheaper
image_urls	array	null	Reference images for style/pose guidance
enable_safety_checker	boolean	true	Must be set to false for NSFW content
Use Case Examples
1. Artistic Nude Portrait
curl -X POST https://eachsense-agent.core.eachlabs.run/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Generate an artistic nude portrait of a woman, renaissance painting style, soft chiaroscuro lighting, classical pose reminiscent of Botticelli, fine art gallery quality"}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "max",
    "enable_safety_checker": false
  }'

2. Glamour Photography
curl -X POST https://eachsense-agent.core.eachlabs.run/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Generate a glamour photography shot, elegant woman in silk lingerie, luxurious bedroom setting, soft golden hour lighting through sheer curtains, high-end fashion magazine quality"}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "max",
    "enable_safety_checker": false
  }'

3. Boudoir Photography
curl -X POST https://eachsense-agent.core.eachlabs.run/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Generate an intimate boudoir photograph, woman on a vintage chaise lounge, romantic candlelit atmosphere, soft focus, warm skin tones, tasteful and elegant composition"}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "max",
    "enable_safety_checker": false
  }'

4. Fantasy Art
curl -X POST https://eachsense-agent.core.eachlabs.run/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Generate a fantasy art scene, elven queen in a moonlit forest glade, ethereal beauty, flowing translucent fabrics, magical atmosphere with floating lights, sensual and mystical"}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "max",
    "enable_safety_checker": false
  }'

5. Vintage Pin-Up Style
curl -X POST https://eachsense-agent.core.eachlabs.run/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Generate a 1950s style pin-up illustration, playful pose, retro swimsuit, classic Vargas girl aesthetic, vibrant colors, vintage americana style"}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "max",
    "enable_safety_checker": false
  }'

6. Fine Art Figure Study
curl -X POST https://eachsense-agent.core.eachlabs.run/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Generate a classical figure study, graceful female form, marble sculpture aesthetic, dramatic studio lighting, museum quality fine art, anatomically elegant"}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "max",
    "enable_safety_checker": false
  }'

7. Cinematic Sensual Scene
curl -X POST https://eachsense-agent.core.eachlabs.run/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Generate a cinematic film still, intimate moment between lovers, noir lighting with venetian blind shadows, moody atmosphere, art house film aesthetic"}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "max",
    "enable_safety_checker": false
  }'

8. Editorial Fashion Nude
curl -X POST https://eachsense-agent.core.eachlabs.run/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Generate a high fashion editorial photograph, artistic partial nude, avant-garde styling with dramatic jewelry, stark white studio background, Helmut Newton inspired composition"}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "max",
    "enable_safety_checker": false
  }'

9. Consistent Character Series (Multi-Turn)

Use session_id to maintain character consistency across multiple generations:

# First image - establish character
curl -X POST https://eachsense-agent.core.eachlabs.run/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Generate a glamour portrait, woman with long auburn hair, green eyes, elegant features, wearing a silk robe, soft window lighting"}],
    "model": "eachsense/beta",
    "session_id": "glamour-series-001",
    "mode": "max",
    "model": "eachsense/beta",
    "stream": true,
    "enable_safety_checker": false
  }'

# Second image - same character, different scene
curl -X POST https://eachsense-agent.core.eachlabs.run/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Generate the same woman from the previous image, now in an outdoor setting, sheer summer dress, golden hour beach scene"}],
    "model": "eachsense/beta",
    "session_id": "glamour-series-001",
    "mode": "max",
    "model": "eachsense/beta",
    "stream": true,
    "enable_safety_checker": false
  }'

# Third image - same character, artistic pose
curl -X POST https://eachsense-agent.core.eachlabs.run/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Generate the same woman in an artistic nude pose, classical sculpture aesthetic, studio lighting"}],
    "model": "eachsense/beta",
    "session_id": "glamour-series-001",
    "mode": "max",
    "model": "eachsense/beta",
    "stream": true,
    "enable_safety_checker": false
  }'

10. Reference-Based Generation

Use image_urls to provide style or pose references:

curl -X POST https://eachsense-agent.core.eachlabs.run/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Generate a glamour photograph matching the pose and lighting style from this reference image, but with a different model and setting"}],
    "model": "eachsense/beta",
    "image_urls": ["https://example.com/reference-pose.jpg"],
    "mode": "max",
    "model": "eachsense/beta",
    "stream": true,
    "enable_safety_checker": false
  }'

Mode Selection
MAX Mode (Recommended for NSFW)

Uses the highest quality models for detailed, refined output. Best for final content and publication-ready images.

curl -X POST https://eachsense-agent.core.eachlabs.run/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Generate artistic boudoir photography..."}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "max",
    "enable_safety_checker": false
  }'

ECO Mode

Faster and more cost-effective. Good for testing prompts and generating drafts.

curl -X POST https://eachsense-agent.core.eachlabs.run/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Generate artistic boudoir photography..."}],
    "model": "eachsense/beta",
    "mode": "eco",
    "model": "eachsense/beta",
    "stream": true,
    "enable_safety_checker": false
  }'

Best Practices
Artistic Approach
Use artistic terminology - Reference fine art, photography styles, and classical aesthetics
Describe lighting - Chiaroscuro, golden hour, soft diffused, dramatic shadows
Reference art movements - Renaissance, Baroque, Art Nouveau, contemporary
Emphasize composition - Rule of thirds, leading lines, negative space
Quality Prompts
Be descriptive - Include setting, mood, lighting, and artistic style
Use quality modifiers - "gallery quality," "high-end editorial," "museum-worthy"
Specify camera details - Depth of field, focal length, lens characteristics
Define mood - Romantic, dramatic, playful, mysterious, elegant
Content Guidelines
Artistic intent - Frame requests as art or professional photography
Consent themes - All generated content depicts fictional, consenting adults
Platform compliance - Ensure generated content meets your platform's policies
Commercial use - Review EachLabs terms for commercial usage rights
Prompt Tips

Effective prompt structure:

[Subject description] + [Setting/environment] + [Lighting] + [Style/aesthetic] + [Quality modifiers]


Example:

"Elegant woman with flowing dark hair + luxurious marble bathroom setting +
soft candlelight with warm reflections + Helmut Newton inspired glamour +
fashion magazine quality, 8K, detailed"

Age Verification Disclaimer

This API feature is intended for adult users only. By using enable_safety_checker: false, you acknowledge that:

You are of legal age in your jurisdiction to view and create adult content
You will not generate content depicting minors
You will comply with all applicable laws regarding adult content
You assume responsibility for the appropriate use and distribution of generated content
Generated content is fictional and does not represent real individuals unless you have explicit consent
Error Handling
Common Errors
Error Message	Cause	Solution
Safety check failed	Forgot to disable safety checker	Add `"model": "eachsense/beta",
"stream": true,
"enable_safety_checker": false` |


| Failed to create prediction: HTTP 422 | Insufficient balance | Top up at eachlabs.ai | | Invalid API key | Missing/wrong API key | Check EACHLABS_API_KEY | | Rate limit exceeded | Too many requests | Wait and retry |

Timeout Settings

For complex generations, increase your timeout:

curl --max-time 600 -X POST https://eachsense-agent.core.eachlabs.run/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Generate detailed artistic content..."}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "max",
    "enable_safety_checker": false
  }'

SSE Response Format

The endpoint returns Server-Sent Events (SSE) with real-time updates.

Key events to monitor:

Event	Description
thinking_delta	AI reasoning in real-time
status	Current operation status
generation_response	Generated image URL
complete	Final event with all outputs
error	Error information

See SSE-EVENTS.md for complete event documentation.

Related Skills
each-sense - General purpose content generation
ai-influencer-generation - Consistent character creation
eachlabs-image-generation - Standard image generation
Weekly Installs
87
Repository
eachlabs/skills
GitHub Stars
12
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketFail
SnykWarn