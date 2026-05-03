---
title: ctf-reverse
url: https://skills.sh/ramzxy/ctf/ctf-reverse
---

# ctf-reverse

skills/ramzxy/ctf/ctf-reverse
ctf-reverse
Installation
$ npx skills add https://github.com/ramzxy/ctf --skill ctf-reverse
SKILL.md
CTF Reverse Engineering

Quick reference for RE challenges. For detailed techniques, see supporting files.

Additional Resources
tools.md - Tool-specific commands (GDB, Ghidra, radare2, IDA)
patterns.md - Common patterns, VMs, obfuscation, anti-debugging
Problem-Solving Workflow
Start with strings extraction - many easy challenges have plaintext flags
Try ltrace/strace - dynamic analysis often reveals flags without reversing
Map control flow before modifying execution
Automate manual processes via scripting (r2pipe, Python)
Validate assumptions by comparing decompiler outputs
Quick Wins (Try First!)
# Plaintext flag extraction
strings binary | grep -E "flag\{|CTF\{|pico"
strings binary | grep -iE "flag|secret|password"
rabin2 -z binary | grep -i "flag"

# Dynamic analysis - often captures flag directly
ltrace ./binary
strace -f -s 500 ./binary

# Hex dump search
xxd binary | grep -i flag

# Run with test inputs
./binary AAAA
echo "test" | ./binary

Initial Analysis
file binary           # Type, architecture
checksec --file=binary # Security features (for pwn)
chmod +x binary       # Make executable

Memory Dumping Strategy

Key insight: Let the program compute the answer, then dump it.

gdb ./binary
start
b *main+0x198           # Break at final comparison
run
# Enter any input of correct length
x/s $rsi                # Dump computed flag
x/38c $rsi              # As characters

Decoy Flag Detection

Pattern: Multiple fake targets before real check.

Identification:

Look for multiple comparison targets in sequence
Check for different success messages
Trace which comparison is checked LAST

Solution: Set breakpoint at FINAL comparison, not earlier ones.

GDB PIE Debugging

PIE binaries randomize base address. Use relative breakpoints:

gdb ./binary
start                    # Forces PIE base resolution
b *main+0xca            # Relative to main
run

Comparison Direction (Critical!)

Two patterns:

transform(flag) == stored_target - Reverse the transform
transform(stored_target) == flag - Flag IS the transformed data!

Pattern 2 solution: Don't reverse - just apply transform to stored target.

Common Encryption Patterns
XOR with single byte - try all 256 values
XOR with known plaintext (flag{, CTF{)
RC4 with hardcoded key
Custom permutation + XOR
XOR with position index (^ i or ^ (i & 0xff)) layered with a repeating key
Quick Tool Reference
# Radare2
r2 -d ./binary     # Debug mode
aaa                # Analyze
afl                # List functions
pdf @ main         # Disassemble main

# Ghidra (headless)
analyzeHeadless project/ tmp -import binary -postScript script.py

# IDA
ida64 binary       # Open in IDA64

Binary Types
Python .pyc
import marshal, dis
with open('file.pyc', 'rb') as f:
    f.read(16)  # Skip header
    code = marshal.load(f)
    dis.dis(code)

WASM
wasm2c checker.wasm -o checker.c
gcc -O3 checker.c wasm-rt-impl.c -o checker

Android APK
apktool d app.apk -o decoded/   # Best - decodes resources
jadx app.apk                     # Decompile to Java
grep -r "flag" decoded/res/values/strings.xml

.NET
dnSpy - debugging + decompilation
ILSpy - decompiler
Packed (UPX)
upx -d packed -o unpacked

Anti-Debugging Bypass

Common checks:

IsDebuggerPresent() (Windows)
ptrace(PTRACE_TRACEME) (Linux)
/proc/self/status TracerPid
Timing checks

Bypass: Set breakpoint at check, modify register to bypass conditional.

S-Box / Keystream Patterns

Xorshift32: Shifts 13, 17, 5 Xorshift64: Shifts 12, 25, 27 Magic constants: 0x2545f4914f6cdd1d, 0x9e3779b97f4a7c15

Custom VM Analysis
Identify structure: registers, memory, IP
Reverse executeIns for opcode meanings
Write disassembler mapping opcodes to mnemonics
Often easier to bruteforce than fully reverse
Look for the bytecode file loaded via command-line arg

VM challenge workflow (C'est La V(M)ie):

# 1. Find entry point: entry() → __libc_start_main(FUN_xxx, ...)
# 2. Identify loader function (reads .bin file into global buffer)
# 3. Find executor with giant switch statement (opcode dispatch)
# 4. Map each case to instruction: MOVI, ADD, XOR, CMP, JZ, READ, PRINT, HLT...
# 5. Write disassembler, annotate output
# 6. Identify flag transform (often reversible byte-by-byte)


Common VM opcodes to look for:

Pattern in decompiler	Likely instruction
global[param1] = param2	MOVI (move immediate)
global[p1] = global[p2]	MOVR (move register)
global[p1] ^= global[p2]	XOR
global[p1] op global[p2]; set flag	CMP
if (flag) IP = param	JZ/JNZ
read(stdin, &global[p1], 1)	READ
write(stdout, &global[p1], 1)	PRINT
Python Bytecode Reversing

Pattern (Slithering Bytes): Given dis.dis() output of a flag checker.

Key instructions:

LOAD_GLOBAL / LOAD_FAST — push name/variable onto stack
CALL N — pop function + N args, call, push result
BINARY_SUBSCR — pop index and sequence, push seq[idx]
COMPARE_OP — pop two values, compare (55=!=, 40===)
POP_JUMP_IF_TRUE/FALSE — conditional branch

Reversing XOR flag checkers:

# Pattern: ord(flag[i]) ^ KEY == EXPECTED[i]
# Reverse: chr(EXPECTED[i] ^ KEY) for each position

# Interleaved tables (odd/even indices):
odd_table = [...]   # Values for indices 1, 3, 5, ...
even_table = [...]  # Values for indices 0, 2, 4, ...
flag = [''] * 30
for i, val in enumerate(even_table):
    flag[i*2] = chr(val ^ key_even)
for i, val in enumerate(odd_table):
    flag[i*2+1] = chr(val ^ key_odd)

Signal-Based Binary Exploration

Pattern (Signal Signal Little Star): Binary uses UNIX signals as a binary tree navigation mechanism.

Identification:

Multiple sigaction() calls with SA_SIGINFO
sigaltstack() setup (alternate signal stack)
Handler decodes embedded payload, installs next pair of signals
Two types: Node (installs children) vs Leaf (prints message + exits)

Solving approach:

Hook sigaction via LD_PRELOAD to log signal installations
DFS through the binary tree by sending signals
At each stage, observe which 2 signals are installed
Send one, check if program exits (leaf) or installs 2 more (node)
If wrong leaf, backtrack and try sibling
// LD_PRELOAD interposer to log sigaction calls
int sigaction(int signum, const struct sigaction *act, ...) {
    if (act && (act->sa_flags & SA_SIGINFO))
        log("SET %d SA_SIGINFO=1\n", signum);
    return real_sigaction(signum, act, oldact);
}

Malware Anti-Analysis Bypass via Patching

Pattern (Carrot): Malware with multiple environment checks before executing payload.

Common checks to patch:

Check	Technique	Patch
ptrace(PTRACE_TRACEME)	Anti-debug	Change cmp -1 to cmp 0
sleep(150)	Anti-sandbox timing	Change sleep value to 1
/proc/cpuinfo "hypervisor"	Anti-VM	Flip JNZ to JZ
"VMware"/"VirtualBox" strings	Anti-VM	Flip JNZ to JZ
getpwuid username check	Environment	Flip comparison
LD_PRELOAD check	Anti-hook	Skip check
Fan count / hardware check	Anti-VM	Flip JLE to JGE
Hostname check	Environment	Flip JNZ to JZ

Ghidra patching workflow:

Find check function, identify the conditional jump
Click on instruction → Ctrl+Shift+G → modify opcode
For JNZ (0x75) → JZ (0x74), or vice versa
For immediate values: change operand bytes directly
Export: press O → choose "Original File" format
chmod +x the patched binary

Server-side validation bypass:

If patched binary sends system info to remote server, patch the data too
Modify string addresses in data-gathering functions
Change format strings to embed correct values directly
Expected Values Tables

Locating:

objdump -s -j .rodata binary | less
# Look near comparison instructions
# Size matches flag length

x86-64 Gotchas

Sign extension: 0xffffffc7 behaves differently in XOR vs addition

# For XOR: use low byte
esi_xor = esi & 0xff

# For addition: use full value with overflow
result = (r13 + esi) & 0xffffffff

Iterative Solver Pattern
for pos in range(flag_length):
    for c in range(256):
        computed = compute_output(c, current_state)
        if computed == EXPECTED[pos]:
            flag.append(c)
            update_state(c, computed)
            break


Uniform transform shortcut: if changing one input byte only changes one output byte, build a 0..255 mapping by repeating a single byte across the whole input, then invert.

Unicorn Emulation (Complex State)
from unicorn import *
from unicorn.x86_const import *

mu = Uc(UC_ARCH_X86, UC_MODE_64)
# Map segments, set up stack
# Hook to trace register changes
mu.emu_start(start_addr, end_addr)


Mixed-mode pitfall: if a 64-bit stub jumps into 32-bit code via retf/retfq, you must switch to a UC_MODE_32 emulator and copy GPRs, EFLAGS, and XMM regs; missing XMM state will corrupt SSE-based transforms.

Multi-Stage Shellcode Loaders

Pattern (I Heard You Liked Loaders): Nested shellcode with XOR decode loops and anti-debug.

Debugging workflow:

Break at call rax in launcher, step into shellcode
Bypass ptrace anti-debug: step to syscall, set $rax=0
Step through XOR decode loop (or break on int3 if hidden)
Repeat for each stage until final payload

Flag extraction from mov instructions:

# Final stage loads flag 4 bytes at a time via mov ebx, value
# Extract little-endian 4-byte chunks
values = [0x6174654d, 0x7b465443, ...]  # From disassembly
flag = b''.join(v.to_bytes(4, 'little') for v in values)

Timing Side-Channel Attack

Pattern (Clock Out): Validation time varies per correct character (longer sleep on match).

Exploitation:

import time
from pwn import *

flag = ""
for pos in range(flag_length):
    best_char, best_time = '', 0
    for c in string.printable:
        io = remote(host, port)
        start = time.time()
        io.sendline((flag + c).ljust(total_len, 'X'))
        io.recvall()
        elapsed = time.time() - start
        if elapsed > best_time:
            best_time = elapsed
            best_char = c
        io.close()
    flag += best_char

Godot Game Asset Extraction

Pattern (Steal the Xmas): Encrypted Godot .pck packages.

Tools:

gdsdecomp - Extract Godot packages
KeyDot - Extract encryption key from Godot executables

Workflow:

Run KeyDot against game executable → extract encryption key
Input key into gdsdecomp
Extract and open project in Godot editor
Search scripts/resources for flag data
Unstripped Binary Information Leaks

Pattern (Bad Opsec): Debug info and file paths leak author identity.

Quick checks:

strings binary | grep "/home/"    # Home directory paths
strings binary | grep "/Users/"   # macOS paths
file binary                       # Check if stripped
readelf -S binary | grep debug    # Debug sections present?

Custom Mangle Function Reversing

Pattern (Flag Appraisal): Binary mangles input 2 bytes at a time with intermediate state, compares to static target.

Approach:

Extract static target bytes from .rodata section
Understand mangle: processes pairs with running state value
Write inverse function (process in reverse, undo each operation)
Feed target bytes through inverse → recovers flag
Hex-Encoded String Comparison

Pattern (Spider's Curse): Input converted to hex, compared against hex constant.

Quick solve: Extract hex constant from strings/Ghidra, decode:

echo "4d65746143..." | xxd -r -p

Weekly Installs
18
Repository
ramzxy/ctf
GitHub Stars
1
First Seen
Feb 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail