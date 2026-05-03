---
title: integrations
url: https://skills.sh/alsk1992/cloddsbot/integrations
---

# integrations

skills/alsk1992/cloddsbot/integrations
integrations
Installation
$ npx skills add https://github.com/alsk1992/cloddsbot --skill integrations
SKILL.md
Integrations - Complete API Reference

Manage external data sources, add custom connectors, and plug in new data streams for trading bots.

Chat Commands
List Data Sources
/integrations                               List all data sources
/integrations status                        Show source health
/integrations sources                       Available source types

Manage Sources
/integrations enable fedwatch              Enable CME FedWatch
/integrations disable 538                   Disable FiveThirtyEight
/integrations add webhook "my-signals"      Add custom webhook source
/integrations add rest "my-api" <url>       Add REST API source
/integrations remove <source-id>            Remove data source

Configure Sources
/integrations config fedwatch              View source config
/integrations set fedwatch interval 60     Set refresh interval
/integrations set fedwatch key <api-key>   Set API key
/integrations test <source-id>             Test source connection

View Data
/integrations data fedwatch                Latest data from source
/integrations history <source> --hours 24  Historical data
/integrations subscribe <source>           Real-time updates

TypeScript API Reference
Create Integrations Manager
import { createIntegrationsManager } from 'clodds/integrations';

const integrations = createIntegrationsManager({
  // Storage
  storage: 'sqlite',
  dbPath: './integrations.db',

  // Default refresh interval
  defaultIntervalMs: 60000,

  // Retry settings
  maxRetries: 3,
  retryDelayMs: 5000,
});

Built-in Data Sources
// Enable built-in sources
await integrations.enable('fedwatch');     // CME FedWatch
await integrations.enable('538');          // FiveThirtyEight
await integrations.enable('silver');       // Silver Bulletin
await integrations.enable('rcp');          // RealClearPolitics
await integrations.enable('odds-api');     // The Odds API
await integrations.enable('polymarket');   // Polymarket prices
await integrations.enable('kalshi');       // Kalshi prices
await integrations.enable('binance');      // Binance spot prices
await integrations.enable('crypto');       // Multi-exchange crypto

Add Custom Webhook Source
// Add webhook to receive custom signals
const source = await integrations.addWebhook({
  name: 'my-signals',
  description: 'Custom trading signals',

  // Webhook config
  path: '/webhooks/my-signals',
  secret: process.env.WEBHOOK_SECRET,

  // Data schema (optional validation)
  schema: {
    type: 'object',
    properties: {
      signal: { type: 'string', enum: ['BUY', 'SELL', 'HOLD'] },
      symbol: { type: 'string' },
      confidence: { type: 'number', min: 0, max: 1 },
    },
    required: ['signal', 'symbol'],
  },

  // Transform incoming data
  transform: (payload) => ({
    signal: payload.signal,
    symbol: payload.symbol,
    confidence: payload.confidence || 0.5,
    timestamp: Date.now(),
  }),
});

console.log(`Webhook URL: ${source.url}`);
// POST to: https://your-domain.com/webhooks/my-signals

Add Custom REST Source
// Add REST API data source
const source = await integrations.addRest({
  name: 'my-api',
  description: 'Custom price API',

  // API config
  url: 'https://api.example.com/prices',
  method: 'GET',
  headers: {
    'Authorization': `Bearer ${process.env.MY_API_KEY}`,
  },

  // Polling interval
  intervalMs: 30000,

  // Transform response
  transform: (response) => ({
    price: response.data.price,
    volume: response.data.volume,
    timestamp: Date.now(),
  }),
});

Add WebSocket Source
// Add WebSocket data source
const source = await integrations.addWebSocket({
  name: 'live-prices',
  description: 'Real-time price feed',

  // WebSocket config
  url: 'wss://stream.example.com/prices',

  // Message handlers
  onMessage: (data) => ({
    type: 'price',
    symbol: data.s,
    price: parseFloat(data.p),
    timestamp: data.t,
  }),

  // Subscription message
  subscribe: {
    method: 'SUBSCRIBE',
    params: ['btcusdt@trade'],
  },

  // Reconnect settings
  reconnect: true,
  reconnectIntervalMs: 5000,
});

Subscribe to Data
// Subscribe to real-time updates
integrations.subscribe('my-signals', (data) => {
  console.log(`Signal: ${data.signal} ${data.symbol}`);
  console.log(`Confidence: ${data.confidence}`);

  if (data.signal === 'BUY' && data.confidence > 0.8) {
    // Execute trade logic
  }
});

// Subscribe to multiple sources
integrations.subscribeAll(['fedwatch', 'crypto', 'my-signals'], (source, data) => {
  console.log(`[${source}] ${JSON.stringify(data)}`);
});

Get Latest Data
// Get current data from source
const fedData = await integrations.getData('fedwatch');

console.log('Fed Rate Probabilities:');
for (const meeting of fedData.meetings) {
  console.log(`${meeting.date}: ${meeting.probabilities}`);
}

// Get with freshness check
const data = await integrations.getData('crypto', {
  maxAgeMs: 60000,  // Refetch if older than 60s
});

Check Status
// Get source status
const status = await integrations.getStatus('my-api');

console.log(`Status: ${status.status}`);  // 'healthy' | 'degraded' | 'error'
console.log(`Last fetch: ${status.lastFetch}`);
console.log(`Last error: ${status.lastError}`);
console.log(`Fetch count: ${status.fetchCount}`);
console.log(`Error count: ${status.errorCount}`);

// Get all statuses
const all = await integrations.getAllStatuses();

Built-in Data Sources
Source	Type	Data	Refresh
fedwatch	REST	Fed rate probabilities	5 min
538	REST	Election forecasts	1 hour
silver	REST	Silver Bulletin forecasts	1 hour
rcp	REST	Polling averages	15 min
odds-api	REST	Sports betting odds	1 min
polymarket	WebSocket	Market prices	Real-time
kalshi	WebSocket	Market prices	Real-time
binance	WebSocket	Crypto prices	Real-time
Custom Source Types
Type	Best For	Latency
webhook	External signals pushed to you	Instant
rest	APIs you poll periodically	Seconds
websocket	Real-time streaming data	Milliseconds
Using Data in Bots
import { createTradingBot } from 'clodds/trading';
import { createIntegrationsManager } from 'clodds/integrations';

const integrations = createIntegrationsManager();
const bot = createTradingBot();

// Use custom signals in bot strategy
integrations.subscribe('my-signals', async (signal) => {
  if (signal.signal === 'BUY' && signal.confidence > 0.9) {
    await bot.execute({
      platform: 'polymarket',
      market: signal.symbol,
      side: 'YES',
      size: 100 * signal.confidence,
    });
  }
});

// Use Fed data for macro bets
integrations.subscribe('fedwatch', async (data) => {
  const cutProb = data.meetings[0].probabilities['25bp_cut'];
  if (cutProb > 0.8) {
    // High probability of rate cut
    await bot.execute({
      platform: 'kalshi',
      market: 'fed-rate-cut',
      side: 'YES',
      size: 500,
    });
  }
});

Environment Variables
# Built-in sources
CME_FEDWATCH_API_KEY=your-key
FIVETHIRTYEIGHT_API_KEY=your-key
ODDS_API_KEY=your-key

# Custom sources
MY_SIGNALS_WEBHOOK_SECRET=your-secret
MY_API_KEY=your-key

Best Practices
Validate incoming data — Use schemas for webhooks
Set appropriate intervals — Don't poll too frequently
Handle errors gracefully — Sources will fail sometimes
Monitor freshness — Alert on stale data
Transform consistently — Normalize data formats
Use WebSocket for latency — When milliseconds matter
Weekly Installs
10
Repository
alsk1992/cloddsbot
GitHub Stars
194
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn