---
title: upgrading-react-native-storybook
url: https://skills.sh/storybookjs/react-native/upgrading-react-native-storybook
---

# upgrading-react-native-storybook

skills/storybookjs/react-native/upgrading-react-native-storybook
upgrading-react-native-storybook
Installation
$ npx skills add https://github.com/storybookjs/react-native --skill upgrading-react-native-storybook
SKILL.md
React Native Storybook Upgrades

Upgrade one supported version step at a time. Do not jump from an older major directly to the latest release in a single pass.

Rules
Detect the project's package manager first and use it consistently.
Detect the currently installed Storybook version from package.json, lockfiles, and config files before editing anything.
Apply exactly one migration step per run. If a project is multiple versions behind, complete the next hop, verify it, and then report the next required hop.
During the 6.5.x -> 7.6.x step, convert any remaining storiesOf stories to CSF instead of preserving compatibility mode.
Preserve the project's existing app structure. Only make the migration changes required for the current step.
Version Detection

Look at these signals together:

package.json versions for @storybook/react-native, storybook, @storybook/react, and @storybook/addon-ondevice-*
Whether the config folder is .storybook/ or .rnstorybook/
Metro config imports such as metro/withStorybook, metro/withStorybookConfig, or default-vs-named withStorybook
Story format usage: CSF vs storiesOf
Generated file names such as storybook.requires.js vs storybook.requires.ts

If the version is ambiguous, stop and clarify the current installed version instead of guessing.

Migration Selection

Use exactly one reference file:

9.x -> 10.x: references/from-9-to-10.md
8.x -> 9.x: references/from-8-to-9.md
7.6.x -> 8.3.x: references/from-7-6-to-8-3.md
6.5.x -> 7.6.x: references/from-6-5-to-7-6.md
5.3.x -> 6.5.x: references/from-5-3-to-6-5.md
Workflow
Confirm the current Storybook version and whether the repo uses Expo, Expo Router, React Native CLI, or Re.Pack.
Pick the next migration step only. Never bundle multiple major upgrades together.
Apply the dependency, config, and source-file changes from the matching reference.
Regenerate storybook.requires or restart Metro when that step requires it.
Run the smallest useful verification available for the repo, such as the generation script, tests, lint, or the local Storybook app launch path.
If the repo still is not on the user's target version, stop with a clear note describing the next required migration step.
Output Expectations

When you finish a migration step, report:

The version hop that was completed
The files and config surfaces that changed
The verification you ran, or what you could not run
The next required migration hop, if the project is still behind
Weekly Installs
59
Repository
storybookjs/react-native
GitHub Stars
1.3K
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass