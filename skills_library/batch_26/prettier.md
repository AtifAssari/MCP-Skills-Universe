---
title: prettier
url: https://skills.sh/avvale/aurora-front/prettier
---

# prettier

skills/avvale/aurora-front/prettier
prettier
Installation
$ npx skills add https://github.com/avvale/aurora-front --skill prettier
SKILL.md
When to Use

Use this skill when:

After creating or modifying ANY TypeScript file
After generating code with Aurora CLI
Before creating a git commit
When fixing code style inconsistencies
After implementing handlers, services, guards, interceptors
After writing tests

CRITICAL: Format code IMMEDIATELY after editing, not at the end of session

Critical Patterns
⚠️ MANDATORY: Format After Every Edit

Rule: Format IMMEDIATELY after modifying each file

# After editing/creating a single file
npm run format -- path/to/file.ts

# After modifying multiple files
npm run format -- path/to/file1.ts path/to/file2.ts

# Format entire directory
npm run format -- src/@app/tesla/model/**/*.ts


Workflow:

✅ Read/edit file
✅ IMMEDIATELY run prettier on that file
✅ Verify no formatting errors
✅ Move to next file

❌ NEVER:

Skip formatting
Format "later" or "at the end"
Leave unformatted code
Ignore prettier errors
Commands
Format Single File
npm run format -- <file-path>

# Example
npm run format -- src/@app/tesla/model/application/create/tesla-create-model.handler.ts

Format Multiple Files
npm run format -- <file1> <file2> <file3>

# Example
npm run format -- src/@app/tesla/model/application/create/*.ts

Format Specific Directory
npm run format -- <directory>/**/*.ts

# Example - Format all TypeScript files in module
npm run format -- src/@app/tesla/model/**/*.ts

Check Formatting (Without Writing)
npm run format:check -- <file-path>

# Useful for CI/CD or verification
npm run format:check -- src/@app/tesla/model/**/*.ts

Usage Patterns
Pattern 1: After Editing Handler
// 1. Edit the file
/* #region AI-generated code */
async execute(command: CreateTeslaModelCommand): Promise<void> {
    if (command.payload.price <= 0) {
        throw new InvalidPriceException();
    }
    await this.service.main(command.payload, command.cQMetadata);
}
/* #endregion */

// 2. IMMEDIATELY format
npm run format -- src/@app/tesla/model/application/create/tesla-create-model.handler.ts

Pattern 2: After Creating New File
# 1. Create exception file
# 2. Write content
# 3. IMMEDIATELY format
npm run format -- src/@app/tesla/model/domain/exceptions/tesla-invalid-price.exception.ts

Pattern 3: After Aurora CLI Regeneration
# 1. Regenerate module
aurora load back module -n=tesla/model -t

# 2. Format ALL generated files
npm run format -- src/@app/tesla/model/**/*.ts
npm run format -- src/@api/tesla/model/**/*.ts

Pattern 4: Before Git Commit
# 1. Check which files were modified
git status

# 2. Format all modified files
npm run format -- src/@app/tesla/model/application/create/tesla-create-model.handler.ts \
                  src/@app/tesla/model/domain/exceptions/tesla-invalid-price.exception.ts

# 3. Verify formatting succeeded
# 4. Create commit
git add .
git commit -m "feat(tesla/model): add price validation"

Integration with Other Skills
From aurora-development

After implementing business logic:

1. Edit handler/service/guard
2. Use **prettier** skill to format immediately
3. Continue to next file

From aurora-cli

After regenerating code:

1. Run aurora load command
2. Use **prettier** skill to format all generated files
3. Verify no errors

From jest-nestjs

After writing tests:

1. Write test file
2. Use **prettier** skill to format test file
3. Run tests

From conventional-commits

Before creating commit:

1. Format all modified files with **prettier** skill
2. Verify git diff shows only logical changes (not formatting)
3. Create conventional commit

Configuration

Prettier configuration is in project root:

# Configuration file (check this for project rules)
.prettierrc

# Ignore patterns
.prettierignore


Common Aurora/NestJS Configuration:

{
  "singleQuote": true,
  "trailingComma": "all",
  "tabWidth": 4,
  "semi": true,
  "printWidth": 120,
  "arrowParens": "avoid"
}


DO NOT modify prettier config without team approval.

Troubleshooting
Error: "No files matching pattern"
# Check file path is correct
ls -la src/@app/tesla/model/application/create/

# Use absolute path if needed
npm run format -- $(pwd)/src/@app/tesla/model/application/create/tesla-create-model.handler.ts

Error: "Parsing error"
# File has syntax errors - fix them first
# Check for:
# - Missing closing braces
# - Missing semicolons
# - Incomplete statements

Pre-commit Hook Fails
# Format all staged files
npm run format -- $(git diff --cached --name-only --diff-filter=ACM | grep '\.ts$')

# Or format all modified files
npm run format -- $(git diff --name-only --diff-filter=ACM | grep '\.ts$')

Quick Reference
When	Command
After editing file	npm run format -- <file>
Multiple files	npm run format -- <file1> <file2>
Entire directory	npm run format -- <dir>/**/*.ts
Check only	npm run format:check -- <file>
Before commit	Format all modified files
Best Practices
✅ DO
Format immediately after editing
Format one file at a time during development
Verify formatting succeeded (no errors)
Check git diff after formatting (should show only logical changes)
Include formatted files in commits
Run format:check in CI/CD
❌ DON'T
Wait until end of session to format
Skip formatting "unimportant" files
Ignore prettier errors
Modify .prettierrc without approval
Commit unformatted code
Disable prettier in IDE
Editor Integration (Optional but Recommended)
VS Code
// .vscode/settings.json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  }
}

Benefits:
✅ Automatic formatting on save
✅ Less manual npm commands
✅ Consistent style while coding
✅ Faster workflow

Still run npm run format to be sure!

Remember
🚨 Format IMMEDIATELY after editing each file
🚨 Never skip formatting
🚨 Verify formatting succeeded
✅ Formatting is part of the coding process, not an afterthought
✅ Consistent formatting = fewer merge conflicts
✅ Pre-commit hooks will enforce formatting

Integration:

Other skills reference this skill for formatting
This skill is invoked AFTER file modifications
This skill is invoked BEFORE git commits
Weekly Installs
14
Repository
avvale/aurora-front
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass