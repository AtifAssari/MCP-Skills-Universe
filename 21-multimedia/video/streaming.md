---
rating: ⭐⭐
title: streaming
url: https://skills.sh/alsk1992/cloddsbot/streaming
---

# streaming

skills/alsk1992/cloddsbot/streaming
streaming
Installation
$ npx skills add https://github.com/alsk1992/cloddsbot --skill streaming
SKILL.md
Streaming - Complete API Reference

Configure response streaming, typing indicators, and real-time message delivery.

Chat Commands
View Settings
/streaming                                  Show current settings
/streaming status                           Streaming status

Configure Streaming
/streaming enable                           Enable streaming
/streaming disable                          Disable streaming
/streaming chunk-size 50                    Set chunk size (chars)
/streaming delay 100                        Set delay between chunks (ms)

Typing Indicators
/streaming typing on                        Enable typing indicators
/streaming typing off                       Disable typing indicators
/streaming typing duration 3000             Typing duration (ms)

Platform Settings
/streaming platforms                        Show platform limits
/streaming platform telegram chunk 100      Set per-platform

TypeScript API Reference
Create Streaming Config
import { createStreamingConfig } from 'clodds/streaming';

const streaming = createStreamingConfig({
  // Enable streaming
  enabled: true,

  // Chunk settings
  minChunkSize: 20,    // Min chars per chunk
  maxChunkSize: 200,   // Max chars per chunk
  chunkDelayMs: 50,    // Delay between chunks

  // Typing indicators
  showTyping: true,
  typingDurationMs: 3000,

  // Platform-specific limits
  platformLimits: {
    telegram: { maxMessageLength: 4096, maxChunkSize: 100 },
    discord: { maxMessageLength: 2000, maxChunkSize: 150 },
    slack: { maxMessageLength: 40000, maxChunkSize: 200 },
  },
});

Enable/Disable
// Enable streaming
streaming.enable();

// Disable streaming
streaming.disable();

// Check status
const enabled = streaming.isEnabled();

Configure Chunks
// Set chunk size
streaming.setChunkSize(100);

// Set delay
streaming.setChunkDelay(75);

// Get current settings
const settings = streaming.getSettings();
console.log(`Chunk size: ${settings.chunkSize}`);
console.log(`Delay: ${settings.chunkDelayMs}ms`);

Platform Settings
// Set platform-specific limit
streaming.setPlatformLimit('telegram', {
  maxMessageLength: 4096,
  maxChunkSize: 80,
});

// Get platform limits
const limits = streaming.getPlatformLimits();

Typing Indicators
// Enable typing
streaming.enableTyping();

// Disable typing
streaming.disableTyping();

// Set duration
streaming.setTypingDuration(5000);

Platform Limits
Platform	Max Message	Recommended Chunk
Telegram	4,096 chars	80-100
Discord	2,000 chars	100-150
Slack	40,000 chars	150-200
WhatsApp	65,536 chars	100-150
WebChat	Unlimited	150-200
Best Practices
Smaller chunks for mobile — Better UX on slow connections
Adjust delay for readability — 50-100ms feels natural
Disable for short responses — Don't stream "OK"
Monitor performance — Streaming adds overhead
Weekly Installs
9
Repository
alsk1992/cloddsbot
GitHub Stars
194
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass