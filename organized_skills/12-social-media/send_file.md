---
rating: ⭐⭐⭐
title: send-file
url: https://skills.sh/ninehills/skills/send-file
---

# send-file

skills/ninehills/skills/send-file
send-file
Installation
$ npx skills add https://github.com/ninehills/skills --skill send-file
SKILL.md
Send File Skill

Send files directly to the current Telegram chat. The ALMA_CHAT_ID environment variable is automatically available in your Bash environment.

Commands
# Send a photo/image
alma send photo /path/to/image.jpg "optional caption"

# Send a document/file
alma send file /path/to/document.pdf "optional caption"

# Send audio/music
alma send audio /path/to/song.mp3 "optional caption"

# Send a video
alma send video /path/to/video.mp4 "optional caption"

# Send a voice message (ogg format)
alma send voice /path/to/voice.ogg

Type Aliases
photo / image → sends as photo (compressed, inline preview)
file / document / doc → sends as document (original quality, download)
audio / music → sends as audio (with player UI)
video → sends as video (inline player)
voice → sends as voice message
Tips
Photos are compressed by Telegram. If quality matters, send as file instead.
Caption is optional — omit it if not needed.
ALMA_CHAT_ID is set automatically. You do NOT need to figure out the chat ID.
If you want to send to a different chat, use --chat <chatId>: alma send photo --chat 12345 /path/to/img.jpg
Always verify the file exists before sending.
⚠️ IMPORTANT

When you generate an image, create a file, or produce any output the user should receive as a file:

Generate/create the file
Use alma send to deliver it
Mention what you sent in your text reply (but do NOT include the raw file path)

Do NOT just paste file paths in your reply and expect them to be auto-sent. YOU must explicitly send files.

Weekly Installs
117
Repository
ninehills/skills
GitHub Stars
267
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass