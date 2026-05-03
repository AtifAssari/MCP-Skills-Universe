---
rating: ⭐⭐⭐
title: ckvd-testing
url: https://skills.sh/terrylica/crypto-kline-vision-data/ckvd-testing
---

# ckvd-testing

skills/terrylica/crypto-kline-vision-data/ckvd-testing
ckvd-testing
Installation
$ npx skills add https://github.com/terrylica/crypto-kline-vision-data --skill ckvd-testing
SKILL.md
Testing Crypto Kline Vision Data

Run tests for: $ARGUMENTS

Test Workflow Checklist

Copy this checklist and track progress:

Test Progress:
- [ ] Step 1: Run lint check (ruff check)
- [ ] Step 2: Run unit tests (fast, no network)
- [ ] Step 3: Verify import works
- [ ] Step 4: Run integration tests (if changing APIs)
- [ ] Step 5: Check coverage (if adding new code)


Step 1: uv run -p 3.13 ruff check --fix . Step 2: uv run -p 3.13 pytest tests/unit/ -v Step 3: uv run -p 3.13 python -c "from ckvd import CryptoKlineVisionData; print('OK')" Step 4: uv run -p 3.13 pytest tests/integration/ -v (if needed) Step 5: uv run -p 3.13 pytest tests/unit/ --cov=src/ckvd

Test Organization
tests/
├── unit/                    # Fast, no network (~0.5s)
│   └── streaming/           # Async streaming tests (pytest-asyncio)
├── integration/             # External services
├── okx/                     # OKX API integration
└── fcp_pm/                  # FCP protocol tests

Running Tests
Unit Tests (Fast)
# Quick validation
uv run -p 3.13 pytest tests/unit/ -v

# With coverage
uv run -p 3.13 pytest tests/unit/ --cov=src/ckvd --cov-report=term-missing

Integration Tests
# Requires network access
uv run -p 3.13 pytest tests/integration/ -v

# OKX-specific tests
uv run -p 3.13 pytest tests/okx/ -m okx -v

All Tests
uv run -p 3.13 pytest tests/ -v

Test Markers
Marker	Purpose
@pytest.mark.integration	Tests that call external APIs
@pytest.mark.okx	OKX-specific tests
@pytest.mark.serial	Must run sequentially
@pytest.mark.asyncio	Async streaming tests
Writing New Tests
import pytest
from ckvd import CryptoKlineVisionData, DataProvider, MarketType

class TestMyFeature:
    """Tests for MyFeature."""

    def test_basic_functionality(self):
        """Verify basic operation."""
        # Arrange
        manager = CryptoKlineVisionData.create(DataProvider.BINANCE, MarketType.SPOT)

        # Act
        result = manager.some_method()

        # Assert
        assert result is not None
        manager.close()

    @pytest.mark.integration
    def test_with_network(self):
        """Test requiring network access."""
        # Mark with @pytest.mark.integration for external calls
        pass

Mocking HTTP Calls
from unittest.mock import patch, MagicMock

@patch("ckvd.core.sync.crypto_kline_vision_data.FSSpecVisionHandler")
@patch("ckvd.core.sync.crypto_kline_vision_data.UnifiedCacheManager")
def test_with_mocks(self, mock_cache, mock_handler):
    mock_handler.return_value = MagicMock()
    mock_cache.return_value = MagicMock()
    # Test logic...

Async Streaming Tests

Streaming tests use pytest-asyncio. Ensure it's installed (uv run -p 3.13 pip install pytest-asyncio).

import pytest
from ckvd import CryptoKlineVisionData, DataProvider, MarketType, StreamConfig, KlineUpdate
from unittest.mock import AsyncMock, MagicMock, patch


@pytest.fixture
async def stream_manager():
    """Create streaming manager for tests (auto-cleanup)."""
    manager = CryptoKlineVisionData.create(DataProvider.BINANCE, MarketType.FUTURES_USDT)
    yield manager
    manager.close()


@pytest.mark.asyncio
async def test_stream_creation(stream_manager):
    """Verify stream creation."""
    config = StreamConfig(market_type=MarketType.FUTURES_USDT, confirmed_only=True)
    stream = stream_manager.create_stream(config)
    assert stream is not None


@pytest.mark.asyncio
async def test_stream_subscribe_and_receive():
    """Test async streaming with mocked KlineStream."""
    manager = CryptoKlineVisionData.create(DataProvider.BINANCE, MarketType.FUTURES_USDT)

    with patch("ckvd.core.streaming.kline_stream.KlineStream") as MockStream:
        # Mock the stream to emit KlineUpdate objects
        mock_stream_instance = AsyncMock()
        MockStream.return_value = mock_stream_instance

        # Simulate 2 updates: one open, one closed
        mock_updates = [
            MagicMock(spec=KlineUpdate, symbol="BTCUSDT", interval="1h", is_closed=False),
            MagicMock(spec=KlineUpdate, symbol="BTCUSDT", interval="1h", is_closed=True, close=42500.0),
        ]
        mock_stream_instance.__aenter__.return_value = mock_stream_instance
        mock_stream_instance.__aiter__.return_value = iter(mock_updates)

        config = StreamConfig(market_type=MarketType.FUTURES_USDT)
        stream = manager.create_stream(config)

        updates_received = []
        async with stream:
            await stream.subscribe("BTCUSDT", "1h")
            async for update in stream:
                updates_received.append(update)

        assert len(updates_received) == 2
        assert updates_received[1].is_closed is True
        manager.close()

Examples

Practical test examples:

@examples/unit-test-patterns.md - Basic tests, fixtures, mocking
@examples/integration-test-patterns.md - API tests, markers, FCP testing
Helper Scripts

Quick test runner:

# Run all quick checks (lint + unit tests + import)
./docs/skills/ckvd-testing/scripts/run_quick_tests.sh

# Run with test pattern filter
./docs/skills/ckvd-testing/scripts/run_quick_tests.sh test_timestamp

TodoWrite Task Templates
Template A: Run Quick Test
1. Run ruff lint check (uv run -p 3.13 ruff check --fix .)
2. Run unit tests (uv run -p 3.13 pytest tests/unit/ -v)
3. Verify package import works
4. Report pass/fail summary

Template B: Add Unit Test for Feature
1. Identify module and function under test
2. Read existing test patterns in tests/unit/ for the module
3. Write test class following Arrange/Act/Assert pattern
4. Mock external services (FSSpecVisionHandler, UnifiedCacheManager)
5. Add appropriate markers (@pytest.mark.integration if needed)
6. Run new tests and verify they pass
7. Check coverage for new code

Template C: Check Coverage
1. Run unit tests with coverage (uv run -p 3.13 pytest tests/unit/ --cov=src/ckvd --cov-report=term-missing)
2. Identify modules below target coverage
3. Write tests for uncovered paths
4. Re-run coverage to verify improvement

Template D: Write Async Stream Test
1. Import pytest-asyncio and async test utilities (@pytest.mark.asyncio)
2. Create async fixture for stream manager (yield pattern)
3. Set up StreamConfig with desired options
4. Create stream via manager.create_stream()
5. Mock KlineStream if testing without network (AsyncMock)
6. Use async context manager (async with stream)
7. Subscribe to symbol/interval
8. Iterate updates with async for loop
9. Assert on KlineUpdate fields (is_closed, close, volume, etc.)
10. Run with: uv run -p 3.13 pytest tests/unit/streaming/ -v --asyncio-mode=auto

Post-Change Checklist

After modifying this skill:

 Test commands use uv run -p 3.13 and correct paths
 Test organization diagram matches actual directory structure
 Mocking examples match actual import paths
 @-links to references/ and examples/ resolve
 Append changes to evolution-log.md
Detailed References

For deeper information, see:

@references/fixtures.md - Pytest fixtures and auto-cleanup patterns
@references/coverage.md - Coverage configuration and thresholds
@references/mocking-patterns.md - CKVD-specific mocking patterns
@references/markers.md - Pytest markers and test categorization
@references/evolution-log.md - Skill change history
Weekly Installs
13
Repository
terrylica/crypt…ion-data
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn