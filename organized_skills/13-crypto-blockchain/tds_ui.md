---
rating: ⭐⭐
title: tds-ui
url: https://skills.sh/jingjing2222/create-rn-miniapp/tds-ui
---

# tds-ui

skills/jingjing2222/create-rn-miniapp/tds-ui
tds-ui
Installation
$ npx skills add https://github.com/jingjing2222/create-rn-miniapp --skill tds-ui
SKILL.md
TDS UI Decision Skill

이 Skill은 MiniApp 화면 요구사항을 TDS React Native 컴포넌트로 정확히 매핑할 때 사용한다. 이 Skill은 TDS를 다시 설명하는 문서가 아니다. source repo에서는 metadata.json의 공식 llms.txt / llms-full.txt URL을 canonical source로 삼고, create scaffold가 설치한 workspace에서는 같은 문서를 generated/llms.txt / generated/llms-full.txt로 mirror해 local lookup을 빠르게 만든다. 기본 탐색은 항상 index-first다. 먼저 llms.txt에서 docs path와 canonical heading 후보를 좁히고, 필요한 section만 llms-full.txt로 확인한다. 이 Skill은 그 공식 문서로 라우팅하고 repo-specific anomaly와 답변 계약만 덧입히는 overlay다.

Use when
입력/선택 UI를 결정해야 할 때
리스트, 요약, 스텝, 카드, 배너, 차트 같은 화면 구성 요소를 정해야 할 때
로딩/에러/완료/토스트/다이얼로그 같은 상태 UI를 정해야 할 때
상단/하단 UI boundary를 정해야 할 때
공개 문서 slug와 실제 export가 일치하는지 확인해야 할 때
Do not use for
MiniApp capability / API 탐색
route path, navigation tree, page entry 설계
provider/runtime bootstrap
TDS 밖 native module 선택
Canonical truth sources
https://tossmini-docs.toss.im/tds-react-native/llms.txt
https://tossmini-docs.toss.im/tds-react-native/llms-full.txt
generated/anomalies.json

source repo에는 llms snapshot을 커밋하지 않는다. 대신 create scaffold는 tds-ui 설치 직후 metadata.json의 installMirrors 경로에 공식 llms 문서를 내려받아 넣는다. official docs와 로컬 overlay가 충돌하면, 컴포넌트 의미와 prop contract는 official llms를 우선하고 로컬 파일은 slug/import/docs-missing 같은 anomaly와 output contract만 보강한다.

Read in order
metadata.json
upstreamSources에서 공식 llms URL을 찾고, 설치된 workspace라면 installMirrors 경로를 같이 확인한다.
generated/llms.txt 또는 공식 llms.txt
설치된 workspace에서 mirror가 있으면 local file을 우선 사용한다.
index entrypoint다. 어떤 component/foundation/start/migration 문서가 있는지, docs path와 canonical heading alias가 무엇인지 먼저 확인한다.
generated/llms-full.txt 또는 공식 llms-full.txt
설치된 workspace에서 mirror가 있으면 local file을 우선 사용한다.
llms.txt에서 shortlist가 정해진 뒤에만 연다.
후보 section heading을 검색해서 examples, interface, foundation semantics를 확인한다.
generated/anomalies.json
docs slug alias, root import gap, export-only / docs-missing gate를 로컬 overlay로 적용한다.
AGENTS.md
output contract와 review rule index를 확인한다.
references/*.md
공식 문서를 대체하지 않는다.
필요한 category의 index shortlist 이름과 repo-specific comparison 질문만 빠르게 확인한다.
Decision algorithm
요구사항을 먼저 분류한다.
text-input / search / multi-select / single-select / boolean-toggle / content-tabs / menu
numeric-stepper / keypad / range-slider / rating
list / list-summary / grid / accordion / step-flow / hero-amount / article / disclaimer / chart
primary-action / text-action / icon-action / dialog / toast / loading / result / error-page
top-nav / bottom-action / sheet
metadata.json에서 official llms URL과 install mirror 경로를 확인한다.
설치된 workspace면 generated/llms.txt, 아니면 공식 llms.txt에서 canonical section 이름, docs path, heading alias를 먼저 찾는다.
component 선택이면 component section을 찾는다.
color / typography / visual token 질문이면 foundation section을 먼저 찾는다.
설치/마이그레이션 질문이면 start / migration section을 찾되, 이 Skill의 본업은 UI 선택이라는 점을 명시한다.
shortlist가 정해진 뒤에만 설치된 workspace면 generated/llms-full.txt, 아니면 공식 llms-full.txt를 열어 해당 section heading의 examples, interface, foundation semantics를 읽는다.
docs slug mismatch는 anomaly alias를 따른다.
chart -> docs Chart/bar-chart
stepper-row -> docs stepper
export mismatch는 anomaly 규칙을 따른다.
navbar는 docs는 있지만 root export path가 다르므로 @toss/tds-react-native/extensions/page-navbar를 먼저 확인한다.
public docs 없는 export는 기본 추천 대상이 아니다.
agreement, bottom-cta, bottom-sheet, fixed-bottom-cta, icon, tooltip, top, txt
이 항목은 사용자가 명시적으로 요구하거나 기존 코드베이스에서 이미 쓰고 있을 때만 추천한다.
추천 시 반드시 export-only / docs-missing이라고 표시한다.
paragraph는 기본 추천 금지다.
component dir는 있지만 root export와 public docs가 약하다.
상태 관리는 공식 문서와 references/form-patterns.md 기준을 그대로 따른다.
controlled: value/onChange, checked/onCheckedChange, onValueChange
uncontrolled: defaultValue, defaultChecked
로컬 references는 공식 문서 요약본이 아니라 비교 관점 checklist로만 쓴다.
최종 답변에는 반드시 아래를 포함한다.
추천 컴포넌트
왜 이 컴포넌트인지
왜 가장 가까운 대안이 아닌지
controlled/uncontrolled 패턴
loading / error / empty / disabled / a11y 고려사항
docs URL
root export module
anomaly note 여부
위 7항 중 하나라도 빠지면 incomplete answer로 간주한다.
export-only를 추천할 때는 반드시 doc-backed fallback도 같이 적는다.
TDS로 대체 가능한 RN primitive를 직접 추천하지 않는다.
Canonical lookup shortcuts
input / selection surfaces: references/form-patterns.md
action / feedback / loading surfaces: references/feedback-and-loading.md
list / navigation / boundary surfaces: references/layout-and-navigation.md
display / visual utility surfaces: references/display-patterns.md
category shortlist와 foundation/start/migration 진입: references/decision-matrix.md
export gap, docs-missing gate, output contract: references/export-gaps.md, references/policy-summary.md
upstream URL + install mirror contract: metadata.json
Required comparisons
text-field vs search-field
checkbox vs switch
radio vs segmented-control vs tab
numeric-spinner vs keypad vs slider
button vs text-button vs icon-button
toast vs dialog vs result vs error-page
list-row vs table-row
bottom-info vs post
doc-backed vs export-only / docs-missing
Refusal / fallback rules
문서도 없고 기존 코드베이스 근거도 없으면 export-only 컴포넌트는 추천하지 않는다.
대신 doc-backed 조합으로 대체안을 제시한다.
unknown bottom action surface는 우선 button 중심 조합으로 답하고 anomaly note를 남긴다.
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