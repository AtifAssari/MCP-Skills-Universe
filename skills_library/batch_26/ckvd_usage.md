---
title: ckvd-usage
url: https://skills.sh/terrylica/crypto-kline-vision-data/ckvd-usage
---

# ckvd-usage

skills/terrylica/crypto-kline-vision-data/ckvd-usage
ckvd-usage
Installation
$ npx skills add https://github.com/terrylica/crypto-kline-vision-data --skill ckvd-usage
SKILL.md
CryptoKlineVisionData Usage

Fetch market data for: $ARGUMENTS

Use automatic failover between data sources.

Quick Start
from ckvd import CryptoKlineVisionData, DataProvider, MarketType, Interval
from datetime import datetime, timedelta, timezone

# Create manager for USDT-margined futures
manager = CryptoKlineVisionData.create(DataProvider.BINANCE, MarketType.FUTURES_USDT)

# Fetch data with automatic failover (cache → Vision → REST)
# IMPORTANT: Always use UTC timezone-aware datetimes
end_time = datetime.now(timezone.utc)
start_time = end_time - timedelta(days=7)

df = manager.get_data(
    symbol="BTCUSDT",
    start_time=start_time,
    end_time=end_time,
    interval=Interval.HOUR_1
)

print(f"Loaded {len(df)} bars")
manager.close()

Key Concepts
Concept	Quick Reference
Market Types	SPOT, FUTURES_USDT, FUTURES_COIN
Intervals	MINUTE_1, MINUTE_5, HOUR_1, HOUR_4, DAY_1
FCP Priority	Cache (~1ms) → Vision (~1-5s) → REST (~100-500ms)
Symbol Format	BTCUSDT (spot/futures), BTCUSD_PERP (coin-margined)
Streaming	Real-time klines (sync/async), KlineUpdate objects
High-Level API

For simpler use cases, use fetch_market_data:

from ckvd import fetch_market_data, DataProvider, MarketType, Interval, ChartType
from datetime import datetime, timedelta, timezone

df, elapsed_time, records_count = fetch_market_data(
    provider=DataProvider.BINANCE,
    market_type=MarketType.FUTURES_USDT,
    chart_type=ChartType.KLINES,
    symbol="BTCUSDT",
    interval=Interval.HOUR_1,
    start_time=datetime.now(timezone.utc) - timedelta(days=30),
    end_time=datetime.now(timezone.utc)
)
print(f"Loaded {records_count} bars in {elapsed_time:.2f}s")

Streaming Real-Time Klines

For real-time market data, use the streaming API (requires pip install crypto-kline-vision-data[streaming]):

Synchronous Streaming
from ckvd import CryptoKlineVisionData, DataProvider, MarketType

manager = CryptoKlineVisionData.create(DataProvider.BINANCE, MarketType.FUTURES_USDT)

# Blocking iterator - receives KlineUpdate objects
for update in manager.stream_data_sync("BTCUSDT", "1h"):
    if update.is_closed:
        print(f"Closed candle: open={update.open}, close={update.close}, volume={update.volume}")
    else:
        print(f"Open candle (time: {update.open_time})")

manager.close()

Asynchronous Streaming
import asyncio
from ckvd import CryptoKlineVisionData, DataProvider, MarketType, StreamConfig

async def main():
    manager = CryptoKlineVisionData.create(DataProvider.BINANCE, MarketType.FUTURES_USDT)

    # Create stream with optional config
    config = StreamConfig(
        market_type=MarketType.FUTURES_USDT,
        confirmed_only=True,  # Only emit when candle closes
        queue_maxsize=1000
    )
    stream = manager.create_stream(config)

    async with stream:
        await stream.subscribe("BTCUSDT", "1h")
        async for update in stream:
            print(f"{update.symbol} {update.interval}: close={update.close}")

asyncio.run(main())


KlineUpdate fields: open_time (UTC datetime), open, high, low, close, volume (all float), symbol, interval, is_closed (bool)

Examples

Practical code examples:

@examples/basic-fetch.md - Single/multiple symbols, market types
@examples/error-handling.md - Exception patterns, validation, retries
Helper Scripts

Utility scripts for common operations:

# Validate symbol format
uv run -p 3.13 python docs/skills/ckvd-usage/scripts/validate_symbol.py BTCUSDT FUTURES_COIN

# Check cache status
uv run -p 3.13 python docs/skills/ckvd-usage/scripts/check_cache.py BTCUSDT futures_usdt 1h

# Diagnose FCP behavior (with debug logging)
uv run -p 3.13 python docs/skills/ckvd-usage/scripts/diagnose_fcp.py BTCUSDT futures_usdt 1h --days 3

TodoWrite Task Templates
Template A: Fetch Data for Symbol
1. Determine market type from symbol format (BTCUSDT vs BTCUSD_PERP)
2. Create CryptoKlineVisionData manager with correct MarketType
3. Define UTC time range with datetime.now(timezone.utc)
4. Call get_data() with symbol, interval, and time range
5. Validate returned DataFrame (not empty, monotonic index)
6. Close manager when done

Template B: Debug Empty Results
1. Validate symbol format for market type (validate_symbol_for_market_type)
2. Verify time range is in the past and UTC-aware
3. Enable debug logging (CKVD_LOG_LEVEL=DEBUG)
4. Test each FCP source individually with enforce_source
5. Check cache directory exists and has data
6. Document root cause and resolution

Template C: Switch Market Type
1. Identify current market type and symbol format
2. Map symbol to new market type format (e.g., BTCUSDT -> BTCUSD_PERP)
3. Create new manager with target MarketType
4. Verify data fetches correctly for new market type
5. Update any dependent code with new symbol format

Template D: Stream Real-Time Data
1. Determine if sync (blocking) or async streaming is needed
   - Sync: Simple use case, single symbol, main thread OK
   - Async: Multiple symbols, integration with other async code
2. Create CryptoKlineVisionData manager
3. For sync: Use manager.stream_data_sync("SYMBOL", "INTERVAL")
4. For async: Create StreamConfig, create_stream(), subscribe to symbols
5. Process KlineUpdate objects in loop
6. Check is_closed flag to detect candle completion
7. Close manager when done (use context manager for async)

Post-Change Checklist

After modifying this skill:

 Quick Start code example still matches actual API
 Helper script commands are correct and scripts exist
 @-links to references/ and examples/ resolve
 Append changes to evolution-log.md
Detailed References

For deeper information, see:

@references/market-types.md - Detailed market type documentation
@references/intervals.md - Complete interval reference
@references/fcp-protocol.md - FCP architecture and debugging
@references/debugging.md - Debugging techniques and troubleshooting
@references/evolution-log.md - Skill change history
Weekly Installs
22
Repository
terrylica/crypt…ion-data
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass