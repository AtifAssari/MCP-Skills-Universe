---
title: email-and-password-best-practices
url: https://skills.sh/better-auth/skills/email-and-password-best-practices
---

# email-and-password-best-practices

skills/better-auth/skills/email-and-password-best-practices
email-and-password-best-practices
Installation
$ npx skills add https://github.com/better-auth/skills --skill email-and-password-best-practices
Summary

Email verification, password reset flows, and customizable password policies for Better Auth.

Supports email verification with optional enforcement to block sign-in until verified, plus configurable token expiration and single-use reset tokens
Password reset flows with built-in security: background email sending, timing attack prevention, dummy operations on invalid requests, and optional session revocation on reset
Configurable password length limits (default 8–256 characters) and custom hashing algorithms via pluggable hash and verify functions
Requires absolute callback URLs and sendVerificationEmail / sendResetPassword functions to integrate with your email provider
SKILL.md
Quick Start
Enable email/password: emailAndPassword: { enabled: true }
Configure emailVerification.sendVerificationEmail
Add sendResetPassword for password reset flows
Run npx @better-auth/cli@latest migrate
Verify: attempt sign-up and confirm verification email triggers
Email Verification Setup

Configure emailVerification.sendVerificationEmail to verify user email addresses.

import { betterAuth } from "better-auth";
import { sendEmail } from "./email"; // your email sending function

export const auth = betterAuth({
  emailVerification: {
    sendVerificationEmail: async ({ user, url, token }, request) => {
      await sendEmail({
        to: user.email,
        subject: "Verify your email address",
        text: `Click the link to verify your email: ${url}`,
      });
    },
  },
});


Note: The url parameter contains the full verification link. The token is available if you need to build a custom verification URL.

Requiring Email Verification

For stricter security, enable emailAndPassword.requireEmailVerification to block sign-in until the user verifies their email. When enabled, unverified users will receive a new verification email on each sign-in attempt.

export const auth = betterAuth({
  emailAndPassword: {
    requireEmailVerification: true,
  },
});


Note: This requires sendVerificationEmail to be configured and only applies to email/password sign-ins.

Client Side Validation

Implement client-side validation for immediate user feedback and reduced server load.

Callback URLs

Always use absolute URLs (including the origin) for callback URLs in sign-up and sign-in requests. This prevents Better Auth from needing to infer the origin, which can cause issues when your backend and frontend are on different domains.

const { data, error } = await authClient.signUp.email({
  callbackURL: "https://example.com/callback", // absolute URL with origin
});

Password Reset Flows

Provide sendResetPassword in the email and password config to enable password resets.

import { betterAuth } from "better-auth";
import { sendEmail } from "./email"; // your email sending function

export const auth = betterAuth({
  emailAndPassword: {
    enabled: true,
    // Custom email sending function to send reset-password email
    sendResetPassword: async ({ user, url, token }, request) => {
      void sendEmail({
        to: user.email,
        subject: "Reset your password",
        text: `Click the link to reset your password: ${url}`,
      });
    },
    // Optional event hook
    onPasswordReset: async ({ user }, request) => {
      // your logic here
      console.log(`Password for user ${user.email} has been reset.`);
    },
  },
});

Security Considerations

Built-in protections: background email sending (timing attack prevention), dummy operations on invalid requests, constant response messages regardless of user existence.

On serverless platforms, configure a background task handler:

export const auth = betterAuth({
  advanced: {
    backgroundTasks: {
      handler: (promise) => {
        // Use platform-specific methods like waitUntil
        waitUntil(promise);
      },
    },
  },
});

Token Security

Tokens expire after 1 hour by default. Configure with resetPasswordTokenExpiresIn (in seconds):

export const auth = betterAuth({
  emailAndPassword: {
    enabled: true,
    resetPasswordTokenExpiresIn: 60 * 30, // 30 minutes
  },
});


Tokens are single-use — deleted immediately after successful reset.

Session Revocation

Enable revokeSessionsOnPasswordReset to invalidate all existing sessions on password reset:

export const auth = betterAuth({
  emailAndPassword: {
    enabled: true,
    revokeSessionsOnPasswordReset: true,
  },
});

Password Requirements

Password length limits (configurable):

export const auth = betterAuth({
  emailAndPassword: {
    enabled: true,
    minPasswordLength: 12,
    maxPasswordLength: 256,
  },
});

Sending the Password Reset

Call requestPasswordReset to send the reset link. Triggers the sendResetPassword function from your config.

const data = await auth.api.requestPasswordReset({
  body: {
    email: "john.doe@example.com", // required
    redirectTo: "https://example.com/reset-password",
  },
});


Or authClient:

const { data, error } = await authClient.requestPasswordReset({
  email: "john.doe@example.com", // required
  redirectTo: "https://example.com/reset-password",
});


Note: While the email is required, we also recommend configuring the redirectTo for a smoother user experience.

Password Hashing

Default: scrypt (Node.js native, no external dependencies).

Custom Hashing Algorithm

To use Argon2id or another algorithm, provide custom hash and verify functions:

import { betterAuth } from "better-auth";
import { hash, verify, type Options } from "@node-rs/argon2";

const argon2Options: Options = {
  memoryCost: 65536, // 64 MiB
  timeCost: 3, // 3 iterations
  parallelism: 4, // 4 parallel lanes
  outputLen: 32, // 32 byte output
  algorithm: 2, // Argon2id variant
};

export const auth = betterAuth({
  emailAndPassword: {
    enabled: true,
    password: {
      hash: (password) => hash(password, argon2Options),
      verify: ({ password, hash: storedHash }) =>
        verify(storedHash, password, argon2Options),
    },
  },
});


Note: If you switch hashing algorithms on an existing system, users with passwords hashed using the old algorithm won't be able to sign in. Plan a migration strategy if needed.

Weekly Installs
13.8K
Repository
better-auth/skills
GitHub Stars
187
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass