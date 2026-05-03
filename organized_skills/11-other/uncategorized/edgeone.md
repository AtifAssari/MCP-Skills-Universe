---
rating: ⭐⭐
title: edgeone
url: https://skills.sh/aahl/skills/edgeone
---

# edgeone

skills/aahl/skills/edgeone
edgeone
Installation
$ npx skills add https://github.com/aahl/skills --skill edgeone
SKILL.md
EdgeOne

Deploy HTML content to EdgeOne Pages, return the public URL. No login required, no API key required.

Deploy HTML

HTML or text content to deploy. Provide complete HTML or text content you want to publish, and the system will return a public URL where your content can be accessed.

npx -y mcporter call mcp-on-edge.edgeone.app/mcp-server.deploy-html value="<html>Content</html>"
npx -y mcporter call mcp-on-edge.edgeone.app/mcp-server.deploy-html value="$(cat index.html)"

Weekly Installs
528
Repository
aahl/skills
GitHub Stars
120
First Seen
1 day ago
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn