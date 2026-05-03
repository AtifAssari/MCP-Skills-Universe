---
title: security-checklist
url: https://skills.sh/jamditis/claude-skills-journalism/security-checklist
---

# security-checklist

skills/jamditis/claude-skills-journalism/security-checklist
security-checklist
Installation
$ npx skills add https://github.com/jamditis/claude-skills-journalism --skill security-checklist
SKILL.md
Security checklist

Minimum viable security before shipping any web application. This is not exhaustive—it's the baseline that prevents obvious disasters.

Pre-ship audit

Run through this checklist before any production deployment. If you can't check an item, fix it first.

Authentication
 Passwords hashed with bcrypt, scrypt, or Argon2 (NEVER MD5/SHA1/plain text)
 Password requirements enforced (minimum 12 characters recommended)
 Session tokens are cryptographically random (use crypto.randomBytes or equivalent)
 Sessions expire (24 hours for normal apps, shorter for sensitive data)
 Logout actually invalidates the session server-side
 Password reset tokens are single-use and expire within 1 hour
 Failed login attempts are rate-limited (5 attempts, then cooldown)
 No credentials in code, logs, or error messages
Input validation
 All user input is validated server-side (client validation is UX, not security)
 SQL queries use parameterized statements (NEVER string concatenation)
 HTML output is escaped to prevent XSS (use framework defaults)
 File uploads validate type, size, and are stored outside webroot
 URLs and redirects are validated against allowlist
 JSON/XML parsers have entity expansion limits
Secrets management
 No secrets in source code or git history
 Environment variables or secrets manager for all credentials
 Different secrets for development/staging/production
 API keys have minimum required permissions
 Secrets can be rotated without code deployment
Database security
 Database not exposed to public internet
 Application uses dedicated database user (not root/admin)
 Database user has minimum required permissions
 Row-level security (RLS) enabled where applicable
 Backups encrypted and tested for restoration
 Connection strings use SSL/TLS
Network and transport
 HTTPS only (redirect HTTP to HTTPS)
 TLS 1.2+ (disable older versions)
 HSTS header enabled
 Secure cookie flags set (Secure, HttpOnly, SameSite)
 CORS configured for specific origins (not * in production)
Rate limiting and DDoS
 API endpoints rate-limited per user/IP
 Login endpoints have stricter limits
 CDN or DDoS protection in front of application
 Request size limits configured
 Timeout limits on all external calls
Logging and monitoring
 Authentication events logged (login, logout, failed attempts)
 No sensitive data in logs (passwords, tokens, PII)
 Logs stored securely with retention policy
 Alerts configured for suspicious patterns
 Error messages don't leak system information
Infrastructure
 Firewall configured (deny by default)
 Unnecessary ports closed
 SSH key authentication (no password auth)
 Dependencies updated (check for known vulnerabilities)
 Admin interfaces not publicly accessible
Common vulnerabilities by framework
Node.js/Express
// BAD: SQL injection
db.query(`SELECT * FROM users WHERE id = ${req.params.id}`);

// GOOD: Parameterized query
db.query('SELECT * FROM users WHERE id = $1', [req.params.id]);

// BAD: XSS vulnerability
res.send(`<h1>Hello ${req.query.name}</h1>`);

// GOOD: Use template engine with auto-escaping
res.render('greeting', { name: req.query.name });

// BAD: Secrets in code
const API_KEY = 'sk_live_abc123';

// GOOD: Environment variables
const API_KEY = process.env.API_KEY;

Python/Django/Flask
# BAD: SQL injection
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")

# GOOD: Parameterized query
cursor.execute("SELECT * FROM users WHERE id = %s", [user_id])

# BAD: Pickle deserialization (RCE vulnerability)
data = pickle.loads(user_input)

# GOOD: Use JSON for untrusted data
data = json.loads(user_input)

# BAD: Debug mode in production
app.run(debug=True)

# GOOD: Debug off, proper error handling
app.run(debug=False)

React/Frontend
// BAD: XSS via dangerouslySetInnerHTML
<div dangerouslySetInnerHTML={{ __html: userContent }} />

// GOOD: Let React escape content
<div>{userContent}</div>

// BAD: Storing tokens in localStorage (XSS accessible)
localStorage.setItem('token', authToken);

// BETTER: HttpOnly cookies (not accessible via JS)
// Set via server response header

// BAD: Exposing API keys in frontend code
const API_KEY = 'sk_live_abc123';

// GOOD: Proxy through your backend
const response = await fetch('/api/proxy/external-service');

Password hashing reference
Node.js with bcrypt
const bcrypt = require('bcrypt');

// Hashing (on registration)
const saltRounds = 12;
const hashedPassword = await bcrypt.hash(plainPassword, saltRounds);

// Verification (on login)
const isValid = await bcrypt.compare(plainPassword, hashedPassword);

Python with bcrypt
import bcrypt

# Hashing
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=12))

# Verification
is_valid = bcrypt.checkpw(password.encode('utf-8'), hashed)

Environment variables setup
.env file (development only, never commit)
# .env
DATABASE_URL=postgresql://user:pass@localhost:5432/myapp
JWT_SECRET=your-256-bit-secret-here
API_KEY=sk_test_xxxxx

.gitignore (mandatory)
.env
.env.local
.env.*.local
*.pem
*.key
credentials.json
secrets/

Loading environment variables
// Node.js with dotenv
require('dotenv').config();
const dbUrl = process.env.DATABASE_URL;

// Fail fast if missing
if (!process.env.JWT_SECRET) {
  throw new Error('JWT_SECRET environment variable is required');
}

Database row-level security (Supabase/PostgreSQL)
-- Enable RLS on table
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;

-- Users can only read their own documents
CREATE POLICY "Users can read own documents" ON documents
  FOR SELECT USING (auth.uid() = user_id);

-- Users can only insert documents as themselves
CREATE POLICY "Users can insert own documents" ON documents
  FOR INSERT WITH CHECK (auth.uid() = user_id);

-- Users can only update their own documents
CREATE POLICY "Users can update own documents" ON documents
  FOR UPDATE USING (auth.uid() = user_id);

-- Users can only delete their own documents
CREATE POLICY "Users can delete own documents" ON documents
  FOR DELETE USING (auth.uid() = user_id);

CORS configuration
Express.js
const cors = require('cors');

// BAD: Allow all origins
app.use(cors());

// GOOD: Specific origins
app.use(cors({
  origin: ['https://myapp.com', 'https://www.myapp.com'],
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  credentials: true
}));

Security headers
Express.js with Helmet
const helmet = require('helmet');

app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      imgSrc: ["'self'", "data:", "https:"],
    },
  },
  hsts: {
    maxAge: 31536000,
    includeSubDomains: true,
    preload: true
  }
}));

Manual headers
// Essential security headers
res.setHeader('X-Content-Type-Options', 'nosniff');
res.setHeader('X-Frame-Options', 'DENY');
res.setHeader('X-XSS-Protection', '1; mode=block');
res.setHeader('Strict-Transport-Security', 'max-age=31536000; includeSubDomains');
res.setHeader('Content-Security-Policy', "default-src 'self'");

What NOT to log
// NEVER log these:
// - Passwords (plain or hashed)
// - Session tokens / JWTs
// - API keys
// - Credit card numbers
// - Social security numbers
// - Full request bodies with user data

// BAD
console.log('Login attempt:', { email, password });
console.log('Request:', req.body);

// GOOD
console.log('Login attempt:', { email, success: false, reason: 'invalid_password' });
console.log('Request:', { endpoint: req.path, method: req.method, userId: req.user?.id });

Quick fixes for common issues
"I stored passwords in plain text"
Add password hashing immediately
Force password reset for all users
Invalidate all existing sessions
Check if database was ever exposed/leaked
"My API key is in the git history"
Rotate the key immediately (generate new one)
Revoke the old key
Use git filter-branch or BFG Repo-Cleaner to remove from history
Force push (coordinate with team)
"I don't know what data I'm logging"
Search codebase for console.log, logger., print(
Review what's being logged
Implement structured logging with field allowlists
Set up log rotation and retention
"My database is publicly accessible"
Change database credentials immediately
Configure firewall rules (allow only application server IPs)
Enable SSL/TLS for connections
Review access logs for unauthorized queries
Compliance quick reference
You likely need to care about:
GDPR (EU users): Data deletion rights, consent, breach notification
CCPA (California users): Similar to GDPR
PCI DSS (credit cards): Don't store card numbers, use payment processor
HIPAA (health data): Encryption, access controls, audit logs
SOC 2 (enterprise sales): Security controls documentation
Minimum for any user data:
Privacy policy explaining data collection
Way for users to request data deletion
Encryption in transit (HTTPS) and at rest
Access logs and audit trail
Incident response plan (even if basic)
Resources
OWASP Top 10: https://owasp.org/www-project-top-ten/
OWASP Cheat Sheets: https://cheatsheetseries.owasp.org/
Have I Been Pwned (check for breaches): https://haveibeenpwned.com/
Mozilla Observatory (test your headers): https://observatory.mozilla.org/
SSL Labs (test your TLS): https://www.ssllabs.com/ssltest/
Weekly Installs
93
Repository
jamditis/claude…urnalism
GitHub Stars
179
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass