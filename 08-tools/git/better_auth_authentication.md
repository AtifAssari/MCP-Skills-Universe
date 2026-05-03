---
rating: ⭐⭐
title: better-auth-authentication
url: https://skills.sh/bobmatnyc/claude-mpm-skills/better-auth-authentication
---

# better-auth-authentication

skills/bobmatnyc/claude-mpm-skills/better-auth-authentication
better-auth-authentication
Installation
$ npx skills add https://github.com/bobmatnyc/claude-mpm-skills --skill better-auth-authentication
SKILL.md
Better Auth Authentication
Goals
Enable email/password authentication and social providers.
Implement sign-up, sign-in, sign-out, and verification flows.
Handle redirects and errors consistently.
Quick start
Enable emailAndPassword and configure socialProviders.
Create a client with createAuthClient.
Use signUp.email, signIn.email, signIn.social, and signOut on the client.
import { betterAuth } from "better-auth";

export const auth = betterAuth({
  emailAndPassword: { enabled: true },
  socialProviders: {
    github: {
      clientId: process.env.GITHUB_CLIENT_ID as string,
      clientSecret: process.env.GITHUB_CLIENT_SECRET as string,
    },
  },
});

import { createAuthClient } from "better-auth/client";

const authClient = createAuthClient();

await authClient.signUp.email({
  email,
  password,
  name,
});

await authClient.signIn.email({
  email,
  password,
  callbackURL: "/dashboard",
});

await authClient.signIn.social({
  provider: "github",
  callbackURL: "/dashboard",
});

await authClient.signOut();

Email verification
Provide emailVerification.sendVerificationEmail to send the verification link.
Use emailAndPassword.requireEmailVerification to enforce verification before sign-in.
Social providers
Configure providers in socialProviders with provider-specific credentials.
Use signIn.social to start OAuth flows.
Pass callbackURL, errorCallbackURL, and newUserCallbackURL for redirects.
Guardrails
Call client methods from the client only.
Keep secrets in server-only env variables.
Use rememberMe to control persistent sessions on email/password sign-in.
References
toolchains/platforms/auth/better-auth/better-auth-authentication/references/email-password.md
toolchains/platforms/auth/better-auth/better-auth-authentication/references/providers.md
Weekly Installs
168
Repository
bobmatnyc/claud…m-skills
GitHub Stars
40
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass