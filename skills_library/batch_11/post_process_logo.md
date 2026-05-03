---
title: post-process-logo
url: https://skills.sh/tradingstrategy-ai/web3-ethereum-defi/post-process-logo
---

# post-process-logo

skills/tradingstrategy-ai/web3-ethereum-defi/post-process-logo
post-process-logo
Installation
$ npx skills add https://github.com/tradingstrategy-ai/web3-ethereum-defi --skill post-process-logo
SKILL.md
Post-process logo

This skill transforms original logo images into standardised 256x256 PNG format suitable for vault protocol metadata. It automatically selects the most square variant from available logos and applies padding if needed to create a perfect square output.

Required inputs

Before starting, gather the following from the user:

Input folder - Folder containing original logo files (e.g., eth_defi/data/vaults/original_logos/protocol-name/)
Output folder - Folder where processed logos should be saved (e.g., eth_defi/data/vaults/formatted_logos/)
Variant preference (optional) - Which variant(s) to process: generic, light, dark, or all

If any required input is missing, ask the user before proceeding.

Prerequisites

Ensure the following are available:

Python dependencies installed: poetry install --with dev

Python Pillow is installed for detecting image format, dimensions, and transparency.

Logo vocabulary

There is no universal standard how artist name their logo files for dark and light variants. In our case, we always say

light: light (white) text on dark or transparent background
dark: dark (black) text on white or transparent background

Following vocabulary is used:

Brand mark: same as logo mark, the logo without the brand name text
Word mark: the logo with the brand name text
Step 1: Inventory input logos

List all image files in the input folder and classify them:

Identify file formats: SVG, PNG, JPG, WEBP, etc.
Classify by variant based on filename:
{slug}.generic.{ext} - Generic/default theme
{slug}.light.{ext} - Light background theme (dark logo)
{slug}.dark.{ext} - Dark background theme (light logo)
Always prefer brand marks over word marks as source logo for post processing
Check aspect ratio of each logo:
Square aspect ratio: Width equals height (1:1 ratio). Allow 90% tolerance in the detection as there might be one-off pixel errors in the source material.
Non-square: Width differs from height - will need padding to become square
Check if logos have transparent backgrounds:
Transparent background: PNG files with alpha channel transparency
Assume SVGs are always transparent: SVG files the originals should never contain a solid background
Report findings to user, noting aspect ratios for each variant
Step 2: Variant selection
Automatic selection priority
Pick the most square variant: Calculate aspect ratio (min dimension / max dimension) for each variant and select the one closest to 1.0
If multiple variants have the same squareness:
Prefer transparent variants (PNG with alpha, SVG)
If still tied, prefer generic > light > dark
If user specified a variant preference: Use that variant regardless of squareness
Step 3: Process logo

Process the selected logo variant. The script will automatically add padding to non-square logos to make them square before scaling.

export INPUT_IMAGE=/path/to/original/logo.png
export OUTPUT_IMAGE=/path/to/output/logo.generic.png
poetry run python scripts/logos/post-process-logo.py


The script will:

Convert SVG to PNG if needed
Add transparent padding to make the logo square (if non-square)
Remove background if not already transparent
Recolour for dark background (invert colours if logo is too dark to be visible on dark backgrounds)
Trim any excess padding and scale to 256x256
Step 4: Report results

Provide the user with:

Processed files - List of all output files created
File details - Dimensions, file size for each
Any issues - Note any logos that couldn't be processed or had quality issues
Output naming convention

Output files should follow this naming pattern:

{protocol-slug}/light.png - For light backgrounds
{protocol-slug}/dark.png - For dark backgrounds
Troubleshooting
SVG conversion issues

If SVG conversion fails:

Check if the SVG file is valid XML
Some complex SVGs may not render correctly
Try opening in a browser to verify the SVG displays properly
Background removal issues

If the background isn't removed properly:

The logo may have complex edges or gradients
Try providing a higher resolution input
For logos that already have transparency, the script will skip background removal
Weekly Installs
57
Repository
tradingstrategy…eum-defi
GitHub Stars
806
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass