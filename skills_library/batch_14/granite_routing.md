---
title: granite-routing
url: https://skills.sh/jingjing2222/create-rn-miniapp/granite-routing
---

# granite-routing

skills/jingjing2222/create-rn-miniapp/granite-routing
granite-routing
Installation
$ npx skills add https://github.com/jingjing2222/create-rn-miniapp --skill granite-routing
SKILL.md
Granite Routing Skill

이 Skill은 frontend의 route, page entry, navigation 흐름을 설계하거나 수정할 때 사용합니다.

Use when
route path, page file, params 설계를 결정할 때
createRoute, validateParams, navigation usage 예시가 필요할 때
entry layer와 implementation layer를 어떻게 나눌지 정할 때
Do not use for
MiniApp/AppInToss capability / 공식 API 탐색: docs-search 또는 공식 문서
TDS component 선택과 UI boundary: tds-ui
tRPC contract/app-router 변경 순서: trpc-boundary
읽는 순서
references/patterns.md에서 route/page/navigation 패턴을 확인한다.
강제 규칙과 금지 import는 references/frontend-policy.md를 기준으로 본다.
기능 존재 여부와 공식 API lookup은 docs-search 또는 Granite/AppInToss 공식 문서로 확인하고, UI 선택은 tds-ui로 넘긴다.
핵심 원칙
규칙 요약은 references/frontend-policy.md가 소유한다.
이 Skill은 구현 패턴과 예시를 제공하고, 규칙의 근거 문서를 대체하지 않는다.
route 설계 전에는 entry file, impl file, params 흐름, router.gen.ts 동기화까지 같이 본다.
Weekly Installs
12
Repository
jingjing2222/cr…-miniapp
First Seen
Mar 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass