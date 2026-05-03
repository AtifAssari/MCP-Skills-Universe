---
title: pressto-button
url: https://skills.sh/david-evans03/skills/pressto-button
---

# pressto-button

skills/david-evans03/skills/pressto-button
pressto-button
Installation
$ npx skills add https://github.com/david-evans03/skills --skill pressto-button
SKILL.md
Setup

Add PressablesConfig with haptics to your root layout:

import { PressablesConfig } from "pressto";
import * as Haptics from "expo-haptics";

export default function RootLayout() {
  return (
    <PressablesConfig
      globalHandlers={{
        onPressIn: () => Haptics.selectionAsync(),
      }}
    >
      <Stack>
        <Stack.Screen name="(tabs)" options={{ headerShown: false }} />
      </Stack>
    </PressablesConfig>
  );
}

Usage
import { PressableScale, PressableOpacity } from "pressto";

// Scales down on press
<PressableScale onPress={() => {}}>
  <Text>Scale</Text>
</PressableScale>

// Fades when pressed
<PressableOpacity onPress={() => {}}>
  <Text>Opacity</Text>
</PressableOpacity>


Supports standard Pressable props.

Notes

Do not add extra animations beyond what Pressto provides. Custom animations can cause text to appear blurry when pressing. Use only the built-in scale/opacity effects.

Weekly Installs
10
Repository
david-evans03/skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass