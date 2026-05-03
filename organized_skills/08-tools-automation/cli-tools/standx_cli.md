---
rating: ⭐⭐⭐
title: standx-cli
url: https://skills.sh/wjllance/standx-cli/standx-cli
---

# standx-cli

skills/wjllance/standx-cli/standx-cli
standx-cli
Installation
$ npx skills add https://github.com/wjllance/standx-cli --skill standx-cli
SKILL.md
StandX CLI Skill

StandX CLI is a crypto trading command-line tool for the StandX exchange.

Installation
Option 1: ClawHub (Recommended - Auto-install)
clawhub install standx-cli

Option 2: Homebrew

Security Note: This uses a third-party tap. You can inspect the formula before installing:

# View the formula source
curl -sL https://raw.githubusercontent.com/wjllance/homebrew-standx-cli/main/standx-cli.rb

# Then install
brew tap wjllance/standx-cli
brew install standx-cli

brew tap wjllance/standx-cli
brew install standx-cli

Quick Start

Check installation:

standx --version


View BTC price:

standx market ticker BTC-USD
# Or use short alias
standx m t BTC-USD

Command Short Aliases

StandX CLI supports short aliases for faster typing:

Full Command	Short Alias
standx market ticker	standx m t
standx market depth	standx m d
standx market kline	standx m k
standx account balances	standx a b
standx account positions	standx a p
standx account orders	standx a o
standx portfolio snapshot	standx p s
standx dashboard --watch	standx d -w
Authentication

Most commands require authentication. StandX CLI supports multiple secure authentication methods.

Environment Variables (Recommended)

The most secure way to authenticate. Credentials are not stored in shell history or command logs.

# Add to ~/.bashrc or ~/.zshrc
export STANDX_JWT="your_jwt_token"
export STANDX_PRIVATE_KEY="your_ed25519_private_key"

# Reload shell configuration
source ~/.bashrc


Security Best Practices:

Never hardcode credentials in commands (appears in shell history)
Never commit credentials to version control
Set file permissions to 600 for any files containing credentials
Rotate tokens regularly (they expire after 7 days)
Get Credentials

Visit https://standx.com/user/session to generate:

JWT Token (required) - Valid for 7 days, used for reading account data
Ed25519 Private Key (optional but recommended) - Required for trading operations
Verify Authentication
standx auth status

Alternative Authentication Methods
Interactive Login

For first-time setup or testing:

standx auth login --interactive

File-based Login

For automation scripts where environment variables are not available:

# Store credentials in files with restricted permissions
echo "your_jwt_token" > ~/.standx_token
echo "your_private_key" > ~/.standx_key
chmod 600 ~/.standx_token ~/.standx_key

# Login using files
standx auth login --token-file ~/.standx_token --key-file ~/.standx_key


⚠️ Avoid this in production:

# DANGER: Credentials will be visible in shell history
standx auth login --token "your_token" --private-key "your_key"

Logout
standx auth logout

Market Data (No auth required)
List trading pairs
standx market symbols

Get ticker
standx market ticker BTC-USD
standx market ticker ETH-USD

Order book depth
standx market depth BTC-USD --limit 10

K-line (candlestick) data
# Last 24 hours, 1-hour candles
standx market kline BTC-USD -r 60 --from 1d

# Last 7 days, daily candles
standx market kline BTC-USD -r 1D --from 7d

# Specific date range
standx market kline BTC-USD -r 60 --from 2024-01-01 --to 2024-01-07

Funding rate
standx market funding BTC-USD --days 7

Account & Trading (Auth required)
Account info
standx account balances
standx account positions
standx account orders
standx account history --limit 20

Create order
# Limit buy
standx order create BTC-USD buy limit --qty 0.01 --price 60000

# Market sell
standx order create BTC-USD sell market --qty 0.01

Cancel order
standx order cancel BTC-USD --order-id 123456
standx order cancel-all BTC-USD

Trade history
standx trade history BTC-USD --from 7d

Dashboard & Portfolio (Auth required)
Real-time Dashboard

Interactive trading dashboard with auto-refresh:

# Launch dashboard with auto-refresh (watch mode)
standx dashboard --watch

# Dashboard for specific symbols
standx dashboard --symbols BTC-USD,ETH-USD

# Dashboard with custom refresh interval (seconds)
standx dashboard --watch --interval 5


Dashboard Features:

Real-time account balance display
Active positions with PnL
Open orders summary
Order book depth visualization
Recent trades panel (BUY/SELL)
Auto-refresh with graceful exit (Ctrl+C)
Portfolio Snapshot

View portfolio summary and performance:

# Portfolio snapshot
standx portfolio snapshot

# Short alias
standx p s

Leverage & Margin (Auth required)
# Query leverage
standx leverage get BTC-USD

# Set leverage
standx leverage set BTC-USD 10

# Query margin mode
standx margin mode BTC-USD

# Set margin mode
standx margin mode BTC-USD --set isolated

Real-time Streaming
Public streams (No auth)
# Price stream
standx stream price BTC-USD

# Order book stream
standx stream depth BTC-USD --levels 5

# Trade stream
standx stream trade BTC-USD

User streams (Auth required)
standx stream order     # Order updates
standx stream position  # Position updates
standx stream balance   # Balance updates
standx stream fills     # Fill updates

Output Formats
# JSON output
standx -o json market ticker BTC-USD

# CSV export
standx -o csv market symbols > symbols.csv

# Quiet mode (just values)
standx -o quiet config get base_url

Special Modes
OpenClaw mode (AI-optimized JSON)
standx --openclaw market ticker BTC-USD

Dry run (preview without executing)
standx --dry-run order create BTC-USD buy limit --qty 0.01 --price 60000

References
API Documentation
Authentication Details
Command Examples
Troubleshooting
Links
GitHub: https://github.com/wjllance/standx-cli
Docs: https://github.com/wjllance/standx-cli/tree/main/docs
Issues: https://github.com/wjllance/standx-cli/issues
Weekly Installs
12
Repository
wjllance/standx-cli
GitHub Stars
17
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn