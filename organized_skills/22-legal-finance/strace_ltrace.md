---
rating: ⭐⭐⭐
title: strace-ltrace
url: https://skills.sh/mohitmishra786/low-level-dev-skills/strace-ltrace
---

# strace-ltrace

skills/mohitmishra786/low-level-dev-skills/strace-ltrace
strace-ltrace
Installation
$ npx skills add https://github.com/mohitmishra786/low-level-dev-skills --skill strace-ltrace
SKILL.md
strace / ltrace
Purpose

Guide agents through tracing system calls with strace and library calls with ltrace — the most effective tools for diagnosing incorrect binary behaviour without a crash or debugger.

Triggers
"My program behaves incorrectly — how do I trace what it's doing?"
"How do I find what files a binary is opening?"
"strace shows ENOENT — how do I interpret it?"
"How do I trace network calls with strace?"
"What is ltrace and how does it differ from strace?"
"How do I trace a running process?"
Workflow
1. Basic strace usage
# Trace all syscalls of a command
strace ./myapp arg1 arg2

# Attach to running process
strace -p 12345

# Trace child processes too (-f = follow fork)
strace -f ./myapp

# Save to file (raw output — not stdout)
strace ./myapp 2> trace.txt

# Most useful: timestamps + summary
strace -t -f ./myapp 2>&1 | head -100

2. Filter by syscall category
# Trace file operations only
strace -e trace=file ./myapp

# Trace network syscalls
strace -e trace=network ./myapp

# Trace specific syscalls
strace -e trace=open,openat,read,write ./myapp

# Trace process management
strace -e trace=process ./myapp

# Trace memory operations
strace -e trace=memory ./myapp

# Trace signals
strace -e trace=signal ./myapp

# Multiple categories
strace -e trace=file,network ./myapp

Category	Syscalls included
file	open, openat, stat, access, unlink, rename, ...
network	socket, connect, bind, accept, send, recv, ...
process	fork, exec, wait, clone, exit, ...
memory	mmap, munmap, mprotect, brk, ...
signal	kill, sigaction, sigprocmask, ...
ipc	pipe, socket pair, shmget, ...
desc	close, dup, poll, select, epoll, ...
3. Interpreting common errors
# See return values and errors
strace -e trace=file ./myapp 2>&1 | grep -E "ENOENT|EPERM|EACCES|ENOTSUP"

Error	Meaning	Common cause
ENOENT	No such file or directory	Config file missing, wrong path
EACCES	Permission denied	File permissions, SELinux
EPERM	Operation not permitted	Missing capability, suid needed
EADDRINUSE	Address already in use	Port already bound
ETIMEDOUT	Connection timed out	Network unreachable, firewall
ECONNREFUSED	Connection refused	Server not listening
EAGAIN	Resource temporarily unavailable	Non-blocking I/O, try again
ENOMEM	Out of memory	Allocation failed
EBADF	Bad file descriptor	Using closed/invalid fd
ENOEXEC	Exec format error	Wrong binary format for arch
# Find what file is not found
strace ./myapp 2>&1 | grep 'ENOENT'
# Example output:
# openat(AT_FDCWD, "/etc/myapp.conf", O_RDONLY) = -1 ENOENT (No such file or directory)
# → Config file expected at /etc/myapp.conf

4. Useful strace flags
# Show strings fully (default truncates at 32 chars)
strace -s 256 ./myapp

# Timestamps
strace -t ./myapp     # wall clock time
strace -T ./myapp     # time spent in each syscall
strace -r ./myapp     # relative timestamps

# System call count summary
strace -c ./myapp
# Shows count, time, errors per syscall — great for profiling

# Trace with PIDs in output (for -f)
strace -f -p ./myapp
# Output: [pid 12346] open("/etc/passwd", O_RDONLY) = 3

# Decode numerical arguments
strace -e verbose=all ./myapp

# Print instruction pointer at each syscall
strace -i ./myapp

5. ltrace — library call tracing
# Trace all library calls
ltrace ./myapp

# Trace specific library function
ltrace -e malloc,free,fopen ./myapp

# Trace nested calls (lib → lib)
ltrace -n 2 ./myapp   # indent nested calls

# Trace with syscalls too
ltrace -S ./myapp

# Attach to running process
ltrace -p 12345

# Summary statistics
ltrace -c ./myapp


Typical ltrace output:

malloc(1024) = 0x55a1b2c3d000
fopen("/etc/myapp.conf", "r") = 0
free(0x55a1b2c3d000) = <void>


strace vs ltrace:

	strace	ltrace
Traces	Kernel syscalls	User-space library calls
Overhead	Lower	Higher (PLT hooking)
Shows	open(), read(), write()	fopen(), malloc(), printf()
Use when	Binary interacts with OS/files/network	Binary calls library functions you can't see
6. Practical diagnosis workflows
# Find missing config file
strace -e trace=openat,open ./myapp 2>&1 | grep ENOENT

# Find what network connections are made
strace -e trace=network -f ./myapp 2>&1 | grep connect

# Debug dynamic library loading failures
strace -e trace=openat ./myapp 2>&1 | grep "\.so"

# Find permission issues
strace -e trace=file ./myapp 2>&1 | grep -E "EACCES|EPERM"

# Debug slow startup (find where time is spent)
strace -c ./myapp 2>&1
# Look for high % time in unexpected syscalls

# Watch IPC/shared memory
strace -e trace=ipc,shm ./myapp

# Find what the binary exec's
strace -e trace=execve -f ./myapp

7. seccomp filter debugging

If a program is killed by a seccomp policy, strace reveals which syscall triggered it:

strace -e trace=all ./myapp 2>&1 | tail -5
# Often shows the last syscall before SIGSYS


For strace output patterns and ltrace filtering examples, see references/strace-patterns.md.

Related skills
Use skills/debuggers/gdb when strace shows the failing location and you need to inspect internals
Use skills/binaries/elf-inspection to understand what libraries and symbols a binary uses
Use skills/binaries/dynamic-linking for diagnosing LD_* and library loading issues
Use skills/profilers/linux-perf for performance profiling (strace overhead is too high for perf)
Weekly Installs
101
Repository
mohitmishra786/…v-skills
GitHub Stars
80
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass