---
title: voice
url: https://skills.sh/alsk1992/cloddsbot/voice
---

# voice

skills/alsk1992/cloddsbot/voice
voice
Installation
$ npx skills add https://github.com/alsk1992/cloddsbot --skill voice
SKILL.md
Voice - Complete API Reference

Voice-controlled interface with wake word detection, speech-to-text, and text-to-speech.

Chat Commands
Voice Control
/voice start                                Start voice listening
/voice stop                                 Stop voice listening
/voice status                               Check voice status
/voice wake "hey clodds"                    Set wake word

Settings
/voice language en-US                       Set language
/voice sensitivity high                     Wake word sensitivity
/voice timeout 30                           Silence timeout (seconds)
/voice continuous on                        Enable continuous mode

TypeScript API Reference
Create Voice Assistant
import { createVoiceAssistant } from 'clodds/voice';

const voice = createVoiceAssistant({
  // Wake word
  wakeWord: 'hey clodds',
  wakeWordSensitivity: 0.5,  // 0-1

  // Speech-to-text
  stt: {
    provider: 'whisper',  // 'whisper' | 'vosk' | 'google'
    model: 'base',        // 'tiny' | 'base' | 'small' | 'medium' | 'large'
    language: 'en',
  },

  // Text-to-speech
  tts: {
    provider: 'elevenlabs',  // 'elevenlabs' | 'say' | 'espeak'
    voice: 'rachel',
    speed: 1.0,
  },

  // Timeouts
  silenceTimeoutMs: 3000,
  maxRecordingMs: 30000,
});

Start/Stop Listening
// Start listening for wake word
await voice.start();

// Check if listening
const isListening = voice.isListening();

// Stop listening
await voice.stop();

Event Handlers
// Wake word detected
voice.on('wake', () => {
  console.log('Wake word detected!');
});

// Speech recognized
voice.on('speech', (text: string) => {
  console.log(`User said: ${text}`);
});

// Transcription complete
voice.on('transcript', (result) => {
  console.log(`Final: ${result.text}`);
  console.log(`Confidence: ${result.confidence}`);
  console.log(`Duration: ${result.durationMs}ms`);
});

// Error handling
voice.on('error', (error) => {
  console.error('Voice error:', error);
});

// Silence detected
voice.on('silence', () => {
  console.log('User stopped speaking');
});

Speak (TTS)
// Speak text
await voice.speak('Your order has been placed');

// Speak with options
await voice.speak('Market is up 5%', {
  voice: 'josh',
  speed: 1.2,
  pitch: 1.0,
});

// Cancel speaking
voice.cancelSpeech();

Manual Transcription
// Transcribe audio buffer
const result = await voice.transcribe(audioBuffer, {
  language: 'en',
  prompt: 'Trading commands',  // Context hint
});

console.log(`Text: ${result.text}`);
console.log(`Language: ${result.language}`);

Voice Activity Detection
// Check if user is speaking
const vad = voice.getVAD();

vad.on('speechStart', () => {
  console.log('User started speaking');
});

vad.on('speechEnd', (audio) => {
  console.log('User stopped speaking');
  // audio contains the recorded speech
});

Wake Word Configuration
Setting	Values	Description
wakeWord	Any phrase	Trigger phrase
sensitivity	0.0 - 1.0	Detection threshold

Built-in wake words:

"hey clodds"
"okay clodds"
"clodds"
STT Providers
Provider	Quality	Speed	Offline
Whisper	Excellent	Medium	Yes
Vosk	Good	Fast	Yes
Google	Excellent	Fast	No
TTS Providers
Provider	Quality	Voices	API Key
ElevenLabs	Premium	30+	Required
say (macOS)	Good	System	None
espeak	Basic	Many	None
Voice Commands Examples

Once voice is active, speak naturally:

"Hey Clodds, what's my portfolio value?"
"Hey Clodds, buy 100 dollars of Trump YES"
"Hey Clodds, what are the top arbitrage opportunities?"
"Hey Clodds, set a price alert for Bitcoin at 100k"

Best Practices
Quiet environment — Background noise affects accuracy
Clear speech — Speak clearly for best recognition
Short commands — Keep voice commands concise
Confirmation — Enable confirmations for trades
Fallback — Text input always available
Weekly Installs
19
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