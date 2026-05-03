---
rating: ⭐⭐
title: cdk-bootstrap-configuration
url: https://skills.sh/loxosceles/ai-dev/cdk-bootstrap-configuration
---

# cdk-bootstrap-configuration

skills/loxosceles/ai-dev/cdk-bootstrap-configuration
cdk-bootstrap-configuration
Installation
$ npx skills add https://github.com/loxosceles/ai-dev --skill cdk-bootstrap-configuration
SKILL.md
CDK Bootstrap Configuration

This is a reference pattern. Learn from the approach, adapt to your context — don't copy verbatim.

Audience: CDK infrastructure developers. If you're building services that read configuration, see SSM Runtime Configuration.

Problem: Using CDK's valueFromLookup() for bootstrap configuration causes context caching issues, requiring manual intervention and creating circular dependencies between deployment scripts and infrastructure code.

Solution: Separate bootstrap configuration (deployment inputs) from runtime configuration (infrastructure outputs). Bootstrap flows through environment files into CDK at synth time; runtime outputs flow from infrastructure into SSM Parameter Store for service consumption.

Pattern

Architecture Flow:

┌─────────────────────────────────────────────────────────────┐
│ BOOTSTRAP LAYER (Pre-Infrastructure)                        │
│ - Lives in: .env.{stage} files (local) or CI variables      │
│ - Purpose: External constants needed to CREATE infra        │
│ - Examples: domain, certificate ARN, account ID             │
│ - Access: Read by CDK at synth time                         │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ CDK SYNTHESIS                                                │
│ - Reads bootstrap from environment directly                 │
│ - No SSM lookup at synth time                               │
│ - Generates CloudFormation template                         │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ CDK DEPLOYMENT                                               │
│ - Creates infrastructure resources                          │
│ - Writes outputs to SSM for runtime consumption             │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ SSM PARAMETER STORE (Post-Infrastructure)                   │
│ - Contains: Stack outputs for runtime consumption           │
│ - Purpose: Runtime config for services/lambdas/frontend     │
│ - Access: Services read at runtime                          │
└─────────────────────────────────────────────────────────────┘


Key Components:

Bootstrap Configuration: External constants (domain, cert ARN, account ID) needed to create infrastructure
Environment Manager: Loads bootstrap from files (local) or environment variables (CI/CD)
Stack Props: Bootstrap values passed through props to keep stacks decoupled
SSM Outputs: Infrastructure results written to Parameter Store for service consumption

Core Principle: SSM should store the RESULT of deployment, not the INPUT to deployment.

Why This Pattern?

Benefits:

No CDK Context Caching: Eliminates cdk.context.json and manual intervention
Clear Separation: Bootstrap (inputs) vs outputs (results) are architecturally distinct
CI/CD Friendly: Works seamlessly in both local and CI environments
Type-Safe: Validation at synth time catches missing configuration early
No Circular Dependencies: Deployment scripts don't pre-populate what CDK reads
Git-Friendly: No environment-specific context files to manage

Use Cases:

CDK projects with production domains and certificates
Multi-environment deployments (dev, staging, prod)
Projects with CI/CD pipelines
Teams experiencing CDK context caching issues
Implementation
1. Environment Manager
// lib/core/environment-manager.ts
export class EnvironmentManager {
  private loadEnv(stage: string): Record<string, string> {
    const envPath = path.join(this.infraRootPath, `.env.${stage}`);
    
    // Try file first (local), fall back to process.env (CI)
    if (fs.existsSync(envPath)) {
      const fileEnv = dotenv.parse(fs.readFileSync(envPath));
      
      // Filter undefined from process.env
      const processEnv: Record<string, string> = {};
      Object.entries(process.env).forEach(([key, value]) => {
        if (value !== undefined) processEnv[key] = value;
      });
      
      // CI variables override file values
      return { ...fileEnv, ...processEnv };
    }
    
    // CI path: use process.env only
    const processEnv: Record<string, string> = {};
    Object.entries(process.env).forEach(([key, value]) => {
      if (value !== undefined) processEnv[key] = value;
    });
    
    if (Object.keys(processEnv).length === 0) {
      throw new Error(
        `No configuration found for stage '${stage}'.\n` +
        `Expected file: ${envPath}\n` +
        `Or environment variables in CI/CD context.`
      );
    }
    
    return processEnv;
  }
  
  public getStackEnv(stackType: string): IStackEnv {
    const baseEnv = this.loadEnv(this.stage);
    const isProd = this.stage === 'prod';
    
    // Validate required bootstrap values
    this.validateBootstrap(baseEnv, isProd);
    
    return {
      awsAccountId: baseEnv.CDK_DEFAULT_ACCOUNT,
      awsRegionDefault: baseEnv.CDK_DEFAULT_REGION,
      stage: this.stage,
      // Add stage-specific bootstrap values
      ...(isProd && {
        prodDomainName: baseEnv.PROD_DOMAIN_NAME,
        certificateArn: baseEnv.CERTIFICATE_ARN
      })
    };
  }
  
  private validateBootstrap(env: Record<string, string>, isProd: boolean): void {
    const required = ['CDK_DEFAULT_ACCOUNT', 'CDK_DEFAULT_REGION'];
    
    if (isProd) {
      required.push('PROD_DOMAIN_NAME', 'CERTIFICATE_ARN');
    }
    
    const missing = required.filter(key => !env[key]);
    
    if (missing.length > 0) {
      throw new Error(
        `Missing required bootstrap configuration: ${missing.join(', ')}\n` +
        `Check .env.${this.stage} or CI/CD environment variables`
      );
    }
  }
}


Key Details:

Type Safety: Filters undefined values from process.env before using
Validation: Fail-fast at synth time with clear error messages
Merge Strategy: File values + process.env (CI overrides file)
2. CDK App Entry Point
// bin/app.ts
const envManager = new EnvironmentManager(config);
const stackEnv = envManager.getStackEnv('web');

new WebStack(app, `WebStack-${envManager.getStage()}`, {
  env: { 
    account: stackEnv.awsAccountId, 
    region: stackEnv.awsRegionDefault 
  },
  stackEnv: stackEnv  // Pass bootstrap through props
});


Why Props: Keeps stacks decoupled from EnvironmentManager, easier to test.

3. Stack Implementation
// lib/stacks/web-stack.ts
export class WebStack extends Stack {
  constructor(scope: Construct, id: string, props: WebStackProps) {
    super(scope, id, props);
    
    const isProd = props.stackEnv.stage === 'prod';
    
    // Use bootstrap values from props (NOT from SSM lookup)
    let domainName: string | undefined;
    let certificateArn: string | undefined;
    
    if (isProd) {
      domainName = props.stackEnv.prodDomainName;
      certificateArn = props.stackEnv.certificateArn;
    }
    
    // Create infrastructure...
    const distribution = new cloudfront.Distribution(this, 'Distribution', {
      domainNames: domainName ? [domainName] : undefined,
      certificate: certificateArn 
        ? acm.Certificate.fromCertificateArn(this, 'Cert', certificateArn)
        : undefined,
      // ... other config
    });
    
    // Write outputs to SSM for runtime consumption
    new ssm.StringParameter(this, 'CloudFrontDomainOutput', {
      parameterName: `/${projectId}/${stage}/outputs/CLOUDFRONT_DOMAIN`,
      stringValue: distribution.distributionDomainName,
      description: 'CloudFront distribution domain name',
      tier: ssm.ParameterTier.STANDARD
    });
  }
}


Critical: Remove any ssm.StringParameter.valueFromLookup() calls for bootstrap values.

4. Stack Props Interface
// types/stack-env.ts
export interface IStackEnv {
  awsAccountId: string;
  awsRegionDefault: string;
  stage: string;
  // Stage-specific bootstrap values
  prodDomainName?: string;
  certificateArn?: string;
}

export interface WebStackProps extends StackProps {
  stackEnv: IStackEnv;
}

5. Bootstrap Configuration

Local Development (.env.{stage} - gitignored):

# Bootstrap values for CDK synthesis
CDK_DEFAULT_ACCOUNT=123456789012
CDK_DEFAULT_REGION=us-east-1
PROD_DOMAIN_NAME=example.com
CERTIFICATE_ARN=arn:aws:acm:us-east-1:123456789012:certificate/abc123


CI/CD: Configure as repository variables (GitHub Actions Variables, CodeBuild environment, etc.)

Critical Tradeoff: Bootstrap vs Runtime

The Fundamental Distinction:

Aspect	Bootstrap (Inputs)	Runtime (Outputs)
When	Before infrastructure exists	After infrastructure exists
Source	.env files or CI variables	SSM Parameter Store
Purpose	Create infrastructure	Configure services
Read By	CDK at synth time	Services at runtime
Examples	Domain, cert ARN, account ID	CloudFront domain, bucket name

Why This Matters:

Using valueFromLookup() for bootstrap creates circular dependency
CDK caches lookup results in cdk.context.json (environment-specific, not git-friendly)
Context loss requires manual intervention and debugging time

The Fix:

Bootstrap: Read directly from environment (no SSM lookup)
Runtime: Write to SSM after deployment (for services)
When NOT to Use
Simple single-environment projects: If you only have one environment and no production domain, this separation may be overkill
Non-CDK projects: This pattern is specific to AWS CDK context caching issues
Projects without external dependencies: If all config is generated by CDK itself, simpler approaches may suffice

Alternatives:

CDK Context Values: For truly static, never-changing values (not recommended for environment-specific config)
CloudFormation Parameters: For values that change per deployment (adds deployment complexity)
Related Patterns
SSM Runtime Configuration - How services consume runtime configuration from SSM (this pattern writes to SSM, that pattern reads from it)
Environment Validation - Fail-fast validation patterns used in the validateBootstrap() method
Environment Deployment Strategy - Multi-environment deployment approach that defines what "dev", "prod", etc. mean
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