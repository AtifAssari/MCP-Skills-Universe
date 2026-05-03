---
rating: ⭐⭐⭐
title: security-updates
url: https://skills.sh/acquia/acquia-skills/security-updates
---

# security-updates

skills/acquia/acquia-skills/security-updates
security-updates
Installation
$ npx skills add https://github.com/acquia/acquia-skills --skill security-updates
SKILL.md
Security Updates for Drupal with Composer

Use when:

Running a security audit on a Drupal project
Fixing packages flagged by composer audit
Applying a specific security advisory
Verifying no known vulnerabilities remain
Before You Start — Create a Branch

This step is mandatory. Do not run any composer commands until a new branch is created and confirmed. Never update packages directly on main or master.

Check the current branch first:

git branch --show-current


If the user is on main, master, or any protected branch, stop and ask: "What would you like to name the new branch for these security fixes?"

Suggest a default if they are unsure (e.g., security/drupal-updates-YYYY-MM-DD).

git checkout -b <branch-name>


Confirm the new branch is active before proceeding:

git branch --show-current


Only continue to the next step once the output confirms a non-protected branch.

Audit for Vulnerabilities
composer audit


Output lists packages with known advisories, CVE IDs, and links to the advisory.

JSON output (for scripting)
composer audit --format=json

Audit without dev dependencies
composer audit --no-dev

Fix a Specific Vulnerable Package
composer update drupal/package --with-all-dependencies


Use --with-all-dependencies to allow transitive dependency version changes required by the update.

Example — fix a known advisory in drupal/core
composer update drupal/core-recommended drupal/core-composer-scaffold --with-all-dependencies

Fix All Packages with Advisories

Update only packages flagged by the audit, staying within the version constraints in composer.json:

composer update --with-all-dependencies $(composer audit --format=json 2>/dev/null \
  | python3 -c "import sys,json; data=json.load(sys.stdin); print(' '.join(set(a['packageName'] for a in data.get('advisories', {}).values() if isinstance(a, dict)) or [v[0]['packageName'] for v in data.get('advisories', {}).values()]))" 2>/dev/null)


Or update them manually after reviewing the audit output:

# List vulnerable packages from audit output, then update each
composer update drupal/package1 drupal/package2 --with-all-dependencies

Verify No Vulnerabilities Remain
composer audit


Expected output after all fixes:

No security vulnerability advisories found.


After the audit is clean, always ask the user these questions in order:

1. "Do you want to commit these changes?"

If yes:
git add composer.json composer.lock
git commit -m "Apply Drupal security updates"

If no → remind the user that composer.json and composer.lock are uncommitted before proceeding.

2. "Do you want to deploy these changes to an Acquia environment?"

If yes → follow the Drupal Update and Deploy playbook to push code, switch the environment, and optionally trigger a pipeline build.
If no → done.
Troubleshooting
"Your requirements could not be resolved"

The version required to fix the advisory conflicts with another constraint. Options:

# Check what requires the package
composer why drupal/package

# Check what prevents the update
composer why-not drupal/package 2.x

# Relax the constraint in composer.json if safe, then retry
composer update drupal/package --with-all-dependencies

Advisory persists after update

Composer's local advisory database may be stale. Refresh it:

composer audit --update-cache
composer audit

Package cannot be updated without breaking other packages

Pin the conflicting package temporarily and file a follow-up:

# Check the full dependency tree
composer depends drupal/conflicting-package


Resolve the constraint in composer.json before retrying.

Best Practices
Run composer audit before every deploy — catch new advisories early.
Use --with-all-dependencies — security fixes often require transitive updates.
Review composer.lock diff — confirm only expected packages changed.
Check the advisory link — understand what the vulnerability is before updating.
Weekly Installs
23
Repository
acquia/acquia-skills
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass