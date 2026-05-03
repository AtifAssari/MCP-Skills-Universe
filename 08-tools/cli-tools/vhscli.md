---
rating: ⭐⭐⭐
title: vhscli
url: https://skills.sh/getvhs/vhscli-skills/vhscli
---

# vhscli

skills/getvhs/vhscli-skills/vhscli
vhscli
Installation
$ npx skills add https://github.com/getvhs/vhscli-skills --skill vhscli
SKILL.md
vhscli

vhscli is a command-line tool for multimodal AI: chat about text/images/video/pdfs, or generate images and videos from prompts. It's a thin client — auth, uploads, and model execution all happen server-side, so users don't store any provider API keys locally.

Run vhscli --help or vhscli <command> --help to see current help — the CLI is the source of truth.

Invocation

Always run via npx @getvhs/vhscli@latest so you pick up the newest models, flags, and fixes. Don't pin a version, and don't call a bare vhscli binary even if one is on PATH — it may be stale.

npx @getvhs/vhscli@latest <command> ...


Throughout this doc, commands are written as vhscli ... for readability — substitute npx @getvhs/vhscli@latest ... when running.

Requires Node.js ≥ 22. file is needed for MIME detection; sips (ships with macOS) for image conversion; ffmpeg for cross-format video conversion.

Top-level
vhscli [-v|--version] [-h|--help]
vhscli <command> [options] ...

-v, --version — print version (only when no command is given)
-h, --help — show help (works on root and every subcommand)

Commands:

login — log in with google (opens browser; saves session to ~/.vhs/session.json)
logout — log out and delete local access tokens
whoami — print the logged-in user's email
models — list available models
generate <model> <prompt> [-o <path>] — generate an image or video
chat <prompt> — chat with seed-2.0 (text, image, video, or pdf input)
resume <task_id> [-o <output>] — finish a generation that was aborted, by task id
Auth

Assume auth is already configured. If a command fails with an auth error, run vhscli login to open a browser for Google OAuth. Do NOT run vhscli login preemptively — it requires interactive browser login.

Models
Chat / understand (text / image / video / pdf): seed-2.0 — under vhscli chat
Generate images: seedream-5 (default), seedream-4-5, nano-banana-2, nano-banana-pro, gpt-image-2 — under vhscli generate
Generate video: seedance-2 — under vhscli generate
Prompt guides

Before you invoke vhscli generate (or do non-trivial understanding with vhscli chat), Read the matching prompt guide first and shape the prompt around it. The guides are concise, model-specific references distilled from each provider's docs — formulas, what to lead with, what works, what fails. Wording that's great for one model often underperforms on another, so don't skip this.

Model(s)	Guide file (Read before prompting)
seed-2.0 (used by vhscli chat)	prompt_guide/seed-2.txt
seedream-5, seedream-4-5	prompt_guide/seedream.txt
nano-banana-2, nano-banana-pro	prompt_guide/nano-banana.txt
seedance-2	prompt_guide/seedance-2.txt
gpt-image-2	prompt_guide/gpt-image-2.txt

Trigger: any time the user asks for output from one of these models, Read its guide before building the prompt. For trivial chat (plain text Q&A with no media) you can skip seed-2.txt.

Stdin prompts

Every command that takes a prompt also accepts - as the prompt, meaning "read from stdin":

cat my_prompt.txt | vhscli generate nano-banana-pro -
echo "what is this?" | vhscli chat - -i photo.jpg

vhscli chat — chat about text, images, video, or pdfs
vhscli chat <prompt> [-i <image>...] [-f <pdf>...] [-v <video>] [--fps <n>]


Mode is picked from your flags:

prompt only → text chat
-i → ask about images (repeatable)
-f → ask about pdf documents (repeatable)
-v → ask about a single video

Options:

-i, --image <path> — image to ask about (repeat -i for more)
-f, --file <path> — pdf document to ask about (repeat -f for more)
-v, --video <path> — single video to ask about
--fps <n> — frames/sec sampled from the video, 0.2–5 (default: 1)

One-shot — each call is independent, no memory of previous calls. Output goes to stdout, nothing is saved to disk. Audio inside a video is not understood.

Examples:

vhscli chat "explain how to make sourdough in 5 steps"
vhscli chat "describe the scene. return json with objects, setting, mood." -i photo.jpg
vhscli chat "transcribe all visible text verbatim, preserving line breaks." -i receipt.jpg
vhscli chat "compare image 1 and image 2 in 3 bullets." -i a.jpg -i b.jpg
vhscli chat "summarize this paper in 5 bullets; include a page number per bullet." -f paper.pdf
vhscli chat "list key events with start_time and end_time in HH:mm:ss as json." -v clip.mp4 --fps 2

vhscli generate seedream-5 — generate an image (default choice)
vhscli generate seedream-5 <prompt> [-o <path>] [-i <image>...] [--size <size>]


Options:

-o, --output <path> — output file path (default: ./vhscli-seedream-5-<timestamp>.jpg)
-i, --image <path> — reference image, max 14 (repeat -i for more)
--size <size> — 2K, 3K, or WxH like 1024x1536 (default: 2K)
WxH pixel count must be in [3,686,400, 10,404,496]
WxH aspect ratio must be in [1:16, 16:1]

Output format is determined by the output path extension (.png, .jpg/.jpeg, .webp). The provider returns png or jpeg; the cli transcodes via sips if the extension differs.

Examples:

vhscli generate seedream-5 "a red fox in a snowy forest" -o fox.jpg
vhscli generate seedream-5 "swap the outfit" -o out.png -i person.jpg -i outfit.jpg --size 3K

vhscli generate seedream-4-5 — generate an image (larger size range)
vhscli generate seedream-4-5 <prompt> [-o <path>] [-i <image>...] [--size <size>]


Options:

-o, --output <path> — output file path (default: ./vhscli-seedream-4-5-<timestamp>.jpg)
-i, --image <path> — reference image, max 14 (repeat -i for more)
--size <size> — 2K, 4K, or WxH (default: 2K)
WxH pixel count must be in [3,686,400, 16,777,216]
WxH aspect ratio must be in [1:16, 16:1]

Example:

vhscli generate seedream-4-5 "a mountain at sunrise" -o mountain.jpg --size 4K

vhscli generate nano-banana-2 — generate an image (Google, with search grounding)
vhscli generate nano-banana-2 <prompt> [-o <path>] [-i <image>...]
                              [--ratio <r>] [--size <size>]
                              [--think <level>] [--search] [--image-search]


Options:

-o, --output <path> — output file path (default: ./vhscli-nano-banana-2-<timestamp>.png)
-i, --image <path> — reference image, max 14 (repeat -i for more)
--ratio <r> — aspect ratio (default: 1:1). one of: 1:1, 1:4, 1:8, 2:3, 3:2, 3:4, 4:1, 4:3, 4:5, 5:4, 8:1, 9:16, 16:9, 21:9
--size <size> — 512, 1K, 2K, or 4K (default: 1K)
--think <level> — how hard the model thinks: minimal or high (default: minimal)
--search — use google search while generating
--image-search — also use google image search (implies --search)

Examples:

vhscli generate nano-banana-2 "90s skateboarder poster" -o poster.png --ratio 9:16 --size 2K
vhscli generate nano-banana-2 "diagram of the latest iphone" -o d.png --image-search
vhscli generate nano-banana-2 "a typographic poster spelling 'NEW YORK' over a skyline" --think high

vhscli generate nano-banana-pro — generate an image (Google, premium)
vhscli generate nano-banana-pro <prompt> [-o <path>] [-i <image>...] [--ratio <r>] [--size <size>]


Options:

-o, --output <path> — output file path (default: ./vhscli-nano-banana-pro-<timestamp>.png)
-i, --image <path> — reference image, max 14 (repeat -i for more)
--ratio <r> — aspect ratio (default: 1:1). one of: 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9
--size <size> — 1K, 2K, or 4K (default: 1K)

Higher-quality sibling of nano-banana-2 — better text rendering, richer textures. No --search or --think flags.

Example:

vhscli generate nano-banana-pro "studio portrait, cinematic lighting" -o portrait.jpg --ratio 3:4 --size 2K

vhscli generate gpt-image-2 — generate or edit an image (OpenAI)
vhscli generate gpt-image-2 <prompt> [-o <path>] [-i <image>...] [--mask <path>] [--size <size>]


Options:

-o, --output <path> — output file path (default: ./vhscli-gpt-image-2-<timestamp>.png)
-i, --image <path> — reference image for edits (repeat -i for more). switches to the edit endpoint
--mask <path> — edit mask (png with transparent pixels marking edit regions); requires -i
--size <size> — preset (auto, 1024x1024, 1536x1024, 1024x1536, 2048x2048, 2048x1152, 3840x2160) or WxH (default: auto)
both sides must be multiples of 16, max edge 3840
total pixels in [655,360, 8,294,400]
aspect ratio in [1:3, 3:1]

Output format is derived from the -o extension (.png, .jpg/.jpeg, .webp) and sent to the provider — no local transcode. Use png or webp for transparent backgrounds.

Examples:

vhscli generate gpt-image-2 "a children's book drawing of a veterinarian examining a cat"
vhscli generate gpt-image-2 "replace the background with a starry night, keep the subject unchanged" -i photo.jpg
vhscli generate gpt-image-2 "add a red balloon in the masked area" -i room.png --mask hole.png
vhscli generate gpt-image-2 "ultra-wide landscape of the swiss alps at golden hour" --size 3840x2160 -o alps.jpg

vhscli generate seedance-2 — generate a video
vhscli generate seedance-2 <prompt> [-o <path>]
                           [--first-frame <image>] [--last-frame <image>]
                           [-i <image>...] [-v <video>...] [-a <audio>...]
                           [--ratio <r>] [--resolution <res>] [--duration <n>]
                           [--silent] [--seed <n>]


Mode is picked from your flags:

prompt only → text-to-video
--first-frame → animate from that frame (optionally --last-frame too)
-i / -v / -a → use as references

Options:

-o, --output <path> — output file path (default: ./vhscli-seedance-2-<timestamp>.mp4)
--first-frame <image> — use as the first frame
--last-frame <image> — use as the last frame (requires --first-frame)
-i, --image <path> — reference image, max 9 (repeat -i). conflicts with --first-frame
-v, --video <path> — reference video, max 3 (repeat -v)
-a, --audio <path> — reference audio, max 3 (repeat -a). requires -i or -v
--ratio <r> — aspect ratio (default: adaptive). one of: 16:9, 4:3, 1:1, 3:4, 9:16, 21:9, adaptive
--resolution <res> — 480p, 720p, or 1080p (default: 720p)
--duration <n> — length in seconds, 4–15, or -1 for auto (default: 5)
--silent — make a silent video (no audio track)
--seed <n> — random seed for reproducible output

Defaults to 5s @ 720p with audio. Jobs run in the cloud and can take minutes — the CLI polls automatically, but if it's interrupted, save the printed task_id and use vhscli resume <task_id> later.

Examples:

# text-to-video
vhscli generate seedance-2 "a cat jumping off a couch" -o cat.mp4 --duration 6 --ratio 16:9

# animate a still image
vhscli generate seedance-2 "camera pans right" -o pan.mp4 --first-frame start.jpg

# with a first and last frame
vhscli generate seedance-2 "morph between these" -o morph.mp4 --first-frame a.jpg --last-frame b.jpg

# reference-based with audio
vhscli generate seedance-2 "lip sync the words" -o out.mp4 -i face.jpg -a voice.mp3

vhscli resume — finish an aborted generation
vhscli resume <task_id> [-o <output>]


Every vhscli generate command prints a line task_id: <uuid> to stdout before kicking off the backend task. If the cli process is aborted mid-generation (ctrl-c, crash, closed terminal, lost network), the backend keeps running; save that id and later run vhscli resume <task_id> to wait for it and download the result.

Behavior:

Polls the task row until it has a result or an error, then saves the result.
The cli dispatches on the task's endpoint and saves with the right model's logic.
Output extension is decided by the model (mp4 for videos, png/jpg for images); pass -o to override the path/extension (transcoded if needed).
Exit code is non-zero on task error, missing task, or save failure.
vhscli chat does not create a resumable task — chat is fast and streams to stdout.

Example:

# kick off a generation, note the printed task_id, then if it aborts:
vhscli resume 8f3a1b2c-9e0f-4a1b-9c8d-1e2f3a4b5c6d -o cat.mp4

Understanding local images, video, and pdfs

Do NOT use the Read tool, or any built-in file-reading capability, to "look at" images, video, or pdfs. That path either fails or gives you a garbled snippet. The only correct way to understand local visual or document content is vhscli chat with -i / -v / -f.

vhscli chat "what's happening?" -i photo.jpg
vhscli chat "transcribe the speech" -v clip.mp4 --fps 2
vhscli chat "summarize this paper" -f paper.pdf

Prompt patterns for visual / document understanding

vhscli chat understands images, pdfs, and video frames, but not audio inside videos. Ask for structured JSON output when you'll parse the answer, and name every field you want. Be explicit about formats (timestamp style, units, language).

Image — describe / classify:

vhscli chat "describe the scene. return json {objects:[{label,bbox?}], setting, mood, dominant_colors:[]}." -i photo.jpg
vhscli chat "classify the image into one of: cat, dog, bird, other. return json {label, confidence_0_1, reasoning}." -i pic.jpg


Image — OCR / text extraction:

vhscli chat "transcribe all visible text verbatim, preserving line breaks and reading order. do not paraphrase." -i receipt.jpg
vhscli chat "extract the receipt as json {merchant, date_iso, items:[{name, qty, unit_price, line_total}], subtotal, tax, total, currency}." -i receipt.jpg


Image — comparison (number them in the prompt):

vhscli chat "compare image 1 and image 2. return json {same_subject:bool, differences:[], which_is_better, why}." -i a.jpg -i b.jpg
vhscli chat "image 1 is the original, image 2 is an edit. list every visible change as json {changes:[{region, before, after}]}." -i orig.png -i edit.png


PDF — summarize / outline (always ask for page anchors):

vhscli chat "summarize this paper in 5 bullets. each bullet must include the source page as {page:int, point:string}. return json {bullets:[...]}." -f paper.pdf
vhscli chat "extract the outline as json [{page, heading_level, heading, bullets:[]}]." -f doc.pdf


PDF — QA / extraction:

vhscli chat "answer using only this document. question: what is the experimental setup? return json {answer, citations:[{page, quote}]}." -f paper.pdf
vhscli chat "extract every table as json [{page, title?, headers:[], rows:[[...]]}]." -f report.pdf


Video — events / timeline (state the timestamp format):

vhscli chat "list key events. return json [{start_time, end_time, event}]. use HH:mm:ss." -v clip.mp4 --fps 2
vhscli chat "describe the movement sequence and any safety risks. return json [{start_time, end_time, event, danger:'none'|'low'|'med'|'high'}]. HH:mm:ss." -v clip.mp4 --fps 3


Video — temporal QA / counting:

vhscli chat "at what timestamp does the referee first appear? return json {timestamp_hms, evidence}." -v match.mp4 --fps 2
vhscli chat "count how many distinct people appear. return json {count, per_person:[{first_seen_hms, description}]}." -v scene.mp4 --fps 3


Choosing --fps for video (default 1, range 0.2–5):

3–5 — counting actions, sports, fast cuts, dense motion.
1 — general description, dialogue scenes.
0.2–0.5 — long static footage, headcount, slow surveillance.

Higher fps = more detail but more tokens and slower. Lower fps = cheaper but may miss brief events.

Tips
Always quote prompts.
-o is optional for vhscli generate — defaults to ./vhscli-<model>-<timestamp>.<ext> in the current folder. Output format is detected from the -o extension; mismatches are transcoded via sips (images) or ffmpeg (videos).
Short options accept no-space form: -ofoo.jpg. Long options accept =: --size=2K.
Use -- to pass a prompt starting with a dash: vhscli generate seedream-5 -o x.jpg -- "-weird prompt".
Reference images (-i, --first-frame, --last-frame) can be any common format — the cli detects the real mime via file and auto-converts non-jpeg/png inputs (e.g. heic, webp, tiff, bmp) to jpeg via sips before upload.
Uploads are deduplicated by content hash, so passing the same reference repeatedly is cheap.
Unknown command? vhscli will suggest the closest match.
Weekly Installs
13
Repository
getvhs/vhscli-skills
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn