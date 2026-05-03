---
title: jwt-encode
url: https://skills.sh/jsonwebtoken/jwt-skills/jwt-encode
---

# jwt-encode

skills/jsonwebtoken/jwt-skills/jwt-encode
jwt-encode
Installation
$ npx skills add https://github.com/jsonwebtoken/jwt-skills --skill jwt-encode
SKILL.md
JWT Encode

Create and sign JWTs for testing and development.

Steps
Gather inputs: claims/payload, algorithm (default: HS256), secret or key, expiration (default: 1 hour).
Build header: {"alg": "HS256", "typ": "JWT"}. Add kid if provided.
Build payload: Always include iat and exp unless the user opts out. Add user-specified claims.
Sign the token using the best available method (see below).
Display the result: the full JWT string and a decoded breakdown of header + payload.
Signing Methods

Pick the first available. Use the user's claims, secret, and algorithm — the examples below are templates only. Always pass the secret via an inline env var to avoid shell history exposure.

Node.js (preferred):

First, ensure jose is available — install it globally if missing:

node --input-type=module -e "await import('jose')" 2>/dev/null || npm install -g jose


Then sign the token:

JWT_SECRET='user-provided-secret' node --input-type=module -e "import {SignJWT} from 'jose'; console.log(await new SignJWT({sub:'1234567890'}).setProtectedHeader({alg:'HS256'}).setIssuedAt().setExpirationTime('1h').sign(new TextEncoder().encode(process.env.JWT_SECRET)))"


Python:

JWT_SECRET='user-provided-secret' python3 -c "import jwt,time; print(jwt.encode({'sub':'1234567890','iat':int(time.time()),'exp':int(time.time())+3600}, __import__('os').environ['JWT_SECRET'], algorithm='HS256'))"


Bash (HMAC-SHA256 only):

header=$(printf '{"alg":"HS256","typ":"JWT"}' | openssl base64 -e -A | tr '+/' '-_' | tr -d '=')
payload=$(printf '{"sub":"1234567890","iat":1700000000,"exp":1700003600}' | openssl base64 -e -A | tr '+/' '-_' | tr -d '=')
signature=$(printf '%s.%s' "$header" "$payload" | openssl dgst -sha256 -hmac "$JWT_SECRET" -binary | openssl base64 -e -A | tr '+/' '-_' | tr -d '=')
printf '%s.%s.%s\n' "$header" "$payload" "$signature"

Generating Test Keys

Only when the user needs asymmetric keys:

# RSA
openssl genrsa -out private.pem 2048 && openssl rsa -in private.pem -pubout -out public.pem
# ECDSA P-256
openssl ecparam -genkey -name prime256v1 -noout -out private-ec.pem && openssl ec -in private-ec.pem -pubout -out public-ec.pem

Security Rules
Never pass secrets as literal command-line arguments. Use environment variables ($JWT_SECRET) or file input (--secret-file). Command args are visible in shell history and ps output.
Never install packages without user consent. Do not use npx -y or pip install silently.
If the user doesn't provide a secret, generate a random one with openssl rand -base64 32 and clearly label it as a test-only secret.
alg: none — If the user requests it, warn that this creates an unsigned token exploitable via CVE-2015-9235. Only create it after explicit confirmation.
Generated key files — Remind the user to delete test keys when done. Never write keys to version-controlled directories.
Weekly Installs
93
Repository
jsonwebtoken/jwt-skills
GitHub Stars
2
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail