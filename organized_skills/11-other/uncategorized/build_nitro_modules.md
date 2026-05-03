---
rating: ⭐⭐⭐
title: build-nitro-modules
url: https://skills.sh/riteshshukla04/agent-skills/build-nitro-modules
---

# build-nitro-modules

skills/riteshshukla04/agent-skills/build-nitro-modules
build-nitro-modules
Installation
$ npx skills add https://github.com/riteshshukla04/agent-skills --skill build-nitro-modules
SKILL.md
Build Nitro Modules
Overview

End-to-end skill for building a React Native Nitro Module: monorepo scaffolding via Nitrogen, TypeScript HybridObject spec authoring, native code generation, platform implementation (C++/Swift/Kotlin), example app wiring, and publish preparation.

Nitro Modules use a codegen pipeline (nitrogen) that reads .nitro.ts spec files and generates native C++/Swift/Kotlin boilerplate. You then fill in the implementation. This is fundamentally different from old-style turbo modules.

NEVER modify any file inside nitrogen/generated/. These files are fully regenerated every time npx nitrogen runs — any manual edits will be silently overwritten. Always edit only the .nitro.ts spec file, then re-run nitrogen to regenerate.

Ask First — Before Doing Anything

First, determine what the user wants to do:

"Are you creating a new Nitro Module library from scratch, or adding a new HybridObject to an existing library?"

If creating a new library — ask all of these before any command:
Library name — What should the library be called? (e.g. react-native-math)
Monorepo with packages/ folder — Should the library live in packages/<name> inside a monorepo? (Strongly recommended — default: yes)
Example app — Should an example app be created to test the module? (Recommended — default: yes)
Native languages — Which platforms and languages?
iOS: swift (default) or cpp
Android: kotlin (default) or cpp
Cross-platform C++ only: both cpp
Module purpose — Briefly describe what the module does so the correct spec methods can be designed

Do not proceed past Step 1 of the build sequence until all five questions are answered.

If adding a HybridObject to an existing library — ask only:
HybridObject name — What should the new HybridObject be called? (e.g. Camera, Crypto)
Native languages — iOS: swift or cpp? Android: kotlin or cpp?
Purpose — What does this HybridObject do?

Then skip directly to spec-hybrid-object.md (write the spec), spec-nitro-json.md (add autolinking entry), native-nitrogen-codegen.md (re-run nitrogen), and the relevant native implementation file. Skip all setup, monorepo, and example app steps.

Typical Build Sequence
# 1. Scaffold
npx nitrogen@latest init react-native-math

# 2. Run codegen (from package folder after writing spec + nitro.json)
cd packages/react-native-math && npx nitrogen

# 3. Create example app
npx @react-native-community/cli@latest init --skip-install MathExample

# 4. Install and test
cd example && bun add ../packages/react-native-math
bun add react-native-nitro-modules
bun example android
bun example ios


Full step-by-step references below.

When to Apply

Reference these guidelines when:

Creating any new React Native native module using the Nitro framework
Writing HybridObject TypeScript specs (*.nitro.ts files)
Running Nitrogen codegen and implementing generated interfaces
Setting up a monorepo example app for a Nitro library
Configuring Android Gradle paths for a monorepo structure
Debugging autolinking failures or missing generated files
Preparing a Nitro module package for npm publishing
Priority-Ordered Guidelines
Priority	Category	Impact	Reference
1	Monorepo scaffold	CRITICAL	setup-monorepo-init.md
2	HybridObject spec	CRITICAL	spec-hybrid-object.md
3	nitro.json autolinking	CRITICAL	spec-nitro-json.md
4	Nitrogen codegen	HIGH	native-nitrogen-codegen.md
5	C++ implementation	HIGH	native-implement-cpp.md
6	Kotlin implementation	HIGH	native-implement-kotlin.md
7	Swift implementation	HIGH	native-implement-swift.md
8	Example app setup (if requested)	HIGH	example-app-setup.md
9	Android Gradle paths (if example app)	HIGH	example-android-config.md
10	Metro + install + test (if example app)	HIGH	example-metro-install.md
11	npm publish prep	MEDIUM	spec-package-publish.md
Quick Reference
Minimum HybridObject Spec (src/specs/Math.nitro.ts)
import { type HybridObject, NitroModules } from 'react-native-nitro-modules'

interface Math extends HybridObject<{ ios: 'swift'; android: 'kotlin' }> {
  add(a: number, b: number): number
}

const math = NitroModules.createHybridObject<Math>('Math')
export { math }

Minimum nitro.json
{
  "$schema": "https://nitro.margelo.com/nitro.schema.json",
  "cxxNamespace": ["math"],
  "ios": { "iosModuleName": "ReactNativeMath" },
  "android": {
    "androidNamespace": ["math"],
    "androidCxxLibName": "ReactNativeMath"
  },
  "autolinking": {
    "Math": { "swift": "HybridMath", "kotlin": "HybridMath" }
  }
}

Root package.json Scripts
{
  "scripts": {
    "specs": "bun --cwd packages/react-native-math run specs",
    "example": "bun --cwd example"
  }
}


Run: bun example android, bun example ios, bun specs

References
File	Description
setup-monorepo-init.md	Monorepo workspace structure and nitrogen init scaffold
spec-hybrid-object.md	Writing *.nitro.ts specs and exporting HybridObjects
spec-nitro-json.md	nitro.json all fields, autolinking, namespace configuration
native-nitrogen-codegen.md	Running Nitrogen and verifying generated files
native-implement-cpp.md	Implementing HybridObjects in C++
native-implement-kotlin.md	Implementing HybridObjects in Kotlin (Android)
native-implement-swift.md	Implementing HybridObjects in Swift (iOS)
example-app-setup.md	RN CLI example app init, workspace wiring, version alignment
example-android-config.md	settings.gradle and build.gradle monorepo path fixes
example-metro-install.md	Metro watchFolders, library install, App.tsx usage, test runs
spec-package-publish.md	package.json author, files field, npm publish readiness
Problem → Skill Mapping
Problem	Reference	Action
Don't know where to start	setup-monorepo-init.md	Scaffold with nitrogen init
Spec file syntax error	spec-hybrid-object.md	Fix *.nitro.ts interface
Autolinking not working	spec-nitro-json.md	Check nitro.json autolinking block
Nitrogen generates no files	native-nitrogen-codegen.md	Verify spec file extension and run command from right dir
C++ types unclear	native-implement-cpp.md	Follow type reference links to canonical examples
Kotlin compilation error	native-implement-kotlin.md	Check annotations and override modifiers
Swift compilation error	native-implement-swift.md	Check class inheritance and property signatures
Example app won't build (Android)	example-android-config.md	Fix Gradle monorepo path configuration
Metro can't resolve library	example-metro-install.md	Add watchFolders to metro.config.js
Version mismatch between example and package	example-app-setup.md	Align react-native versions across workspaces
Package missing files on npm	spec-package-publish.md	Fix files field in package.json
Weekly Installs
15
Repository
riteshshukla04/…t-skills
GitHub Stars
35
First Seen
Mar 8, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn