---
title: laravel:prompt-structure
url: https://skills.sh/jpcaparas/superpowers-laravel/laravel:prompt-structure
---

# laravel:prompt-structure

skills/jpcaparas/superpowers-laravel/laravel:prompt-structure
laravel:prompt-structure
Installation
$ npx skills add https://github.com/jpcaparas/superpowers-laravel --skill laravel:prompt-structure
SKILL.md
Prompt Structure

Well-structured prompts get complete, actionable responses. Poor structure leads to back-and-forth clarifications and incomplete solutions.

Separate Concerns
Ineffective

"Update the User model to add email verification and also create an API endpoint for password reset and add validation for the profile update form"

Effective

Break into focused requests:

"Add email verification to User model using Laravel's MustVerifyEmail trait"
"Create password reset API endpoint at POST /api/password/reset"
"Add validation to ProfileUpdateRequest for name, email, and bio fields"

Each request has one clear goal. Easier to review, test, and iterate.

Prioritize and Sequence
Ineffective

"Need authentication, user dashboard, admin panel, and email notifications"

Effective

"Let's build authentication first:

Set up Sanctum for API authentication
Create login/register endpoints
Add middleware to protect routes

Once auth works, we'll add the user dashboard, then admin features, then notifications."

Sequence matters. Build foundation first, then features that depend on it.

Specify Acceptance Criteria
Vague

"Make the checkout process work"

Specific

"Implement checkout process with these requirements:

User must be authenticated
Cart must have at least one item
Calculate total including tax (8.5%)
Create Order record with 'pending' status
Dispatch ProcessOrderJob to queue
Return order ID and confirmation message
Handle payment failures gracefully"

Clear criteria = clear implementation.

Break Down Work
Too Large

"Build a complete blog system with posts, comments, categories, tags, and search"

Right-Sized

"Let's start with core post functionality:

Phase 1: Basic Posts

Create Post model (title, content, published_at)
Add CRUD endpoints
Write feature tests for create/read/update/delete

Phase 2: Categories

Add Category model with belongsToMany relationship
Update post endpoints to handle categories
Test category assignment

Phase 3: Comments (and so on...)

Each phase is testable and deliverable."

Refactoring Requests
Unclear

"This code is messy, clean it up"

Clear

"Refactor UserController@store:

Current problem:

80 lines in one method
Mixes validation, business logic, and email sending
Hard to test individual pieces

Desired improvements:

Extract validation to UserStoreRequest
Move user creation logic to UserService
Dispatch SendWelcomeEmail job instead of inline sending
Controller should orchestrate, not implement"

Explain the problem and the desired state.

Planning Features
Ineffective

"Add social login"

Effective

"Add GitHub OAuth login:

Acceptance criteria:

User clicks 'Login with GitHub' button
Redirects to GitHub OAuth
On callback, create or find user by github_id
Store github_token for API access
Redirect to dashboard with session

Testable increments:

Set up Socialite with GitHub provider
Add github_id and github_token columns to users
Create OAuth controller with redirect and callback methods
Write feature test for full OAuth flow
Add 'Login with GitHub' button to login page"

Break it down. Make it testable.

Quick Reference

Structure your prompts:

One concern per request - Don't mix unrelated changes
Sequence logically - Build dependencies first
Define success - What does "done" look like?
Break down large work - Aim for testable increments
Explain refactoring - Current problem + desired state

Clear structure = clear results.

Weekly Installs
52
Repository
jpcaparas/super…-laravel
GitHub Stars
131
First Seen
Jan 21, 2026