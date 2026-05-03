---
rating: ⭐⭐⭐
title: ruby-on-rails
url: https://skills.sh/faqndo97/ai-skills/ruby-on-rails
---

# ruby-on-rails

skills/faqndo97/ai-skills/ruby-on-rails
ruby-on-rails
Installation
$ npx skills add https://github.com/faqndo97/ai-skills --skill ruby-on-rails
SKILL.md

<essential_principles>

Vanilla Rails Philosophy

"No one paradigm" - Pragmatism over purity. Rails provides everything needed without complex architectural patterns.

1. Rich Domain Models Over Service Objects

Business logic lives in models. Use nested operation classes for complex workflows:

# Model method delegates to nested class
class Quote < ApplicationRecord
  def create_purchase_order
    PurchaseOrderCreation.new(self).call
  end
end

# app/models/quote/purchase_order_creation.rb
class Quote::PurchaseOrderCreation
  def initialize(quote) = @quote = quote

  def call
    ApplicationRecord.transaction do
      po = create_purchase_order
      update_quote_status
      po
    end
  end
end

2. Concerns for Cohesive Traits

Concerns represent domain concepts, not junk drawers:

module Closable
  extend ActiveSupport::Concern

  included do
    scope :open, -> { where(closed_at: nil) }
    scope :closed, -> { where.not(closed_at: nil) }
  end

  def close! = update!(closed_at: Time.current)
  def closed? = closed_at.present?
  def open? = !closed?
end

3. Thin Controllers, Fat Models

Controllers coordinate; models contain logic. Use filter chaining:

def index
  resources = Resource.all
    .then(&method(:apply_scoping))
    .then(&method(:filter_by_status))
    .then(&method(:apply_ordering))

  render json: ResourceBlueprint.render(resources)
end

4. Current Pattern for Request Context

Use Current for cross-cutting concerns:

class Current < ActiveSupport::CurrentAttributes
  attribute :user, :organization
end

# Set once in controller, use anywhere
Current.organization


</essential_principles>

Build a new feature/endpoint
Debug an existing issue
Write/run tests
Optimize performance
Refactor code
Something else

Then read the matching workflow from workflows/ and follow it.

<verification_loop>

After Every Change
# 1. Syntax check
ruby -c app/models/changed_file.rb

# 2. Run tests
bin/rails test test/models/changed_file_test.rb

# 3. Lint
bundle exec rubocop app/models/changed_file.rb -a


Report: "Syntax: OK | Tests: X pass | Lint: clean" </verification_loop>

<reference_index>

Domain Knowledge

All in references/:

Architecture: architecture.md Models: models.md Controllers: controllers.md Serialization: blueprints.md Validations: validations-callbacks.md Background Jobs: background-jobs.md Performance: performance.md Testing: testing.md Multi-Tenant: multi-tenant.md Anti-Patterns: anti-patterns.md </reference_index>

<workflows_index>

Workflows

All in workflows/:

File	Purpose
build-feature.md	Create new feature/endpoint from scratch
debug.md	Find and fix bugs
write-tests.md	Write and run tests
optimize-performance.md	Profile and speed up
refactor.md	Restructure code following patterns
</workflows_index>	
Weekly Installs
19
Repository
faqndo97/ai-skills
GitHub Stars
32
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass