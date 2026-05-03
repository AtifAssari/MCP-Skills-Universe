---
title: stimulus
url: https://skills.sh/faqndo97/ai-skills/stimulus
---

# stimulus

skills/faqndo97/ai-skills/stimulus
stimulus
Installation
$ npx skills add https://github.com/faqndo97/ai-skills --skill stimulus
SKILL.md

<essential_principles>

How Stimulus Works

Stimulus is a modest JavaScript framework that connects JavaScript behavior to HTML via data attributes. It doesn't render HTML—it enhances existing HTML with interactivity.

1. HTML-First Philosophy

State lives in the DOM, not JavaScript. Controllers can be discarded between page changes and reinitialize from cached HTML. Design controllers to read state from data attributes and restore themselves on reconnection.

2. Convention Over Configuration

Stimulus uses predictable naming conventions:

Controller: data-controller="clipboard"
Targets: data-clipboard-target="source"
Actions: data-action="click->clipboard#copy"
Values: data-clipboard-url-value="/api/copy"
Classes: data-clipboard-supported-class="visible"
Outlets: data-clipboard-result-outlet="#result"
3. Lifecycle Awareness

Controllers have three lifecycle callbacks:

initialize() - Called once when controller is instantiated
connect() - Called when controller is connected to DOM (can happen multiple times with Turbo)
disconnect() - Called when controller is removed from DOM

Always clean up in disconnect() what you set up in connect() (timers, event listeners, observers).

4. Scope Isolation

Each controller only sees elements within its scope (the element with data-controller and its descendants). Targets must be within scope. Use outlets to communicate across controller boundaries.

5. Progressive Enhancement

Build HTML that works without JavaScript first. Use Stimulus to enhance, not replace. Check for API support before using features:

connect() {
  if ("clipboard" in navigator) {
    this.element.classList.add(this.supportedClass)
  }
}


</essential_principles>

Build a new controller
Debug an existing controller
Add a feature to a controller
Review controller(s) for best practices
Optimize performance
Implement a UI pattern (modal, dropdown, tabs, etc.)
Integrate with Turbo
Handle forms
Something else

Wait for response before proceeding.

After reading the workflow, follow it exactly.

<verification_loop>

After Every Change
Does it connect? Check browser console for Stimulus connection messages
Do targets resolve? Verify this.hasXxxTarget returns true
Do actions fire? Add temporary console.log in action methods
Does it clean up? Navigate away and back - no errors, no memory leaks
// Debug mode - add to application.js
application.debug = true


Report to the user:

"Controller connects: ✓"
"Targets found: X of Y"
"Actions working: ✓/✗"
"Ready for testing" </verification_loop>

<reference_index>

Domain Knowledge

All in references/:

Core APIs: architecture.md, targets.md, values.md, actions.md, outlets.md, classes.md Ecosystem: stimulus-use.md, ui-patterns.md Integration: turbo-integration.md Quality: testing-debugging.md, performance.md, anti-patterns.md </reference_index>

<workflows_index>

Workflows

All in workflows/:

File	Purpose
build-new-controller.md	Create new controller from scratch
debug-controller.md	Find and fix bugs
add-feature.md	Add functionality to existing controller
review-controller.md	Audit controllers for best practices
optimize-performance.md	Profile and speed up
implement-ui-pattern.md	Build modals, dropdowns, tabs, etc.
integrate-turbo.md	Work with Turbo Frames/Streams
handle-forms.md	Form validation and submission
</workflows_index>	
Weekly Installs
21
Repository
faqndo97/ai-skills
GitHub Stars
32
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass