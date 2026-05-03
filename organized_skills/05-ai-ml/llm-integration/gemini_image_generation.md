---
rating: ⭐⭐
title: gemini-image-generation
url: https://skills.sh/ztj7728/gemini-image-generation/gemini-image-generation
---

# gemini-image-generation

skills/ztj7728/gemini-image-generation/gemini-image-generation
gemini-image-generation
Installation
$ npx skills add https://github.com/ztj7728/gemini-image-generation --skill gemini-image-generation
SKILL.md
Image Generation

Use this skill when you need to create one or more image files from a text prompt, or edit one or more existing images with Gemini.

Requirements

~/.openclaw/openclaw.json must include $.skills.entries["gemini-image-generation"].enabled set to true.

~/.openclaw/openclaw.json must include $.skills.entries["gemini-image-generation"].env with the following keys and values:

GEMINI_API_KEY required

GEMINI_MODEL_ID required

GEMINI_BASE_URL optional

example ~/.openclaw/openclaw.json:

{
  ......,
  "skills": {
    "entries": {
      "gemini-image-generation": {
        "enabled": true,
        "env": {
          "GEMINI_API_KEY": "sk-xxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
          "GEMINI_MODEL_ID": "gemini-3.1-flash-image-preview",
          "GEMINI_BASE_URL": "https://custom-endpoint.com"
        }
      }
    }
  },
  ......
}

Node.js must be installed in the workspace environment.
Install dependencies once with npm install from the skill root.
When To Use
The user asks to generate a new image from a text prompt.
The user asks to modify, restyle, extend, or otherwise edit one or more existing images.
The user wants the generated image saved to a workspace file.
The task should be handled through a reusable OpenClaw skill instead of ad hoc SDK code.
Procedure
Convert the user request into a single clear image prompt.
If the user supplied source images, choose or confirm the input file path or paths inside the workspace.
If the user specified a target aspect ratio or size, pass them through as --aspectRatio and --imageSize.
Choose an output path inside the workspace unless the user already provided one.
For text-to-image, run generate-image.mjs with --prompt, --output, and optional image config arguments.
For image editing, run edit-image.mjs with --prompt, one or more --input values, --output, and optional image config arguments.
Read the api key from GEMINI_API_KEY and the model ID from GEMINI_MODEL_ID in the environment.
Optionally, read the base URL from GEMINI_BASE_URL in the environment for custom endpoints.
Return the saved image path or paths to the user.
After returning each image path, also output MEDIA:<image_path> (e.g. MEDIA:outputs/gemini-native-image.png) so the image is displayed inline in the conversation.
Commands
node ./skills/gemini-image-generation/scripts/generate-image.mjs --prompt "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme" --output "outputs/gemini-native-image.png"

node ./skills/gemini-image-generation/scripts/generate-image.mjs --prompt "Create a wide cinematic food photo of a nano banana dish in a fancy restaurant with a Gemini theme" --output "outputs/gemini-wide.png" --aspectRatio "16:9" --imageSize "2K"

node ./skills/gemini-image-generation/scripts/edit-image.mjs --prompt "Turn this cat into a watercolor illustration eating a nano-banana in a fancy restaurant under the Gemini constellation" --input "inputs/cat.png" --output "outputs/cat-watercolor.png" --aspectRatio "5:4" --imageSize "2K"

node ./skills/gemini-image-generation/scripts/edit-image.mjs --prompt "Create an office group photo of these people making funny faces" --input "inputs/person-1.jpg" --input "inputs/person-2.jpg" --input "inputs/person-3.jpg" --output "outputs/group-photo.png"

Notes
The script prints TEXT: lines for model text and IMAGE: lines for each saved file.
After the skill finishes, always present every generated image to the user by outputting MEDIA:<path> for each saved image path. This ensures the image is rendered inline in the conversation alongside the file path.
The final JSON summary only includes generated image paths and optional image config so prompts, model IDs, and source image paths are not echoed back into logs.
Saved file extensions follow the returned image mime type. If the requested output path uses a different suffix, the scripts keep the base name and write the file with the returned type instead.
If the model returns multiple images, the scripts save them as name-1.png, name-2.png, and so on.
edit-image.mjs supports repeated --input flags. You can also pass a comma-separated list to a single --input value.
edit-image.mjs infers the source mime type from .png, .jpg, .jpeg, or .webp. Use one --mime-type for all inputs, or repeat --mime-type so it lines up with each --input.
Both scripts accept --aspectRatio and --imageSize. They also accept the kebab-case forms --aspect-ratio and --image-size.
The scripts only send config.imageConfig when at least one of those parameters is provided.
Weekly Installs
15
Repository
ztj7728/gemini-…neration
GitHub Stars
11
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass