---
rating: ⭐⭐
title: pixel art animator
url: https://skills.sh/willibrandon/pixel-plugin/pixel-art-animator
---

# pixel art animator

skills/willibrandon/pixel-plugin/Pixel Art Animator
Pixel Art Animator
Installation
$ npx skills add https://github.com/willibrandon/pixel-plugin --skill 'Pixel Art Animator'
SKILL.md
Pixel Art Animator
Overview

This Skill handles all animation-related tasks for sprites, including frame management, timing, animation tags (sequences), and linked cels for efficient animation.

When to Use

Use this Skill when the user:

Wants to "animate" a sprite or "add animation"
Mentions "frames", "keyframes", or "frame rate"
Describes motion: "walk cycle", "run cycle", "idle animation", "attack animation"
Asks about "animation tags", "loops", or "playback"
Wants to create "sprite sheets" for animation (coordinate with exporter Skill)

Trigger Keywords: animate, animation, frames, walk cycle, run, idle, attack, loop, movement, motion

Instructions
1. Understanding Animation Basics

Frame: A single image in an animation sequence. Sprites start with 1 frame.

Frame Duration: How long each frame displays (in milliseconds). Default: 100ms (10 FPS).

Animation Tag: Named sequence of frames (e.g., "walk" frames 1-4, "idle" frames 5-8).

Linked Cel: A cel that shares image data with another cel. Editing one updates all linked cels.

Playback Direction:

Forward: Frames play 1 → 2 → 3 → 4, then loop
Reverse: Frames play 4 → 3 → 2 → 1, then loop
Ping-pong: Frames play 1 → 2 → 3 → 4 → 3 → 2 → 1, then loop
2. Creating Animation Frames

Adding Frames: Use mcp__aseprite__add_frame to create new frames:

Frames are numbered starting from 1
New frames start as copies of the current frame (or blank)

Common Frame Counts:

Idle Animation: 2-4 frames (subtle movement)
Walk Cycle: 4-8 frames (legs alternate)
Run Cycle: 6-8 frames (faster, exaggerated)
Attack Animation: 3-6 frames (windup, strike, recovery)
Jump: 4-6 frames (crouch, ascend, peak, descend, land)

Duplicating Frames: Use mcp__aseprite__duplicate_frame to copy existing frames:

Useful for creating variations
Starting point for similar frames

Deleting Frames: Use mcp__aseprite__delete_frame to remove frames:

Cannot delete the last remaining frame
Frames are renumbered after deletion
3. Setting Frame Timing

Frame Duration: Use mcp__aseprite__set_frame_duration:

Duration in milliseconds (ms)
100ms = 10 FPS
50ms = 20 FPS
33ms ≈ 30 FPS
16ms ≈ 60 FPS

Common Timing Patterns:

Even Timing: All frames same duration. Simple and predictable.

Walk cycle: all frames 100ms (smooth 10 FPS)

Variable Timing: Different durations for emphasis.

Idle: slow frames (150ms) for breathing effect
Attack: fast strike (30ms), slower recovery (100ms)

Hold Frames: Longer duration for dramatic effect.

Jump peak: 200ms (hang time)
Impact: 50ms (quick flash)
4. Creating Animation Tags

Purpose: Organize frames into named sequences.

Use mcp__aseprite__create_tag:

Name: "walk", "idle", "attack", etc.
From Frame: starting frame (1-indexed)
To Frame: ending frame (inclusive)
Direction: "forward", "reverse", or "ping-pong"

Example Tags:

Tag "idle": frames 1-2, ping-pong direction
Tag "walk": frames 3-6, forward direction
Tag "attack": frames 7-10, forward direction

Benefits:

Export specific animations separately
Organize complex sprite sheets
Game engines can reference tags
5. Using Linked Cels

Purpose: Share image data across frames to save memory and maintain consistency.

Use mcp__aseprite__link_cel:

Useful when frame content doesn't change
Example: background layer stays same across animation
Editing one linked cel updates all

When to Use:

Static background elements
Character face in walk cycle (if body animates separately)
Repeated frames in animation

Workflow:

Create frames with content
Link cels that should share data
Edit once, updates everywhere
6. Animation Workflows

Workflow 1: Walk Cycle (4 frames)

Create base sprite (or use existing)
Add 3 more frames (total 4)
Edit each frame for walk positions:
Frame 1: Left foot forward
Frame 2: Contact (both feet touching)
Frame 3: Right foot forward
Frame 4: Contact (both feet touching)
Set all frames to 100ms duration
Create tag "walk": frames 1-4, forward direction

Workflow 2: Idle Animation (2 frames)

Create base sprite
Add 1 more frame (total 2)
Slight variations:
Frame 1: Normal stance
Frame 2: Subtle movement (breathing, blinking)
Set frames to 500ms duration (slow, subtle)
Create tag "idle": frames 1-2, ping-pong direction

Workflow 3: Complex Multi-Animation Sprite

Create base sprite
Add enough frames for all animations:
Idle: 2 frames
Walk: 4 frames
Jump: 4 frames
Total: 10 frames
Arrange frames sequentially
Create separate tags:
Tag "idle": frames 1-2
Tag "walk": frames 3-6
Tag "jump": frames 7-10
Set appropriate frame durations per animation
Examples
Example 1: Simple 2-Frame Idle

User Request:

"Add a simple idle animation to this sprite"

Approach:

Add 1 frame (now have frame 1 and 2)
On frame 2, make subtle change (move pixels up/down 1-2 pixels)
Set both frames to 500ms duration
Create tag "idle": frames 1-2, ping-pong direction
Result: gentle back-and-forth idle motion
Example 2: 4-Frame Walk Cycle

User Request:

"Create a walk cycle animation for this character"

Approach:

Add 3 frames (now have 1, 2, 3, 4)
Edit each frame for walk poses
Set all frames to 100ms duration
Create tag "walk": frames 1-4, forward direction
Result: looping walk animation at 10 FPS
Example 3: Variable Timing Attack

User Request:

"Add an attack animation with a fast strike"

Approach:

Add 5 frames (total 6 frames, assuming frame 1 exists)
Frame sequence:
Frame 2: Windup (slow)
Frame 3: Prepare (slow)
Frame 4: Strike (fast)
Frame 5: Follow-through (medium)
Frame 6: Recovery (slow)
Set durations:
Frames 2-3: 150ms (slow windup)
Frame 4: 30ms (fast strike)
Frame 5: 80ms (medium follow-through)
Frame 6: 120ms (slow recovery)
Create tag "attack": frames 2-6, forward direction
Example 4: Linked Background

User Request:

"Animate the character but keep the background static"

Approach:

Assume 2 layers: "Background", "Character"
Add frames for animation
Edit "Character" layer on each frame for animation
Link all cels on "Background" layer:
Link frame 2's background to frame 1
Link frame 3's background to frame 1
Link frame 4's background to frame 1
Background stays identical, character animates
Technical Details
Frame Numbering
Frames are 1-indexed (first frame is frame 1)
Adding frame at position N inserts at that position
Deleting frame N renumbers subsequent frames
Frame Duration Limits
Minimum: 1ms (not recommended, too fast)
Maximum: 65535ms (65.5 seconds)
Practical range: 16ms (60 FPS) to 500ms (2 FPS)
Animation Tag Limits
No hard limit on number of tags
Tags can overlap frames
Tag names should be unique and descriptive
Linked Cel Behavior
Editing one linked cel updates all linked instances
Unlinking creates independent copy
Useful for memory optimization in large animations
Performance
Adding frame: <20ms
Duplicating frame: <30ms
Setting frame duration: <10ms
Creating tag: <15ms
Linking cel: <25ms
Common Patterns
Pattern: Breathing Idle

2 frames, ping-pong, slow timing (400-500ms)

Frame 1: Normal
Frame 2: Slight vertical shift (1-2 pixels)
Pattern: Basic Walk

4 frames, forward, even timing (100ms)

Frame 1: Left foot forward, right foot back
Frame 2: Both feet together (contact)
Frame 3: Right foot forward, left foot back
Frame 4: Both feet together (contact)
Pattern: Run Cycle

6-8 frames, forward, faster timing (60-80ms)

More exaggerated poses than walk
Longer strides
Leaning forward
Pattern: Jump Sequence

5-6 frames, forward, variable timing

Frame 1: Crouch (100ms)
Frame 2: Launch (50ms)
Frame 3: Ascend (80ms)
Frame 4: Peak (200ms) - hang time
Frame 5: Descend (80ms)
Frame 6: Land (100ms)
Integration with Other Skills
Start with pixel-art-creator to create base sprite before animating
Use pixel-art-professional for polish (shading, antialiasing) after animation
Hand off to pixel-art-exporter when user wants to export spritesheet or GIF
Error Handling

Cannot delete last frame:

Sprites must have at least 1 frame
Inform user if they try to delete last frame

Invalid frame numbers:

Frame numbers must be 1 to N (where N is total frames)
Check bounds before operations

Tag frame range errors:

"From" frame must be ≤ "To" frame
Both must be valid frame numbers
Success Indicators

You've successfully used this Skill when:

Frames added/modified correctly
Frame durations set appropriately for desired FPS
Animation tags created with correct ranges
User understands animation will loop or play as specified
Animation is ready for export or further refinement
Weekly Installs
–
Repository
willibrandon/pi…l-plugin
GitHub Stars
155
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass