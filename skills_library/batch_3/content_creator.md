---
title: content-creator
url: https://skills.sh/sickn33/antigravity-awesome-skills/content-creator
---

# content-creator

skills/sickn33/antigravity-awesome-skills/content-creator
content-creator
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill content-creator
Summary

Brand voice analysis, SEO optimization, and platform-specific content frameworks for consistent marketing.

Includes brand voice analyzer to establish and maintain consistent tone across content, plus SEO optimizer that scores content and provides keyword density and structure recommendations
Provides content frameworks and templates for blog posts, social media, and content calendars, with platform-specific optimization guidelines
Supports batch content creation workflows with 40/25/25/10 content pillar ratios and integration points for analytics, scheduling, and email marketing platforms
Built-in best practices cover keyword research (500-5000 monthly search volume), heading structure, internal/external linking, and platform-appropriate formatting
SKILL.md
Content Creator

Professional-grade brand voice analysis, SEO optimization, and platform-specific content frameworks.

When to Use

Use this skill when writing blog posts, creating social media content, establishing brand voice, optimizing content for SEO, or planning content calendars.

Keywords

content creation, blog posts, SEO, brand voice, social media, content calendar, marketing content, content strategy, content marketing, brand consistency, content optimization, social media marketing, content planning, blog writing, content frameworks, brand guidelines, social media strategy

Quick Start
For Brand Voice Development
Run scripts/brand_voice_analyzer.py on existing content to establish baseline
Review references/brand_guidelines.md to select voice attributes
Apply chosen voice consistently across all content
For Blog Content Creation
Choose template from references/content_frameworks.md
Research keywords for topic
Write content following template structure
Run scripts/seo_optimizer.py [file] [primary-keyword] to optimize
Apply recommendations before publishing
For Social Media Content
Review platform best practices in references/social_media_optimization.md
Use appropriate template from references/content_frameworks.md
Optimize based on platform-specific guidelines
Schedule using assets/content_calendar_template.md
Core Workflows
Establishing Brand Voice (First Time Setup)

When creating content for a new brand or client:

Analyze Existing Content (if available)

python scripts/brand_voice_analyzer.py existing_content.txt


Define Voice Attributes

Review brand personality archetypes in references/brand_guidelines.md
Select primary and secondary archetypes
Choose 3-5 tone attributes
Document in brand guidelines

Create Voice Sample

Write 3 sample pieces in chosen voice
Test consistency using analyzer
Refine based on results
Creating SEO-Optimized Blog Posts

Keyword Research

Identify primary keyword (search volume 500-5000/month)
Find 3-5 secondary keywords
List 10-15 LSI keywords

Content Structure

Use blog template from references/content_frameworks.md
Include keyword in title, first paragraph, and 2-3 H2s
Aim for 1,500-2,500 words for comprehensive coverage

Optimization Check

python scripts/seo_optimizer.py blog_post.md "primary keyword" "secondary,keywords,list"


Apply SEO Recommendations

Adjust keyword density to 1-3%
Ensure proper heading structure
Add internal and external links
Optimize meta description
Social Media Content Creation

Platform Selection

Identify primary platforms based on audience
Review platform-specific guidelines in references/social_media_optimization.md

Content Adaptation

Start with blog post or core message
Use repurposing matrix from references/content_frameworks.md
Adapt for each platform following templates

Optimization Checklist

Platform-appropriate length
Optimal posting time
Correct image dimensions
Platform-specific hashtags
Engagement elements (polls, questions)
Content Calendar Planning

Monthly Planning

Copy assets/content_calendar_template.md
Set monthly goals and KPIs
Identify key campaigns/themes

Weekly Distribution

Follow 40/25/25/10 content pillar ratio
Balance platforms throughout week
Align with optimal posting times

Batch Creation

Create all weekly content in one session
Maintain consistent voice across pieces
Prepare all visual assets together
Key Scripts
brand_voice_analyzer.py

Analyzes text content for voice characteristics, readability, and consistency.

Usage: python scripts/brand_voice_analyzer.py <file> [json|text]

Returns:

Voice profile (formality, tone, perspective)
Readability score
Sentence structure analysis
Improvement recommendations
seo_optimizer.py

Analyzes content for SEO optimization and provides actionable recommendations.

Usage: python scripts/seo_optimizer.py <file> [primary_keyword] [secondary_keywords]

Returns:

SEO score (0-100)
Keyword density analysis
Structure assessment
Meta tag suggestions
Specific optimization recommendations
Reference Guides
When to Use Each Reference

references/brand_guidelines.md

Setting up new brand voice
Ensuring consistency across content
Training new team members
Resolving voice/tone questions

references/content_frameworks.md

Starting any new content piece
Structuring different content types
Creating content templates
Planning content repurposing

references/social_media_optimization.md

Platform-specific optimization
Hashtag strategy development
Understanding algorithm factors
Setting up analytics tracking
Best Practices
Content Creation Process
Always start with audience need/pain point
Research before writing
Create outline using templates
Write first draft without editing
Optimize for SEO
Edit for brand voice
Proofread and fact-check
Optimize for platform
Schedule strategically
Quality Indicators
SEO score above 75/100
Readability appropriate for audience
Consistent brand voice throughout
Clear value proposition
Actionable takeaways
Proper visual formatting
Platform-optimized
Common Pitfalls to Avoid
Writing before researching keywords
Ignoring platform-specific requirements
Inconsistent brand voice
Over-optimizing for SEO (keyword stuffing)
Missing clear CTAs
Publishing without proofreading
Ignoring analytics feedback
Performance Metrics

Track these KPIs for content success:

Content Metrics
Organic traffic growth
Average time on page
Bounce rate
Social shares
Backlinks earned
Engagement Metrics
Comments and discussions
Email click-through rates
Social media engagement rate
Content downloads
Form submissions
Business Metrics
Leads generated
Conversion rate
Customer acquisition cost
Revenue attribution
ROI per content piece
Integration Points

This skill works best with:

Analytics platforms (Google Analytics, social media insights)
SEO tools (for keyword research)
Design tools (for visual content)
Scheduling platforms (for content distribution)
Email marketing systems (for newsletter content)
Quick Commands
# Analyze brand voice
python scripts/brand_voice_analyzer.py content.txt

# Optimize for SEO
python scripts/seo_optimizer.py article.md "main keyword"

# Check content against brand guidelines
grep -f references/brand_guidelines.md content.txt

# Create monthly calendar
cp assets/content_calendar_template.md this_month_calendar.md

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
677
Repository
sickn33/antigra…e-skills
GitHub Stars
36.1K
First Seen
Jan 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass