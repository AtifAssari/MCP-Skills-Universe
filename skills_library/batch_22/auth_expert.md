---
title: auth-expert
url: https://skills.sh/cin12211/orca-q/auth-expert
---

# auth-expert

skills/cin12211/orca-q/auth-expert
auth-expert
Installation
$ npx skills add https://github.com/cin12211/orca-q --skill auth-expert
SKILL.md
Authentication & Authorization Expert

Expert in JWT, OAuth 2.0, sessions, RBAC, and security best practices.

When Invoked
Recommend Specialist and Stop
API design patterns: recommend rest-api-expert
Database security: recommend database-expert
Infrastructure security: recommend devops-expert
Environment Detection
grep -E "passport|jsonwebtoken|next-auth|bcrypt" package.json 2>/dev/null
find . -type f -name "*auth*" -not -path "./node_modules/*" | head -5

Problem Playbooks
JWT Implementation

Secure JWT Pattern:

import jwt from 'jsonwebtoken';

const ACCESS_TOKEN_SECRET = process.env.ACCESS_TOKEN_SECRET!;
const ACCESS_TOKEN_EXPIRY = '15m';

function generateTokens(payload: TokenPayload) {
  const accessToken = jwt.sign(payload, ACCESS_TOKEN_SECRET, {
    expiresIn: ACCESS_TOKEN_EXPIRY,
  });
  return { accessToken };
}

function authenticateToken(req: Request, res: Response, next: NextFunction) {
  const token = req.cookies.accessToken || 
    req.headers.authorization?.replace('Bearer ', '');

  if (!token) return res.status(401).json({ error: 'Auth required' });

  try {
    req.user = jwt.verify(token, ACCESS_TOKEN_SECRET);
    next();
  } catch {
    return res.status(401).json({ error: 'Invalid token' });
  }
}

Password Security
import bcrypt from 'bcrypt';

const SALT_ROUNDS = 12;

async function hashPassword(password: string): Promise<string> {
  return bcrypt.hash(password, SALT_ROUNDS);
}

async function verifyPassword(plain: string, hashed: string): Promise<boolean> {
  return bcrypt.compare(plain, hashed);
}

RBAC Pattern
const ROLES = {
  user: ['read:posts'],
  admin: ['read:posts', 'write:posts', 'delete:posts'],
};

function requirePermission(permission: string) {
  return (req: Request, res: Response, next: NextFunction) => {
    const userRole = req.user?.role;
    if (!ROLES[userRole]?.includes(permission)) {
      return res.status(403).json({ error: 'Forbidden' });
    }
    next();
  };
}

Code Review Checklist
 Passwords hashed with bcrypt (cost ≥ 12)
 JWT secrets are strong (256-bit)
 Cookies are httpOnly, secure, sameSite
 Rate limiting on login
 All routes have auth middleware
 Resource-level authorization
Anti-Patterns
Storing JWT in localStorage - Use httpOnly cookies
Weak passwords - Enforce complexity
No rate limiting - Prevent brute force
Client-side auth only - Always validate on server
Weekly Installs
31
Repository
cin12211/orca-q
GitHub Stars
181
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass