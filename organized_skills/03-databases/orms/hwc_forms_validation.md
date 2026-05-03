---
rating: ⭐⭐
title: hwc-forms-validation
url: https://skills.sh/thehotwireclub/hotwire_club-skills/hwc-forms-validation
---

# hwc-forms-validation

skills/thehotwireclub/hotwire_club-skills/hwc-forms-validation
hwc-forms-validation
Installation
$ npx skills add https://github.com/thehotwireclub/hotwire_club-skills --skill hwc-forms-validation
SKILL.md
Forms & Validation

Implement form-centric Hotwire workflows with Turbo Frames and Stimulus.

Core Workflow
Identify the form flow: create/edit, inline edit, typeahead, modal form, or external controls.
Wrap the form interaction scope in a Turbo Frame when validation errors must rerender in place.
Return 422 for validation failures and 303 for successful redirects.
Handle post-submit behavior with turbo:submit-end only when Turbo defaults are insufficient.
Preserve user context during rerenders (focus/caret/selection).
Guardrails
Keep one source of truth for input state; avoid duplicate controls across frame and non-frame DOM.
Use the HTML form attribute for controls rendered outside the target <form> hierarchy.
Avoid firing submit logic on every keystroke without debounce/throttle.
Keep post-submit behavior explicit when form responses update only a frame.
Load References Selectively

Open only the file needed for the current request.

Inline editing: references/2024-02-27-turbo-frames-inline-edit.md
Modal validation flows: references/2024-05-21-turbo-frames-modals-validation.md
Typeahead search: references/2023-11-07-turbo-frames-typeahead-search.md
Typeahead validation with focus handling: references/2025-10-20-turbo-frames-typeahead-validation.md
External form controls in frames: references/2026-02-03-turbo-frames-external-form.md
Stimulus action parameters for forms: references/2024-01-16-stimulus-action-parameters.md

Use references/INDEX.md for the full catalog.

Escalate to Neighbor Skills
Navigation/history/cache behavior: use hwc-navigation-content
WebSocket or Turbo Stream push updates: use hwc-realtime-streaming
Media upload/playback behavior: use hwc-media-content
Generic UX polish (spinners/progress/transitions): use hwc-ux-feedback
General Stimulus API design questions: use hwc-stimulus-fundamentals
Weekly Installs
118
Repository
thehotwireclub/…b-skills
GitHub Stars
118
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass