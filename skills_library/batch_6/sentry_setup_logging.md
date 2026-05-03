---
title: sentry-setup-logging
url: https://skills.sh/getsentry/sentry-agent-skills/sentry-setup-logging
---

# sentry-setup-logging

skills/getsentry/sentry-agent-skills/sentry-setup-logging
sentry-setup-logging
Installation
$ npx skills add https://github.com/getsentry/sentry-agent-skills --skill sentry-setup-logging
SKILL.md
Setup Sentry Logging

Configure Sentry's structured logging feature.

Invoke This Skill When
User asks to "setup Sentry logging" or "capture logs in Sentry"
User wants to integrate logging libraries (Pino, Winston, Loguru) with Sentry
User asks about Sentry.logger or sentry_sdk.logger

Important: The SDK versions, API names, and code samples below are examples. Always verify against docs.sentry.io before implementing, as APIs and minimum versions may have changed.

Quick Reference
Platform	Min SDK	Enable Flag	Logger API
JavaScript	9.41.0+	enableLogs: true	Sentry.logger.*
Python	2.35.0+	enable_logs=True	sentry_sdk.logger.*
Ruby	5.24.0+	config.enable_logs = true	Sentry.logger.*
JavaScript Setup
1. Verify SDK version
grep -E '"@sentry/(nextjs|react|node|browser)"' package.json

2. Enable in Sentry.init()
Sentry.init({
  dsn: "YOUR_DSN",
  enableLogs: true,
});

3. Console capture (optional)
integrations: [
  Sentry.consoleLoggingIntegration({ levels: ["warn", "error"] }),
],

4. Use structured logging
Sentry.logger.info("User logged in", { userId: "123" });
Sentry.logger.error("Payment failed", { orderId: "456", amount: 99.99 });

// Template literals (creates searchable attributes)
Sentry.logger.info(Sentry.logger.fmt`User ${userId} purchased ${productName}`);

Third-party integrations
Library	Integration	Min SDK
Consola	Sentry.createConsolaReporter()	10.12.0+
Console capture	Sentry.consoleLoggingIntegration()	10.13.0+
Python Setup
1. Verify SDK version
pip show sentry-sdk | grep Version

2. Enable in init()
sentry_sdk.init(
    dsn="YOUR_DSN",
    enable_logs=True,
)

3. Stdlib logging capture (optional)
from sentry_sdk.integrations.logging import LoggingIntegration
integrations=[LoggingIntegration(sentry_logs_level=logging.INFO)]

4. Use structured logging
from sentry_sdk import logger as sentry_logger

sentry_logger.info("User logged in: {user_id}", user_id="123")
sentry_logger.error("Payment failed", order_id="456", amount=99.99)

Loguru integration
from sentry_sdk.integrations.loguru import LoguruIntegration
integrations=[LoguruIntegration(sentry_logs_level=LoggingLevels.INFO.value)]

Ruby Setup
1. Verify SDK version
bundle show sentry-ruby

2. Enable in init
Sentry.init do |config|
  config.dsn = "YOUR_DSN"
  config.enable_logs = true
  config.enabled_patches << :logger  # Optional: capture stdlib Logger
end

3. Use structured logging
Sentry.logger.info("User logged in")
Sentry.logger.error("Payment failed. Order: %{order_id}", order_id: "456")

Log Filtering
JavaScript
beforeSendLog: (log) => log.level === "info" ? null : log,

Python
def before_send_log(log, hint):
    return None if log["severity_text"] == "info" else log

Verification

After enabling logs, emit a test log and check the Sentry Logs dashboard (Explore > Logs):

Sentry.logger.info("Sentry logging test");

Troubleshooting
Issue	Solution
Logs not appearing	Verify SDK version, check enableLogs/enable_logs is set
Too many logs	Use beforeSendLog to filter, reduce captured levels
Console not captured	Add consoleLoggingIntegration to integrations array
Weekly Installs
264
Repository
getsentry/sentr…t-skills
GitHub Stars
19
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass