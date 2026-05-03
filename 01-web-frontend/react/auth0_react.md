---
rating: ⭐⭐⭐
title: auth0-react
url: https://skills.sh/auth0/agent-skills/auth0-react
---

# auth0-react

skills/auth0/agent-skills/auth0-react
auth0-react
Installation
$ npx skills add https://github.com/auth0/agent-skills --skill auth0-react
Summary

Authentication for React SPAs using Auth0 Universal Login with redirect-based flows.

Supports React 16–19 with Vite or Create React App; wraps your app with Auth0Provider and exposes hooks like useAuth0(), loginWithRedirect(), and logout()
Handles user sessions, access tokens, and profile data automatically; SDK manages secure token storage without manual localStorage handling
Includes protected routes, API token injection, and error handling patterns documented in the integration guide
Not suitable for Next.js, React Native, server-side rendering, or embedded login flows; use framework-specific skills instead
SKILL.md
Auth0 React Integration

Add authentication to React single-page applications using @auth0/auth0-react.

Prerequisites
React 16.11+ application (Vite or Create React App) - supports React 16, 17, 18, and 19
Auth0 account and application configured
If you don't have Auth0 set up yet, use the auth0-quickstart skill first
When NOT to Use
Next.js applications - Use auth0-nextjs skill for both App Router and Pages Router
React Native mobile apps - Use auth0-react-native skill for iOS/Android
Server-side rendered React - Use framework-specific SDK (Next.js, Remix, etc.)
Embedded login - This SDK uses Auth0 Universal Login (redirect-based)
Backend API authentication - Use express-openid-connect or JWT validation instead
Quick Start Workflow
1. Install SDK
npm install @auth0/auth0-react

2. Configure Environment

For automated setup with Auth0 CLI, see Setup Guide for complete scripts.

For manual setup:

Create .env file:

Vite:

VITE_AUTH0_DOMAIN=your-tenant.auth0.com
VITE_AUTH0_CLIENT_ID=your-client-id


Create React App:

REACT_APP_AUTH0_DOMAIN=your-tenant.auth0.com
REACT_APP_AUTH0_CLIENT_ID=your-client-id

3. Wrap App with Auth0Provider

Update src/main.tsx (Vite) or src/index.tsx (CRA):

import React from 'react';
import ReactDOM from 'react-dom/client';
import { Auth0Provider } from '@auth0/auth0-react';
import App from './App';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <Auth0Provider
      domain={import.meta.env.VITE_AUTH0_DOMAIN} // or process.env.REACT_APP_AUTH0_DOMAIN
      clientId={import.meta.env.VITE_AUTH0_CLIENT_ID}
      authorizationParams={{
        redirect_uri: window.location.origin
      }}
    >
      <App />
    </Auth0Provider>
  </React.StrictMode>
);

4. Add Authentication UI
import { useAuth0 } from '@auth0/auth0-react';

export function LoginButton() {
  const { loginWithRedirect, logout, isAuthenticated, user, isLoading } = useAuth0();

  if (isLoading) return <div>Loading...</div>;

  if (isAuthenticated) {
    return (
      <div>
        <span>Welcome, {user?.name}</span>
        <button onClick={() => logout({ logoutParams: { returnTo: window.location.origin } })}>
          Logout
        </button>
      </div>
    );
  }

  return <button onClick={() => loginWithRedirect()}>Login</button>;
}

5. Test Authentication

Start your dev server and test the login flow:

npm run dev  # Vite
# or
npm start    # CRA

Detailed Documentation
Setup Guide - Automated setup scripts (Bash/PowerShell), CLI commands, manual configuration
Integration Guide - Protected routes, API calls, error handling, advanced patterns
API Reference - Complete SDK API, configuration options, hooks reference, testing strategies
Common Mistakes
Mistake	Fix
Forgot to add redirect URI in Auth0 Dashboard	Add your application URL (e.g., http://localhost:3000, https://app.example.com) to Allowed Callback URLs in Auth0 Dashboard
Using wrong env var prefix	Vite uses VITE_ prefix, Create React App uses REACT_APP_
Not handling loading state	Always check isLoading before rendering auth-dependent UI
Storing tokens in localStorage	Never manually store tokens - SDK handles secure storage automatically
Missing Auth0Provider wrapper	Entire app must be wrapped in <Auth0Provider>
Provider not at root level	Auth0Provider must wrap all components that use auth hooks
Wrong import path for env vars	Vite uses import.meta.env.VITE_*, CRA uses process.env.REACT_APP_*
Using acr_values redirect for in-app MFA	Use useAuth0().mfa API for in-app enrollment/challenge/verify flows
Not catching MfaRequiredError	Wrap getAccessTokenSilently in try/catch and check instanceof MfaRequiredError
Making direct HTTP calls to MFA endpoints	Use the mfa property from useAuth0() — it handles token management automatically
Forgetting refresh tokens for step-up MFA	Set useRefreshTokens={true} on Auth0Provider when using interactiveErrorHandler="popup"
Related Skills
auth0-quickstart - Basic Auth0 setup
auth0-migration - Migrate from another auth provider
auth0-mfa - Add Multi-Factor Authentication
Quick Reference

Core Hooks:

useAuth0() - Main authentication hook
isAuthenticated - Check if user is logged in
user - User profile information
loginWithRedirect() - Initiate login
logout() - Log out user
getAccessTokenSilently() - Get access token for API calls
mfa - MFA API client for enrollment, challenge, and verification
mfa.getAuthenticators(mfaToken) - List enrolled authenticators
mfa.getEnrollmentFactors(mfaToken) - Get available enrollment factors
mfa.enroll(params) - Enroll new authenticator (OTP, SMS, Email, Voice, Push)
mfa.challenge(params) - Initiate MFA challenge
mfa.verify(params) - Verify MFA challenge and complete authentication

MFA Error Types (import from @auth0/auth0-react):

MfaRequiredError - Thrown by getAccessTokenSilently when MFA is needed (has mfa_token and mfa_requirements)
MfaEnrollmentError, MfaChallengeError, MfaVerifyError - Thrown by respective mfa.* methods

Common Use Cases:

Login/Logout buttons → See Step 4 above
Protected routes → Integration Guide
API calls with tokens → Integration Guide
Error handling → Integration Guide
MFA handling → Integration Guide
References
Auth0 React SDK Documentation
Auth0 React Quickstart
SDK GitHub Repository
Weekly Installs
742
Repository
auth0/agent-skills
GitHub Stars
18
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn