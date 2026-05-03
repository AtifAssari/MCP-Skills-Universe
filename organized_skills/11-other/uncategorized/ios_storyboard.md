---
rating: ⭐⭐
title: ios-storyboard
url: https://skills.sh/pproenca/dot-skills/ios-storyboard
---

# ios-storyboard

skills/pproenca/dot-skills/ios-storyboard
ios-storyboard
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill ios-storyboard
SKILL.md
iOS Storyboard Best Practices

Legacy interoperability guidance for storyboard-heavy code that still exists in clinic projects. Not for new SwiftUI clinic feature development.

Comprehensive UI design and architecture guide for Xcode Storyboard and Interface Builder, focused on building maintainable, adaptive, and accessible iOS interfaces. Contains 45 rules across 8 categories, prioritized by impact to guide automated refactoring and code generation.

Clinic Architecture Contract (iOS 26 / Swift 6.2)

All guidance in this skill assumes the clinic modular MVVM-C architecture:

Feature modules import Domain + DesignSystem only (never Data, never sibling features)
App target is the convergence point and owns DependencyContainer, concrete coordinators, and Route Shell wiring
Domain stays pure Swift and defines models plus repository, *Coordinating, ErrorRouting, and AppError contracts
Data owns SwiftData/network/sync/retry/background I/O and implements Domain protocols
Read/write flow defaults to stale-while-revalidate reads and optimistic queued writes
ViewModels call repository protocols directly (no default use-case/interactor layer)
When to Apply

Reference these guidelines when:

Creating or modifying Storyboard scenes in Xcode Interface Builder
Setting up Auto Layout constraints for adaptive layouts
Designing navigation flows with segues and storyboard references
Configuring size classes and trait variations for universal apps
Reviewing storyboard XML diffs and resolving merge conflicts
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Storyboard Architecture	CRITICAL	arch-
2	Auto Layout Constraints	CRITICAL	layout-
3	Navigation & Segues	HIGH	nav-
4	Adaptive Layout & Size Classes	HIGH	adapt-
5	View Hierarchy & Stack Views	MEDIUM-HIGH	view-
6	Accessibility & VoiceOver	MEDIUM	ally-
7	Version Control & Collaboration	MEDIUM	vcs-
8	Debugging & Inspection	LOW-MEDIUM	debug-
Quick Reference
1. Storyboard Architecture (CRITICAL)
arch-split-storyboards - Split Monolithic Storyboards into Feature Modules
arch-storyboard-references - Use Storyboard References for Cross-Module Navigation
arch-one-scene-per-flow - Limit Each Storyboard to a Single User Flow
arch-initial-view-controller - Set Initial View Controller Explicitly in Every Storyboard
arch-avoid-hardcoded-identifiers - Avoid Hardcoded Storyboard and Cell Identifiers
arch-scene-naming - Use Descriptive Scene Labels in Document Outline
arch-modular-xibs - Extract Reusable Views into Separate XIB Files
2. Auto Layout Constraints (CRITICAL)
layout-avoid-fixed-dimensions - Avoid Fixed Width and Height Constraints
layout-leading-trailing - Use Leading and Trailing Instead of Left and Right
layout-safe-area - Constrain Views to Safe Area Guides
layout-content-hugging - Set Content Hugging and Compression Resistance Priorities
layout-constraint-nearest-neighbor - Constrain to Nearest Neighbor Views
layout-avoid-constant-offsets - Use Layout Margins Instead of Constant Offsets
layout-inequality-constraints - Use Inequality Constraints for Flexible Minimums and Maximums
layout-constraint-priorities - Assign Distinct Priorities to Optional Constraints
3. Navigation & Segues (HIGH)
nav-prepare-for-segue - Pass Data via prepare(for:sender:) Instead of Direct Property Access
nav-unwind-segues - Use Unwind Segues to Navigate Backward
nav-avoid-mixed-navigation - Avoid Mixing Segue and Programmatic Navigation
nav-adaptive-segues - Use Show and Show Detail Instead of Push and Modal
nav-perform-segue-validation - Validate Segue Conditions with shouldPerformSegue
nav-container-view-controllers - Use Container Views for Embedded Child View Controllers
4. Adaptive Layout & Size Classes (HIGH)
adapt-size-classes - Configure Constraints per Size Class Using Vary for Traits
adapt-trait-variations - Use Trait Variations for Font and Spacing Adjustments
adapt-safe-area-all-devices - Test Adaptive Layouts on All Device Size Classes
adapt-readable-content-guide - Use Readable Content Guide for Text on Large Screens
adapt-dynamic-type - Support Dynamic Type for All Text Labels
5. View Hierarchy & Stack Views (MEDIUM-HIGH)
view-prefer-stack-views - Use Stack Views Instead of Manual Constraints for Linear Layouts
view-avoid-deep-nesting - Avoid Deeply Nested Stack Views Beyond Two Levels
view-intrinsic-content-size - Rely on Intrinsic Content Size for Standard UIKit Controls
view-placeholder-intrinsic-size - Use Placeholder Intrinsic Size for Custom Views in Storyboard
view-clip-to-bounds - Enable Clip to Bounds for Views with Corner Radius
view-content-mode - Set Correct Content Mode for UIImageView in Storyboard
6. Accessibility & VoiceOver (MEDIUM)
ally-labels - Set Accessibility Labels for All Interactive Elements
ally-traits - Assign Correct Accessibility Traits in Interface Builder
ally-grouping - Group Related Elements for VoiceOver Navigation
ally-identifiers - Set Accessibility Identifiers for UI Testing
ally-dynamic-labels - Update Accessibility Labels for Dynamic Content
7. Version Control & Collaboration (MEDIUM)
vcs-one-scene-per-developer - Assign Storyboard Scenes to Individual Developers
vcs-open-as-source - Review Storyboard Diffs as Source Code Before Committing
vcs-lock-storyboard-files - Use Git File Locking for Active Storyboard Edits
vcs-gitattributes-merge - Configure .gitattributes to Use Union Merge for Storyboards
8. Debugging & Inspection (LOW-MEDIUM)
debug-view-hierarchy - Use Debug View Hierarchy to Inspect Layout Issues
debug-ambiguous-layout - Use hasAmbiguousLayout to Detect Constraint Problems at Runtime
debug-constraint-identifier - Assign Identifiers to Constraints for Readable Logs
debug-stale-outlets - Remove Stale Outlet Connections to Prevent Crashes
How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions - Category structure and impact levels
Rule template - Template for adding new rules
Reference Files
File	Description
references/_sections.md	Category definitions and ordering
assets/templates/_template.md	Template for new rules
metadata.json	Version and reference information
Weekly Installs
127
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass