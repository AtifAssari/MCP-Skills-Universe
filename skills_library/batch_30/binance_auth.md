---
title: binance-auth
url: https://skills.sh/ticruz38/skills/binance-auth
---

# binance-auth

skills/ticruz38/skills/binance-auth
binance-auth
Installation
$ npx skills add https://github.com/ticruz38/skills --skill binance-auth
SKILL.md
Binance Auth Skill

Authentication skill for Binance cryptocurrency exchange API. Built on top of auth-provider for secure API key storage and management. Supports both Binance production and testnet environments.

Features
Secure API Key Storage: Encrypted storage of API keys and secrets
Environment Toggle: Switch between production and testnet seamlessly
Permission Validation: Verify API key permissions (spot, margin, futures)
Health Checks: Validate API connectivity and key status
Multi-Profile: Support multiple Binance accounts
Balance Queries: Check account balances as part of health validation
Installation
npm install
npm run build

Environment Variables

No environment variables required - API keys are configured per-profile via CLI.

CLI Usage
View Status
node dist/cli.js status

Connect API Key
# Production environment
node dist/cli.js connect prod \
  --key YOUR_API_KEY \
  --secret YOUR_API_SECRET \
  --env production

# Testnet environment
node dist/cli.js connect test \
  --key YOUR_API_KEY \
  --secret YOUR_API_SECRET \
  --env testnet

Health Check
# Check specific profile
node dist/cli.js health prod

# Check all profiles
node dist/cli.js health

List Profiles
node dist/cli.js list

Get Balance
node dist/cli.js balance prod

Validate Permissions
node dist/cli.js validate prod

Disconnect
node dist/cli.js disconnect prod

JavaScript/TypeScript API
Initialize Client
import { BinanceAuthClient, getBinanceAuth } from '@openclaw/binance-auth';

// Create client for specific profile
const binance = new BinanceAuthClient('prod');

// Or use singleton
const binance = getBinanceAuth('prod');

Connect API Key
const result = await binance.connect({
  apiKey: 'your-api-key',
  apiSecret: 'your-api-secret',
  environment: 'production', // or 'testnet'
});

if (result.success) {
  console.log('Connected! Permissions:', result.permissions);
}

Check Connection
const isConnected = await binance.isConnected();
console.log('Connected:', isConnected);

Get API Credentials
const credentials = await binance.getCredentials();
if (credentials) {
  console.log('API Key:', credentials.apiKey);
  console.log('Environment:', credentials.environment);
}

Health Check
const health = await binance.healthCheck();
console.log('Status:', health.status); // 'healthy' | 'unhealthy'
console.log('Message:', health.message);

Get Account Balance
const balance = await binance.getBalance();
if (balance) {
  console.log('Total BTC:', balance.totalBTC);
  console.log('Balances:', balance.balances);
  console.log('Permissions:', balance.permissions);
}

Validate Permissions
const validation = await binance.validatePermissions();
console.log('Valid:', validation.valid);
console.log('Can Trade:', validation.canTrade);
console.log('Can Withdraw:', validation.canWithdraw);
console.log('Permissions:', validation.permissions);

Disconnect
const disconnected = await binance.disconnect();
console.log('Disconnected:', disconnected);

API Permissions

Binance API keys can have the following permissions:

SPOT - Spot trading
MARGIN - Margin trading
FUTURES - Futures trading
DELIVERY - Coin-margined futures
PERM - Permanent API key
IP_RESTRICTED - IP-restricted access
Environments
Production
API Base: https://api.binance.com
Real trading with real funds
Requires verified Binance account
Testnet
API Base: https://testnet.binance.vision
Paper trading with test funds
Free testnet registration at: https://testnet.binance.vision/
Storage Location

Credentials are stored in the auth-provider database:

~/.openclaw/skills/auth-provider/credentials.db


API keys are encrypted with AES-256.

TypeScript Types
interface BinanceCredentials {
  apiKey: string;
  apiSecret: string;
  environment: 'production' | 'testnet';
  permissions?: string[];
}

interface BinanceConnectionResult {
  success: boolean;
  permissions?: string[];
  canTrade?: boolean;
  canWithdraw?: boolean;
  error?: string;
}

interface BinanceBalance {
  totalBTC: string;
  balances: Array<{
    asset: string;
    free: string;
    locked: string;
  }>;
  permissions: string[];
}

interface BinanceValidationResult {
  valid: boolean;
  permissions: string[];
  canTrade: boolean;
  canWithdraw: boolean;
}

Error Handling
try {
  await binance.connect({ apiKey, apiSecret, environment: 'production' });
} catch (error) {
  if (error.message.includes('Invalid API key')) {
    // API key format is invalid
  } else if (error.message.includes('API key validation failed')) {
    // Key rejected by Binance
  }
}

Security Notes
API secrets are never exposed after storage
All API calls use HMAC-SHA256 signatures
Database file has 0600 permissions (user read/write only)
Use IP restrictions on your Binance API keys for added security
Never commit API credentials to version control
Testing
# Type checking
npm run typecheck

# Build
npm run build

# Run CLI
npm run cli -- status

Dependencies
@openclaw/auth-provider - Secure credential storage
Uses crypto module for HMAC-SHA256 signatures
Weekly Installs
45
Repository
ticruz38/skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail