---
title: react
url: https://skills.sh/dalestudy/skills/react
---

# react

skills/dalestudy/skills/react
react
Installation
$ npx skills add https://github.com/dalestudy/skills --skill react
SKILL.md
React

Vercel 가이드 기반 React 성능 최적화 베스트 프랙티스. 프레임워크 비종속(Next.js, Remix, Vite 등 무관).

각 규칙의 상세 설명과 코드 예제는 references/ 참고. 원본 Vercel 가이드의 전체 규칙(Next.js/SSR 포함)은 vercel-react-best-practices 참고.

규칙 카테고리
우선순위	카테고리	영향도	접두사
1	비동기 워터폴 제거	CRITICAL	async-
2	번들 사이즈 최적화	CRITICAL	bundle-
3	리렌더링 최적화	MEDIUM	rerender-
4	렌더링 성능	MEDIUM	rendering-
5	클라이언트 데이터/이벤트	MEDIUM	client-
6	JavaScript 성능	LOW-MEDIUM	js-
7	고급 패턴	LOW	advanced-
빠른 참조
1. 비동기 워터폴 제거 (CRITICAL)
async-parallel - Promise.all()로 독립 작업 병렬화
async-defer-await - 불필요한 경로에서 await 지연
async-suspense-boundaries - Suspense로 부분 렌더링
async-dependencies - 부분 의존성 있는 작업의 최대 병렬화
2. 번들 사이즈 최적화 (CRITICAL)
bundle-barrel-imports - barrel file 직접 import 지양
bundle-lazy - React.lazy로 코드 스플리팅
bundle-preload - hover/focus 시 프리로드
bundle-conditional - 기능 활성화 시에만 모듈 로드
bundle-defer-third-party - 비필수 서드파티 하이드레이션 후 로드
3. 리렌더링 최적화 (MEDIUM)
rerender-functional-setstate - 함수형 setState로 안정적 콜백
rerender-lazy-state-init - 비용 큰 초기값 지연 초기화
rerender-derived-state - 파생 boolean 구독
rerender-dependencies - Effect 의존성 좁히기
rerender-memo - memo로 비용 큰 작업 분리
rerender-transitions - startTransition으로 UI 반응성 유지
rerender-ref-callbacks - ref callback으로 DOM 접근 (useRef+useEffect 대체)
rerender-avoid-usestate - useState 대체 패턴 판단 가이드
rerender-url-state - URL 검색 매개변수로 상태 관리
rerender-form-libraries - 폼 라이브러리로 useState 제거
rerender-discriminated-union - discriminated union으로 불가능한 상태 방지
rerender-use-reducer - useReducer로 복잡한 상태 전이
rerender-derived-state-no-effect - 파생 상태를 렌더링 중 계산
rerender-defer-reads - 상태 읽기를 사용 시점으로 지연
rerender-memo-with-default-value - memo 컴포넌트 기본값 상수 추출
rerender-move-effect-to-event - 인터랙션 로직을 이벤트 핸들러로 이동
rerender-simple-expression-in-memo - 단순 표현식에 useMemo 사용 금지
rerender-use-ref-transient-values - 일시적 값에 useRef 사용
rerender-simplify-useeffect - useEffect를 커스텀 훅으로 단순화
4. 렌더링 성능 (MEDIUM)
rendering-animate-svg-wrapper - SVG 래퍼로 GPU 가속
rendering-content-visibility - 긴 목록 오프스크린 최적화
rendering-hoist-jsx - 정적 JSX 호이스팅
rendering-conditional-render - 삼항 연산자로 falsy 버그 방지
rendering-hydration-no-flicker - 하이드레이션 불일치 없이 깜빡임 방지
rendering-activity - Activity/CSS로 상태/DOM 보존
rendering-svg-precision - SVG 좌표 정밀도 축소 (SVGO)
rendering-usetransition-loading - useTransition으로 수동 로딩 상태 대체
rendering-inp-css-feedback - CSS :active + yield로 INP 개선
rendering-composition-vs-early-return - Composition vs Early Return 선택 기준
5. 클라이언트 데이터/이벤트 (MEDIUM)
client-passive-event-listeners - passive로 스크롤 지연 제거
client-localstorage-schema - localStorage 버전 관리
client-sync-external-store - useSyncExternalStore로 브라우저 API/외부 스토어 구독
client-event-listeners - 글로벌 이벤트 리스너 중복 제거
client-data-dedup - TanStack Query/SWR로 데이터 페칭 중복 제거
client-abort-redundant-work - AbortController로 불필요한 비동기 작업 취소
6. JavaScript 성능 (LOW-MEDIUM)
js-index-maps - Map으로 O(1) 조회
js-tosorted-immutable - toSorted()로 불변성 유지
js-set-map-lookups - Set으로 O(1) 멤버십 검사
js-early-exit - 조기 반환으로 불필요한 처리 방지
js-batch-dom-css - DOM 읽기/쓰기 분리로 레이아웃 스래싱 방지
js-cache-function-results - 반복 함수 호출 모듈 레벨 캐싱
js-cache-property-access - 루프 내 프로퍼티 접근 캐싱
js-cache-storage - localStorage/cookie 읽기 메모리 캐싱
js-combine-iterations - 복수 배열 순회를 단일 루프로
js-hoist-regexp - RegExp를 모듈 스코프로 호이스팅
js-length-check-first - 배열 비교 시 길이 먼저 확인
js-min-max-loop - 정렬 대신 단일 루프로 min/max
js-iterator-helpers - Iterator Helper로 지연 처리
7. 고급 패턴 (LOW)
advanced-event-handler-refs - 이벤트 핸들러를 ref에 저장 (재구독 방지)
advanced-use-latest - useEffectEvent/useLatest로 안정적 콜백 ref
advanced-init-once - 앱 초기화를 컴포넌트가 아닌 모듈 레벨에서
advanced-closure-scope - 클로저 스코프 격리로 메모리 누수 방지
Vercel 원본 가이드 추가 규칙

이 스킬은 프레임워크 비종속 규칙만 포함. Next.js/SSR 전용 규칙은 원본 참고:

규칙	영향도	설명
server-cache-react	MEDIUM	React.cache()로 요청 내 중복 제거
server-cache-lru	HIGH	LRU 캐시로 요청 간 캐싱
server-serialization	HIGH	RSC 경계에서 직렬화 최소화
server-parallel-fetching	CRITICAL	컴포넌트 구성으로 서버 데이터 병렬 페칭
server-after-nonblocking	MEDIUM	after()로 논블로킹 후처리
server-auth-actions	MEDIUM	서버 액션 인증 검증
server-dedup-props	LOW	중복 props 제거
bundle-dynamic-imports	CRITICAL	next/dynamic으로 동적 임포트
rendering-hydration-suppress-warning	LOW	suppressHydrationWarning 사용
async-api-routes	MEDIUM	API 라우트 비동기 패턴

원본 전체 문서: vercel-labs/agent-skills: react-best-practices

참고
React 공식 문서
React Compiler - 사용 시 memo(), useMemo() 수동 적용 불필요
Vercel: How we made the dashboard twice as fast
Vercel: How we optimized package imports
Weekly Installs
168
Repository
dalestudy/skills
GitHub Stars
4
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass