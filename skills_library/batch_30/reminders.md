---
title: reminders
url: https://skills.sh/ticruz38/skills/reminders
---

# reminders

skills/ticruz38/skills/reminders
reminders
Installation
$ npx skills add https://github.com/ticruz38/skills --skill reminders
SKILL.md
Reminders Skill

Set and manage one-time or recurring reminders. Stores all data locally in SQLite. No external APIs required.

Features
One-time reminders: Set reminders for specific dates/times
Recurring reminders: Daily, weekly, or monthly recurring reminders
Natural language parsing: "in 2 hours", "tomorrow", "14:30"
Snooze functionality: Temporarily dismiss reminders
Daemon mode: Check for due reminders (for cron/systemd integration)
SQLite storage: All data stored locally
Capabilities
Add a one-time reminder
npx reminders add "<datetime>" "<message>"


Datetime formats:

"2026-02-15 14:00" - Specific date and time
"tomorrow" - Tomorrow at current time
"in 2 hours" - Relative time
"in 30 minutes" - Relative time in minutes
"in 3 days" - Relative time in days
"14:30" - Today at specific time (or tomorrow if passed)

Examples:

npx reminders add "in 30 minutes" "Call mom"
npx reminders add "tomorrow" "Dentist appointment"
npx reminders add "2026-02-15 09:00" "Team meeting"
npx reminders add "14:30" "Standup meeting"

Add a recurring reminder
npx reminders recurring <type> "<time>" "<message>"


Types: daily, weekly, monthly

Examples:

npx reminders recurring daily "09:00" "Take vitamins"
npx reminders recurring weekly "Monday 10:00" "Weekly review"
npx reminders recurring monthly "1st 12:00" "Pay rent"

List reminders
npx reminders list                    # List pending reminders
npx reminders list --all              # Include completed
npx reminders list --limit 20         # Limit results

List due reminders
npx reminders due                     # Show reminders that are due now

Get reminder details
npx reminders get <id>

Complete a reminder
npx reminders complete <id>


For recurring reminders, this schedules the next occurrence. For one-time reminders, it moves to history.

Snooze a reminder
npx reminders snooze <id> <minutes>


Example:

npx reminders snooze 123 30          # Snooze for 30 minutes

Delete a reminder
npx reminders delete <id>

View history
npx reminders history                 # Show completed reminders
npx reminders history --limit 50      # Show last 50

View statistics
npx reminders stats                   # Show pending, completed, overdue counts

Daemon mode

Check for due reminders (for use with cron or systemd):

npx reminders daemon                  # Output JSON with due reminders


Cron example:

# Check for reminders every minute
* * * * * /usr/bin/node /path/to/dist/cli.js daemon | some-notifier

Health check
npx reminders health                  # Check database status

Test natural language parsing
npx reminders parse "in 2 hours"      # Test how a datetime string is parsed

Storage

SQLite database at ~/.openclaw/skills/reminders/reminders.db:

reminders - All active reminders with schedule info
history - Completed one-time reminders
API Usage
import { RemindersSkill } from '@openclaw/reminders';

const reminders = new RemindersSkill();

// Add a one-time reminder
const reminder = await reminders.addReminder({
  message: "Call mom",
  scheduledAt: new Date("2026-02-15T14:00:00"),
});

// Parse natural language datetime
const when = reminders.parseNaturalDateTime("in 2 hours");
await reminders.addReminder({
  message: "Take a break",
  scheduledAt: when,
});

// Add recurring reminder
await reminders.addRecurringReminder({
  message: "Take vitamins",
  type: "daily",
});

// List due reminders
const due = await reminders.getDueReminders();

// Complete a reminder
await reminders.completeReminder(reminder.id);

// Snooze for 30 minutes
await reminders.snoozeReminder(reminder.id, 30);

// Close connection
await reminders.close();

No External Dependencies

This skill works entirely offline:

No API keys required
No external services
All data stored in local SQLite
Natural language parsing is done locally
Weekly Installs
28
Repository
ticruz38/skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass