---
title: utility-tools
url: https://skills.sh/vikiboss/60s-skills/utility-tools
---

# utility-tools

skills/vikiboss/60s-skills/utility-tools
utility-tools
Installation
$ npx skills add https://github.com/vikiboss/60s-skills --skill utility-tools
SKILL.md
Utility Tools Skill

This skill provides various utility functions for common tasks like translation, IP lookup, QR code generation, and more.

Available Tools
IP Address Lookup - Get location and ISP info for any IP
Text Translation - Translate between multiple languages
QR Code Generation - Create QR codes for any text/URL
Hash Calculation - Calculate MD5, SHA1, SHA256, SHA512
OG Metadata Extraction - Extract Open Graph metadata from URLs
WHOIS Lookup - Domain registration information
Password Generation - Generate secure random passwords
API Endpoints
Tool	Endpoint	Method
IP Lookup	/v2/ip	GET
Translation	/v2/fanyi	POST
QR Code	/v2/qrcode	GET
Hash	/v2/hash	POST
OG Metadata	/v2/og	POST
WHOIS	/v2/whois	GET
Password	/v2/password	GET
1. IP Address Lookup
import requests

# Lookup specific IP
response = requests.get('https://60s.viki.moe/v2/ip', params={'ip': '8.8.8.8'})
ip_info = response.json()

print(f"IP: {ip_info['ip']}")
print(f"Location: {ip_info['location']}")
print(f"ISP: {ip_info['isp']}")

# Get your own IP info (no params)
my_ip = requests.get('https://60s.viki.moe/v2/ip').json()

2. Text Translation
# Translate text
data = {
    'text': 'Hello World',
    'from': 'en',  # or 'auto' for auto-detection
    'to': 'zh'     # target language
}

response = requests.post('https://60s.viki.moe/v2/fanyi', json=data)
translation = response.json()

print(f"Original: {translation['text']}")
print(f"Translated: {translation['result']}")
print(f"From: {translation['from']} To: {translation['to']}")


Supported Languages:

zh - Chinese
en - English
ja - Japanese
ko - Korean
fr - French
de - German
es - Spanish
ru - Russian
And more...
# Get supported languages
response = requests.post('https://60s.viki.moe/v2/fanyi/langs')
languages = response.json()

3. QR Code Generation
# Generate QR code
params = {
    'text': 'https://github.com/vikiboss/60s',
    'size': 300  # pixels, default 200, min 50, max 1000
}

response = requests.get('https://60s.viki.moe/v2/qrcode', params=params)

# Save the QR code image
with open('qrcode.png', 'wb') as f:
    f.write(response.content)

4. Hash Calculation
# Calculate hash
data = {
    'text': 'Hello World',
    'algorithm': 'md5'  # md5, sha1, sha256, sha512
}

response = requests.post('https://60s.viki.moe/v2/hash', json=data)
result = response.json()

print(f"Algorithm: {result['algorithm']}")
print(f"Hash: {result['hash']}")

5. OG Metadata Extraction
# Extract Open Graph metadata from URL
data = {'url': 'https://github.com/vikiboss/60s'}

response = requests.post('https://60s.viki.moe/v2/og', json=data)
metadata = response.json()

print(f"Title: {metadata['title']}")
print(f"Description: {metadata['description']}")
print(f"Image: {metadata['image']}")
print(f"URL: {metadata['url']}")

6. WHOIS Lookup
# Domain WHOIS information
params = {'domain': 'github.com'}

response = requests.get('https://60s.viki.moe/v2/whois', params=params)
whois_info = response.json()

print(f"Domain: {whois_info['domain']}")
print(f"Registrar: {whois_info['registrar']}")
print(f"Created: {whois_info['created_date']}")
print(f"Expires: {whois_info['expiration_date']}")

7. Password Generation
# Generate secure password
params = {
    'length': 16,        # 6-128
    'numbers': True,     # include numbers
    'lowercase': True,   # include lowercase
    'uppercase': True,   # include uppercase
    'symbols': True      # include special characters
}

response = requests.get('https://60s.viki.moe/v2/password', params=params)
password_data = response.json()

print(f"Password: {password_data['password']}")
print(f"Strength: {password_data['strength']}")

Example Use Cases
Multi-language Chatbot
def auto_translate(text, target_lang='zh'):
    data = {
        'text': text,
        'from': 'auto',
        'to': target_lang
    }
    response = requests.post('https://60s.viki.moe/v2/fanyi', json=data)
    return response.json()['result']

# Usage
user_input = "Hello, how are you?"
translated = auto_translate(user_input, 'zh')
print(translated)  # 你好，你好吗？

URL Shortener with QR Code
def create_qr_for_url(url, size=200):
    params = {'text': url, 'size': size}
    response = requests.get('https://60s.viki.moe/v2/qrcode', params=params)
    return response.content

# Generate and save
qr_image = create_qr_for_url('https://example.com')
with open('url_qr.png', 'wb') as f:
    f.write(qr_image)

Security Tools
def check_password_hash(password):
    """Generate multiple hashes for password"""
    algorithms = ['md5', 'sha1', 'sha256', 'sha512']
    hashes = {}
    
    for algo in algorithms:
        data = {'text': password, 'algorithm': algo}
        response = requests.post('https://60s.viki.moe/v2/hash', json=data)
        hashes[algo] = response.json()['hash']
    
    return hashes

def generate_secure_password(length=16):
    params = {
        'length': length,
        'numbers': True,
        'lowercase': True,
        'uppercase': True,
        'symbols': True
    }
    response = requests.get('https://60s.viki.moe/v2/password', params=params)
    return response.json()['password']

Website Preview Card
def get_link_preview(url):
    """Get rich preview data for a URL"""
    data = {'url': url}
    response = requests.post('https://60s.viki.moe/v2/og', json=data)
    og = response.json()
    
    preview = f"""
    📄 {og['title']}
    📝 {og['description']}
    🖼️ {og['image']}
    🔗 {og['url']}
    """
    return preview

Best Practices
Translation: Use 'auto' for source language when unsure
QR Codes: Keep size between 200-500px for most uses
Hashing: Use SHA256 or SHA512 for security applications
Passwords: Always use all character types for strong passwords
Error Handling: Always validate inputs and handle API errors
Example Interactions
User: "把这段话翻译成英文：你好世界"
data = {'text': '你好世界', 'from': 'zh', 'to': 'en'}
response = requests.post('https://60s.viki.moe/v2/fanyi', json=data)
print(response.json()['result'])  # Hello World

User: "生成一个强密码"
params = {'length': 20, 'symbols': True, 'uppercase': True, 'lowercase': True, 'numbers': True}
response = requests.get('https://60s.viki.moe/v2/password', params=params)
print(f"🔐 生成的密码：{response.json()['password']}")

User: "查询这个IP地址的位置：1.1.1.1"
response = requests.get('https://60s.viki.moe/v2/ip', params={'ip': '1.1.1.1'})
info = response.json()
print(f"📍 IP: {info['ip']}")
print(f"🌍 位置: {info['location']}")
print(f"🏢 运营商: {info['isp']}")

Related Resources
60s API Documentation
GitHub Repository
Weekly Installs
56
Repository
vikiboss/60s-skills
GitHub Stars
32
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn