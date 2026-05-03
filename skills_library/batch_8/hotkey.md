---
title: hotkey
url: https://skills.sh/lobehub/lobe-chat/hotkey
---

# hotkey

skills/lobehub/lobe-chat/hotkey
hotkey
Originally fromlobehub/lobehub
Installation
$ npx skills add https://github.com/lobehub/lobe-chat --skill hotkey
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
443
Repository
lobehub/lobe-chat
GitHub Stars
75.9K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass