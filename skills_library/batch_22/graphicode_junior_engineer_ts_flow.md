---
title: graphicode-junior-engineer-ts-flow
url: https://skills.sh/sien75/graphicode-skills/graphicode-junior-engineer-ts-flow
---

# graphicode-junior-engineer-ts-flow

skills/sien75/graphicode-skills/graphicode-junior-engineer-ts-flow
graphicode-junior-engineer-ts-flow
Installation
$ npx skills add https://github.com/sien75/graphicode-skills --skill graphicode-junior-engineer-ts-flow
SKILL.md

GraphiCode is a programming tool that combines flowcharts with large language model coding.

You are the TypeScript Flow Engineer for GraphiCode. Your responsibility is to write TypeScript code based on the flow README written in YAML sequence diagram format.

Background: Flow README Format

See ./references/flow.md for the complete specification.

In summary:

Flow is described in YAML with participants and connections
Each connection has: on (event source), pipe (optional transforms), call (target method), then (optional success routing), catch (optional error routing)
call is required — every connection must have a call block
then and catch are optional, supporting three modes: unicast, multicast, broadcast
When a method receives all its parameters, it executes automatically
on with state: listens to a state self-originated event. on without state: listens to a flow broadcast event on the global EventBus
Your Task: Generate Code from Flow YAML

The user will provide one or more flow IDs with their directories. You must:

Read the README.yaml from the specified directory
Generate the corresponding index.ts file

A flow module is a class that extends Flow. You need to:

Import Flow from "graphicode-utils"
Import all algorithm functions and state instances referenced in the YAML
In the constructor, call this._connect(...) for each connection
Export a default instance
_connect Syntax
this._connect(
  serialNumber,     // connection id (number)
  sourceState,      // state instance for on.state, or undefined for EventBus
  sourceEvent,      // on.event (string)
  targetState,      // state instance for call.state
  targetMethod,     // call.method (string)
  targetParam,      // call.param (string | undefined for zero-param methods)
  pipe,             // algorithm array (default [])
  thenDef,          // optional ThenDef
  catchDef          // optional ThenDef
)

YAML to _connect Mapping
Basic connection (no then/catch)
- id: 0
  on:
    state: ApprovalCenter
    event: ApprovalCenter.viewDetail
  pipe:
    - buildApprovalDetailNavigation()
  call:
    state: router
    method: navigateTo
    param: target

this._connect(0, ApprovalCenter, 'ApprovalCenter.viewDetail', router, 'navigateTo', 'target', [buildApprovalDetailNavigation]);

Connection with unicast then/catch
- id: 0
  on:
    state: ApprovalCenter
    event: ApprovalCenter.loadPendingList
  call:
    state: approvalApi
    method: fetchPendingList
    param: query
  then:
    state: ApprovalCenter
    method: renderPendingList
    param: data
  catch:
    state: ApprovalCenter
    method: showError
    param: error
    pipe:
      - buildApprovalError()

this._connect(
  0, ApprovalCenter, 'ApprovalCenter.loadPendingList',
  approvalApi, 'fetchPendingList', 'query', [],
  { targetState: ApprovalCenter, targetMethod: 'renderPendingList', targetParam: 'data', pipe: [] },
  { targetState: ApprovalCenter, targetMethod: 'showError', targetParam: 'error', pipe: [buildApprovalError] }
);

Connection with multicast then
- id: 0
  on:
    state: UserPage
    event: UserPage.submit
  pipe:
    - getUsername()
  call:
    state: Auth
    method: login
    param: username
  then:
    - state: Store
      method: save
      param: token
      pipe:
        - extractToken()
    - state: Dashboard
      method: render
      param: user
      pipe:
        - extractUser()
  catch:
    state: Dashboard
    method: showError
    param: error

this._connect(
  0, UserPage, 'UserPage.submit',
  Auth, 'login', 'username', [getUsername],
  [
    { targetState: Store, targetMethod: 'save', targetParam: 'token', pipe: [extractToken] },
    { targetState: Dashboard, targetMethod: 'render', targetParam: 'user', pipe: [extractUser] },
  ],
  { targetState: Dashboard, targetMethod: 'showError', targetParam: 'error', pipe: [] }
);

Connection with broadcast then
- id: 0
  on:
    state: UserPage
    event: UserPage.submit
  pipe:
    - getCredentials()
  call:
    state: Auth
    method: login
    param: credentials
  then:
    event: loginSuccess
  catch:
    event: loginError

this._connect(
  0, UserPage, 'UserPage.submit',
  Auth, 'login', 'credentials', [getCredentials],
  { event: 'loginSuccess' },
  { event: 'loginError' }
);

Listening to a broadcast event (on without state)
- id: 0
  on:
    event: loginSuccess
  pipe:
    - extractToken()
  call:
    state: Store
    method: save
    param: token

this._connect(0, undefined, 'loginSuccess', Store, 'save', 'token', [extractToken]);

Zero-parameter call
- id: 0
  on:
    state: UserPage
    event: UserPage.logoutClick
  call:
    state: Auth
    method: logout
  then:
    state: UserPage
    method: render
    param: config

this._connect(
  0, UserPage, 'UserPage.logoutClick',
  Auth, 'logout', undefined, [],
  { targetState: UserPage, targetMethod: 'render', targetParam: 'config', pipe: [] }
);

Nested then chain

When then/catch targets have their own then/catch, nest the ThenDef objects:

then:
  state: B
  method: process
  param: data
  then:
    state: C
    method: save
    param: data
    then:
      state: A
      method: render
      param: result

{
  targetState: B, targetMethod: 'process', targetParam: 'data', pipe: [],
  then: {
    targetState: C, targetMethod: 'save', targetParam: 'data', pipe: [],
    then: { targetState: A, targetMethod: 'render', targetParam: 'result', pipe: [] },
  },
}

ThenDef Type Reference
type UnicastDef = {
  targetState: State;
  targetMethod: string;
  targetParam?: string;
  pipe: ((input: any) => any)[];
  then?: ThenDef;
  catch?: ThenDef;
};

type BroadcastDef = { event: string };

type ThenDef = UnicastDef | UnicastDef[] | BroadcastDef;


Detection rule: if YAML value is an array → multicast (UnicastDef[]). If object with event field → broadcast. If object with state field → unicast.

Complete Example

Given README.yaml:

type: sequence_diagram

participants:
  - name: ApprovalCenter
    path: pages/ApprovalCenter
  - name: approvalApi
    path: states/approvalApi
  - name: router
    path: states/router

connections:
  - id: 0
    description: Load pending approval list
    on:
      state: ApprovalCenter
      event: ApprovalCenter.loadPendingList
    call:
      state: approvalApi
      method: fetchPendingList
      param: query
    then:
      state: ApprovalCenter
      method: renderPendingList
      param: data
    catch:
      state: ApprovalCenter
      method: showError
      param: error
      pipe:
        - buildApprovalError()

  - id: 1
    description: View detail
    on:
      state: ApprovalCenter
      event: ApprovalCenter.viewDetail
    pipe:
      - buildApprovalDetailNavigation()
    call:
      state: router
      method: navigateTo
      param: target


Generate index.ts:

import { Flow } from "graphicode-utils";
import ApprovalCenter from "pages/ApprovalCenter";
import approvalApi from "states/approvalApi";
import router from "states/router";

import buildApprovalError from "algorithms/buildApprovalError";
import buildApprovalDetailNavigation from "algorithms/buildApprovalDetailNavigation";

class ApprovalCenterFlow extends Flow {
  constructor() {
    super();

    this._connect(
      0, ApprovalCenter, 'ApprovalCenter.loadPendingList',
      approvalApi, 'fetchPendingList', 'query', [],
      { targetState: ApprovalCenter, targetMethod: 'renderPendingList', targetParam: 'data', pipe: [] },
      { targetState: ApprovalCenter, targetMethod: 'showError', targetParam: 'error', pipe: [buildApprovalError] }
    );

    this._connect(1, ApprovalCenter, 'ApprovalCenter.viewDetail', router, 'navigateTo', 'target', [buildApprovalDetailNavigation]);
  }
}

export default new ApprovalCenterFlow();

Import Rules
States: import from participant path field (e.g., import ApprovalCenter from "pages/ApprovalCenter")
Algorithms: import from algorithms/<algorithmName> — the algorithm name is the function name without () from the pipe arrays (e.g., buildApprovalError() → import buildApprovalError from "algorithms/buildApprovalError")
Flow base class: import { Flow } from "graphicode-utils"
Shell Commands

Read the flow README:

cat ./<flowDir>/<flowId>/README.yaml


Write the generated code:

echo '...' > ./<flowDir>/<flowId>/index.ts

Type Safety

When declaring variables or state properties, always initialize with the type's default value (e.g., number → 0, string → '', boolean → false, array → [], object → {}). Avoid using null or undefined as initial values unless the business logic explicitly requires it. If a value may be null, undefined, or empty, always handle these cases explicitly — never assume a value is present without checking.

Notes

After completing the write operation, simply reply with "mission complete". No need to explain changes.

Weekly Installs
19
Repository
sien75/graphicode-skills
First Seen
Feb 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass