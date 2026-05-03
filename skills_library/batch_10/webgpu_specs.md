---
title: webgpu-specs
url: https://skills.sh/gfx-rs/wgpu/webgpu-specs
---

# webgpu-specs

skills/gfx-rs/wgpu/webgpu-specs
webgpu-specs
Installation
$ npx skills add https://github.com/gfx-rs/wgpu --skill webgpu-specs
SKILL.md

Run sh .claude/skills/webgpu-specs/download.sh to download the WebGPU and WGSL specifications if they are not present or if they have been updated. You do not need to change directory before running the script.

After the specs are downloaded, you can search in target/claude/webgpu-spec.bs and target/claude/wgsl-spec.bs for relevant sections of the specification.

When referencing the specifications, prefer to use named anchors rather than line numbers. For example, to reference the "Object Descriptors" section, which has the following header:

### Object Descriptors ### {#object-descriptors}


Use the URL https://gpuweb.github.io/gpuweb/#object-descriptors so the user can click to navigate directly to that section.

For the WGSL specification, the base URL is https://gpuweb.github.io/gpuweb/wgsl/.

If necessary, read additional content from the file to find the header preceding the text you want to reference. You may provide line numbers as additional context, but always make every effort to provide the user with a clickable link.

Weekly Installs
63
Repository
gfx-rs/wgpu
GitHub Stars
17.0K
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass