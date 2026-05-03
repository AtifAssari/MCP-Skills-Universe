---
rating: ⭐⭐
title: b2c-slas-auth-patterns
url: https://skills.sh/salesforcecommercecloud/b2c-developer-tooling/b2c-slas-auth-patterns
---

# b2c-slas-auth-patterns

skills/salesforcecommercecloud/b2c-developer-tooling/b2c-slas-auth-patterns
b2c-slas-auth-patterns
Installation
$ npx skills add https://github.com/salesforcecommercecloud/b2c-developer-tooling --skill b2c-slas-auth-patterns
SKILL.md
B2C SLAS Authentication Patterns

Advanced authentication patterns for SLAS (Shopper Login and API Access Service) beyond basic login. These patterns enable passwordless authentication, hybrid storefront support, and system-to-system integration.

Authentication Methods Overview
Method	Use Case	User Experience
Password	Traditional login	Username + password form
Email OTP	Passwordless email	Code sent to email
SMS OTP	Passwordless SMS	Code sent to phone
Passkeys	FIDO2/WebAuthn	Biometric or device PIN
Session Bridge	Hybrid storefronts	Seamless PWA ↔ SFRA
Hybrid Auth	B2C 25.3+	Built-in platform auth sync
TSOB	System integration	Backend service calls
Passwordless Email OTP

Send one-time passwords via email for passwordless login.

Flow Overview
Call /oauth2/passwordless/login with callback URI
SLAS POSTs pwdless_login_token to your callback
Your app sends OTP to shopper via email
Shopper enters OTP, app exchanges for tokens
Step 1: Initiate Passwordless Login
// POST /shopper/auth/v1/organizations/{org}/oauth2/passwordless/login
async function initiatePasswordlessLogin(email, siteId) {
    const response = await fetch(
        `https://${shortCode}.api.commercecloud.salesforce.com/shopper/auth/v1/organizations/${orgId}/oauth2/passwordless/login`,
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams({
                user_id: email,
                mode: 'callback',
                channel_id: siteId,
                callback_uri: 'https://yoursite.com/api/passwordless/callback'
            })
        }
    );

    // SLAS will POST to your callback_uri with pwdless_login_token
    return response.json();
}

Step 2: Handle Callback and Send OTP

Your callback endpoint receives pwdless_login_token. Generate an OTP and send it to the user:

// Your callback endpoint (receives POST from SLAS)
app.post('/api/passwordless/callback', async (req, res) => {
    const { pwdless_login_token, user_id } = req.body;

    // Generate 6-digit OTP
    const otp = Math.floor(100000 + Math.random() * 900000).toString();

    // Store token + OTP mapping (e.g., Redis with 10 min TTL)
    await redis.setex(`pwdless:${otp}`, 600, JSON.stringify({
        token: pwdless_login_token,
        email: user_id
    }));

    // Send OTP via email (configure in SLAS Admin UI)
    await sendOTPEmail(user_id, otp);

    res.status(200).send('OK');
});

Step 3: Exchange OTP for Tokens
// POST /shopper/auth/v1/organizations/{org}/oauth2/passwordless/token
async function exchangeOTPForToken(otp, clientId, clientSecret, siteId) {
    // Retrieve stored token
    const stored = JSON.parse(await redis.get(`pwdless:${otp}`));
    if (!stored) throw new Error('Invalid or expired OTP');

    const response = await fetch(
        `https://${shortCode}.api.commercecloud.salesforce.com/shopper/auth/v1/organizations/${orgId}/oauth2/passwordless/token`,
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': `Basic ${btoa(clientId + ':' + clientSecret)}`
            },
            body: new URLSearchParams({
                grant_type: 'client_credentials',
                hint: 'pwdless_login',
                pwdless_login_token: stored.token,
                channel_id: siteId
            })
        }
    );

    // Returns: { access_token, refresh_token, ... }
    return response.json();
}

Rate Limits
6 requests per user per 10 minutes
1,000 requests/month per endpoint on non-production tenants
Passwordless SMS OTP

Send OTP via SMS using Marketing Cloud or custom integration.

Using Marketing Cloud

Configure SMS through Salesforce Marketing Cloud:

Set up Marketing Cloud connector
Configure SMS journey with OTP template
Trigger via SLAS callback (same flow as email OTP)
Custom SMS Provider

Use the same callback flow as email, but send via SMS provider:

// In your callback handler
const twilio = require('twilio')(accountSid, authToken);

async function sendOTPSMS(phoneNumber, otp) {
    await twilio.messages.create({
        body: `Your login code is: ${otp}`,
        from: '+1234567890',
        to: phoneNumber
    });
}

Passkeys (FIDO2/WebAuthn)

Enable biometric authentication using FIDO2/WebAuthn passkeys. Registration requires prior identity verification via OTP. The flow involves starting registration with SLAS, creating a credential via the browser WebAuthn API, then completing registration. Authentication follows a similar start/authenticate/finish pattern.

See references/PASSKEYS.md for full registration and authentication code examples.

Session Bridge

Maintain session continuity between PWA Kit and SFRA storefronts using signed bridge tokens (dwsgst for guest, dwsrst for registered). Supports both PWA-to-SFRA and SFRA-to-PWA directions. Note that DWSID is deprecated for registered shoppers.

See references/SESSION-BRIDGE.md for full implementation details including token generation, redirect patterns, callback handlers, and error handling.

Hybrid Authentication (B2C 25.3+)

Hybrid Auth replaces Plugin SLAS for hybrid PWA/SFRA storefronts. It's built directly into the B2C platform and provides automatic session synchronization.

Benefits
No manual session bridge implementation needed
Automatic sync between PWA and SFRA
Simplified token management
Built-in platform support
Migration from Plugin SLAS

If using Plugin SLAS, migrate to Hybrid Auth:

Upgrade to B2C Commerce 25.3+
Enable Hybrid Auth in Business Manager
Remove Plugin SLAS cartridge
Update storefront to use platform auth
Token Refresh

Important: The channel_id parameter is required for guest token refresh.

Public Clients (Single-Use Refresh)

Public clients (no secret) receive single-use refresh tokens:

async function refreshTokenPublic(refreshToken, clientId, siteId) {
    const response = await fetch(
        `https://${shortCode}.api.commercecloud.salesforce.com/shopper/auth/v1/organizations/${orgId}/oauth2/token`,
        {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams({
                grant_type: 'refresh_token',
                refresh_token: refreshToken,
                client_id: clientId,
                channel_id: siteId  // REQUIRED
            })
        }
    );

    // Returns NEW refresh_token (old one is invalidated)
    return response.json();
}

Private Clients (Reusable Refresh)

Private clients can reuse refresh tokens:

async function refreshTokenPrivate(refreshToken, clientId, clientSecret, siteId) {
    const response = await fetch(
        `https://${shortCode}.api.commercecloud.salesforce.com/shopper/auth/v1/organizations/${orgId}/oauth2/token`,
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': `Basic ${btoa(clientId + ':' + clientSecret)}`
            },
            body: new URLSearchParams({
                grant_type: 'refresh_token',
                refresh_token: refreshToken,
                channel_id: siteId  // REQUIRED
            })
        }
    );

    // Same refresh_token can be used again
    return response.json();
}

Trusted System on Behalf (TSOB)

Server-to-server authentication to act on behalf of a shopper.

Use Cases
Backend services accessing shopper data
Order management systems
Customer service applications
Get Token on Behalf of Shopper
async function getTSOBToken(shopperLoginId) {
    const response = await fetch(
        `https://${shortCode}.api.commercecloud.salesforce.com/shopper/auth/v1/organizations/${orgId}/oauth2/trusted-system/token`,
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': `Basic ${btoa(clientId + ':' + clientSecret)}`
            },
            body: new URLSearchParams({
                grant_type: 'client_credentials',
                login_id: shopperLoginId,
                channel_id: siteId,
                usid: shopperUsid // Optional: reuse existing session
            })
        }
    );

    // Returns tokens that act as the specified shopper
    return response.json();
}

Important Constraints

3-Second Protection Window: Multiple TSOB calls for the same shopper within 3 seconds return HTTP 409:

"Tenant id <id> has already performed a login operation for user id <user_id> in the last 3 seconds."


Handle this in your code:

async function getTSOBTokenWithRetry(shopperLoginId, maxRetries = 3) {
    for (let i = 0; i < maxRetries; i++) {
        try {
            return await getTSOBToken(shopperLoginId);
        } catch (error) {
            if (error.status === 409 && i < maxRetries - 1) {
                await new Promise(r => setTimeout(r, 3000));
                continue;
            }
            throw error;
        }
    }
}

Required Configuration
SLAS client must have TSOB enabled (sfcc.ts_ext_on_behalf_of scope)
Configure in SLAS Admin API or Business Manager
Secure the client secret (server-side only)
Keep login_id length under 60 characters
JWT Validation

Validate SLAS tokens using JWKS (JSON Web Key Set).

Get JWKS
async function getJWKS() {
    const response = await fetch(
        `https://${shortCode}.api.commercecloud.salesforce.com/shopper/auth/v1/organizations/${orgId}/oauth2/jwks`
    );
    return response.json();
}

Validate Token
const jose = require('jose');

async function validateToken(accessToken) {
    // Get JWKS
    const jwksUrl = `https://${shortCode}.api.commercecloud.salesforce.com/shopper/auth/v1/organizations/${orgId}/oauth2/jwks`;
    const JWKS = jose.createRemoteJWKSet(new URL(jwksUrl));

    // Verify token
    const { payload } = await jose.jwtVerify(accessToken, JWKS, {
        issuer: `https://${shortCode}.api.commercecloud.salesforce.com/shopper/auth/v1/organizations/${orgId}`,
        audience: clientId
    });

    return payload;
}

Token Claims
Claim	Description
sub	Subject (customer ID or guest ID)
isb	Identity subject binding
iss	Issuer
aud	Audience (client ID)
exp	Expiration time
iat	Issued at time
scope	Granted scopes
tsob	TSOB token type (for trusted system tokens)
Best Practices
Security
Never expose client secrets in frontend code
Use HTTPS for all token exchanges
Validate tokens server-side for sensitive operations
Implement proper CORS policies
Store tokens securely (httpOnly cookies preferred)
Token Management
Implement proactive token refresh before expiry
Handle refresh token rotation for public clients
Clear tokens on logout from all storage locations
Use short-lived access tokens where possible
Always include channel_id in refresh requests
User Experience
Provide fallback authentication methods
Show clear error messages for auth failures
Remember user's preferred auth method
Handle session expiry gracefully
Detailed References
Passkeys (FIDO2/WebAuthn) - Registration and authentication code examples
Session Bridge Flows - Detailed session bridge implementation
Token Lifecycle - Token expiry and refresh patterns
Weekly Installs
88
Repository
salesforcecomme…-tooling
GitHub Stars
39
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass