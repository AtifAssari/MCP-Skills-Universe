---
title: youtube thumbnail generation
url: https://skills.sh/eachlabs/skills/youtube-thumbnail-generation
---

# youtube thumbnail generation

skills/eachlabs/skills/YouTube Thumbnail Generation
YouTube Thumbnail Generation
Installation
$ npx skills add https://github.com/eachlabs/skills --skill 'YouTube Thumbnail Generation'
SKILL.md
YouTube Thumbnail Generation

Generate high-converting YouTube thumbnails designed for maximum click-through rates. Create attention-grabbing visuals with expressive faces, bold colors, clear text spaces, and proven thumbnail formulas that drive views.

Overview

The each::sense API creates YouTube thumbnails optimized for engagement:

High CTR Designs: Thumbnails engineered for maximum click-through rates
Expressive Faces: Shocked, excited, curious, and emotional expressions that draw attention
Text Space: Clean areas for overlay text and titles
Bold Color Palettes: Bright, saturated colors that stand out in feeds
High Contrast: Sharp visual separation that pops at any size
1280x720 Resolution: Standard YouTube thumbnail dimensions
Quick Start
curl -X POST "https://eachsense-agent.core.eachlabs.run/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Generate a YouTube thumbnail: shocked face reaction to an unbelievable reveal, mouth wide open, eyes popping, bright yellow and red background, space on the right side for text overlay, dramatic lighting, ultra high contrast, 1280x720 aspect ratio"}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "max"
  }'

Thumbnail Styles
Style	Description	Key Elements
Reaction Face	Exaggerated emotional expressions	Wide eyes, open mouth, dramatic lighting
Before/After	Side-by-side transformation	Split composition, contrast between states
Listicle	Numbered list or top 10 format	Bold numbers, multiple elements arranged
Tutorial	How-to and educational content	Steps visualization, clean layout
Vlog	Personal and lifestyle content	Candid feel, warm colors, relatable
Gaming	Game-related content	Action scenes, game elements, energetic
Review	Product or service reviews	Product focus, rating visual, comparison
Use Case Examples
Reaction/Shocked Face Thumbnail

Classic YouTube thumbnail with exaggerated shocked expression.

curl -X POST "https://eachsense-agent.core.eachlabs.run/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Create a YouTube thumbnail with a person showing extreme shock and disbelief, jaw dropped, eyes wide open, hands on cheeks, bright neon pink and electric blue gradient background, dramatic side lighting creating shadows, space in the upper right corner for text, hyper-saturated colors, 1280x720 YouTube thumbnail format"}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "max"
  }'

Before/After Transformation Thumbnail

Split-screen showing dramatic transformation.

curl -X POST "https://eachsense-agent.core.eachlabs.run/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Generate a before and after YouTube thumbnail, split down the middle, left side showing a messy cluttered room in dull gray tones, right side showing the same room transformed into a beautiful organized space with warm golden lighting, red arrow pointing from left to right, high contrast, text space at top, 1280x720 aspect ratio"}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "max"
  }'

Tutorial Thumbnail with Steps

Educational content with clear step visualization.

curl -X POST "https://eachsense-agent.core.eachlabs.run/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Create a tutorial YouTube thumbnail showing someone at a computer with code on screen, confident helpful expression, pointing gesture toward the screen, clean modern workspace, teal and orange color scheme, large empty space on the left side for step numbers and text overlay, professional lighting, 1280x720 thumbnail dimensions"}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "max"
  }'

Vlog Style Thumbnail

Personal and authentic vlog aesthetic.

curl -X POST "https://eachsense-agent.core.eachlabs.run/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Generate a vlog YouTube thumbnail, person with genuine excited smile in an interesting location, travel destination background with beautiful scenery, warm golden hour lighting, candid natural pose, soft bokeh background, space at the bottom for text, lifestyle aesthetic, bright and inviting colors, 1280x720 format"}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "max"
  }'

Gaming Thumbnail

High-energy gaming content thumbnail.

curl -X POST "https://eachsense-agent.core.eachlabs.run/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Create an epic gaming YouTube thumbnail, intense gamer with headset showing competitive focus, RGB lighting in purple and green, gaming setup visible, action game scene explosion in background, dynamic diagonal composition, neon glow effects, bold and aggressive style, text space in corner, extremely vibrant colors, 1280x720 thumbnail"}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "max"
  }'

Product Review Thumbnail

Clear product-focused review thumbnail.

curl -X POST "https://eachsense-agent.core.eachlabs.run/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Generate a product review YouTube thumbnail, person holding a tech gadget with curious examining expression, clean white and blue gradient background, product prominently displayed, subtle star rating visual element, professional studio lighting, space on the right for review verdict text, crisp and clean aesthetic, 1280x720 aspect ratio"}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "max"
  }'

Listicle/Top 10 Thumbnail

Multiple elements for list-style content.

curl -X POST "https://eachsense-agent.core.eachlabs.run/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Create a top 10 listicle YouTube thumbnail, collage style with multiple small images arranged creatively, person with thoughtful counting gesture, bold red and yellow color scheme, large number 10 visual element, energetic diagonal layout, space for list title text at top, high saturation, eye-catching composition, 1280x720 thumbnail format"}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "max"
  }'

Comparison Thumbnail

Side-by-side product or concept comparison.

curl -X POST "https://eachsense-agent.core.eachlabs.run/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Generate a comparison YouTube thumbnail, VS battle style, two products or options facing each other from opposite sides, lightning bolt or versus symbol in the center, red versus blue color split background, dramatic confrontational lighting, person in the middle with confused deciding expression, text space at top and bottom, 1280x720 dimensions"}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "max"
  }'

Story Time Thumbnail

Engaging storytelling content thumbnail.

curl -X POST "https://eachsense-agent.core.eachlabs.run/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Create a story time YouTube thumbnail, person with dramatic secretive expression, finger over lips or whispering gesture, mysterious dark purple and black background with spotlight effect, intriguing shadowy elements suggesting the story topic, gossip or secret-sharing vibe, text space for story title on the side, dramatic theatrical lighting, 1280x720 thumbnail"}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "max"
  }'

Challenge Video Thumbnail

Action-packed challenge content.

curl -X POST "https://eachsense-agent.core.eachlabs.run/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Generate a challenge video YouTube thumbnail, person mid-action with determined intense expression, dynamic motion blur suggesting movement, bright orange and cyan color scheme, timer or countdown element, extreme angle shot, high energy chaotic composition, sweat and effort visible, bold space for challenge name text, 1280x720 aspect ratio"}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "max"
  }'

Best Practices for YouTube Thumbnails
Design Principles

Faces Drive Clicks: Include expressive human faces whenever possible. Emotions like shock, joy, curiosity, and disbelief perform best.

Exaggerate Emotions: Subtle expressions get lost. Go bigger with facial expressions than feels natural.

High Contrast: Thumbnails appear small in feeds. Strong contrast ensures visibility at any size.

Readable Text Space: Leave clean areas for text overlay. Busy backgrounds make text illegible.

Standard Dimensions: Always use 1280x720 pixels (16:9 aspect ratio) for optimal display.

Color Psychology: Bright yellows, reds, and blues grab attention. Avoid muted or dark color schemes.

Rule of Thirds: Position key elements along thirds for balanced, professional composition.

Consistent Branding: Maintain recognizable style elements across your channel thumbnails.

Prompt Tips

Craft effective prompts for maximum thumbnail impact:

# Include these elements in your prompts:

# 1. Expressive Faces
"shocked expression, wide eyes, open mouth, exaggerated emotion"

# 2. Bold Color Specifications
"bright neon colors, high saturation, vivid yellow and red, electric blue"

# 3. Clear Focal Point
"subject centered, attention directed to main element, clear visual hierarchy"

# 4. Text Space Planning
"space on the right for text overlay, clean area at top for title, uncluttered corner"

# 5. Lighting Direction
"dramatic side lighting, spotlight effect, high contrast shadows"

# 6. Aspect Ratio
"1280x720, YouTube thumbnail format, 16:9 aspect ratio"

# 7. Energy Level
"dynamic composition, diagonal lines, action and movement"

Mode Selection

Choose the appropriate mode based on your needs:

Max Mode (Recommended for Thumbnails)

Higher quality output ideal for final thumbnails.

curl -X POST "https://eachsense-agent.core.eachlabs.run/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Generate a professional YouTube thumbnail with maximum detail and quality, person with excited expression, vibrant colors, perfect for publishing"}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "max"
  }'

Eco Mode

Faster generation for rapid iteration and concept testing.

curl -X POST "https://eachsense-agent.core.eachlabs.run/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Quick thumbnail concept: shocked face, yellow background, text space right side"}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "eco"
  }'

Multi-Turn Sessions for Channel Consistency

Use session_id to maintain consistent style across multiple thumbnails for your channel.

Start a Thumbnail Session
curl -X POST "https://eachsense-agent.core.eachlabs.run/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "I am creating thumbnails for a tech review YouTube channel. The style should be: clean modern aesthetic, blue and white color scheme, product focus with reviewer face, professional lighting, consistent text placement on the right side. Generate the first thumbnail for a smartphone review."}],
    "model": "eachsense/beta",
    "stream": true,
    "session_id": "tech-channel-thumbnails-001",
    "mode": "max"
  }'

Continue with Consistent Style
curl -X POST "https://eachsense-agent.core.eachlabs.run/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Now create a thumbnail for a laptop review using the same channel style"}],
    "model": "eachsense/beta",
    "stream": true,
    "session_id": "tech-channel-thumbnails-001",
    "mode": "max"
  }'

Build a Thumbnail Series
curl -X POST "https://eachsense-agent.core.eachlabs.run/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Create the third thumbnail in this series for a headphones review, maintaining brand consistency"}],
    "model": "eachsense/beta",
    "stream": true,
    "session_id": "tech-channel-thumbnails-001",
    "mode": "max"
  }'

A/B Testing Variations

Generate multiple thumbnail variations to test which performs best.

Variation A: Emotion Focus
curl -X POST "https://eachsense-agent.core.eachlabs.run/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "YouTube thumbnail variation A: extreme shocked face taking up most of the frame, minimal background, pure emotional impact, red and yellow, text space bottom, 1280x720"}],
    "model": "eachsense/beta",
    "stream": true,
    "session_id": "ab-test-video-123",
    "mode": "max"
  }'

Variation B: Context Focus
curl -X POST "https://eachsense-agent.core.eachlabs.run/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "YouTube thumbnail variation B: same topic but showing more context and environment, smaller face with interesting background elements, blue and orange, text space top right, 1280x720"}],
    "model": "eachsense/beta",
    "stream": true,
    "session_id": "ab-test-video-123",
    "mode": "max"
  }'

Variation C: Minimalist Approach
curl -X POST "https://eachsense-agent.core.eachlabs.run/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "YouTube thumbnail variation C: clean minimalist design, single powerful visual element, bold solid color background, maximum contrast, text space centered, 1280x720"}],
    "model": "eachsense/beta",
    "stream": true,
    "session_id": "ab-test-video-123",
    "mode": "max"
  }'

Error Handling

Handle API responses appropriately in your applications.

# Check response status and handle errors
response=$(curl -s -w "\n%{http_code}" -X POST "https://eachsense-agent.core.eachlabs.run/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $EACHLABS_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "messages": [{"role": "user", "content": "Generate a YouTube thumbnail with shocked expression, bright colors, 1280x720"}],
    "model": "eachsense/beta",
    "stream": true,
    "mode": "max"
  }')

http_code=$(echo "$response" | tail -n1)
body=$(echo "$response" | sed '$d')

if [ "$http_code" -eq 200 ]; then
  echo "Thumbnail generated successfully"
  echo "$body"
elif [ "$http_code" -eq 401 ]; then
  echo "Error: Invalid API key"
elif [ "$http_code" -eq 429 ]; then
  echo "Error: Rate limit exceeded. Please wait before retrying."
else
  echo "Error: HTTP $http_code"
  echo "$body"
fi

Related Skills
Image Generation - General purpose image generation
Product Visuals - Product photography and visuals
Image Edit - Edit and enhance existing images
Weekly Installs
–
Repository
eachlabs/skills
GitHub Stars
12
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass