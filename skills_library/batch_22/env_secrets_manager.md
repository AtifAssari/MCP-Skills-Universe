---
title: env-secrets-manager
url: https://skills.sh/patricio0312rev/skills/env-secrets-manager
---

# env-secrets-manager

skills/patricio0312rev/skills/env-secrets-manager
env-secrets-manager
Installation
$ npx skills add https://github.com/patricio0312rev/skills --skill env-secrets-manager
SKILL.md
Environment Secrets Manager

Securely manage secrets and environment variables across environments.

Core Workflow
Identify secrets: Classify sensitive data
Choose provider: Select secrets manager
Configure storage: Encrypted storage
Implement access: Secure retrieval
Setup rotation: Automatic key rotation
Audit access: Monitor usage
Local Development
Environment Files
# .env.example (commit this)
DATABASE_URL=postgresql://user:password@localhost:5432/mydb
REDIS_URL=redis://localhost:6379
API_KEY=your-api-key-here
JWT_SECRET=your-jwt-secret-here

# AWS
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=us-east-1

# Third-party services
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...

# .env.local (never commit)
DATABASE_URL=postgresql://user:actualpassword@localhost:5432/mydb
JWT_SECRET=super-secret-jwt-key-that-is-long-enough
STRIPE_SECRET_KEY=sk_test_actual_key

# .gitignore
.env
.env.local
.env.*.local
.env.production
*.pem
*.key
secrets/

Environment Validation
// config/env.ts
import { z } from 'zod';

const envSchema = z.object({
  NODE_ENV: z.enum(['development', 'test', 'production']).default('development'),
  PORT: z.coerce.number().default(3000),

  // Database
  DATABASE_URL: z.string().url(),

  // Redis
  REDIS_URL: z.string().url().optional(),

  // Authentication
  JWT_SECRET: z.string().min(32),
  JWT_EXPIRES_IN: z.string().default('7d'),

  // AWS (optional in development)
  AWS_ACCESS_KEY_ID: z.string().optional(),
  AWS_SECRET_ACCESS_KEY: z.string().optional(),
  AWS_REGION: z.string().default('us-east-1'),

  // External Services
  STRIPE_SECRET_KEY: z.string().startsWith('sk_'),
  STRIPE_WEBHOOK_SECRET: z.string().startsWith('whsec_'),
});

export type Env = z.infer<typeof envSchema>;

function validateEnv(): Env {
  const result = envSchema.safeParse(process.env);

  if (!result.success) {
    console.error('❌ Invalid environment variables:');
    console.error(result.error.format());
    throw new Error('Invalid environment configuration');
  }

  return result.data;
}

export const env = validateEnv();

T3 Env Pattern
// env.mjs (for Next.js)
import { createEnv } from '@t3-oss/env-nextjs';
import { z } from 'zod';

export const env = createEnv({
  server: {
    DATABASE_URL: z.string().url(),
    JWT_SECRET: z.string().min(32),
    STRIPE_SECRET_KEY: z.string().startsWith('sk_'),
  },
  client: {
    NEXT_PUBLIC_API_URL: z.string().url(),
    NEXT_PUBLIC_STRIPE_KEY: z.string().startsWith('pk_'),
  },
  runtimeEnv: {
    DATABASE_URL: process.env.DATABASE_URL,
    JWT_SECRET: process.env.JWT_SECRET,
    STRIPE_SECRET_KEY: process.env.STRIPE_SECRET_KEY,
    NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL,
    NEXT_PUBLIC_STRIPE_KEY: process.env.NEXT_PUBLIC_STRIPE_KEY,
  },
});

AWS Secrets Manager
// lib/secrets/aws.ts
import {
  SecretsManagerClient,
  GetSecretValueCommand,
  CreateSecretCommand,
  UpdateSecretCommand,
  RotateSecretCommand,
} from '@aws-sdk/client-secrets-manager';

const client = new SecretsManagerClient({
  region: process.env.AWS_REGION,
});

// Cache for secrets
const secretsCache = new Map<string, { value: any; expiresAt: number }>();
const CACHE_TTL = 5 * 60 * 1000; // 5 minutes

export async function getSecret<T = Record<string, string>>(
  secretName: string
): Promise<T> {
  // Check cache
  const cached = secretsCache.get(secretName);
  if (cached && cached.expiresAt > Date.now()) {
    return cached.value as T;
  }

  try {
    const command = new GetSecretValueCommand({
      SecretId: secretName,
    });

    const response = await client.send(command);

    let secretValue: T;

    if (response.SecretString) {
      secretValue = JSON.parse(response.SecretString);
    } else if (response.SecretBinary) {
      const buff = Buffer.from(response.SecretBinary);
      secretValue = JSON.parse(buff.toString('utf-8'));
    } else {
      throw new Error('Secret has no value');
    }

    // Update cache
    secretsCache.set(secretName, {
      value: secretValue,
      expiresAt: Date.now() + CACHE_TTL,
    });

    return secretValue;
  } catch (error) {
    console.error(`Failed to retrieve secret ${secretName}:`, error);
    throw error;
  }
}

export async function createSecret(
  secretName: string,
  secretValue: Record<string, string>
): Promise<void> {
  const command = new CreateSecretCommand({
    Name: secretName,
    SecretString: JSON.stringify(secretValue),
    Tags: [
      { Key: 'Environment', Value: process.env.NODE_ENV || 'development' },
      { Key: 'Application', Value: 'my-app' },
    ],
  });

  await client.send(command);
}

export async function updateSecret(
  secretName: string,
  secretValue: Record<string, string>
): Promise<void> {
  const command = new UpdateSecretCommand({
    SecretId: secretName,
    SecretString: JSON.stringify(secretValue),
  });

  await client.send(command);

  // Invalidate cache
  secretsCache.delete(secretName);
}

export async function rotateSecret(secretName: string): Promise<void> {
  const command = new RotateSecretCommand({
    SecretId: secretName,
    RotateImmediately: true,
  });

  await client.send(command);

  // Invalidate cache
  secretsCache.delete(secretName);
}

Initialize Secrets on Startup
// lib/secrets/init.ts
import { getSecret } from './aws';

interface AppSecrets {
  database: {
    url: string;
    readUrl?: string;
  };
  jwt: {
    secret: string;
    refreshSecret: string;
  };
  stripe: {
    secretKey: string;
    webhookSecret: string;
  };
}

let appSecrets: AppSecrets | null = null;

export async function initializeSecrets(): Promise<AppSecrets> {
  if (appSecrets) return appSecrets;

  const [dbSecrets, jwtSecrets, stripeSecrets] = await Promise.all([
    getSecret<{ url: string; readUrl?: string }>('myapp/production/database'),
    getSecret<{ secret: string; refreshSecret: string }>('myapp/production/jwt'),
    getSecret<{ secretKey: string; webhookSecret: string }>('myapp/production/stripe'),
  ]);

  appSecrets = {
    database: dbSecrets,
    jwt: jwtSecrets,
    stripe: stripeSecrets,
  };

  return appSecrets;
}

export function getSecrets(): AppSecrets {
  if (!appSecrets) {
    throw new Error('Secrets not initialized. Call initializeSecrets() first.');
  }
  return appSecrets;
}

// Usage in app startup
async function startApp() {
  await initializeSecrets();
  // ... start server
}

HashiCorp Vault
// lib/secrets/vault.ts
import vault from 'node-vault';

const vaultClient = vault({
  apiVersion: 'v1',
  endpoint: process.env.VAULT_ADDR,
  token: process.env.VAULT_TOKEN,
});

export async function getSecretFromVault<T>(path: string): Promise<T> {
  try {
    const result = await vaultClient.read(`secret/data/${path}`);
    return result.data.data as T;
  } catch (error) {
    console.error(`Failed to read secret from path ${path}:`, error);
    throw error;
  }
}

export async function writeSecretToVault(
  path: string,
  data: Record<string, string>
): Promise<void> {
  await vaultClient.write(`secret/data/${path}`, { data });
}

// Dynamic database credentials
export async function getDatabaseCredentials(): Promise<{
  username: string;
  password: string;
}> {
  const result = await vaultClient.read('database/creds/my-role');
  return {
    username: result.data.username,
    password: result.data.password,
  };
}

Doppler Integration
// lib/secrets/doppler.ts
import { DopplerSDK } from '@dopplerhq/node-sdk';

const doppler = new DopplerSDK({
  accessToken: process.env.DOPPLER_TOKEN,
});

export async function fetchSecrets(
  project: string,
  config: string
): Promise<Record<string, string>> {
  const response = await doppler.secrets.download({
    project,
    config,
    format: 'json',
  });

  return JSON.parse(response);
}

// CLI usage
// doppler run -- npm start

Local Encryption
// lib/secrets/local.ts
import { createCipheriv, createDecipheriv, randomBytes, scrypt } from 'crypto';
import { promisify } from 'util';
import fs from 'fs/promises';

const scryptAsync = promisify(scrypt);

const ALGORITHM = 'aes-256-gcm';
const KEY_LENGTH = 32;
const IV_LENGTH = 16;
const AUTH_TAG_LENGTH = 16;
const SALT_LENGTH = 32;

export async function encrypt(plaintext: string, password: string): Promise<string> {
  const salt = randomBytes(SALT_LENGTH);
  const key = (await scryptAsync(password, salt, KEY_LENGTH)) as Buffer;
  const iv = randomBytes(IV_LENGTH);

  const cipher = createCipheriv(ALGORITHM, key, iv);
  const encrypted = Buffer.concat([
    cipher.update(plaintext, 'utf8'),
    cipher.final(),
  ]);
  const authTag = cipher.getAuthTag();

  // Combine: salt + iv + authTag + encrypted
  const combined = Buffer.concat([salt, iv, authTag, encrypted]);
  return combined.toString('base64');
}

export async function decrypt(ciphertext: string, password: string): Promise<string> {
  const combined = Buffer.from(ciphertext, 'base64');

  const salt = combined.subarray(0, SALT_LENGTH);
  const iv = combined.subarray(SALT_LENGTH, SALT_LENGTH + IV_LENGTH);
  const authTag = combined.subarray(
    SALT_LENGTH + IV_LENGTH,
    SALT_LENGTH + IV_LENGTH + AUTH_TAG_LENGTH
  );
  const encrypted = combined.subarray(SALT_LENGTH + IV_LENGTH + AUTH_TAG_LENGTH);

  const key = (await scryptAsync(password, salt, KEY_LENGTH)) as Buffer;

  const decipher = createDecipheriv(ALGORITHM, key, iv);
  decipher.setAuthTag(authTag);

  const decrypted = Buffer.concat([
    decipher.update(encrypted),
    decipher.final(),
  ]);

  return decrypted.toString('utf8');
}

// Encrypted env file
export async function loadEncryptedEnv(filepath: string, password: string): Promise<void> {
  const encrypted = await fs.readFile(filepath, 'utf8');
  const decrypted = await decrypt(encrypted, password);

  const lines = decrypted.split('\n');
  for (const line of lines) {
    const [key, ...valueParts] = line.split('=');
    if (key && valueParts.length > 0) {
      process.env[key.trim()] = valueParts.join('=').trim();
    }
  }
}

Kubernetes Secrets
# k8s/secrets.yaml
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
  namespace: production
type: Opaque
stringData:
  DATABASE_URL: postgresql://user:password@host:5432/db
  JWT_SECRET: your-jwt-secret
  STRIPE_SECRET_KEY: sk_live_...
---
# Using External Secrets Operator
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: app-secrets
  namespace: production
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: aws-secrets-manager
    kind: ClusterSecretStore
  target:
    name: app-secrets
    creationPolicy: Owner
  data:
    - secretKey: DATABASE_URL
      remoteRef:
        key: production/myapp/database
        property: url
    - secretKey: JWT_SECRET
      remoteRef:
        key: production/myapp/auth
        property: jwtSecret

// Reading K8s secrets in Node.js
import fs from 'fs';

function getSecretFromVolume(secretName: string): string {
  const secretPath = `/var/run/secrets/${secretName}`;
  return fs.readFileSync(secretPath, 'utf8').trim();
}

Secret Rotation
// lib/secrets/rotation.ts
interface RotationConfig {
  secretName: string;
  rotationInterval: number; // milliseconds
  onRotation: (newSecret: string) => Promise<void>;
}

class SecretRotator {
  private intervals: Map<string, NodeJS.Timeout> = new Map();

  async startRotation(config: RotationConfig): Promise<void> {
    // Immediate rotation
    await this.rotate(config);

    // Schedule recurring rotation
    const interval = setInterval(
      () => this.rotate(config),
      config.rotationInterval
    );

    this.intervals.set(config.secretName, interval);
  }

  private async rotate(config: RotationConfig): Promise<void> {
    try {
      // Generate new secret
      const newSecret = this.generateSecret();

      // Update in secrets manager
      await updateSecret(config.secretName, { value: newSecret });

      // Notify application
      await config.onRotation(newSecret);

      console.log(`Rotated secret: ${config.secretName}`);
    } catch (error) {
      console.error(`Failed to rotate ${config.secretName}:`, error);
    }
  }

  private generateSecret(): string {
    return randomBytes(32).toString('base64');
  }

  stopRotation(secretName: string): void {
    const interval = this.intervals.get(secretName);
    if (interval) {
      clearInterval(interval);
      this.intervals.delete(secretName);
    }
  }
}

Best Practices
Never commit secrets: Use .gitignore
Validate on startup: Fail fast on missing secrets
Use secret managers: AWS, Vault, Doppler
Rotate regularly: Automate key rotation
Encrypt at rest: Even in env files
Audit access: Log secret retrieval
Limit scope: Minimal permissions
Different per environment: Never share production secrets
Output Checklist

Every secrets implementation should include:

 .env.example with placeholders
 .gitignore for secret files
 Environment validation schema
 Secret manager integration
 Caching with TTL
 Rotation mechanism
 Audit logging
 Kubernetes/Docker support
 Development vs production separation
 Documentation for team
Weekly Installs
105
Repository
patricio0312rev/skills
GitHub Stars
35
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass