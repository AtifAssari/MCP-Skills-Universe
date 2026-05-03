---
title: hotkey
url: https://skills.sh/lobehub/lobehub/hotkey
---

# hotkey

skills/lobehub/lobehub/hotkey
hotkey
Installation
$ npx skills add https://github.com/lobehub/lobehub --skill hotkey
Summary

Structured guide for implementing keyboard shortcuts in a chat application.

Covers five-step implementation process: defining hotkey constants, registering default key combinations, adding i18n translations, creating and registering hooks, and optionally adding tooltips
Supports scope-based hotkey management (global or chat-specific) with conflict detection and platform-agnostic key modifiers
Includes best practices for grouping, conflict checking, and clear user descriptions, plus troubleshooting steps for common issues like scope mismatches and registration problems
SKILL.md
Adding Keyboard Shortcuts Guide
Steps to Add a New Hotkey
1. Update Hotkey Constant

In src/types/hotkey.ts:

export const HotkeyEnum = {
  // existing...
  ClearChat: 'clearChat', // Add new
} as const;

2. Register Default Hotkey

In src/const/hotkeys.ts:

import { KeyMapEnum as Key, combineKeys } from '@lobehub/ui';

export const HOTKEYS_REGISTRATION: HotkeyRegistration = [
  {
    group: HotkeyGroupEnum.Conversation,
    id: HotkeyEnum.ClearChat,
    keys: combineKeys([Key.Mod, Key.Shift, Key.Backspace]),
    scopes: [HotkeyScopeEnum.Chat],
  },
];

3. Add i18n Translation

In src/locales/default/hotkey.ts:

const hotkey: HotkeyI18nTranslations = {
  clearChat: {
    desc: '清空当前会话的所有消息记录',
    title: '清空聊天记录',
  },
};

4. Create and Register Hook

In src/hooks/useHotkeys/chatScope.ts:

export const useClearChatHotkey = () => {
  const clearMessages = useChatStore((s) => s.clearMessages);
  return useHotkeyById(HotkeyEnum.ClearChat, clearMessages);
};

export const useRegisterChatHotkeys = () => {
  useClearChatHotkey();
  // ...other hotkeys
};

5. Add Tooltip (Optional)
const clearChatHotkey = useUserStore(settingsSelectors.getHotkeyById(HotkeyEnum.ClearChat));

<Tooltip hotkey={clearChatHotkey} title={t('clearChat.title', { ns: 'hotkey' })}>
  <Button icon={<DeleteOutlined />} onClick={clearMessages} />
</Tooltip>;

Best Practices
Scope: Choose global or chat scope based on functionality
Grouping: Place in appropriate group (System/Layout/Conversation)
Conflict check: Ensure no conflict with system/browser shortcuts
Platform: Use Key.Mod instead of hardcoded Ctrl or Cmd
Clear description: Provide title and description for users
Troubleshooting
Not working: Check scope and RegisterHotkeys hook
Not in settings: Verify HOTKEYS_REGISTRATION config
Conflict: HotkeyInput component shows warnings
Page-specific: Ensure correct scope activation
Weekly Installs
675
Repository
lobehub/lobehub
GitHub Stars
75.9K
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass