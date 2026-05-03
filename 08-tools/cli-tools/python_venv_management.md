---
title: python-venv-management
url: https://skills.sh/findinfinitelabs/chuuk/python-venv-management
---

# python-venv-management

skills/findinfinitelabs/chuuk/python-venv-management
python-venv-management
Installation
$ npx skills add https://github.com/findinfinitelabs/chuuk --skill python-venv-management
SKILL.md
Python Virtual Environment Management
Core Principle

ALWAYS use the project's .venv when running Python commands in the terminal. NEVER run Python commands without first activating or using the virtual environment.

Critical Rules
Check for .venv first - Always verify .venv exists before running Python commands
Use activation commands - Activate .venv in every terminal session
Shell-aware - Detect shell type (Bash, Zsh, PowerShell) and use appropriate commands
No global Python - Never use system Python when .venv exists
Fail fast - If .venv doesn't exist, create it or fail clearly
macOS default - Prefer Bash/Zsh patterns on macOS
Shell Detection & Commands
macOS Terminal (Zsh - Default)
# Activate .venv
source .venv/bin/activate

# Run Python commands
python app.py
pip install -r requirements.txt

# Check if activated
echo $VIRTUAL_ENV                 # Should show .venv path

# Direct execution (no activation needed)
.venv/bin/python app.py
.venv/bin/pip install package

macOS PowerShell
# Activate .venv
./.venv/bin/Activate.ps1

# Run Python commands
python -m <module>
pip install <package>

# Check if activated
$env:VIRTUAL_ENV                  # Should show .venv path

Linux Bash
# Activate .venv
source .venv/bin/activate

# Run Python commands
python app.py
pip install -r requirements.txt

# Check if activated
echo $VIRTUAL_ENV                 # Should show .venv path

Windows PowerShell
# Activate .venv
.\.venv\Scripts\Activate.ps1

# Run Python commands
python -m <module>
pip install <package>

# Check if activated
$env:VIRTUAL_ENV                  # Should show .venv path

Windows Command Prompt
# Activate .venv
.venv\Scripts\activate.bat

# Run Python commands
python app.py
pip install -r requirements.txt

Command Patterns
Pattern 1: Direct Execution (PREFERRED - No activation needed)
# macOS/Linux - Most reliable method
.venv/bin/python app.py
.venv/bin/python -m flask run
.venv/bin/pip install package

# PowerShell
./.venv/bin/python app.py
./.venv/bin/python -m flask run

Pattern 2: Activation + Command (macOS Zsh)
source .venv/bin/activate && python app.py

Pattern 3: Activation + Command (PowerShell)
./.venv/bin/Activate.ps1 ; python app.py

OS-Specific Paths
OS	Activation Script	Python Executable
macOS (Zsh)	.venv/bin/activate	.venv/bin/python
macOS (PowerShell)	.venv/bin/Activate.ps1	.venv/bin/python
Linux (Bash)	.venv/bin/activate	.venv/bin/python
Windows (PowerShell)	.venv\Scripts\Activate.ps1	.venv\Scripts\python.exe
Windows (CMD)	.venv\Scripts\activate.bat	.venv\Scripts\python.exe
Implementation Checklist

Before running ANY Python command, verify:

 Is this a Python project? (Check for .venv, requirements.txt, *.py files)
 Does .venv exist? (Check for .venv directory)
 What shell am I using? (PowerShell vs Bash/Zsh)
 Am I using the correct activation syntax?
 Can I use direct .venv/bin/python instead of activating?
Standard Workflows
Workflow 1: Running Python Scripts

PowerShell:

# Method 1: Activate then run
./.venv/bin/Activate.ps1 ; python app.py

# Method 2: Direct execution (PREFERRED)
./.venv/bin/python app.py


Bash:

# Method 1: Activate then run
source .venv/bin/activate && python app.py

# Method 2: Direct execution (PREFERRED)
.venv/bin/python app.py

Workflow 2: Installing Packages

PowerShell:

./.venv/bin/Activate.ps1 ; pip install <package>
# OR
./.venv/bin/python -m pip install <package>


Bash:

source .venv/bin/activate && pip install <package>
# OR
.venv/bin/python -m pip install <package>

Workflow 3: Running Flask/Django

PowerShell:

./.venv/bin/Activate.ps1 ; python app.py
# OR
./.venv/bin/python app.py


Bash:

source .venv/bin/activate && python app.py
# OR
.venv/bin/python app.py

Virtual Environment Setup
Check if .venv Exists
# PowerShell
Test-Path .venv

# Bash
test -d .venv && echo "exists" || echo "missing"

Create .venv if Missing
# PowerShell
python -m venv .venv

# Bash
python3 -m venv .venv

Verify Activation
# PowerShell - Should show .venv path
$env:VIRTUAL_ENV

# Bash - Should show .venv path
echo $VIRTUAL_ENV

Common Errors & Solutions
Error: "Activate.ps1 cannot be loaded"

Solution: Set PowerShell execution policy

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Error: "python: command not found"

Solution: Use python3 or direct .venv path

# Use python3
python3 -m venv .venv

# Or use .venv directly
./.venv/bin/python app.py

Error: "No module named 'flask'"

Solution: Ensure .venv is activated and packages installed

./.venv/bin/Activate.ps1 ; pip install -r requirements.txt

Best Practices
Always use .venv/bin/python directly - Most reliable method
Never assume system Python - Always check for .venv
Detect shell type - Use appropriate activation syntax
Fail gracefully - If .venv missing, create it first
Document requirements - Keep requirements.txt updated
Use python -m - More reliable than calling pip/flask directly
Terminal Command Template

Use this template for ALL Python-related terminal commands:

# Step 1: Detect shell
shell_type = "powershell" if on_windows or using_pwsh else "bash"

# Step 2: Check .venv exists
if not exists(".venv"):
    create_venv()

# Step 3: Build command with activation
if shell_type == "powershell":
    command = "./.venv/bin/Activate.ps1 ; <your_command>"
else:
    command = "source .venv/bin/activate && <your_command>"

# Step 4: Execute
run_in_terminal(command)

Quick Reference
Task	PowerShell	Bash
Activate	./.venv/bin/Activate.ps1	source .venv/bin/activate
Run Python	./.venv/bin/python app.py	.venv/bin/python app.py
Install package	./.venv/bin/pip install pkg	.venv/bin/pip install pkg
Check activation	$env:VIRTUAL_ENV	echo $VIRTUAL_ENV
Deactivate	deactivate	deactivate
Integration with Other Skills
git-workflow-management: Activate .venv before running git hooks with Python
code-documentation-standards: Ensure .venv active when generating docs
ai-training-data-generation: Activate .venv before training scripts
Example Commands
Starting Flask App
# PowerShell (PREFERRED)
./.venv/bin/python app.py

# Or with activation
./.venv/bin/Activate.ps1 ; python app.py

Installing Requirements
# PowerShell (PREFERRED)
./.venv/bin/python -m pip install -r requirements.txt

# Or with activation
./.venv/bin/Activate.ps1 ; pip install -r requirements.txt

Running Tests
# PowerShell (PREFERRED)
./.venv/bin/python -m pytest tests/

# Or with activation
./.venv/bin/Activate.ps1 ; pytest tests/

Multiple Commands
# PowerShell
./.venv/bin/Activate.ps1 ; pip install flask ; python app.py

# Bash
source .venv/bin/activate && pip install flask && python app.py

Validation

Before completing any Python task, verify:

✅ .venv exists in project root
✅ Correct shell syntax used (PowerShell vs Bash)
✅ Virtual environment activated in command
✅ No system Python used accidentally
✅ Command tested and working
Time Savings

Using this skill saves time by:

❌ No more "python: command not found" errors
❌ No more "No module named X" errors
❌ No more debugging which Python is running
✅ Consistent environment every time
✅ One command that always works
✅ No manual activation needed
Remember

The most important rule: If you're running Python code, you MUST use .venv. No exceptions.

Weekly Installs
13
Repository
findinfinitelabs/chuuk
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass