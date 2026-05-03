---
rating: ⭐⭐⭐
title: mac-wash
url: https://skills.sh/wghust/stark-skills/mac-wash
---

# mac-wash

skills/wghust/stark-skills/mac-wash
mac-wash
Installation
$ npx skills add https://github.com/wghust/stark-skills --skill mac-wash
SKILL.md
mac-wash Skill

Language: Respond in the same language as the user (中文提问则中文回答).

Zero-dependency macOS performance diagnosis and cleanup skill. Identifies bottlenecks, presents interactive cleanup options, and executes safe optimization scripts.

Execution Flow
Step 0 · Detect Language

Detect user's language from input and use it for all output.

Step 1 · System Diagnosis (Read-Only)

Run diagnostic commands in parallel to assess system state. All commands are read-only and safe.

1A · Disk Space Analysis
# User caches
du -sh ~/Library/Caches 2>/dev/null

# System logs
du -sh ~/Library/Logs 2>/dev/null

# Trash
du -sh ~/.Trash 2>/dev/null

# Browser caches
du -sh ~/Library/Caches/Google/Chrome 2>/dev/null
du -sh ~/Library/Caches/com.apple.Safari 2>/dev/null
du -sh ~/Library/Caches/Firefox 2>/dev/null

# Xcode derived data (if exists)
du -sh ~/Library/Developer/Xcode/DerivedData 2>/dev/null

# npm cache (if exists)
du -sh ~/.npm 2>/dev/null

# yarn cache (if exists)
du -sh ~/Library/Caches/Yarn 2>/dev/null

1B · Memory Pressure
# Memory stats
vm_stat | grep -E "Pages (free|active|inactive|speculative|wired down)"

# Swap usage
sysctl vm.swapusage


Parse output to calculate:

Total memory used
Free memory
Swap used (if >1GB, flag as moderate/high pressure)
1C · Process Monitoring
# Top 10 processes by memory
ps -A -o %mem,rss,comm | sort -nr | head -10

# Top 10 processes by CPU
ps -A -o %cpu,comm | sort -nr | head -10

1D · Large Files (Optional)
# Find files >1GB (limit to 10 results)
mdfind "kMDItemFSSize > 1000000000" 2>/dev/null | head -10 | xargs -I {} du -sh {}


Skip if mdfind fails or takes >5 seconds.

Step 2 · Present Findings

Format diagnosis results in structured output:

English format:

## macOS Performance Analysis

### Disk Space Opportunities
- User caches: X.X GB (~/Library/Caches)
- System logs: X.X GB (~/Library/Logs)
- Browser caches: X.X GB
- Xcode derived data: X.X GB (if exists)
- npm/yarn cache: X.X GB (if exists)
- Trash: X.X GB

**Total reclaimable: ~XX GB**

### Memory Status
- Used: X.X GB / Total: XX GB
- Swap: X.X GB (pressure level: low/moderate/high)

### Top Resource Consumers
1. ProcessName: X.X GB RAM, XX% CPU
2. ProcessName: X.X GB RAM, XX% CPU
...


Chinese format:

## macOS 性能分析

### 磁盘空间清理机会
- 用户缓存: X.X GB (~/Library/Caches)
- 系统日志: X.X GB (~/Library/Logs)
- 浏览器缓存: X.X GB
- Xcode 派生数据: X.X GB (如存在)
- npm/yarn 缓存: X.X GB (如存在)
- 废纸篓: X.X GB

**可回收总计: ~XX GB**

### 内存状态
- 已用: X.X GB / 总计: XX GB
- 交换空间: X.X GB (压力等级: 低/中/高)

### 资源占用 Top 进程
1. 进程名: X.X GB 内存, XX% CPU
2. 进程名: X.X GB 内存, XX% CPU
...

Step 3 · Interactive Cleanup Selection

Use AskUserQuestion tool to present cleanup options:

Options (include only categories with >100MB):

User Caches (X.X GB) - Safe, regenerates automatically
System Logs (X.X GB) - Safe, system recreates as needed
Browser Caches (X.X GB) - Safe, browsers will rebuild
Xcode Derived Data (X.X GB) - Safe, Xcode rebuilds on next use
npm/yarn Cache (X.X GB) - Safe, reinstalls on next use
Empty Trash (X.X GB) - Permanent deletion

Question format:

English: "Which cleanup actions would you like to perform?"
Chinese: "您想执行哪些清理操作？"

Set multiSelect: true to allow multiple selections.

Step 4 · Dry-Run Preview

For selected cleanup actions, show what will be removed:

# Example for user caches
ls -lh ~/Library/Caches | head -20


Ask for final confirmation:

English: "Proceed with cleanup? This will remove the files listed above."
Chinese: "继续清理？这将删除上面列出的文件。"
Step 5 · Execute Cleanup

Execute cleanup using pre-written scripts from skills/mac-wash/scripts/:

# User Caches
bash skills/mac-wash/scripts/clean-user-caches.sh

# System Logs
bash skills/mac-wash/scripts/clean-system-logs.sh

# Browser Caches
bash skills/mac-wash/scripts/clean-browser-caches.sh

# Xcode Derived Data
bash skills/mac-wash/scripts/clean-xcode.sh

# npm/yarn Cache
bash skills/mac-wash/scripts/clean-npm-yarn.sh

# Empty Trash
bash skills/mac-wash/scripts/clean-trash.sh


Interactive cleanup (user selects multiple options):

bash skills/mac-wash/scripts/clean-all.sh


Scripts automatically report space reclaimed and handle errors gracefully.

Step 6 · Summary

Report total space reclaimed and suggest next steps if memory pressure is high:

English:

## Cleanup Complete

**Total space reclaimed: XX.X GB**

### Recommendations
- Restart your Mac to clear memory caches
- Close unused applications to reduce memory pressure
- Consider upgrading RAM if swap usage remains high


Chinese:

## 清理完成

**总计回收空间: XX.X GB**

### 建议
- 重启 Mac 以清除内存缓存
- 关闭未使用的应用以降低内存压力
- 如交换空间使用仍然很高，考虑升级内存

Safety Guarantees
Read-only diagnosis: All diagnostic commands are non-destructive
User confirmation required: No cleanup executes without explicit approval
Protected directories: Never touches ~/Documents, ~/Desktop, ~/Pictures, ~/Music, ~/Movies
Reversible operations: All cleaned items are caches that regenerate automatically
No sudo required: All operations run in user space
Error Handling
Error	Action
Permission denied	Skip that cleanup, note in summary
Command not found	Skip that diagnostic, continue with others
Directory doesn't exist	Skip silently (e.g., Xcode not installed)
Cleanup fails	Log error, continue with remaining cleanups
Examples
Example A — User requests performance check

Input (English): "My Mac is slow, can you help optimize it?"

Actions:

Run all diagnostic commands
Present findings with disk space opportunities
Offer cleanup options via AskUserQuestion
Execute selected cleanups with confirmation
Example B — User requests cleanup (Chinese)

Input (Chinese): "我的电脑很卡，帮我清理一下"

Actions:

运行所有诊断命令
用中文展示发现的问题和磁盘空间清理机会
通过 AskUserQuestion 提供清理选项
确认后执行选定的清理操作
Weekly Installs
12
Repository
wghust/stark-skills
GitHub Stars
4
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass