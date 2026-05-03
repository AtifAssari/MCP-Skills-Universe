---
rating: ⭐⭐⭐
title: viewcomponent-patterns
url: https://skills.sh/thibautbaissac/rails_ai_agents/viewcomponent-patterns
---

# viewcomponent-patterns

skills/thibautbaissac/rails_ai_agents/viewcomponent-patterns
viewcomponent-patterns
Installation
$ npx skills add https://github.com/thibautbaissac/rails_ai_agents --skill viewcomponent-patterns
SKILL.md
ViewComponent Patterns for Rails 8
Overview

ViewComponents are Ruby objects for building reusable, testable view components:

Faster than partials (no partial lookup)
Unit testable without full request cycle
Encapsulate view logic with Ruby
Type-safe with explicit interfaces
Quick Start
# Add to Gemfile
bundle add view_component

# Generate component
bin/rails generate component Card title

TDD Workflow
ViewComponent Progress:
- [ ] Step 1: Write component spec (RED)
- [ ] Step 2: Run spec (fails - no component)
- [ ] Step 3: Generate component skeleton
- [ ] Step 4: Implement component
- [ ] Step 5: Run spec (GREEN)
- [ ] Step 6: Add variants/slots if needed

Project Structure
app/components/
├── application_component.rb    # Base class
├── card_component.rb
├── card_component.html.erb
├── badge_component.rb
├── badge_component.html.erb
├── table/
│   ├── component.rb
│   ├── component.html.erb
│   ├── header_component.rb
│   └── row_component.rb
└── modal/
    ├── component.rb
    └── component.html.erb

spec/components/
├── card_component_spec.rb
├── badge_component_spec.rb
└── table/
    └── component_spec.rb

Base Component
# app/components/application_component.rb
class ApplicationComponent < ViewComponent::Base
  include ActionView::Helpers::TagHelper
  include ActionView::Helpers::NumberHelper

  # Shared helper for nil values
  def not_specified_span
    tag.span(I18n.t("components.common.not_specified"), class: "text-slate-400 italic")
  end
end

Basic Component
# app/components/card_component.rb
class CardComponent < ApplicationComponent
  def initialize(title:, subtitle: nil)
    @title = title
    @subtitle = subtitle
  end

  attr_reader :title, :subtitle

  def subtitle?
    subtitle.present?
  end
end

<%# app/components/card_component.html.erb %>
<div class="bg-white rounded-lg shadow p-6">
  <h3 class="text-lg font-semibold text-slate-900"><%= title %></h3>
  <% if subtitle? %>
    <p class="subtitle text-sm text-slate-500"><%= subtitle %></p>
  <% end %>
  <div class="mt-4">
    <%= content %>
  </div>
</div>

Common Patterns

Five patterns are available. See patterns.md for full implementations:

Status Badge - BadgeComponent with variant constants (success/warning/error/info/neutral)
Component with Slots - renders_one/renders_many for flexible layouts (header, footer, actions)
Collection Component - TableComponent with optional custom rows slot
Modal Component - Size variants and slot-based structure
Wrapping Models (Presenter-like) - with_collection_parameter, delegate, and nested component rendering
Usage in Views
<%# Simple component %>
<%= render BadgeComponent.new(text: "Active", variant: :success) %>

<%# Component with block %>
<%= render CardComponent.new(title: "Stats") do %>
  <p>Content here</p>
<% end %>

<%# Component with slots %>
<%= render CardComponent.new do |card| %>
  <% card.with_header do %>
    <h2>Header</h2>
  <% end %>
  Content
<% end %>

<%# Collection %>
<%= render EventCardComponent.with_collection(@events) %>

Testing Components

Use render_inline and Capybara matchers (have_css, have_text) in specs tagged type: :component. See testing.md for:

Basic variant specs
Optional argument specs
Slot testing
Collection rendering specs
ViewComponent Previews setup
Checklist
 Spec written first (RED)
 Extends ApplicationComponent
 Uses slots for flexible content
 Variants use constants (Open/Closed)
 Tested with different inputs
 Collection rendering tested
 Preview created for development
 All specs GREEN
References
patterns.md - Badge, Slots, Table, Modal, Presenter-like, and Helpers patterns
testing.md - Component specs, slot testing, collection testing, Previews
Weekly Installs
24
Repository
thibautbaissac/…i_agents
GitHub Stars
520
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass