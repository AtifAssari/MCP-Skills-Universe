---
title: security-vite
url: https://skills.sh/igorwarzocha/opencode-workflows/security-vite
---

# security-vite

skills/igorwarzocha/opencode-workflows/security-vite
security-vite
Installation
$ npx skills add https://github.com/igorwarzocha/opencode-workflows --skill security-vite
SKILL.md

Security audit patterns for Vite applications focusing on environment variable exposure, build-time secrets, and SPA-specific vulnerabilities.

Environment Variable Exposure
The VITE_ Footgun
VITE_*    → Bundled into client JavaScript → Visible to everyone
No prefix → Only available in vite.config.ts → Safe for secrets


Audit steps:

grep -r "VITE_" . -g "*.env*"
Check import.meta.env.VITE_* usage in source
Common mistakes:
VITE_API_SECRET (SHOULD be server-only)
VITE_DATABASE_URL (MUST NOT use)
VITE_STRIPE_SECRET_KEY (only publishable keys)
Env Files Priority

Vite loads in this order (later overrides earlier):

.env                # Always loaded
.env.local          # Always loaded, gitignored
.env.[mode]         # e.g., .env.production
.env.[mode].local   # e.g., .env.production.local, gitignored


Check: Are .env.local and .env.*.local in .gitignore?

envPrefix Overrides

If envPrefix is configured, Vite exposes any variables with those prefixes. Treat envPrefix as a security-sensitive setting.

Build-Time vs Runtime
Dangerous: Secrets in vite.config.ts
// ❌ Secret in config (ends up in bundle)
export default defineConfig({
  define: {
    'process.env.API_KEY': JSON.stringify(process.env.API_KEY),
  },
});

// The above makes API_KEY available in client code!

Safe Pattern
// Only use VITE_ prefix for truly public values
export default defineConfig({
  define: {
    '__APP_VERSION__': JSON.stringify(process.env.npm_package_version),
  },
});

// Keep secrets on server (use a backend API)

Dev Server Security
Open to Network
// ❌ Exposes dev server to network
export default defineConfig({
  server: {
    host: '0.0.0.0',  // or host: true
  },
});


This is dangerous on shared networks. Check if intentional.

Proxy Misconfiguration
export default defineConfig({
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:3000',
        changeOrigin: true,
        // ❌ Missing secure options for production-like setup
      },
    },
  },
});

SPA Security Issues
Client-Side Auth Only
// ❌ "Protection" only in React Router
const ProtectedRoute = ({ children }) => {
  const { user } = useAuth();
  if (!user) return <Navigate to="/login" />;
  return children;
};

// API calls still need server-side auth!
// This is UI convenience, not security.

Secrets in Bundle
# Check the built bundle for secrets
rg -a "(sk_live|sk_test|AKIA|api[_-]?key)" dist/

Source Maps in Production
// Check vite.config.ts
export default defineConfig({
  build: {
    sourcemap: true,  // ❌ Exposes source code in production
  },
});


<severity_table>

Common Vulnerabilities
Issue	Where to Look	Severity
VITE_* secrets	.env*, source files	CRITICAL
Secrets in define	vite.config.ts	CRITICAL
Source maps in prod	vite.config.ts	MEDIUM
Dev server exposed	vite.config.ts server.host	MEDIUM
Client-only auth	Route guards without API auth	HIGH
API keys in bundle	dist/ directory	CRITICAL

</severity_table>

Quick Audit Commands
# Find VITE_ secrets
grep -r "VITE_" . -g "*.env*"

# Find import.meta.env usage
rg 'import\.meta\.env' . -g "*.ts" -g "*.tsx" -g "*.vue"

# Check define in config
rg 'define:' vite.config.*

# Scan built bundle for secrets
rg -a "(sk_live|AKIA|ghp_|api[_-]?key['\"]?\s*[:=])" dist/

# Check for source maps
fd '\.map$' dist/

Hardening Checklist
 No secrets in VITE_* variables
 .env.local and .env.*.local in .gitignore
 sourcemap: false in production build
 server.host is not 0.0.0.0 or true (unless intentional)
 All sensitive API calls go through a backend (not direct from browser)
 No secrets in vite.config.ts define block
Weekly Installs
41
Repository
igorwarzocha/op…orkflows
GitHub Stars
111
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass