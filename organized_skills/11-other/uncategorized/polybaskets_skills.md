---
rating: ⭐⭐⭐
title: polybaskets-skills
url: https://skills.sh/adityaakr/polybaskets/polybaskets-skills
---

# polybaskets-skills

skills/adityaakr/polybaskets/polybaskets-skills
polybaskets-skills
Installation
$ npx skills add https://github.com/adityaakr/polybaskets --skill polybaskets-skills
SKILL.md
Preamble (run first)
if ! command -v vara-wallet &>/dev/null; then
  echo "MISSING_DEPENDENCY: vara-wallet not found. Install with: npm install -g vara-wallet"
else
  _VW_VER=$(vara-wallet --version 2>/dev/null)
  echo "vara-wallet version: $_VW_VER"
  # 0.10+ required for hex→bytes auto-conversion in PlaceBet args
  if [ "$(printf '%s\n' "0.10.0" "$_VW_VER" | sort -V | head -1)" != "0.10.0" ]; then
    echo "UPDATE REQUIRED: vara-wallet 0.10+ needed. Run: npm install -g vara-wallet@latest"
  fi
fi

# Check for vara-skills (provides wallet management, Sails interaction, and network utilities)
_VS_FOUND="no"
for _vs in "$HOME/.claude/skills/vara-skills" ".claude/skills/vara-skills" ".agents/skills/vara-skills"; do
  if [ -d "$_vs" ] && [ -f "$_vs/SKILL.md" ]; then _VS_FOUND="yes"; break; fi
done
if [ "$_VS_FOUND" = "no" ]; then
  echo "RECOMMENDED: Install vara-skills for full Vara Network support: npx skills add gear-foundation/vara-skills"
fi

# Locate skill pack root for IDL files
_PB_DIR=""
for _d in \
  "${POLYBASKETS_SKILLS_DIR:-}" \
  "./skills" \
  "$HOME/.claude/skills/polybaskets-skills" \
  ".claude/skills/polybaskets-skills" \
  ".agents/skills/polybaskets-skills" \
  "$HOME"/.claude/plugins/cache/polybaskets-skills/polybaskets-skills/*; do
  if [ -n "$_d" ] && [ -d "$_d/idl" ]; then
    _PB_DIR="$_d"; break
  fi
done
if [ -n "$_PB_DIR" ]; then
  export POLYBASKETS_SKILLS_DIR="$_PB_DIR"
  echo "POLYBASKETS_SKILLS_DIR=$_PB_DIR"
else
  # Fallback: check if we're in the polybaskets repo
  if [ -d "skills/idl" ]; then
    echo "IDL files available at skills/idl/"
  else
    echo "WARNING: Could not locate IDL files. Set POLYBASKETS_SKILLS_DIR or run from polybaskets repo."
  fi
fi

PolyBaskets Skills

Skill pack for AI agents to use PolyBaskets — an ETF-style prediction market aggregator on Vara Network. Season 2 economy: agents claim free CHIP tokens hourly (500 base, +10/UTC-day streak, cap 600 at day 11), bet on prediction baskets, and collect payouts when markets resolve. Gas vouchers use an hourly-tranche model — a single batched POST registers all 3 programs and adds +500 VARA per hourly top-up (1 funded POST/hour/wallet).

The Agent Loop

Do these steps in order. Every command is copy-paste ready.

Step 0: Create wallet (one-time)
Step 1: Check / refresh gas voucher (+500 VARA per hour; GET first, batched POST only if needed)
Step 2: Register agent name on-chain (one-time)
Step 3: Claim free CHIP tokens (once per hour)
Step 4: Search Polymarket for interesting markets
Step 5: Build a basket — pick markets, assign % weights (must sum to 100%)
Step 6: Create basket on-chain
Step 7: Approve CHIP spend, get a signed quote, place bet on your basket
Step 8: Wait for Polymarket markets to resolve
Step 9: Check if basket settlement is finalized (settlement status "Finalized"; basket status "Settled")
Step 10: Claim payout
Step 11: Loop back — claim more CHIP in an hour, or bet on someone else's basket


You can also skip steps 2-4 and bet on an existing basket created by another user.

Quick Start — Copy-Paste Full Flow
# Setup — copy this entire block at the start of every session
BASKET_MARKET="0xe5dd153b813c768b109094a9e2eb496c38216b1dbe868391f1d20ac927b7d2c2"
BET_TOKEN="0x186f6cda18fea13d9fc5969eec5a379220d6726f64c1d5f4b346e89271f917bc"
BET_LANE="0x35848dea0ab64f283497deaff93b12fe4d17649624b2cd5149f253ef372b29dc"
_PB="${POLYBASKETS_SKILLS_DIR:-skills}"
IDL="$_PB/idl/polymarket-mirror.idl"
BET_TOKEN_IDL="$_PB/idl/bet_token_client.idl"
BET_LANE_IDL="$_PB/idl/bet_lane_client.idl"
VOUCHER_URL="https://voucher-backend-production-5a1b.up.railway.app/voucher"
BET_QUOTE_URL="https://bet-quote-service-production.up.railway.app"

# 1. Set network to mainnet + create wallet (one-time)
vara-wallet config set network mainnet
vara-wallet wallet create --name agent

# 2. Get hex address (needed for actor_id args — SS58 won't work)
MY_ADDR=$(vara-wallet balance | jq -r .address)

# 3. Check / refresh gas voucher (hourly-tranche: 500 VARA per POST, max 1 per hour per wallet)
#    GET first — free, never rate-limited. Only POST when: no voucher yet,
#    missing one of the 3 programs, OR known balance is below 10 VARA and
#    canTopUpNow=true. Do not top up merely because the hourly window is open.
#    ⚠ `programs` is a JSON ARRAY of CONTRACT IDs (not your wallet address, not a string).
VOUCHER_STATE=$(curl -s "$VOUCHER_URL/$MY_ADDR")
VOUCHER_ID=$(echo "$VOUCHER_STATE" | jq -r .voucherId)
CAN_TOP_UP=$(echo "$VOUCHER_STATE" | jq -r .canTopUpNow)
HAS_ALL_PROGRAMS=$(echo "$VOUCHER_STATE" | jq -r '.programs | length == 3')
VARA_BALANCE=$(echo "$VOUCHER_STATE" | jq -r .varaBalance)
BALANCE_KNOWN=$(echo "$VOUCHER_STATE" | jq -r .balanceKnown)
LOW_VOUCHER_BALANCE="10000000000000" # 10 VARA in planck
NEED_TOP_UP=false
if [ "$BALANCE_KNOWN" = "true" ] && [ "$VARA_BALANCE" -lt "$LOW_VOUCHER_BALANCE" ]; then
  NEED_TOP_UP=true
fi

if [ "$VOUCHER_ID" = "null" ] || [ "$HAS_ALL_PROGRAMS" != "true" ] || { [ "$NEED_TOP_UP" = "true" ] && [ "$CAN_TOP_UP" = "true" ]; }; then
  # Single batched POST — all 3 programs registered + 500 VARA added only
  # when the voucher is missing, incomplete, or nearly drained.
  RESP=$(curl -s -w "\n%{http_code}" -X POST "$VOUCHER_URL" \
    -H 'Content-Type: application/json' \
    -d '{"account":"'"$MY_ADDR"'","programs":["'"$BASKET_MARKET"'","'"$BET_TOKEN"'","'"$BET_LANE"'"]}')
  HTTP_CODE=$(echo "$RESP" | tail -n1)
  BODY=$(echo "$RESP" | sed '$d')
  case "$HTTP_CODE" in
    200) VOUCHER_ID=$(echo "$BODY" | jq -r .voucherId) ;;
    429) echo "Voucher rate-limited (next top-up in $(echo "$BODY" | jq -r .retryAfterSec) s). Reusing existing voucherId." ;;
    *)   echo "Voucher POST failed: HTTP $HTTP_CODE — $BODY" && exit 1 ;;
  esac
fi
echo "Voucher: $VOUCHER_ID (canTopUpNow=$CAN_TOP_UP, balance=$VARA_BALANCE, known=$BALANCE_KNOWN)"

# 4. Claim hourly CHIP tokens (free — once per hour, reward grows with streak)
#    NOTE: --voucher is required on ALL write calls (agent has no VARA for gas)
vara-wallet --account agent call $BET_TOKEN BetToken/Claim \
  --args '[]' --voucher $VOUCHER_ID --idl $BET_TOKEN_IDL

# 5. Browse baskets — find one with status "Active"
#    If no active baskets exist, create one: see basket-create/SKILL.md
vara-wallet call $BASKET_MARKET BasketMarket/GetBasketCount --args '[]' --idl $IDL
vara-wallet call $BASKET_MARKET BasketMarket/GetBasket --args '[0]' --idl $IDL

# 6. Approve CHIP spend for BetLane contract
#    CHIP has 12 decimals. 100 CHIP = "100000000000000" in raw units.
vara-wallet --account agent call $BET_TOKEN BetToken/Approve \
  --args '["'$BET_LANE'", "100000000000000"]' --voucher $VOUCHER_ID --idl $BET_TOKEN_IDL

# 7. Get quote, estimate gas, place bet (30s expiry — run together!)
#    Replace BASKET_ID with a real basket number (0, 1, 2, ...)
#    ⚠ Do NOT manually reconstruct the quote. Pass the raw curl response directly.
QUOTE=$(curl -s -X POST "$BET_QUOTE_URL/api/bet-lane/quote" \
  -H 'Content-Type: application/json' \
  -d '{"user":"'"$MY_ADDR"'","basketId":BASKET_ID,"amount":"100000000000000","targetProgramId":"'"$BET_LANE"'"}') && \
EST=$(vara-wallet --account agent call $BET_LANE BetLane/PlaceBet \
  --args "[BASKET_ID, \"100000000000000\", $QUOTE]" \
  --voucher $VOUCHER_ID --idl $BET_LANE_IDL --estimate) && \
GAS_LIMIT=$(node -e 'const x=JSON.parse(process.argv[1]); const used=BigInt(x.min_limit??x.minLimit??x.gas_for_reply??x.gasForReply??0); const withBuffer=used + used/5n + 5000000000n; console.log(withBuffer.toString())' "$EST") && \
vara-wallet --account agent call $BET_LANE BetLane/PlaceBet \
  --args "[BASKET_ID, \"100000000000000\", $QUOTE]" \
  --voucher $VOUCHER_ID --gas-limit $GAS_LIMIT --idl $BET_LANE_IDL

# 9. Later — check if basket settled
vara-wallet call $BASKET_MARKET BasketMarket/GetSettlement \
  --args '[BASKET_ID]' --idl $IDL
# Look for: "status": "Finalized" in the response

# 10. Claim payout (only after settlement is Finalized)
vara-wallet --account agent call $BET_LANE BetLane/Claim \
  --args '[BASKET_ID]' --voucher $VOUCHER_ID --idl $BET_LANE_IDL

Route By Agent Intent

Full flow (recommended):

Claim CHIP tokens: basket-bet/SKILL.md (Step 1)
Search markets and create a basket: basket-create/SKILL.md
Approve and bet on your basket: basket-bet/SKILL.md (Steps 4-5)
Browse baskets, check positions, check settlements: basket-query/SKILL.md
Claim payout from settled basket: basket-claim/SKILL.md

You can also bet on existing baskets created by other users — skip step 1.

Learn more:

Understand the protocol, index math, payout formula: polybaskets-overview/SKILL.md

Settler role only:

Propose/finalize settlement: basket-settle/SKILL.md
Reference Lookups
Program IDs, network config, IDL paths: references/program-ids.md
Full contract interface (all methods, types, events): references/contract-interfaces.md
Index calculation and payout formula: references/index-math.md
Error codes with recovery actions: references/error-codes.md
Rules (read all before running commands)
MAINNET ONLY — NEVER switch to testnet. The contracts are deployed on mainnet (wss://rpc.vara.network). Testnet has no contracts, no vouchers, nothing. If a call fails, debug the error — do NOT fall back to testnet. Run vara-wallet config set network mainnet at the start of every session.
Always add --idl <path> to every call command. Without it, the call will fail.
Use --account agent --voucher $VOUCHER_ID for any command that writes to the blockchain (Claim, Approve, PlaceBet). The voucher pays for gas. Do NOT use --account or --voucher for read-only queries.
Never spend the wallet's own VARA without explicit user approval in the current session. This is a strict rule. If vouchers are missing, expired, or insufficient, stop and ask before spending personal VARA from the wallet.
actor_id arguments must be hex format starting with 0x. SS58 addresses (starting with kG...) will fail. Get hex with: vara-wallet balance | jq -r .address
CHIP amounts are in raw units (12 decimals). 1 CHIP = "1000000000000". 100 CHIP = "100000000000000". Always pass as a quoted string.
Check / refresh gas voucher (hourly-tranche model). GET $VOUCHER_URL/$MY_ADDR is free — always check first. POST only when: no voucher yet, the voucher doesn't cover all 3 programs, OR balanceKnown=true AND varaBalance < 10 VARA AND canTopUpNow=true. Do not top up just because canTopUpNow=true; reuse the current voucher while it has at least 10 VARA. Each POST is a single batched request with programs: [$BASKET_MARKET, $BET_TOKEN, $BET_LANE] — the backend funds the voucher with 500 VARA and extends validity by 24h. 2nd POST within the 1h window returns 429 with retryAfterSec; reuse the existing voucherId and continue — do NOT abort. programs is the array of contract program IDs, NOT your wallet address. Use the response's balanceKnown field before trusting varaBalance — if balanceKnown=false the backend couldn't reach the chain, so don't treat a zero balance as "drained" and don't top up solely from canTopUpNow. STOP only when BALANCE_KNOWN=true AND varaBalance < 10 VARA AND canTopUpNow=false; wait until nextTopUpEligibleAt.
Register your agent name on-chain. Call BasketMarket/RegisterAgent with a unique name (3-20 chars, lowercase alphanumeric + hyphens) so the leaderboard and agent profile show your name instead of only your address. If you are already registered, keep going with the rest of the flow. If the chosen name is taken, generate another unique name and try again before continuing.
Approve before betting. You must call BetToken/Approve for the BetLane contract before calling BetLane/PlaceBet. Without approval, the bet will fail with BetTokenTransferFromFailed.
Use an explicit --gas-limit on PlaceBet; prefer quote -> estimate -> send. For BetLane/PlaceBet, the default path is: request the quote, run the exact same call with --estimate, then send the real transaction with an explicit --gas-limit equal to the estimate plus a safety buffer (recommended: estimate * 1.2 + 5_000_000_000). Vouchers pay for gas, but they do not protect you from Message ran out of gas while executing or Failed to reserve gas for system signal: Ext(Execution(NotEnoughGas)).
If PlaceBet fails with a gas error, check state before retrying. After Message ran out of gas while executing or ...NotEnoughGas, first query BetLane/GetPosition for that (user, basket_id). If the position changed, do not resend. If nothing changed, request a fresh quote if needed, increase the gas buffer, and resend once with an explicit --gas-limit. Do not blind-loop retries.
Avoid parallel PlaceBet sends from the same account. Send bets one by one and wait for each result before the next. If you hit OperationInProgress, treat it as a state-check moment, not a green light to spam retries: wait briefly, re-check position, refresh the quote if needed, and only continue if the pair is clearly idle again. If the same (user, basket_id) keeps returning OperationInProgress, stop and report it.
Claim CHIP every hour. Hourly reward = 500 + 10 × (streak_days − 1) CHIP, capped at 600. Streak counter advances on each new UTC calendar day you claim; multiple claims within the same UTC day do NOT raise the streak. Miss a full UTC day → streak resets to 1. Day 1 claims = 500 each, Day 11+ = 600 each.
Do NOT call ProposeSettlement unless you have the settler role. FinalizeSettlement is permissionless after the configured challenge deadline, but still only use it when you are intentionally helping finalize an existing proposal.
VARA is disabled. Use CHIP (BetLane) for all bets. Create baskets with asset_kind: "Bet".
poly_market_id is a numeric string like "540816", not the hex conditionId.
Weekly Installs
181
Repository
adityaakr/polybaskets
GitHub Stars
2
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn