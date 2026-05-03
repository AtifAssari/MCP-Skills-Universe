---
rating: ⭐⭐⭐
title: video-explorer
url: https://skills.sh/cygnusfear/agent-skills/video-explorer
---

# video-explorer

skills/cygnusfear/agent-skills/video-explorer
video-explorer
Installation
$ npx skills add https://github.com/cygnusfear/agent-skills --skill video-explorer
SKILL.md
Video Explorer

Analyze video content through hierarchical frame extraction. Start wide, identify interesting regions, zoom in.

Workflow
1. Overview First

Extract quick thumbnails to see the video timeline:

./skills/video-explorer/scripts/videx overview <video>


This creates small frames (320px) at 10-second intervals in ./videx-out/<name>/overview/.

Read all overview frames to understand video structure:

ls ./videx-out/<name>/overview/


Then use the Read tool on the jpg files to see them.

⚠️ Triplet Rule: Never Single-Frame Sample

A single snapshot tells you nothing about change. Overview automatically extracts 3 frames per sample point (t-δ, t, t+δ) so you see motion at each checkpoint. Default δ=0.1s (~3 frames at 30fps) — tight enough to show micro-motion against the long interval between samples.

Triplet files are suffixed _a, _b, _c. Always compare the triplet together.

Configure delta for your needs:

--triplet=0.1 (default) — subtle motion, UI transitions
--triplet=0.5 — broader change, scene transitions
--triplet=1.0 — wide spread, slow-moving content
2. Identify Regions of Interest

After viewing overview frames, identify timestamps where:

Something interesting is happening
More detail is needed
Action is occurring that requires temporal resolution
3. Zoom In

For a time range (more frames, higher resolution):

./skills/video-explorer/scripts/videx range <video> <start>-<end>
# Example: videx range talk.mp4 5:30-6:00


For higher temporal resolution (catch fast action):

./skills/video-explorer/scripts/videx range <video> <start>-<end> --fps=10


For a single frame at full detail:

./skills/video-explorer/scripts/videx zoom <video> <time>
# Example: videx zoom talk.mp4 5:45

4. Iterate

Repeat zoom operations as needed until the question is answered.

Commands Reference
Command	Purpose	Output
videx overview <video>	Quick timeline scan	320px triplets @ 10s intervals (±0.1s)
videx overview <video> 5 480	Denser timeline	480px triplets @ 5s intervals
videx overview <video> 10 320 0.5	Wider triplet delta	320px triplets @ 10s, ±0.5s spread
videx range <video> <start>-<end>	Extract segment	1280px frames @ 2fps (no triplets)
videx range <video> <start>-<end> --fps=10	Fast action	1280px frames @ 10fps
videx range <video> <start>-<end> --triplet=0.1	Range with triplets	1280px triplets @ 2fps
videx zoom <video> <time>	Single frame detail	1920px single frame
videx zoom <video> <time> --hd	Maximum detail	Full resolution frame
Time Formats

All commands accept these time formats:

1:30 = 1 minute 30 seconds
01:30:00 = 1 hour 30 minutes
90 = 90 seconds
1:30.5 = 1 minute 30.5 seconds
Output Structure

Frames are saved with timestamps in filenames for easy reference:

./videx-out/
└── video-name/
    ├── overview/
    │   ├── t_00-00-00.00.jpg
    │   ├── t_00-00-10.00.jpg
    │   └── ...
    ├── range_5-30_6-00/
    │   ├── t_00-05-30.00.jpg
    │   └── ...
    └── zoom/
        └── t_00-05-45.00.jpg

Example Session

User asks: "What happens in this lecture video around the 10 minute mark?"

Run overview to understand video structure
View overview frames, note that slides change around 9:30-11:00
Extract that range: videx range lecture.mp4 9:30-11:00
View range frames, find the specific slide transition at 10:15
Zoom for detail: videx zoom lecture.mp4 10:15
Report findings with specific timestamps
Weekly Installs
34
Repository
cygnusfear/agent-skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass