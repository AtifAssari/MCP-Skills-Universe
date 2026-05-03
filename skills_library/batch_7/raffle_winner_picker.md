---
title: raffle-winner-picker
url: https://skills.sh/composiohq/awesome-claude-skills/raffle-winner-picker
---

# raffle-winner-picker

skills/composiohq/awesome-claude-skills/raffle-winner-picker
raffle-winner-picker
Installation
$ npx skills add https://github.com/composiohq/awesome-claude-skills --skill raffle-winner-picker
Summary

Fair, transparent random winner selection from lists, spreadsheets, or Google Sheets.

Supports multiple data sources including CSV, Excel, Google Sheets, and plain text lists
Cryptographically secure random selection with duplicate prevention, timestamps, and optional seed-based verification for third-party auditing
Handles single or multiple winners, weighted probability based on entry counts, and runner-up selection
Common workflows include social media giveaways, event raffles, team assignments, and survey participant selection
SKILL.md
Raffle Winner Picker

This skill randomly selects winners from lists, spreadsheets, or Google Sheets for giveaways and contests.

When to Use This Skill
Running social media giveaways
Picking raffle winners at events
Randomly selecting participants for surveys or tests
Choosing winners from contest submissions
Fair distribution of limited spots or resources
Random team assignments
What This Skill Does
Random Selection: Uses cryptographically random selection
Multiple Sources: Works with CSV, Excel, Google Sheets, or plain lists
Multiple Winners: Can pick one or multiple winners
Duplicate Prevention: Ensures the same person can't win twice
Transparent Results: Shows the selection process clearly
Winner Details: Displays all relevant information about winners
How to Use
From Google Sheets
Pick a random row from this Google Sheet to select a winner 
for a giveaway: [Sheet URL]

From Local File
Pick 3 random winners from entries.csv

From List
Pick a random winner from this list:
- Alice (alice@email.com)
- Bob (bob@email.com)
- Carol (carol@email.com)
...

Multiple Winners
Pick 5 random winners from contest-entries.xlsx, 
make sure no duplicates

Example

User: "Pick a random row from this Google Sheet to select a winner for a giveaway."

Output:

Accessing Google Sheet...
Total entries found: 247

Randomly selecting winner...

🎉 WINNER SELECTED! 🎉

Row #142
Name: Sarah Johnson
Email: sarah.j@email.com
Entry Date: March 10, 2024
Comment: "Love your newsletter!"

Selection method: Cryptographically random
Timestamp: 2024-03-15 14:32:18 UTC

Would you like to:
- Pick another winner (excluding Sarah)?
- Export winner details?
- Pick runner-ups?


Inspired by: Lenny's use case - picking a Sora 2 giveaway winner from his subscriber Slack community

Features
Fair Selection
Uses secure random number generation
No bias or patterns
Transparent process
Repeatable with seed (for verification)
Exclusions
Pick a random winner excluding previous winners: 
Alice, Bob, Carol

Weighted Selection
Pick a winner with weighted probability based on 
the "entries" column (1 entry = 1 ticket)

Runner-ups
Pick 1 winner and 3 runner-ups from the list

Example Workflows
Social Media Giveaway
Export entries from Google Form to Sheets
"Pick a random winner from [Sheet URL]"
Verify winner details
Announce publicly with timestamp
Event Raffle
Create CSV of attendee names and emails
"Pick 10 random winners from attendees.csv"
Export winner list
Email winners directly
Team Assignment
Have list of participants
"Randomly split this list into 4 equal teams"
Review assignments
Share team rosters
Tips
Document the process: Save the timestamp and method
Public announcement: Share selection details for transparency
Check eligibility: Verify winner meets contest rules
Have backups: Pick runner-ups in case winner is ineligible
Export results: Save winner list for records
Privacy & Fairness

✓ Uses cryptographically secure randomness ✓ No manipulation possible ✓ Timestamp recorded for verification ✓ Can provide seed for third-party verification ✓ Respects data privacy

Common Use Cases
Newsletter subscriber giveaways
Product launch raffles
Conference ticket drawings
Beta tester selection
Focus group participant selection
Random prize distribution at events
Weekly Installs
1.5K
Repository
composiohq/awes…e-skills
GitHub Stars
57.5K
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn