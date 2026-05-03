---
title: aave-risk-assessor
url: https://skills.sh/0xweaksheep/aave_farmore/aave-risk-assessor
---

# aave-risk-assessor

skills/0xweaksheep/aave_farmore/aave-risk-assessor
aave-risk-assessor
Installation
$ npx skills add https://github.com/0xweaksheep/aave_farmore --skill aave-risk-assessor
SKILL.md
AAVE V3 Risk Assessor

Assess risk metrics for AAVE V3 positions including Health Factor, LTV ratios, and liquidation risk.

Runtime Compatibility: This skill uses AskUserQuestion for interactive prompts. If AskUserQuestion is not available in your runtime, collect the same parameters through natural language conversation instead.

Overview

Calculate and interpret risk metrics for AAVE V3 positions:

Health Factor (HF) - Primary liquidation risk indicator
LTV (Loan-to-Value) - Current and maximum borrowing capacity
Liquidation Threshold - Point at which liquidation becomes possible
Risk Level Classification - Safe, Moderate, High, Critical, Liquidation
Trigger Phrases

This skill should be invoked when users say:

"health factor"
"liquidation risk"
"aave risk"
"will I be liquidated"
"safe to borrow"
"my account health"
"collateral risk"
"liquidation price"
Risk Metrics
Health Factor

The Health Factor is a numeric representation of position safety:

HF = (Σ Collateral_i × LiquidationThreshold_i) / TotalDebt

Health Factor	Risk Level	Description	Recommended Action
> 2.0	Safe	Position is well-collateralized	Normal operation
1.5 - 2.0	Moderate	Position is healthy but monitor	Continue monitoring
1.2 - 1.5	High	Position is at risk	Consider adding collateral or repaying debt
1.0 - 1.2	Critical	Position is near liquidation	Urgent: Add collateral or repay immediately
< 1.0	Liquidation	Position can be liquidated	Position is being or will be liquidated
Risk Level Implementation
function getRiskLevel(healthFactor: number): RiskLevel {
  if (healthFactor > 2.0) return 'safe';
  if (healthFactor >= 1.5) return 'moderate';
  if (healthFactor >= 1.2) return 'high';
  if (healthFactor >= 1.0) return 'critical';
  return 'liquidation';
}

type RiskLevel = 'safe' | 'moderate' | 'high' | 'critical' | 'liquidation';

const riskLevelMessages: Record<RiskLevel, string> = {
  safe: 'Your position is well-collateralized.',
  moderate: 'Your position is healthy, but continue monitoring.',
  high: 'Your position is at risk. Consider adding collateral or repaying debt.',
  critical: 'Warning: Your position is near liquidation! Add collateral or repay immediately.',
  liquidation: 'Your position is eligible for liquidation.'
};

Risk Assessment Interface
interface RiskAssessment {
  // Core metrics
  healthFactor: string;           // Current health factor (e.g., "1.85")
  maxLTV: string;                 // Maximum LTV allowed (e.g., "0.80")
  currentLTV: string;             // Current LTV ratio (e.g., "0.45")
  liquidationThreshold: string;   // Liquidation threshold (e.g., "0.825")
  liquidationPenalty: string;     // Liquidation penalty (e.g., "0.05")

  // eMode status
  eModeStatus: boolean;           // Whether eMode is enabled
  eModeCategory?: number;         // eMode category ID if enabled

  // Risk classification
  riskLevel: 'safe' | 'moderate' | 'high' | 'critical' | 'liquidation';

  // Additional metrics
  totalCollateralUSD: string;     // Total collateral value in USD
  totalDebtUSD: string;           // Total debt value in USD
  availableBorrowsUSD: string;    // Available borrowing power in USD
}

Workflow
Step 1: Get Wallet Address

If not provided in context, ask the user for their wallet address.

Input validation:

Address must match ^0x[a-fA-F0-9]{40}$
Must be a valid checksummed Ethereum address
Step 2: Determine Chain

If not specified, ask which chain to check: Ethereum or Arbitrum.

Step 3: Query On-Chain Data

Use the Pool contract to get user account data:

import { createPublicClient, http, parseAbi } from 'viem';
import { mainnet, arbitrum } from 'viem/chains';

const POOL_ADDRESSES = {
  1: '0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2',    // Ethereum
  42161: '0x794a61358D6845594F94dc1DB02A252b5b4814aD'  // Arbitrum
};

const poolAbi = parseAbi([
  'function getUserAccountData(address user) view returns (uint256 totalCollateralBase, uint256 totalDebtBase, uint256 availableBorrowsBase, uint256 currentLiquidationThreshold, uint256 ltv, uint256 healthFactor)'
]);

Step 4: Present Risk Assessment

Format the output with clear risk indicators:

## AAVE Position Risk Assessment

### Risk Summary

| Metric | Value | Status |
|--------|-------|--------|
| Health Factor | {healthFactor} | {riskEmoji} {riskLevel} |
| Total Collateral | ${totalCollateralUSD} | - |
| Total Debt | ${totalDebtUSD} | - |
| Available to Borrow | ${availableBorrowsUSD} | - |


Risk Emojis:

Safe: ✅
Moderate: ℹ️
High: ⚠️
Critical: 🚨
Liquidation: ❌
Asset-Specific Risk Parameters
Ethereum Mainnet (Chain ID: 1)
Asset	LTV	Liquidation Threshold	Liquidation Penalty
USDC	77%	80%	5%
USDT	75%	80%	5%
DAI	77%	80%	5%
WETH	80%	82.5%	5%
WBTC	73%	78%	7.5%
Arbitrum (Chain ID: 42161)
Asset	LTV	Liquidation Threshold	Liquidation Penalty
USDC	80%	85%	5%
USDT	75%	80%	5%
DAI	75%	80%	5%
WETH	80%	82.5%	5%
WBTC	73%	78%	7.5%
References
references/health-factor.md - Detailed Health Factor calculation
references/risk-thresholds.md - Complete risk parameters by asset
Weekly Installs
9
Repository
0xweaksheep/aave_farmore
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn