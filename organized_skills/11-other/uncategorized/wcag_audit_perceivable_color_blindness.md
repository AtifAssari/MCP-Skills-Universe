---
rating: ⭐⭐⭐
title: wcag-audit-perceivable-color-blindness
url: https://skills.sh/jkense/agent-skills-wcag/wcag-audit-perceivable-color-blindness
---

# wcag-audit-perceivable-color-blindness

skills/jkense/agent-skills-wcag/wcag-audit-perceivable-color-blindness
wcag-audit-perceivable-color-blindness
Installation
$ npx skills add https://github.com/jkense/agent-skills-wcag --skill wcag-audit-perceivable-color-blindness
SKILL.md
When to Use

Use this tool when designing color schemes to ensure accessibility for users with color vision deficiencies, testing color-dependent information, or validating color contrast for different types of color blindness.

Usage
Command Line
node scripts/simulate.js --color "#FF0000" --type protanopia
node scripts/simulate.js --color "rgb(255,0,0)" --type deuteranopia
node scripts/simulate.js --color "#00FF00" --type tritanopia

JSON Input
node scripts/simulate.js --json '{"color": "#FF0000", "type": "protanopia"}'

Parameters
--color: Color to simulate (hex, rgb)
--type: Type of color blindness (protanopia, deuteranopia, tritanopia)
--json: JSON input with color and type properties
Supported Color Blindness Types
Protanopia: Red-blind (missing red cones)
Deuteranopia: Green-blind (missing green cones)
Tritanopia: Blue-blind (missing blue cones)
Output

Returns JSON with simulated color values:

{
  "original": "#FF0000",
  "simulated": "#5A5A5A",
  "type": "protanopia",
  "description": "Red-blind simulation"
}

Examples
Simulate red color for protanopia
$ node scripts/simulate.js --color "#FF0000" --type protanopia
Original: #FF0000 (rgb(255,0,0))
Protanopia: #5A5A5A (rgb(90,90,90))
This red appears as a dark gray to someone with protanopia

Test multiple colors
$ node scripts/simulate.js --color "#00FF00" --type deuteranopia
Original: #00FF00 (rgb(0,255,0))
Deuteranopia: #8C8C8C (rgb(140,140,140))
This green appears as a medium gray to someone with deuteranopia

Best Practices
Don't rely on color alone: Use shapes, patterns, or text labels in addition to color
Test critical color combinations: Check that important information remains distinguishable
Consider contrast: Even with color blindness simulation, ensure adequate contrast ratios
Test all types: Check designs against all three main types of color blindness
Learn More

For more information about Agent Skills and how they extend AI capabilities.

Weekly Installs
8
Repository
jkense/agent-skills-wcag
GitHub Stars
1
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass