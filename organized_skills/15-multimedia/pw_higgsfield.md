---
rating: ⭐⭐
title: pw-higgsfield
url: https://skills.sh/alb-o/pw-rs/pw-higgsfield
---

# pw-higgsfield

skills/alb-o/pw-rs/pw-higgsfield
pw-higgsfield
Installation
$ npx skills add https://github.com/alb-o/pw-rs --skill pw-higgsfield
SKILL.md
higgsfield ai

generate images and videos with higgsfield ai using pw and higgsfield.nu.

setup

requires cdp connection to your browser with an active higgsfield session:

pw exec connect --input '{"launch":true}'
pw exec navigate --input '{"url":"https://higgsfield.ai"}'

invocation
use pw.nu
use higgsfield.nu *

generation

higgsfield create-image generate image.

--model (-m): default nano_banana_2.
--wait-for-result (-w): wait for completion.
--spend: allow credit usage.

higgsfield create-video generate video.

--model (-m): default wan_2_6.
--wait-for-result (-w): wait for completion (5min timeout).
--spend: allow credit usage.
unlimited mode

commands auto-check/enable "unlimited" toggle. use --spend if unlimited unavailable.

see higgsfield.md for full reference.

Weekly Installs
12
Repository
alb-o/pw-rs
GitHub Stars
3
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn