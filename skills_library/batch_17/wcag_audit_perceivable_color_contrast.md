---
title: wcag-audit-perceivable-color-contrast
url: https://skills.sh/jkense/agent-skills-wcag/wcag-audit-perceivable-color-contrast
---

# wcag-audit-perceivable-color-contrast

skills/jkense/agent-skills-wcag/wcag-audit-perceivable-color-contrast
wcag-audit-perceivable-color-contrast
Installation
$ npx skills add https://github.com/jkense/agent-skills-wcag --skill wcag-audit-perceivable-color-contrast
SKILL.md
When to Use

Use this tool when checking color combinations for WCAG compliance, testing text readability, or validating non-text contrast ratios.

Usage
Command Line
node scripts/calculate.js --foreground "#000000" --background "#FFFFFF"
node scripts/calculate.js --fg "rgb(0,0,0)" --bg "rgb(255,255,255)"
node scripts/calculate.js --fg "#FF0000" --bg "#00FF00" --type "non-text"

JSON Input
node scripts/calculate.js --json '{"foreground": "#000000", "background": "#FFFFFF"}'

Parameters
--foreground, --fg: Foreground color (hex, rgb, hsl)
--background, --bg: Background color (hex, rgb, hsl)
--type: "text" (default) or "non-text"
--json: JSON input with color properties
Output

Returns JSON with contrast ratio and WCAG compliance levels:

{
  "contrastRatio": 21.0,
  "compliance": {
    "AA": {
      "normal": true,
      "large": true
    },
    "AAA": {
      "normal": true,
      "large": true
    }
  },
  "colors": {
    "foreground": "#000000",
    "background": "#FFFFFF"
  }
}

Examples
Text Contrast Check
$ node scripts/calculate.js --fg "#000000" --bg "#FFFFFF"
Contrast Ratio: 21.0:1
✅ AA Large Text: PASS
✅ AA Normal Text: PASS
✅ AAA Large Text: PASS
✅ AAA Normal Text: PASS

Non-Text Contrast Check
$ node scripts/calculate.js --fg "#FF6B35" --bg "#F7F3E9" --type "non-text"
Contrast Ratio: 3.2:1
✅ Non-text contrast: PASS

WCAG Standards
Text AA: 4.5:1 for normal text, 3:1 for large text (18pt+ or 14pt+ bold)
Text AAA: 7:1 for normal text, 4.5:1 for large text
Non-text: 3:1 minimum contrast ratio
Learn More

For more information about Agent Skills and how they extend AI capabilities.

Weekly Installs
11
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