---
title: ai-scanner-garak
url: https://skills.sh/aradotso/trending-skills/ai-scanner-garak
---

# ai-scanner-garak

skills/aradotso/trending-skills/ai-scanner-garak
ai-scanner-garak
Installation
$ npx skills add https://github.com/aradotso/trending-skills --skill ai-scanner-garak
SKILL.md
AI Scanner (0din-ai/ai-scanner)

Skill by ara.so — Daily 2026 Skills collection.

AI Scanner is an open-source Ruby on Rails web application for AI model security assessments, wrapping NVIDIA garak with a multi-tenant UI, scheduling, PDF reports, and SIEM integration. It runs 179 community probes across 35 vulnerability families aligned with the OWASP LLM Top 10.

Installation
Quick Install (Docker)
curl -sL https://raw.githubusercontent.com/0din-ai/ai-scanner/main/scripts/install.sh | bash

Manual Install
curl -O https://raw.githubusercontent.com/0din-ai/ai-scanner/main/dist/docker-compose.yml
curl -O https://raw.githubusercontent.com/0din-ai/ai-scanner/main/.env.example
cp .env.example .env


Edit .env with required values:

# Generate a secure key
openssl rand -hex 64

# .env minimum required values
SECRET_KEY_BASE=<output_of_above_command>
POSTGRES_PASSWORD=<your_secure_db_password>

docker compose up -d


Access at http://localhost — default credentials: admin@example.com / password.
Change the default password immediately after first login.

Configuration (.env)
# Required
SECRET_KEY_BASE=<64-byte-hex>
POSTGRES_PASSWORD=<strong-password>

# Optional: custom port
PORT=8080

# Optional: SIEM integration
SPLUNK_HEC_URL=https://splunk.example.com:8088/services/collector
SPLUNK_HEC_TOKEN=$SPLUNK_HEC_TOKEN
RSYSLOG_HOST=syslog.example.com
RSYSLOG_PORT=514

# Optional: email
SMTP_HOST=smtp.example.com
SMTP_PORT=587
SMTP_USERNAME=$SMTP_USERNAME
SMTP_PASSWORD=$SMTP_PASSWORD

Core Concepts
Concept	Description
Target	An AI system to test — API-based LLM or browser-based chat UI
Probe	A single attack test (e.g., prompt injection, data leakage)
Scan	A run of selected probes against a target
ASR	Attack Success Rate — percentage of probes that succeeded
Organization	Tenant boundary; users and scans are scoped per org
Setting Up a Target

Targets define what you're scanning. Two types:

API-based LLM Target (e.g., OpenAI-compatible endpoint):

# In Rails console or via UI — representative model
target = Target.create!(
  name: "Production GPT-4",
  target_type: "api",
  api_endpoint: "https://api.openai.com/v1/chat/completions",
  api_key: ENV["OPENAI_API_KEY"],
  model_name: "gpt-4",
  organization: current_organization
)


Browser-based Chat UI Target:

target = Target.create!(
  name: "Internal Chatbot UI",
  target_type: "browser",
  url: "https://chatbot.internal.example.com",
  organization: current_organization
)

Running a Scan
Via UI
Navigate to Targets → select your target
Click New Scan
Select probe families or individual probes
Click Run Scan
Via Rails Console
# On-demand scan with specific probe families
scan = Scan.create!(
  target: target,
  probe_families: ["prompt_injection", "data_leakage", "insecure_output"],
  organization: current_organization
)
ScanJob.perform_later(scan.id)

Scheduled Recurring Scan
# Weekly scan every Monday at 2am
scheduled_scan = ScheduledScan.create!(
  target: target,
  probe_families: ["prompt_injection", "jailbreak"],
  cron_expression: "0 2 * * 1",
  organization: current_organization
)

Probe Families (35 total, aligned to OWASP LLM Top 10)

Key probe families available:

# List all available probe families
Garak::ProbeRegistry.families
# => ["prompt_injection", "jailbreak", "data_leakage", "insecure_output",
#     "supply_chain", "sensitive_info", "excessive_agency", "overreliance",
#     "model_theft", "malicious_plugins", ...]

# Get probes within a family
Garak::ProbeRegistry.probes_for("prompt_injection")
# => 179 total probes across all families

Viewing Results
Attack Success Rate (ASR)
scan = Scan.find(scan_id)

puts scan.asr_score          # => 0.23 (23% attack success rate)
puts scan.status             # => "completed"
puts scan.probe_results.count # => 47

# Per-probe breakdown
scan.probe_results.each do |result|
  puts "#{result.probe_name}: #{result.passed? ? 'SAFE' : 'VULNERABLE'}"
  puts "  Attempts: #{result.attempt_count}"
  puts "  ASR: #{result.asr_score}"
end

Trend Tracking
# Compare ASR across scan runs for a target
target.scans.completed.order(:created_at).map do |scan|
  { date: scan.created_at, asr: scan.asr_score }
end

PDF Report Export
# Generate PDF report for a scan
scan = Scan.find(scan_id)
pdf_path = ReportExporter.export_pdf(scan)
# Includes: executive summary, per-probe results, per-attempt drill-down


Via UI: Navigate to a completed scan → Export PDF.

SIEM Integration
Splunk
# config/initializers/siem.rb
SiemIntegration.configure do |config|
  config.provider = :splunk
  config.splunk_hec_url = ENV["SPLUNK_HEC_URL"]
  config.splunk_hec_token = ENV["SPLUNK_HEC_TOKEN"]
  config.forward_on_completion = true
end

Rsyslog
SiemIntegration.configure do |config|
  config.provider = :rsyslog
  config.rsyslog_host = ENV["RSYSLOG_HOST"]
  config.rsyslog_port = ENV["RSYSLOG_PORT"].to_i
end

Multi-Tenant Organization Management
# Create a new organization
org = Organization.create!(name: "Security Team Alpha")

# Invite a user
user = User.invite!(
  email: "analyst@example.com",
  organization: org,
  role: "analyst"   # roles: "admin", "analyst", "viewer"
)

# Data is encrypted at rest per organization
org.encryption_key  # => managed automatically

Development Setup
git clone https://github.com/0din-ai/ai-scanner.git
cd ai-scanner
cp .env.example .env.development

# Install dependencies
bundle install

# Database setup
rails db:create db:migrate db:seed

# Install garak (Python dependency)
pip install garak

# Start development server
bin/dev

Running Tests
# Full test suite
bundle exec rspec

# Specific area
bundle exec rspec spec/models/scan_spec.rb
bundle exec rspec spec/jobs/scan_job_spec.rb

# Lint
bundle exec rubocop

Common Patterns
Testing a New LLM Before Deployment
# Comprehensive pre-deployment scan
target = Target.create!(
  name: "New Model v2 - Pre-deploy",
  target_type: "api",
  api_endpoint: ENV["NEW_MODEL_ENDPOINT"],
  api_key: ENV["NEW_MODEL_API_KEY"],
  model_name: "new-model-v2",
  organization: current_organization
)

# Run all 35 probe families
scan = Scan.create!(
  target: target,
  probe_families: Garak::ProbeRegistry.families,
  organization: current_organization
)
ScanJob.perform_now(scan.id)

if scan.reload.asr_score > 0.15
  puts "WARNING: ASR #{scan.asr_score} exceeds threshold. Review before deploying."
else
  puts "PASS: Model meets security threshold."
end

Using the Mock LLM for Testing Scanner Setup

The built-in Mock LLM lets you validate your scanner configuration without hitting real APIs:

target = Target.create!(
  name: "Mock LLM",
  target_type: "mock",
  organization: current_organization
)
# Run a quick scan to verify everything works end-to-end

Webhook on Scan Completion
# config/initializers/scan_hooks.rb
ActiveSupport::Notifications.subscribe("scan.completed") do |_, _, _, _, payload|
  scan = Scan.find(payload[:scan_id])
  if scan.asr_score > 0.20
    SlackNotifier.alert(
      channel: "#security-alerts",
      message: "High ASR detected: #{scan.asr_score} on #{scan.target.name}"
    )
  end
end

Docker Compose Production Tips
# docker-compose.override.yml — production additions
services:
  web:
    environment:
      RAILS_ENV: production
      FORCE_SSL: "true"
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.scanner.rule=Host(`scanner.example.com`)"
      - "traefik.http.routers.scanner.tls.certresolver=letsencrypt"

# Upgrade
docker compose pull
docker compose up -d
docker compose exec web rails db:migrate

Troubleshooting
Problem	Solution
Scan stuck in "running"	Check docker compose logs worker — garak Python process may have crashed
SECRET_KEY_BASE error on start	Run openssl rand -hex 64 and set in .env
Can't connect to target API	Verify API key env var is set; check firewall allows outbound from container
Browser target scan fails	Ensure Playwright/Chrome is available in the worker container
PDF export blank	Check wkhtmltopdf is installed in the web container
SIEM not receiving events	Verify SPLUNK_HEC_URL includes full path /services/collector
# View all service logs
docker compose logs -f

# Check worker specifically (runs garak)
docker compose logs -f worker

# Rails console for debugging
docker compose exec web rails console

# Check garak is working
docker compose exec worker python -c "import garak; print(garak.__version__)"

Key Files (for Contributors)
app/
  models/
    scan.rb          # Core scan model, ASR calculation
    target.rb        # Target types and validation
    probe_result.rb  # Per-probe result storage
  jobs/
    scan_job.rb      # Async job that invokes garak
  services/
    garak_runner.rb  # Ruby wrapper around garak CLI
    report_exporter.rb
    siem_integration.rb
lib/
  garak/
    probe_registry.rb  # 179 probes, 35 families
dist/
  docker-compose.yml   # Production compose file
scripts/
  install.sh           # One-line installer

Resources
Full Documentation
Quick Start Guide
NVIDIA garak
OWASP LLM Top 10
CONTRIBUTING.md
SECURITY.md
Weekly Installs
647
Repository
aradotso/trending-skills
GitHub Stars
42
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykWarn