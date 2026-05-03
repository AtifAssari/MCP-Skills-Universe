---
title: blueprint-gem
url: https://skills.sh/faqndo97/ai-skills/blueprint-gem
---

# blueprint-gem

skills/faqndo97/ai-skills/blueprint-gem
blueprint-gem
Installation
$ npx skills add https://github.com/faqndo97/ai-skills --skill blueprint-gem
SKILL.md

<essential_principles>

# Good - concise
fields :id, :name, :email, :created_at

# Only use singular when needed
field :full_name do |user|
  "#{user.first_name} #{user.last_name}"
end


</essential_principles>

<quick_reference>

fields :email, :name, :created_at end

Usage

UserBlueprint.render(user) # JSON string UserBlueprint.render_as_hash(user) # Ruby Hash

</pattern>

<pattern name="computed-field">
```ruby
field :full_name do |user|
  "#{user.first_name} #{user.last_name}"
end

# With options access
field :display_name do |user, options|
  options[:admin] ? user.admin_name : user.public_name
end

Usage

UserBlueprint.render(user, view: :extended)

</pattern>

<pattern name="conditional-field">
```ruby
field :salary, if: ->(field_name, user, options) { options[:show_salary] }
field :age, unless: ->(field_name, user, options) { user.hide_age? }


</quick_reference>

Create a new blueprint
Understand a specific concept (views, associations, transformers, etc.)
Debug a blueprint issue
Something else

For option 2, specify the concept and I'll load the relevant reference.

After reading, apply the knowledge to the user's specific situation.

<reference_index>

Core Concepts:

fields-and-identifiers.md - Fields, identifiers, computed fields, field options
views.md - Views, include/exclude, view inheritance
associations.md - Nested blueprints, polymorphic associations

Advanced:

configuration.md - Global config, JSON generators, field sorting
transformers-and-extractors.md - Custom transformers and extractors
conditionals-and-defaults.md - Conditional fields, defaults, nil handling

Troubleshooting:

anti-patterns.md - Common mistakes and how to fix them

</reference_index>

<workflows_index>

Workflow	Purpose
create-blueprint.md	Create a new blueprint with proper structure
</workflows_index>	
Weekly Installs
11
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