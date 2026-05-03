---
title: google-drive
url: https://skills.sh/odyssey4me/agent-skills/google-drive
---

# google-drive

skills/odyssey4me/agent-skills/google-drive
google-drive
Installation
$ npx skills add https://github.com/odyssey4me/agent-skills --skill google-drive
SKILL.md
Google Drive

Interact with Google Drive for file management, search, and sharing.

Installation

Dependencies: pip install --user google-auth google-auth-oauthlib google-api-python-client keyring pyyaml

Setup Verification

After installation, verify the skill is properly configured:

$SKILL_DIR/scripts/google-drive.py check


This will check:

Python dependencies (google-auth, google-auth-oauthlib, google-api-python-client, keyring, pyyaml)
Authentication configuration
Connectivity to Google Drive API

If anything is missing, the check command will provide setup instructions.

Authentication

Google Drive uses OAuth 2.0 for authentication. For complete setup instructions, see:

GCP Project Setup Guide - Create project, enable Drive API
Google OAuth Setup Guide - Configure credentials
Quick Start

Create ~/.config/agent-skills/google.yaml:

oauth_client:
  client_id: your-client-id.apps.googleusercontent.com
  client_secret: your-client-secret


Run $SKILL_DIR/scripts/google-drive.py check to trigger OAuth flow and verify setup.

On scope or authentication errors, see the OAuth troubleshooting guide.

Script Usage

See permissions.md for read/write classification of each command.

# Setup and auth
$SKILL_DIR/scripts/google-drive.py check
$SKILL_DIR/scripts/google-drive.py auth setup --client-id ID --client-secret SECRET
$SKILL_DIR/scripts/google-drive.py auth reset
$SKILL_DIR/scripts/google-drive.py auth status

# Files
$SKILL_DIR/scripts/google-drive.py files list [--query QUERY] [--max-results N] [--order-by FIELD]
$SKILL_DIR/scripts/google-drive.py files search [--name NAME] [--mime-type TYPE] [--folder ID]
$SKILL_DIR/scripts/google-drive.py files get FILE_ID
$SKILL_DIR/scripts/google-drive.py files download FILE_ID --output PATH
$SKILL_DIR/scripts/google-drive.py files upload PATH [--parent ID] [--name NAME] [--mime-type TYPE] [--convert-to MIME_TYPE]
$SKILL_DIR/scripts/google-drive.py files move FILE_ID --parent FOLDER_ID
$SKILL_DIR/scripts/google-drive.py files delete FILE_ID
$SKILL_DIR/scripts/google-drive.py files rename FILE_ID --name NAME
$SKILL_DIR/scripts/google-drive.py files copy FILE_ID [--name NAME] [--parent ID]

# Folders
$SKILL_DIR/scripts/google-drive.py folders create NAME [--parent ID]
$SKILL_DIR/scripts/google-drive.py folders list FOLDER_ID [--max-results N]

# Sharing and permissions
$SKILL_DIR/scripts/google-drive.py share FILE_ID --email EMAIL [--role ROLE] [--no-notify]
$SKILL_DIR/scripts/google-drive.py permissions list FILE_ID
$SKILL_DIR/scripts/google-drive.py permissions delete FILE_ID PERMISSION_ID

# Comments
$SKILL_DIR/scripts/google-drive.py comments list FILE_ID [--max-results N] [--include-deleted]


See command-reference.md for full argument details and examples.

Examples
Verify Setup
$SKILL_DIR/scripts/google-drive.py check

Find recent PDF files
$SKILL_DIR/scripts/google-drive.py files list --query "mimeType='application/pdf'" --max-results 5

Search for documents by name
$SKILL_DIR/scripts/google-drive.py files search --name "project proposal"

Download a file
# First, find the file ID
$SKILL_DIR/scripts/google-drive.py files search --name "report.pdf"

# Then download it
$SKILL_DIR/scripts/google-drive.py files download FILE_ID -o ./report.pdf

Upload and share a file
# Upload the file
$SKILL_DIR/scripts/google-drive.py files upload ./presentation.pdf --name "Q4 Presentation"

# Share with a colleague
$SKILL_DIR/scripts/google-drive.py share FILE_ID --email colleague@example.com --role writer

Upload with format conversion

Use --convert-to to convert uploaded files to native Google formats:

# Upload HTML and convert to Google Docs
$SKILL_DIR/scripts/google-drive.py files upload ./report.html \
  --convert-to "application/vnd.google-apps.document"

# Upload CSV and convert to Google Sheets
$SKILL_DIR/scripts/google-drive.py files upload ./data.csv \
  --convert-to "application/vnd.google-apps.spreadsheet"

Permanently delete a file
$SKILL_DIR/scripts/google-drive.py files delete FILE_ID

Rename a file
$SKILL_DIR/scripts/google-drive.py files rename FILE_ID --name "New Name"

Copy a file
# Copy with default name ("Copy of <original>")
$SKILL_DIR/scripts/google-drive.py files copy FILE_ID

# Copy with custom name into a specific folder
$SKILL_DIR/scripts/google-drive.py files copy FILE_ID --name "Backup" --parent FOLDER_ID

Organize files into folders
# Create a folder
$SKILL_DIR/scripts/google-drive.py folders create "Project Documents"

# Upload files to the folder
$SKILL_DIR/scripts/google-drive.py files upload ./doc1.pdf --parent FOLDER_ID
$SKILL_DIR/scripts/google-drive.py files upload ./doc2.pdf --parent FOLDER_ID

# List folder contents
$SKILL_DIR/scripts/google-drive.py folders list FOLDER_ID

List comments on a file
$SKILL_DIR/scripts/google-drive.py comments list FILE_ID

Drive Search Query Syntax

See drive-queries.md for operators, searchable fields, and query examples.

Common MIME Types

See api-reference.md for MIME types used with --mime-type and search queries.

Unsupported Operations

See api-reference.md for operations not yet implemented and their alternatives.

Error Handling

Authentication and scope errors are not retryable. If a command fails with an authentication error, insufficient scope error, or permission denied error (exit code 1), stop and inform the user. Do not retry or attempt to fix the issue autonomously — these errors require user interaction (browser-based OAuth consent). Point the user to the OAuth troubleshooting guide.

Retryable errors: Rate limiting (HTTP 429) and temporary server errors (HTTP 5xx) may succeed on retry after a brief wait. All other errors should be reported to the user.

Model Guidance

This skill makes API calls requiring structured input/output. A standard-capability model is recommended.

Troubleshooting
Cannot download Google Docs

Google Docs, Sheets, and Slides are not binary files - they cannot be downloaded directly. Use the Google Drive web interface to export them to a downloadable format (PDF, DOCX, etc.).

Weekly Installs
148
Repository
odyssey4me/agent-skills
GitHub Stars
3
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail