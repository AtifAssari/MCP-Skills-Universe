---
rating: ⭐⭐
title: nbitcoin
url: https://skills.sh/stuartf303/sorcha/nbitcoin
---

# nbitcoin

skills/stuartf303/sorcha/nbitcoin
nbitcoin
Installation
$ npx skills add https://github.com/stuartf303/sorcha --skill nbitcoin
SKILL.md
NBitcoin Skill

NBitcoin provides HD wallet operations in Sorcha through the Sorcha.Wallet.Core project. The codebase wraps NBitcoin types in domain value objects (Mnemonic, DerivationPath) and uses them exclusively for BIP32/39/44 key derivation—NOT for transaction building. Actual signing uses Sorcha.Cryptography (ED25519, P-256, RSA-4096).

Quick Start
Generate a Mnemonic
// src/Common/Sorcha.Wallet.Core/Domain/ValueObjects/Mnemonic.cs
var mnemonic = Mnemonic.Generate(12);  // or 24 for higher security
// NEVER log mnemonic.Phrase - use mnemonic.ToString() which returns "Mnemonic(12 words)"

Derive Keys at BIP44 Path
// src/Common/Sorcha.Wallet.Core/Services/Implementation/KeyManagementService.cs:62-111
var masterKey = await _keyManagement.DeriveMasterKeyAsync(mnemonic, passphrase);
var path = DerivationPath.CreateBip44(coinType: 0, account: 0, change: 0, addressIndex: 0);
var (privateKey, publicKey) = await _keyManagement.DeriveKeyAtPathAsync(masterKey, path, "ED25519");

Validate a Mnemonic
if (Mnemonic.IsValid(userProvidedPhrase))
{
    var mnemonic = new Mnemonic(userProvidedPhrase);
}

Key Concepts
Concept	Usage	Example
Mnemonic	Wraps NBitcoin.Mnemonic	Mnemonic.Generate(12)
DerivationPath	Wraps NBitcoin.KeyPath	DerivationPath.CreateBip44(0, 0, 0, 0)
ExtKey	Extended private key	ExtKey.CreateFromSeed(masterKey)
System Paths	Sorcha-specific aliases	"sorcha:register-attestation" → "m/44'/0'/0'/0/100"
Gap Limit	BIP44: max 20 unused addresses	Enforced in WalletManager.cs:493-508
Common Patterns
Wallet Creation Flow

When: User creates a new wallet.

// 1. Generate mnemonic (NEVER store on server)
var mnemonic = Mnemonic.Generate(12);

// 2. Derive master key with optional passphrase
var masterKey = await _keyManagement.DeriveMasterKeyAsync(mnemonic, passphrase);

// 3. Derive first key at m/44'/0'/0'/0/0
var path = DerivationPath.CreateBip44(0, 0, 0, 0);
var (privateKey, publicKey) = await _keyManagement.DeriveKeyAtPathAsync(masterKey, path, algorithm);

// 4. Encrypt private key before storage
var (encryptedKey, keyId) = await _keyManagement.EncryptPrivateKeyAsync(privateKey, string.Empty);

System Path Resolution

When: Using Sorcha-specific derivation purposes.

// src/Common/Sorcha.Wallet.Core/Constants/SorchaDerivationPaths.cs
var resolvedPath = SorchaDerivationPaths.IsSystemPath(derivationPath)
    ? SorchaDerivationPaths.ResolvePath(derivationPath)  // "sorcha:register-attestation" → "m/44'/0'/0'/0/100"
    : derivationPath;

See Also
patterns - Value objects, key derivation, security patterns
workflows - Wallet creation, recovery, address management
Related Skills
See the cryptography skill for signing operations (ED25519, P-256, RSA-4096)
See the dotnet skill for .NET 10 patterns and DI configuration
See the xunit skill and fluent-assertions skill for testing HD wallet operations
Documentation Resources

Fetch latest NBitcoin documentation with Context7.

How to use Context7:

Use mcp__context7__resolve-library-id to search for "nbitcoin"
Query with mcp__context7__query-docs using the resolved library ID

Library ID: /metacosa/nbitcoin

Recommended Queries:

"NBitcoin BIP32 BIP39 BIP44 key derivation"
"NBitcoin ExtKey master key child derivation"
"NBitcoin Mnemonic passphrase seed"
Weekly Installs
23
Repository
stuartf303/sorcha
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn