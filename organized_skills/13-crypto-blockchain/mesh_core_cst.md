---
rating: ⭐⭐⭐
title: mesh-core-cst
url: https://skills.sh/meshjs/skills/mesh-core-cst
---

# mesh-core-cst

skills/meshjs/skills/mesh-core-cst
mesh-core-cst
Installation
$ npx skills add https://github.com/meshjs/skills --skill mesh-core-cst
SKILL.md
Mesh SDK Core CST Skill

AI-assisted low-level Cardano utilities using @meshsdk/core-cst.

Package Info
npm install @meshsdk/core-cst
# or
npm install @meshsdk/core  # includes core-cst + transaction + wallet + provider

What is core-cst?

@meshsdk/core-cst provides low-level utilities for:

Serialization - Convert transactions to/from CBOR
Resolvers - Extract hashes, addresses, keys from various formats
Message Signing - CIP-8 COSE sign and verify
Plutus Tools - Apply parameters to scripts, normalize encodings
Data Conversion - Plutus data ↔ JSON ↔ CBOR
Address Utilities - Parse, serialize, convert address formats
Quick Reference
Resolvers
import {
  resolveDataHash,
  resolvePaymentKeyHash,
  resolveStakeKeyHash,
  resolveRewardAddress,
  resolvePlutusScriptAddress,
  resolvePlutusScriptHash,
  resolveNativeScriptAddress,
  resolveNativeScriptHash,
  resolvePoolId,
  resolvePrivateKey,
  resolveTxHash,
  resolveScriptRef,
  resolveScriptHashDRepId,
  resolveEd25519KeyHash,
} from '@meshsdk/core-cst';

// Get data hash from Plutus data
const hash = resolveDataHash({ constructor: 0, fields: [] });

// Get payment key hash from address
const keyHash = resolvePaymentKeyHash('addr_test1qp...');

// Get stake/reward address from base address
const rewardAddr = resolveRewardAddress('addr_test1qp...');

// Get script address from Plutus script
const scriptAddr = resolvePlutusScriptAddress(
  { code: '59...', version: 'V2' },
  0  // networkId
);

// Get tx hash from tx CBOR
const txHash = resolveTxHash(txCborHex);

Message Signing (CIP-8)
import { signData, checkSignature } from '@meshsdk/core-cst';

// Sign data
const signature = signData('Hello Cardano!', signer);
// { key: 'a401...', signature: '845846...' }

// Verify signature
const isValid = await checkSignature(
  'Hello Cardano!',
  signature,
  'addr_test1qp...'  // optional address verification
);

Plutus Tools
import { applyParamsToScript, normalizePlutusScript } from '@meshsdk/core-cst';

// Apply parameters to parameterized script
const appliedScript = applyParamsToScript(
  rawScriptHex,
  [{ constructor: 0, fields: [{ bytes: 'abc123' }] }],
  'Mesh'  // or 'JSON' or 'CBOR'
);

// Normalize script encoding
const normalized = normalizePlutusScript(scriptHex, 'DoubleCBOR');

Data Conversion
import {
  toPlutusData,
  fromBuilderToPlutusData,
  fromPlutusDataToJson,
  parseDatumCbor,
} from '@meshsdk/core-cst';

// Mesh Data → PlutusData
const plutusData = toPlutusData({ constructor: 0, fields: ['hello', 42] });

// BuilderData → PlutusData (handles Mesh/JSON/CBOR)
const data = fromBuilderToPlutusData({ type: 'Mesh', content: myData });

// PlutusData → JSON
const json = fromPlutusDataToJson(plutusData);

// Parse datum CBOR to JSON
const datum = parseDatumCbor<MyDatumType>(datumCborHex);

Address Utilities
import {
  deserializeBech32Address,
  serialzeAddress,
  scriptHashToBech32,
  addrBech32ToPlutusDataHex,
} from '@meshsdk/core-cst';

// Deserialize address to components
const { pubKeyHash, scriptHash, stakeCredentialHash } =
  deserializeBech32Address('addr_test1qp...');

// Script hash to bech32 address
const addr = scriptHashToBech32(scriptHash, stakeKeyHash, 0);

// Address to Plutus data (for on-chain use)
const addrPlutusHex = addrBech32ToPlutusDataHex('addr_test1qp...');

CardanoSDKSerializer
import { CardanoSDKSerializer } from '@meshsdk/core-cst';

const serializer = new CardanoSDKSerializer(protocolParams);

// Serialize transaction body
const txCbor = serializer.serializeTxBody(meshTxBuilderBody);

// Add signing keys to transaction
const signedTx = serializer.addSigningKeys(txCbor, [privateKeyHex]);

// Serialize data
const dataCbor = serializer.serializeData({ type: 'Mesh', content: myData });

// Serialize address from components
const addr = serializer.serializeAddress({
  pubKeyHash: '...',
  stakeCredentialHash: '...',
}, 0);

Files
CORE-CST.md - Complete API reference
PATTERNS.md - Common usage patterns
TROUBLESHOOTING.md - Error solutions
Module Exports
Module	Purpose
resolvers	Hash/address resolution functions
serializer	CardanoSDKSerializer class
message-signing	CIP-8 COSE utilities
plutus-tools	Script parameterization
utils	Data, address, encoding utilities
types	Re-exports from @cardano-sdk/core
Important Notes
This is a low-level package - Most users should use @meshsdk/transaction instead
Used internally by Mesh - Powers MeshTxBuilder serialization
Requires understanding of Cardano primitives - CBOR, Plutus data, addresses
Re-exports cardano-sdk - Access via Cardano, Serialization, Crypto exports
Weekly Installs
26
Repository
meshjs/skills
GitHub Stars
2
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn