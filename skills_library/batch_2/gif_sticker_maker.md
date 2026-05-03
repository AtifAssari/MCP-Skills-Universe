---
title: gif-sticker-maker
url: https://skills.sh/minimax-ai/skills/gif-sticker-maker
---

# gif-sticker-maker

skills/minimax-ai/skills/gif-sticker-maker
gif-sticker-maker
Installation
$ npx skills add https://github.com/minimax-ai/skills --skill gif-sticker-maker
SKILL.md
GIF Sticker Maker

Convert user photos into 4 animated GIF stickers (Funko Pop / Pop Mart style).

Style Spec
Funko Pop / Pop Mart blind box 3D figurine
C4D / Octane rendering quality
White background, soft studio lighting
Caption: black text + white outline, bottom of image
Prerequisites

Before starting any generation step, ensure:

Python venv is activated with dependencies from requirements.txt installed
MINIMAX_API_KEY is exported (e.g. export MINIMAX_API_KEY='your-key')
ffmpeg is available on PATH (for Step 3 GIF conversion)

If any prerequisite is missing, set it up first. Do NOT proceed to generation without all three.

Workflow
Step 0: Collect Captions

Ask user (in their language):

"Would you like to customize the captions for your stickers, or use the defaults?"

Custom: Collect 4 short captions (1–3 words). Actions auto-match caption meaning.
Default: Look up captions table by detected user language. Never mix languages.
Step 1: Generate 4 Static Sticker Images

Tool: scripts/minimax_image.py

Analyze the user's photo — identify subject type (person / animal / object / logo).
For each of the 4 stickers, build a prompt from image-prompt-template.txt by filling {action} and {caption}.
If subject is a person: pass --subject-ref <user_photo_path> so the generated figurine preserves the person's actual facial likeness.
Generate (all 4 are independent — run concurrently):
python3 scripts/minimax_image.py "<prompt>" -o output/sticker_hi.png --ratio 1:1 --subject-ref <photo>
python3 scripts/minimax_image.py "<prompt>" -o output/sticker_laugh.png --ratio 1:1 --subject-ref <photo>
python3 scripts/minimax_image.py "<prompt>" -o output/sticker_cry.png --ratio 1:1 --subject-ref <photo>
python3 scripts/minimax_image.py "<prompt>" -o output/sticker_love.png --ratio 1:1 --subject-ref <photo>


--subject-ref only works for person subjects (API limitation: type=character). For animals/objects/logos, omit the flag and rely on text description.

Step 2: Animate Each Image → Video

Tool: scripts/minimax_video.py with --image flag (image-to-video mode)

For each sticker image, build a prompt from video-prompt-template.txt, then:

python3 scripts/minimax_video.py "<prompt>" --image output/sticker_hi.png -o output/sticker_hi.mp4
python3 scripts/minimax_video.py "<prompt>" --image output/sticker_laugh.png -o output/sticker_laugh.mp4
python3 scripts/minimax_video.py "<prompt>" --image output/sticker_cry.png -o output/sticker_cry.mp4
python3 scripts/minimax_video.py "<prompt>" --image output/sticker_love.png -o output/sticker_love.mp4


All 4 calls are independent — run concurrently.

Step 3: Convert Videos → GIF

Tool: scripts/convert_mp4_to_gif.py

python3 scripts/convert_mp4_to_gif.py output/sticker_hi.mp4 output/sticker_laugh.mp4 output/sticker_cry.mp4 output/sticker_love.mp4


Outputs GIF files alongside each MP4 (e.g. sticker_hi.gif).

Step 4: Deliver

Output format (strict order):

Brief status line (e.g. "4 stickers created:")
<deliver_assets> block with all GIF files
NO text after deliver_assets
<deliver_assets>
<item><path>output/sticker_hi.gif</path></item>
<item><path>output/sticker_laugh.gif</path></item>
<item><path>output/sticker_cry.gif</path></item>
<item><path>output/sticker_love.gif</path></item>
</deliver_assets>

Default Actions
#	Action	Filename ID	Animation
1	Happy waving	hi	Wave hand, slight head tilt
2	Laughing hard	laugh	Shake with laughter, eyes squint
3	Crying tears	cry	Tears stream, body trembles
4	Heart gesture	love	Heart hands, eyes sparkle

See references/captions.md for multilingual caption defaults.

Rules
Detect user's language, all outputs follow it
Captions MUST come from captions.md matching user's language column — never mix languages
All image prompts must be in English regardless of user language (only caption text is localized)
<deliver_assets> must be LAST in response, no text after
Weekly Installs
931
Repository
minimax-ai/skills
GitHub Stars
11.5K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass