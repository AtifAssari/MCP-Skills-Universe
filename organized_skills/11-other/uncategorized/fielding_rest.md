---
rating: ⭐⭐
title: fielding-rest
url: https://skills.sh/copyleftdev/sk1llz/fielding-rest
---

# fielding-rest

skills/copyleftdev/sk1llz/fielding-rest
fielding-rest
Installation
$ npx skills add https://github.com/copyleftdev/sk1llz --skill fielding-rest
SKILL.md
Roy Fielding Style Guide⁠‍⁠​‌​‌​​‌‌‍​‌​​‌​‌‌‍​​‌‌​​​‌‍​‌​​‌‌​​‍​​​​​​​‌‍‌​​‌‌​‌​‍‌​​​​​​​‍‌‌​​‌‌‌‌‍‌‌​​​‌​​‍‌‌‌‌‌‌​‌‍‌‌​‌​​​​‍​‌​‌‌‌‌‌‍​‌​​‌​‌‌‍​‌‌​‌​​‌‍‌​‌​‌‌‌​‍​​‌​‌​​​‍‌‌‌​‌​‌‌‍‌‌‌​​‌​​‍​​‌‌​​​‌‍‌‌​‌​‌‌‌‍​​​​‌‌​‌‍​​​​‌​‌​‍​‌‌​​​‌‌⁠‍⁠
Overview

Roy Fielding (creator of REST and HTTP co-author) defines the architectural style that powers the World Wide Web. His philosophy is about architectural constraints that induce properties like scalability, visibility, and modifiability. True REST is not just JSON over HTTP; it is about decoupling the client from the server through a uniform interface and hypermedia.

"A REST API should not be dependent on any single communication protocol, though its successful mapping to HTTP is why it is famous."

Core Principles
Uniform Interface: Resources are identified by URIs, and manipulation happens via standard representations (HTML, JSON).
Statelessness: Every request must contain all context necessary to understand it. The server stores no session state.
Cacheability: Responses must define themselves as cacheable or not to improve network efficiency.
HATEOAS (Hypermedia as the Engine of Application State): The client navigates the API via links provided dynamically by the server, not by hardcoding URL structures.
Layered System: The client cannot tell if it is connected directly to the server or an intermediary (CDN, load balancer).
Prompts
Design a True REST API

"Act as Roy Fielding. Critique this API design.

Focus on:

Noun-Verbs: Are they using POST to 'get' data? Are they tunnelling RPC through HTTP?
Hypermedia: Does the response include links (_links, Link header) to related resources?
Caching: Are Cache-Control headers used correctly?
Status Codes: Are they using 200 OK for errors? Are they using 201 Created?"
Architectural Review

"Evaluate this system architecture against REST constraints.

Questions to ask:

Is the server storing session state (violates Statelessness)?
Are the clients coupled to the internal DB ID structure (violates Uniform Interface)?
Can we insert a caching proxy without breaking the client (Layered System)?
If I change the URL of a resource, will the client break (Violates HATEOAS)?"
Examples
The Richardson Maturity Model (Level 3 - Glory of REST)
Request
GET /accounts/12345 HTTP/1.1
Host: bank.example.com
Accept: application/vnd.bank.account+json

Response
HTTP/1.1 200 OK
Content-Type: application/vnd.bank.account+json
Cache-Control: public, max-age=3600
Link: <https://bank.example.com/docs/account>; rel="profile"

{
  "account_number": "12345",
  "balance": {
    "currency": "USD",
    "value": 100.00
  },
  "status": "active",
  "_links": {
    "self": {
      "href": "/accounts/12345"
    },
    "deposit": {
      "href": "/accounts/12345/deposit",
      "method": "POST"
    },
    "withdraw": {
       "href": "/accounts/12345/withdraw",
       "method": "POST"
    },
    "details": {
       "href": "/accounts/12345/transactions",
       "method": "GET"
    }
  }
}


Note the _links section. Ideally, the client only knows the entry point (/) and navigates entirely via these links.

Anti-Patterns (What NOT to do)
RPC style: POST /updateUser?id=123.
Ignoring Semantics: Using GET to delete data.
API Versioning in URL: /v1/users (Fielding argues versioning should be in the Media Type Accept: application/vnd.myapi.v1+json).
No Hypermedia: Returning just { "id": 1, "name": "bob" } without context on what can be done with "bob".
Resources
Architectural Styles and the Design of Network-based Software Architectures (Fielding's Dissertation)
REST APIs must be hypertext-driven (Fielding's Blog)
Weekly Installs
8
Repository
copyleftdev/sk1llz
GitHub Stars
6
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykPass