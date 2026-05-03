---
rating: ⭐⭐⭐
title: basket-settle
url: https://skills.sh/adityaakr/polybaskets/basket-settle
---

# basket-settle

skills/adityaakr/polybaskets/basket-settle
basket-settle
Installation
$ npx skills add https://github.com/adityaakr/polybaskets --skill basket-settle
SKILL.md
Basket Settle

Propose and finalize settlement for PolyBaskets baskets. ProposeSettlement requires the settler role. FinalizeSettlement does not require the settler role, but only works after the challenge deadline has passed.

Setup

MAINNET ONLY. Run vara-wallet config set network mainnet before anything else. NEVER switch to testnet — there are no contracts there.

vara-wallet config set network mainnet
BASKET_MARKET="0xe5dd153b813c768b109094a9e2eb496c38216b1dbe868391f1d20ac927b7d2c2"
_PB="${POLYBASKETS_SKILLS_DIR:-skills}"
IDL="$_PB/idl/polymarket-mirror.idl"

Verify Settler Role

Only the address assigned as settler_role in the contract config can call ProposeSettlement.

# Check who has settler role
vara-wallet call $BASKET_MARKET BasketMarket/GetConfig --args '[]' --idl $IDL | jq -r '.result.settler_role'

# Check agent's hex actor id
MY_ADDR=$(vara-wallet balance --account agent | jq -r .address)
echo "$MY_ADDR"


If your address does not match settler_role, you cannot propose a new settlement. You may still finalize an already proposed settlement after challenge_deadline.

Settlement Flow
1. Check basket is Active
2. Verify all items have resolved on Polymarket
3. ProposeSettlement → starts the configured challenge window
4. Wait for challenge_deadline to pass
5. FinalizeSettlement → basket becomes Settled, users can claim

Step 1: Check Basket Status
vara-wallet call $BASKET_MARKET BasketMarket/GetBasket \
  --args '[<basket_id>]' --idl $IDL | jq '.result.ok.status'


Must be "Active".

Step 2: Check Polymarket Resolution

For each item in the basket, check if the market has resolved on Polymarket:

curl -s "https://gamma-api.polymarket.com/markets?slug=<poly_slug>" | jq '.[0] | {closed, outcomePrices}'


All items must be resolved (closed: true) with final prices near 0 or 1.

Step 3: Propose Settlement

Build the item_resolutions array — one ItemResolution per basket item:

{
  "item_index": 0,
  "resolved": "YES",
  "poly_slug": "will-btc-hit-100k",
  "poly_condition_id": "0xabc123...",
  "poly_price_yes": 9900,
  "poly_price_no": 100
}


Rules:

Provide exactly one resolution per basket item
item_index is 0-based, must be unique, and within basket items range
poly_slug must match the basket item's slug exactly
poly_price_yes + poly_price_no should reflect final Polymarket prices in bps
resolved is the final outcome: "YES" or "NO"
poly_condition_id is optional
Example: Propose settlement for a 2-item basket
vara-wallet --account agent call $BASKET_MARKET BasketMarket/ProposeSettlement --voucher $VOUCHER_ID \
  --args '[
    0,
    [
      {
        "item_index": 0,
        "resolved": "YES",
        "poly_slug": "will-btc-hit-100k",
        "poly_condition_id": null,
        "poly_price_yes": 9900,
        "poly_price_no": 100
      },
      {
        "item_index": 1,
        "resolved": "NO",
        "poly_slug": "will-eth-hit-5k",
        "poly_condition_id": null,
        "poly_price_yes": 200,
        "poly_price_no": 9800
      }
    ],
    "Resolved via Polymarket API"
  ]' \
  --idl $IDL


After proposal, the basket enters SettlementPending status and the configured challenge window begins.

Step 4: Wait for Challenge Window
# Check challenge deadline
vara-wallet call $BASKET_MARKET BasketMarket/GetSettlement \
  --args '[<basket_id>]' --idl $IDL | jq '.result.ok | {status, challenge_deadline, proposed_at}'


The challenge_deadline is a block timestamp. The liveness window is configured in BasketMarket/GetConfig.liveness_ms; do not hardcode a duration.

Wait until the current block timestamp exceeds challenge_deadline.

Step 5: Finalize Settlement
vara-wallet --account agent call $BASKET_MARKET BasketMarket/FinalizeSettlement --voucher $VOUCHER_ID \
  --args '[<basket_id>]' --idl $IDL


After finalization:

Basket status becomes Settled
finalized_at is set
Users can now claim payouts via ../basket-claim/SKILL.md
Verify
vara-wallet call $BASKET_MARKET BasketMarket/GetSettlement \
  --args '[<basket_id>]' --idl $IDL | jq '.result.ok | {status, payout_per_share, finalized_at}'

Common Errors
Error	Cause	Fix
Unauthorized	Not the settler role for ProposeSettlement	Check config for settler_role address
BasketNotActive	Basket already in settlement	Check status
SettlementAlreadyExists	Already proposed	Wait and finalize
InvalidResolutionCount	Wrong number of resolutions	Provide one per item
ResolutionSlugMismatch	Slug doesn't match basket item	Use exact slug from basket
DuplicateResolutionIndex	Same item_index twice	Make indices unique
ResolutionIndexOutOfBounds	Index >= items count	Use 0 to items.length-1
ChallengeDeadlineNotPassed	Too early to finalize	Wait for challenge window
SettlementNotProposed	No proposal exists	Propose first
Weekly Installs
180
Repository
adityaakr/polybaskets
GitHub Stars
2
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn