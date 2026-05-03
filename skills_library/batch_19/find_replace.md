---
title: find-replace
url: https://skills.sh/0xdarkmatter/claude-mods/find-replace
---

# find-replace

skills/0xdarkmatter/claude-mods/find-replace
find-replace
Installation
$ npx skills add https://github.com/0xdarkmatter/claude-mods --skill find-replace
SKILL.md
Find Replace

Modern find-and-replace using sd.

sd Basics
# Replace in file (in-place)
sd 'oldText' 'newText' file.txt

# Replace in multiple files
sd 'oldText' 'newText' *.js

# Preview without changing (pipe)
cat file.txt | sd 'old' 'new'

sd vs sed
sed	sd
sed 's/old/new/g'	sd 'old' 'new'
sed -i 's/old/new/g'	sd 'old' 'new' file
sed 's#path/to#new/path#g'	sd 'path/to' 'new/path'

Key difference: sd is global by default, no delimiter issues.

Common Patterns
# Variable/function rename
sd 'oldName' 'newName' src/**/*.ts

# Word boundaries (avoid partial matches)
sd '\boldName\b' 'newName' src/**/*.ts

# Import path update
sd "from '../utils'" "from '@/utils'" src/**/*.ts

# Capture groups
sd 'console\.log\((.*)\)' 'logger.info($1)' src/**/*.js

Safe Batch Workflow
# 1. List affected files
rg -l 'oldPattern' src/

# 2. Preview replacements
rg 'oldPattern' -r 'newPattern' src/

# 3. Apply
sd 'oldPattern' 'newPattern' $(rg -l 'oldPattern' src/)

# 4. Verify
rg 'oldPattern' src/  # Should return nothing
git diff              # Review changes

Special Characters
Character	Escape
.	\.
*	\*
[ ]	\[ \]
$	\$
\	\\
Tips
Tip	Reason
Always preview with rg -r first	Avoid mistakes
Use git before bulk changes	Easy rollback
Use \b for word boundaries	Avoid partial matches
Quote patterns	Prevent shell interpretation
Additional Resources

For detailed patterns, load:

./references/advanced-patterns.md - Regex, batch workflows, real-world examples
Weekly Installs
45
Repository
0xdarkmatter/claude-mods
GitHub Stars
17
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass