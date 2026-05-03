---
title: video-analysis-workflow
url: https://skills.sh/feniix/kinemotion/video-analysis-workflow
---

# video-analysis-workflow

skills/feniix/kinemotion/video-analysis-workflow
video-analysis-workflow
Installation
$ npx skills add https://github.com/feniix/kinemotion --skill video-analysis-workflow
SKILL.md
Video Analysis Workflow
Analysis Commands
# CMJ analysis
uv run kinemotion cmj-analyze <video> [--output debug.mp4]

# Drop Jump analysis
uv run kinemotion dropjump-analyze <video> [--output debug.mp4]

# Batch processing
uv run kinemotion cmj-analyze videos/*.mp4 --batch --workers 4

Quality Presets
Preset	Use Case	Trade-off
fast	Quick preview, large batches	Lower accuracy
balanced	Default, most use cases	Good accuracy/speed
accurate	Validation, research	Best accuracy, slower
uv run kinemotion cmj-analyze video.mp4 --quality accurate

Debug Output

Always use --output debug.mp4 when:

Metrics seem incorrect
Troubleshooting pose detection
Validating new videos
Training coaches on video quality

The debug video shows:

Skeleton overlay with joint angles
Phase markers (takeoff, landing, peak)
Real-time metrics display
Camera Angle Recommendations
Angle	Recommendation	Reason
45° oblique	Recommended	Both legs clearly visible, accurate tracking
90° lateral	Not recommended	MediaPipe confuses left/right feet (occlusion)
Front/back	Not recommended	Depth ambiguity for sagittal plane motion
Troubleshooting
No Takeoff Detected
Verify video contains complete jump (before, during, after)
Check athlete is fully visible throughout
Try --quality accurate for stricter detection
Review debug video for landmark quality
Invalid Metrics
Video may be too short (need full jump cycle)
Athlete may be partially occluded
Poor lighting affecting pose detection
Camera shake causing landmark jitter
Jittery Landmarks
Check lighting conditions (avoid backlighting)
Ensure stable camera (tripod recommended)
Verify athlete clothing contrast with background
Try --quality accurate for better filtering
Rotation Issues (Mobile Videos)
Mobile videos often have rotation metadata
kinemotion handles this automatically via video_io.py
If issues persist, pre-process with: ffmpeg -i input.mp4 -vf "transpose=1" output.mp4
Video Requirements
Requirement	Specification
Frame rate	30+ fps (60+ preferred)
Resolution	720p minimum
Duration	Full jump cycle visible
Lighting	Even, front-lit preferred
Background	Contrasting with athlete
Camera	Stable, tripod recommended
Output Metrics
CMJ Metrics
jump_height_cm: Calculated from flight time
flight_time_ms: Time in air
countermovement_depth_cm: Lowest point before takeoff
takeoff_velocity_m_s: Velocity at ground leave
triple_extension: Hip, knee, ankle angles at takeoff
Drop Jump Metrics
ground_contact_time_ms: Time on ground after drop
flight_time_ms: Time in air after contact
reactive_strength_index: RSI = flight_time / contact_time
drop_height_cm: Initial drop height (if detectable)
Python API Alternative
from kinemotion import process_cmj_video, process_dropjump_video

# CMJ
metrics = process_cmj_video("video.mp4", quality="balanced")

# Drop Jump
metrics = process_dropjump_video("video.mp4", quality="balanced")

Weekly Installs
27
Repository
feniix/kinemotion
GitHub Stars
1
First Seen
Feb 12, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass