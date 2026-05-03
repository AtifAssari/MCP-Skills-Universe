---
title: whatsapp-web-js
url: https://skills.sh/goncy/skills/whatsapp-web-js
---

# whatsapp-web-js

skills/goncy/skills/whatsapp-web-js
whatsapp-web-js
Installation
$ npx skills add https://github.com/goncy/skills --skill whatsapp-web-js
SKILL.md
WhatsApp Web.js

Provides expert guidance for whatsapp-web.js, a library that automates WhatsApp Web by controlling a Chromium browser instance via Puppeteer.

Quick Start

Initialize client with authentication strategy and listen for events:

const { Client, LocalAuth } = require('whatsapp-web.js');

const client = new Client({
    authStrategy: new LocalAuth(),
    puppeteer: { headless: true }
});

client.on('qr', (qr) => console.log('Scan QR:', qr));
client.on('ready', () => console.log('Client ready'));
client.on('message', async (msg) => {
    if (msg.body === 'ping') await msg.reply('pong');
});

client.initialize();  // Non-blocking - listen for 'ready' event


Requirements: Node.js >= 18.0.0, puppeteer (required), ffmpeg (optional for stickers).

ID Format Conventions

Always use correct ID format for chat operations:

Private chats: <country_code><phone>@c.us (e.g., 5511999999999@c.us)
Groups: <id>@g.us (e.g., 120363XXX@g.us)
Channels: <id>@newsletter
Status broadcasts: status@broadcast

Phone numbers exclude + and leading zeros. Example: US +1 (234) 567-8901 becomes 12345678901@c.us.

Authentication Strategies

Choose based on deployment model:

// No persistence - QR scan every restart
new NoAuth()

// Local filesystem - recommended for single-instance bots
new LocalAuth({ clientId: 'bot1' })

// Remote store - for cloud/multi-instance deployments
new RemoteAuth({ store: myStore, clientId: 'bot1', backupSyncIntervalMs: 60000 })

Pairing Code Authentication

Skip QR scanning by using phone number pairing:

const client = new Client({
    authStrategy: new LocalAuth(),
    pairWithPhoneNumber: {
        phoneNumber: '5511999999999',  // country code + number, no symbols
        showNotification: true,
        intervalMs: 180000
    }
});
client.on('code', (code) => console.log('Pairing code:', code));

Essential Patterns
Sending Messages
// Text message
await client.sendMessage('5511999999999@c.us', 'Hello!');

// Reply to received message
await msg.reply('Got it!');

// With mentions
await client.sendMessage(chatId, 'Hi @5511999999999', {
    mentions: ['5511999999999@c.us']
});

// Quote specific message
await client.sendMessage(chatId, 'Replying to this', {
    quotedMessageId: msg.id._serialized
});

Media Handling
const { MessageMedia } = require('whatsapp-web.js');

// From file
const media = MessageMedia.fromFilePath('/path/to/image.png');
await client.sendMessage(chatId, media, { caption: 'Check this out' });

// From URL
const media = await MessageMedia.fromUrl('https://example.com/image.png');
await client.sendMessage(chatId, media);

// Download received media
if (msg.hasMedia) {
    const media = await msg.downloadMedia();
    // Access: media.mimetype, media.data (base64), media.filename
}

Media Send Variants

Control how media is sent with specific options:

// As sticker (requires ffmpeg)
await client.sendMessage(chatId, media, { sendMediaAsSticker: true });

// As voice note
await client.sendMessage(chatId, audio, { sendAudioAsVoice: true });

// As HD quality
await client.sendMessage(chatId, media, { sendMediaAsHd: true });

// As view-once
await client.sendMessage(chatId, media, { isViewOnce: true });

// As document
await client.sendMessage(chatId, media, { sendMediaAsDocument: true });

Polls, Reactions, Location
const { Poll, Location } = require('whatsapp-web.js');

// Poll (single choice)
await client.sendMessage(chatId, new Poll('Question?', ['A', 'B']));

// Poll (multiple choice)
await client.sendMessage(chatId, new Poll('Pick', ['A', 'B', 'C'], 
    { allowMultipleAnswers: true }));

// React to message
await msg.react('👍');   // add reaction
await msg.react('');      // remove reaction

// Send location
await client.sendMessage(chatId, 
    new Location(37.422, -122.084, { name: 'Googleplex' }));

Message Operations
// Edit sent message
const sent = await client.sendMessage(chatId, 'Original');
await sent.edit('Edited text');

// Delete message
await sent.delete(true);  // true = delete for everyone

// Pin message
await msg.pin(86400);     // Pin for 24h (86400|604800|2592000 seconds)
await msg.unpin();

Critical Gotchas
client.initialize() is non-blocking — Always listen for ready event before using client
message event fires only for incoming — Use message_create to capture outgoing messages too
Message IDs require ._serialized — Use msg.id._serialized for string representation
Group admin operations — Bot must be admin to setSubject, removeParticipants, etc.
Rate limiting — Add delays between bulk sends to avoid temporary blocks
fetchMessages() loads from cache — Call chat.syncHistory() for full history sync
Sticker conversion requires ffmpeg — Install on system PATH for sticker support
Memory considerations — Runs real Chromium instance; plan for multi-client setups
Status messages — Send to status@broadcast as chatId
Key Events

Essential events for bot logic:

Event	Use Case
ready	Client ready to use
message	Incoming message only
message_create	All messages (including own)
message_ack	Track delivery status (0=pending, 1=server, 2=device, 3=read, 4=played)
qr	QR code for authentication
authenticated	Auth successful
disconnected	Handle reconnection logic
References

Consult these detailed references when implementing specific features:

detailed-guide.md — Read when implementing any WhatsApp Web.js feature. Contains comprehensive API reference organized by category: messaging, media, chats, groups, channels, contacts, events. Includes all method signatures, options, return types, and code examples. Start here for unfamiliar operations or when debugging unexpected behavior.
Weekly Installs
76
Repository
goncy/skills
GitHub Stars
16
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn