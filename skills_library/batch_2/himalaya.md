---
title: himalaya
url: https://skills.sh/steipete/clawdis/himalaya
---

# himalaya

skills/steipete/clawdis/himalaya
himalaya
Installation
$ npx skills add https://github.com/steipete/clawdis --skill himalaya
SKILL.md
Himalaya Email CLI

Himalaya is a CLI email client that lets you manage emails from the terminal using IMAP, SMTP, Notmuch, or Sendmail backends.

References
references/configuration.md (config file setup + IMAP/SMTP authentication)
references/message-composition.md (MML syntax for composing emails)
Prerequisites
Himalaya CLI installed (himalaya --version to verify)
A configuration file at ~/.config/himalaya/config.toml
IMAP/SMTP credentials configured (password stored securely)
Configuration Setup

Run the interactive wizard to set up an account:

himalaya account configure


Or create ~/.config/himalaya/config.toml manually:

[accounts.personal]
email = "you@example.com"
display-name = "Your Name"
default = true

backend.type = "imap"
backend.host = "imap.example.com"
backend.port = 993
backend.encryption.type = "tls"
backend.login = "you@example.com"
backend.auth.type = "password"
backend.auth.cmd = "pass show email/imap"  # or use keyring

message.send.backend.type = "smtp"
message.send.backend.host = "smtp.example.com"
message.send.backend.port = 587
message.send.backend.encryption.type = "start-tls"
message.send.backend.login = "you@example.com"
message.send.backend.auth.type = "password"
message.send.backend.auth.cmd = "pass show email/smtp"

Common Operations
List Folders
himalaya folder list

List Emails

List emails in INBOX (default):

himalaya envelope list


List emails in a specific folder:

himalaya envelope list --folder "Sent"


List with pagination:

himalaya envelope list --page 1 --page-size 20

Search Emails
himalaya envelope list from john@example.com subject meeting

Read an Email

Read email by ID (shows plain text):

himalaya message read 42


Export raw MIME:

himalaya message export 42 --full

Reply to an Email

Interactive reply (opens $EDITOR):

himalaya message reply 42


Reply-all:

himalaya message reply 42 --all

Forward an Email
himalaya message forward 42

Write a New Email

Interactive compose (opens $EDITOR):

himalaya message write


Send directly using template:

cat << 'EOF' | himalaya template send
From: you@example.com
To: recipient@example.com
Subject: Test Message

Hello from Himalaya!
EOF


Or with headers flag:

himalaya message write -H "To:recipient@example.com" -H "Subject:Test" "Message body here"

Move/Copy Emails

Move to folder:

himalaya message move 42 "Archive"


Copy to folder:

himalaya message copy 42 "Important"

Delete an Email
himalaya message delete 42

Manage Flags

Add flag:

himalaya flag add 42 --flag seen


Remove flag:

himalaya flag remove 42 --flag seen

Multiple Accounts

List accounts:

himalaya account list


Use a specific account:

himalaya --account work envelope list

Attachments

Save attachments from a message:

himalaya attachment download 42


Save to specific directory:

himalaya attachment download 42 --dir ~/Downloads

Output Formats

Most commands support --output for structured output:

himalaya envelope list --output json
himalaya envelope list --output plain

Debugging

Enable debug logging:

RUST_LOG=debug himalaya envelope list


Full trace with backtrace:

RUST_LOG=trace RUST_BACKTRACE=1 himalaya envelope list

Tips
Use himalaya --help or himalaya <command> --help for detailed usage.
Message IDs are relative to the current folder; re-list after folder changes.
For composing rich emails with attachments, use MML syntax (see references/message-composition.md).
Store passwords securely using pass, system keyring, or a command that outputs the password.
Weekly Installs
1.5K
Repository
steipete/clawdis
GitHub Stars
367.2K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn