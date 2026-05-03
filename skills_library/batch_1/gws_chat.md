---
title: gws-chat
url: https://skills.sh/googleworkspace/cli/gws-chat
---

# gws-chat

skills/googleworkspace/cli/gws-chat
gws-chat
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-chat
Summary

Manage Google Chat spaces, messages, custom emojis, and media through API commands.

Access 10+ API resources including spaces, messages, members, custom emojis, and media with create, read, update, delete, and search operations
Create and manage spaces with initial members, find or list direct messages, and handle space imports and deletion
Upload and download media attachments, and manage custom emojis (Google Workspace only, requires admin enablement)
Requires gws binary and authentication setup via shared gws-shared/SKILL.md documentation
SKILL.md
chat (v1)

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

gws chat <resource> <method> [flags]

Helper Commands
Command	Description
+send	Send a message to a space
API Resources
customEmojis
create — Creates a custom emoji. Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see Learn about custom emojis in Google Chat and Manage custom emoji permissions.
delete — Deletes a custom emoji. By default, users can only delete custom emoji they created. Emoji managers assigned by the administrator can delete any custom emoji in the organization. See Learn about custom emojis in Google Chat. Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization.
get — Returns details about a custom emoji. Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see Learn about custom emojis in Google Chat and Manage custom emoji permissions.
list — Lists custom emojis visible to the authenticated user. Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see Learn about custom emojis in Google Chat and Manage custom emoji permissions.
media
download — Downloads media. Download is supported on the URI /v1/media/{+name}?alt=media.
upload — Uploads an attachment. For an example, see Upload media as a file attachment.
spaces
completeImport — Completes the import process for the specified space and makes it visible to users.
create — Creates a space. Can be used to create a named space, or a group chat in Import mode. For an example, see Create a space.
delete — Deletes a named space. Always performs a cascading delete, which means that the space's child resources—like messages posted in the space and memberships in the space—are also deleted. For an example, see Delete a space.
findDirectMessage — Returns the existing direct message with the specified user. If no direct message space is found, returns a 404 NOT_FOUND error. For an example, see Find a direct message. With app authentication, returns the direct message space between the specified user and the calling Chat app.
get — Returns details about a space. For an example, see Get details about a space.
list — Lists spaces the caller is a member of. Group chats and DMs aren't listed until the first message is sent. For an example, see List spaces.
patch — Updates a space. For an example, see Update a space. If you're updating the displayName field and receive the error message ALREADY_EXISTS, try a different display name.. An existing space within the Google Workspace organization might already use this display name.
search — Returns a list of spaces in a Google Workspace organization based on an administrator's search. In the request, set use_admin_access to true. For an example, see Search for and manage spaces.
setup — Creates a space and adds specified users to it. The calling user is automatically added to the space, and shouldn't be specified as a membership in the request. For an example, see Set up a space with initial members. To specify the human members to add, add memberships with the appropriate membership.member.name. To add a human user, use users/{user}, where {user} can be the email address for the user.
members — Operations on the 'members' resource
messages — Operations on the 'messages' resource
spaceEvents — Operations on the 'spaceEvents' resource
users
sections — Operations on the 'sections' resource
spaces — Operations on the 'spaces' resource
Discovering Commands

Before calling any API method, inspect it:

# Browse resources and methods
gws chat --help

# Inspect a method's required params, types, and defaults
gws schema chat.<resource>.<method>


Use gws schema output to build your --params and --json flags.

Weekly Installs
12.3K
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass