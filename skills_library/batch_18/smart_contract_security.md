---
title: smart-contract-security
url: https://skills.sh/pluginagentmarketplace/custom-plugin-blockchain/smart-contract-security
---

# smart-contract-security

skills/pluginagentmarketplace/custom-plugin-blockchain/smart-contract-security
smart-contract-security
Installation
$ npx skills add https://github.com/pluginagentmarketplace/custom-plugin-blockchain --skill smart-contract-security
SKILL.md
Smart Contract Security Skill

Master smart contract security with vulnerability detection, auditing methodology, and incident response procedures.

Quick Start
# Invoke this skill for security analysis
Skill("smart-contract-security", topic="vulnerabilities", severity="high")

Topics Covered
1. Common Vulnerabilities

Recognize and prevent:

Reentrancy: CEI pattern violation
Access Control: Missing modifiers
Oracle Manipulation: Flash loan attacks
Integer Issues: Precision loss
2. Auditing Methodology

Systematic review process:

Manual Review: Line-by-line analysis
Static Analysis: Automated tools
Fuzzing: Property-based testing
Formal Verification: Mathematical proofs
3. Security Tools

Essential tooling:

Slither: Fast static analysis
Mythril: Symbolic execution
Foundry: Fuzzing, invariants
Certora: Formal verification
4. Incident Response

Handle security events:

Triage: Assess severity
Mitigation: Emergency actions
Post-mortem: Root cause analysis
Disclosure: Responsible reporting
Vulnerability Quick Reference
Critical: Reentrancy
// VULNERABLE
function withdraw(uint256 amount) external {
    (bool ok,) = msg.sender.call{value: amount}("");
    require(ok);
    balances[msg.sender] -= amount;  // After call!
}

// FIXED: CEI Pattern
function withdraw(uint256 amount) external {
    balances[msg.sender] -= amount;  // Before call
    (bool ok,) = msg.sender.call{value: amount}("");
    require(ok);
}

High: Missing Access Control
// VULNERABLE
function setAdmin(address newAdmin) external {
    admin = newAdmin;  // Anyone can call!
}

// FIXED
function setAdmin(address newAdmin) external onlyOwner {
    admin = newAdmin;
}

High: Unchecked Return Value
// VULNERABLE
IERC20(token).transfer(to, amount);  // Ignored!

// FIXED: Use SafeERC20
using SafeERC20 for IERC20;
IERC20(token).safeTransfer(to, amount);

Medium: Precision Loss
// VULNERABLE: Division before multiplication
uint256 fee = (amount / 1000) * rate;

// FIXED: Multiply first
uint256 fee = (amount * rate) / 1000;

Audit Checklist
Pre-Audit
 Code compiles without warnings
 Tests pass with good coverage
 Documentation reviewed
Core Security
 CEI pattern followed
 Reentrancy guards present
 Access control on admin functions
 Input validation complete
DeFi Specific
 Oracle staleness checks
 Slippage protection
 Flash loan resistance
 Sandwich prevention
Security Tools
Static Analysis
# Slither - Fast vulnerability detection
slither . --exclude-dependencies

# Mythril - Symbolic execution
myth analyze src/Contract.sol

# Semgrep - Custom rules
semgrep --config "p/smart-contracts" .

Fuzzing
// Foundry fuzz test
function testFuzz_Withdraw(uint256 amount) public {
    amount = bound(amount, 1, type(uint128).max);

    vm.deal(address(vault), amount);
    vault.deposit{value: amount}();

    uint256 before = address(this).balance;
    vault.withdraw(amount);

    assertEq(address(this).balance, before + amount);
}

Invariant Testing
function invariant_BalancesMatchTotalSupply() public {
    uint256 sum = 0;
    for (uint i = 0; i < actors.length; i++) {
        sum += token.balanceOf(actors[i]);
    }
    assertEq(token.totalSupply(), sum);
}

Severity Classification
Severity	Impact	Examples
Critical	Direct fund loss	Reentrancy, unprotected init
High	Significant damage	Access control, oracle manipulation
Medium	Conditional impact	Precision loss, timing issues
Low	Minor issues	Missing events, naming
Incident Response
1. Detection
# Monitor for suspicious activity
cast logs --address $CONTRACT --from-block latest

2. Mitigation
// Emergency pause
function pause() external onlyOwner {
    _pause();
}

3. Recovery
Assess damage scope
Coordinate disclosure
Deploy fixes with audit
Common Pitfalls
Pitfall	Risk	Prevention
Only testing happy path	Missing edge cases	Fuzz test boundaries
Ignoring integrations	External call risks	Review all dependencies
Trusting block.timestamp	Miner manipulation	Use for long timeframes only
Cross-References
Bonded Agent: 06-smart-contract-security
Related Skills: solidity-development, defi-protocols
Resources
SWC Registry: Common weakness enumeration
Rekt News: Hack post-mortems
Immunefi: Bug bounties
Version History
Version	Date	Changes
2.0.0	2025-01	Production-grade with tools, methodology
1.0.0	2024-12	Initial release
Weekly Installs
195
Repository
pluginagentmark…ockchain
GitHub Stars
1
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass