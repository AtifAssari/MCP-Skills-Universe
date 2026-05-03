---
title: powershell-windows
url: https://skills.sh/sickn33/antigravity-awesome-skills/powershell-windows
---

# powershell-windows

skills/sickn33/antigravity-awesome-skills/powershell-windows
powershell-windows
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill powershell-windows
Summary

Essential syntax rules and pitfalls for Windows PowerShell scripting.

Parentheses required around all cmdlet calls when using logical operators (-or, -and); missing them causes parsing errors
Unicode and emoji characters prohibited in scripts; use ASCII-only alternatives like [OK], [!], [WARN] for status indicators
Null checks mandatory before property access; always validate objects exist before calling methods or accessing properties
JSON operations require explicit -Depth parameter to serialize nested objects correctly
Error handling via $ErrorActionPreference and try/catch patterns; avoid returning inside try blocks and use finally for cleanup
SKILL.md
PowerShell Windows Patterns

Critical patterns and pitfalls for Windows PowerShell.

1. Operator Syntax Rules
CRITICAL: Parentheses Required
❌ Wrong	✅ Correct
if (Test-Path "a" -or Test-Path "b")	if ((Test-Path "a") -or (Test-Path "b"))
if (Get-Item $x -and $y -eq 5)	if ((Get-Item $x) -and ($y -eq 5))

Rule: Each cmdlet call MUST be in parentheses when using logical operators.

2. Unicode/Emoji Restriction
CRITICAL: No Unicode in Scripts
Purpose	❌ Don't Use	✅ Use
Success	✅ ✓	[OK] [+]
Error	❌ ✗ 🔴	[!] [X]
Warning	⚠️ 🟡	[*] [WARN]
Info	ℹ️ 🔵	[i] [INFO]
Progress	⏳	[...]

Rule: Use ASCII characters only in PowerShell scripts.

3. Null Check Patterns
Always Check Before Access
❌ Wrong	✅ Correct
$array.Count -gt 0	$array -and $array.Count -gt 0
$text.Length	if ($text) { $text.Length }
4. String Interpolation
Complex Expressions
❌ Wrong	✅ Correct
"Value: $($obj.prop.sub)"	Store in variable first

Pattern:

$value = $obj.prop.sub
Write-Output "Value: $value"

5. Error Handling
ErrorActionPreference
Value	Use
Stop	Development (fail fast)
Continue	Production scripts
SilentlyContinue	When errors expected
Try/Catch Pattern
Don't return inside try block
Use finally for cleanup
Return after try/catch
6. File Paths
Windows Path Rules
Pattern	Use
Literal path	C:\Users\User\file.txt
Variable path	Join-Path $env:USERPROFILE "file.txt"
Relative	Join-Path $ScriptDir "data"

Rule: Use Join-Path for cross-platform safety.

7. Array Operations
Correct Patterns
Operation	Syntax
Empty array	$array = @()
Add item	$array += $item
ArrayList add	`$list.Add($item)
8. JSON Operations
CRITICAL: Depth Parameter
❌ Wrong	✅ Correct
ConvertTo-Json	ConvertTo-Json -Depth 10

Rule: Always specify -Depth for nested objects.

File Operations
Operation	Pattern
Read	`Get-Content "file.json" -Raw
Write	`$data
9. Common Errors
Error Message	Cause	Fix
"parameter 'or'"	Missing parentheses	Wrap cmdlets in ()
"Unexpected token"	Unicode character	Use ASCII only
"Cannot find property"	Null object	Check null first
"Cannot convert"	Type mismatch	Use .ToString()
10. Script Template
# Strict mode
Set-StrictMode -Version Latest
$ErrorActionPreference = "Continue"

# Paths
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Main
try {
    # Logic here
    Write-Output "[OK] Done"
    exit 0
}
catch {
    Write-Warning "Error: $_"
    exit 1
}


Remember: PowerShell has unique syntax rules. Parentheses, ASCII-only, and null checks are non-negotiable.

When to Use

This skill is applicable to execute the workflow or actions described in the overview.

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
1.5K
Repository
sickn33/antigra…e-skills
GitHub Stars
36.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass