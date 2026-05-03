---
title: miniqmt-skills
url: https://skills.sh/zxzvsdcj/miniqmt-skills/miniqmt-skills
---

# miniqmt-skills

skills/zxzvsdcj/miniqmt-skills/miniqmt-skills
miniqmt-skills
Installation
$ npx skills add https://github.com/zxzvsdcj/miniqmt-skills --skill miniqmt-skills
SKILL.md
MiniQMT / XtQuant Skill

Use this skill to deliver executable, risk-aware XtQuant solutions quickly.

Workflow
Verify runtime prerequisites.
Load only the reference file needed for the current subtask.
Build the smallest runnable script first, then extend.
Add callback-safe logic (non-blocking, recoverable).
Validate with a simulated account before live trading.
Runtime Prerequisites
Start MiniQMT client before running Python code.
Use 64-bit Python 3.6 to 3.12.
Point path to the correct user directory:
Broker client: ...\\userdata_mini
Research client: ...\\userdata
Use a unique session_id per strategy process.
Keep reconnect interval > 3 seconds for the same session_id.
Reference Map
references/getting_started.md: environment, startup sequence, minimal bootstrap.
references/api.md: full API index (quick lookup).
references/xtdata_api.md: market data APIs and return shapes.
references/xttrader_api.md: trading APIs, callbacks, account/query flow.
references/data_structures.md: tick/kline fields, financial fields, trade objects, constants.
references/examples.md: end-to-end strategy templates.
references/troubleshooting.md: common errors and operational guardrails.
references/index.md: navigation and search shortcuts.
Implementation Guardrails
Download required history (download_*) before reading local historical series.
Use get_market_data_ex as the default read API.
Keep callback handlers fast; move heavy logic to queues/workers.
Stock order volume should follow lot rules (typically multiples of 100).
order_remark in MiniQMT has length limits; avoid long Chinese text.
Do not hardcode account IDs, tokens, or live credentials in source files.
Minimal Bootstraps
xtdata quick check
from xtquant import xtdata

xtdata.download_history_data("000001.SZ", period="1d", incrementally=True)
data = xtdata.get_market_data_ex(["close"], ["000001.SZ"], period="1d", count=5)
print(data["close"])

xttrader quick check
import time
from xtquant.xttrader import XtQuantTrader
from xtquant.xttype import StockAccount

path = r"D:\\迅投极速交易终端 睿智融科版\\userdata_mini"
session_id = int(time.time())
trader = XtQuantTrader(path, session_id)
account = StockAccount("YOUR_ACCOUNT", "STOCK")

trader.start()
print("connect:", trader.connect())
print("subscribe:", trader.subscribe(account))

Weekly Installs
14
Repository
zxzvsdcj/miniqmt-skills
GitHub Stars
1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn