---
rating: ⭐⭐
title: taproot-multisig
url: https://skills.sh/aibtcdev/skills/taproot-multisig
---

# taproot-multisig

skills/aibtcdev/skills/taproot-multisig
taproot-multisig
Installation
$ npx skills add https://github.com/aibtcdev/skills --skill taproot-multisig
SKILL.md
Taproot Multisig Skill

Agent-to-agent Bitcoin Taproot multisig. Proven on mainnet — Arc completed a 2-of-2 (block 937,849) and 3-of-3 (block 938,206) using BIP-340 Schnorr, BIP-342 OP_CHECKSIGADD, and QuorumClaw coordination.

Usage
bun run taproot-multisig/taproot-multisig.ts <subcommand> [options]

Subcommands
get-pubkey

Get your x-only Taproot internal public key for registering with a multisig coordinator. Requires unlocked wallet.

bun run taproot-multisig/taproot-multisig.ts get-pubkey


Output:

{
  "success": true,
  "internalPubKey": "abc123...",
  "taprootAddress": "bc1p...",
  "network": "mainnet",
  "keyFormat": "x-only (32 bytes)",
  "derivationPath": "m/86'/0'/0'/0/0",
  "usage": "Register internalPubKey when joining a multisig.",
  "warning": "Always register internalPubKey, NOT the tweaked key."
}

verify-cosig

Verify a BIP-340 Schnorr signature from a co-signer. No wallet unlock required.

bun run taproot-multisig/taproot-multisig.ts verify-cosig \
  --digest <64-char-hex> \
  --signature <128-char-hex> \
  --public-key <64-char-hex>


Options:

--digest (required) — 32-byte sighash from coordination API
--signature (required) — 64-byte BIP-340 Schnorr signature from co-signer
--public-key (required) — 32-byte x-only public key of the co-signer

Output:

{
  "success": true,
  "isValid": true,
  "digest": "...",
  "signature": "...",
  "publicKey": "...",
  "message": "Signature is valid — this co-signer's key signed this digest."
}

guide

Print the complete step-by-step Taproot multisig workflow as JSON.

bun run taproot-multisig/taproot-multisig.ts guide


Returns the full workflow: key registration, sighash signing, co-signer verification, witness stack format, and the BIP-86 internal-vs-tweaked key gotcha.

Key Signing Command

Signing a sighash uses the signing skill, not this skill:

bun run signing/signing.ts schnorr-sign-digest \
  --digest <sighash_hex> \
  --confirm-blind-sign


This signs with your BIP-86 internal Taproot key (m/86'/0'/0'/0/0). Always register internalPubKey from get-pubkey so the keys match.

Critical: Internal Key vs Tweaked Key

Register internalPubKey. Sign with schnorr-sign-digest. They match.

The tweaked pubkey (embedded in your bc1p... address) is different from the internal pubkey. If you register the tweaked key but sign with the internal key, your signature is valid but against the wrong key — the coordination API rejects it.

Proven Transactions
Type	TXID	Block	Signers
2-of-2	d05806c87ceae62e8f47daafb9fe4842c837fa3f333864cd5a5ec9d2a38cf96b	937,849	Arc + Aetos
3-of-3	47dbaf5185b582902b43241e757c6bc6a1c60b4418453d93b2ffbb0315f87e92	938,206	Arc + Aetos + Bitclaw
Weekly Installs
104
Repository
aibtcdev/skills
GitHub Stars
6
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn