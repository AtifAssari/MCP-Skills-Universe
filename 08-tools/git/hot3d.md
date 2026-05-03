---
title: hot3d
url: https://skills.sh/wu-yc/labclaw/hot3d
---

# hot3d

skills/wu-yc/labclaw/hot3d
hot3d
Installation
$ npx skills add https://github.com/wu-yc/labclaw --skill hot3d
SKILL.md
HOT3D - Multi-View 3D Hand & Object Tracking
Overview

State-of-the-art multi-view 3D tracking system for egocentric hand-object interactions from Meta Facebook Research. Designed for Aria smart glasses and Quest VR headsets, HOT3D provides precise 3D world coordinates for hand joints, manipulated objects, and their interactions. The system includes visualization tools for rendering 3D overlays on video frames with joint projections, hand meshes, and object models.

Project page: https://facebookresearch.github.io/hot3d

Best for: Research-grade 3D tracking with multi-camera setups, high-precision applications, and XR device integration.

When to Use This Skill

Use when you need:

Multi-view 3D tracking with world coordinates
High-precision hand pose in 3D space (millimeter accuracy)
Object tracking during manipulation
Aria/Quest integration for wearable devices
Research-grade tracking benchmarks
Hand-object interaction analysis in 3D

vs alternatives:

More advanced than single-view methods (hands-3d-pose)
Higher precision than bounding box detection (handtracking)
Full 3D world coordinates vs 2D projections
Core Capabilities
1. Multi-View 3D Hand Tracking

21-keypoint 3D hand pose from multiple synchronized cameras:

3D world coordinates (x, y, z) for each joint
Joint confidence scores
Left/right hand identification
Temporal consistency across frames
Hand mesh reconstruction
2. Object Pose Estimation

6DOF object pose tracking:

3D position and orientation (quaternion/rotation matrix)
Object mesh alignment
Tracking during manipulation
Multiple object support
3. Hand-Object Interaction

Interaction analysis:

Contact point detection
Grasp type classification
Manipulation phase detection
Force estimation (with sensor data)
4. Visualization Tools

Rich visualization options:

3D skeleton projected to each camera view
Hand mesh rendering
Object model overlay
Trajectory visualization
Multi-view synchronized display
Quick Start
# Clone repository
git clone https://github.com/facebookresearch/hot3d.git
cd hot3d

# Install dependencies
pip install -r requirements.txt
# Key: PyTorch3D, Open3D, vispy

# Download dataset (requires registration)
# https://facebookresearch.github.io/hot3d/dataset.html

# Run demo
python demo/visualize_tracking.py \
    --sequence demo_sequence \
    --output_dir ./visualizations

Usage Example
from hot3d import HOT3DTracker
import numpy as np

# Initialize tracker
tracker = HOT3DTracker()
tracker.load_sequence('path/to/sequence')

# Get frame data
frame_data = tracker.get_frame(frame_id=100)

# Access 3D hand pose
hand_pose_3d = frame_data['left_hand']  # 21x3 array
print(f"Wrist position: {hand_pose_3d[0]}")  # [x, y, z]

# Access object pose
object_pose = frame_data['object_001']
position = object_pose['position']  # [x, y, z]
rotation = object_pose['rotation']  # 3x3 matrix

# Visualize
tracker.visualize_frame(
    frame_id=100,
    show_hands=True,
    show_objects=True,
    show_meshes=True,
    save_path='output.png'
)

Model Specs
Input: Multi-view RGB-D video streams (typically 3-5 cameras)
Output: 3D coordinates in world frame (millimeters)
Accuracy: ~5-10mm hand joint error
Frame rate: 30-60 Hz (depends on hardware)
Latency: <100ms for real-time applications
Requirements
Hardware: Multi-camera setup or Aria/Quest device
Computation: GPU recommended (NVIDIA RTX 3080 or better)
Storage: Large dataset (several TB for full HOT3D)
Software: PyTorch, PyTorch3D, Open3D
Dataset

HOT3D dataset includes:

100+ sequences of daily activities
Multi-view RGB-D video
3D hand and object annotations
Aria/Quest recordings
Smart glasses data

Access: https://facebookresearch.github.io/hot3d

Integration

Works with:

hand-tracking-toolkit: Evaluation and metrics
Aria SDK: Device integration
PyTorch3D: 3D processing
OpenXR: XR platform integration
Limitations
Requires multi-view setup or specialized hardware
Computational intensive
Dataset access requires registration
Complex setup compared to single-view methods
Best For
XR applications with smart glasses
Research in 3D hand tracking
High-precision manipulation analysis
Benchmarking new algorithms
References
Project: https://facebookresearch.github.io/hot3d
GitHub: https://github.com/facebookresearch/hot3d
Paper: HOT3D dataset publication
Citation: See project page
License

CC-BY-NC 4.0 (non-commercial only)

Weekly Installs
12
Repository
wu-yc/labclaw
GitHub Stars
972
First Seen
Mar 15, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass