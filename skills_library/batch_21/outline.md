---
title: outline
url: https://skills.sh/sanjay3290/ai-skills/outline
---

# outline

skills/sanjay3290/ai-skills/outline
outline
Installation
$ npx skills add https://github.com/sanjay3290/ai-skills --skill outline
SKILL.md
Outline Wiki Skill

Search, read, create, and manage documents in any Outline wiki instance. Works with all AI clients supporting the Agent Skills Standard.

Requirements
Python 3.8+
Dependencies: pip install -r requirements.txt
Setup

Get your API key from your Outline wiki:

Go to Settings > API Tokens
Create a new token with appropriate permissions

Configure the environment:

cp .env.example .env
# Edit .env with your API key


Set the environment variables:

export OUTLINE_API_KEY=your-api-key-here
# Optional: for self-hosted instances
export OUTLINE_API_URL=https://your-wiki.example.com/api

Usage
Search documents
python3 scripts/outline.py search "deployment guide"
python3 scripts/outline.py search "API documentation" --limit 10
python3 scripts/outline.py search "onboarding" --collection-id <id>

Read a document
python3 scripts/outline.py read <document-id>
python3 scripts/outline.py read <document-id> --json

List collections
python3 scripts/outline.py list-collections
python3 scripts/outline.py list-collections --limit 50

List documents in a collection
python3 scripts/outline.py list-documents --collection-id <id>

Get collection details
python3 scripts/outline.py get-collection <collection-id>

Create a document
python3 scripts/outline.py create --title "New Guide" --collection-id <id>
python3 scripts/outline.py create --title "Guide" --collection-id <id> --text "# Content here"
python3 scripts/outline.py create --title "Draft" --collection-id <id> --draft

Update a document
python3 scripts/outline.py update <document-id> --title "Updated Title"
python3 scripts/outline.py update <document-id> --text "New content"
python3 scripts/outline.py update <document-id> --publish

Export document as markdown
python3 scripts/outline.py export <document-id>
python3 scripts/outline.py export <document-id> --output doc.md

Test authentication
python3 scripts/outline.py auth-info

JSON Output

Add --json flag to any command for machine-readable output:

python3 scripts/outline.py search "query" --json
python3 scripts/outline.py read <id> --json

Operations Reference
Command	Description	Required Args
search	Full-text search	query
read	Get document content	document_id
list-collections	List all collections	-
list-documents	List docs (optionally in collection)	-
get-collection	Get collection details	collection_id
create	Create new document	--title, --collection-id
update	Update existing document	document_id
export	Export as markdown	document_id
auth-info	Test API connection	-
Environment Variables
Variable	Required	Default	Description
OUTLINE_API_KEY	Yes	-	Your Outline API token
OUTLINE_API_URL	No	https://app.getoutline.com/api	API URL
OUTLINE_TIMEOUT	No	30	Request timeout (seconds)
OUTLINE_VERIFY_SSL	No	true	Set to false to skip SSL verification (for self-hosted instances with self-signed certs)
Troubleshooting
Error	Solution
API key not configured	Set OUTLINE_API_KEY environment variable
Authentication failed	Verify API key is valid and not expired
Connection timeout	Check OUTLINE_API_URL and network connectivity
SSL certificate error	Set OUTLINE_VERIFY_SSL=false for self-signed certs
Document not found	Verify document ID is correct
Permission denied	Check API token has required permissions
Exit Codes
0: Success
1: Error (auth failed, not found, invalid request)
Workflow
Run auth-info to verify connection
Run list-collections to see available collections
Run search or list-documents to find content
Run read to get full document content
Use create/update to modify wiki content
Weekly Installs
161
Repository
sanjay3290/ai-skills
GitHub Stars
246
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn