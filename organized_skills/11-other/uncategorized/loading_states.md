---
rating: ⭐⭐⭐
title: loading-states
url: https://skills.sh/sanky369/vibe-building-skills/loading-states
---

# loading-states

skills/sanky369/vibe-building-skills/loading-states
loading-states
Installation
$ npx skills add https://github.com/sanky369/vibe-building-skills --skill loading-states
SKILL.md
Loading & Empty States

Maintain user confidence when content isn't immediately available.

Loading State Types
Choose by Duration
Duration	Recommendation
< 100ms	No indicator needed
100ms - 1s	Subtle indicator (opacity change)
1s - 10s	Skeleton screen or spinner
> 10s	Progress bar with estimate
Skeleton Screens
When to Use
Page or section content loading
Lists, cards, tables
Better than spinners for known layouts
Basic Skeleton
.skeleton {
  background: #e5e7eb;
  border-radius: 4px;
}

/* Animated shimmer */
.skeleton-animated {
  background: linear-gradient(
    90deg,
    #f3f4f6 25%,
    #e5e7eb 50%,
    #f3f4f6 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}

@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

Skeleton Components
<!-- Text skeleton -->
<div class="skeleton skeleton-text" style="width: 80%"></div>
<div class="skeleton skeleton-text" style="width: 60%"></div>

<!-- Avatar skeleton -->
<div class="skeleton skeleton-avatar"></div>

<!-- Image skeleton -->
<div class="skeleton skeleton-image"></div>

.skeleton-text {
  height: 16px;
  margin-bottom: 8px;
}

.skeleton-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
}

.skeleton-image {
  width: 100%;
  aspect-ratio: 16/9;
}

Card Skeleton Example
<article class="card card-skeleton">
  <div class="skeleton skeleton-image"></div>
  <div class="card-content">
    <div class="skeleton skeleton-text" style="width: 70%"></div>
    <div class="skeleton skeleton-text" style="width: 90%"></div>
    <div class="skeleton skeleton-text" style="width: 50%"></div>
  </div>
</article>

What NOT to Skeleton
Modals (should be instant or loading indicator inside)
Toasts/notifications
Dropdown menus
The skeleton itself shouldn't have a skeleton
Spinners
When to Use
Unknown content structure
Short operations (1-3 seconds)
Small areas (buttons, inputs)
Simple Spinner
.spinner {
  width: 24px;
  height: 24px;
  border: 3px solid #e5e7eb;
  border-top-color: var(--primary);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

Button Loading State
.button-loading {
  position: relative;
  color: transparent; /* Hide text */
  pointer-events: none;
}

.button-loading::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 20px;
  height: 20px;
  border: 2px solid currentColor;
  border-top-color: transparent;
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
}

Inline Loading Text
<span class="loading-text">
  Loading
  <span class="loading-dots">
    <span>.</span><span>.</span><span>.</span>
  </span>
</span>

Progress Bars
When to Use
Operations > 10 seconds
File uploads/downloads
Multi-step processes
Basic Progress Bar
<div class="progress">
  <div
    class="progress-bar"
    role="progressbar"
    style="width: 65%"
    aria-valuenow="65"
    aria-valuemin="0"
    aria-valuemax="100"
  >
    65%
  </div>
</div>

.progress {
  height: 8px;
  background: #e5e7eb;
  border-radius: 4px;
  overflow: hidden;
}

.progress-bar {
  height: 100%;
  background: var(--primary);
  transition: width 0.3s ease-out;
}

Indeterminate Progress
.progress-indeterminate .progress-bar {
  width: 30%;
  animation: indeterminate 1.5s infinite ease-in-out;
}

@keyframes indeterminate {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(400%); }
}

Empty States
Types of Empty States
First Use: User hasn't added data yet
No Results: Search/filter returned nothing
Error State: Something went wrong
Success Empty: Completed all tasks (inbox zero)
First Use Empty State
<div class="empty-state">
  <img src="illustration.svg" alt="" class="empty-illustration">
  <h3 class="empty-title">No projects yet</h3>
  <p class="empty-description">
    Create your first project to get started
  </p>
  <button class="button-primary">
    Create Project
  </button>
</div>

No Results Empty State
<div class="empty-state">
  <span class="empty-icon">🔍</span>
  <h3 class="empty-title">No results found</h3>
  <p class="empty-description">
    Try adjusting your search or filters
  </p>
  <button class="button-secondary">
    Clear Filters
  </button>
</div>

Empty State Styles
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
  text-align: center;
}

.empty-illustration {
  width: 200px;
  max-width: 100%;
  margin-bottom: 24px;
}

.empty-icon {
  font-size: 48px;
  margin-bottom: 16px;
}

.empty-title {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 8px;
  color: var(--text-primary);
}

.empty-description {
  font-size: 14px;
  color: var(--text-secondary);
  max-width: 300px;
  margin-bottom: 24px;
}

Error States
<div class="empty-state error-state">
  <span class="empty-icon">⚠️</span>
  <h3 class="empty-title">Something went wrong</h3>
  <p class="empty-description">
    We couldn't load your data. Please try again.
  </p>
  <button class="button-primary">
    Retry
  </button>
</div>

Best Practices
Do
Match skeleton layout to actual content
Show loading state immediately (don't wait)
Use animations to indicate activity
Provide progress info when possible
Include helpful actions in empty states
Keep messaging friendly and helpful
Don't
Show spinners for everything
Use loading states for instant operations
Leave users without feedback
Make empty states feel like dead ends
Animate aggressively (respect motion preferences)
Accessibility
/* Announce loading to screen readers */
.loading-region[aria-busy="true"]::before {
  content: "Loading...";
  position: absolute;
  clip: rect(0, 0, 0, 0);
}

/* Respect reduced motion */
@media (prefers-reduced-motion: reduce) {
  .skeleton-animated {
    animation: none;
  }

  .spinner {
    animation-duration: 1.5s;
  }
}

Checklist
 Loading appears within 100ms of action
 Skeleton matches content structure
 Progress shown for long operations (>10s)
 Empty states have helpful actions
 Error states include retry option
 Animations respect prefers-reduced-motion
 Screen readers announce loading state
 Loading doesn't block entire page unnecessarily
Weekly Installs
37
Repository
sanky369/vibe-b…g-skills
GitHub Stars
21
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass