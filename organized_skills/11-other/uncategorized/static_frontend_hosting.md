---
rating: ⭐⭐
title: static-frontend-hosting
url: https://skills.sh/loxosceles/ai-dev/static-frontend-hosting
---

# static-frontend-hosting

skills/loxosceles/ai-dev/static-frontend-hosting
static-frontend-hosting
Installation
$ npx skills add https://github.com/loxosceles/ai-dev --skill static-frontend-hosting
SKILL.md
Static Frontend Hosting with Edge Authentication

This is a reference pattern. Learn from the approach, adapt to your context — don't copy verbatim.

Problem: Need low-cost, globally distributed frontend hosting with authentication but without requiring users to log in.

Solution: Static site on S3 + CloudFront CDN + Lambda@Edge for transparent authentication.

Pattern

Architecture:

User Request
    ↓
CloudFront (CDN)
    ↓
Lambda@Edge (us-east-1) ← Validates token, sets cookies
    ↓
S3 Bucket (Static Files)


Key Components:

S3 Bucket: Hosts static frontend build (HTML, JS, CSS)
CloudFront: Global CDN for fast delivery
Lambda@Edge: Intercepts requests to handle authentication
Origin Access Control: Secures S3 bucket (only CloudFront can access)
Why This Pattern?

Benefits:

Low Cost: No servers running 24/7, pay only for storage and bandwidth
Global Performance: CloudFront edge locations worldwide
Scalability: Handles traffic spikes automatically
Transparent Auth: Users get authenticated via link, no login screen
Static Security: No server-side vulnerabilities, just static files

Use Cases:

Portfolio sites with personalized access
Demo applications with invite-only access
Marketing sites with gated content
Documentation with customer-specific views
Implementation

S3 Bucket:

const websiteBucket = new s3.Bucket(this, 'WebsiteBucket', {
  bucketName: `${PROJECT_ID}-web-${environment}`,
  blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL, // Not public!
  removalPolicy: cdk.RemovalPolicy.DESTROY
});


CloudFront Distribution:

const distribution = new cloudfront.Distribution(this, 'Distribution', {
  defaultBehavior: {
    origin: new origins.S3Origin(websiteBucket),
    viewerProtocolPolicy: cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
    edgeLambdas: [{
      functionVersion: authFunction.currentVersion,
      eventType: cloudfront.LambdaEdgeEventType.VIEWER_REQUEST
    }]
  }
});


Lambda@Edge Function:

export async function handler(event) {
  const request = event.Records[0].cf.request;
  const queryParams = new URLSearchParams(request.querystring);
  const token = queryParams.get('token');
  
  if (token) {
    // Validate token (check signature, expiration, etc.)
    const isValid = await validateToken(token);
    
    if (isValid) {
      // Set authentication cookie
      return {
        status: '302',
        headers: {
          'location': [{ value: '/' }],
          'set-cookie': [{ value: `auth_token=${token}; Secure; HttpOnly` }]
        }
      };
    }
  }
  
  // Check existing cookie
  const cookies = request.headers.cookie?.[0]?.value || '';
  if (cookies.includes('auth_token=')) {
    return request; // Authenticated, proceed
  }
  
  // Not authenticated, show public view or error
  return request;
}

Critical Tradeoff: Lambda@Edge Region Requirement

Constraint: Lambda@Edge functions MUST be deployed in us-east-1 region.

Why: CloudFront is a global service managed from us-east-1. Edge functions replicate globally from this region.

Implications:

Your CDK stack for web hosting must deploy to us-east-1
If your main infrastructure is in another region (e.g., eu-central-1), you need separate stacks
Cross-region references become complex

Workaround:

// Main stack in eu-central-1
const mainStack = new MainStack(app, 'MainStack', {
  env: { region: 'eu-central-1' }
});

// Web stack in us-east-1 (for Lambda@Edge)
const webStack = new WebStack(app, 'WebStack', {
  env: { region: 'us-east-1' }
});

// Pass data via SSM Parameter Store, not direct references

Deployment Pipeline

Build Process:

Build static frontend (npm run build)
Deploy infrastructure (S3, CloudFront, Lambda@Edge)
Upload static files to S3
Invalidate CloudFront cache

Example:

# buildspec.yml
phases:
  build:
    commands:
      - cd frontend && npm run build
      - cd infrastructure && cdk deploy WebStack
      - aws s3 sync frontend/out s3://${BUCKET_NAME}
      - aws cloudfront create-invalidation --distribution-id ${DIST_ID} --paths "/*"

When NOT to Use
Server-Side Rendering: Use ECS/Lambda with API Gateway instead
Real-time Updates: Use WebSocket API with Lambda
Complex Auth Flows: Use Cognito Hosted UI or custom auth service
Frequent Content Updates: Consider incremental static regeneration or dynamic rendering
Related Patterns
Link-Based Authentication - How to implement the auth tokens
Environment Deployment Strategy - How to deploy across environments
CDK Stack Organization - Managing multi-region stacks
Progressive Improvement

If the developer corrects a behavior that this skill should have prevented, suggest a specific amendment to this skill to prevent the same correction in the future.

Weekly Installs
52
Repository
loxosceles/ai-dev
First Seen
Mar 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass