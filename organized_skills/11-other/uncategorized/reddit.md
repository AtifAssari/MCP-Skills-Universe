---
rating: ⭐⭐⭐
title: reddit
url: https://skills.sh/resciencelab/opc-skills/reddit
---

# reddit

skills/resciencelab/opc-skills/reddit
reddit
Installation
$ npx skills add https://github.com/resciencelab/opc-skills --skill reddit
Summary

Search and retrieve Reddit posts, comments, subreddit info, and user profiles via the public JSON API.

Requires no API key; uses Reddit's public JSON endpoint accessible by appending .json to any URL
Supports four main command categories: subreddit posts with sorting (hot, new, top, rising, controversial), cross-subreddit search, subreddit metadata, and user profiles with optional post history
Includes flexible filtering: sort by time range (hour through all-time), set result limits, and scope searches to specific subreddits
Rate limited to 100 requests per minute; all commands run as Python scripts from the skill directory
SKILL.md
Reddit Skill

Get posts, comments, subreddit info, and user profiles from Reddit via the public JSON API.

Prerequisites

No API key required! Reddit's public JSON API works without authentication.

Quick Check:

cd <skill_directory>
python3 scripts/get_posts.py python --limit 3

Commands

All commands run from the skill directory.

Subreddit Posts
python3 scripts/get_posts.py python --limit 20           # Hot posts (default)
python3 scripts/get_posts.py python --sort new --limit 20
python3 scripts/get_posts.py python --sort top --time week
python3 scripts/get_posts.py python --sort top --time all --limit 10

Search Posts
python3 scripts/search_posts.py "AI agent" --limit 20
python3 scripts/search_posts.py "MCP server" --subreddit ClaudeAI --limit 10
python3 scripts/search_posts.py "async python" --sort top --time year

Subreddit Info
python3 scripts/get_subreddit.py python
python3 scripts/get_subreddit.py ClaudeAI

Post & Comments
python3 scripts/get_post.py abc123                       # Get post by ID
python3 scripts/get_post.py abc123 --comments 50         # With more comments

User Profile
python3 scripts/get_user.py spez
python3 scripts/get_user.py spez --posts 10              # Include recent posts

Sort Options
Sort	Description	Time Options
hot	Trending posts (default)	-
new	Latest posts	-
top	Highest voted	hour, day, week, month, year, all
rising	Gaining traction	-
controversial	Mixed votes	hour, day, week, month, year, all
API Info
Method: Public JSON API (no auth needed)
Trick: Append .json to any Reddit URL
Rate Limit: 100 requests/minute
Docs: https://www.reddit.com/dev/api
Weekly Installs
2.1K
Repository
resciencelab/opc-skills
GitHub Stars
828
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn