---
title: get-block-number
url: https://skills.sh/tradingstrategy-ai/web3-ethereum-defi/get-block-number
---

# get-block-number

skills/tradingstrategy-ai/web3-ethereum-defi/get-block-number
get-block-number
Installation
$ npx skills add https://github.com/tradingstrategy-ai/web3-ethereum-defi --skill get-block-number
SKILL.md
Get latest block number

This skill retrieves the latest block number from a blockchain using the configured JSON-RPC environment variables and Web3.py.

ALWAYS USE SCRIPT. NEVER RELY ON THE HISTORICAL INFORMATION OR GUESS.

Required inputs
Chain name: The blockchain to query (e.g., Ethereum, Arbitrum, Base, Polygon)
Running the script

Generate and run a Python script to fetch the block number. Run it Python commadn line inline, don't write a new file.

import os
from web3 import Web3

from eth_defi.provider.multi_provider import create_multi_provider_web3

# Replace {CHAIN} with the uppercase chain name
json_rpc_url = os.environ.get("JSON_RPC_{CHAIN}")

if not json_rpc_url:
    raise ValueError("JSON_RPC_{CHAIN} environment variable not set")

web3 = create_multi_provider_web3(json_rpc_url)
block_number = web3.eth.block_number

print(f"Latest block number: {block_number}")


Run the script with:

source .local-test.env && poetry run python <script_path>

Display output

Return the block number to the user in a clear format, e.g.:

Chain: Ethereum
Latest block number: 19,234,567

Weekly Installs
68
Repository
tradingstrategy…eum-defi
GitHub Stars
806
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass