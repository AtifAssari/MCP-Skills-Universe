---
title: hackernews
url: https://skills.sh/vm0-ai/vm0-skills/hackernews
---

# hackernews

skills/vm0-ai/vm0-skills/hackernews
hackernews
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill hackernews
Summary

Fetch Hacker News stories, comments, and user data via the free, open API.

Supports six story categories: top, best, new, Ask HN, Show HN, and job postings, plus real-time item and profile updates
Retrieve full item details including title, URL, score, comment count, and nested comment threads by item ID
Look up user profiles with karma scores, account creation dates, and submission history
No API key required; use direct curl calls with jq filtering to extract and process JSON responses
SKILL.md
How to Use
1. Get Top Stories

Fetch IDs of the current top 500 stories:

curl -s "https://hacker-news.firebaseio.com/v0/topstories.json" | jq '.[:10]'

2. Get Best Stories

Fetch the best stories (highest voted over time):

curl -s "https://hacker-news.firebaseio.com/v0/beststories.json" | jq '.[:10]'

3. Get New Stories

Fetch the newest stories:

curl -s "https://hacker-news.firebaseio.com/v0/newstories.json" | jq '.[:10]'

4. Get Ask HN Stories

Fetch "Ask HN" posts:

curl -s "https://hacker-news.firebaseio.com/v0/askstories.json" | jq '.[:10]'

5. Get Show HN Stories

Fetch "Show HN" posts:

curl -s "https://hacker-news.firebaseio.com/v0/showstories.json" | jq '.[:10]'

6. Get Job Stories

Fetch job postings:

curl -s "https://hacker-news.firebaseio.com/v0/jobstories.json" | jq '.[:10]'

Item Details
7. Get Story/Comment/Job Details

Fetch full details for any item by ID. Replace <item-id> with the actual item ID:

curl -s "https://hacker-news.firebaseio.com/v0/item/<item-id>.json"


Response fields:

Field	Description
id	Unique item ID
type	story, comment, job, poll, pollopt
by	Username of author
time	Unix timestamp
title	Story title (stories only)
url	Story URL (if external link)
text	Content text (Ask HN, comments)
score	Upvote count
descendants	Total comment count
kids	Array of child comment IDs
8. Get Multiple Stories with Details

Fetch top 5 stories with full details. Replace <item-id> with the actual item ID:

curl -s "https://hacker-news.firebaseio.com/v0/topstories.json" | jq '.[:5][]' | while read id; do
  curl -s "https://hacker-news.firebaseio.com/v0/item/${id}.json" | jq '{id, title, score, url, by}'
done

9. Get Story with Comments

Fetch a story and its top-level comments. Replace <story-id> with the actual story ID:

curl -s "https://hacker-news.firebaseio.com/v0/item/<story-id>.json" | jq '{title, score, descendants, kids}'


Then for each comment ID in the kids array, replace <comment-id> with the actual comment ID:

curl -s "https://hacker-news.firebaseio.com/v0/item/<comment-id>.json" | jq '{by, text, score}'

User Data
10. Get User Profile

Fetch user details. Replace <username> with the actual username:

curl -s "https://hacker-news.firebaseio.com/v0/user/<username>.json"


Response fields:

Field	Description
id	Username
created	Account creation timestamp
karma	User's karma score
about	User bio (HTML)
submitted	Array of item IDs submitted
11. Get User's Recent Submissions

Fetch a user's recent submissions. Replace <username> with the actual username:

curl -s "https://hacker-news.firebaseio.com/v0/user/<username>.json" | jq '.submitted[:5]'

Real-time Updates
12. Get Max Item ID

Get the current largest item ID (useful for polling new items):

curl -s "https://hacker-news.firebaseio.com/v0/maxitem.json"

13. Get Changed Items and Profiles

Get recently changed items and profiles (for real-time updates):

curl -s "https://hacker-news.firebaseio.com/v0/updates.json"

Practical Examples
Fetch Today's Top 10 with Scores
curl -s "https://hacker-news.firebaseio.com/v0/topstories.json" | jq '.[:10][]' | while read id; do
  curl -s "https://hacker-news.firebaseio.com/v0/item/${id}.json" | jq -r '"\(.score) points | \(.title) | \(.url // "Ask HN")"'
done

Find High-Scoring Stories (100+ points)
curl -s "https://hacker-news.firebaseio.com/v0/topstories.json" | jq '.[:30][]' | while read id; do
  curl -s "https://hacker-news.firebaseio.com/v0/item/${id}.json" | jq -r 'select(.score >= 100) | "\(.score) | \(.title)"'
done

Get Latest AI/ML Related Stories
curl -s "https://hacker-news.firebaseio.com/v0/topstories.json" | jq '.[:50][]' | while read id; do
  curl -s "https://hacker-news.firebaseio.com/v0/item/${id}.json" | jq -r 'select(.title | test("AI|GPT|LLM|Machine Learning|Neural"; "i")) | "\(.score) | \(.title)"'
done

API Endpoints Summary
Endpoint	Description
/v0/topstories.json	Top 500 stories
/v0/beststories.json	Best stories
/v0/newstories.json	Newest 500 stories
/v0/askstories.json	Ask HN stories
/v0/showstories.json	Show HN stories
/v0/jobstories.json	Job postings
/v0/item/{id}.json	Item details
/v0/user/{id}.json	User profile
/v0/maxitem.json	Current max item ID
/v0/updates.json	Changed items/profiles
Guidelines
No rate limits documented: But be respectful, add delays for bulk fetching
Use jq for filtering: Filter JSON responses to extract needed data
Cache results: Stories don't change frequently, cache when possible
Batch requests carefully: Each item requires a separate API call
Handle nulls: Some fields may be null or missing (e.g., url for Ask HN)
Unix timestamps: All times are Unix timestamps, convert as needed
Weekly Installs
2.7K
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn