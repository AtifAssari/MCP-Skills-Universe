---
title: mobile web domain knowledge
url: https://skills.sh/danhvb/my-ba-skills/mobile-web-domain-knowledge
---

# mobile web domain knowledge

skills/danhvb/my-ba-skills/Mobile Web Domain Knowledge
Mobile Web Domain Knowledge
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'Mobile Web Domain Knowledge'
SKILL.md
Mobile/Web Domain Knowledge Skill
Purpose

Provide comprehensive knowledge for analyzing requirements in mobile and web application projects, covering platform differences, UX patterns, and technical considerations.

Application Types
Web Applications

Static Website: HTML/CSS, no server logic Single Page App (SPA): Client-side rendering (React, Vue, Angular) Server-Side Rendering (SSR): Server renders HTML (Next.js, Nuxt) Progressive Web App (PWA): Web app with native-like features

Mobile Applications

Native: Platform-specific (Swift/iOS, Kotlin/Android) Cross-Platform: Single codebase (React Native, Flutter) Hybrid: Web in native container (Ionic, Cordova) PWA: Web app installable on mobile

Comparison
Aspect	Native	Cross-Platform	PWA
Performance	Best	Good	Good
Device Access	Full	Most	Limited
Development Cost	High (2 codebases)	Medium	Low
App Store	Required	Required	Optional
Update Speed	App store review	App store review	Instant
Offline	Full	Full	Limited
Platform Requirements
iOS Considerations
Swift/Objective-C or React Native/Flutter
iOS 15+ support (recommended)
App Store guidelines compliance
Apple Sign-In required if social login
Face ID/Touch ID for authentication
Push notifications via APNs
In-app purchases via Apple (30% fee)
Privacy nutrition labels
Android Considerations
Kotlin/Java or React Native/Flutter
Android 12+ support (recommended)
Google Play Store guidelines
Material Design principles
Fingerprint/biometric authentication
Push notifications via FCM
Multiple screen sizes/densities
Permissions model
Web Considerations
Browser compatibility (Chrome, Safari, Firefox, Edge)
Responsive design (mobile-first)
Accessibility (WCAG 2.1 AA)
SEO requirements
Performance (Core Web Vitals)
Progressive enhancement
Common Requirements Patterns
Authentication

Requirements:

REQ-AUTH-001: User shall login with email and password
REQ-AUTH-002: User shall login with social accounts (Google, Facebook, Apple)
REQ-AUTH-003: User shall use biometric authentication (Face ID, Touch ID, Fingerprint)
REQ-AUTH-004: Session shall expire after 30 minutes of inactivity
REQ-AUTH-005: User shall reset password via email link


Security Considerations:

Secure token storage (Keychain/Keystore)
Certificate pinning
HTTPS only
OAuth 2.0/OIDC standards
Rate limiting
Offline Functionality

Levels of Offline Support:

Level 1: Read-only Cache

View previously loaded data
No modifications offline
Simple implementation

Level 2: Optimistic Updates

View cached data
Make changes offline
Sync when online
Conflict resolution needed

Level 3: Full Offline

Complete feature set offline
Queue all actions
Complex sync logic
Background sync

Requirements Example:

REQ-OFFLINE-001: App shall cache last 50 orders for offline viewing
REQ-OFFLINE-002: App shall indicate offline status to user
REQ-OFFLINE-003: App shall queue actions when offline
REQ-OFFLINE-004: App shall auto-sync when connection restored
REQ-OFFLINE-005: App shall notify user of sync conflicts

Push Notifications

Types:

Transactional: Order updates, password reset
Marketing: Promotions, recommendations
Re-engagement: Cart abandonment, inactive user

Requirements:

REQ-PUSH-001: User shall receive order status notifications
REQ-PUSH-002: User shall opt-in to marketing notifications
REQ-PUSH-003: Notification shall deep-link to relevant screen
REQ-PUSH-004: User shall manage notification preferences in settings


Technical:

iOS: APNs (Apple Push Notification service)
Android: FCM (Firebase Cloud Messaging)
Web: Web Push API
Performance Requirements

Mobile Performance:

REQ-PERF-001: App shall launch in < 2 seconds (cold start)
REQ-PERF-002: Screen transitions shall complete in < 300ms
REQ-PERF-003: API responses shall complete in < 2 seconds
REQ-PERF-004: App shall maintain 60 fps during scrolling
REQ-PERF-005: Crash rate shall be < 1%


Web Performance (Core Web Vitals):

REQ-PERF-010: LCP (Largest Contentful Paint) < 2.5 seconds
REQ-PERF-011: FID (First Input Delay) < 100ms
REQ-PERF-012: CLS (Cumulative Layout Shift) < 0.1
REQ-PERF-013: TTI (Time to Interactive) < 3.8 seconds

Responsive Design

Breakpoints:

Mobile: < 768px
Tablet: 768px - 1024px
Desktop: > 1024px

Requirements:

REQ-RESP-001: Layout shall adapt to screen sizes 320px to 2560px
REQ-RESP-002: Touch targets shall be minimum 44x44 pixels on mobile
REQ-RESP-003: Content shall be readable without horizontal scroll
REQ-RESP-004: Images shall use responsive sizing (srcset)

Accessibility (WCAG 2.1)

Requirements:

REQ-A11Y-001: All images shall have alt text
REQ-A11Y-002: Color contrast ratio shall be 4.5:1 minimum
REQ-A11Y-003: All interactive elements shall be keyboard accessible
REQ-A11Y-004: Form fields shall have visible labels
REQ-A11Y-005: Error messages shall be associated with fields
REQ-A11Y-006: App shall support screen readers (VoiceOver, TalkBack)

Key UX Patterns
Navigation
Tab bar (mobile): 3-5 main sections
Hamburger menu: Secondary navigation
Bottom sheets: Contextual actions
Modal dialogs: Focused tasks
Forms
Single column layout (mobile)
Keyboard type matching input
Inline validation
Clear error messages
Progress indicators for multi-step
Loading States
Skeleton screens
Pull to refresh
Infinite scroll vs pagination
Optimistic UI updates
Gestures (Mobile)
Tap: Primary action
Long press: Secondary menu
Swipe: List actions, navigation
Pinch: Zoom
App Store Considerations
App Store (iOS)
Review time: 24-48 hours
Human review for initial submission
Reject reasons: bugs, crashes, guideline violations
Required: Privacy policy, age rating
In-app purchases: 15-30% commission
Google Play (Android)
Review time: Few hours to days
Automated + human review
Required: Privacy policy, age rating
In-app purchases: 15-30% commission
Common Rejection Reasons
Crashes or bugs
Incomplete functionality
Privacy issues
Guideline violations
Misleading metadata
Broken links
Analytics & Tracking

Key Events:

App install/open
Screen views
Feature usage
Conversion events
Errors/crashes

Tools:

Firebase Analytics
Mixpanel
Amplitude
App Store Connect / Google Play Console
Questions for Stakeholders
Native vs cross-platform vs PWA?
Which platforms and versions to support?
Offline functionality needed?
Push notification use cases?
Performance expectations?
Accessibility requirements?
App store presence required?
Analytics requirements?
References
Apple Human Interface Guidelines
Material Design Guidelines
Web Content Accessibility Guidelines (WCAG)
Core Web Vitals Documentation
Weekly Installs
–
Repository
danhvb/my-ba-skills
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass