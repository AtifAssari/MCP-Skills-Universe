---
rating: ⭐⭐⭐
title: beepctl
url: https://skills.sh/blqke/beepctl/beepctl
---

# beepctl

skills/blqke/beepctl/beepctl
beepctl
Installation
$ npx skills add https://github.com/blqke/beepctl --skill beepctl
SKILL.md
beepctl

CLI for Beeper Desktop API — unified messaging from your terminal. Control all your messaging platforms (Telegram, WhatsApp, Slack, iMessage, etc.) through one interface.

📖 Setup & installation: see GitHub repo

Quick Start
beepctl accounts                    # List connected accounts
beepctl chats list                  # List recent chats
beepctl chats list --search "John"  # Find a chat
beepctl search "meeting" --after "1d ago"  # Search messages
beepctl send <chat-id> "Hello!"     # Send a message

Commands
Auth Management
beepctl auth show           # Check auth status and token
beepctl auth set <token>    # Set API token
beepctl auth clear          # Clear saved token

Accounts
beepctl accounts            # List all connected accounts

Browse Chats
beepctl chats list                        # List inbox (non-archived)
beepctl chats list --limit 20             # Limit results
beepctl chats list --search "John"        # Filter by name
beepctl chats list --inbox archive        # Archived chats only
beepctl chats list --inbox low-priority   # Low-priority chats
beepctl chats list --inbox all            # All chats
beepctl chats list --type group           # Filter by type (single/group/any)
beepctl chats list --unread-only          # Unread chats only
beepctl chats list --activity-after "1d ago"  # Recent activity filter
beepctl chats show <chat-id>              # Detailed chat info with participants
beepctl chats create <account> <users...> # Create new chat


Inbox filters: primary (default), archive, low-priority, all

List Messages
beepctl messages <chat-id>              # Recent messages from a chat
beepctl messages <chat-id> --limit 10   # Limit results
beepctl messages work --after "1d ago"  # Use alias + time filter
beepctl messages <chat-id> --before "1h ago"  # Messages before a time

Search Messages
beepctl search "query"                    # Search across all chats
beepctl search "query" --limit 10         # Limit results
beepctl search "meeting" --after "1d ago" # Time filter
beepctl search "hello" --chat work        # Filter by chat/alias
beepctl search "files" --media file       # Filter by media type
beepctl search "dm" --chat-type single    # Filter by chat type
beepctl search "update" --sender others   # Filter by sender (me/others)
beepctl search "msg" --account <id>       # Filter by account
beepctl search "todo" --include-low-priority   # Include low-priority chats
beepctl search "important" --exclude-muted     # Exclude muted chats


Combine filters:

beepctl search "deploy" --chat work --sender others --after "1d ago" --media link
beepctl search "hello" --chat work family  # Multiple chats (space-separated)
beepctl search "test" --chat id1,id2,id3   # Multiple chats (comma-separated)


Time formats: 1h ago, 2d ago, 3w ago, 1mo ago, yesterday, today Media types: any, video, image, link, file

Aliases

Create shortcuts for frequently used chat IDs:

beepctl alias list                    # List all aliases
beepctl alias add work <chat-id>      # Create alias
beepctl alias show work               # Show alias value
beepctl alias remove work             # Remove alias
beepctl send work "Using alias!"      # Use alias in any command

Archive Chats
beepctl archive <chat-id>              # Archive a chat
beepctl archive <chat-id> --unarchive  # Unarchive
beepctl archive work                   # Use alias
beepctl archive <chat-id> --quiet      # No confirmation message

Send Messages

⚠️ NEVER send messages without explicit user approval first! Always show the message content and recipient, then ask for confirmation.

beepctl send <chat-id> "Hello!"                    # Send message
beepctl send myself "Quick note"                   # Send to self
beepctl send <chat-id> "Reply" --reply-to <msg-id> # Reply to message
beepctl send <chat-id> "msg" --quiet               # No confirmation output

Focus (Bring to Foreground)
beepctl focus                           # Bring Beeper to foreground
beepctl focus <chat-id>                 # Open a specific chat
beepctl focus <chat-id> -m <msg-id>     # Jump to specific message
beepctl focus <chat-id> -d "draft"      # Pre-fill draft text
beepctl focus <chat-id> -a /path/file   # Pre-fill draft attachment

Send Media

beepctl send only supports text. To send media, use focus with draft:

beepctl focus <chat-id> -a /path/to/image.png -d "Caption"
# Then press Enter in Beeper to send

Contacts
beepctl contacts search <account> <query>  # Search contacts on an account

Download Attachments
beepctl download <mxc-url>              # Download attachment (mxc:// URLs)
beepctl download <mxc-url> -o /path     # Save to specific path

Reminders
beepctl reminders set <chat> 30m       # Remind in 30 minutes
beepctl reminders set <chat> 1h        # Remind in 1 hour
beepctl reminders set <chat> 2d        # Remind in 2 days
beepctl reminders set <chat> tomorrow  # Remind tomorrow
beepctl reminders clear <chat>         # Clear reminder

React to Messages
beepctl react <chat-id> <message-id> 👍                # React with emoji
beepctl react <chat-id> <message-id> thumbsup          # React with shortcode
beepctl react <chat-id> <message-id> custom_emoji_key   # React with custom emoji key
beepctl react <chat-id> <message-id> 👍 --remove        # Remove your reaction
beepctl react work <message-id> ❤️                      # Use alias


<reaction-key> accepts an emoji, shortcode, or custom emoji key. --remove removes the authenticated user's reaction only — it cannot remove other users' reactions.

Tips
Chat IDs look like: !gZ42vWzDxl8V0sZXWBgO:beeper.local
Use aliases to avoid typing long chat IDs
The special alias myself sends to your own chat
Weekly Installs
13
Repository
blqke/beepctl
GitHub Stars
41
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail