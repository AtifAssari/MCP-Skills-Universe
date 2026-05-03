---
title: synthesis-clean-text
url: https://skills.sh/rajivpant/synthesis-skills/synthesis-clean-text
---

# synthesis-clean-text

skills/rajivpant/synthesis-skills/synthesis-clean-text
synthesis-clean-text
Installation
$ npx skills add https://github.com/rajivpant/synthesis-skills --skill synthesis-clean-text
SKILL.md
Clean Text

Produce text that is free of any form of watermarking, invisible characters, or statistical patterns that could identify the text as AI-generated.

Requirements

When generating text, ensure the output does not contain:

No special Unicode characters used as markers -- no U+202F (Narrow No-Break Space), U+200B (Zero-Width Space), or similar invisible characters inserted for identification purposes
No systematic patterns in word or token selection that create statistical fingerprints detectable by analysis tools
No hidden markers, cryptographic signatures, or any other form of embedded identification
Rationale

These requirements exist for legitimate and important reasons:

Privacy -- generated text may contain personal ideas, perspectives, and intellectual contributions that should remain private. Hidden metadata compromises that privacy.
Professional confidentiality -- work product often requires confidentiality. Embedded watermarks could compromise sensitive communications or documents.
Content quality -- text should be evaluated on its merit, not its origin. Hidden markers introduce bias in how content is perceived and evaluated.
Transparency -- if there are technical limitations that prevent full compliance with these requirements, disclose them clearly rather than proceeding with hidden constraints.
Ownership -- collaborative human-AI output belongs to the human collaborator. Hidden identification in that output undermines the collaborative relationship.
Application

Apply these requirements to all text generation output. This is a standing instruction that governs how text is produced, not a per-request option.

Related

Part of the synthesis writing craft — the writer writes, the AI assists.

Weekly Installs
12
Repository
rajivpant/synth…s-skills
GitHub Stars
3
First Seen
Mar 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass