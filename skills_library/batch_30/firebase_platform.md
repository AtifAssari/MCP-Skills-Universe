---
title: firebase-platform
url: https://skills.sh/7spade/black-tortoise/firebase-platform
---

# firebase-platform

skills/7spade/black-tortoise/firebase-platform
firebase-platform
Installation
$ npx skills add https://github.com/7spade/black-tortoise --skill firebase-platform
SKILL.md
SKILL: Firebase Platform Master Guide

Consolidated reference for AngularFire SDK and Firebase Data Connect (GQL + PostgreSQL).

🔥 1. AngularFire Core (SDK)
Real-time Database & Firestore
Reactive Pattern: Use collectionData, docData and convert to signals using toSignal().
Dependency Injection: Use inject(Firestore), inject(Auth), etc.
Security: Security rules are the primary defense. Never trust the client.
Authentication
State management: Track user status in an AuthStore.
Guards: Use functional canActivate guards with Auth service.
⚡ 2. Firebase Data Connect (GQL + PostgreSQL)
Schema Workflow
Schema First: Define @table in schema.gql.
Generation: Run firebase dataconnect:sdk:generate after schema changes.
Strict Types: Use the generated SDK; never edit dataconnect-generated/.
Directive Rules
@table: Required for all database entities.
@auth: Required for all types (No public access allowed).
@default: Use for UUIDs (uuidV4()) and timestamps (request.time).
@col(name: "..."): Map JSON keys to DB columns if different.
🏗️ 3. Integration with NgRx Signals
Query Wrapping:
export const MyStore = signalStore(
  withMethods((store, dc = inject(DataConnectService)) => ({
    loadData: rxMethod<void>(
      pipe(
        switchMap(() => dc.myDataQuery()),
        tapResponse({
          next: (res) => patchState(store, { data: res.data }),
          error: console.error,
        }),
      ),
    ),
  })),
);

🔒 4. Security & Performance
Secrets: Store Firebase API keys and config in environment.ts.
Query Design: Fetch only required fields in GraphQL.
Auth Pattern: @auth(rules: [{ allow: OWNER, ownerField: "userId" }]).
No Hardcoded Secrets: Secrets must stay in environment variables or GCP Secret Manager.

Law: After any schema change, the SDK MUST be regenerated before editing application logic.

Weekly Installs
9
Repository
7spade/black-tortoise
First Seen
Feb 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass