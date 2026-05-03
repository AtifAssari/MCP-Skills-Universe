---
rating: ⭐⭐⭐
title: twitter-automation
url: https://skills.sh/inference-sh/skills/twitter-automation
---

# twitter-automation

skills/inference-sh/skills/twitter-automation
twitter-automation
Originally frominfsh-skills/skills
Installation
$ npx skills add https://github.com/inference-sh/skills --skill twitter-automation
Summary

Post, like, retweet, and manage Twitter/X accounts via CLI commands.

Nine app commands covering tweet posting with media, liking, retweeting, DM sending, user following, and profile retrieval
Supports media attachment through URLs, enabling workflows that combine image or video generation with social posting
Requires inference.sh CLI authentication; integrates with other inference.sh skills for end-to-end content creation and distribution pipelines
SKILL.md
Twitter/X Automation

Automate Twitter/X via inference.sh CLI.

Quick Start

Requires inference.sh CLI (belt). Install instructions

belt login

# Post a tweet
belt app run x/post-tweet --input '{"text": "Hello from inference.sh!"}'

Available Apps
App	App ID	Description
Post Tweet	x/post-tweet	Post text tweets
Create Post	x/post-create	Post with media
Like Post	x/post-like	Like a tweet
Retweet	x/post-retweet	Retweet a post
Delete Post	x/post-delete	Delete a tweet
Get Post	x/post-get	Get tweet by ID
Send DM	x/dm-send	Send direct message
Follow User	x/user-follow	Follow a user
Get User	x/user-get	Get user profile
Examples
Post a Tweet
belt app run x/post-tweet --input '{"text": "Just shipped a new feature! 🚀"}'

Post with Media
belt app sample x/post-create --save input.json

# Edit input.json:
# {
#   "text": "Check out this AI-generated image!",
#   "media_url": "https://your-image-url.jpg"
# }

belt app run x/post-create --input input.json

Like a Tweet
belt app run x/post-like --input '{"tweet_id": "1234567890"}'

Retweet
belt app run x/post-retweet --input '{"tweet_id": "1234567890"}'

Send a DM
belt app run x/dm-send --input '{
  "recipient_id": "user_id_here",
  "text": "Hey! Thanks for the follow."
}'

Follow a User
belt app run x/user-follow --input '{"username": "elonmusk"}'

Get User Profile
belt app run x/user-get --input '{"username": "OpenAI"}'

Get Tweet Details
belt app run x/post-get --input '{"tweet_id": "1234567890"}'

Delete a Tweet
belt app run x/post-delete --input '{"tweet_id": "1234567890"}'

Workflow: Generate AI Image and Post
# 1. Generate image
belt app run falai/flux-dev-lora --input '{"prompt": "sunset over mountains"}' > image.json

# 2. Post to Twitter with the image URL
belt app run x/post-create --input '{
  "text": "AI-generated art of a sunset 🌅",
  "media_url": "<image-url-from-step-1>"
}'

Workflow: Generate and Post Video
# 1. Generate video
belt app run google/veo-3-1-fast --input '{"prompt": "waves on a beach"}' > video.json

# 2. Post to Twitter
belt app run x/post-create --input '{
  "text": "AI-generated video 🎬",
  "media_url": "<video-url-from-step-1>"
}'

Related Skills
# Full platform skill (all 250+ apps)
npx skills add inference-sh/skills@infsh-cli

# Image generation (create images to post)
npx skills add inference-sh/skills@ai-image-generation

# Video generation (create videos to post)
npx skills add inference-sh/skills@ai-video-generation

# AI avatars (create presenter videos)
npx skills add inference-sh/skills@ai-avatar-video


Browse all apps: belt app list

Documentation
X.com Integration - Setting up Twitter/X integration
X.com Integration Example - Complete Twitter workflow
Apps Overview - Understanding the app ecosystem
Weekly Installs
612
Repository
inference-sh/skills
GitHub Stars
395
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn