---
title: gmaps-cli
url: https://skills.sh/mic92/mics-skills/gmaps-cli
---

# gmaps-cli

skills/mic92/mics-skills/gmaps-cli
gmaps-cli
Installation
$ npx skills add https://github.com/mic92/mics-skills --skill gmaps-cli
SKILL.md
Usage
# Search for a specific place
gmaps-cli search "Nobu Malibu"

# Find nearby places
gmaps-cli nearby "coffee" --limit 5
gmaps-cli nearby "restaurants" --location "48.1351,11.5820" --limit 3

# Get directions
gmaps-cli route "Munich" "Berlin"
gmaps-cli route "Times Square" "Central Park" --mode walking
gmaps-cli route "Brooklyn" "Manhattan" --mode transit

Output Examples
Search
Nobu Malibu
22706 Pacific Coast Hwy, Malibu, CA 90265, USA
34.0259216, -118.6819819
Rating: 4.4 (1234 reviews)

Nearby
1. Blue Bottle Coffee
   123 Main St, Los Angeles, CA 90012, USA
   Rating: 4.5 $$

Route
Route from Los Angeles, CA, USA to San Francisco, CA, USA
Distance: 382 mi
Duration: 5 hours 48 mins


See README.md for setup and full documentation.

Weekly Installs
10
Repository
mic92/mics-skills
GitHub Stars
14
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn