---
rating: ⭐⭐⭐
title: rss-fetch
url: https://skills.sh/vm0-ai/vm0-skills/rss-fetch
---

# rss-fetch

skills/vm0-ai/vm0-skills/rss-fetch
rss-fetch
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill rss-fetch
SKILL.md
How to Use
1. Fetch Raw RSS Feed
curl -s "https://hnrss.org/frontpage" | head -100

2. Parse RSS with xmllint

Extract titles from RSS feed:

curl -s "https://hnrss.org/frontpage" | xmllint --xpath '//item/title/text()' - 2>/dev/null


Extract titles and links:

curl -s "https://hnrss.org/frontpage" | xmllint --format - | grep -E '<title>|<link>' | head -20

3. Get Items with Details
curl -s "https://hnrss.org/frontpage" | xmllint --xpath '//item' - 2>/dev/null | xmllint --format - | head -50

4. Parse Atom Feeds

Atom feeds use <entry> instead of <item>:

curl -s "https://github.com/blog.atom" | xmllint --xpath '//entry/title/text()' - 2>/dev/null

Popular RSS Feeds
Source	URL
Hacker News	https://hnrss.org/frontpage
HN Best	https://hnrss.org/best
TechCrunch	https://techcrunch.com/feed/
Ars Technica	https://feeds.arstechnica.com/arstechnica/index
The Verge	https://www.theverge.com/rss/index.xml
Reddit (any sub)	https://www.reddit.com/r/programming/.rss
GitHub Blog	https://github.blog/feed/
Examples
Fetch Hacker News Top Stories
curl -s "https://hnrss.org/frontpage?count=10" | xmllint --xpath '//item/title/text()' - 2>/dev/null | tr '\n' '\n'

Get Story Links
curl -s "https://hnrss.org/frontpage?count=5" | grep -oP '<link>\K[^<]+' | grep -v hnrss

Fetch Multiple Feeds
FEEDS=(
  "https://hnrss.org/frontpage?count=5"
  "https://techcrunch.com/feed/"
)

for feed in "${FEEDS[@]}"; do
  echo "=== $feed ==="
  curl -s "$feed" | xmllint --xpath '//item/title/text()' - 2>/dev/null | head -5
  echo ""
done

Extract Title, Link, and Date
curl -s "https://hnrss.org/frontpage?count=3" | xmllint --format - | awk '
  /<item>/ { in_item=1 }
  /<\/item>/ { in_item=0; print "---" }
  in_item && /<title>/ { gsub(/<[^>]*>/, ""); print "Title: " $0 }
  in_item && /<link>/ { gsub(/<[^>]*>/, ""); print "Link: " $0 }
  in_item && /<pubDate>/ { gsub(/<[^>]*>/, ""); print "Date: " $0 }
  '

Save Feed to File
curl -s "https://hnrss.org/frontpage" -o /tmp/hn-feed.xml
xmllint --xpath '//item/title/text()' /tmp/hn-feed.xml

HN RSS Options

Hacker News RSS (hnrss.org) supports parameters:

Parameter	Description
count=N	Number of items (default 20)
points=N	Minimum points
comments=N	Minimum comments
q=keyword	Search keyword
# Top stories with 100+ points
curl -s "https://hnrss.org/frontpage?points=100&count=10"

# Search for "AI" topics
curl -s "https://hnrss.org/frontpage?q=AI&count=10"

RSS vs Atom Format
Element	RSS	Atom
Container	<item>	<entry>
Title	<title>	<title>
Link	<link>	<link href="...">
Summary	<description>	<summary>
Date	<pubDate>	<published>
Guidelines
Check feed format: Use head first to see if it's RSS or Atom
Use xmllint: Best tool for XPath queries on XML
Handle errors: Some feeds may be slow or rate-limited
Respect robots.txt: Don't hammer feeds with requests
Cache results: Feeds don't update every second
Weekly Installs
41
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn