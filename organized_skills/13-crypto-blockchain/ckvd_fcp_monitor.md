---
rating: ⭐⭐⭐
title: ckvd-fcp-monitor
url: https://skills.sh/terrylica/crypto-kline-vision-data/ckvd-fcp-monitor
---

# ckvd-fcp-monitor

skills/terrylica/crypto-kline-vision-data/ckvd-fcp-monitor
ckvd-fcp-monitor
Installation
$ npx skills add https://github.com/terrylica/crypto-kline-vision-data --skill ckvd-fcp-monitor
SKILL.md
FCP Monitor

Monitor and diagnose Failover Control Protocol behavior for: $ARGUMENTS

Quick Diagnostics
# Check FCP behavior for a symbol
uv run -p 3.13 python docs/skills/ckvd-usage/scripts/diagnose_fcp.py BTCUSDT futures_usdt 1h

# Check cache health
uv run -p 3.13 python docs/skills/ckvd-fcp-monitor/scripts/cache_health.py

FCP Decision Flow
Request
    │
    ▼
┌─────────────────┐
│ 1. Cache Check  │ ──── Hit (99%) ───▶ Return (~1ms)
└─────────────────┘
    │ Miss (1%)
    ▼
┌─────────────────┐
│ 2. Vision API   │ ──── OK (95%) ────▶ Cache + Return (~2s)
│    (S3 bulk)    │
└─────────────────┘
    │ Fail (5%)
    ▼
┌─────────────────┐
│ 3. REST API     │ ──── OK (99%) ────▶ Return (~200ms)
│    (real-time)  │
└─────────────────┘
    │ Fail (1%)
    ▼
Raise DataSourceError

Common Issues
Cache Not Being Used

Symptoms: Always hitting REST, slow performance

Diagnostics:

# Check cache directory exists and has data (macOS path via platformdirs)
ls -la ~/Library/Caches/crypto-kline-vision-data/data/binance/futures_usdt/daily/klines/BTCUSDT/1h/

# Or use the cache_health.py script for a full report
uv run -p 3.13 python docs/skills/ckvd-fcp-monitor/scripts/cache_health.py --verbose


Solutions:

Verify cache directory permissions (should be writable)
Check if requested interval matches cached interval
Ensure date range overlaps with cached data
Vision API 403 Errors

Symptoms: "403 Forbidden" in logs, fallback to REST

Cause: Binance Vision API has regional restrictions

Solution: FCP handles this automatically. No action needed.

Rate Limit Errors

Symptoms: 429 responses, RateLimitError

Solutions:

# Use smaller date ranges
for chunk in date_chunks(start, end, chunk_days=7):
    df = manager.get_data(symbol="BTCUSDT", start_time=chunk[0], end_time=chunk[1])
    time.sleep(0.5)  # Rate-limit friendly

# Or use lower frequency intervals
df = manager.get_data(symbol="BTCUSDT", interval=Interval.HOUR_1)  # vs MINUTE_1

Performance Optimization
Cache Warm-Up

Pre-populate cache for frequently accessed symbols:

from datetime import datetime, timedelta, timezone
from ckvd import CryptoKlineVisionData, DataProvider, MarketType, Interval

symbols = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
manager = CryptoKlineVisionData.create(DataProvider.BINANCE, MarketType.FUTURES_USDT)

end = datetime.now(timezone.utc) - timedelta(days=2)  # Avoid recent data
start = end - timedelta(days=365)

for symbol in symbols:
    print(f"Warming cache for {symbol}...")
    df = manager.get_data(symbol=symbol, start_time=start, end_time=end, interval=Interval.HOUR_1)
    print(f"  Cached {len(df)} bars")

manager.close()

Batch Fetching

Fetch multiple symbols efficiently:

from concurrent.futures import ThreadPoolExecutor

def fetch_symbol(symbol: str) -> tuple[str, int]:
    manager = CryptoKlineVisionData.create(DataProvider.BINANCE, MarketType.FUTURES_USDT)
    df = manager.get_data(symbol=symbol, start_time=start, end_time=end, interval=Interval.HOUR_1)
    manager.close()
    return symbol, len(df)

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(fetch_symbol, symbols))

Streaming and FCP

Important: Streaming operates on a PARALLEL data path and does not interact with FCP.

Aspect	FCP (Historical)	Streaming (Real-Time)
API Method	get_data()	stream_data_sync(), create_stream()
Data Flow	Cache → Vision → REST	WebSocket → KlineUpdate stream
Cache Used	Yes (Arrow IPC)	No
Failover	Vision → REST	No fallback
Latency	~1-500ms	Real-time (ms)
Use Case	Historical backtesting, batch analysis	Live trading, real-time monitoring

Monitoring FCP does not affect streaming performance. The two systems are independent. If streaming is slow, check WebSocket connectivity, not FCP sources.

Scripts
Script	Purpose
cache_health.py	Check cache directory health
TodoWrite Task Templates

Note: All templates below are for FCP-based data fetching. For streaming issues, check WebSocket connectivity and async event loop, not FCP sources.

Template A: Diagnose Slow Fetches
1. Enable debug logging (CKVD_LOG_LEVEL=DEBUG)
2. Run fetch and check which FCP sources are hit
3. Verify cache is populated (run cache_health.py)
4. Check if Vision API is being skipped (data too recent)
5. Check REST rate limit headers in debug output
6. Document data source breakdown and latency

Template B: Check Cache Health
1. Run cache_health.py with --verbose flag
2. Verify cache directory exists and is writable
3. Check for expected symbols and intervals
4. Verify Arrow file sizes are reasonable (not zero-byte)
5. Report cache coverage vs requested date ranges

Template C: Debug Vision 403
1. Confirm data is older than 48h (Vision API delay)
2. Check symbol exists on Binance Vision (S3)
3. Enable debug logging and test Vision source directly
4. Verify FCP falls back to REST correctly
5. Document whether 403 is expected or anomalous

Post-Change Checklist

After modifying this skill:

 Script commands reference existing scripts
 Cache paths match platformdirs output
 FCP Decision Flow diagram matches actual implementation
 Append changes to evolution-log.md
Related
@src/CLAUDE.md - FCP implementation, cache patterns, exception hierarchy
@docs/skills/ckvd-usage/references/debugging.md - General debugging
@./references/evolution-log.md - Skill improvement history
Weekly Installs
12
Repository
terrylica/crypt…ion-data
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass