---
title: veo-3.1-prompting
url: https://skills.sh/apexdiscordy/veo3.1-prompting/veo-3.1-prompting
---

# veo-3.1-prompting

skills/apexdiscordy/veo3.1-prompting/veo-3.1-prompting
veo-3.1-prompting
Installation
$ npx skills add https://github.com/apexdiscordy/veo3.1-prompting --skill veo-3.1-prompting
SKILL.md
Veo 3.1 Prompting
Core Capabilities

Veo 3.1 generates video with native audio synthesis and advanced physical realism. Key specifications:

Resolutions: 720p, 1080p, or 4K
Aspect Ratios: 16:9 (landscape) or 9:16 (portrait)
Duration: 4, 6, or 8 seconds per generation (billed as 8s minimum)
Framerate: 24 FPS (cinematic standard)
Native Audio: Dialogue, ambient sound, and music synchronized to video
Reference Images: Up to 3 images for character/style consistency ("Ingredients to Video")
Advanced Controls: First/Last Frame interpolation, Timestamp Prompting for multi-shot narratives
The Five-Part Formula

Structure every prompt in this order:

[Cinematography] + [Subject] + [Action] + [Context] + [Style & Audio]

Example:

Tracking shot following a weathered fisherman mending nets on a wooden dock. Golden hour sun flares through rigging. Salt spray visible in air. Cinematic 35mm film grain. Sound: seagulls crying, rope creaking, gentle waves.

Critical: Lead with camera movement. Veo 3.1 weights early tokens heavily.

1. Cinematography Specifications

Always specify shot type, camera movement, and lens characteristics first.

Shot Framing

Extreme close-up, Close-up, Medium shot, Wide establishing shot
Over-the-shoulder, POV, Bird's eye view, Worm's eye view

Camera Movement (See camera-techniques.md)

Linear: Dolly in/out, Tracking shot, Pan, Tilt, Truck
Dynamic: Handheld, Gimbal smooth, Whip pan, Rack focus
Aerial: Drone descending, Orbit clockwise, Crane up

Lens & Focus

Shallow depth of field with creamy bokeh
Deep focus everything sharp
Anamorphic lens with horizontal flares
Macro lens for extreme detail
2. Subject Specification

Describe subjects with exhaustive visual detail for consistency:

Character Anchors (Essential for multi-clip consistency)

Physical: "Elderly man, silver hair cropped short, weathered face with scar above left eyebrow"
Clothing: "Faded navy pea coat, brass buttons tarnished, wool scarf with fringe"
Distinctive markers: "Red-rimmed glasses", "tattoo of anchor on forearm", "gold pocket watch chain"

Object Details

Material and condition: "Brushed titanium, fingerprint-smudged", "distressed leather with patina"
Interaction points: "Steam rising from ceramic rim", "condensation beads on cold glass"
3. Action & Physics

Use dynamic verbs demonstrating physical interaction:

Motion quality: strides confidently, shuffles nervously, explodes outward, cascades smoothly
Physics indicators: realistic water displacement, accurate gravity, cloth simulation, hair physics
Temporal markers: gradually accelerating, suddenly freezing, continuously swirling

Physics Strengths: Fluid dynamics, fire/smoke, fabric movement, particle systems (dust, snow, sparks).

4. Context & Atmosphere

Establish environment and mood:

Lighting

Time: dawn blue hour, golden hour, harsh midday, neon-lit night
Quality: volumetric god rays, chiaroscuro shadows, soft diffused overcast, practical lamp light
Effects: lens flare, bloom, atmospheric haze

Environment

Spatial: cramped interior, vast open landscape, claustrophobic corridor
Weather: rain-streaked windows, fog-choked streets, snow-dusted
5. Style & Audio Synthesis

Visual Style (See style-reference.md)

Genre: cinematic noir, BBC Earth documentary, Pixar 3D animation, vintage 16mm
Color: teal and orange blockbuster grade, bleach bypass desaturated, vibrant anime saturation
Texture: film grain 35mm, digital sharpness, VHS tracking lines

Native Audio (See audio-synthesis.md)

Dialogue: "Smooth baritone voice: 'The package has arrived.'"
Ambient: "Coffee shop murmur, ceramic cup placed on saucer"
Effects: "Satisfying mechanical keyboard clack", "metallic slide and lock"
Music: "Tense strings building to crescendo", "lo-fi hip hop beat 80bpm"

Audio Sync Tips

Time dialogue: "At 2-second mark, character speaks"
Match motion: "Music swells as camera pushes in"
Layer sounds: "Base ambiance, then specific Foley, then dialogue"
Advanced Workflows
Ingredients to Video (Character Consistency)

Use when maintaining characters across multiple clips:

Upload 1-3 reference images (character face, outfit, environment)
Prompt structure: "Same woman from reference image, now walking through rainy Tokyo street. Maintaining red leather jacket and bob haircut."
Keep anchors consistent: "Same scar on cheek, same gold hoop earrings"
First & Last Frame Interpolation

Create specific transitions:

Describe starting state: "Sealed envelope on mahogany desk"
Describe ending state: "Open envelope, letter partially pulled out, handwritten text visible"
Veo generates smooth 8-second transition between states
Use for: reveals, transformations, camera moves through portals
Timestamp Prompting (Multi-Shot Narrative)

Break 8 seconds into precise segments for narrative control:

0-2s: Wide shot of empty desert highway, heat shimmer rising
2-4s: Close-up of motorcycle speedometer needle climbing
4-6s: Tracking shot of rider leaning into turn, dust cloud trailing
6-8s: Wide shot motorcycle disappearing into sunset, engine roar fading
Model Selection
Model	Speed	Use Case
veo-3.1-generate-001	Standard	High-quality commercial content, final delivery
veo-3.1-fast-generate-001	Fast	Rapid iteration, social media drafts, testing compositions
Structured Prompting (JSON)

For complex commercial workflows, use JSON structure:

{
  "project_meta": {
    "aspect_ratio": "16:9",
    "resolution": "1080p",
    "model": "veo-3.1-generate-001"
  },
  "scene": {
    "cinematography": "Macro lens, slow orbit 360 degrees",
    "subject": "Artisan coffee cup, steam rising in spiral patterns",
    "action": "Hand enters frame, gentle grip, lifting slowly",
    "context": "Minimalist white studio, softbox lighting from above",
    "style": "Premium commercial aesthetic, shallow depth of field",
    "audio": "Ceramic on ceramic sound, gentle sip, ambient cafe hum"
  },
  "timeline": [
    {"time": "0-3s", "focus": "Product detail, steam physics"},
    {"time": "3-6s", "focus": "Hand interaction, human element"},
    {"time": "6-8s", "focus": "Logo reveal, satisfying audio punctuate"}
  ]
}

Technical Constraints
Prompt limit: 2,000 characters
Image input: Maximum 20MB (JPEG/PNG) for Ingredients to Video
Audio: Generate natively or add post-production; Veo audio works best with clear, brief dialogue (1-2 sentences max)
Text rendering: Veo struggles with legible text; avoid critical text overlays or specify "stylized unreadable text"
Concurrent requests: 50 per minute per region (free tier)
Troubleshooting
Issue	Solution
Blurry motion	Add "sharp motion capture, 1/1000s shutter freeze" or "slow-motion 240fps"
Character inconsistency	Use Ingredients to Video with reference images; anchor with unique clothing/jewelry
Unwanted morphing	Specify rigidity: "maintains solid form", "no deformation"; use negative prompting
Physics look artificial	Explicitly state "realistic physics", "accurate weight and momentum"
Audio out of sync	Use timestamp markers: "dialogue starts at 2s", "sound matches impact at 4s"
Flat lighting	Specify contrast: "dramatic side lighting", "deep shadows", "rim light separation"
Boring composition	Lead with dynamic camera: "whip pan", "aggressive tracking shot", "rapid dolly in"
When to Load References
Task	Resource
Camera movement vocabulary	camera-techniques.md
Visual styles and color grading	style-reference.md
Genre-specific templates	prompt-patterns.md
Audio generation techniques	audio-synthesis.md
Copy-paste templates	assets/prompt-templates/
Camera Techniques for Veo 3.1

Veo 3.1 excels at film grammar and camera movement. Precise terminology yields better motion control.

Movement Types
Linear Motion
Term	Description	Best For
Dolly in/out	Physical camera movement toward/away subject	Emotional reveals, focus shifts
Tracking shot	Camera moves parallel to subject	Following subjects, dynamic action
Truck left/right	Horizontal lateral movement	Revealing environments
Pedestal up/down	Vertical movement without angle change	Elevating reveals
Crane up/down	Sweeping vertical arc	Epic scale reveals
Push-in	Zoom while maintaining perspective	Intensifying moments
Rotational Motion
Term	Description	Best For
Pan left/right	Horizontal rotation, fixed position	Scanning landscapes, following movement
Tilt up/down	Vertical rotation, fixed position	Revealing height, vertical subjects
Orbit clockwise/counter-clockwise	360° circular path around subject	Product showcases, dramatic encirclement
Dutch angle	Tilted horizon	Disorientation, tension, stylized action
Dynamic Techniques
Term	Description	Best For
Handheld	Slight organic jitter	Documentary realism, urgency
Gimbal smooth	Stabilized fluid motion	Cinematic tracking, luxury aesthetic
Whip pan	Fast blur transition between subjects	Energy, scene transitions
Rack focus	Shifts focal plane between foreground/background	Narrative focus shifts, depth emphasis
Slow push-in	Gradual camera advance	Contemplative, intimate moments
Shot Framing Hierarchy

Prefix camera moves with framing:

Extreme close-up — Detail only (eyes, texture)
Close-up — Head and shoulders
Medium shot — Waist up
Wide shot — Full subject with environment
Extreme wide/Establishing — Environment dominant
Over-the-shoulder — Dialogue scenes
POV (Point of view) — Immersive perspective
Bird's eye view — Top-down, detachment
Worm's eye view — Looking up, empowerment/intimidation
Speed and Time Modifiers
Slow-motion 240fps — Smooth, detailed action
Real-time 24fps — Natural motion
Time-lapse — Compressed time, clouds, construction
Hyperlapse — Moving time-lapse
Staccato/jerky motion — Uneven, mechanical, horror
Lens Characteristics

Include to control optical personality:

Anamorphic lens — Horizontal flares, oval bokeh, cinematic width
Wide angle 16mm — Distortion, expansive space
Telephoto 85mm — Compressed space, portrait perspective
Macro lens — Extreme close focus, shallow depth
Fisheye — Spherical distortion, extreme wide
Vintage lens — Softness, chromatic aberration, character
Example Combinations

Extreme close-up of eye, slow push-in, rack focus to reflection in iris, anamorphic flares

Wide establishing shot, crane down through clouds to reveal mountain valley, golden hour lighting

Handheld medium shot following subject through crowded market, whip pan to street sign

Weekly Installs
43
Repository
apexdiscordy/ve…rompting
First Seen
Feb 22, 2026