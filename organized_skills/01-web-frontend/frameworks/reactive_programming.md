---
rating: ⭐⭐
title: reactive-programming
url: https://skills.sh/aj-geddes/useful-ai-prompts/reactive-programming
---

# reactive-programming

skills/aj-geddes/useful-ai-prompts/reactive-programming
reactive-programming
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill reactive-programming
SKILL.md
Reactive Programming
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Build responsive applications using reactive streams and observables for handling asynchronous data flows.

When to Use
Complex async data flows
Real-time data updates
Event-driven architectures
UI state management
WebSocket/SSE handling
Combining multiple data sources
Quick Start

Minimal working example:

import {
  Observable,
  Subject,
  BehaviorSubject,
  fromEvent,
  interval,
} from "rxjs";
import {
  map,
  filter,
  debounceTime,
  distinctUntilChanged,
  switchMap,
} from "rxjs/operators";

// Create observable from array
const numbers$ = new Observable<number>((subscriber) => {
  subscriber.next(1);
  subscriber.next(2);
  subscriber.next(3);
  subscriber.complete();
});

numbers$.subscribe({
  next: (value) => console.log(value),
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
RxJS Basics	RxJS Basics
Search with Debounce	Search with Debounce
State Management	State Management
WebSocket with Reconnection	WebSocket with Reconnection
Combining Multiple Streams	Combining Multiple Streams
Backpressure Handling	Backpressure Handling
Custom Operators	Custom Operators
Best Practices
✅ DO
Unsubscribe to prevent memory leaks
Use operators to transform data
Handle errors properly
Use shareReplay for expensive operations
Combine streams when needed
Test reactive code
❌ DON'T
Subscribe multiple times to same observable
Forget to unsubscribe
Use nested subscriptions
Ignore error handling
Make observables stateful
Weekly Installs
306
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass