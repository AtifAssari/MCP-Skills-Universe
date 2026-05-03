---
rating: ⭐⭐⭐
title: image-to-3d
url: https://skills.sh/catfishw/i23dagentskill/image-to-3d
---

# image-to-3d

skills/catfishw/i23dagentskill/image-to-3d
image-to-3d
Installation
$ npx skills add https://github.com/catfishw/i23dagentskill --skill image-to-3d
SKILL.md
Image to 3D Agent Skill

This skill allows you (the AI agent) to convert 2D images into 3D meshes with PBR textures. It is powered by Hunyuan3D-2.1.

When to use

Use this skill when the user explicitly asks to generate, create, or build a 3D asset, model, or mesh from a 2D image or picture.

How to Execute

You have two ways to interact with this skill. Since the code is located in the same directory as this file, you can run the scripts directly:

Option 1: CLI Wrapper (Terminal)

You can execute the Node.js CLI script directly:

# Generate a 3D model with background removal and textures (default)
node ./bin/cli.js /path/to/input.png -o /path/to/output.glb

# Disable background removal and textures (faster)
node ./bin/cli.js /path/to/input.png -o /path/to/output.glb --no-bg --no-texture


Note: The CLI connects to the backend API (default: http://localhost:23555/I23D). Generation takes 1-3 minutes.

Option 2: Model Context Protocol (MCP) Server

If your agent framework supports MCP, you can connect to the server by executing:

node ./mcp.js


This will expose the following tools to you over stdio:

check_server_status: Verify the backend is reachable.
generate_3d_model: Takes an imagePath and an outputPath. Returns success or semantic error messages.
API Configuration

By default, this skill connects to a local backend at http://localhost:23555/I23D.

To use a remote backend (e.g., https://mc.agaii.org/I23D/), set the environment variable:

export I23D_API_URL=https://mc.agaii.org/I23D


Or pass it directly to the CLI:

node ./bin/cli.js /path/to/input.png -o output.glb -u https://mc.agaii.org/I23D

Important Rules & Constraints
Backend Required: This skill requires a running Hunyuan3D-2.1 backend API. Start it locally with python api_server_enhanced.py --port 23555 in the backend folder.
Patience: 3D generation is computationally heavy. Expect 60 seconds to 3 minutes per model.
Format: Only .glb (glTF binary) format is officially supported for the output.
Input Constraints: The image should ideally feature a single, clear subject in the center. While the tool attempts background removal automatically, highly cluttered images might fail.
Weekly Installs
11
Repository
catfishw/i23dagentskill
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass