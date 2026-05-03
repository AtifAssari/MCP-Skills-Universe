---
rating: ⭐⭐⭐
title: form-object-patterns
url: https://skills.sh/thibautbaissac/rails_ai_agents/form-object-patterns
---

# form-object-patterns

skills/thibautbaissac/rails_ai_agents/form-object-patterns
form-object-patterns
Installation
$ npx skills add https://github.com/thibautbaissac/rails_ai_agents --skill form-object-patterns
SKILL.md
Form Object Patterns for Rails 8
Overview

Form objects encapsulate complex form logic:

Multi-model forms (user + profile + address)
Search/filter forms (non-persisted)
Wizard/multi-step forms
Virtual attributes with validation
Decoupled from ActiveRecord models
When to Use Form Objects
Scenario	Use Form Object?
Single model CRUD	No (use model)
Multi-model creation	Yes
Complex validations across models	Yes
Search/filter forms	Yes
Wizard/multi-step forms	Yes
API params transformation	Yes
Contact forms (no persistence)	Yes
TDD Workflow
Form Object Progress:
- [ ] Step 1: Define form requirements
- [ ] Step 2: Write form object spec (RED)
- [ ] Step 3: Run spec (fails)
- [ ] Step 4: Create form object
- [ ] Step 5: Run spec (GREEN)
- [ ] Step 6: Wire up controller
- [ ] Step 7: Create view form

Project Structure
app/
├── forms/
│   ├── application_form.rb       # Base class
│   ├── registration_form.rb      # Multi-model
│   ├── search_form.rb            # Non-persisted
│   └── wizard/
│       ├── base_form.rb
│       ├── step_one_form.rb
│       └── step_two_form.rb
spec/forms/
├── registration_form_spec.rb
└── search_form_spec.rb

Base Form Class
# app/forms/application_form.rb
class ApplicationForm
  include ActiveModel::Model
  include ActiveModel::Attributes
  include ActiveModel::Validations

  def self.model_name
    ActiveModel::Name.new(self, nil, name.chomp("Form"))
  end

  def persisted?
    false
  end

  def save
    return false unless valid?
    persist!
    true
  rescue ActiveRecord::RecordInvalid => e
    errors.add(:base, e.message)
    false
  end

  private

  def persist!
    raise NotImplementedError
  end
end

Patterns

Four patterns are implemented with full TDD cycles. See patterns.md:

Pattern 1: Multi-Model Registration Form — creates a User and Account in a transaction; validates email uniqueness and password confirmation; exposes form.user and form.account after save. Includes spec (RED) and implementation (GREEN).
Pattern 2: Search/Filter Form — non-persisted form with query, type, status, and date range filters applied as chainable scopes; exposes results and any_filters? helpers for views. Includes spec and implementation.
Pattern 3: Wizard/Multi-Step Form — Wizard::BaseForm provides next_step, previous_step, first_step?, last_step?, and progress_percentage; each step subclass declares its own attributes and validations.
Pattern 4: Contact Form (No Persistence) — overrides #save directly (no persist!); dispatches via deliver_later without writing to the database.
Controller and View Integration

See controller-and-views.md for:

Standard controller with allow_unauthenticated_access, #new / #create, render :new, status: :unprocessable_entity on failure
form_with model: @form views with error display
Search form partial with selects, date fields, and a "Clear" link when filters are active

Key conventions:

Use form_with model: @form, url: explicit_path — the form object is not an ActiveRecord model
Permit params with params.require(:model_name).permit(...) using the snake-case class name without "Form"
Always render :new, status: :unprocessable_entity on failure so Turbo handles the response
Checklist
 Spec written first (RED)
 Extends ApplicationForm or includes ActiveModel::Model
 Attributes declared with types
 Validations defined
 #save method with transaction (if multi-model)
 Controller uses form object
 View uses form_with model: @form
 Error handling in place
 All specs GREEN
References
patterns.md — Full TDD implementations of all 4 patterns: multi-model registration, search/filter, wizard/multi-step, and contact form
controller-and-views.md — Controller with unauthenticated access, registration form view, and search form partial
Weekly Installs
19
Repository
thibautbaissac/…i_agents
GitHub Stars
520
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass