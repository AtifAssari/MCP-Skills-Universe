---
title: wechat-to-notebooklm
url: https://skills.sh/zstmfhy/wechat-to-notebooklm/wechat-to-notebooklm
---

# wechat-to-notebooklm

skills/zstmfhy/wechat-to-notebooklm/wechat-to-notebooklm
wechat-to-notebooklm
Installation
$ npx skills add https://github.com/zstmfhy/wechat-to-notebooklm --skill wechat-to-notebooklm
SKILL.md
WeChat to NotebookLM

Automatically sync WeChat Official Account articles to Google NotebookLM for AI-powered analysis, summarization, and content generation.

What This Does

This skill automates the entire workflow of getting a WeChat article into NotebookLM:

Fetches the article content from the URL
Converts to clean Markdown format
Creates a NotebookLM notebook (optionally with custom title)
Uploads the article as a source
Returns the notebook ID for further interaction
When to Use

Use this skill when you:

Have a WeChat Official Account article URL (mp.weixin.qq.com)
Want to save the article to NotebookLM for analysis
Want to create a podcast/video from the article
Want to chat with the article content using AI
Want to summarize or extract insights from the article

Example triggers:

"Sync this WeChat article to NotebookLM"
"Add this mp.weixin.qq.com link to my notebook"
"Create a notebook from this WeChat article"
"Save this article to NotebookLM"
Prerequisites

Before using this skill, ensure NotebookLM CLI is authenticated:

notebooklm login          # Opens browser for Google OAuth
notebooklm status         # Verify authentication

Workflow
Complete Sync Process

Step 1: Fetch Article Content

Use the web reader MCP tool to fetch the WeChat article:

mcp__web_reader__webReader
URL: <WeChat article URL>
return_format: markdown
retain_images: false (optional, saves bandwidth)


This returns the article content in Markdown format.

Step 2: Save Content to File

Save the fetched content to a temporary Markdown file:

# Extract title from content or use default
# Save to /tmp/<sanitized_title>.md


The file should be saved with a descriptive name based on the article title.

Step 3: Create NotebookLM Notebook

Create a new notebook with the article title:

notebooklm create "<article_title>" --json


Parse the JSON response to get the notebook ID:

{"notebook": {"id": "abc-123-def", "title": "..."}}


Step 4: Upload Article to Notebook

Add the Markdown file as a source to the notebook:

notebooklm source add /tmp/<article_title>.md --notebook <notebook_id> --json


Parse the response to get the source ID:

{"source": {"id": "source-xyz-789", "title": "...", "type": "text"}}


Step 5: Confirm Success

Report to the user:

Notebook title and ID
Source file name
Notebook ID for further use
Suggested next steps (ask questions, generate podcast, etc.)
Progress Updates

Provide brief, clear status updates:

✅ Fetching article from WeChat...
✅ Converting to Markdown...
✅ Creating notebook "Article Title"...
✅ Uploading to NotebookLM...
✅ Done! Notebook ID: abc-123-def

Output Summary

When complete, provide:

Successfully synced WeChat article to NotebookLM!

📓 Notebook: [Article Title]
   ID: abc-123-def

📄 Source: article_title.md
   ID: source-xyz-789

💡 Next steps:
   - Use: notebooklm use abc-123-def
   - Ask: notebooklm ask "Summarize this article"
   - Generate: notebooklm generate audio "Create a podcast"

Error Handling
Common Issues

1. Article URL is invalid or inaccessible

Error: Failed to fetch content
Solution: Verify the URL is correct and accessible
Alternative: Try copying the article content manually

2. NotebookLM authentication failed

Error: Auth/cookie error
Solution: Run notebooklm login again
Check: notebooklm status to verify

3. File upload failed

Error: Invalid file or upload error
Solution: Check if Markdown file was created correctly
Verify: File path and permissions

4. Notebook creation failed

Error: Rate limiting or API error
Solution: Wait a few minutes and retry
Alternative: Add to existing notebook with --notebook flag
Advanced Features
Add to Existing Notebook

If user wants to add to an existing notebook:

# Get list of notebooks
notebooklm list --json

# Use existing notebook ID
notebooklm source add /tmp/article.md --notebook <existing_notebook_id> --json

Batch Processing

For multiple WeChat articles:

# Create notebook once
notebooklm create "WeChat Articles Collection" --json

# Add multiple articles
for url in "${urls[@]}"; do
  # Fetch, save, upload to same notebook
done

Follow-up Actions

After successful upload, suggest:

For analysis:

notebooklm use <notebook_id>
notebooklm ask "What are the key insights?"
notebooklm ask "Summarize in 3 bullet points"


For content generation:

notebooklm generate audio "Create an engaging podcast"
notebooklm generate video "Make an explanatory video"
notebooklm generate quiz "Test understanding"


For research:

notebooklm source add-research "related topics" --mode deep
notebooklm ask "Compare with other sources"

Limitations
WeChat articles only: Optimized for mp.weixin.qq.com URLs
Text content: Focuses on text, images are preserved as links
Public articles: Requires publicly accessible articles
Rate limits: NotebookLM has rate limits on uploads
Troubleshooting

Problem: Article content is incomplete

Cause: WeChat page uses JavaScript rendering
Solution: web reader tool handles most cases, but some dynamic content may be missed

Problem: Chinese characters display incorrectly

Cause: File encoding issues
Solution: Ensure UTF-8 encoding when saving files

Problem: NotebookLM says "Processing" for too long

Cause: Large articles take time to index
Solution: Wait 1-2 minutes, then check status with notebooklm source list
Best Practices
Use descriptive notebook titles: Extract from article title or topic
Keep articles organized: Use separate notebooks for different topics
Verify uploads: Check notebooklm source list after upload
Clean up temp files: Remove /tmp files after successful upload
Handle rate limits: If uploads fail, wait 5-10 minutes before retry
Quick Reference
Task	Command/Tool
Fetch article	mcp__web_reader__webReader
Create notebook	notebooklm create "Title" --json
Upload file	notebooklm source add file.md --notebook <id> --json
Check sources	notebooklm source list --notebook <id> --json
Chat with article	notebooklm use <id>; notebooklm ask "question"
Generate podcast	notebooklm generate audio "instructions" --notebook <id>
Example Usage

User: "Sync this WeChat article to NotebookLM: https://mp.weixin.qq.com/s/xxxxx"

Agent workflow:

Fetch article using web reader
Save to /tmp/article_title.md
Create notebook "Article Title"
Upload markdown file
Report success with IDs and next steps

Time estimate: 30-60 seconds total

Weekly Installs
8
Repository
zstmfhy/wechat-…tebooklm
GitHub Stars
93
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn