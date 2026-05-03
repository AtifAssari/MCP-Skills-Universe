---
title: busybox-on-windows
url: https://skills.sh/sickn33/antigravity-awesome-skills/busybox-on-windows
---

# busybox-on-windows

skills/sickn33/antigravity-awesome-skills/busybox-on-windows
busybox-on-windows
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill busybox-on-windows
SKILL.md

BusyBox is a single binary that implements many common Unix tools.

Use this skill only on Windows. If you are on UNIX, then stop here.

Run the following steps only if you cannot find a busybox.exe file in the same directory as this document is. These are PowerShell commands, if you have a classic cmd.exe terminal, then you must use powershell -Command "..." to run them.

Print the type of CPU: Get-CimInstance -ClassName Win32_Processor | Select-Object Name, NumberOfCores, MaxClockSpeed
Print the OS versions: Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" | Select-Object ProductName, DisplayVersion, CurrentBuild
Download a suitable build of BusyBox by running one of these PowerShell commands:
32-bit x86 (ANSI): $ProgressPreference = 'SilentlyContinue'; Invoke-WebRequest -Uri https://frippery.org/files/busybox/busybox.exe -OutFile busybox.exe
64-bit x86 (ANSI): $ProgressPreference = 'SilentlyContinue'; Invoke-WebRequest -Uri https://frippery.org/files/busybox/busybox64.exe -OutFile busybox.exe
64-bit x86 (Unicode): $ProgressPreference = 'SilentlyContinue'; Invoke-WebRequest -Uri https://frippery.org/files/busybox/busybox64u.exe -OutFile busybox.exe
64-bit ARM (Unicode): $ProgressPreference = 'SilentlyContinue'; Invoke-WebRequest -Uri https://frippery.org/files/busybox/busybox64a.exe -OutFile busybox.exe

Useful commands:

Help: busybox.exe --list
Available UNIX commands: busybox.exe --list

Usage: Prefix the UNIX command with busybox.exe, for example: busybox.exe ls -1

If you need to run a UNIX command under another CWD, then use the absolute path to busybox.exe.

Documentation: https://frippery.org/busybox/ Original BusyBox: https://busybox.net/

When to Use

This skill is applicable to execute the workflow or actions described in the overview.

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
298
Repository
sickn33/antigra…e-skills
GitHub Stars
36.1K
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail