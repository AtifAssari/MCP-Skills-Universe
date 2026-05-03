---
title: hig-patterns
url: https://skills.sh/raintree-technology/apple-hig-skills/hig-patterns
---

# hig-patterns

skills/raintree-technology/apple-hig-skills/hig-patterns
hig-patterns
Installation
$ npx skills add https://github.com/raintree-technology/apple-hig-skills --skill hig-patterns
SKILL.md
Apple HIG: Interaction Patterns

Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered.

Key Principles

Minimize modality. Use modality only when it is critical to get attention, a task must be completed or abandoned, or saving changes is essential. Prefer non-modal alternatives.

Provide clear feedback. Every action should produce visible, audible, or haptic response. Activity indicators for indeterminate waits, progress bars for determinate, haptics for physical confirmation.

Support undo over confirmation dialogs. Destructive actions should be reversible when possible. Undo is almost always better than "Are you sure?"

Launch quickly. Display a launch screen that transitions seamlessly into the first screen. No splash screens with logos. Restore previous state.

Defer sign-in. Let users explore before requiring account creation. Support Sign in with Apple and passkeys.

Keep onboarding brief. Three screens max. Let users skip. Teach through progressive disclosure and contextual hints.

Use progressive disclosure. Show essentials first, let users drill into details. Don't overwhelm with every option on one screen.

Respect user attention. Consolidate notifications, minimize interruptions, give users control over alerts. Never use notifications for marketing.

Reference Index
Reference	Topic	Key content
charting-data.md	Charting Data	Data visualization patterns, accessible charts, interactive elements
collaboration-and-sharing.md	Collaboration & Sharing	Share sheets, activity views, collaborative editing, SharePlay
drag-and-drop.md	Drag and Drop	Drag sources, drop targets, spring loading, multi-item drag, visual feedback
entering-data.md	Entering Data	Text fields, pickers, steppers, input validation, keyboard types, autofill
feedback.md	Feedback	Alerts, action sheets, haptic patterns, sound feedback, visual indicators
file-management.md	File Management	Document browser, file providers, iCloud integration, document lifecycle
going-full-screen.md	Going Full Screen	Full-screen transitions, immersive content, exiting full screen
launching.md	Launching	Launch screens, state restoration, cold vs warm launch
live-viewing-apps.md	Live Viewing Apps	Live content display, real-time updates, Live Activities, Dynamic Island
loading.md	Loading	Activity indicators, progress views, skeleton screens, lazy loading, placeholders
managing-accounts.md	Managing Accounts	Sign in with Apple, passkeys, account creation, credential autofill, account deletion
managing-notifications.md	Managing Notifications	Permission requests, grouping, actionable notifications, provisional delivery
modality.md	Modality	Sheets, alerts, popovers, full-screen modals, when to use each
multitasking.md	Multitasking	iPad Split View, Slide Over, Stage Manager, responsive layout, size class transitions
offering-help.md	Offering Help	Contextual tips, onboarding hints, help menus, support links
onboarding.md	Onboarding	Welcome screens, feature highlights, progressive onboarding, skip options
playing-audio.md	Playing Audio	Audio sessions, background audio, Now Playing, audio routing, interruptions
playing-haptics.md	Playing Haptics	Core Haptics, UIFeedbackGenerator, haptic patterns, custom haptics
playing-video.md	Playing Video	Video player controls, picture-in-picture, AirPlay, full-screen video
printing.md	Printing	Print dialogs, page setup, AirPrint integration
ratings-and-reviews.md	Ratings & Reviews	SKStoreReviewController, timing, frequency limits, in-app feedback
searching.md	Searching	Search bars, suggestions, scoped search, results display, recents
settings.md	Settings	In-app vs Settings app, preference organization, toggles, defaults
undo-and-redo.md	Undo and Redo	Shake to undo, undo/redo stack, multi-level undo
workouts.md	Workouts	Workout sessions, live metrics, Always On display, summaries, HealthKit
Pattern Selection Guide
User Goal	Recommended Pattern	Avoid
First app experience	Brief onboarding (max 3 screens) + progressive disclosure	Long tutorials, mandatory sign-up
Waiting for content	Skeleton screens or progress indicators	Blocking spinners with no context
Confirming destructive action	Undo support	Excessive "Are you sure?" dialogs
Collecting user input	Inline validation, smart defaults, autofill	Modal forms for simple inputs
Requesting permissions	Contextual, just-in-time with explanation	Requesting all permissions at launch
Providing feedback	Haptics + visual indicator	Silent actions with no confirmation
Organizing preferences	In-app settings for frequent items	Burying all settings in system Settings app
Output Format
Recommended pattern with rationale, citing the relevant reference file.
Step-by-step implementation covering each screen or state.
Platform variations for targeted platforms.
Common pitfalls that violate HIG for this pattern.
Questions to Ask
Where in the app does this pattern appear? What comes before and after?
Which platforms?
Designing from scratch or improving an existing flow?
Does this involve sensitive actions? (Destructive operations, payments, permissions)
Related Skills
hig-foundations -- Accessibility, color, typography, and privacy principles underlying every pattern
hig-platforms -- Platform-specific pattern implementations
hig-components-layout -- Structural components (tab bars, sidebars, split views) for navigation patterns
hig-components-content -- Content display within patterns (charts, collections, search results)

Built by Raintree Technology · More developer tools

Weekly Installs
166
Repository
raintree-techno…g-skills
GitHub Stars
45
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass