---
title: feature-flags
url: https://skills.sh/facebook/react/feature-flags
---

# feature-flags

skills/facebook/react/feature-flags
feature-flags
Installation
$ npx skills add https://github.com/facebook/react --skill feature-flags
Summary

Manage React feature flags across channels, gate tests conditionally, and debug flag-specific test failures.

Four flag files control defaults and channel-specific overrides (canary, www, React Native, test renderer) with __VARIANT__ flags simulating gatekeepers tested in both states
Use @gate flagName pragma to skip tests entirely when a flag is unavailable, or inline gate() to branch assertions when behavior differs
Adding a new flag requires entries in the main file plus all fork files; set to __VARIANT__ in www/native-fb forks if the flag should vary by channel
Common pitfalls include forgetting to test both __VARIANT__ states, using @gate for behavior differences instead of inline gate(), and omitting fork file entries
SKILL.md
React Feature Flags
Flag Files
File	Purpose
packages/shared/ReactFeatureFlags.js	Default flags (canary), __EXPERIMENTAL__ overrides
packages/shared/forks/ReactFeatureFlags.www.js	www channel, __VARIANT__ overrides
packages/shared/forks/ReactFeatureFlags.native-fb.js	React Native, __VARIANT__ overrides
packages/shared/forks/ReactFeatureFlags.test-renderer.js	Test renderer
Gating Tests
@gate pragma (test-level)

Use when the feature is completely unavailable without the flag:

// @gate enableViewTransition
it('supports view transitions', () => {
  // This test only runs when enableViewTransition is true
  // and is SKIPPED (not failed) when false
});

gate() inline (assertion-level)

Use when the feature exists but behavior differs based on flag:

it('renders component', async () => {
  await act(() => root.render(<App />));

  if (gate(flags => flags.enableNewBehavior)) {
    expect(container.textContent).toBe('new output');
  } else {
    expect(container.textContent).toBe('legacy output');
  }
});

Adding a New Flag
Add to ReactFeatureFlags.js with default value
Add to each fork file (*.www.js, *.native-fb.js, etc.)
If it should vary in www/RN, set to __VARIANT__ in the fork file
Gate tests with @gate flagName or inline gate()
Checking Flag States

Use /flags to view states across channels. See the flags skill for full command options.

__VARIANT__ Flags (GKs)

Flags set to __VARIANT__ simulate gatekeepers - tested twice (true and false):

/test www <pattern>              # __VARIANT__ = true
/test www variant false <pattern> # __VARIANT__ = false

Debugging Channel-Specific Failures
Run /flags --diff <channel1> <channel2> to compare values
Check @gate conditions - test may be gated to specific channels
Run /test <channel> <pattern> to isolate the failure
Verify flag exists in all fork files if newly added
Common Mistakes
Forgetting both variants - Always test www AND www variant false for __VARIANT__ flags
Using @gate for behavior differences - Use inline gate() if both paths should run
Missing fork files - New flags must be added to ALL fork files, not just the main one
Wrong gate syntax - It's gate(flags => flags.name), not gate('name')
Weekly Installs
826
Repository
facebook/react
GitHub Stars
244.8K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass