---
title: designing-canvas-images
url: https://skills.sh/dtyq/magic/designing-canvas-images
---

# designing-canvas-images

skills/dtyq/magic/designing-canvas-images
designing-canvas-images
Installation
$ npx skills add https://github.com/dtyq/magic --skill designing-canvas-images
SKILL.md
Canvas Image Design Skill

Provides AI image generation, web image search and download, and design marker processing capabilities.

How to Use This Document

This document provides quick guidance covering basic usage and core rules. When encountering the following situations, read the corresponding reference documentation:

Detailed Image-to-Image Guidelines → reference/image-generation.md
Web Image Search → reference/image-search.md
Design Marker Processing ([@design_marker:xxx]) → reference/design-marker.md
Code Execution Method (Critical)

All Python code examples in this skill must be executed via the run_skills_snippet tool in Agent environment.

Correct example:

# Correct! Must use run_skills_snippet to execute
run_skills_snippet(
    python_code="""
from sdk.tool import tool
result = tool.call('create_design_project', {
    "project_path": "my-design"
})
"""
)


All code blocks in this document starting with from sdk.tool import tool follow this rule: pass them via the python_code parameter of run_skills_snippet for execution.

Quick Start

Create a new canvas project:

from sdk.tool import tool

result = tool.call('create_design_project', {
    "project_path": "my-design"
})


Generate AI images:

from sdk.tool import tool

result = tool.call('generate_images_to_canvas', {
    "project_path": "my-design",
    "name": "北京景点",
    "prompts": ["长城全景，专业摄影", "故宫太和殿，专业摄影", "天坛祈年殿，专业摄影"],
    "size": "2048x2048"
})


Query canvas overview:

from sdk.tool import tool

result = tool.call('query_canvas_overview', {
    "project_path": "my-design",
    "sort_by": "layer"
})


Query element by image path:

from sdk.tool import tool

result = tool.call('query_canvas_element', {
    "project_path": "my-design",
    "src": "my-design/images/cat.jpg"
})

Core Tools and Required Parameters
create_design_project - Create Canvas Project
Parameter	Required	Description
project_path	Yes	Project relative path, e.g., "my-design"

Return data (result.data):

Field	Type	Description
project_path	string	Project path
project_name	string	Project name
generate_images_to_canvas - Generate AI Images
Parameter	Required	Description
project_path	Yes	Project path
name	Yes	Element name, automatically adds suffix _1, _2 for multiple images
prompts	Yes	List of prompts (max 6 prompts for multiple prompts mode)
size	Yes	Image size, format: 'widthxheight', e.g., "2048x2048", "2560x1440"
image_count	No	Number of images in a set, max 4 (mutually exclusive with multiple prompts)
image_paths	No	Reference image paths (used for image-to-image generation)

Return data (result.data):

Field	Type	Description
created_elements	array	Created element list, each contains { id, name, type, x, y, width, height }
succeeded_count	number	Number of successfully generated images
failed_count	number	Number of failed images
query_canvas_overview - Query Canvas Overview
Parameter	Required	Description
project_path	Yes	Project path
sort_by	No	Sort method: "layer", "position", "type"
visible_only	No	Whether to show only visible elements

Return data (result.data):

Field	Type	Description
elements	array	Element list, each contains { id, name, type, size, position }
canvas_info.total_elements	number	Total element count
project_name	string	Project name
query_canvas_element - Query Element Details
Parameter	Required	Description
project_path	Yes	Project path
element_id	No	Element ID (choose one between element_id and src)
src	No	Image path (choose one between element_id and src, used to find element by image path)

Return data (result.data):

Field	Type	Description
size	{ width, height }	Element size, use for image-to-image
image_properties.src	string	Image path (for image elements)
id	string	Element ID
name	string	Element name
Key Rules
Coordinate System

Canvas uses absolute coordinate system:

Coordinate origin: Canvas top-left corner is (0, 0)
Coordinate direction: X-axis increases rightward, Y-axis increases downward
x, y coordinate meaning: Represents the top-left corner position of the element (absolute coordinates relative to canvas)
Infinite canvas: Elements can be placed at any position
Image Processing Principles
Do not modify original image files - All content changes must create new elements
Do not delete elements - Never delete elements under any circumstances
Do not modify image content through properties - Cannot change image content in any way (e.g., changing colors, adding text)
Use generate_images_to_canvas for content changes - Create new elements while keeping original elements unchanged
"Add XX to image" means image-to-image - Generate images containing new content, NOT create separate XX element on canvas
Operation Flow Principles
Canvas Selection: By default, use the same canvas - Unless user explicitly requests a new canvas
Prioritize finding or reusing existing projects, avoid unnecessary project creation
Only create new projects when user explicitly expresses intent like "create new canvas" or "create new project"
Must query existing canvases before operations - Use query_canvas_overview
Do not assume file paths - Must reference paths based on query results
Query original image size before image-to-image - Use query_canvas_element with src parameter
Image Size Guide

Size format: 'widthxheight', e.g., '2048x2048'

Available sizes: Select from "当前图片生成模型可用的尺寸选项" in the user message

Common sizes (use when no available sizes in configuration):

'2048x2048' - 2K square (recommended, suitable for most scenarios)
'2304x1728' - Horizontal rectangle
'1728x2304' - Vertical rectangle
'2560x1440' - 16:9 horizontal
'1440x2560' - 9:16 vertical
'2496x1664' - 3:2 horizontal
'1664x2496' - 2:3 vertical
'3024x1296' - Ultra-wide horizontal

Image-to-image size handling:

If user hasn't explicitly requested a specific size, use the reference image's original size
If user explicitly specified a size, use the user-specified size
AI Generation Mode Selection
Mode 1: Independent Images of Different Themes

Generate images of different themes → Use multiple prompts (max 6)

from sdk.tool import tool

result = tool.call('generate_images_to_canvas', {
    "project_path": "landmarks",
    "name": "北京景点",
    "prompts": ["长城全景", "故宫太和殿", "天坛祈年殿", "颐和园昆明湖"],
    "size": "2048x2048"
}))

Mode 2: Style-Consistent Variants (Set)

Generate style-consistent variants → Use single prompt + image_count (max 4)

from sdk.tool import tool

result = tool.call('generate_images_to_canvas', {
    "project_path": "product",
    "name": "产品图",
    "prompts": ["产品摄影，多角度展示"],
    "image_count": 4,
    "size": "2048x2048"
}))

Mode 3: Image-to-Image (Based on Reference)

Generate new images based on existing images, suitable for design modifications or processing design markers.

Important: Must query original image size before image-to-image and use the same size

# Step 1: Query original image size by src
from sdk.tool import tool

result = tool.call('query_canvas_element', {
    "project_path": "my-design",
    "src": "my-design/images/cat.jpg"
})

# Step 2: Use result.data to get original size
if result.ok and result.data:
    width = result.data['size']['width']
    height = result.data['size']['height']
    src = result.data['image_properties']['src']

    # Step 3: Generate with same size
    result2 = tool.call('generate_images_to_canvas', {
        "project_path": "my-design",
        "name": "修改后的猫",
        "image_paths": [src],
        "prompts": ["将右上角的耳朵改为红色，保持其他部分不变"],
        "size": f"{width}x{height}"
    })

Image-to-Image Core Principles

When user provides reference images, follow these core principles:

Must use reference images - Include image_paths parameter, emphasize visual consistency in prompts
Maintain subject integrity - Don't add content not in original, keep product count and types consistent
Separate subject from style - Can change photography style, background, lighting, but not subject's features
Precise requirement delivery - Write every user keyword into Prompt, clearly state how to use reference

Need detailed explanation? For complex image-to-image scenarios (e.g., product design, brand consistency requirements), read: reference/image-generation.md

Design Marker Processing
What is Design Marker

Users mark areas on images that need modification or content addition. Format: [@design_marker:marker_name]

Example information:

[@design_marker:红色耳朵]
- Image location: my-design/images/dog.jpg
- Marked area: Small area at top right of image
- Coordinates: Top left (64.0%, 7.0%)

Processing Steps
Parse marker information - Extract image location, marked area, user requirements from marker
Query original image size - Use query_canvas_element(src=...)
Construct Prompt - [location] + [modification] + [keep original]
Call image-to-image - Use generate_images_to_canvas with image_paths parameter

Important: If user message contains [@design_marker:xxx] markers, MUST read detailed processing workflow: reference/design-marker.md

Tool Selection Decision Tree
Need to create new canvas?
├─ Yes → create_design_project
└─ No → Continue

Need to generate AI images?
├─ Yes → generate_images_to_canvas
│   ├─ Have reference? → First query_canvas_element (src) to get size
│   ├─ Different themes? → Multiple prompts
│   └─ Style-consistent? → Single prompt + image_count
└─ No → Continue

Need to search web images?
├─ Yes → See reference/image-search.md
└─ No → Continue

Need to query information?
├─ Canvas overview → query_canvas_overview
├─ Element details (known ID) → query_canvas_element (element_id)
└─ Element details (known image path) → query_canvas_element (src)

Web Image Search

To use web image search: See reference/image-search.md

Weekly Installs
14
Repository
dtyq/magic
GitHub Stars
4.8K
First Seen
Mar 21, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn