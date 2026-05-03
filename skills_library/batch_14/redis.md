---
title: redis
url: https://skills.sh/stuartf303/sorcha/redis
---

# redis

skills/stuartf303/sorcha/redis
redis
Installation
$ npx skills add https://github.com/stuartf303/sorcha --skill redis
SKILL.md
Redis Skill

Sorcha uses Redis via StackExchange.Redis for caching, token revocation tracking, rate limiting, and distributed coordination. All services share a single Redis instance managed by .NET Aspire with circuit breaker resilience.

Quick Start
Aspire Configuration
// src/Apps/Sorcha.AppHost/AppHost.cs
var redis = builder.AddRedis("redis")
    .WithRedisCommander();

// Reference from any service
var blueprintService = builder.AddProject<Projects.Sorcha_Blueprint_Service>()
    .WithReference(redis);

Cache Store Usage
// Inject ICacheStore from Sorcha.Storage.Redis
public class MyService(ICacheStore cache)
{
    public async Task<User?> GetUserAsync(string id)
    {
        return await cache.GetAsync<User>($"user:{id}");
    }
    
    public async Task SetUserAsync(User user)
    {
        await cache.SetAsync($"user:{user.Id}", user, TimeSpan.FromMinutes(15));
    }
}

Direct IConnectionMultiplexer
// For operations beyond ICacheStore (Sets, rate limiting, etc.)
public class TokenService(IConnectionMultiplexer redis)
{
    private readonly IDatabase _db = redis.GetDatabase();
    
    public async Task TrackTokenAsync(string userId, string jti)
    {
        await _db.SetAddAsync($"auth:user_tokens:{userId}", jti);
    }
}

Key Concepts
Concept	Usage	Example
Key prefix	Namespace isolation	sorcha:, auth:
TTL	Automatic expiration	TimeSpan.FromMinutes(15)
Circuit breaker	Graceful degradation	Breaks after 5 failures
Sets	Token tracking	SetAddAsync, SetMembersAsync
Counters	Rate limiting	StringIncrementAsync
Common Patterns
Rate Limiting

When: Protecting auth endpoints from brute force.

public async Task<bool> IsRateLimitedAsync(string identifier)
{
    var key = $"auth:failed:{identifier}";
    var count = await _db.StringIncrementAsync(key);
    
    if (count == 1)
        await _db.KeyExpireAsync(key, TimeSpan.FromSeconds(60));
    
    return count >= MaxFailedAttempts;
}

Token Revocation

When: Invalidating JWTs before expiration.

public async Task RevokeTokenAsync(string jti, DateTimeOffset expiresAt)
{
    var ttl = expiresAt - DateTimeOffset.UtcNow;
    if (ttl > TimeSpan.Zero)
        await _db.StringSetAsync($"auth:revoked:{jti}", "revoked", ttl);
}

See Also
patterns - Caching, resilience, key naming
workflows - Setup, testing, debugging
Related Skills
aspire - Redis resource configuration and service discovery
jwt - Token revocation integration
signalr - Redis backplane for scale-out
docker - Redis container configuration
Documentation Resources

Fetch latest Redis and StackExchange.Redis documentation with Context7.

How to use Context7:

Use mcp__context7__resolve-library-id to search for "StackExchange.Redis" or "redis"
Prefer website documentation (/websites/redis_io) for concepts
Use /stackexchange/stackexchange.redis for .NET-specific patterns

Library IDs:

/stackexchange/stackexchange.redis - .NET client (344 snippets)
/websites/redis_io - Redis concepts (29k+ snippets)

Recommended Queries:

"Connection pooling multiplexer patterns best practices"
"Caching patterns TTL expiration strategies"
"Pub/Sub patterns distributed systems"
Weekly Installs
26
Repository
stuartf303/sorcha
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn