---
rating: ⭐⭐⭐
title: dhh-rails-style
url: https://skills.sh/everyinc/compound-engineering-plugin/dhh-rails-style
---

# dhh-rails-style

skills/everyinc/compound-engineering-plugin/dhh-rails-style
dhh-rails-style
Installation
$ npx skills add https://github.com/everyinc/compound-engineering-plugin --skill dhh-rails-style
Summary

Rails code following 37signals conventions: REST purity, fat models, thin controllers, and clarity over cleverness.

Applies DHH style patterns including CRUD controllers, state-as-records instead of booleans, and Current attributes for defaults
Covers controllers, models, views, architecture, testing, and dependency decisions with specific naming conventions and code examples
Emphasizes vanilla Rails over gems: Minitest over RSpec, fixtures over factory_bot, Solid Queue over Sidekiq, database over Redis
Includes REST resource mapping patterns, concerns for horizontal behavior, authorization on User models, and Turbo/Stimulus for interactivity
SKILL.md

<essential_principles>

Core Philosophy

"The best code is the code you don't write. The second best is the code that's obviously correct."

Vanilla Rails is plenty:

Rich domain models over service objects
CRUD controllers over custom actions
Concerns for horizontal code sharing
Records as state instead of boolean columns
Database-backed everything (no Redis)
Build solutions before reaching for gems

What they deliberately avoid:

devise (custom ~150-line auth instead)
pundit/cancancan (simple role checks in models)
sidekiq (Solid Queue uses database)
redis (database for everything)
view_component (partials work fine)
GraphQL (REST with Turbo sufficient)
factory_bot (fixtures are simpler)
rspec (Minitest ships with Rails)
Tailwind (native CSS with layers)

Development Philosophy:

Ship, Validate, Refine - prototype-quality code to production to learn
Fix root causes, not symptoms
Write-time operations over read-time computations
Database constraints over ActiveRecord validations </essential_principles>
Controllers - REST mapping, concerns, Turbo responses, API patterns
Models - Concerns, state records, callbacks, scopes, POROs
Views & Frontend - Turbo, Stimulus, CSS, partials
Architecture - Routing, multi-tenancy, authentication, jobs, caching
Testing - Minitest, fixtures, integration tests
Gems & Dependencies - What to use vs avoid
Code Review - Review code against DHH style
General Guidance - Philosophy and conventions

Specify a number or describe your task.

Response	Reference to Read
1, controller	references/controllers.md
2, model	references/models.md
3, view, frontend, turbo, stimulus, css	references/frontend.md
4, architecture, routing, auth, job, cache	references/architecture.md
5, test, testing, minitest, fixture	references/testing.md
6, gem, dependency, library	references/gems.md
7, review	Read all references, then review code
8, general task	Read relevant references based on context

After reading relevant references, apply patterns to the user's code.

<quick_reference>

Naming Conventions

Verbs: card.close, card.gild, board.publish (not set_style methods)

Predicates: card.closed?, card.golden? (derived from presence of related record)

Concerns: Adjectives describing capability (Closeable, Publishable, Watchable)

Controllers: Nouns matching resources (Cards::ClosuresController)

Scopes:

chronologically, reverse_chronologically, alphabetically, latest
preloaded (standard eager loading name)
indexed_by, sorted_by (parameterized)
active, unassigned (business terms, not SQL-ish)
REST Mapping

Instead of custom actions, create new resources:

POST /cards/:id/close    → POST /cards/:id/closure
DELETE /cards/:id/close  → DELETE /cards/:id/closure
POST /cards/:id/archive  → POST /cards/:id/archival

Ruby Syntax Preferences
# Symbol arrays with spaces inside brackets
before_action :set_message, only: %i[ show edit update destroy ]

# Private method indentation
  private
    def set_message
      @message = Message.find(params[:id])
    end

# Expression-less case for conditionals
case
when params[:before].present?
  messages.page_before(params[:before])
else
  messages.last_page
end

# Bang methods for fail-fast
@message = Message.create!(params)

# Ternaries for simple conditionals
@room.direct? ? @room.users : @message.mentionees

Key Patterns

State as Records:

Card.joins(:closure)         # closed cards
Card.where.missing(:closure) # open cards


Current Attributes:

belongs_to :creator, default: -> { Current.user }


Authorization on Models:

class User < ApplicationRecord
  def can_administer?(message)
    message.creator == self || admin?
  end
end


</quick_reference>

<reference_index>

Domain Knowledge

All detailed patterns in references/:

File	Topics
references/controllers.md	REST mapping, concerns, Turbo responses, API patterns, HTTP caching
references/models.md	Concerns, state records, callbacks, scopes, POROs, authorization, broadcasting
references/frontend.md	Turbo Streams, Stimulus controllers, CSS layers, OKLCH colors, partials
references/architecture.md	Routing, authentication, jobs, Current attributes, caching, database patterns
references/testing.md	Minitest, fixtures, unit/integration/system tests, testing patterns
references/gems.md	What they use vs avoid, decision framework, Gemfile examples
</reference_index>	

<success_criteria> Code follows DHH style when:

Controllers map to CRUD verbs on resources
Models use concerns for horizontal behavior
State is tracked via records, not booleans
No unnecessary service objects or abstractions
Database-backed solutions preferred over external services
Tests use Minitest with fixtures
Turbo/Stimulus for interactivity (no heavy JS frameworks)
Native CSS with modern features (layers, OKLCH, nesting)
Authorization logic lives on User model
Jobs are shallow wrappers calling model methods </success_criteria>

Important Disclaimers:

LLM-generated guide - may contain inaccuracies
Code examples from Fizzy are licensed under the O'Saasy License
Not affiliated with or endorsed by 37signals
Weekly Installs
701
Repository
everyinc/compou…g-plugin
GitHub Stars
16.0K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass