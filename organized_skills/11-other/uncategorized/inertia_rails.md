---
rating: ⭐⭐⭐
title: inertia-rails
url: https://skills.sh/faqndo97/ai-skills/inertia-rails
---

# inertia-rails

skills/faqndo97/ai-skills/inertia-rails
inertia-rails
Installation
$ npx skills add https://github.com/faqndo97/ai-skills --skill inertia-rails
SKILL.md

<essential_principles>

How Inertia Rails Works

Inertia is a bridge between Rails and modern JavaScript frameworks (React, Vue, Svelte). It lets you build SPAs using classic server-side routing and controllers—no client-side routing or separate APIs needed.

1. Server-Driven Architecture

Controllers render Inertia responses instead of views. Data flows from Rails to JavaScript components as props:

render inertia: 'Users/Show', props: { user: user.as_json }

2. No Client-Side Routing

Routes live in config/routes.rb. Inertia intercepts link clicks and form submissions, making XHR requests that return JSON with component name and props. The client swaps components without full page reloads.

3. Convention-Based Component Resolution

By default, render inertia: { user: } in UsersController#show renders app/frontend/pages/users/show.(jsx|vue|svelte). Override with explicit component names when needed.

4. Validation via Redirects

Unlike typical SPAs returning 422 JSON responses, Inertia follows traditional Rails patterns:

Controller validates and redirects back on failure
Errors are flashed and shared as props
Form state is preserved automatically
5. Shared Data Pattern

Use inertia_share in controllers to provide data to all pages (current_user, flash messages, notifications). Data is included in every response—use sparingly. </essential_principles>

Set up Inertia in a Rails project
Create a new page/component
Build a form with validation
Add shared data (auth, flash, etc.)
Handle redirects and navigation
Debug an Inertia issue
Test an Inertia controller
Optimize with partial reloads
Something else

Wait for response before proceeding.

After reading the workflow, follow it exactly.

<verification_loop>

After Every Change
Does the page render? Check Rails logs for Inertia response
Are props received? Console.log props in component
Does navigation work? Click links - should not full-reload
Do forms submit? Check Network tab for XHR requests
Are errors displayed? Test validation failures
# Rails debug - check response type
render inertia: 'Page', props: { debug: true }

// Frontend debug - log all props
console.log(usePage().props)


Report to the user:

"Inertia response: ✓"
"Props received: X keys"
"Navigation: SPA mode ✓/✗"
"Ready for testing" </verification_loop>

<reference_index>

Domain Knowledge

All in references/:

Core: setup.md, responses.md, forms.md, validation.md Data Flow: shared-data.md, links.md Quality: testing.md Cookbook: cookbook.md (shadcn/ui, Inertia Modal, meta tags, error types) </reference_index>

<workflows_index>

Workflows

All in workflows/:

File	Purpose
setup-inertia.md	Install and configure Inertia Rails
create-page.md	Build new pages with props
build-form.md	Forms with validation and useForm
shared-data.md	Share auth/flash across all pages
navigation.md	Links, redirects, router methods
debug-inertia.md	Find and fix Inertia issues
testing.md	Test Inertia controllers
partial-reloads.md	Optimize with selective data loading
</workflows_index>	
Weekly Installs
13
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