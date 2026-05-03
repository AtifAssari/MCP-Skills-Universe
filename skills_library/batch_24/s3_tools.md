---
title: s3-tools
url: https://skills.sh/winsorllc/upgraded-carnival/s3-tools
---

# s3-tools

skills/winsorllc/upgraded-carnival/s3-tools
s3-tools
Installation
$ npx skills add https://github.com/winsorllc/upgraded-carnival --skill s3-tools
SKILL.md
S3 Tools Skill

S3-compatible storage operations using AWS CLI or compatible tools.

When to Use
Upload files to S3
Download files from S3
List buckets and objects
Manage S3 permissions
Sync directories
Setup
Configure AWS CLI
# Configure with credentials
aws configure

# Or with specific profile
aws configure --profile myprofile

# Set environment variables
export AWS_ACCESS_KEY_ID="your-key"
export AWS_SECRET_ACCESS_KEY="your-secret"
export AWS_DEFAULT_REGION="us-east-1"

MinIO (Self-Hosted S3)
# Configure for MinIO
aws configure set aws_access_key_id minioadmin
aws configure set aws_secret_access_key minioadmin
aws configure set default.region us-east-1

# Use custom endpoint
aws --endpoint-url http://localhost:9000 s3 ls

Common Operations
List Buckets
# List all buckets
aws s3 ls

# List with creation date
aws s3 ls --recursive

List Objects
# List bucket contents
aws s3 ls s3://my-bucket/

# List recursively
aws s3 ls s3://my-bucket/ --recursive

# Filter by prefix
aws s3 ls s3://my-bucket/folder/

Upload Files
# Upload single file
aws s3 cp file.txt s3://my-bucket/

# Upload with metadata
aws s3 cp file.txt s3://my-bucket/ --content-type "text/plain"

# Upload folder
aws s3 cp ./folder s3://my-bucket/folder/ --recursive

# Set cache control
aws s3 cp file.html s3://my-bucket/ --cache-control "max-age=3600"

Download Files
# Download single file
aws s3 cp s3://my-bucket/file.txt ./

# Download folder
aws s3 cp s3://my-bucket/folder/ ./folder --recursive

# Download with specific version
aws s3 cp s3://my-bucket/file.txt ./ --version-id version-id

Delete Objects
# Delete single file
aws s3 rm s3://my-bucket/file.txt

# Delete folder
aws s3 rm s3://my-bucket/folder/ --recursive

# Delete with prefix
aws s3 rm s3://my-bucket/ --exclude "*" --include "*.log"

Sync
# Sync local to S3
aws s3 sync ./folder s3://my-bucket/folder/

# Sync S3 to local
aws s3 sync s3://my-bucket/folder/ ./folder

# Sync with deletion (remove files not in source)
aws s3 sync s3://my-bucket/folder/ ./folder --delete

# Sync with excludes
aws s3 sync ./folder s3://my-bucket/folder/ --exclude "*.tmp" --exclude ".git/*"

Presigned URLs
Generate Presigned URL
# Generate URL (default 1 hour)
aws s3 presign s3://my-bucket/file.txt

# With custom expiration
aws s3 presign s3://my-bucket/file.txt --expires-in 86400

# Upload presigned URL
aws s3 presign s3://my-bucket/file.txt --put

Bucket Operations
Create Bucket
# Create bucket
aws s3 mb s3://my-new-bucket

# Create in specific region
aws s3 mb s3://my-new-bucket --region us-west-2

Delete Bucket
# Delete empty bucket
aws s3 rb s3://my-bucket

# Force delete (remove all objects first)
aws s3 rb s3://my-bucket --force

Examples
Backup to S3
#!/bin/bash
# Daily backup script

DATE=$(date +%Y-%m-%d)
BUCKET="my-backups"
SOURCE="/data"

aws s3 sync "$SOURCE" "s3://$BUCKET/backup-$DATE/" \
  --storage-class STANDARD_IA \
  --exclude "*.tmp"

Clean Old Backups
# Delete backups older than 30 days
aws s3 ls s3://my-bucket/backups/ | while read -r date time size file; do
  filedate=$(echo "$date" | tr -d '-')
  if [ "$filedate" -lt "$(date -d '30 days ago' +%Y%m%d)" ]; then
    aws s3 rm "s3://my-bucket/backups/$file" --recursive
  fi
done

Set Public Access
# Make object publicly readable
aws s3 cp file.txt s3://my-bucket/ --acl public-read

# Make entire bucket public (use carefully!)
aws s3api put-bucket-acl --bucket my-bucket --grant-read 'uri="http://acs.amazonaws.com/groups/global/AllUsers"'

Useful Flags
Flag	Description
--recursive	Process all files/dirs
--dryrun	Show what would happen
--quiet	Suppress output
--storage-class	Set storage tier
--content-type	Set MIME type
--cache-control	Set caching headers
--acl	Set access control
Notes
Use aws s3api for advanced operations
Consider using lifecycle policies for cost savings
Enable versioning for important buckets
Use IAM roles instead of access keys when possible
Weekly Installs
8
Repository
winsorllc/upgra…carnival
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail