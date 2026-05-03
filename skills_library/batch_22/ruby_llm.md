---
title: ruby-llm
url: https://skills.sh/faqndo97/ai-skills/ruby-llm
---

# ruby-llm

skills/faqndo97/ai-skills/ruby-llm
ruby-llm
Installation
$ npx skills add https://github.com/faqndo97/ai-skills --skill ruby-llm
SKILL.md

<essential_principles>

How RubyLLM Works

RubyLLM provides one beautiful Ruby API for all LLM providers. Same interface whether using GPT, Claude, Gemini, or local Ollama models.

1. One API for Everything
# Chat with any provider - same interface
chat = RubyLLM.chat(model: 'gpt-4.1')
chat = RubyLLM.chat(model: 'claude-sonnet-4-5')
chat = RubyLLM.chat(model: 'gemini-2.0-flash')

# All return the same RubyLLM::Message object
response = chat.ask("Hello!")
puts response.content

2. Configuration First

Always configure API keys before use:

# config/initializers/ruby_llm.rb
RubyLLM.configure do |config|
  config.openai_api_key = ENV['OPENAI_API_KEY']
  config.anthropic_api_key = ENV['ANTHROPIC_API_KEY']
  config.gemini_api_key = ENV['GEMINI_API_KEY']
  config.request_timeout = 120
  config.max_retries = 3
end

3. Tools Are Ruby Classes

Define tools as RubyLLM::Tool subclasses with description, param, and execute:

class Weather < RubyLLM::Tool
  description "Get current weather for a location"
  param :latitude, type: 'number', desc: "Latitude"
  param :longitude, type: 'number', desc: "Longitude"

  def execute(latitude:, longitude:)
    # Return structured data, not exceptions
    { temperature: 22, conditions: "Sunny" }
  rescue => e
    { error: e.message }  # Let LLM handle errors gracefully
  end
end

chat.with_tool(Weather).ask("What's the weather in Berlin?")

4. Rails Integration with acts_as_chat

Persist conversations automatically:

class Chat < ApplicationRecord
  acts_as_chat
end

chat = Chat.create!(model: 'gpt-4.1')
chat.ask("Hello!")  # Automatically persists messages

5. Streaming with Blocks

Real-time responses via blocks:

chat.ask("Tell me a story") do |chunk|
  print chunk.content  # Print as it arrives
end


</essential_principles>

Build a new AI feature (chat, embeddings, image generation)
Add Rails chat integration (acts_as_chat, Turbo Streams)
Implement tools/function calling
Add streaming responses
Debug an LLM interaction
Optimize for production
Something else

Wait for response, then read the matching workflow.

After reading the workflow, follow it exactly.

<verification_loop>

After Every Change
# 1. Does it load?
bin/rails console -e test
> RubyLLM.chat.ask("Test")

# 2. Do tests pass?
bin/rails test test/models/chat_test.rb

# 3. Check for errors
bin/rails test 2>&1 | grep -E "(Error|Fail|exception)"


Report to user:

"Config: API keys loaded"
"Chat: Working with [model]"
"Tests: X pass, Y fail" </verification_loop>

<reference_index>

Domain Knowledge

All in references/:

Getting Started: getting-started.md Core Features: chat-api.md, tools.md, streaming.md, structured-output.md Rails: rails-integration.md Capabilities: embeddings.md, image-audio.md Infrastructure: providers.md, error-handling.md, mcp-integration.md Quality: anti-patterns.md </reference_index>

<workflows_index>

Workflows

All in workflows/:

File	Purpose
build-new-feature.md	Create new AI feature from scratch
add-rails-chat.md	Add persistent chat to Rails app
implement-tools.md	Create custom tools/function calling
add-streaming.md	Add real-time streaming responses
debug-llm.md	Find and fix LLM issues
optimize-performance.md	Production optimization
</workflows_index>	
Weekly Installs
19
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