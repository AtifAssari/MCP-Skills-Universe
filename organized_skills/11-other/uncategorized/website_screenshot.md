---
rating: ⭐⭐
title: website-screenshot
url: https://skills.sh/html2png/skills/website-screenshot
---

# website-screenshot

skills/html2png/skills/website-screenshot
website-screenshot
Installation
$ npx skills add https://github.com/html2png/skills --skill website-screenshot
SKILL.md
Website Screenshot API

Capture screenshots of any live website via html2png.dev.

Endpoint
POST https://html2png.dev/api/screenshot

Request
curl -X POST "https://html2png.dev/api/screenshot" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com", "width": 1280, "fullPage": true}'

Parameters
Parameter	Type	Default	Description
url	string	required	Website URL to capture
width	int	1280	Viewport width
height	int	800	Viewport height
fullPage	bool	false	Capture entire scrollable page
format	string	png	png, webp, pdf
deviceScaleFactor	float	2	Retina scale (1-4)
delay	int	0	Wait ms before capture
omitBackground	bool	false	Transparent bg
colorScheme	string	-	light or dark
userAgent	string	-	Custom user agent
Response
{
  "success": true,
  "url": "https://html2png.dev/api/blob/screenshot-abc.png",
  "format": "png",
  "timestamp": "2025-01-27T10:30:00.000Z"
}

Examples
Basic Screenshot
curl -X POST "https://html2png.dev/api/screenshot" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://github.com"}'

Full Page Capture
curl -X POST "https://html2png.dev/api/screenshot" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com", "fullPage": true, "delay": 2000}'

Mobile Viewport
curl -X POST "https://html2png.dev/api/screenshot" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com", "width": 375, "height": 812, "deviceScaleFactor": 3}'

PDF Export
curl -X POST "https://html2png.dev/api/screenshot" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com", "format": "pdf", "fullPage": true}'

Dark Mode
curl -X POST "https://html2png.dev/api/screenshot" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com", "colorScheme": "dark"}'

JavaScript Example
const response = await fetch("https://html2png.dev/api/screenshot", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    url: "https://example.com",
    width: 1280,
    fullPage: true,
    delay: 1000,
  }),
});

const data = await response.json();
console.log(data.url);

Tips
Use delay for sites with heavy JavaScript or animations
fullPage captures the entire scrollable content
deviceScaleFactor=2 or higher for crisp text
No caching - each request captures fresh content
Rate Limits

50 requests/hour per IP.

Weekly Installs
36
Repository
html2png/skills
GitHub Stars
7
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn