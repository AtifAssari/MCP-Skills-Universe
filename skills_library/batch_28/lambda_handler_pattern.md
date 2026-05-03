---
title: lambda-handler-pattern
url: https://skills.sh/loxosceles/ai-dev/lambda-handler-pattern
---

# lambda-handler-pattern

skills/loxosceles/ai-dev/lambda-handler-pattern
lambda-handler-pattern
Installation
$ npx skills add https://github.com/loxosceles/ai-dev --skill lambda-handler-pattern
SKILL.md
Lambda Handler Pattern

This is a reference pattern. Learn from the approach, adapt to your context — don't copy verbatim.

Problem: Lambda functions need environment variables and AWS clients, but improper initialization causes cold start issues or hard-to-test code.

Solution: Initialize and validate everything at module level (runs once on cold start), inject dependencies into pure helper functions.

Core Pattern

Key Principle: Lambda environment variables are immutable at runtime. Validate once on cold start, use safely throughout the module.

Module Level: Environment Variables + AWS Clients
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient } from '@aws-sdk/lib-dynamodb';

// 1. Validate environment variables (fail fast on cold start)
const TABLE_NAME = process.env.TABLE_NAME;
const API_KEY = process.env.API_KEY;
const REGION = process.env.AWS_REGION;

if (!TABLE_NAME) {
  throw new Error('TABLE_NAME not set. Configure in SSM: /myapp/${env}/table-name');
}
if (!API_KEY) {
  throw new Error('API_KEY not set. Configure in SSM: /myapp/${env}/api-key');
}
if (!REGION) {
  throw new Error('AWS_REGION not set');
}

// 2. Initialize AWS clients (cached across warm invocations)
const dynamoClient = new DynamoDBClient({ region: REGION });
const docClient = DynamoDBDocumentClient.from(dynamoClient);

// 3. Handler: Thin orchestration layer
export const handler = async (event: APIGatewayProxyEvent) => {
  return processEvent(event, TABLE_NAME, API_KEY, docClient);
};

// 4. Pure function: All dependencies injected
async function processEvent(
  event: APIGatewayProxyEvent,
  tableName: string,
  apiKey: string,
  client: DynamoDBDocumentClient
) {
  // Business logic here - fully testable without env vars
  const body = JSON.parse(event.body || '{}');
  
  await client.send(new PutCommand({
    TableName: tableName,
    Item: { id: body.id, data: body.data }
  }));
  
  return {
    statusCode: 200,
    body: JSON.stringify({ success: true })
  };
}


Why This Pattern:

✅ Fail fast: Missing config caught on cold start, before any invocation
✅ Performance: Clients cached across warm invocations
✅ Testability: Helper functions are pure, dependencies injected
✅ Industry standard: Aligns with AWS documentation and common practice
✅ Consistency: Both env vars and clients at module level
Helper Function for Validation

For cleaner validation with helpful error messages:

function getRequiredEnv(key: string, ssmPath?: string): string {
  const value = process.env[key];
  if (!value) {
    const hint = ssmPath ? ` Configure in SSM: ${ssmPath}` : '';
    throw new Error(`${key} environment variable not set.${hint}`);
  }
  return value;
}

// Usage
const TABLE_NAME = getRequiredEnv('TABLE_NAME', '/myapp/${env}/table-name');
const API_KEY = getRequiredEnv('API_KEY', '/myapp/${env}/api-key');
const REGION = getRequiredEnv('AWS_REGION');

Complete Example
import { APIGatewayProxyEvent, APIGatewayProxyResult } from 'aws-lambda';
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, PutCommand } from '@aws-sdk/lib-dynamodb';

// Helper: Validate required env vars
function getRequiredEnv(key: string, ssmPath?: string): string {
  const value = process.env[key];
  if (!value) {
    const hint = ssmPath ? ` Configure in SSM: ${ssmPath}` : '';
    throw new Error(`${key} environment variable not set.${hint}`);
  }
  return value;
}

// Module level: Validate env vars
const TABLE_NAME = getRequiredEnv('TABLE_NAME', '/myapp/${env}/table-name');
const API_KEY = getRequiredEnv('API_KEY', '/myapp/${env}/api-key');
const REGION = getRequiredEnv('AWS_REGION');

// Module level: Initialize AWS clients
const dynamoClient = new DynamoDBClient({ region: REGION });
const docClient = DynamoDBDocumentClient.from(dynamoClient);

// Handler: Thin orchestration
export const handler = async (
  event: APIGatewayProxyEvent
): Promise<APIGatewayProxyResult> => {
  return processEvent(event, TABLE_NAME, API_KEY, docClient);
};

// Pure function: All dependencies injected
async function processEvent(
  event: APIGatewayProxyEvent,
  tableName: string,
  apiKey: string,
  client: DynamoDBDocumentClient
): Promise<APIGatewayProxyResult> {
  const body = JSON.parse(event.body || '{}');
  
  // Validate API key from request
  if (event.headers['x-api-key'] !== apiKey) {
    return {
      statusCode: 401,
      body: JSON.stringify({ error: 'Unauthorized' })
    };
  }
  
  // Store in DynamoDB
  await client.send(new PutCommand({
    TableName: tableName,
    Item: { id: body.id, data: body.data, timestamp: Date.now() }
  }));
  
  return {
    statusCode: 200,
    body: JSON.stringify({ success: true })
  };
}

What Goes Where
Module Level (Outside Handler)

Initialize once on cold start:

Environment variable validation (fail fast)
AWS SDK clients (DynamoDB, S3, SSM, Secrets Manager, etc.)
Database connection pools
HTTP clients with connection pooling
Compiled templates or schemas
Heavy computations that don't change
// ✅ Module level
const TABLE_NAME = getRequiredEnv('TABLE_NAME');
const s3Client = new S3Client({});
const ssmClient = new SSMClient({});
const httpClient = new HttpClient({ keepAlive: true });

Handler Level (Inside Handler)

Thin orchestration only:

Parse event data
Call pure helper functions with injected dependencies
Return response
// ✅ Handler: Orchestration only
export const handler = async (event: APIGatewayProxyEvent) => {
  // Delegate to pure functions
  return processRequest(event, TABLE_NAME, REGION, s3Client);
};

Testing Benefits

Pure functions are easy to test without environment setup:

// Test without environment variables
describe('processEvent', () => {
  it('stores item in DynamoDB', async () => {
    const mockClient = createMockDocClient();
    const event = createMockEvent({ id: '123', data: 'test' });
    
    const result = await processEvent(
      event,
      'test-table',
      'test-api-key',
      mockClient
    );
    
    expect(result.statusCode).toBe(200);
    expect(mockClient.send).toHaveBeenCalledWith(
      expect.objectContaining({
        input: { 
          TableName: 'test-table', 
          Item: { id: '123', data: 'test', timestamp: expect.any(Number) }
        }
      })
    );
  });
  
  it('returns 401 for invalid API key', async () => {
    const mockClient = createMockDocClient();
    const event = createMockEvent({ id: '123' }, { 'x-api-key': 'wrong-key' });
    
    const result = await processEvent(event, 'test-table', 'correct-key', mockClient);
    
    expect(result.statusCode).toBe(401);
    expect(mockClient.send).not.toHaveBeenCalled();
  });
});

Core Principles Still Apply

All Core Principles remain valid:

Ordering: Imports → Env validation → Constants → Clients → Types → Pure functions → Impure functions → Handler
No Fallbacks: Fail fast if environment variables are missing
Explicit Errors: Clear error messages with SSM parameter paths
Type Safety: Use TypeScript strict mode
Dependency Injection: Pass clients and config to helper functions
Anti-Patterns
❌ Don't: Validate env vars in handler
// ❌ Validates on every invocation (wasteful)
export const handler = async (event: APIGatewayProxyEvent) => {
  const tableName = process.env.TABLE_NAME;
  if (!tableName) throw new Error('TABLE_NAME not set');
  
  return processEvent(event, tableName);
};


Why bad: Validation runs on every invocation instead of once on cold start.

❌ Don't: Initialize clients in handler
// ❌ Recreates client on every invocation
export const handler = async (event: APIGatewayProxyEvent) => {
  const dynamoClient = new DynamoDBClient({});
  const docClient = DynamoDBDocumentClient.from(dynamoClient);
  
  await docClient.send(new PutCommand({ /* ... */ }));
};


Why bad: Loses Lambda's warm container caching benefits, slower performance.

❌ Don't: Use module-level vars in helper functions
// ❌ Helper function depends on global state
const TABLE_NAME = process.env.TABLE_NAME!;

function processEvent(event: APIGatewayProxyEvent) {
  // Uses global TABLE_NAME - not pure, hard to test
  await docClient.send(new PutCommand({ TableName: TABLE_NAME, /* ... */ }));
}


Why bad: Function is not pure, harder to test, hidden dependencies.

✅ Do: Inject dependencies
// ✅ Pure function with explicit dependencies
const TABLE_NAME = getRequiredEnv('TABLE_NAME');

function processEvent(
  event: APIGatewayProxyEvent,
  tableName: string,
  client: DynamoDBDocumentClient
) {
  // All dependencies explicit - easy to test
  await client.send(new PutCommand({ TableName: tableName, /* ... */ }));
}


Related:

Core Principles - Ordering, purity, error handling
Environment Validation - Validating required config
Resource Naming - Lambda layer organization
Progressive Improvement

If the developer corrects a behavior that this skill should have prevented, suggest a specific amendment to this skill to prevent the same correction in the future.

Weekly Installs
39
Repository
loxosceles/ai-dev
First Seen
Mar 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass