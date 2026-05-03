---
rating: ⭐⭐⭐
title: github-image-hosting
url: https://skills.sh/img402/skills/github-image-hosting
---

# github-image-hosting

skills/img402/skills/github-image-hosting
github-image-hosting
Installation
$ npx skills add https://github.com/img402/skills --skill github-image-hosting
SKILL.md
Image Upload for GitHub

Upload an image to img402.dev's free tier and embed the returned URL in GitHub markdown.

Quick reference
# Upload (multipart)
curl -s -X POST https://img402.dev/api/free -F image=@/tmp/screenshot.png

# Response
# {"url":"https://i.img402.dev/aBcDeFgHiJ.png","id":"aBcDeFgHiJ","contentType":"image/png","sizeBytes":182400,"expiresAt":"2026-02-17T..."}

Workflow
Get image: Use an existing file, or capture a screenshot:
screencapture -x /tmp/screenshot.png        # macOS — full screen
screencapture -xw /tmp/screenshot.png       # macOS — frontmost window

Verify size: Must be under 1MB. If larger, resize:
sips -Z 1600 /tmp/screenshot.png  # macOS — scale longest edge to 1600px

Upload:
curl -s -X POST https://img402.dev/api/free -F image=@/tmp/screenshot.png

Embed the returned url in GitHub markdown:
![Screenshot description](https://i.img402.dev/aBcDeFgHiJ.png)

GitHub integration

Use gh CLI to embed images in PRs and issues:

# Add to PR description
gh pr edit --body "$(gh pr view --json body -q .body)

![Screenshot](https://i.img402.dev/aBcDeFgHiJ.png)"

# Add as PR comment
gh pr comment --body "![Screenshot](https://i.img402.dev/aBcDeFgHiJ.png)"

# Add to issue
gh issue comment 123 --body "![Screenshot](https://i.img402.dev/aBcDeFgHiJ.png)"

Constraints
Max size: 1MB
Retention: 7 days — suitable for PR reviews, not permanent docs
Formats: PNG, JPEG, GIF, WebP
Rate limit: 1,000 free uploads/day (global)
No auth required
Tips
Prefer PNG for UI screenshots (sharp text). Use JPEG for photos.
If a screenshot is too large, reduce dimensions with sips -Z 1600 before uploading.
When adding to a PR body or comment, use gh pr comment or gh pr edit with the image markdown.
Paid tier

For permanent images (1 year, 5MB max), use the paid endpoint at $0.01 USDC via x402. See https://img402.dev/blog/paying-x402-apis for details.

Weekly Installs
39
Repository
img402/skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass