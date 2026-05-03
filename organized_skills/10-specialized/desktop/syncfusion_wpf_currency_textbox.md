---
rating: ⭐⭐
title: syncfusion-wpf-currency-textbox
url: https://skills.sh/syncfusion/wpf-ui-components-skills/syncfusion-wpf-currency-textbox
---

# syncfusion-wpf-currency-textbox

skills/syncfusion/wpf-ui-components-skills/syncfusion-wpf-currency-textbox
syncfusion-wpf-currency-textbox
Installation
$ npx skills add https://github.com/syncfusion/wpf-ui-components-skills --skill syncfusion-wpf-currency-textbox
SKILL.md
WPF CurrencyTextBox -- Quick Reference

This skill documents core usage patterns and links to concise reference pages for formatting, validation, styling, and advanced features.

Quick Start

Add the Syncfusion WPF package and drop a CurrencyTextBox in XAML:

<syncfusion:CurrencyTextBox Width="200" Value="1234.56" MinValue="0" MaxValue="10000" />


Bind in MVVM:

<syncfusion:CurrencyTextBox Value="{Binding Amount, UpdateSourceTrigger=PropertyChanged}" />

References
Getting started: references/getting-started.md
Formatting & culture: references/formatting-culture.md
Validation & restrictions: references/validation-restrictions.md
Appearance & styling: references/appearance-styling.md
Advanced features: references/advanced-features.md
Step interval & scrolling: references/step-interval-scrolling.md
Notes
Always use Value (not Text) to get/set the currency amount.
Format priority: dedicated properties > NumberFormat > Culture.
Range adorner requires both MinValue and MaxValue to be set.
Watermark requires UseNullOption = true.
Weekly Installs
48
Repository
syncfusion/wpf-…s-skills
GitHub Stars
2
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass