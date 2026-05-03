---
title: blog-post
url: https://skills.sh/langchain-ai/deepagents/blog-post
---

# blog-post

skills/langchain-ai/deepagents/blog-post
blog-post
Installation
$ npx skills add https://github.com/langchain-ai/deepagents --skill blog-post
Summary

Long-form blog post writing with research delegation, structured content templates, and AI-generated cover images.

Delegates research to subagents before writing, storing findings in markdown for reference and context
Enforces a five-part post structure: hook, context, main content (3–5 sections), practical application, and conclusion with call-to-action
Generates SEO-optimized cover images using detailed prompts covering subject, style, composition, color, and lighting
Outputs posts to blogs/<slug>/post.md with matching cover images at blogs/<slug>/hero.png; both are required for completion
Includes SEO best practices: keyword placement, meta descriptions, and title length guidelines
SKILL.md
Blog Post Writing Skill
Research First (Required)

Before writing any blog post, you MUST delegate research:

Use the task tool with subagent_type: "researcher"
In the description, specify BOTH the topic AND where to save:
task(
    subagent_type="researcher",
    description="Research [TOPIC]. Save findings to research/[slug].md"
)


Example:

task(
    subagent_type="researcher",
    description="Research the current state of AI agents in 2025. Save findings to research/ai-agents-2025.md"
)

After research completes, read the findings file before writing
Output Structure (Required)

Every blog post MUST have both a post AND a cover image:

blogs/
└── <slug>/
    ├── post.md        # The blog post content
    └── hero.png       # REQUIRED: Generated cover image


Example: A post about "AI Agents in 2025" → blogs/ai-agents-2025/

You MUST complete both steps:

Write the post to blogs/<slug>/post.md
Generate a cover image using generate_image and save to blogs/<slug>/hero.png

A blog post is NOT complete without its cover image.

Blog Post Structure

Every blog post should follow this structure:

1. Hook (Opening)
Start with a compelling question, statistic, or statement
Make the reader want to continue
Keep it to 2-3 sentences
2. Context (The Problem)
Explain why this topic matters
Describe the problem or opportunity
Connect to the reader's experience
3. Main Content (The Solution)
Break into 3-5 main sections with H2 headers
Each section covers one key point
Include code examples, diagrams, or screenshots where helpful
Use bullet points for lists
4. Practical Application
Show how to apply the concepts
Include step-by-step instructions if applicable
Provide code snippets or templates
5. Conclusion & CTA
Summarize key takeaways (3 bullets max)
End with a clear call-to-action
Link to related resources
Cover Image Generation

After writing the post, generate a cover image using the generate_cover tool:

generate_cover(prompt="A detailed description of the image...", slug="your-blog-slug")


The tool saves the image to blogs/<slug>/hero.png.

Writing Effective Image Prompts

Structure your prompt with these elements:

Subject: What is the main focus? Be specific and concrete.
Style: Art direction (minimalist, isometric, flat design, 3D render, watercolor, etc.)
Composition: How elements are arranged (centered, rule of thirds, symmetrical)
Color palette: Specific colors or mood (warm earth tones, cool blues and purples, high contrast)
Lighting/Atmosphere: Soft diffused light, dramatic shadows, golden hour, neon glow
Technical details: Aspect ratio considerations, negative space for text overlay
Example Prompts

For a technical blog post:

Isometric 3D illustration of interconnected glowing cubes representing AI agents, each cube has subtle circuit patterns. Cubes connected by luminous data streams. Deep navy background (#0a192f) with electric blue (#64ffda) and soft purple (#c792ea) accents. Clean minimal style, lots of negative space at top for title. Professional tech aesthetic.


For a tutorial/how-to:

Clean flat illustration of hands typing on a keyboard with abstract code symbols floating upward, transforming into lightbulbs and gears. Warm gradient background from soft coral to light peach. Friendly, approachable style. Centered composition with space for text overlay.


For thought leadership:

Abstract visualization of a human silhouette profile merging with geometric neural network patterns. Split composition - organic watercolor texture on left transitioning to clean vector lines on right. Muted sage green and warm terracotta color scheme. Contemplative, forward-thinking mood.

SEO Considerations
Include the main keyword in the title and first paragraph
Use the keyword naturally 3-5 times throughout
Keep the title under 60 characters
Write a meta description (150-160 characters)
Quality Checklist

Before finishing:

 Post saved to blogs/<slug>/post.md
 Hero image generated at blogs/<slug>/hero.png
 Hook grabs attention in first 2 sentences
 Each section has a clear purpose
 Conclusion summarizes key points
 CTA tells reader what to do next
Weekly Installs
970
Repository
langchain-ai/deepagents
GitHub Stars
22.1K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass