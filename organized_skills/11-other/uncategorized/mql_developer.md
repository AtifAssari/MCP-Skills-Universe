---
rating: ⭐⭐
title: mql-developer
url: https://skills.sh/thomaspraun/mql-developer/mql-developer
---

# mql-developer

skills/thomaspraun/mql-developer/mql-developer
mql-developer
Installation
$ npx skills add https://github.com/thomaspraun/mql-developer --skill mql-developer
SKILL.md
MQL Developer

Guide for professional MQL4/MQL5 development on MetaTrader platforms.

Quick Reference Navigation

Load the appropriate reference file based on the task:

Task	Reference File
MQL4 syntax, types, functions, predefined vars	references/mql4-reference.md
MQL5 syntax, OOP, CTrade, Standard Library	references/mql5-reference.md
Project structure, EA architecture, design patterns	references/architecture-patterns.md
Orders, positions, risk management, trailing stops	references/trading-operations.md
Custom indicators, UI panels, scripts, chart objects	references/indicators-and-ui.md
WebRequest, JSON, REST API, Node.js integration	references/external-communication.md
Strategy Tester, optimization, walk-forward, Monte Carlo	references/backtesting.md
Code protection, licensing, anti-decompilation	references/security-licensing.md
Search Patterns for Large References

For targeted lookup in large files, grep for these section headers:

mql4-reference.md: Data Types, Variables, Operators, Arrays, Strings, Program Types, Predefined Variables, Technical Indicator Functions, Order Management, Market Information, Account Functions, Preprocessor, Error Handling, Common Gotchas, File Operations, WebRequest, Utility Functions, Global Terminal Variables

architecture-patterns.md: Project Structure, Simple Single-File, Modular EA, State Machine, Multi-Timeframe, Multi-Symbol, Singleton, Strategy Pattern, Observer, Include File Design, Complete Templates

mql5-reference.md: OOP Features, Trade Functions, CTrade, Native Trade, Event Handlers, Standard Library, Key Enumerations, SQLite, Sockets, Resources, OpenCL

MQL4 vs MQL5 Key Differences
Aspect	MQL4	MQL5
Paradigm	Procedural (C-like)	Full OOP (C++-like)
Trade model	Orders only (OrderSend)	Orders + Deals + Positions (CTrade)
Account model	Hedging only	Netting + Hedging
Indicator buffers	Max 8	Max 512
Draw styles	6 basic	18 (basic + color)
Standard Library	Minimal	Comprehensive
Database	None	SQLite built-in
Sockets	None	TCP + TLS
OpenCL	No	Yes
Core Workflow
Creating an Expert Advisor
Define strategy signal logic (entry/exit conditions)
Choose architecture: simple (single-file) or modular (Signal + Trade + Risk + Filter)
Implement order/position management with proper error handling and retries
Add risk management (position sizing, drawdown control)
Add filters (time, spread, volatility)
Backtest with Strategy Tester (Open Prices first, then Every Tick)
Walk-forward validate and Monte Carlo test
Creating a Custom Indicator
Choose window: indicator_chart_window or indicator_separate_window
Define buffers and plots (indicator_buffers, indicator_plots in MQL5)
Implement OnCalculate() with efficient recalculation using prev_calculated
Set draw styles, colors, labels
Handle multi-timeframe data if needed
Communicating with External APIs
Whitelist URL in Tools > Options > Expert Advisors
Use WebRequest() for REST calls (POST/GET)
Build JSON manually (MQL has no native JSON)
Parse response with string functions
Use EventSetTimer() for polling patterns
Handle network errors with retries
Critical Gotchas
Double comparison: Never use == with doubles. Use NormalizeDouble() or tolerance
4-digit vs 5-digit brokers: 1 pip = 1 point (4-digit) or 10 points (5-digit). Always detect
Reverse loop for closing: Iterate OrdersTotal()-1 down to 0 when closing orders (MQL4)
ECN brokers: Some require two-step: OrderSend() without SL/TP, then OrderModify()
Filling policy (MQL5): Always detect via SYMBOL_FILLING_MODE, never hardcode FOK
WebRequest limitations: Synchronous/blocking, not available in indicators or Strategy Tester
Trade context busy (MQL4): Only one EA can trade at a time per terminal
Array indexing: Series arrays index 0 = newest bar. Use ArraySetAsSeries() to control
Project Structure (Recommended)
MQL5/                          (or MQL4/)
├── Experts/
│   └── MyEA/
│       └── MyEA.mq5           // EA entry point
├── Indicators/
│   └── MyIndicator.mq5
├── Scripts/
│   └── MyScript.mq5
├── Include/
│   ├── Core/
│   │   ├── CTradeManager.mqh  // Order execution + retries
│   │   ├── CRiskManager.mqh   // Position sizing + drawdown
│   │   └── CSignalBase.mqh    // Signal interface
│   ├── Communication/
│   │   ├── CHttpClient.mqh    // WebRequest wrapper
│   │   └── CJsonHelper.mqh    // JSON build/parse
│   ├── UI/
│   │   └── CPanel.mqh         // Trading panel
│   └── Utils/
│       ├── CTimeFilter.mqh    // Session/time filters
│       └── CSymbolHelper.mqh  // Multi-market helpers
└── Libraries/


For simpler projects, a single-file EA with inline functions is acceptable.

Code Style Conventions
Prefix member variables with m_ (e.g., m_magicNumber)
Prefix global variables with g_ (e.g., g_isInitialized)
Use input for user parameters, not extern
Always use #property strict in MQL4
Normalize all prices before sending to server: NormalizeDouble(price, Digits)
Always check return values of OrderSelect(), OrderSend(), trade operations
Comment magic numbers and explain non-obvious trading logic
Official Documentation
MQL4: https://docs.mql4.com/
MQL5: https://www.mql5.com/en/docs
MQL5 Articles: https://www.mql5.com/en/articles
MQL5 Code Base: https://www.mql5.com/en/code
Weekly Installs
123
Repository
thomaspraun/mql…eveloper
GitHub Stars
14
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn