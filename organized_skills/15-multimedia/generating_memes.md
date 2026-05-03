---
rating: ⭐⭐⭐
title: generating-memes
url: https://skills.sh/geekjourneyx/meme-generator-skill/generating-memes
---

# generating-memes

skills/geekjourneyx/meme-generator-skill/generating-memes
generating-memes
Installation
$ npx skills add https://github.com/geekjourneyx/meme-generator-skill --skill generating-memes
SKILL.md
Generating Memes

Creates memes using the meme CLI tool with 298+ templates.

Quick Start

List all templates:

meme list


Search templates by keyword:

meme search <keyword>


Generate a meme:

meme generate <template> --images <paths> --texts <texts>

Popular Templates

Most commonly used templates:

Template	Description	Type
petpet	Petting animation (摸/摸摸)	Image
slap	Slapping animation (一巴掌)	Image
hug	Hugging animation (抱/抱抱)	Image
rub	Nuzzling animation (贴/贴贴)	Image
pat	Patting animation (拍)	Image
kiss	Kissing animation (亲/亲亲)	Image
pinch	Pinching face (捏/捏脸)	Image
5000choyen	Big/small text contrast	Text
always	"Always" format meme	Text
shock	Shocked reaction (震惊)	Text
clown	Clown meme (小丑)	Image
stare_at_you	Staring at you (盯着你)	Image
loading	Loading animation	Text
good_news	Good news header (喜报)	Text
bad_news	Bad news header (悲报)	Text
applaud	Applause (鼓掌)	Image
praise	Praise (表扬)	Text
speechless	Speechless (无语)	Image
run_away	Run away (快逃)	Image
suck	Suck/Sip animation (吸/嗦)	Image

See full template list

Usage Patterns
Image-based Memes

Templates requiring one or more images:

# Single image
meme generate petpet --images /path/to/photo.jpg

# Save to file
meme generate petpet --images /path/to/photo.jpg > output.gif

Text-based Memes

Templates using only text:

# 5000兆 (big/small contrast)
meme generate 5000choyen --texts "IMPORTANT" "ignore this"

# Always meme
meme generate always --texts "the answer is 42"

Mixed (Images + Text)
Recommended Workflow
Search for a template: meme search <keyword>
Preview the template: meme preview <template>
Check requirements: meme info <template>
Generate the meme: meme generate <template> [options]
Example: Create a Petpet Meme
# 1. Verify template exists
meme search pet

# 2. See what it needs
meme info petpet
# Output: needs 1 image, 0 text

# 3. Generate
meme generate petpet --images friend.jpg > petpet.gif

Commands Reference
Command	Description
meme list	List all 298 templates
meme search <keyword>	Search templates by keyword
meme info <template>	Show template requirements (images, texts, params)
meme preview <template>	Generate template preview
meme generate <template>	Create meme
meme download	Download required resources

See more examples

Troubleshooting
"meme: command not found"

The meme CLI is not installed. Install it from GitHub:

# Download the binary
curl -L https://github.com/MemeCrafters/meme-generator-rs/releases/latest/download/meme-x86_64-unknown-linux-gnu -o meme

# Make executable and install
chmod +x meme
sudo mv meme /usr/local/bin/

# Download required resources
meme download


GitHub: https://github.com/MemeCrafters/meme-generator-rs

Alternative: Build from source with Rust:

cargo install meme-generator
meme download

Template Not Found

If generation fails with "unknown template" error:

# Verify template name
meme list | grep <template>

# Search for similar templates
meme search <keyword>

# Check template info
meme info <template>

Missing Resources

If images or templates are missing:

meme download


This downloads all required template assets.

Network Issues (Download Failed)

If meme download fails with connection timeout:

# Error example:
# WARN Failed to download: Connection timed out (os error 110)
# The CLI cannot reach cdn.jsdelivr.net

# Solution: Download resources manually from GitHub releases
# Visit: https://github.com/MemeCrafters/meme-generator-rs/releases


Note: Some templates may work without downloaded resources if they have built-in assets.

Tips
Use meme info <template> before generating to understand requirements
Redirect output to save: > output.gif
Many templates support both images and text
Some templates have optional parameters (like --circle for petpet)
Use meme search for discovery when unsure of template name
Weekly Installs
35
Repository
geekjourneyx/me…or-skill
GitHub Stars
22
First Seen
Feb 9, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail