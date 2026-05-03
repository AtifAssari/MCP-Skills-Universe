---
rating: ⭐⭐
title: extract-test-set
url: https://skills.sh/tradingstrategy-ai/web3-ethereum-defi/extract-test-set
---

# extract-test-set

skills/tradingstrategy-ai/web3-ethereum-defi/extract-test-set
extract-test-set
Installation
$ npx skills add https://github.com/tradingstrategy-ai/web3-ethereum-defi --skill extract-test-set
SKILL.md
Extract test set from raw prices

This is a skill to extract price data from the raw prices for an isolated unit test.

Inputs
Smart contract address and a blockchain as a blockchain explorer link
Test case name
Relevant files

Seek metadata and Parquet information here:

vault database
data wrangling
Ad-hoc script

Create an ad-hoc Python script that reads

Script inputs

chain id (numeric) - address tuple
test case name

Scripts

Extracts the price series from DEFAULT_UNCLEANED_PRICE_DATABASE

Script outputs

Pytest test module with a single test case
Related Parquet file containing price data only for this vault
Write test case

Then the script creates test_xxx file, stores metadata there inline and creates corresponding test_xxx_price.parquet file for the test case to read.

Include only a single test function, do not generate excessive tests
Run the script
After running the script, run the generated test case
Weekly Installs
51
Repository
tradingstrategy…eum-defi
GitHub Stars
806
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass