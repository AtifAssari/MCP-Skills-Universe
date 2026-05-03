---
title: apple-mail
url: https://skills.sh/rbouschery/marketplace/apple-mail
---

# apple-mail

skills/rbouschery/marketplace/apple-mail
apple-mail
Installation
$ npx skills add https://github.com/rbouschery/marketplace --skill apple-mail
SKILL.md
Apple Mail Skill

This skill provides commands to interact with Apple Mail on macOS via AppleScript.

Available Scripts

All scripts are in the ../../scripts/ directory (relative to this file). Execute them via bash from the plugin root.

Account & Mailbox Management
Script	Purpose	Arguments
list-accounts.sh	List all email accounts	none
list-mailboxes.sh	List mailboxes/folders	[account] (optional)
get-unread-count.sh	Get unread email count	[account] [mailbox] (optional)
Reading Emails
Script	Purpose	Arguments
get-emails.sh	Get recent emails	[account] [mailbox] [limit] [include_content] [unread_only]
get-email-by-id.sh	Get specific email by ID	<id> [account] [mailbox] [include_content]
search-emails.sh	Search emails	<query> [account] [mailbox] [limit]
Sending & Composing
Script	Purpose	Arguments
send-email.sh	Send an email	<to> <subject> <body> [cc] [bcc] [from]
create-draft.sh	Create a draft email	<subject> <body> [to] [cc] [bcc] [from]
create-reply-draft.sh	Create reply to email	<message_id> <body> [reply_all] [account] [mailbox]
send-draft.sh	Send front-most draft	none
Email Management
Script	Purpose	Arguments
archive-email.sh	Archive an email	<message_id> [account] [mailbox] [archive_mailbox]
delete-email.sh	Delete an email	<message_id> [account] [mailbox]
mark-read.sh	Mark email as read	<message_id> [account] [mailbox]
mark-unread.sh	Mark email as unread	<message_id> [account] [mailbox]
Output Format

Scripts use delimiters for structured output:

<<>> separates fields within a record
||| separates multiple records
ERROR: prefix indicates an error message
Email Record Format
id<<>>subject<<>>sender<<>>to<<>>cc<<>>bcc<<>>dateSent<<>>isRead<<>>content|||

Usage Examples
List accounts
./scripts/list-accounts.sh

Get recent emails from INBOX
./scripts/get-emails.sh "" "INBOX" 10 false false

Get recent unread emails with content
./scripts/get-emails.sh "" "INBOX" 10 true true

Get specific email by ID
./scripts/get-email-by-id.sh 12345 "iCloud" "INBOX" true

Search emails
./scripts/search-emails.sh "meeting notes" "" "" 20

Send an email
./scripts/send-email.sh "recipient@example.com" "Subject" "Body text"

Send with CC and BCC
./scripts/send-email.sh "to@example.com" "Subject" "Body" "cc@example.com" "bcc@example.com"

Create a draft
./scripts/create-draft.sh "Draft Subject" "Draft body" "recipient@example.com"

Reply to an email
./scripts/create-reply-draft.sh 12345 "Thanks for your message!" false "iCloud" "INBOX"

Send the front-most draft
./scripts/send-draft.sh

Archive an email
./scripts/archive-email.sh 12345 "iCloud" "INBOX"

Mark as read/unread
./scripts/mark-read.sh 12345 "iCloud" "INBOX"
./scripts/mark-unread.sh 12345 "iCloud" "INBOX"

Parsing Output

When receiving email records, parse them like this:

Split by ||| to get individual records
Split each record by <<>> to get fields
Fields are: id, subject, sender, to, cc, bcc, dateSent, isRead, content

Example parsing in bash:

IFS='|||' read -ra emails <<< "$output"
for email in "${emails[@]}"; do
    IFS='<<>>' read -ra fields <<< "$email"
    id="${fields[0]}"
    subject="${fields[1]}"
    sender="${fields[2]}"
    # ... etc
done

Notes
Scripts require macOS with Apple Mail configured
Apple Mail must have at least one account set up
First run may trigger macOS permission prompts for automation
Empty optional arguments should be passed as empty strings ""
For scripts that need arrays (multiple recipients), pass comma-separated values
Reference

For advanced AppleScript patterns and customization, see ./reference/applescript-patterns.md.

Weekly Installs
92
Repository
rbouschery/marketplace
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn