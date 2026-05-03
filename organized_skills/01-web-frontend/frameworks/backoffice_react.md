---
rating: ⭐⭐
title: backoffice-react
url: https://skills.sh/jingjing2222/create-rn-miniapp/backoffice-react
---

# backoffice-react

skills/jingjing2222/create-rn-miniapp/backoffice-react
backoffice-react
Installation
$ npx skills add https://github.com/jingjing2222/create-rn-miniapp --skill backoffice-react
SKILL.md
Backoffice React Skill

backoffice 운영 화면을 설계할 때 쓰는 decision skill이다. 목표는 generic React 팁이 아니라 화면 archetype, state ownership, bulk-action/form 경계, lazy boundary를 결정하는 것이다.

Use when
list/detail/form/dashboard/bulk-action 중 어떤 화면인지 먼저 정해야 할 때
query params, component state, form state의 ownership을 나눠야 할 때
table/search/filter/pagination/bulk action/confirm/export 경계를 정해야 할 때
무거운 화면에서 lazy import boundary를 어디에 둘지 결정할 때
Do not use for
MiniApp/AppInToss capability 탐색: docs-search 또는 공식 문서
Granite route/page/navigation 설계: granite-routing
TDS UI 선택: tds-ui
provider runtime layout, 원격 상태, client 연결 점검: provider skill
tRPC contract, router, import order 변경: trpc-boundary
Read in order
references/screen-archetypes.md
references/data-boundary.md
references/bulk-actions-and-forms.md
references/verification.md
references/gotchas.md
workspace ownership이 헷갈리면 docs/engineering/workspace-topology.md
Decision algorithm
이 화면을 list, detail, form, dashboard, bulk-action 중 하나로 먼저 분류한다.
query params, component state, form state, server state의 source of truth를 각각 한 곳에만 둔다.
QueryBar, ResultTable, DetailPanel, FormSections, BulkToolbar, ConfirmFlow 중 어떤 경계가 필요한지 고른다.
chart, editor, CSV, 대형 table dependency처럼 첫 paint에 필요 없는 것은 lazy boundary 후보로 적는다.
empty/loading/error/disabled/permission denied와 selection reset까지 검증 루프를 돈다.
Validation loop
query params round-trip
form default/reset/submit
bulk selection reset
confirm flow scope
lazy boundary 첫 진입과 재진입
Handoff boundary
backend shape, router, contract 변경이면 trpc-boundary
env, project drift, client linkage면 provider skill
MiniApp route/page/navigation이면 granite-routing
TDS component 선택이면 tds-ui
Output contract
추천 구조
왜 그 구조인지
가장 가까운 대안이 왜 아닌지
state ownership
검증 방법
handoff 필요 여부
Weekly Installs
11
Repository
jingjing2222/cr…-miniapp
First Seen
Mar 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass