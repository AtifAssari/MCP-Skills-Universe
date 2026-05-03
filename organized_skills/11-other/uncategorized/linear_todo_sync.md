---
rating: ⭐⭐⭐
title: linear todo sync
url: https://skills.sh/qdhenry/claude-command-suite/linear-todo-sync
---

# linear todo sync

skills/qdhenry/claude-command-suite/Linear Todo Sync
Linear Todo Sync
Installation
$ npx skills add https://github.com/qdhenry/claude-command-suite --skill 'Linear Todo Sync'
SKILL.md
Linear Todo Sync

Automatically fetch assigned Linear tasks and generate a comprehensive markdown todo list in your project root. This skill queries the Linear GraphQL API to retrieve all open tasks assigned to you, organizing them by project with full details including status, priority, labels, estimates, and due dates.

Setup
1. Install Required Packages

Install the Python dependencies:

pip install requests mdutils python-dotenv


Or using conda:

conda install requests python-dotenv
pip install mdutils

2. Obtain Linear API Key
Navigate to Linear API Settings
Click "Create new key" under Personal API Keys
Give it a descriptive name (e.g., "Claude Code Sync")
Copy the generated API key
3. Configure Environment

Create a .env file in your project root:

cp .claude/skills/linear-todo-sync/assets/.env.example .env


Edit .env and add your API key:

LINEAR_API_KEY=lin_api_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


Important: Ensure .env is in your .gitignore to protect your API key.

4. Verify Setup

Test the configuration by running:

python .claude/skills/linear-todo-sync/scripts/sync_linear_tasks.py


A markdown file named linear-todos-YYYY-MM-DD.md should appear in your project root.

How It Works

When triggered, this skill:

Loads credentials from the .env file in your project root
Queries Linear API using GraphQL to fetch all assigned issues in non-completed states
Retrieves task details including title, description, status, priority, labels, estimates, due dates, project, and URL
Groups tasks by project for better organization
Generates markdown file with filename linear-todos-YYYY-MM-DD.md in the project root
Outputs summary showing total tasks and project count

The generated markdown file provides a comprehensive view of your work with all relevant task metadata, making it easy to review priorities and plan your day.

Usage

Trigger this skill with phrases like:

"What do I need to work on this morning"
"Show me my work"
"Load work"
"Sync my Linear tasks"
"Get my todo list from Linear"

The skill will execute the sync script and create a dated markdown file in your project root.

Generated File Format

The markdown file follows this structure:

# Linear Tasks - January 18, 2025

Generated: 2025-01-18 09:30:45
Total Tasks: 12

## Project Alpha

### Implement user authentication (High)
- **Status**: In Progress
- **Labels**: backend, security
- **Estimate**: 5 points
- **Due**: 2025-01-20
- **Link**: https://linear.app/team/issue/PROJ-123

Add JWT-based authentication to the API endpoints...

### Fix login bug (Urgent)
- **Status**: Todo
- **Labels**: bug, frontend
- **Estimate**: 2 points
- **Due**: 2025-01-19
- **Link**: https://linear.app/team/issue/PROJ-124

Users cannot log in when using Safari...

## Project Beta

...

Customization

To modify the skill's behavior, edit scripts/sync_linear_tasks.py:

Change GraphQL Query

Modify the QUERY variable to fetch additional fields:

QUERY = """
query {
  viewer {
    assignedIssues(filter: { state: { type: { nin: ["completed", "canceled"] } } }) {
      nodes {
        id
        title
        description
        state { name }
        priority
        labels { nodes { name } }
        estimate
        dueDate
        project { name }
        url
        # Add more fields here
        createdAt
        updatedAt
        assignee { name }
      }
    }
  }
}
"""

Adjust Task Filtering

Modify the filter in the GraphQL query to change which tasks are fetched:

# Include completed tasks from the last week
filter: {
  state: { type: { nin: ["canceled"] } }
  completedAt: { gte: "2025-01-11" }
}

Modify Output Format

Customize the markdown generation in the generate_markdown() function to change structure, add sections, or include different metadata.

Change Output Location

Update the output_path variable in main():

# Save to a different directory
output_path = os.path.join(project_root, "docs", filename)

Troubleshooting
Error: "LINEAR_API_KEY not found in environment"

Cause: The .env file is missing or doesn't contain the API key.

Solution:

Verify .env exists in your project root (not in the skill directory)
Check that it contains: LINEAR_API_KEY=lin_api_...
Ensure no extra spaces around the = sign
Restart your terminal session if you just created the file
Error: "Authentication failed: Invalid API key"

Cause: The API key is incorrect or expired.

Solution:

Go to Linear API Settings
Verify your API key is still active
Generate a new key if needed
Update .env with the correct key
Error: "Network request failed"

Cause: Cannot connect to Linear API (network issue, timeout, or API downtime).

Solution:

Check your internet connection
Verify https://linear.app is accessible
Check Linear Status for outages
Try again in a few moments
Error: "Rate limit exceeded (429)"

Cause: Too many API requests in a short period.

Solution:

Wait 60 seconds before retrying
Avoid running the sync multiple times in quick succession
Linear's rate limit is 2000 requests per hour per API key
Warning: "No tasks found"

Cause: You have no assigned tasks in non-completed states.

Solution: This is informational only. The skill will still create a markdown file indicating zero tasks.

Error: "Permission denied when writing file"

Cause: Insufficient file system permissions.

Solution:

Check you have write permissions in the project directory
Verify the directory exists and is accessible
Try running with appropriate permissions
Script runs but no file appears

Cause: File created in unexpected location or script error.

Solution:

Check the script output for the exact file path
Look for error messages in the console
Run with verbose output: python scripts/sync_linear_tasks.py --verbose
Security Best Practices
Never commit .env file: Always add .env to .gitignore
Rotate API keys periodically: Generate new keys every 90 days
Use minimal permissions: Linear API keys inherit your user permissions
Keep packages updated: Run pip install --upgrade requests mdutils python-dotenv
Review generated files: Check markdown files before sharing to ensure no sensitive data
Advanced Usage
Automated Daily Sync

Add to your shell profile (.bashrc, .zshrc) to sync on terminal startup:

# Auto-sync Linear tasks daily
if [ -f "/path/to/project/.env" ]; then
  python /path/to/project/.claude/skills/linear-todo-sync/scripts/sync_linear_tasks.py
fi

Integration with Git Hooks

Create a post-checkout hook to sync after changing branches:

#!/bin/bash
# .git/hooks/post-checkout
python .claude/skills/linear-todo-sync/scripts/sync_linear_tasks.py

CI/CD Integration

Use in continuous integration to track team tasks:

# .github/workflows/sync-tasks.yml
- name: Sync Linear Tasks
  run: |
    pip install requests mdutils python-dotenv
    python .claude/skills/linear-todo-sync/scripts/sync_linear_tasks.py
  env:
    LINEAR_API_KEY: ${{ secrets.LINEAR_API_KEY }}

Additional Resources
Linear GraphQL API Documentation
Linear API Reference
Python Requests Documentation
MDUtils Documentation

For detailed API reference and advanced GraphQL queries, see the Linear API documentation.

Weekly Installs
–
Repository
qdhenry/claude-…nd-suite
GitHub Stars
1.2K
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass