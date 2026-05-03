---
title: add-vault-note
url: https://skills.sh/tradingstrategy-ai/web3-ethereum-defi/add-vault-note
---

# add-vault-note

skills/tradingstrategy-ai/web3-ethereum-defi/add-vault-note
add-vault-note
Installation
$ npx skills add https://github.com/tradingstrategy-ai/web3-ethereum-defi --skill add-vault-note
SKILL.md
Add vault note

This skill adda s human readable note to a specific vault in the database.

Required inputs

Before starting, gather the following information from the user:

Vault smart contract address - The address of an example vault contract on a blockchain
Message: A human readable message
Flags (optional): Flags from VaultFlag enum - if not given set to None
1. Resolve vault name

Can be resolved from https://top-defi-vaults.tradingstrategy.ai/top_vaults_by_chain.json JSON file

It's a list of JSON object records
Use search to find the record
Extract its name
Don't try to open the JSON file, as it is too large

Alternatively use check-vault-onchain.py.

2. Edit the flag.py

The vault notes are stored in ``eth_defi/vault/flag.py`.

Add the vault address VAULT_FLAGS_AND_NOTES

If the address already exist ask for user input
Make sure the address is lowercased
For the message create a Python constant like other messages have in flag.py
Set the message and flag in the dictionary
If the user explicitly did not tell you to use any flag, set flag to None
Add the vault name as a comment on the above line
3. Format code

Run ruff to make sure Python code is formatted.

4. Open PR
Open a pull request.
This is not a feature pull request - no need to add changelog entry
Prefix the pull request "notes" instead of "feat"
Weekly Installs
59
Repository
tradingstrategy…eum-defi
GitHub Stars
806
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn