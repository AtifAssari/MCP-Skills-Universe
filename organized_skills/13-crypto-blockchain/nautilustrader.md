---
rating: ⭐⭐⭐
title: nautilustrader
url: https://skills.sh/felixwayne0318/aitrader/nautilustrader
---

# nautilustrader

skills/felixwayne0318/aitrader/nautilustrader
nautilustrader
Installation
$ npx skills add https://github.com/felixwayne0318/aitrader --skill nautilustrader
SKILL.md
NautilusTrader Reference

High-performance algorithmic trading platform used by AlgVex.

Project Configuration
Item	Value
Version	1.224.0
Python	3.12+
Exchange	Binance Futures
Symbol	BTCUSDT-PERP
AlgVex SRP v6.1 Architecture
Component	File	Purpose
NT Strategy Shell	srp/strategy/srp_strategy.py	NautilusTrader Strategy subclass, order lifecycle
Signal Engine	srp/strategy/signal_engine.py	Pure signal logic (VWMA+RSI-MFI channel + DCA)
Indicators	srp/strategy/pine_indicators.py	Pine-parity indicator calculations
Config	srp/configs/srp.yaml	All SRP parameters
Pine SSoT	srp/docs/v6.pine	Pine Script source of truth
Entry Point	main_live.py	--strategy srp launches SRP
Reference Documentation

Detailed documentation is available in the references/ subdirectory:

File	Content
references/index.md	Overview and navigation
references/getting_started.md	Installation and quick start
references/concepts.md	Core concepts (Strategy, Actor, etc.)
references/strategies.md	Strategy implementation guide
references/data.md	Data types and feeds
references/backtesting.md	Backtesting guide
references/api.md	API reference
references/other.md	Additional topics
Quick Reference
Strategy Base Class
from nautilus_trader.trading.strategy import Strategy

class MyStrategy(Strategy):
    def on_start(self):
        """Called when strategy starts"""
        pass

    def on_bar(self, bar: Bar):
        """Called on each bar update"""
        pass

    def on_order_filled(self, event: OrderFilled):
        """Called when order is filled"""
        pass

Order Submission
order = self.order_factory.market(
    instrument_id=self.instrument.id,
    order_side=OrderSide.BUY,
    quantity=Quantity.from_str("0.001"),
)
self.submit_order(order)

Stop-Loss/Take-Profit
# Submit entry order
entry = self.order_factory.market(...)
self.submit_order(entry)

# In on_position_opened callback, submit SL and TP separately
sl_order = self.order_factory.stop_market(..., reduce_only=True)
self.submit_order(sl_order)

# TP uses limit_if_touched (position-linked, auto-cancels on close)
tp_order = self.order_factory.limit_if_touched(...)
self.submit_order(tp_order)


Important: Do NOT use submit_order_list() with bracket orders.

Common Issues
Issue 1: Indicator Access from Background Thread

Problem: Accessing indicators from non-main thread causes Rust panic. Solution: Cache values in Python variables, access cached values from background threads.

Issue 2: Wrong Indicator Module

Problem: Using nautilus_trader.core.nautilus_pyo3 indicators. Solution: Use nautilus_trader.indicators (Cython version).

Issue 3: Circular Imports

Problem: __init__.py auto-imports cause circular dependencies. Solution: Import modules directly, avoid barrel exports.

Reference Files

This skill includes comprehensive documentation in references/:

api.md - API documentation
backtesting.md - Backtesting documentation
concepts.md - Concepts documentation
data.md - Data documentation
getting_started.md - Getting Started documentation
other.md - Other documentation
strategies.md - Strategies documentation

Use view to read specific reference files when detailed information is needed.

Resources
references/

Organized documentation extracted from official sources. These files contain:

Detailed explanations
Code examples with language annotations
Links to original documentation
Table of contents for quick navigation
Notes
This skill was automatically generated from official documentation
Reference files preserve the structure and examples from source docs
Code examples include language detection for better syntax highlighting
Quick reference patterns are extracted from common usage examples in the docs
Weekly Installs
31
Repository
felixwayne0318/aitrader
GitHub Stars
1
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn