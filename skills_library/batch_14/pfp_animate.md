---
title: pfp-animate
url: https://skills.sh/velinussage/pfp-animate/pfp-animate
---

# pfp-animate

skills/velinussage/pfp-animate/pfp-animate
pfp-animate
Installation
$ npx skills add https://github.com/velinussage/pfp-animate --skill pfp-animate
SKILL.md

Four animation modes:

Veo mode (recommended): Video + audio from text prompt (Veo 3.1, ~$3.20/8s)
Lip-sync mode: Video synced to existing audio file (OmniHuman 1.5, ~$0.16/s)
Video mode: Silent video from prompt (Kling v2.5, ~$0.35/5s)
Keyframe mode: Precise facial expressions as GIF (expression-editor, ~$0.02)

Requires: REPLICATE_API_TOKEN environment variable

<check_setup> CRITICAL: Before ANY animation, check for token:

echo $REPLICATE_API_TOKEN | head -c 10


If empty or missing, ASK the user directly:

"I need your Replicate API token to generate videos. Please provide it, or get one from https://replicate.com/account/api-tokens"

Once user provides token, use it inline:

REPLICATE_API_TOKEN='user_provided_token' python scripts/animate_veo.py ...


Do NOT run animation scripts without first verifying the token is available. </check_setup>

Setup Replicate - Create account, get API token, configure environment
Animate with voice - Generate video with AI-generated voice/audio (Veo 3.1)
Lip-sync to audio - Sync video to existing audio file (OmniHuman 1.5)
Silent video - Generate video without audio (Kling v2.5)
Keyframe animation - Precise facial expressions as GIF
List presets - See available motion presets

Wait for user response before proceeding.

After reading the workflow, follow it exactly.

<quick_reference> Veo 3.1 (video + generated audio):

python scripts/animate_veo.py IMAGE OUTPUT.mp4 --prompt "person speaks to camera"
python scripts/animate_veo.py IMAGE OUTPUT.mp4 --prompt "person says 'Hello world'" --duration 8
python scripts/animate_veo.py IMAGE OUTPUT.mp4 --prompt "dramatic reveal" --reference IMAGE


OmniHuman 1.5 (lip-sync to audio file):

python scripts/animate_audio.py IMAGE AUDIO.mp3 OUTPUT.mp4
python scripts/animate_audio.py IMAGE --tts "Hello world" OUTPUT.mp4 --voice Deep_Voice_Man


Kling v2.5 (silent video):

python scripts/animate_pfp.py IMAGE OUTPUT.mp4 --motion nod
python scripts/animate_pfp.py IMAGE OUTPUT.mp4 --prompt "slowly winking"


Keyframe (precise gestures):

python scripts/animate_keyframe.py IMAGE OUTPUT.gif --motion nod_wink


</quick_reference>

<model_comparison>

Model	Audio	Best For	Cost
Veo 3.1	Generated	Speaking videos, announcements	~$3.20/8s
OmniHuman 1.5	Lip-sync	Sync to specific audio	~$0.16/s
Kling v2.5	None	Silent motion, gestures	~$0.35/5s
Expression-editor	None	Precise facial control	~$0.02
</model_comparison>			

<reference_index> Presets: references/presets.md - Motion presets for keyframe mode Troubleshooting: references/troubleshooting.md - Common errors and fixes API Costs: references/pricing.md - Full pricing reference </reference_index>

<workflows_index>

Workflow	Purpose
setup.md	Create Replicate account and configure API token
veo.md	Generate video with AI voice/audio using Veo 3.1
audio.md	Lip-sync video to existing audio using OmniHuman 1.5
animate.md	Generate silent video using Kling v2.5
keyframe.md	Precise facial expression control with expression-editor
</workflows_index>	

<success_criteria>

Replicate API token configured (echo $REPLICATE_API_TOKEN shows value)
Can run animation script without errors
Output video/GIF saved to specified path </success_criteria>
Weekly Installs
17
Repository
velinussage/pfp-animate
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail