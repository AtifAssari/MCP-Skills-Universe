---
rating: ⭐⭐⭐
title: vvvv-spreads
url: https://skills.sh/tebjan/vvvv-skills/vvvv-spreads
---

# vvvv-spreads

skills/tebjan/vvvv-skills/vvvv-spreads
vvvv-spreads
Installation
$ npx skills add https://github.com/tebjan/vvvv-skills --skill vvvv-spreads
SKILL.md
vvvv Spreads
What Are Spreads

Spread<T> is vvvv's immutable collection type, conceptually similar to ImmutableArray<T>. It is the primary way to pass collections between nodes.

Key properties:

Immutable — never modify in place, always create new spreads
Value semantics — two spreads with same elements are considered equal
Cyclic indexing — in visual patches, indexing wraps around (not in C# API)
Never null — use Spread<T>.Empty instead of null
Creating Spreads
SpreadBuilder (Primary Method)
var builder = new SpreadBuilder<float>(expectedCount);
for (int i = 0; i < count; i++)
    builder.Add(ComputeValue(i));
Spread<float> result = builder.ToSpread();

From Existing Data
// From array (extension method)
Spread<int> fromArray = new int[] { 1, 2, 3 }.ToSpread();

// From array (static factory)
Spread<Waypoint> fromResult = Spread.Create(resultArray);

// Empty spread (NEVER use null)
Spread<float> empty = Spread<float>.Empty;

// Single element
var single = new SpreadBuilder<float>(1);
single.Add(42f);
Spread<float> one = single.ToSpread();

Accessing Elements
// Always check Count before indexing
if (spread.Count > 0)
{
    float first = spread[0];
    float last = spread[spread.Count - 1];
}

// Iterate (preferred — no allocation)
foreach (var item in spread)
    Process(item);

// Index access in loop
for (int i = 0; i < spread.Count; i++)
    Process(spread[i]);

Common Patterns in C#
Map (Transform Each Element)
public static Spread<float> Scale(Spread<float> input, float factor = 1f)
{
    var builder = new SpreadBuilder<float>(input.Count);
    foreach (var value in input)
        builder.Add(value * factor);
    return builder.ToSpread();
}

Filter
public static Spread<float> FilterAbove(Spread<float> input, float threshold = 0.5f)
{
    var builder = new SpreadBuilder<float>();
    foreach (var value in input)
    {
        if (value > threshold)
            builder.Add(value);
    }
    return builder.ToSpread();
}

Zip (Process Two Spreads Together)
public static Spread<float> Add(Spread<float> a, Spread<float> b)
{
    int count = Math.Max(a.Count, b.Count);
    var builder = new SpreadBuilder<float>(count);
    for (int i = 0; i < count; i++)
    {
        float va = a.Count > 0 ? a[i % a.Count] : 0f;
        float vb = b.Count > 0 ? b[i % b.Count] : 0f;
        builder.Add(va + vb);
    }
    return builder.ToSpread();
}

Accumulate (Running Total)
public static Spread<float> RunningSum(Spread<float> input)
{
    var builder = new SpreadBuilder<float>(input.Count);
    float sum = 0f;
    foreach (var value in input)
    {
        sum += value;
        builder.Add(sum);
    }
    return builder.ToSpread();
}

ReadOnlySpan as High-Performance Alternative

For hot-path output (e.g., per-frame simulation data), ReadOnlySpan<T> avoids allocation entirely:

[ProcessNode]
public class ParticleSimulator
{
    private ParticleState[] _states;

    public ReadOnlySpan<ParticleState> Update(SimulationConfig config, float deltaTime)
    {
        // Simulate into pre-allocated array — zero allocation
        Simulate(_states, config, deltaTime);
        return _states.AsSpan();
    }
}


Use Spread<T> for infrequent config inputs; use ReadOnlySpan<T> for high-frequency frame data.

Performance Rules
Pre-allocate builder: new SpreadBuilder<T>(expectedCount) when count is known
No LINQ in hot paths: .Where(), .Select(), .ToList() create hidden allocations
Cache spreads: If output doesn't change, return the cached spread reference
Avoid repeated .ToSpread(): Build once, output the result
For large spreads: Consider Span<T> internally, convert to Spread at the API boundary
Spread change detection: Since Spreads are immutable, reference equality (!= or ReferenceEquals) is sufficient — if the reference changed, the content changed
Spreads in ProcessNodes
[ProcessNode]
public class SpreadProcessor
{
    private Spread<float> _lastInput = Spread<float>.Empty;
    private Spread<float> _cachedOutput = Spread<float>.Empty;

    public void Update(
        out Spread<float> output,
        Spread<float> input = default)
    {
        input ??= Spread<float>.Empty;

        if (!ReferenceEquals(input, _lastInput))
        {
            var builder = new SpreadBuilder<float>(input.Count);
            foreach (var v in input)
                builder.Add(v * 2f);
            _cachedOutput = builder.ToSpread();
            _lastInput = input;
        }

        output = _cachedOutput;
    }
}


For more code examples, see examples.md.

Weekly Installs
47
Repository
tebjan/vvvv-skills
GitHub Stars
23
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass