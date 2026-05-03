---
title: effect-client-wrapper
url: https://skills.sh/rhyssullivan/effect-client-wrapper-skill/effect-client-wrapper
---

# effect-client-wrapper

skills/rhyssullivan/effect-client-wrapper-skill/effect-client-wrapper
effect-client-wrapper
Installation
$ npx skills add https://github.com/rhyssullivan/effect-client-wrapper-skill --skill effect-client-wrapper
SKILL.md
Effect Client Wrapper Pattern

Wrap third-party SDK clients with Effect using the "use" pattern for consistent error handling, tracing, and dependency injection.

Pattern Structure
import { Context, Data, Effect, Layer, Config, Redacted } from "effect";

// 1. Define tagged errors
export class MyClientError extends Data.TaggedError("MyClientError")<{
  cause: unknown;
}> {}

export class MyClientInstantiationError extends Data.TaggedError(
  "MyClientInstantiationError"
)<{
  cause: unknown;
}> {}

// 2. Define service interface with `use` method
export type IMyClient = Readonly<{
  client: ThirdPartyClient;
  use: <A>(
    fn: (client: ThirdPartyClient) => Promise<A>
  ) => Effect.Effect<A, MyClientError, never>;
}>;

// 3. Create the service implementation
const make = Effect.gen(function* () {
  const apiKey = yield* Config.redacted("MY_CLIENT_API_KEY");

  const client = yield* Effect.try({
    try: () => new ThirdPartyClient(Redacted.value(apiKey)),
    catch: (cause) => new MyClientInstantiationError({ cause }),
  });

  const use = <A>(fn: (client: ThirdPartyClient) => Promise<A>) =>
    Effect.tryPromise({
      try: () => fn(client),
      catch: (cause) => new MyClientError({ cause }),
    }).pipe(Effect.withSpan(`my_client.${fn.name ?? "use"}`));

  return { client, use };
});

// 4. Export as Context.Tag with Default layer
export class MyClient extends Context.Tag("MyClient")<MyClient, IMyClient>() {
  static Default = Layer.effect(this, make).pipe(
    Layer.annotateSpans({ module: "MyClient" })
  );
}

Usage
const program = Effect.gen(function* () {
  const myClient = yield* MyClient;

  const result = yield* myClient.use((client) =>
    client.someMethod({ param: "value" })
  );

  return result;
});

// Run with layer
program.pipe(Effect.provide(MyClient.Default));

Key Benefits
Centralized error handling - All client errors wrapped in typed MyClientError
Automatic tracing - Every use call creates a span with function name
Config-based secrets - API keys loaded via Config.redacted
Clean DI - Consumers inject via yield* MyClient
Encapsulation - Raw client hidden behind use interface
Variations
Multiple Error Types
export class MyClientNetworkError extends Data.TaggedError("MyClientNetworkError")<{
  cause: unknown;
}> {}

export class MyClientValidationError extends Data.TaggedError("MyClientValidationError")<{
  message: string;
}> {}

const use = <A>(fn: (client: ThirdPartyClient) => Promise<A>) =>
  Effect.tryPromise({
    try: () => fn(client),
    catch: (cause) => {
      if (cause instanceof NetworkError) {
        return new MyClientNetworkError({ cause });
      }
      return new MyClientError({ cause });
    },
  }).pipe(Effect.withSpan(`my_client.${fn.name ?? "use"}`));

Named Operations

Expose specific methods instead of generic use:

export type IEmailClient = Readonly<{
  sendEmail: (params: SendEmailParams) => Effect.Effect<EmailResult, EmailError>;
  getEmail: (id: string) => Effect.Effect<Email, EmailError>;
}>;

const make = Effect.gen(function* () {
  const resend = yield* ResendClient;

  return {
    sendEmail: (params) =>
      resend
        .use((client) => client.emails.send(params))
        .pipe(Effect.withSpan("email_client.send")),

    getEmail: (id) =>
      resend
        .use((client) => client.emails.get(id))
        .pipe(Effect.withSpan("email_client.get")),
  };
});

With Retry Policy
import { Schedule } from "effect";

const retryPolicy = Schedule.exponential(100).pipe(
  Schedule.intersect(Schedule.recurs(3)),
  Schedule.jittered
);

const use = <A>(fn: (client: ThirdPartyClient) => Promise<A>) =>
  Effect.tryPromise({
    try: () => fn(client),
    catch: (cause) => new MyClientError({ cause }),
  }).pipe(
    Effect.retry(retryPolicy),
    Effect.withSpan(`my_client.${fn.name ?? "use"}`)
  );

Real-World Example: Stripe
import Stripe from "stripe";
import { Context, Data, Effect, Layer, Config, Redacted } from "effect";

export class StripeError extends Data.TaggedError("StripeError")<{
  cause: unknown;
}> {}

export type IStripeClient = Readonly<{
  use: <A>(fn: (stripe: Stripe) => Promise<A>) => Effect.Effect<A, StripeError>;
}>;

const make = Effect.gen(function* () {
  const secretKey = yield* Config.redacted("STRIPE_SECRET_KEY");

  const client = new Stripe(Redacted.value(secretKey));

  const use = <A>(fn: (stripe: Stripe) => Promise<A>) =>
    Effect.tryPromise({
      try: () => fn(client),
      catch: (cause) => new StripeError({ cause }),
    }).pipe(Effect.withSpan(`stripe.${fn.name ?? "use"}`));

  return { use };
});

export class StripeClient extends Context.Tag("StripeClient")<
  StripeClient,
  IStripeClient
>() {
  static Default = Layer.effect(this, make).pipe(
    Layer.annotateSpans({ module: "StripeClient" })
  );
}

// Usage
const createCustomer = Effect.gen(function* () {
  const stripe = yield* StripeClient;

  const customer = yield* stripe.use((client) =>
    client.customers.create({ email: "user@example.com" })
  );

  return customer;
});

Weekly Installs
48
Repository
rhyssullivan/ef…er-skill
GitHub Stars
10
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn