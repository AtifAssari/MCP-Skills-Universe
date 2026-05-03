---
title: curl-http
url: https://skills.sh/1mangesh1/dev-skills-collection/curl-http
---

# curl-http

skills/1mangesh1/dev-skills-collection/curl-http
curl-http
Installation
$ npx skills add https://github.com/1mangesh1/dev-skills-collection --skill curl-http
SKILL.md
curl and HTTPie Reference
HTTP Methods
# GET
curl https://api.example.com/users
curl -s https://api.example.com/users          # suppress progress meter
curl -i https://api.example.com/users          # include response headers
curl -I https://api.example.com/users          # HEAD request (headers only)

# POST (JSON body)
curl -X POST https://api.example.com/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@example.com"}'
curl -X POST https://api.example.com/users -H "Content-Type: application/json" -d @payload.json

# PUT
curl -X PUT https://api.example.com/users/42 \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@example.com"}'

# PATCH
curl -X PATCH https://api.example.com/users/42 \
  -H "Content-Type: application/json" -d '{"status":"active"}'

# DELETE
curl -X DELETE https://api.example.com/users/42
curl -X DELETE https://api.example.com/users/42 -H "Content-Type: application/json" -d '{"reason":"duplicate"}'

Headers
curl -H "X-Request-ID: abc123" https://api.example.com                    # single header
curl -H "Accept: application/json" -H "Content-Type: application/json" \
     -H "X-API-Key: key123" https://api.example.com                       # multiple
curl -H "User-Agent: my-script/1.0" https://api.example.com               # override default
curl -H "Accept:" https://api.example.com                                  # remove a default header

Request Body
# JSON
curl -X POST https://api.example.com/data -H "Content-Type: application/json" \
  -d '{"key":"value","count":10}'

# URL-encoded form data
curl -X POST https://api.example.com/login -d "username=alice&password=secret"
curl -X POST https://api.example.com/search --data-urlencode "q=hello world&limit=10"

# Multipart file upload
curl -X POST https://api.example.com/upload -F "file=@report.pdf" -F "description=Quarterly report"
curl -X POST https://api.example.com/upload -F "file=@photo.png;type=image/png"

# Raw binary upload
curl -X POST https://api.example.com/upload --data-binary @archive.tar.gz \
  -H "Content-Type: application/octet-stream"

Authentication
# Basic auth
curl -u alice:secretpass https://api.example.com/me
curl -H "Authorization: Basic $(echo -n alice:secretpass | base64)" https://api.example.com/me

# Bearer token
curl -H "Authorization: Bearer eyJhbGciOi..." https://api.example.com/me

# API key (as header or query parameter)
curl -H "X-API-Key: abc123" https://api.example.com/data
curl "https://api.example.com/data?api_key=abc123"

# OAuth 2.0 client credentials flow
TOKEN=$(curl -s -X POST https://auth.example.com/oauth/token \
  -d "grant_type=client_credentials" \
  -d "client_id=CLIENT_ID" \
  -d "client_secret=CLIENT_SECRET" | jq -r '.access_token')
curl -H "Authorization: Bearer $TOKEN" https://api.example.com/resource

Response Handling
# Extract status code
curl -s -o /dev/null -w "%{http_code}" https://api.example.com

# Headers only / headers with body
curl -I https://api.example.com
curl -i https://api.example.com

# Save response to file
curl -o response.json https://api.example.com/data
curl -O https://cdn.example.com/file.tar.gz            # keep remote filename
curl -D headers.txt -o body.json https://api.example.com/data  # separate files

# Follow redirects
curl -L https://short.url/abc
curl -L --max-redirs 5 https://short.url/abc

# Check success in scripts
if curl -s -f -o /dev/null https://api.example.com/health; then
  echo "Service is up"
fi

# Pretty-print JSON
curl -s https://api.example.com/data | jq .
curl -s https://api.example.com/data | python3 -m json.tool

Verbose and Debug Modes
curl -v https://api.example.com                        # request/response headers + TLS handshake
curl -v https://api.example.com 2>debug.log            # verbose output to file
curl --trace - https://api.example.com                 # full hex trace to stderr
curl --trace trace.log --trace-time https://api.example.com  # trace with timestamps
curl -s -D - -o /dev/null https://api.example.com      # headers only (less noisy than -v)

Timing Breakdown
# Single metric
curl -s -o /dev/null -w "Total: %{time_total}s\n" https://api.example.com

# Full breakdown (DNS lookup, TCP connect, TLS handshake, TTFB, total)
curl -s -o /dev/null -w "\
  DNS:     %{time_namelookup}s\n\
  Connect: %{time_connect}s\n\
  TLS:     %{time_appconnect}s\n\
  TTFB:    %{time_starttransfer}s\n\
  Total:   %{time_total}s\n\
  Size:    %{size_download} bytes\n\
  Speed:   %{speed_download} bytes/s\n" https://api.example.com

# Reusable: save the format string to a file and reference with -w @curl-timing.txt

Cookies
curl -b "session=abc123" https://api.example.com                           # send a cookie
curl -c cookies.txt https://api.example.com/login -d "user=alice&pass=s"   # save cookies
curl -b cookies.txt https://api.example.com/dashboard                      # load cookies
curl -b cookies.txt -c cookies.txt https://api.example.com/action          # cookie jar

SSL/TLS Options
curl -k https://self-signed.example.com                                    # skip cert verification
curl --cacert /path/to/ca-bundle.crt https://api.example.com               # custom CA bundle
curl --cert client.pem --key client-key.pem https://api.example.com        # client certificate
curl --tlsv1.2 https://api.example.com                                     # force TLS 1.2
curl --tlsv1.3 https://api.example.com                                     # force TLS 1.3

Proxy Settings
curl -x http://proxy.example.com:8080 https://api.example.com              # HTTP proxy
curl --socks5 127.0.0.1:1080 https://api.example.com                       # SOCKS5 proxy
curl --socks5-hostname 127.0.0.1:1080 https://api.example.com              # DNS via proxy
curl -x http://user:pass@proxy.example.com:8080 https://api.example.com    # proxy with auth
curl --noproxy "localhost,127.0.0.1,.internal" https://api.example.com     # bypass proxy

Rate Limiting and Retry
curl --retry 5 https://api.example.com                                     # retry on transient errors
curl --retry 5 --retry-delay 3 https://api.example.com                     # 3s between retries
curl --retry 5 --retry-all-errors https://api.example.com                  # retry all errors (7.71+)
curl --limit-rate 100K https://cdn.example.com/large.zip -o file.zip       # throttle transfer
curl --connect-timeout 5 --max-time 30 https://api.example.com             # timeouts

Downloading Files
curl -O https://cdn.example.com/archive.tar.gz                             # download with progress
curl -sO https://cdn.example.com/archive.tar.gz                            # download silently
curl -C - -O https://cdn.example.com/large-file.iso                        # resume interrupted
curl -O https://cdn.example.com/a.zip -O https://cdn.example.com/b.zip     # multiple files
curl -o local-name.tar.gz https://cdn.example.com/archive.tar.gz           # rename on save

API Testing Patterns
# CRUD cycle
ID=$(curl -s -X POST https://api.example.com/items \
  -H "Content-Type: application/json" -d '{"name":"test"}' | jq -r '.id')
curl -s https://api.example.com/items/$ID | jq .
curl -s -X PATCH https://api.example.com/items/$ID \
  -H "Content-Type: application/json" -d '{"name":"updated"}' | jq .
curl -s -X DELETE https://api.example.com/items/$ID

# GraphQL
curl -X POST https://api.example.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query":"{ users { id name email } }"}'

# Webhook testing
curl -X POST https://your-app.example.com/webhooks \
  -H "Content-Type: application/json" -H "X-Webhook-Secret: secret123" \
  -d '{"event":"order.created","data":{"id":1}}'

# Health check script
for endpoint in /health /ready /metrics; do
  code=$(curl -s -o /dev/null -w "%{http_code}" "https://api.example.com${endpoint}")
  echo "${endpoint}: ${code}"
done

curl to Code Conversion
# Generate C source reproducing the request via libcurl
curl --libcurl generated.c -X POST https://api.example.com/data \
  -H "Content-Type: application/json" -d '{"key":"value"}'

# Third-party converters (curlconverter.com) support Python, JS, Go, PHP, etc.
#   npm install -g curlconverter
#   curlconverter --language python 'curl -X POST ...'

HTTPie as an Alternative

HTTPie (http / https commands) provides a more readable syntax for common tasks.

# GET
http https://api.example.com/users              # colored, formatted output
http -b https://api.example.com/users           # body only
http -h https://api.example.com/users           # headers only

# POST JSON (default content type)
http POST https://api.example.com/users name=Alice email=alice@example.com
http POST https://api.example.com/users name=Alice age:=30 active:=true tags:='["a","b"]'

# Auth
http -a alice:secret https://api.example.com/me              # basic
http https://api.example.com/me "Authorization:Bearer tok"   # bearer

# File upload and download
http --form POST https://api.example.com/upload file@report.pdf
http --download https://cdn.example.com/archive.tar.gz

Comparison table
Operation	curl	HTTPie
GET with headers	curl -i URL	http URL
POST JSON	curl -X POST -H C-T:json -d '{}'	http POST URL key=val
Bearer auth	curl -H "Authorization: Bearer T"	http URL Authorization:Bearer\ T
Download file	curl -O URL	http --download URL
Form upload	curl -F "f=@file"	http --form POST URL f@file
Common Gotchas
Quoting
# Unix: wrap JSON in single quotes
curl -d '{"key":"value"}' https://api.example.com

# Windows cmd.exe: escape inner quotes or use a file
curl -d "{\"key\":\"value\"}" https://api.example.com
curl -d @payload.json https://api.example.com

Windows vs Unix
cmd.exe does not support single quotes; use double quotes with escaped inner quotes.
PowerShell requires backtick escaping or here-strings for JSON bodies.
Line continuation: \ on Unix, ^ on Windows cmd.exe.
Other pitfalls
Forgetting -L when the server returns a 301/302 redirect.
Using -X GET with -d -- curl sends the body but some servers ignore it on GET.
Not URL-encoding query parameters; use --data-urlencode or --url-query (curl 7.87+).
-o /dev/null on Windows should be -o NUL.
Piping binary output without --output - can corrupt the terminal.
Weekly Installs
28
Repository
1mangesh1/dev-s…llection
GitHub Stars
3
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail