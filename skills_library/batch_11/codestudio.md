---
title: codestudio
url: https://skills.sh/acquia/acquia-skills/codestudio
---

# codestudio

skills/acquia/acquia-skills/codestudio
codestudio
Installation
$ npx skills add https://github.com/acquia/acquia-skills --skill codestudio
SKILL.md
Code Studio with Acquia CLI

Use when:

Setting up a new Code Studio project for a Cloud application
Changing the PHP version used in Code Studio builds
Migrating an existing acquia-pipelines.yml to a .gitlab-ci.yml file

Note: This skill covers Code Studio setup only. To trigger builds, check job status, or stream logs, use pipelines-cli (pipelines-cli-pipeline-operations).

Code Studio is Acquia's GitLab-based CI/CD platform. It runs build pipelines, automated tests, and deployments for your Cloud Platform applications.

Set Up Code Studio (Wizard)

The wizard creates and configures a Code Studio project for your application:

acli codestudio:wizard


Alias: acli cs:wizard

The wizard will:

Authenticate with your Cloud Platform application
Connect to your GitLab instance
Create or configure a Code Studio project
Set up CI/CD variables

Non-interactive (provide all credentials upfront):

acli codestudio:wizard \
  --key=YOUR_CLOUD_API_KEY \
  --secret=YOUR_CLOUD_API_SECRET \
  --gitlab-token=YOUR_GITLAB_TOKEN \
  --gitlab-project-id=12345 \
  --gitlab-host-name=code.acquia.com


Options:

Option	Description
--key	Cloud Platform API key for Code Studio to use
--secret	Cloud Platform API secret for Code Studio to use
--gitlab-token	GitLab personal access token
--gitlab-project-id	Integer project ID of the GitLab project to configure
--gitlab-host-name	GitLab hostname (defaults to Acquia's instance)
Change PHP Version in Code Studio

Update the PHP version used in Code Studio build containers:

acli codestudio:php-version <version>


Example:

acli codestudio:php-version 8.2
acli codestudio:php-version 8.3

Typical Workflow: Onboard to Code Studio
# Step 1: Set up Code Studio project
acli codestudio:wizard

# Step 2: Set PHP version if needed
acli codestudio:php-version 8.2

Best Practices
Run the wizard first — It sets up all required CI/CD variables automatically.
Use --key/--secret options for CI — Avoids interactive prompts in automated environments.
Match PHP versions — Ensure codestudio:php-version matches the version in your composer.json platform requirements.
Troubleshooting
"GitLab project not found"

Verify the project ID and that your token has access:

# Re-run wizard interactively to select the right project
acli codestudio:wizard

Authentication errors

Ensure your Cloud API key/secret are valid:

acli auth:login
acli auth:me

Related Topics
Getting Started — Authentication setup
Environment Management — Deploy to environments
Pull & Push — Push build artifacts
Weekly Installs
21
Repository
acquia/acquia-skills
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail