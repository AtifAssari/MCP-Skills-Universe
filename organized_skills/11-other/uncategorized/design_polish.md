---
rating: ⭐⭐⭐
title: design-polish
url: https://skills.sh/vp-k/flutter-craft/design-polish
---

# design-polish

skills/vp-k/flutter-craft/design-polish
design-polish
Installation
$ npx skills add https://github.com/vp-k/flutter-craft --skill design-polish
SKILL.md
디자인 폴리싱 스킬 v2.0

디자인 지식 기반(서비스 유형별 규칙, 컴포넌트 체크리스트, UX 규칙) + 실시간 시각 비교(Puppeteer 스크린샷) + WCAG 자동 검사(axe-core) + 트렌드 검색(WebSearch) 통합 폴리싱.

지식 기반 리소스
knowledge/: 서비스 유형별 UI 규칙, 컴포넌트 체크리스트, UX 규칙 (마크다운 직접 Read)
data/: 66개 디자인 스타일, 96개 색상 팔레트, 57개 타이포그래피, 13개 기술 스택 가이드 (JSON + BM25 검색)
scripts/search.cjs: Node.js BM25 검색 엔진
인수
--apply: (옵션) 개선안을 코드에 직접 적용
--wcag-only: (옵션) WCAG 접근성 체크만 수행
--no-wcag: (옵션) WCAG 체크 생략
$1: (옵션) 레퍼런스 사이트 (미지정시 프로젝트 유형에 맞게 자동 선택)
$2: (옵션) 기능 키워드 (미지정시 전체 디자인 폴리싱)
사용 예시
/design-polish                    # 전체 자동 폴리싱 + WCAG 체크
/design-polish --apply            # 폴리싱 + 코드 적용
/design-polish --wcag-only        # WCAG 접근성 체크만
/design-polish mobbin             # Mobbin에서 검색
/design-polish godly hero         # Godly에서 hero 검색
/design-polish --apply godly hero # hero 폴리싱 + 코드 적용

실행 플로우 개요
전제조건 확인
    ↓
0단계: 프로젝트 분석 + 서비스 유형 감지 + 스크린샷 캡처 [Glob, Read, Bash]
    ↓
1단계: WCAG 접근성 체크 (axe-core) [Bash, Read]
    ↓
1.5단계: 디자인 지식 로딩 [Read, Bash]
    ↓
2단계: 레퍼런스 사이트 선택
    ↓
3단계: 트렌드 검색 → 레퍼런스 캡처 [WebSearch, Bash]
    ↓
4단계: Gap 분석 (시각 비교 + 지식 기반) [Read]
    ↓
5단계: 개선안 도출 (8단계 우선순위)
    ↓
6단계: 결과 출력
    ↓
7단계: 코드 적용 (--apply 시) [Edit, Bash]
    ↓
Pre-delivery 체크리스트

전제조건 확인

실행 전 다음 조건을 확인합니다:

1. 개발 서버 실행 확인
# Mac/Linux - 서버 상태 확인
curl -s -o /dev/null -w "%{http_code}" http://localhost:3000

# Windows PowerShell - 서버 상태 확인
try { (Invoke-WebRequest -Uri http://localhost:3000 -UseBasicParsing -TimeoutSec 5).StatusCode } catch { 0 }


자동 포트 감지 (서버가 3000이 아닐 수 있음):

# Mac/Linux - 실행 중인 개발 서버 포트 탐지
lsof -i -P | grep LISTEN | grep -E ':(3000|5173|8080|4200)'

# Windows PowerShell - 실행 중인 개발 서버 포트 탐지
Get-NetTCPConnection -State Listen | Where-Object { $_.LocalPort -in 3000,5173,8080,4200 }


서버가 실행 중이 아니면 사용자에게 안내:

"개발 서버를 먼저 실행해주세요. (예: npm run dev)"

2. 플러그인 의존성 확인
# 플러그인 디렉토리에서 npm install 실행 여부 확인
ls ~/.claude/plugins/marketplaces/design-polish/node_modules/puppeteer


없으면 안내:

"플러그인 의존성을 설치해주세요: cd ~/.claude/plugins/marketplaces/design-polish && npm install"

3. Node.js 확인
node --version

0단계: 프로젝트 분석 + 서비스 유형 감지

사용 도구: Glob, Read, Bash

프로젝트 유형 감지
디렉토리 구조: src/, components/, pages/, app/ 등
프레임워크: React, Vue, Flutter, Next.js, Nuxt 등
스타일링: CSS, Tailwind, styled-components, CSS Modules, SCSS 등
서비스 유형 감지

프로젝트 코드에서 서비스 유형 신호를 자동 감지합니다:

감지 신호	서비스 유형
결제/장바구니/상품/checkout 코드	Online Shop
인증+대시보드+subscription	SaaS Platform
의료 용어, HIPAA, patient	Healthcare Service
차트+거래+지갑+crypto	Finance & Trading
학습+퀴즈+진도+course	Education & Learning
포트폴리오+작품+projects	Portfolio
.gov, 접근성 중심	Government Service
chat+AI+prompt+stream	AI & Chatbot
메뉴+예약+food	Food & Restaurant
booking+destination+travel	Travel & Booking
property+listing+map	Real Estate
game+score+level+player	Gaming
article+news+breaking	News & Media
feed+like+share+follow	Social Media
workout+fitness+health	Fitness & Gym
럭셔리+프리미엄+브랜드+high-end	Luxury Brand
에이전시+케이스스터디+creative+팀	Creative Agency
웰니스+명상+마음챙김+calm	Wellness & Health
admin+대시보드+analytics+지표	Admin Dashboard
IDE+터미널+코드에디터+syntax+CLI	Developer Tool

감지 방법: Grep으로 주요 코드 파일에서 키워드 빈도 분석, 가장 높은 점수의 서비스 유형을 선택합니다.

디자인 파일 탐지
유형	패턴
컴포넌트	**/*.tsx, **/*.jsx, **/*.js, **/*.vue, **/*.svelte, **/*.dart
스타일	**/*.css, **/*.scss, **/tailwind.config.*
레이아웃	**/layout.*, **/App.*, **/page.*, **/_app.*
현재 디자인 스크린샷 캡처

Bash로 캡처 스크립트 실행:

# 캡처 스크립트 실행 (${CLAUDE_PLUGIN_ROOT}는 플러그인 설치 경로로 자동 치환됨)
node "${CLAUDE_PLUGIN_ROOT}/scripts/capture.cjs" / /about /pricing

# 포트 변경시
BASE_URL=http://localhost:5173 node "${CLAUDE_PLUGIN_ROOT}/scripts/capture.cjs" /


저장 위치: .design-polish/screenshots/current-*.png

캡처 후 Read로 이미지 분석
Read(".design-polish/screenshots/current-main.png")


분석 항목:

레이아웃 구조
색상 팔레트
타이포그래피
컴포넌트 스타일
1단계: WCAG 접근성 체크

사용 도구: Bash, Read

체크 실행
# WCAG 체크 포함 캡처
node "${CLAUDE_PLUGIN_ROOT}/scripts/capture.cjs" --wcag /

체크 항목 (axe-core 기반)
카테고리	체크 항목	WCAG 기준
색상 대비	텍스트-배경 대비	4.5:1 (AA)
색상 대비	대형 텍스트 대비	3:1 (AA)
색상 대비	UI 컴포넌트 대비	3:1
텍스트 크기	최소 텍스트 크기	12px 이상 권장
터치 타겟	최소 타겟 크기	44x44px (모바일)
링크	링크 구분	밑줄 또는 3:1 대비
결과 저장
.design-polish/
├── screenshots/
│   └── current-main.png
└── accessibility/
    └── wcag-report.json

결과 확인
Read(".design-polish/accessibility/wcag-report.json")

1.5단계: 디자인 지식 로딩

사용 도구: Read, Bash

0단계에서 감지된 서비스 유형/기술 스택 정보를 기반으로 디자인 지식을 로딩합니다.

마크다운 직접 로딩 (필수 — 매 실행시)
Read("${CLAUDE_PLUGIN_ROOT}/knowledge/industry-rules.md")
Read("${CLAUDE_PLUGIN_ROOT}/knowledge/component-checklist.md")
Read("${CLAUDE_PLUGIN_ROOT}/knowledge/ux-rules.md")

스크립트 검색 (감지된 서비스 유형/키워드 기반)
# 0단계에서 감지된 서비스 유형 키워드를 사용
# 예: SaaS Platform 감지 시
node "${CLAUDE_PLUGIN_ROOT}/scripts/search.cjs" --domain style "saas dashboard minimal"

# 예: Online Shop 감지 시
node "${CLAUDE_PLUGIN_ROOT}/scripts/search.cjs" --domain color "ecommerce shopping"

# 예: Healthcare Service 감지 시
node "${CLAUDE_PLUGIN_ROOT}/scripts/search.cjs" --domain typography "medical clean accessible"

# 기술 스택 가이드 (코드 적용 시에만)
# 예: React 프로젝트 감지 시
node "${CLAUDE_PLUGIN_ROOT}/scripts/search.cjs" --domain stack --stack react "accessibility aria"

검색 예시
감지된 서비스 유형	스타일 검색	색상 검색	타이포 검색
SaaS Platform	"saas dashboard minimal"	"saas professional trust"	"modern professional clean"
Online Shop	"ecommerce vibrant card"	"ecommerce shopping"	"ecommerce clean shopping"
Healthcare Service	"healthcare accessible calm"	"healthcare calm"	"medical clean accessible"
Finance & Trading	"fintech dark glass"	"fintech crypto"	"financial trust"
Education & Learning	"education playful friendly"	"education playful"	"playful friendly"
Wellness & Health	"wellness organic biophilic"	"wellness nature calm"	"calming soft rounded"
2단계: 레퍼런스 사이트 선택

사용 도구: 판단 로직

$1 미지정시 자동 선택
프로젝트 유형	판단 기준	우선 사이트	대체 사이트
앱 UI/UX	Flutter, React Native, 모바일 우선	Mobbin	Page Flows, Refero
모던 웹/SaaS	Next.js, Nuxt, 대시보드	Godly	Dark Mode Design, Awwwards
감각적/예술적	포트폴리오, 갤러리, 아트 키워드	SiteInspire	Savee, Behance
랜딩페이지	단일 페이지, 마케팅 중심	Lapa Ninja	Httpster
UI 디테일	컴포넌트 중심, 버튼/카드 등	Dribbble	-
3단계: 트렌드 검색

사용 도구: WebSearch, Bash

3-1. WebSearch로 레퍼런스 검색

기능 단위 검색 (업종별 X)

올바른 검색:
- site:mobbin.com onboarding flow
- site:godly.website hero section
- site:dribbble.com dashboard UI 2024

잘못된 검색:
- "금융 앱 디자인"
- "게임 앱 UI"

3-2. 검색 결과에서 URL 추출

WebSearch 결과에서 유용한 레퍼런스 URL을 2-3개 선정.

3-3. Bash로 레퍼런스 캡처
# 단일 레퍼런스 캡처
node "${CLAUDE_PLUGIN_ROOT}/scripts/capture.cjs" ref "https://dribbble.com/shots/..." hero

# 여러 개 캡처 (브라우저 재사용으로 효율적)
node "${CLAUDE_PLUGIN_ROOT}/scripts/capture.cjs" ref "https://site1.com" ref1 "https://site2.com" ref2


저장 위치: .design-polish/screenshots/reference-*.png

검색 실패시 (자동 처리)
대체 사이트로 재시도: 위 표의 대체 사이트 순서대로
site: 제거: 일반 웹 검색으로 전환
키워드 일반화: 예) "checkout" → "ecommerce flow"
4단계: Gap 분석 (시각 비교 + 지식 기반)

사용 도구: Read

Read로 이미지 비교 분석
Read(".design-polish/screenshots/current-main.png")
Read(".design-polish/screenshots/reference-hero.png")

분석 영역
영역	분석 항목	지식 기반 참조
레이아웃	그리드, 여백, 정보 계층, CTA 위치	ux-rules.md → Layout
타이포그래피	폰트, 크기, 행간, 웨이트	search.cjs typography 검색 결과
색상	팔레트, 대비, 다크모드 지원	search.cjs color 검색 결과
인터랙션	호버, 전환, 애니메이션, 로딩	ux-rules.md → Animation
컴포넌트	버튼, 카드, 입력, 모달, 토스트	component-checklist.md
상태	로딩/성공/실패/빈 상태 처리	ux-rules.md → Loading & Error
접근성	WCAG 위반 항목, 터치 타겟, 포커스 표시	ux-rules.md → Accessibility
서비스 유형 적합성	industry-rules.md 기준 스타일/색상 일치 여부	industry-rules.md
스타일 매칭	search.cjs 검색 결과와 현재 디자인 비교	search.cjs style 검색 결과
지식 기반 분석 (추가)
서비스 유형 적합성: industry-rules.md에서 해당 서비스 유형의 추천 스타일/색상과 현재 디자인 비교
컴포넌트 품질: component-checklist.md의 Do/Don't 체크 — 사용 중인 컴포넌트별 위반 확인
UX 규칙 준수: ux-rules.md의 각 카테고리별 패턴 체크
스타일 매칭: search.cjs 검색 결과의 추천 스타일과 현재 디자인 비교
색상/타이포 매칭: 검색된 팔레트/폰트 페어링 vs 현재 사용 중인 값 비교
플랫폼별 추가 기준
플랫폼	핵심 기준
웹	스캔 가능성, 정보 밀도, 반응형
앱	엄지 도달 범위, 제스처, 네이티브 패턴
5단계: 개선안 도출 (8단계 우선순위)
우선순위 분류
우선순위	카테고리	영향	예시
P1	접근성 (WCAG 위반)	CRITICAL	대비 부족, 터치 타겟 미달, 포커스 미표시
P2	터치/인터랙션	CRITICAL	cursor 미지정, 타겟 크기 미달, hover 없음
P3	성능	HIGH	이미지 미최적화, reduced-motion 미지원
P4	레이아웃/반응형	HIGH	CLS, 모바일 깨짐, 뷰포트 이슈
P5	타이포/색상	MEDIUM	행간 부족, 서비스 유형 부적합 색상, 폰트 미매칭
P6	애니메이션	MEDIUM	트랜지션 누락, 과도한 모션, 타이밍 이슈
P7	스타일 적합성	MEDIUM	서비스 유형별 추천 스타일과 불일치
P8	차트/데이터	LOW	차트 접근성, 데이터 시각화 개선

각 개선안에는 다음 정보를 포함합니다:

대상 파일 경로
구체적인 변경 내용
참조 근거 (knowledge 파일, search.cjs 결과, WCAG 기준 등)
6단계: 결과 출력
출력 형식
## 프로젝트 요약

[프레임워크], [스타일링 방식] 기반 [프로젝트 유형]
감지된 서비스 유형: [서비스 유형명]

## WCAG 접근성 체크

| 항목 | 상태 | 세부사항 |
|------|------|----------|
| 색상 대비 | X 3건 위반 | btn-primary: 3.2:1 (필요: 4.5:1) |
| 터치 타겟 | O 통과 | |
| 텍스트 크기 | ! 1건 주의 | caption: 11px |

## 서비스 유형별 적합성

| 항목 | 추천 (industry-rules) | 현재 | 일치 |
|------|----------------------|------|------|
| 스타일 | Glassmorphism + Flat | Flat Design | 부분 일치 |
| 색상 무드 | Trust blue + Accent contrast | Blue + Grey | 일치 |
| 타이포 | Professional + Hierarchy | ... | ... |
| 핵심 효과 | Subtle hover (200-250ms) | 호버 없음 | 불일치 |

## 컴포넌트 체크 결과

| 컴포넌트 | 위반 항목 | 심각도 |
|---------|----------|--------|
| Button | 터치 타겟 38px (최소 44px) | HIGH |
| Card | 호버 효과 없음 | MEDIUM |
| Input | placeholder만 사용, label 없음 | HIGH |

## 트렌드 요약

- [핵심 트렌드 1]
- [핵심 트렌드 2]
- [핵심 트렌드 3]

## Gap 분석

| 영역 | 현재 | 추천 (지식 기반 + 트렌드) | Gap |
|------|------|--------------------------|-----|
| 레이아웃 | ... | ... | ... |
| 타이포그래피 | ... | [추천 폰트 페어링 + URL] | ... |
| 색상 | ... | [추천 팔레트 HEX 코드] | ... |
| 인터랙션 | ... | ... | ... |
| 컴포넌트 | ... | ... | ... |
| 접근성 | 3건 위반 | WCAG AA 준수 | 색상 대비 수정 필요 |
| 스타일 적합성 | ... | [추천 스타일명] | ... |

## 추천 리소스 (search.cjs 결과)

- **추천 스타일**: [스타일명] — [cssHints]
- **추천 색상**: Primary [HEX], Secondary [HEX], CTA [HEX], BG [HEX]
- **추천 폰트**: [Heading Font] + [Body Font] — [Google Fonts URL]

## 개선안 (8단계 우선순위)

### P1: 접근성 (CRITICAL)
- [ ] btn-primary 색상 대비 수정 (src/components/Button.tsx)

### P2: 터치/인터랙션 (CRITICAL)
- [ ] [개선안 + 대상 파일]

### P3: 성능 (HIGH)
- [ ] [개선안 + 대상 파일]

### P4: 레이아웃/반응형 (HIGH)
- [ ] [개선안 + 대상 파일]

### P5: 타이포/색상 (MEDIUM)
- [ ] [개선안 + 대상 파일]

### P6: 애니메이션 (MEDIUM)
- [ ] [개선안 + 대상 파일]

### P7: 스타일 적합성 (MEDIUM)
- [ ] [개선안 + 대상 파일]

### P8: 차트/데이터 (LOW)
- [ ] [개선안 + 대상 파일]

7단계: 코드 적용 (--apply 옵션시만)

사용 도구: Edit, Bash

스택 가이드 참조

코드 적용 전, 감지된 기술 스택의 가이드라인을 참조합니다:

# 기술 스택 가이드 검색 (적용할 영역 키워드로)
# 예: React 프로젝트 감지 시
node "${CLAUDE_PLUGIN_ROOT}/scripts/search.cjs" --domain stack --stack react "accessibility aria"

적용 순서
P1 (접근성 CRITICAL) 우선순위부터 순차 적용
P2~P4 (CRITICAL/HIGH) 적용
P5~P7 (MEDIUM) — 사용자 확인 후 적용
각 수정 후 파일 저장
적용 결과 요약 출력
적용하지 않는 것
새 라이브러리 설치 필요한 변경
대규모 구조 변경 (리팩토링 수준)
브레이킹 체인지
적용 결과 출력
## 적용 완료

| 파일 | 변경 내용 |
|------|----------|
| src/components/Button.tsx | 색상 대비 수정 (4.5:1 이상) |
| src/components/Button.tsx | hover 스타일 추가 |
| src/styles/global.css | 여백 조정 |

## 미적용 (수동 필요)

- [ ] Framer Motion 설치 필요 (애니메이션)

레퍼런스 사이트 목록
실제 서비스 UX 흐름
사이트	URL	특징
Mobbin	mobbin.com	실 서비스 스크린샷, 플로우별 정리
Page Flows	pageflows.com	영상 기반 플로우, 인터랙션 참고
Refero	refero.design	실제 서비스 UI 요소 모음
모던 웹 트렌드 (Tech & SaaS)
사이트	URL	특징
Godly	godly.website	다크 모드, 마이크로 인터랙션
Dark Mode Design	darkmodedesign.com	다크 모드 UI 큐레이션
Awwwards	awwwards.com	창의적/기술적 웹사이트
감각적 & 예술적 영감
사이트	URL	특징
SiteInspire	siteinspire.com	레이아웃, 색감, 분위기
Savee	savee.it	무드보드용 시각적 자극
Behance	behance.net	브랜딩, Case Study
랜딩 페이지 & 마케팅
사이트	URL	특징
Lapa Ninja	lapa.ninja	랜딩 페이지 레퍼런스 최다
Httpster	httpster.net	심플한 타이포그래피
UI 디테일
사이트	URL	특징
Dribbble	dribbble.com	버튼, 카드 등 디테일
Pre-delivery 체크리스트

코드 적용 후 (--apply 시) 또는 최종 결과 보고 전에 다음을 확인합니다:

시각 품질
 색상 대비 4.5:1 이상 (WCAG AA)
 일관된 border-radius (8px/12px/16px 중 택일)
 일관된 spacing scale (예: 4/8/12/16/24/32px)
 폰트 계층 명확 (h1 > h2 > h3 > body > caption)
인터랙션
 모든 클릭 가능 요소에 cursor: pointer
 호버 상태 (150-200ms transition)
 포커스 링 (2-3px, 키보드 사용자)
 로딩 상태 (스켈레톤 또는 스피너)
 에러 상태 (인라인 메시지 + 아이콘)
라이트/다크 모드
 다크 모드 전환시 깨지는 요소 없음
 다크 모드 색상 대비 유지
레이아웃
 모바일 (320px~) 깨지지 않음
 태블릿 (768px) 적절한 배치
 데스크톱 (1024px+) 최대 너비 제한
접근성 최종 점검
 axe-core 위반 0건 (또는 justified)
 키보드 네비게이션 가능
 스크린 리더 호환 (ARIA 레이블)
 prefers-reduced-motion 지원
Weekly Installs
9
Repository
vp-k/flutter-craft
GitHub Stars
6
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn