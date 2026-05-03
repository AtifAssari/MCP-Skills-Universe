---
rating: ⭐⭐
title: seo-wordpress-manager
url: https://skills.sh/nicepkg/ai-workflow/seo-wordpress-manager
---

# seo-wordpress-manager

skills/nicepkg/ai-workflow/seo-wordpress-manager
seo-wordpress-manager
Installation
$ npx skills add https://github.com/nicepkg/ai-workflow --skill seo-wordpress-manager
SKILL.md
SEO WordPress Manager Skill
Purpose

This skill manages Yoast SEO metadata in WordPress sites via the WPGraphQL API. It enables batch updates of:

SEO titles
Meta descriptions
Focus keyphrases
Open Graph metadata
When to Use This Skill
User asks to "update SEO titles" or "fix meta descriptions"
User wants to batch process WordPress posts for SEO
User mentions Yoast SEO optimization
User needs to update SEO metadata across multiple posts
Prerequisites
WordPress Setup Required
WPGraphQL plugin installed and activated
WPGraphQL for Yoast SEO extension installed
Application Password created for authentication
Yoast SEO GraphQL Mutations

Add this to your theme's functions.php to enable mutations:

// Enable Yoast SEO mutations via WPGraphQL
add_action('graphql_register_types', function() {
    register_graphql_mutation('updatePostSeo', [
        'inputFields' => [
            'postId' => ['type' => 'Int', 'description' => 'Post ID'],
            'title' => ['type' => 'String', 'description' => 'SEO Title'],
            'metaDesc' => ['type' => 'String', 'description' => 'Meta Description'],
            'focusKeyphrase' => ['type' => 'String', 'description' => 'Focus Keyphrase'],
        ],
        'outputFields' => [
            'success' => ['type' => 'Boolean'],
            'post' => ['type' => 'Post'],
        ],
        'mutateAndGetPayload' => function($input) {
            $post_id = absint($input['postId']);

            if (!current_user_can('edit_post', $post_id)) {
                throw new \GraphQL\Error\UserError('You do not have permission to edit this post.');
            }

            if (isset($input['title'])) {
                update_post_meta($post_id, '_yoast_wpseo_title', sanitize_text_field($input['title']));
            }
            if (isset($input['metaDesc'])) {
                update_post_meta($post_id, '_yoast_wpseo_metadesc', sanitize_textarea_field($input['metaDesc']));
            }
            if (isset($input['focusKeyphrase'])) {
                update_post_meta($post_id, '_yoast_wpseo_focuskw', sanitize_text_field($input['focusKeyphrase']));
            }

            return [
                'success' => true,
                'post' => get_post($post_id),
            ];
        }
    ]);
});

Configuration

Create a config.json in the skill directory:

{
  "wordpress": {
    "graphql_url": "https://your-site.com/graphql",
    "username": "your-username",
    "app_password": "your-app-password"
  },
  "batch": {
    "size": 10,
    "delay_seconds": 1
  },
  "state_file": "./seo_update_progress.json"
}


Or use environment variables:

WP_GRAPHQL_URL
WP_USERNAME
WP_APP_PASSWORD
Workflow
Step 1: Analyze Posts for SEO Issues
python scripts/analyze_seo.py --all --output analysis.json


This fetches posts and identifies SEO issues (missing titles, too long descriptions, etc.). Output includes instructions for Claude to generate optimized SEO content.

Step 2: Generate Optimized SEO Content

Claude analyzes the analysis.json output and generates a changes.json file with:

Optimized SEO titles (50-60 chars)
Compelling meta descriptions (150-160 chars)
Relevant focus keyphrases
Step 3: Preview Changes (Dry Run)
python scripts/preview_changes.py --input changes.json

Step 4: Apply Updates
python scripts/yoast_batch_updater.py --input changes.json --apply

Step 5: Resume if Interrupted
python scripts/yoast_batch_updater.py --resume

Input Format

The skill expects a JSON file with changes:

{
  "updates": [
    {
      "post_id": 123,
      "post_title": "Original Post Title",
      "current": {
        "seo_title": "Old Title | Site Name",
        "meta_desc": "Old description"
      },
      "new": {
        "seo_title": "New Optimized Title | Site Name",
        "meta_desc": "New compelling meta description under 160 chars"
      }
    }
  ]
}

Output

The skill produces:

Preview report showing before/after for each post
Progress state file for resuming interrupted batches
Final report with success/failure counts
Safety Features
Dry-run mode by default - preview before applying
Confirmation prompt before batch updates
Progress tracking - resume interrupted sessions
Rate limiting - configurable delay between API calls
Backup - logs current values before changing
Example Usage

User: "Update the meta descriptions for all posts in the 'tutorials' category to be more compelling"

Claude will:

Run analyze_seo.py to fetch posts and identify SEO issues
Analyze each post's content and current SEO data
Generate optimized titles, descriptions, and keyphrases
Create a changes.json file with the improvements
Run preview_changes.py to show before/after comparison
Ask for confirmation
Run yoast_batch_updater.py --apply to apply changes
Report results with success/failure counts
Weekly Installs
46
Repository
nicepkg/ai-workflow
GitHub Stars
176
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn