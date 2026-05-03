---
rating: ⭐⭐
title: 1k-feature-guides
url: https://skills.sh/onekeyhq/app-monorepo/1k-feature-guides
---

# 1k-feature-guides

skills/onekeyhq/app-monorepo/1k-feature-guides
1k-feature-guides
Installation
$ npx skills add https://github.com/onekeyhq/app-monorepo --skill 1k-feature-guides
SKILL.md
Feature Development Guides

Comprehensive guides for extending OneKey app functionality.

Quick Reference
Feature	Guide	Key Files
Add blockchain chain	adding-chains.md	packages/core/src/chains/
Add WebSocket events	adding-socket-events.md	packages/shared/types/socket.ts
Push notifications	notification-system.md	packages/kit-bg/src/services/ServiceNotification/
Pages & routes	page-and-route.md	packages/kit/src/routes/
Adding New Chains

See: references/rules/adding-chains.md

Key steps:

Implement chain core logic in packages/core/src/chains/mychain/
Add chain configuration in packages/shared/src/config/chains/
Update UI components for chain-specific features
Add comprehensive tests

Reference implementations:

EVM chains: packages/core/src/chains/evm/
Bitcoin: packages/core/src/chains/btc/
Solana: packages/core/src/chains/sol/
Adding WebSocket Events

See: references/rules/adding-socket-events.md

Key steps:

Define event name in EAppSocketEventNames enum
Define payload type interface with msgId: string
Add event handler in PushProviderWebSocket.initWebSocket()
Always acknowledge messages via ackNotificationMessage
this.socket.on(EAppSocketEventNames.myEvent, (payload: IMyPayload) => {
  void this.backgroundApi.serviceNotification.ackNotificationMessage({
    msgId: payload.msgId,
    action: ENotificationPushMessageAckAction.arrived,
  });
  void this.backgroundApi.someService.handleEvent(payload);
});

Notification System

See: references/rules/notification-system.md

Notification modes:

Mode	Action
1 (page)	Navigate to specific page
2 (dialog)	Show dialog
3 (openInBrowser)	Open URL in external browser
4 (openInApp)	Open URL in in-app browser
5 (openInDapp)	Open URL in DApp browser

Key files:

Service: packages/kit-bg/src/services/ServiceNotification/ServiceNotification.ts
Utils: packages/shared/src/utils/notificationsUtils.ts
Types: packages/shared/types/notification.ts
Pages & Routes

See: references/rules/page-and-route.md

Page types:

Type	Description
modal	Modal overlay pages
stack	Tab route pages
onboarding	Full screen onboarding pages

Route configuration locations:

Modal routes: packages/kit/src/routes/Modal/router.tsx
Tab routes: packages/kit/src/routes/Tab/router.ts
Onboarding: packages/kit/src/views/Onboardingv2/router/index.tsx

Important:

⚠️ Never delete pages - use redirect pattern for deprecated routes
⚠️ Route paths must be unique across the entire application
⚠️ Always use pop: true with navigation.navigate
Related Skills
/1k-coding-patterns - React and TypeScript best practices
/1k-architecture - Project structure and import rules
/1k-state-management - Jotai atom patterns
Weekly Installs
53
Repository
onekeyhq/app-monorepo
GitHub Stars
2.4K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn