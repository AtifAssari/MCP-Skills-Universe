---
title: astro-cta-injector
url: https://skills.sh/nicepkg/ai-workflow/astro-cta-injector
---

# astro-cta-injector

skills/nicepkg/ai-workflow/astro-cta-injector
astro-cta-injector
Installation
$ npx skills add https://github.com/nicepkg/ai-workflow --skill astro-cta-injector
SKILL.md
Astro CTA Injector Skill
Purpose

This skill injects Call-to-Action (CTA) blocks into Astro site content. It supports:

Multiple CTA types (newsletter, product, custom)
Intelligent placement strategies
Content-based relevance scoring
Batch processing with preview
When to Use This Skill
User asks to "add CTAs to blog posts"
User wants to "inject newsletter signup" into content
User mentions "add product promotion" to posts
User needs to batch-add any type of content block to posts
User wants to "add calls to action" to their Astro site
Prerequisites
Astro site with content in .astro or .md files
Python 3.10+
BeautifulSoup4 for HTML parsing
Configuration

Create a config.json in the skill directory:

{
  "content_path": "./src/content/blog",
  "file_patterns": ["*.astro", "*.md"],
  "cta_types": {
    "newsletter": {
      "template": "newsletter.html",
      "default_placement": "after-paragraph-50%",
      "keywords": ["tip", "guide", "learn", "strategy"]
    },
    "product": {
      "template": "product.html",
      "default_placement": "end",
      "keywords": ["productivity", "task", "habit", "goal"]
    }
  },
  "output": {
    "state_file": "./state/cta_injection_progress.json",
    "backup_dir": "./backups",
    "report_file": "./reports/cta_injection_report.md"
  },
  "dry_run": true
}

Placement Strategies
Strategy	Description	Best For
end	After all content	Non-intrusive CTAs
after-paragraph-50%	After 50% of paragraphs	Mid-content engagement
after-paragraph-60%	After 60% of paragraphs	Later engagement
after-heading	After first H2	Early engagement
before-conclusion	Before last paragraph	Strong finish
CTA Templates

Templates are HTML files in the templates/ directory:

<!-- templates/newsletter.html -->
<aside class="cta-newsletter" data-cta-type="newsletter">
  <h3>{{title}}</h3>
  <p>{{description}}</p>
  <form action="{{form_url}}" method="post">
    <input type="email" placeholder="Your email" required />
    <button type="submit">Subscribe</button>
  </form>
</aside>


Variables:

{{title}} - CTA headline
{{description}} - CTA body text
{{form_url}} - Form submission URL
{{product_url}} - Product link
{{image_url}} - Image source
Workflow
Step 1: Score Posts for Relevance
python scripts/score_posts.py --content-path ./src/content/blog --cta-type newsletter

Step 2: Preview Injections
python scripts/preview_injection.py --input scored_posts.json --cta-type newsletter

Step 3: Apply Injections
python scripts/inject_ctas.py --input scored_posts.json --cta-type newsletter

Input Format

Scored posts JSON:

{
  "posts": [
    {
      "file_path": "./src/content/blog/my-post.astro",
      "title": "My Blog Post",
      "relevance_score": 8.5,
      "cta_type": "newsletter",
      "placement": "after-paragraph-50%",
      "cta_data": {
        "title": "Get More Tips Like This",
        "description": "Subscribe to my weekly newsletter"
      }
    }
  ]
}

Scoring Algorithm

Posts are scored for CTA relevance based on:

Keyword density - How many relevant keywords appear
Content length - Longer posts = better candidates
Topic match - Title and content topic alignment
Existing CTAs - Skip posts that already have CTAs

Scores range from 0-10. Default threshold: 5.0

Safety Features
Dry-run mode by default
Backup creation before any modifications
Duplicate detection - Won't inject if CTA already exists
Rollback capability - Restore from backups
Preview diffs - See exactly what will change
Example Usage

User: "Add a newsletter signup CTA to all my productivity-related blog posts"

Claude will:

Scan content directory for posts
Score posts for "newsletter" relevance using productivity keywords
Generate CTA HTML from template
Show preview of changes
Ask for confirmation
Inject CTAs into matching posts
Report results
Weekly Installs
44
Repository
nicepkg/ai-workflow
GitHub Stars
176
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass