---
title: api integration specialist
url: https://skills.sh/davila7/claude-code-templates/api-integration-specialist
---

# api integration specialist

skills/davila7/claude-code-templates/API Integration Specialist
API Integration Specialist
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill 'API Integration Specialist'
Summary

Production-ready patterns for authenticating, transforming, and reliably integrating third-party APIs.

Covers authentication methods including API keys, OAuth 2.0, and JWT with secure credential management
Provides structured error handling, exponential backoff retry logic, and client-side rate limiting with configurable windows
Includes webhook verification via HMAC signatures, request/response transformation, and pagination handling patterns
Demonstrates REST client patterns, timeout management, and circuit breaker concepts for fault tolerance
Includes practical examples for Stripe, SendGrid, and Twilio integrations with troubleshooting guidance for auth, rate limits, and timeouts
SKILL.md
API Integration Specialist

Expert guidance for integrating external APIs into applications with production-ready patterns, security best practices, and comprehensive error handling.

When to Use This Skill

Use this skill when:

Integrating third-party APIs (Stripe, Twilio, SendGrid, etc.)
Building API client libraries or wrappers
Implementing OAuth 2.0, API keys, or JWT authentication
Setting up webhooks and event-driven integrations
Handling rate limits, retries, and circuit breakers
Transforming API responses for application use
Debugging API integration issues
Core Integration Principles
1. Authentication & Security

API Key Management:

// Store keys in environment variables, never in code
const apiClient = new APIClient({
  apiKey: process.env.SERVICE_API_KEY,
  baseURL: process.env.SERVICE_BASE_URL
});


OAuth 2.0 Flow:

// Authorization Code Flow
const oauth = new OAuth2Client({
  clientId: process.env.CLIENT_ID,
  clientSecret: process.env.CLIENT_SECRET,
  redirectUri: process.env.REDIRECT_URI,
  scopes: ['read:users', 'write:data']
});

// Get authorization URL
const authUrl = oauth.getAuthorizationUrl();

// Exchange code for tokens
const tokens = await oauth.exchangeCode(code);

2. Request/Response Handling

Standardized Request Structure:

async function makeRequest(endpoint, options = {}) {
  const defaultHeaders = {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${apiKey}`,
    'User-Agent': 'MyApp/1.0.0'
  };

  const response = await fetch(`${baseURL}${endpoint}`, {
    ...options,
    headers: { ...defaultHeaders, ...options.headers }
  });

  if (!response.ok) {
    throw new APIError(response.status, await response.json());
  }

  return response.json();
}


Response Transformation:

class APIClient {
  async getUser(userId) {
    const raw = await this.request(`/users/${userId}`);

    // Transform external API format to internal model
    return {
      id: raw.user_id,
      email: raw.email_address,
      name: `${raw.first_name} ${raw.last_name}`,
      createdAt: new Date(raw.created_timestamp)
    };
  }
}

3. Error Handling

Structured Error Types:

class APIError extends Error {
  constructor(status, body) {
    super(`API Error: ${status}`);
    this.status = status;
    this.body = body;
    this.isAPIError = true;
  }

  isRateLimited() {
    return this.status === 429;
  }

  isUnauthorized() {
    return this.status === 401;
  }

  isServerError() {
    return this.status >= 500;
  }
}


Retry Logic with Exponential Backoff:

async function retryWithBackoff(fn, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fn();
    } catch (error) {
      if (!error.isAPIError || !error.isServerError()) {
        throw error; // Don't retry client errors
      }

      if (i === maxRetries - 1) throw error;

      const delay = Math.pow(2, i) * 1000; // 1s, 2s, 4s
      await sleep(delay);
    }
  }
}

4. Rate Limiting

Client-Side Rate Limiter:

class RateLimiter {
  constructor(maxRequests, windowMs) {
    this.maxRequests = maxRequests;
    this.windowMs = windowMs;
    this.requests = [];
  }

  async acquire() {
    const now = Date.now();
    this.requests = this.requests.filter(t => now - t < this.windowMs);

    if (this.requests.length >= this.maxRequests) {
      const oldestRequest = this.requests[0];
      const waitTime = this.windowMs - (now - oldestRequest);
      await sleep(waitTime);
      return this.acquire();
    }

    this.requests.push(now);
  }
}

const limiter = new RateLimiter(100, 60000); // 100 requests per minute

async function rateLimitedRequest(endpoint, options) {
  await limiter.acquire();
  return makeRequest(endpoint, options);
}

5. Webhook Handling

Webhook Verification:

function verifyWebhookSignature(payload, signature, secret) {
  const expectedSignature = crypto
    .createHmac('sha256', secret)
    .update(payload)
    .digest('hex');

  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(expectedSignature)
  );
}

app.post('/webhooks/stripe', express.raw({ type: 'application/json' }), (req, res) => {
  const signature = req.headers['stripe-signature'];

  if (!verifyWebhookSignature(req.body, signature, process.env.STRIPE_WEBHOOK_SECRET)) {
    return res.status(401).send('Invalid signature');
  }

  const event = JSON.parse(req.body);
  handleWebhookEvent(event);

  res.status(200).send('Received');
});

Integration Patterns
REST API Client Pattern
class ServiceAPIClient {
  constructor(config) {
    this.apiKey = config.apiKey;
    this.baseURL = config.baseURL;
    this.timeout = config.timeout || 30000;
  }

  async request(method, endpoint, data = null) {
    const options = {
      method,
      headers: {
        'Authorization': `Bearer ${this.apiKey}`,
        'Content-Type': 'application/json'
      },
      timeout: this.timeout
    };

    if (data) {
      options.body = JSON.stringify(data);
    }

    const response = await retryWithBackoff(() =>
      fetch(`${this.baseURL}${endpoint}`, options)
    );

    return response.json();
  }

  // Resource methods
  async getResource(id) {
    return this.request('GET', `/resources/${id}`);
  }

  async createResource(data) {
    return this.request('POST', '/resources', data);
  }

  async updateResource(id, data) {
    return this.request('PUT', `/resources/${id}`, data);
  }

  async deleteResource(id) {
    return this.request('DELETE', `/resources/${id}`);
  }
}

Pagination Handling
async function* fetchAllPages(endpoint, pageSize = 100) {
  let cursor = null;

  do {
    const params = new URLSearchParams({
      limit: pageSize,
      ...(cursor && { cursor })
    });

    const response = await apiClient.request('GET', `${endpoint}?${params}`);

    yield response.data;

    cursor = response.pagination?.next_cursor;
  } while (cursor);
}

// Usage
for await (const page of fetchAllPages('/users')) {
  processUsers(page);
}

Best Practices
Security
Store API keys in environment variables or secrets management
Use HTTPS for all API calls
Verify webhook signatures
Implement request signing for sensitive operations
Rotate API keys regularly
Reliability
Implement exponential backoff retry logic
Handle rate limits gracefully
Set appropriate timeouts
Use circuit breakers for failing services
Log all API interactions for debugging
Performance
Cache responses when appropriate
Batch requests when the API supports it
Use streaming for large responses
Implement connection pooling
Monitor API usage and costs
Monitoring
Track API response times
Alert on error rate increases
Monitor rate limit consumption
Log failed requests with context
Set up health checks for critical integrations
Common Integration Examples
Stripe Payment Processing
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

async function createPaymentIntent(amount, currency = 'usd') {
  return await stripe.paymentIntents.create({
    amount,
    currency,
    automatic_payment_methods: { enabled: true }
  });
}

SendGrid Email Sending
const sgMail = require('@sendgrid/mail');
sgMail.setApiKey(process.env.SENDGRID_API_KEY);

async function sendEmail(to, subject, html) {
  await sgMail.send({
    to,
    from: process.env.FROM_EMAIL,
    subject,
    html
  });
}

Twilio SMS
const twilio = require('twilio')(
  process.env.TWILIO_ACCOUNT_SID,
  process.env.TWILIO_AUTH_TOKEN
);

async function sendSMS(to, body) {
  await twilio.messages.create({
    to,
    from: process.env.TWILIO_PHONE_NUMBER,
    body
  });
}

Troubleshooting
Authentication Issues
Verify API keys are correctly set
Check token expiration
Ensure proper OAuth scopes
Validate signature generation
Rate Limiting
Implement client-side rate limiting
Use batch endpoints when available
Spread requests over time
Consider upgrading API tier
Timeout Errors
Increase timeout values for slow endpoints
Implement request cancellation
Use streaming for large payloads
Check network connectivity

When integrating APIs, prioritize security, reliability, and maintainability. Always test error scenarios and edge cases before production deployment.

Weekly Installs
–
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn