---
rating: ⭐⭐
title: hig-technologies
url: https://skills.sh/raintree-technology/apple-hig-skills/hig-technologies
---

# hig-technologies

skills/raintree-technology/apple-hig-skills/hig-technologies
hig-technologies
Installation
$ npx skills add https://github.com/raintree-technology/apple-hig-skills --skill hig-technologies
SKILL.md
Apple HIG: Technologies

Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered.

Key Principles

Apple technologies extend app capabilities through system integration. Each technology has established user-facing patterns; deviating creates confusion and erodes trust.

Privacy and user control are paramount. Especially for health, payment, and identity technologies. Request only needed data, explain why, respect choices.

Siri: natural, predictable, recoverable. Clear conversational intent phrases that complete quickly and confirm results. Support App Shortcuts for proactive suggestions. Handle errors with clear fallbacks.

Payments: transparent and frictionless. Standard Apple Pay button styles. Never ask for card details when Apple Pay is available. Clearly describe what the user is buying, the price, and whether it's one-time or subscription.

Health data is deeply personal. Explain the health benefit before requesting access. CareKit tasks should be encouraging. ResearchKit consent flows must be thorough, readable, and respect autonomy.

HomeKit: simple and reliable. Immediate response when controlling devices. Clear device state. Graceful handling of connectivity issues.

AR: genuine value, not gimmicks. Use AR when spatial context improves understanding. Guide setup (surface, lighting, space). Provide clear exit back to standard interaction.

ML and generative AI: enhance without surprising. Smart suggestions, image recognition, text prediction. Clearly attribute AI-generated content. Controls to edit, regenerate, or dismiss. Let users correct mistakes.

Sign in with Apple as top option. Standard button styles. Respect email hiding preference. ID Verifier: guided flows, don't store sensitive data beyond what verification requires.

iCloud: invisible and reliable sync. Data appears on all devices without manual intervention. Handle conflicts gracefully. Never lose data.

SharePlay: real-time participation. Support multiple participants, show presence, handle latency. AirPlay: appropriate Now Playing metadata.

CarPlay: driver safety first. Minimize interaction complexity, large touch targets, no distracting content. Only permitted app types: audio, messaging, EV charging, navigation, parking, quick food ordering.

Accessibility is a baseline requirement. Every element has a meaningful VoiceOver label, trait, and action. Support Dynamic Type, Switch Control, and other assistive technologies. Test entirely with VoiceOver enabled.

Reference Index
Reference	Topic	Key content
siri.md	Siri	Intents, shortcuts, voice interaction, App Shortcuts
apple-pay.md	Apple Pay	Payment buttons, checkout flow, security
tap-to-pay-on-iphone.md	Tap to Pay	Merchant flows, contactless payment
in-app-purchase.md	In-app purchase	Subscriptions, one-time purchases, transparency
healthkit.md	HealthKit	Health data access, privacy, permissions
carekit.md	CareKit	Care plans, tasks, health management
researchkit.md	ResearchKit	Studies, informed consent, data collection
homekit.md	HomeKit	Smart home control, device state, scenes
augmented-reality.md	ARKit	Spatial context, surface detection, setup
machine-learning.md	Core ML	Predictions, smart features, confidence handling
generative-ai.md	Generative AI	Attribution, editing, responsible AI, uncertainty
icloud.md	iCloud	CloudKit, cross-device sync, conflict resolution
sign-in-with-apple.md	Sign in with Apple	Authentication, privacy, button styles
id-verifier.md	ID Verifier	Identity verification, document scanning
shareplay.md	SharePlay	Shared experiences, participant presence
airplay.md	AirPlay	Media streaming, Now Playing, wireless display
carplay.md	CarPlay	Driver safety, permitted app types, large targets
game-center.md	Game Center	Achievements, leaderboards, multiplayer
voiceover.md	VoiceOver	Screen reader, labels, traits, accessibility
wallet.md	Wallet	Passes, tickets, loyalty cards
nfc.md	NFC	Tag reading, quick interactions, App Clips
maps.md	Maps	Location display, annotations, directions
mac-catalyst.md	Mac Catalyst	iPad to Mac, menu bar, keyboard, pointer
live-photos.md	Live Photos	Motion capture, playback, editing
imessage-apps-and-stickers.md	iMessage apps	Messages extension, stickers, compact UI
shazamkit.md	ShazamKit	Audio recognition, music identification
always-on.md	Always-on display	Dimmed state, power efficiency, reduced updates
photo-editing.md	Photo editing	System photo editor, filters, adjustments
Output Format
Implementation checklist -- step-by-step requirements per Apple's guidelines.
Required vs optional features for approval.
Privacy and permission requirements -- data access, usage descriptions.
User-facing flow from permission prompt through task completion.
Testing guidance -- key scenarios including edge cases.
Questions to Ask
Which Apple technology?
Core use case?
Which platforms?
API requirements and entitlements reviewed?
What data or permissions needed?
Related Skills
hig-inputs -- Input methods interacting with technologies (voice for Siri, Pencil for AR, gestures for Maps)
hig-components-system -- Widgets, complications, Live Activities surfacing technology data
hig-components-status -- Progress indicators for technology operations (sync, payment, AR loading)

Built by Raintree Technology · More developer tools

Weekly Installs
154
Repository
raintree-techno…g-skills
GitHub Stars
45
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn