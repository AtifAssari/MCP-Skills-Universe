---
rating: ⭐⭐⭐
title: apple shortcuts integration
url: https://skills.sh/claude-office-skills/skills/apple-shortcuts-integration
---

# apple shortcuts integration

skills/claude-office-skills/skills/Apple Shortcuts Integration
Apple Shortcuts Integration
Installation
$ npx skills add https://github.com/claude-office-skills/skills --skill 'Apple Shortcuts Integration'
SKILL.md
Apple Shortcuts Integration

Integrate with Apple ecosystem for iOS and macOS automation.

Core Capabilities
Run Shortcuts
shortcut_execution:
  run:
    name: "Morning Routine"
    input: optional
    
  run_with_input:
    name: "Process Text"
    input: "{{text_to_process}}"
    
  run_with_clipboard:
    name: "Share to App"
    input: clipboard

Apple Reminders
reminders:
  create:
    title: "{{task}}"
    list: "Work"
    due_date: "{{date}}"
    due_time: "09:00"
    priority: high
    notes: "{{details}}"
    
  query:
    list: "Shopping"
    completed: false
    
  complete:
    reminder_id: "{{id}}"

Apple Notes
notes:
  create:
    title: "Meeting Notes - {{date}}"
    folder: "Work"
    body: |
      # {{meeting_title}}
      
      ## Attendees
      {{attendees}}
      
      ## Notes
      {{notes}}
      
  append:
    note_title: "Running Log"
    content: "- {{date}}: {{entry}}"
    
  search:
    query: "project alpha"
    folder: "Projects"

Calendar
calendar:
  create_event:
    title: "{{event_title}}"
    calendar: "Work"
    start: "{{start_time}}"
    end: "{{end_time}}"
    location: "{{location}}"
    notes: "{{notes}}"
    alerts:
      - 30  # minutes before
      
  query:
    calendar: "all"
    start: today
    end: "+7 days"

Shortcut Examples
Daily Log
shortcut_daily_log:
  steps:
    - get_current_date
    - prompt_for_input:
        message: "How was your day?"
    - append_to_note:
        title: "Daily Journal"
        content: |
          ## {{date}}
          {{input}}
    - create_reminder:
        title: "Journal entry"
        due: tomorrow 9am

Quick Capture
shortcut_quick_capture:
  trigger: share_sheet
  steps:
    - get_shared_input
    - create_note:
        title: "Captured - {{date}}"
        body: "{{input}}"
    - notify: "Captured successfully"

Integration Workflows
Cross-Platform Sync
sync_workflow:
  trigger: note_created
  actions:
    - if: tag == "work"
      then:
        - sync_to: notion
        - sync_to: obsidian
    - if: has_task
      then:
        - create_reminder: from_task

Best Practices
Naming: Clear, descriptive shortcut names
Input Handling: Validate inputs
Error Handling: Graceful failures
Privacy: Minimize data exposure
Testing: Test on all devices
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
SnykPass