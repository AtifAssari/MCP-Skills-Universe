---
rating: ⭐⭐
title: cloudinary-docs
url: https://skills.sh/cloudinary-devs/skills/cloudinary-docs
---

# cloudinary-docs

skills/cloudinary-devs/skills/cloudinary-docs
cloudinary-docs
Installation
$ npx skills add https://github.com/cloudinary-devs/skills --skill cloudinary-docs
SKILL.md
Cloudinary Documentation

Helps developers integrate Cloudinary into their applications by providing documentation and code examples retrieved directly from the optimized markdown files in the Cloudinary documentation.

When to Use
When a user asks questions or requests code implementation relating to image or video upload, management, optimization, or transformations (resizing, applying effects, visual improvements, adding overlays, generative AI, etc.)
User asks about Cloudinary SDKs, upload APIs, or integration guides
General Cloudinary documentation lookup (account settings, webhooks, DAM features)
Looking up specific Cloudinary API endpoints or SDK methods
Use this skill in conjunction with more specialized Cloudinary skills when relevant.
Instructions

When answering image and video upload, management, optimization, or transformation questions or when implementing Cloudinary code:

First, get the documentation index using llms.txt with the llms.txt URL - https://cloudinary.com/documentation/llms.txt
Analyze the llms.txt content to understand what documentation pages are available
Reflect on the user's question and identify which specific documentation URLs would be most relevant
Navigate to the specific relevant documentation URLs from the llms.txt index (you can make multiple calls)
Use the fetched documentation to provide a comprehensive, accurate answer or code implementation. When relevant, use in conjunction with more specialized Cloudinary skills like cloudinary-transformations. The best practices defined in the specialized skills should guide which doc instructions to use.

Example workflows:

Example 1: Upload question

User asks: "How do I upload images to Cloudinary?"
You retrieve the llms.txt index: https://cloudinary.com/documentation/llms.txt
You analyze the llms.txt content to understand what documentation pages are available
You identify relevant pages like "image_upload.md" or "upload_api.md"
You retrieve those specific pages from the llms.txt index
You provide an answer with code examples and citations

Example 2: Transformation question

User asks: "How do I resize and crop images?"
You retrieve the llms.txt index
You identify relevant pages like "image_transformations.md" or "transformation_reference.md"
You fetch the specific documentation
You provide transformation syntax and examples

Example 3: SDK question

User asks: "What's the Node.js SDK for Cloudinary?"
You retrieve the llms.txt index
You identify SDK-related pages
You provide installation instructions and usage examples
Weekly Installs
95
Repository
cloudinary-devs/skills
GitHub Stars
3
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn