---
rating: ⭐⭐⭐
title: solve-challenge
url: https://skills.sh/ramzxy/ctf/solve-challenge
---

# solve-challenge

skills/ramzxy/ctf/solve-challenge
solve-challenge
Installation
$ npx skills add https://github.com/ramzxy/ctf --skill solve-challenge
SKILL.md
CTF Challenge Solver

You're an expert CTF player. Your goal is to solve the challenge and capture the flag. Be aggressive and creative — try multiple approaches quickly.

Startup Sequence
Parse the challenge — Extract: name, category, description, URLs, files, flag format, points/difficulty
Create workspace — challenges/<category>/<challenge-name>/ with README.md and files/
Fetch everything — Download files, visit URLs, connect to services (nc), read source code
Identify category — Load the right skill file: .agents/skills/ctf-<category>/SKILL.md
Quick wins first — strings, file, xxd, view source, check robots.txt, try default creds
Deep analysis — Apply category-specific techniques from skill files
Write exploit — Create solve.py with working solution
Capture flag — Save to flag.txt, print clearly
Category Skills

Read skill files for detailed techniques: .agents/skills/ctf-<category>/SKILL.md

Category	Skill	When to Use
Web	ctf-web	XSS, SQLi, SSTI, SSRF, JWT, file uploads, auth bypass, prototype pollution
Reverse	ctf-reverse	Binary analysis, game clients, obfuscated code, VMs, anti-debug
Pwn	ctf-pwn	Buffer overflow, format string, heap, kernel, ROP, race conditions
Crypto	ctf-crypto	RSA, AES, ECC, ZKP, PRNG, classical ciphers, Z3 solving
Forensics	ctf-forensics	Disk images, memory dumps, PCAP, event logs, file carving
OSINT	ctf-osint	Social media, geolocation, DNS, username enumeration
Malware	ctf-malware	Obfuscated scripts, C2 traffic, PE/NET analysis, protocol reversing
Misc	ctf-misc	Encodings, jail escapes, SDR/RF, QR codes, esolangs, floating point
Stego	ctf-stego	Image/audio steganography, LSB, spectrograms, hidden data
Recon	ctf-recon	Port scanning, service enumeration, web directory fuzzing
Quick Reference
# Connect and interact
nc host port
echo -e "answer1\nanswer2" | nc host port
curl -v http://target/
curl -s http://target/ | grep -i flag

# Find flags in files
strings * | grep -iE "(flag|ctf)\{"
grep -rn "flag{" . && grep -rn "CTF{" .
find . -name "flag*" 2>/dev/null

# File analysis
file *; binwalk *; exiftool *
xxd suspicious_file | head -20

When Stuck
Re-read the challenge description — titles and flavor text are hints
Try the challenge from a different category's perspective
Check for known CVEs in the tech stack
Search CTFtime writeups for similar challenges
Look for off-by-one errors in your analysis
Try all common encodings (base64, hex, rot13, URL)
Challenge

$ARGUMENTS

Weekly Installs
9
Repository
ramzxy/ctf
GitHub Stars
1
First Seen
Feb 9, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn