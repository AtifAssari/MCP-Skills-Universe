---
rating: ⭐⭐⭐
title: fnox-providers
url: https://skills.sh/thebushidocollective/han/fnox-providers
---

# fnox-providers

skills/thebushidocollective/han/fnox-providers
fnox-providers
Installation
$ npx skills add https://github.com/thebushidocollective/han --skill fnox-providers
SKILL.md
Fnox - Providers

Configuring encryption and secret storage providers in Fnox for secure secrets management.

Provider Types

Fnox supports three categories of providers:

Encryption - Local encryption (age, AWS KMS, Azure, GCP)
Cloud Storage - Remote secret storage (AWS Secrets Manager, Azure Key Vault, GCP Secret Manager, Vault)
Password Managers - Integration with password managers (1Password, Bitwarden, Infisical, pass)
Age Encryption (Recommended)
Setup Age Provider
# Generate age key pair
age-keygen -o ~/.config/fnox/keys/identity.txt

# Get public key
cat ~/.config/fnox/keys/identity.txt | grep "public key"
# age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p

Configure Age in fnox.toml
# fnox.toml (committed)
[providers.age]
type = "age"
public_keys = ["age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p"]

# fnox.local.toml (gitignored)
[providers.age]
identity = "~/.config/fnox/keys/identity.txt"

Store Secrets with Age
# Set encrypted secret
fnox set DATABASE_PASSWORD
# Prompts for value, encrypts with age public key

# Set from command
echo "secret-value" | fnox set API_KEY --provider age

Team Setup with Age
# Multiple recipients for team access
[providers.age]
type = "age"
public_keys = [
  "age1ql3z...",  # Alice
  "age1qw4r...",  # Bob
  "age1qx5t...",  # CI/CD
]

AWS Secrets Manager
Configure AWS Secrets Manager
[providers.aws-sm]
type = "aws-sm"
region = "us-east-1"
# Optional: profile = "production"

Store Secrets in AWS
# Reference AWS secret
fnox set DATABASE_URL --provider aws-sm
# Enter: prod/database-url (AWS secret name)

AWS Secrets Manager Configuration
[secrets]
DATABASE_URL = {
  provider = "aws-sm",
  value = "prod/database-url",
  description = "Production database connection string"
}

API_KEY = {
  provider = "aws-sm",
  value = "prod/api-key"
}

AWS KMS Encryption
Configure AWS KMS
[providers.kms]
type = "aws-kms"
key_id = "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012"
region = "us-east-1"

Use AWS KMS
# Encrypt with KMS
fnox set SECRET_KEY --provider kms

Azure Key Vault
Configure Azure
[providers.azure]
type = "azure-kv"
vault_url = "https://my-vault.vault.azure.net"
# Authentication via Azure CLI or environment variables

Azure Secrets
[secrets]
DATABASE_PASSWORD = {
  provider = "azure",
  value = "database-password",
  description = "Azure Key Vault secret name"
}

GCP Secret Manager
Configure GCP
[providers.gcp]
type = "gcp-sm"
project_id = "my-project"
# Authentication via gcloud or service account

GCP Secrets
[secrets]
API_KEY = {
  provider = "gcp",
  value = "projects/my-project/secrets/api-key/versions/latest"
}

HashiCorp Vault
Configure Vault
[providers.vault]
type = "vault"
address = "https://vault.example.com"
token = { env = "VAULT_TOKEN" }  # From environment

Vault Secrets
[secrets]
DATABASE_URL = {
  provider = "vault",
  value = "secret/data/prod/database-url"
}

1Password
Configure 1Password
[providers.onepassword]
type = "1password"
# Requires 1Password CLI (op) installed

1Password References
[secrets]
API_KEY = {
  provider = "onepassword",
  value = "op://Production/API Keys/api-key"
}

DATABASE_PASSWORD = {
  provider = "onepassword",
  value = "op://Production/Database/password"
}

Bitwarden
Configure Bitwarden
[providers.bitwarden]
type = "bitwarden"
# Requires Bitwarden CLI (bw) installed and unlocked

Bitwarden Secrets
[secrets]
STRIPE_KEY = {
  provider = "bitwarden",
  value = "item-id/field-name"
}

Provider Testing
Test Provider Configuration
# Test specific provider
fnox provider test age
fnox provider test aws-sm

# List configured providers
fnox provider list

# Add provider interactively
fnox provider add

# Remove provider
fnox provider remove age

Best Practices
Choose the Right Provider
# Development: age (simple, local encryption)
[providers.age]
type = "age"
public_keys = ["age1ql3z..."]

# Production: Cloud secret manager
[providers.aws-sm]
type = "aws-sm"
region = "us-east-1"

# Team collaboration: 1Password or Bitwarden
[providers.onepassword]
type = "1password"

Use Multiple Providers
# Different providers for different secrets
[providers.age]
type = "age"
public_keys = ["age1ql3z..."]

[providers.aws-sm]
type = "aws-sm"
region = "us-east-1"

[secrets]
# Development secrets with age
DEV_API_KEY = { provider = "age", value = "age[...]" }

# Production secrets with AWS
PROD_DATABASE_URL = { provider = "aws-sm", value = "prod/db-url" }

Provider Aliases
# Name providers descriptively
[providers.prod-secrets]
type = "aws-sm"
region = "us-east-1"

[providers.staging-secrets]
type = "aws-sm"
region = "us-west-2"

[secrets]
DATABASE_URL = { provider = "prod-secrets", value = "prod/db" }

Common Patterns
Development to Production Migration
# fnox.toml (development)
[providers.age]
type = "age"
public_keys = ["age1ql3z..."]

[secrets]
DATABASE_URL = { provider = "age", value = "age[...]" }

# fnox.production.toml
[providers.aws-sm]
type = "aws-sm"
region = "us-east-1"

[secrets]
DATABASE_URL = { provider = "aws-sm", value = "prod/database-url" }

Multi-Region Setup
[providers.us-secrets]
type = "aws-sm"
region = "us-east-1"

[providers.eu-secrets]
type = "aws-sm"
region = "eu-west-1"

[secrets]
US_API_ENDPOINT = { provider = "us-secrets", value = "us/api-endpoint" }
EU_API_ENDPOINT = { provider = "eu-secrets", value = "eu/api-endpoint" }

Hybrid Approach
# Development secrets: age encryption
[providers.age]
type = "age"
public_keys = ["age1ql3z..."]

# Shared team secrets: 1Password
[providers.team]
type = "1password"

# Production secrets: AWS
[providers.prod]
type = "aws-sm"
region = "us-east-1"

[secrets]
DEV_DATABASE_URL = { provider = "age", value = "age[...]" }
TEAM_SLACK_WEBHOOK = { provider = "team", value = "op://Team/Slack/webhook" }
PROD_DATABASE_URL = { provider = "prod", value = "prod/db-url" }

Anti-Patterns
Don't Hardcode Credentials
# Bad: Hardcoded credentials
[providers.aws-sm]
type = "aws-sm"
region = "us-east-1"
access_key_id = "AKIAIOSFODNN7EXAMPLE"  # NEVER DO THIS
secret_access_key = "wJalrXUtnFEMI/..."  # NEVER DO THIS

# Good: Use AWS credentials chain
[providers.aws-sm]
type = "aws-sm"
region = "us-east-1"
# Credentials from ~/.aws/credentials or environment

Don't Mix Provider Types Unnecessarily
# Bad: Too many providers for simple project
[providers.age]
type = "age"

[providers.aws-sm]
type = "aws-sm"

[providers.azure]
type = "azure-kv"

[providers.gcp]
type = "gcp-sm"

# Good: Choose one appropriate provider
[providers.age]
type = "age"
public_keys = ["age1ql3z..."]

Don't Share Private Keys
# Bad: Private key in config
[providers.age]
identity = "AGE-SECRET-KEY-..."  # NEVER COMMIT THIS

# Good: Reference external file
[providers.age]
identity = "~/.config/fnox/keys/identity.txt"  # Gitignored

Provider-Specific Features
Age: Multiple Recipients
[providers.age]
type = "age"
public_keys = [
  "age1ql3z...",  # Team member 1
  "age1qw4r...",  # Team member 2
  "age1qx5t...",  # CI/CD system
]

AWS: Cross-Account Access
[providers.shared-secrets]
type = "aws-sm"
region = "us-east-1"
role_arn = "arn:aws:iam::123456789012:role/CrossAccountSecretsRole"

Vault: Namespace Support
[providers.vault-prod]
type = "vault"
address = "https://vault.example.com"
namespace = "production"
token = { env = "VAULT_TOKEN" }

Related Skills
configuration: Managing fnox.toml structure and secrets
security-best-practices: Security guidelines for providers
Weekly Installs
21
Repository
thebushidocollective/han
GitHub Stars
145
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass