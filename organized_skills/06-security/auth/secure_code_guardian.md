---
rating: ⭐⭐
title: secure-code-guardian
url: https://skills.sh/jeffallan/claude-skills/secure-code-guardian
---

# secure-code-guardian

skills/jeffallan/claude-skills/secure-code-guardian
secure-code-guardian
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill secure-code-guardian
Summary

Custom security implementations for authentication, authorization, input validation, and OWASP Top 10 vulnerability prevention.

Covers password hashing (bcrypt/argon2), parameterized SQL queries, JWT validation, and rate limiting with explicit code examples
Includes validation checkpoints for authentication (brute-force, session fixation, token expiration), authorization (privilege escalation), input handling (SQL injection, XSS), and security headers
Enforces must-do constraints: hashed passwords, parameterized queries, input sanitization, security headers (CSP, HSTS), and environment-based secret storage
Provides reference guides for OWASP patterns, authentication flows, input validation with Zod, XSS/CSRF prevention, and Helmet configuration
SKILL.md
Secure Code Guardian
Core Workflow
Threat model — Identify attack surface and threats
Design — Plan security controls
Implement — Write secure code with defense in depth; see code examples below
Validate — Test security controls with explicit checkpoints (see below)
Document — Record security decisions
Validation Checkpoints

After each implementation step, verify:

Authentication: Test brute-force protection (lockout/rate limit triggers), session fixation resistance, token expiration, and invalid-credential error messages (must not leak user existence).
Authorization: Verify horizontal and vertical privilege escalation paths are blocked; test with tokens belonging to different roles/users.
Input handling: Confirm SQL injection payloads (' OR 1=1--) are rejected; confirm XSS payloads (<script>alert(1)</script>) are escaped or rejected.
Headers/CORS: Validate with a security scanner (e.g., curl -I, Mozilla Observatory) that security headers are present and CORS origin allowlist is correct.
Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
OWASP	references/owasp-prevention.md	OWASP Top 10 patterns
Authentication	references/authentication.md	Password hashing, JWT
Input Validation	references/input-validation.md	Zod, SQL injection
XSS/CSRF	references/xss-csrf.md	XSS prevention, CSRF
Headers	references/security-headers.md	Helmet, rate limiting
Constraints
MUST DO
Hash passwords with bcrypt/argon2 (never MD5/SHA-1/unsalted hashes)
Use parameterized queries (never string-interpolated SQL)
Validate and sanitize all user input before use
Implement rate limiting on auth endpoints
Set security headers (CSP, HSTS, X-Frame-Options)
Log security events (failed auth, privilege escalation attempts)
Store secrets in environment variables or secret managers (never in source code)
MUST NOT DO
Store passwords in plaintext or reversibly encrypted form
Trust user input without validation
Expose sensitive data in logs or error responses
Use weak or deprecated algorithms (MD5, SHA-1, DES, ECB mode)
Hardcode secrets or credentials in code
Code Examples
Password Hashing (bcrypt)
import bcrypt from 'bcrypt';

const SALT_ROUNDS = 12; // minimum 10; 12 balances security and performance

export async function hashPassword(plaintext: string): Promise<string> {
  return bcrypt.hash(plaintext, SALT_ROUNDS);
}

export async function verifyPassword(plaintext: string, hash: string): Promise<boolean> {
  return bcrypt.compare(plaintext, hash);
}

Parameterized SQL Query (Node.js / pg)
// NEVER: `SELECT * FROM users WHERE email = '${email}'`
// ALWAYS: use positional parameters
import { Pool } from 'pg';
const pool = new Pool();

export async function getUserByEmail(email: string) {
  const { rows } = await pool.query(
    'SELECT id, email, role FROM users WHERE email = $1',
    [email]  // value passed separately — never interpolated
  );
  return rows[0] ?? null;
}

Input Validation with Zod
import { z } from 'zod';

const LoginSchema = z.object({
  email: z.string().email().max(254),
  password: z.string().min(8).max(128),
});

export function validateLoginInput(raw: unknown) {
  const result = LoginSchema.safeParse(raw);
  if (!result.success) {
    // Return generic error — never echo raw input back
    throw new Error('Invalid credentials format');
  }
  return result.data;
}

JWT Validation
import jwt from 'jsonwebtoken';

const JWT_SECRET = process.env.JWT_SECRET!; // never hardcode

export function verifyToken(token: string): jwt.JwtPayload {
  // Throws if expired, tampered, or wrong algorithm
  const payload = jwt.verify(token, JWT_SECRET, {
    algorithms: ['HS256'],   // explicitly allowlist algorithm
    issuer: 'your-app',
    audience: 'your-app',
  });
  if (typeof payload === 'string') throw new Error('Invalid token payload');
  return payload;
}

Securing an Endpoint — Full Flow
import express from 'express';
import rateLimit from 'express-rate-limit';
import helmet from 'helmet';

const app = express();
app.use(helmet()); // sets CSP, HSTS, X-Frame-Options, etc.
app.use(express.json({ limit: '10kb' })); // limit payload size

const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 10,                   // 10 attempts per window per IP
  standardHeaders: true,
  legacyHeaders: false,
});

app.post('/api/login', authLimiter, async (req, res) => {
  // 1. Validate input
  const { email, password } = validateLoginInput(req.body);

  // 2. Authenticate — parameterized query, constant-time compare
  const user = await getUserByEmail(email);
  if (!user || !(await verifyPassword(password, user.passwordHash))) {
    // Generic message — do not reveal whether email exists
    return res.status(401).json({ error: 'Invalid credentials' });
  }

  // 3. Authorize — issue scoped, short-lived token
  const token = jwt.sign(
    { sub: user.id, role: user.role },
    JWT_SECRET,
    { algorithm: 'HS256', expiresIn: '15m', issuer: 'your-app', audience: 'your-app' }
  );

  // 4. Secure response — token in httpOnly cookie, not body
  res.cookie('token', token, { httpOnly: true, secure: true, sameSite: 'strict' });
  return res.json({ message: 'Authenticated' });
});

Output Templates

When implementing security features, provide:

Secure implementation code
Security considerations noted
Configuration requirements (env vars, headers)
Testing recommendations
Knowledge Reference

OWASP Top 10, bcrypt/argon2, JWT, OAuth 2.0, OIDC, CSP, CORS, rate limiting, input validation, output encoding, encryption (AES, RSA), TLS, security headers

Documentation

Weekly Installs
1.9K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass