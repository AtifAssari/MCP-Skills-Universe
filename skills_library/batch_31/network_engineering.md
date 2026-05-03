---
title: network-engineering
url: https://skills.sh/89jobrien/steve/network-engineering
---

# network-engineering

skills/89jobrien/steve/network-engineering
network-engineering
Installation
$ npx skills add https://github.com/89jobrien/steve --skill network-engineering
SKILL.md
Network Engineering

Comprehensive network engineering skill covering network design, troubleshooting, load balancing, DNS, and network security.

When to Use This Skill
Designing network topologies
Troubleshooting connectivity issues
Configuring load balancers
DNS configuration and troubleshooting
SSL/TLS setup and debugging
Network security implementation
Performance optimization
CDN configuration
Network Architecture
OSI Model Reference
Layer	Name	Protocols	Troubleshooting
7	Application	HTTP, DNS, SMTP	curl, browser tools
6	Presentation	SSL/TLS	openssl
5	Session	NetBIOS	-
4	Transport	TCP, UDP	netstat, ss
3	Network	IP, ICMP	ping, traceroute
2	Data Link	Ethernet	arp
1	Physical	-	cable tester
VPC/Network Design

Subnet Strategy:

VPC CIDR: 10.0.0.0/16 (65,536 IPs)

Public Subnets (internet-facing):
  - 10.0.1.0/24 (AZ-a) - Load balancers, bastion
  - 10.0.2.0/24 (AZ-b)
  - 10.0.3.0/24 (AZ-c)

Private Subnets (application tier):
  - 10.0.11.0/24 (AZ-a) - App servers
  - 10.0.12.0/24 (AZ-b)
  - 10.0.13.0/24 (AZ-c)

Database Subnets (isolated):
  - 10.0.21.0/24 (AZ-a) - Databases only
  - 10.0.22.0/24 (AZ-b)
  - 10.0.23.0/24 (AZ-c)


Traffic Flow:

Internet → Load Balancer (public) → App (private) → DB (isolated)
NAT Gateway for private subnet outbound
VPC Endpoints for AWS services
Load Balancing
Load Balancer Types
Type	Layer	Use Case
Application (ALB)	7	HTTP/HTTPS, path routing
Network (NLB)	4	TCP/UDP, static IP, high performance
Classic	4/7	Legacy
Gateway	3	Third-party appliances
Health Checks
# ALB Health Check
health_check:
  path: /health
  protocol: HTTP
  port: 8080
  interval: 30
  timeout: 5
  healthy_threshold: 2
  unhealthy_threshold: 3
  matcher: "200-299"

Routing Strategies
Round Robin: Equal distribution
Least Connections: Route to least busy
IP Hash: Sticky sessions by client IP
Weighted: Percentage-based distribution
Path-based: Route by URL path
Host-based: Route by hostname
DNS
Record Types
Type	Purpose	Example
A	IPv4 address	example.com → 192.0.2.1
AAAA	IPv6 address	example.com → 2001:db8::1
CNAME	Alias	www → example.com
MX	Mail server	example.com → mail.example.com
TXT	Arbitrary text	SPF, DKIM, verification
NS	Name server	DNS delegation
SRV	Service location	_sip._tcp.example.com
CAA	Certificate authority	Restrict CA issuance
DNS Debugging
# Query specific record type
dig example.com A
dig example.com MX
dig example.com TXT

# Query specific DNS server
dig @8.8.8.8 example.com

# Trace DNS resolution
dig +trace example.com

# Check propagation
dig +short example.com @{dns-server}

TTL Strategy
Record Type	Recommended TTL
Static content	86400 (1 day)
Dynamic content	300 (5 min)
Failover records	60 (1 min)
Pre-migration	Lower to 60
SSL/TLS
Certificate Types
Type	Validation	Use Case
DV	Domain ownership	Basic sites
OV	Organization verified	Business sites
EV	Extended validation	High-trust sites
Wildcard	*.domain.com	Multiple subdomains
SAN	Multi-domain	Multiple specific domains
TLS Configuration

Recommended Settings:

TLS 1.2 and 1.3 only
Strong cipher suites (AEAD)
HSTS enabled
OCSP stapling
Certificate transparency
Debugging SSL
# Check certificate
openssl s_client -connect example.com:443 -servername example.com

# Check certificate chain
openssl s_client -connect example.com:443 -showcerts

# Check expiration
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -dates

# Test TLS versions
openssl s_client -connect example.com:443 -tls1_2
openssl s_client -connect example.com:443 -tls1_3

Troubleshooting
Connectivity Checklist
Physical/Cloud layer: Is the instance running?
Security groups: Are ports open?
NACLs: Are subnets allowing traffic?
Route tables: Is routing correct?
DNS: Does name resolve?
Application: Is service listening?
Common Commands
# Check if port is listening
netstat -tlnp | grep :80
ss -tlnp | grep :80

# Test TCP connectivity
nc -zv hostname 443
telnet hostname 443

# Check routes
ip route
traceroute hostname
mtr hostname

# DNS resolution
nslookup hostname
dig hostname
host hostname

# Network interfaces
ip addr
ifconfig

# Active connections
netstat -an
ss -tuln

Performance Debugging
# Bandwidth test
iperf3 -c server-ip

# Latency analysis
ping -c 100 hostname | tail -1

# MTU issues
ping -M do -s 1472 hostname

# Packet capture
tcpdump -i eth0 port 443

Reference Files
references/troubleshooting.md - Detailed troubleshooting workflows
Integration with Other Skills
cloud-infrastructure - For cloud networking
security-engineering - For network security
performance - For network optimization
Weekly Installs
63
Repository
89jobrien/steve
GitHub Stars
4
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass