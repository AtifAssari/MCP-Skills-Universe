---
rating: ⭐⭐
title: letzai-api
url: https://skills.sh/letz-ai/letzai-skill/letzai-api
---

# letzai-api

skills/letz-ai/letzai-skill/letzai-api
letzai-api
Installation
$ npx skills add https://github.com/letz-ai/letzai-skill --skill letzai-api
Summary

Generate AI images and videos with multiple model options, custom trained models, editing, and upscaling via LetzAI API.

Supports three image models (Nano Banana Pro, Flux2 Max, SeeDream) and three video models (VEO, Kling, Wan) with configurable resolution modes and dimensions
Includes context-based image editing, skin fixing, and upscaling with strength control (1-3x)
Custom trained models for persons, objects, and styles accessible via @modelname syntax in prompts
Asynchronous generation with polling pattern (3-second intervals for images/edits, 2-3 seconds for videos) until status reaches "ready"
Requires Bearer token authentication and paid LetzAI subscription; credit costs vary by model and resolution
SKILL.md
LetzAI API Integration Skill
Overview

This skill enables Claude to help users integrate with the LetzAI API for AI-powered image and video generation, editing, and upscaling. Users can also leverage custom-trained AI models (persons, objects, styles) via the @modelname syntax.

Authentication
Base URL: https://api.letz.ai
Authentication: Bearer token in Authorization header
Get API Key: letz.ai/subscription
API Documentation: api.letz.ai/doc
Setting Up Authentication
const headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer YOUR_API_KEY'
};

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer YOUR_API_KEY'
}

Core Workflows
1. Image Generation

Endpoint: POST /images

Required Parameters:

prompt (string): Text description of the desired image. Can include @modelname to use trained models.

Optional Parameters:

baseModel: AI model to use
"gemini-3-pro-image-preview" - Nano Banana Pro (recommended)
"flux2-max" - Flux2 Max
"seedream-4-5-251128" - SeeDream 4.5
mode: Resolution mode (varies by model)
Nano Banana Pro: "default", "2k", "4k"
Flux2 Max: "1k", "hd"
SeeDream: "2k", "4k"
width / height: Image dimensions (520-2160px)

Workflow:

POST to /images with parameters
Receive id in response
Poll GET /images/{id} every 3 seconds
When status === "ready", access imageVersions.original

For code examples, see examples/image_generation.js

2. Video Generation

Endpoint: POST /videos

Required Parameters:

prompt (string): Text description of the desired video
Source image (one of):
imageUrl: URL of source image
originalImageCompletionId: ID from previous image generation

Optional Parameters:

settings.mode: Video model
"default" - Default model
"veo31" - VEO 3.1
"kling26" - Kling 2.6
"wan25" - Wan 2.5
settings.duration: Video length in seconds (2-12 depending on model)

Workflow:

Ensure you have a source image (generate one first if needed)
POST to /videos with parameters
Receive id in response
Poll GET /videos/{id} every 2-3 seconds
When status === "ready", access videoPaths

For code examples, see examples/video_generation.py

3. Image Editing (Context Editing)

Endpoint: POST /image-edits

Required Parameters:

mode: Edit mode
"context" - AI editing (primary mode)
"skin" - Skin fix
prompt: Edit instruction (e.g., "change background to beach")
Source image (one of):
imageUrl: URL of source image
inputImageUrls[]: Array of source image URLs (max 9)
originalImageCompletionId: ID of previously generated LetzAI image

Optional Parameters:

settings.model: "gemini-3-pro-image-preview", "flux2-max", "seedream-4-5-251128"
settings.resolution: "2k" (HD) or "4k" (Ultra HD)
settings.aspect_ratio: "1:1", "16:9", "9:16", "4:3", "3:4", "21:9", "9:21"
baseModel: Alternative to settings.model
webhookUrl: Optional callback URL
organizationId: Optional org ID for billing

Workflow:

POST to /image-edits with parameters
Receive id in response
Poll GET /image-edits/{id} every 3 seconds
When status === "ready", access generatedImageCompletion.imageVersions.original

Note: Inpainting (mode: "in") and Outpainting (mode: "out") are deprecated - use Context Editing instead.

4. Image Upscaling

Endpoint: POST /upscales

Required Parameters:

Source image (one of):
imageUrl: URL of source image
imageCompletionId: ID from previous image generation

Optional Parameters:

strength: Upscale factor (1-3)

Workflow:

POST to /upscales with parameters
Receive id in response
Poll GET /upscales/{id} every 3 seconds
When status === "ready", access upscaled image
5. Custom AI Models (Trained Models)

LetzAI users can train custom AI models on persons, objects, or styles via the web interface. These trained models can be used in prompts via the @modelname syntax.

List Models Endpoint: GET /models

Query Parameters:

page: int (default: 1)
limit: int (default: 10)
sortBy: "createdAt" | "usages"
sortOrder: "ASC" | "DESC"
class: "person" | "object" | "style"

Get Model Details: GET /models/{id}

Model Classes:

person: Trained on photos of a specific person
object: Trained on product/object images
style: Trained on artistic style examples

Using Models in Prompts: Tag models with @modelname syntax:

@john_doe on the beach at sunset - Use a person model
A product photo featuring @my_product - Use an object model
Portrait in @vintage_style aesthetic - Use a style model

Note: Model training is done via the LetzAI web interface (letz.ai), not via API.

Workflow Decision Tree
User wants to create an image:
Determine appropriate model based on quality/cost needs
Use POST /images with appropriate baseModel
If using a trained model, include @modelname in the prompt
Poll GET /images/{id} every 3s until ready
Return imageVersions.original URL
User wants to use a custom trained model:
Use GET /models to list available trained models (filter by class if needed)
Include @modelname in the prompt when generating images
Generate image normally with POST /images
User wants to edit an existing image:
Obtain source image URL, inputImageUrls array, or originalImageCompletionId
Use POST /image-edits with mode="context"
Include settings for resolution, aspect_ratio, and model as needed
Poll GET /image-edits/{id} every 3s until ready
Return generatedImageCompletion.imageVersions.original
User wants to create a video:
Ensure they have a source image (URL or imageCompletionId)
If no source image, generate one first using /images
Use POST /videos with desired settings
Poll GET /videos/{id} every 2-3s until ready
Return video URL from videoPaths
User wants to upscale an image:
Obtain source image URL or imageCompletionId
Use POST /upscales with desired strength
Poll GET /upscales/{id} every 3s until ready
Return upscaled image URL
Status Polling Pattern

LetzAI uses asynchronous generation. After any POST request, you must poll the corresponding GET endpoint until the job completes.

Status Values
Status	Meaning
new	Job created, queued for processing
in progress / generating	Currently processing
ready	Complete - fetch URLs from response
failed	Error occurred - check error message
Polling Intervals
Images: Every 3 seconds
Videos: Every 2-3 seconds
Image Edits: Every 3 seconds
Upscales: Every 3 seconds

For detailed polling implementation, see examples/polling_pattern.md

Pricing Reference
Feature	Model	Credits
Image Gen	Nano Banana Pro	80/160/240 (1k/HD/4K)
Image Gen	Flux2 Max	60/120 (1k/HD)
Image Gen	SeeDream	80/160 (HD/4K)
Editing	Same as above	Same pricing
Video	Default	60 cr/sec (2-6 sec)
Video	VEO 3.1	1500-6000 cr (8 sec)
Video	Kling 2.6	750-1500 cr (5-10 sec)
Upscale	All	40 cr
Error Handling
Common HTTP Status Codes
Status	Meaning	Solution
401	Invalid or missing API key	Check Authorization header format
402	Insufficient credits	Top up at letz.ai/subscription
400	Invalid parameters	Verify baseModel, mode, dimensions
404	Resource not found	Check the ID is correct
429	Rate limited	Implement exponential backoff
500	Server error	Retry after delay
Error Response Format
{
  "error": "Error description",
  "code": "ERROR_CODE"
}

Limitations
Async Generation: All generation is asynchronous - must poll for results
Video Source: Video generation requires a source image
Reference Images: Maximum 9 reference images for image editing
Model Training: Cannot train custom AI models via API - use letz.ai web interface
API Key Required: Paid subscription required for API access
Quick Reference: API Endpoints
Endpoint	Method	Purpose
/images	GET	List user's images
/images	POST	Create image (prompt, baseModel, mode, width, height)
/images/{id}	GET	Get image status & URLs (poll every 3s)
/images/{id}/interruption	PUT	Stop image generation
/images/{id}/privacy	PUT	Change image privacy
/videos	GET	List user's videos
/videos	POST	Create video (prompt, imageUrl, settings)
/videos/{id}	GET	Get video status & URLs (poll every 2-3s)
/videos/{id}/interruption	PUT	Stop video generation
/videos/{id}/privacy	PUT	Change video privacy
/image-edits	GET	List user's edits
/image-edits	POST	Edit image (mode, prompt, imageUrl/inputImageUrls, settings)
/image-edits/{id}	GET	Get edit status & URLs (poll every 3s)
/upscales	POST	Upscale image (imageUrl/imageUrls, strength, mode, size)
/upscales/{id}	GET	Get upscale status & URLs (poll every 3s)
/models	GET	List trained AI models (filter by class: person/object/style)
/models/{id}	GET	Get specific model details
Key Response Fields
Images/Upscales: imageVersions.original, imageVersions["1920x1920"], imageVersions["640x640"]
Edits: generatedImageCompletion.imageVersions.original
Videos: videoPaths object, videoVersions array
Status values: new, in progress/generating, ready, failed
Additional Resources
API Documentation: api.letz.ai/doc
Developer Docs: letz.ai/docs/api
Detailed API Reference: api_reference.md
Code Examples: examples/
Weekly Installs
877
Repository
letz-ai/letzai-skill
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn