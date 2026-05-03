---
title: navigation-3
url: https://skills.sh/android/skills/navigation-3
---

# navigation-3

skills/android/skills/navigation-3
navigation-3
Installation
$ npx skills add https://github.com/android/skills --skill navigation-3
SKILL.md
Migration guide
Navigation 2 to Navigation 3 migration guide: Step-by-step guide to migrate an Android application from Navigation 2 to Navigation 3, covering dependency updates, route changes, state management, and UI component replacements.
Requirements
Guide: Migrate to type-safe navigation in Compose : Step-by-step guide to migrating an Android application from string-based navigation to Type-Safe Navigation in Jetpack Compose using Jetpack Navigation 2.
Developer documentation
*Navigation 3. Search documentation for more information on basics, saving and managing navigation state, modularizing navigation code, creating custom layouts using Scenes, animating between destinations, or applying logic or wrappers to destinations.
Recipes

Code examples showcasing common patterns.

Basic API usage
Basic: Shows most basic API usage.
Saveable back stack: Shows basic API usage with a persistent back stack.
Entry provider DSL: Shows basic API usage using the entryProvider DSL.
Common UI
Common UI: Demonstrates how to implement a common navigation UI pattern with a bottom navigation bar and multiple back stacks, where each tab in the navigation bar has its own navigation history.
Deep links
Basic: Shows how to parse a deep link URL from an Android Intent into a navigation key.
Advanced: Shows how to handle deep links with a synthetic back stack and correct "Up" navigation behavior.
Scenes
Use built-in Scenes
Dialog: Shows how to create a Dialog.
Create custom Scenes
BottomSheet: Shows how to create a BottomSheet destination.
List-Detail Scene: Demonstrates how to implement adaptive list-detail layouts using the Navigation 3 Scenes API.
Two pane Scene: Demonstrates how to implement adaptive two-pane layouts using the Navigation 3 Scenes API.
Material Adaptive
Material List-Detail: Demonstrates how to implement an adaptive list-detail layout using Material 3 Adaptive.
Material Supporting Pane: Demonstrates how to implement an adaptive supporting pane layout using Material 3 Adaptive.
Animations
Animations: Shows how to override the default animations for all destinations and a single destination.
Common back stack behavior
Multiple back stacks: Shows how to create multiple top level routes, each with its own back stack. Top level routes are displayed in a navigation bar allowing users to switch between them. State is retained for each top level route, and the navigation state persists config changes and process death.
Conditional navigation
Conditional navigation: Switch to a different navigation flow when a condition is met. For example, for authentication or first-time user onboarding.
Architecture
Modularized navigation code (Hilt): Demonstrates how to decouple navigation code into separate modules using Hilt or Dagger for DI.
Modularized navigation code (Koin): Demonstrates how to decouple navigation code into separate modules using Koin for DI.
Working with ViewModel
Passing navigation arguments
Basic ViewModel : Navigation arguments are passed to a ViewModel constructed using viewModel()
Returning results
Returning Results as Events : Returning results as events to content in another NavEntry
Returning Results as State : Returning results as state stored in a CompositionLocal
Weekly Installs
216
Repository
android/skills
GitHub Stars
4.5K
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn