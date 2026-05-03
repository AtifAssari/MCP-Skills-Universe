---
title: mobile-security
url: https://skills.sh/kiwamizamurai/cctf/mobile-security
---

# mobile-security

skills/kiwamizamurai/cctf/mobile-security
mobile-security
Installation
$ npx skills add https://github.com/kiwamizamurai/cctf --skill mobile-security
SKILL.md
Mobile Security Skill
Quick Workflow
Progress:
- [ ] Extract APK/IPA
- [ ] Decompile (jadx for Android)
- [ ] Search for hardcoded secrets
- [ ] Check native libraries
- [ ] Dynamic analysis with Frida if needed
- [ ] Extract flag

Quick Analysis Pipeline
# Android APK
file app.apk
apktool d app.apk -o extracted/
jadx app.apk -d output/
grep -r "flag\|secret" output/

# iOS IPA
unzip app.ipa -d extracted/
strings Payload/App.app/App | grep -i flag

Reference Files
Topic	Reference
Android APK Analysis	reference/android.md
iOS IPA Analysis	reference/ios.md
Frida & objection	reference/frida.md
Tools Summary
Tool	Purpose	Install
jadx	Java decompiler	github.com/skylot/jadx
apktool	APK decode/rebuild	apktool.org
Frida	Dynamic instrumentation	pip install frida-tools
objection	Runtime exploration	pip install objection
Ghidra	Native lib reversing	ghidra-sre.org
dex2jar	DEX to JAR	github.com/pxb1988/dex2jar
CTF Quick Patterns
# Flag in resources
grep -r "flag\|ctf\|secret" extracted/res/

# Flag in native library
strings extracted/lib/*/*.so | grep -i flag

# Hardcoded secrets
grep -r "api_key\|secret\|password" output/

Weekly Installs
25
Repository
kiwamizamurai/cctf
GitHub Stars
7
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail