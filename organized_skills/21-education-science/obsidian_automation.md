---
title: obsidian automation
url: https://skills.sh/claude-office-skills/skills/obsidian-automation
---

# obsidian automation

skills/claude-office-skills/skills/Obsidian Automation
Obsidian Automation
Installation
$ npx skills add https://github.com/claude-office-skills/skills --skill 'Obsidian Automation'
SKILL.md
Obsidian Automation

Automate Obsidian knowledge management and personal knowledge base workflows.

Core Capabilities
Note Creation
note_templates:
  daily_note:
    filename: "{{date:YYYY-MM-DD}}"
    folder: "Daily Notes"
    template: |
      # {{date:dddd, MMMM D, YYYY}}
      
      ## Morning Intentions
      - [ ] 
      
      ## Tasks
      - [ ] 
      
      ## Notes
      
      ## Evening Reflection
      
      ---
      [[{{date:YYYY-MM-DD|-1d}}|← Yesterday]] | [[{{date:YYYY-MM-DD|+1d}}|Tomorrow →]]

  meeting_note:
    filename: "Meeting - {{title}} - {{date}}"
    folder: "Meetings"
    template: |
      ---
      date: {{date}}
      attendees: {{attendees}}
      tags: meeting
      ---
      
      # {{title}}
      
      ## Agenda
      
      ## Notes
      
      ## Action Items
      - [ ] 
      
      ## Follow-ups
      
      [[Meetings MOC]]

Smart Linking
auto_linking:
  rules:
    - pattern: "[[Person/{{name}}]]"
      trigger: "@{{name}}"
      create_if_missing: true
      
    - pattern: "[[Project/{{project}}]]"
      trigger: "#proj/{{project}}"
      
  backlink_suggestions:
    enabled: true
    min_mentions: 2
    
  alias_support:
    - "[[Machine Learning|ML]]"
    - "[[Artificial Intelligence|AI]]"

Dataview Queries
dataview_examples:
  tasks_due_today:
    query: |
      ```dataview
      TASK
      WHERE !completed AND due = date(today)
      SORT due ASC
      ```
      
  recent_meetings:
    query: |
      ```dataview
      TABLE date, attendees
      FROM "Meetings"
      WHERE date >= date(today) - dur(7 days)
      SORT date DESC
      LIMIT 10
      ```
      
  project_dashboard:
    query: |
      ```dataview
      TABLE status, due, priority
      FROM #project
      WHERE status != "completed"
      SORT priority ASC
      ```

Templates
templates:
  zettelkasten:
    filename: "{{date:YYYYMMDDHHmmss}}"
    content: |
      ---
      id: {{date:YYYYMMDDHHmmss}}
      tags: 
      links: 
      ---
      
      # {{title}}
      
      ## Idea
      
      ## Source
      
      ## Connections
      - Related to: 
      
      ## References
      
  book_note:
    filename: "Book - {{title}}"
    content: |
      ---
      author: {{author}}
      finished: 
      rating: 
      tags: book
      ---
      
      # {{title}}
      by {{author}}
      
      ## Summary
      
      ## Key Ideas
      
      ## Highlights
      
      ## My Thoughts
      
      ## Action Items

Workflow Automations
Web Clipper
web_clipper:
  trigger: browser_extension
  actions:
    - extract_content:
        title: "{{page.title}}"
        url: "{{page.url}}"
        content: "{{selection}}"
    - create_note:
        folder: "Clippings"
        template: web_clip
    - add_tags: ["web-clip", "{{domain}}"]

Research Workflow
research_workflow:
  steps:
    - create_topic_note:
        filename: "Research - {{topic}}"
        folder: "Research"
    - gather_sources:
        search: "{{topic}}"
        link_to_note: true
    - generate_questions:
        based_on: sources
    - create_sub_notes:
        for_each: key_concept

Graph Analysis
graph_insights:
  orphan_notes:
    query: "notes without incoming links"
    action: suggest_connections
    
  clusters:
    identify: true
    visualize: true
    
  link_suggestions:
    based_on: content_similarity
    threshold: 0.7

Best Practices
Atomic Notes: One idea per note
Consistent Naming: Use conventions
Link Liberally: Connect related ideas
Daily Practice: Regular review
Templates: Standardize note types
Tags vs Links: Use both strategically
Weekly Installs
–
Repository
claude-office-s…s/skills
GitHub Stars
94
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn