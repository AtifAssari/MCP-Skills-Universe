---
rating: ⭐⭐⭐
title: jc
url: https://skills.sh/knoopx/pi/jc
---

# jc

skills/knoopx/pi/jc
jc
Installation
$ npx skills add https://github.com/knoopx/pi --skill jc
SKILL.md
jc

JSONifies the output of CLI tools and file-types for easier parsing.

Basic Usage
command | jc --parser          # Pipe output
jc command                    # Magic syntax
jc --help                     # List all parsers
jc --help --parser            # Parser docs

Examples
dig example.com | jc --dig | jq '.answer[].data'
ps aux | jc --ps
ifconfig | jc --ifconfig

Parsers
Category	Parsers
System	ps, top, free, df, du, ls, stat, uptime
Network	dig, ping, traceroute, netstat, ss, ifconfig
Files	ls, find, stat, file, mount, fstab
Packages	dpkg -l, rpm -qi, pacman, brew
Logs	syslog, clf (Common Log Format)
Dev	git log, docker ps, kubectl
Options
Flag	Description
-p	Pretty format JSON
-r	Raw output (less processed)
-u	Unbuffered output
-q	Quiet (suppress warnings)
-d	Debug mode
-y	YAML output
-M	Add metadata
-s	Slurp multi-line input
Slicing

Skip lines: START:STOP syntax

cat file.txt | jc 1:-1 --parser  # Skip first/last lines

Slurp Mode

For multi-line parsers: --slurp outputs array

cat ips.txt | jc --slurp --ip-address

Python Library
import jc

# Parse command output
data = jc.parse('dig', output_string)

# Or parse directly
data = jc.parsers.dig.parse(output_string)

Tips
Magic syntax: jc command auto-detects parser
Use jq for processing: jc cmd | jq '.field'
--slurp for multiple items per file
Streaming parsers for large outputs
Python lib returns dict/list, not JSON
Related Skills
nu-shell: Alternative structured data processing
toon: Compact JSON representation
Weekly Installs
29
Repository
knoopx/pi
GitHub Stars
45
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass