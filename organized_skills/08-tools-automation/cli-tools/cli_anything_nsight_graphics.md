---
rating: ⭐⭐
title: cli-anything-nsight-graphics
url: https://skills.sh/hkuds/cli-anything/cli-anything-nsight-graphics
---

# cli-anything-nsight-graphics

skills/hkuds/cli-anything/cli-anything-nsight-graphics
cli-anything-nsight-graphics
Installation
$ npx skills add https://github.com/hkuds/cli-anything --skill cli-anything-nsight-graphics
SKILL.md
Nsight Graphics CLI Skill

Command-line orchestration of official NVIDIA Nsight Graphics activities.

Capabilities
Probe installed Nsight binaries and compatibility mode
Launch an application detached under Nsight
Attach Nsight to a running PID
Trigger Frame Debugger capture
Trigger GPU Trace capture, auto-export, and summarize
Trigger Generate C++ Capture
Commands
doctor
cli-anything-nsight-graphics --json doctor info
cli-anything-nsight-graphics --json doctor versions
cli-anything-nsight-graphics --nsight-path "C:\Path\To\Nsight Graphics 2024.2\host\windows-desktop-nomad-x64" --json doctor info

launch
cli-anything-nsight-graphics launch detached --activity "Frame Debugger" --exe "C:\Path\To\App.exe"
cli-anything-nsight-graphics launch attach --activity "Frame Debugger" --pid 12345

frame capture
cli-anything-nsight-graphics --output-dir D:\captures frame capture ^
  --exe "C:\Path\To\App.exe" ^
  --wait-frames 10

GPU Trace
cli-anything-nsight-graphics --output-dir D:\traces gpu-trace capture ^
  --exe "C:\Path\To\App.exe" ^
  --start-after-ms 1000 ^
  --limit-to-frames 1 ^
  --auto-export ^
  --summarize

cli-anything-nsight-graphics gpu-trace summarize ^
  --input-dir D:\traces

Generate C++ Capture
cli-anything-nsight-graphics --output-dir D:\cpp cpp capture ^
  --exe "C:\Path\To\App.exe" ^
  --wait-seconds 5

Agent Notes
Prefer doctor info first to discover the available compatibility mode.
Use doctor versions to list detected installs when multiple Nsight Graphics versions exist.
Use --nsight-path to force a specific install directory or ngfx.exe.
Use --json for programmatic workflows.
Prefer gpu-trace capture --auto-export --summarize for one-step performance triage.
Frame/GPU/C++ capture commands require a launch target through --exe or a preconfigured root-level --project.
V1 is orchestration-focused; it does not expose shader, pipeline, or resource inspection commands.
Weekly Installs
32
Repository
hkuds/cli-anything
GitHub Stars
33.2K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass