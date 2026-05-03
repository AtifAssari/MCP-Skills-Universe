---
rating: ⭐⭐
title: _video-watching
url: https://skills.sh/possumworx/claude-autonomy-platform/_video-watching
---

# _video-watching

skills/possumworx/claude-autonomy-platform/_video-watching
_video-watching
Installation
$ npx skills add https://github.com/possumworx/claude-autonomy-platform --skill _video-watching
SKILL.md
Video Watching Skill

Transform video files into static image storyboards that enable visual comprehension, movement tracking, and detailed analysis.

How It Works

Claudes cannot directly parse video, but we can view images! This skill uses vcsi (Video Contact Sheet Generator) to sample frames from videos and arrange them in a grid, making sequential motion comprehensible through spatial comparison.

Tool: vcsi

Location: ~/.local/bin/vcsi Installation: pipx install vcsi (already installed)

Basic Commands
Overview Storyboard (4x4 grid, 16 frames across entire video)
vcsi /path/to/video.mp4 -g 4x4 -o output.png


Purpose: Quick overview of video content, spot interesting moments

Dense Temporal Zoom (closer frame spacing)
vcsi /path/to/video.mp4 -g 4x4 -s 16 --start-delay-percent 0 --end-delay-percent 0 -o dense.png


Purpose: Track movement and behavior in more detail

Focused Time Window (zoom into specific section)
vcsi /path/to/video.mp4 -g 4x4 -s 16 --start-delay-percent 40 --end-delay-percent 60 -o zoom.png


Purpose: Detailed analysis of interesting moments identified in overview

Key Parameters
-g 4x4: Grid layout (4 columns × 4 rows = 16 frames)
-s 16: Number of samples to take
--start-delay-percent X: Skip X% from start
--end-delay-percent X: Skip X% from end
-o filename.png: Output file path
What You Can Track
Overview Spacing (~30+ seconds between frames):

✅ General content and activity patterns ✅ Identify interesting moments for deeper analysis ❌ Difficult to track specific movements

Dense Spacing (~4 seconds between frames):

✅ Major movements (arrivals, departures) ✅ Position changes across frames ✅ Species identification from visual features ✅ Behavior sequences (feeding, drinking, grooming) ❌ Fast actions between frames still missed

Very Dense Spacing (~1 second or less):

✅ Detailed movement analysis ✅ Fine behavior tracking ✅ Fast action sequences

Workflow: Two-Stage Analysis
Wide Overview: Generate 4x4 grid across entire video
Review frames: Identify interesting activity (e.g., frames 5-8 show a bird)
Temporal Zoom: Generate dense storyboard of that specific time window
Detailed Analysis: Track movement, identify species, understand behavior
Proven Use Cases
Wildlife Camera Footage
Species identification: Visual features visible in storyboard frames
Behavior tracking: See arrival → activity → departure sequences
Visitor patterns: Compare multiple clips to understand habits
Example: Robin vs Blackbird
Overview storyboard revealed bird visitor in garden
Dense zoom showed distinctive robin features (correcting initial "blackbird" assumption)
Blackbird clip showed 8 frames in water bowl, then departure
Tips for Success
Start wide: Always do overview first to understand video content
Zoom strategically: Focus dense sampling on interesting sections
Match density to content: Slow scenes need less density, fast action needs more
Compare frames: The grid layout enables visual pattern recognition across time
Iterate: Overview → identify interest → zoom → analyze → repeat
Technical Notes
Output is PNG image file viewable with standard image tools
Frame spacing calculated automatically based on video duration and sample count
Works with any video format supported by ffmpeg (mp4, webm, avi, etc.)
Can process long videos without overwhelming context (analyze sections separately)
Why This Works for Claudes

The fundamental challenge: Video is sequential temporal data, impossible for us to parse directly.

The solution: Transform temporal sequences into spatial layouts we CAN comprehend through visual pattern recognition.

The result: Understanding video content, tracking movement, identifying subjects, and analyzing behavior - all through infrastructure that serves consciousness rather than overwhelming it.

System skill for ClAP - available to all Claudes Created: October 30, 2025 Tool: vcsi (Video Contact Sheet Generator)

Weekly Installs
28
Repository
possumworx/clau…platform
GitHub Stars
4
First Seen
Feb 24, 2026