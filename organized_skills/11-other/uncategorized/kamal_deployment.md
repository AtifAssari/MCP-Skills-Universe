---
rating: ⭐⭐⭐
title: kamal-deployment
url: https://skills.sh/faqndo97/ai-skills/kamal-deployment
---

# kamal-deployment

skills/faqndo97/ai-skills/kamal-deployment
kamal-deployment
Installation
$ npx skills add https://github.com/faqndo97/ai-skills --skill kamal-deployment
SKILL.md
Kamal 2 Deployment

Kamal is a deployment tool by 37signals that deploys containerized applications to any Linux server using Docker, SSH, and Kamal Proxy. It offers zero-downtime deploys, rolling restarts, automatic SSL/TLS certificates, and auxiliary services management.

Quick Start
# Install
gem install kamal

# Initialize in your project
kamal init
# Creates: config/deploy.yml, .kamal/secrets, .kamal/hooks/

# First deploy (bootstraps servers + deploys)
kamal setup

# Subsequent deploys
kamal deploy

Key Concepts
Service: Your application name, used to uniquely configure containers
Server: A virtual or physical host running your application image
Role: A server group running the same command (e.g., web, job)
Accessory: A long-running auxiliary service (database, Redis) with independent lifecycle
Kamal Proxy: Reverse proxy for zero-downtime deploys and SSL termination on each server
Kamal 2 provides its own private network called kamal - do NOT add a custom private network in your config
Configuration Reference

For complete deploy.yml configuration, see configuration.md.

Workflows
Initial Setup
Run kamal init to generate config files
Configure config/deploy.yml (see configuration.md)
Set up .kamal/secrets with registry credentials and app secrets
Ensure your app has a Dockerfile exposing port 80 with a /up health check
Set config.assume_ssl = true and config.force_ssl = true in production.rb
Exclude /up from host authorization in Rails 7+:
config.host_authorization = { exclude: ->(request) { request.path == "/up" } }

Run kamal setup for the first deployment
Deploying Updates
kamal deploy                    # Full deploy (build + push + deploy)
kamal deploy --skip-push        # Deploy existing image from registry
kamal deploy --version=VERSION  # Deploy specific version

Managing Accessories
kamal accessory boot all        # Boot all accessories
kamal accessory boot postgres   # Boot specific accessory
kamal accessory reboot redis    # Reboot an accessory
kamal accessory remove postgres # Remove an accessory
kamal accessory details postgres
kamal accessory logs postgres

Maintenance & Debugging
# Logs
kamal app logs                  # Application logs
kamal app logs -f               # Follow logs
kamal app logs -r web           # Logs for specific role
kamal proxy logs                # Proxy logs

# Console access
kamal app exec -i 'bin/rails console'
kamal app exec -i --reuse bash  # Shell into running container
kamal app exec --primary "bin/rails about"

# Rollback
kamal app containers            # List available versions
kamal rollback [VERSION]         # Rollback to version

# Redeploy (skip bootstrap, proxy setup, pruning, registry login)
kamal redeploy

# Locks
kamal lock status               # Check deploy lock
kamal lock acquire -m "reason"  # Prevent deploys
kamal lock release              # Allow deploys again

# Server management
kamal server bootstrap          # Bootstrap servers with Docker
kamal details                   # Show details about all containers
kamal audit                     # Show audit log from servers
kamal prune                     # Prune old images and containers
kamal config                    # Show combined config (includes secrets!)
kamal docs [SECTION]            # Show Kamal configuration docs

# Cleanup
kamal remove                    # Remove everything from servers

Global Flags
Flag	Description
-v, --verbose	Detailed logging
-q, --quiet	Minimal logging
--version=VERSION	Run against specific app version
-p, --primary	Primary host only
-h, --hosts=HOSTS	Comma-separated hosts (supports wildcards)
-r, --roles=ROLES	Comma-separated roles (supports wildcards)
-d, --destination	Deployment destination
-H, --skip-hooks	Skip hook execution
Database Operations
# Run migrations via entrypoint (recommended)
# bin/docker-entrypoint handles db:prepare automatically

# Or via pre-deploy hook
kamal app exec -p -q -d $KAMAL_DESTINATION --version $KAMAL_VERSION "rails db:migrate"

# Database backup (with S3 backup accessory)
kamal accessory exec s3_backup "sh backup.sh"
kamal accessory exec s3_backup "sh restore.sh"

Architecture Patterns

For complete examples of single-server and multi-server setups, see examples.md.

Single Server (Rails + PostgreSQL + Redis + Sidekiq)

All services on one VPS with Let's Encrypt SSL. Best for small-to-medium apps.

Multi-Server (Scaled)

Separate servers for web, job, database, and cache behind a load balancer on a private network. Best for high-traffic apps.

Hooks

Custom scripts in .kamal/hooks/ that run at deployment points. If a hook returns non-zero, the command aborts.

Available: docker-setup, pre-connect, pre-build, pre-deploy, post-deploy, pre-app-boot, post-app-boot, pre-proxy-reboot, post-proxy-reboot.

For details, see configuration.md.

Upgrading from Kamal 1
kamal upgrade              # In-place upgrade from Kamal 1 to 2
kamal upgrade --rolling    # Zero-downtime upgrade
kamal downgrade            # Reverse if needed

Common Gotchas
Kamal 2 creates its own kamal network - remove any custom private network from your config
Always set config.assume_ssl = true in production.rb when using SSL
Do NOT use your domain name as the VM hostname - it overrides /etc/resolv.conf
Docker port exposure bypasses UFW - closing ports in UFW is not enough, Docker rules are higher in iptables
Short deploy_timeout causes failures on underpowered servers - increase it if deploys fail
Asset bridging must be explicitly configured with asset_path - it's not automatic
Accessories must be removed before moving to a new destination
Kamal 2 doesn't support ERB in config/deploy.yml (unlike Kamal 1)
Set config.reload_routes = false in Devise initializer to fix ActionController::RoutingError
Enable forward_headers: true in proxy config when behind Cloudflare to preserve real client IPs
CI/CD

For GitHub Actions deployment workflows, see cicd.md.

Backups

For database backup strategies with S3, see backups.md.

Server Hardening

For production server security setup, see server-hardening.md.

Logging & Monitoring

For Vector log aggregation and structured logging, see logging.md.

Weekly Installs
30
Repository
faqndo97/ai-skills
GitHub Stars
32
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass