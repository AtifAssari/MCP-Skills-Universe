---
rating: ⭐⭐⭐
title: peach-e2e-browse
url: https://skills.sh/peachsolution/peach-harness/peach-e2e-browse
---

# peach-e2e-browse

skills/peachsolution/peach-harness/peach-e2e-browse
peach-e2e-browse
Installation
$ npx skills add https://github.com/peachsolution/peach-harness --skill peach-e2e-browse
SKILL.md
AI 브라우저 탐색

agent-browser(기본) + playwright-cli(fallback)로 Chrome Beta를 제어한다. 사람이 Chrome Beta 고정 프로필에서 로그인을 완료한 브라우저를 AI가 이어받아 탐색한다.

단독 실행 가능: e2e/ 폴더나 ./e2e.sh setup이 없어도 agent-browser만 설치되어 있으면 핵심 기능(탐색/검증/확인)이 동작한다.

강제 게이트

아래 4가지는 권장이 아니라 강제 규칙이다.

agent-browser connect 9222 후 반드시 agent-browser tab list를 먼저 실행한다.
사용자가 탭 번호를 명시하기 전에는 어떤 조작도 하지 않는다.
금지: open, tab, click, fill, press, eval
Google 로그인, OAuth, 관리자 콘솔, 결제, 기존 프로필 세션 유지가 중요한 작업은 분석만 수행하고 실행은 사용자 확인 후 진행한다.
agent-browser가 비정상 동작하면 OS 레벨 우회(open -a, 다른 브라우저 실행, 다른 프로필 경로 사용) 금지. 즉시 상태를 보고하고 사용자 확인을 받는다.

인증이 필요한 페이지에 도달하면 AI가 직접 로그인/2차 인증을 시도하지 않는다. Chrome Beta의 $HOME/.chrome-beta-e2e-profile에서 사용자가 직접 로그인이나 인증을 완료하도록 안내한 뒤, 같은 프로필 세션을 AI가 이어받는다.

도구 역할 분담
용도	도구	이유
탐색/검증/확인	agent-browser	eval 6.6x 빠름, 토큰 2.3x 절약
시나리오 실행	playwright-cli (./e2e.sh run)	lib/connect.js 기반 시나리오 인프라
fallback	playwright-cli (직접 호출)	iframe 등 agent-browser 미지원 기능
의사결정 트리 (최우선 확인)
웹사이트 도착
│
├─ connect 9222 → tab list → 사용자 탭 번호 확인
│  ├─ 탭 미확인
│  │  → 상태만 보고하고 대기
│  ├─ Google/OAuth/관리자/결제/기존 세션 유지 작업
│  │  → 탭 번호 확인 후에도 분석만 수행, 실행은 사용자 승인 후
│  └─ 일반 탐색 작업
│     → 아래 흐름 진행
│
├─ eval "document.title + ' | ' + location.href" 로 현재 상태 파악
│
├─ 정상 텍스트 반환 (일반 HTML / SPA)
│  ├─ 데이터 읽기 → eval 한 줄로 해결
│  ├─ 셀렉터를 알고 있다 → eval로 click/value 설정
│  │  ⚠️ eval click()은 isTrusted:false — 보안 폼에서 안 될 수 있음
│  │  → 안 되면 snapshot -i -c -s "form" → click ref
│  ├─ 셀렉터를 모른다
│  │  ├─ find role button --name "버튼명" (snapshot 없이 탐색)
│  │  └─ snapshot -i -c -s "관심영역" → ref 확보 → click/fill
│  └─ SPA 로딩 대기 필요
│     → wait --load networkidle 또는 eval "!!querySelector('타겟')" 체크
│  └─ SPA 입력 후 버튼이 [disabled] 유지
│     → 이벤트 미발행 의심 (Angular ngModel / React controlled input)
│     → eval "el.dispatchEvent(new Event('input', {bubbles:true}))"
│     → 여전히 [disabled] → change 이벤트도 추가 발행
│     → 여전히 [disabled] → CDP Input.insertText (자동화 스크립트 필요)
│     (references/SPA-프레임워크-입력패턴.md §1 참조)
│  └─ 파일 업로드 필요 (input[type=file])
│     → 기본값: CDP 인터셉트 방식 (처음 시도하는 사이트는 항상 이 방법)
│        인터셉트 스크립트 백그라운드 실행 (TAB_TARGET_ID로 탭 특정)
│        → agent-browser click (isTrusted:true 필수 — eval click은 무시됨)
│        → Page.fileChooserOpened 이벤트 → setFileInputFiles(backendNodeId)
│     ⚠️ 직접 주입(DOM.setFileInputFiles)은 OS 다이얼로그가 안 뜨는 사이트임이
│        검증된 경우에만 허용. 다이얼로그가 열리면 CDP/Escape로 닫을 수 없어 세션 막힘.
│     (references/SPA-프레임워크-입력패턴.md §3 스크립트 템플릿 참조)
│
├─ "로딩 중입니다" or 빈 값 → Flutter/Canvas 의심
│  ├─ eval "!!querySelector('flt-semantics-placeholder')" → Flutter 확정
│  ├─ accessibility 활성화
│  │  ├─ eval "querySelector('flt-semantics-placeholder')?.click()"
│  │  └─ 안 되면 snapshot -i -c → click e2 (flutter-view)
│  ├─ 활성화 후 → snapshot -i -c로 ref 확보 → 메뉴 조작
│  ├─ ⚠️ 페이지 이동마다 accessibility 재활성화 필요
│  └─ **우회 전략 (권장)**: dart.js에서 API method 추출 → fetch 직접 호출
│     (references/Flutter-웹앱-패턴.md 참조)
│
├─ iframe 내부 접근
│  → playwright-cli fallback (references/iframe-모달-패턴.md 참조)
│
└─ 세션 끊김 (CDP error: Session not found)
   → connect 9222 → tab list → tab N → eval "document.title"


핵심: 탭 확인이 먼저, eval은 그 다음. snapshot은 최후수단. Flutter는 API 직접 호출이 최강.

워크플로우
1. 환경 확인 (인라인 체크 — e2e/ 폴더 불필요)
2. CDP 연결 (agent-browser connect 9222)
3. tab list → 사용자에게 탭 목록 보여주고 작업 탭 확인
4. 선택된 탭에서 작업 (eval/click/snapshot)
5. 결과를 사용자에게 보고


중단 조건

탭 번호 미확인
Chrome Beta 고정 프로필 유지가 핵심인 작업
로그인/OAuth/관리자 콘솔/결제 등 민감 세션 작업
agent-browser connect, tab list, tab new가 비정상 응답인 상태

위 조건이면 조작하지 말고 현재 상태만 보고한 뒤 사용자 지시를 기다린다.

1단계: 환경 확인 (단독 실행)

e2e/ 폴더나 setup 스크립트 없이 직접 확인한다:

# a) agent-browser 설치 여부
command -v agent-browser && echo "✅ agent-browser 설치됨" || echo "❌ agent-browser 미설치 → npm i -g agent-browser"

# b) Chrome Beta CDP 연결 여부
curl -s http://127.0.0.1:9222/json/version && echo "✅ CDP 연결됨" || echo "❌ CDP 미연결"


CDP 미연결이면 자동 복구를 먼저 시도한다.

e2e/ 폴더가 있으면 cd e2e && ./e2e.sh chrome & 실행 후 sleep 4, cd e2e && ./e2e.sh status로 재확인한다.
e2e/ 폴더가 없으면 아래 OS별 Chrome Beta CDP 실행 명령을 직접 실행한 뒤 재확인한다.
재확인 후에도 미연결이면 그때 사용자에게 수동 실행을 안내한다.
Chrome Beta CDP 직접 실행 (CDP 미연결 시)

⚠️ 프로필 경로 고정 규칙: --user-data-dir 는 반드시 $HOME/.chrome-beta-e2e-profile 고정. 어떤 상황에서도 다른 경로로 변경하지 않는다. 오류가 나더라도 경로는 바꾸지 않는다. 이 프로필에 Google 계정, OAuth, 사내 SSO 같은 인증을 미리 유지해 두면 이후 AI가 같은 세션을 이어받아 작업할 수 있다.

macOS:

# --disable-extensions: 확장 프로그램이 웹 콘텐츠에 다크모드를 강제 적용하는 문제 방지
nohup "/Applications/Google Chrome Beta.app/Contents/MacOS/Google Chrome Beta" \
  --remote-debugging-port=9222 \
  "--remote-allow-origins=*" \
  "--user-data-dir=$HOME/.chrome-beta-e2e-profile" \
  --disable-extensions > /tmp/chrome-beta.log 2>&1 &
sleep 5
curl -s "http://127.0.0.1:9222/json/version"


Windows (Git Bash):

# --disable-extensions: 확장 프로그램이 웹 콘텐츠에 다크모드를 강제 적용하는 문제 방지
"/c/Program Files/Google/Chrome Beta/Application/chrome.exe" \
  --remote-debugging-port=9222 \
  --remote-allow-origins=* \
  --user-data-dir="$(cygpath -w "$HOME/.chrome-beta-e2e-profile")" \
  --disable-extensions &


e2e/ 폴더가 있다면 cd e2e && ./e2e.sh chrome으로도 실행 가능.

2단계: CDP 연결
agent-browser connect 9222


1회 연결하면 세션 유지. 매 명령마다 재연결 불필요.

수동 검증 전 CDP 상주 세션 점검 필수 agent-browser connect 9222 실행 시 상주 daemon이 생성된다. 이 daemon이 붙어 있으면 사이트의 native alert/confirm/prompt가 자동으로 닫힐 수 있다. 사용자가 직접 dialog를 확인해야 하는 작업이면 먼저 연결 상태를 점검한다.

lsof -iTCP:9222 -sTCP:ESTABLISHED -n -P   # 연결 확인
ps -p <PID> -o pid,ppid,command=            # daemon 식별
kill <PID>                                   # daemon 종료


상세: references/native-dialog-주의사항.md 참조

3단계: 탭 확인 → 사용자에게 선택 요청
agent-browser tab list


탭 목록을 사용자에게 보여주고 "몇 번 탭에서 작업할까요?" 라고 확인한다. 출력 예:

  [0] Daum - https://www.daum.net/
  [1]  - chrome://webui-toolbar.top-chrome/
→ [2] NAVER - https://www.naver.com/
  [3] Google - https://www.google.com/


→ 표시는 agent-browser 내부 포커스이지 Chrome UI 포커스가 아니다. CDP는 사용자가 Chrome에서 보고 있는 탭을 알 수 없다. 따라서 작업 시작 전 반드시 사용자에게 탭 번호를 확인해야 한다.

사용자가 탭 번호를 지정하면 agent-browser tab N으로 전환 후 진행한다.

탭 번호를 받기 전에는 여기서 멈춘다. open, tab, click, fill, press, eval을 이어서 실행하지 않는다. Google/OAuth/관리자 콘솔처럼 세션 유지가 핵심인 작업은 탭 번호를 받아도 추가 실행 승인이 없으면 분석만 수행한다. agent-browser tab N 직후에는 반드시 eval "document.title + ' | ' + location.href"로 예상한 탭이 맞는지 재확인한다. 다르면 tab list를 다시 출력하고 재선택한다.

4단계: 조작

선택된 탭에서 eval → 판단 → 추가 eval/click.

5단계: 결과 보고

eval 결과, 페이지 상태를 텍스트로 요약하여 사용자에게 보고.

탭 규칙

현재 탭에서 작업. 탭 전환은 사용자 명시적 지시 시에만.

사용자가 URL을 지정하면 → 현재 탭에서 agent-browser open "URL"
"N번 탭으로 가줘" → agent-browser tab N
"새 탭으로 열어줘" → agent-browser tab new "URL"
AI가 임의로 탭 전환/새 탭 열기 금지

탭 번호 확인 전에는 위 명령을 하나도 실행하지 않는다. 민감 세션 작업에서는 탭 번호 확인 뒤에도 사용자 실행 승인 전까지는 분석만 수행한다.

open URL --new-tab 사용 금지! 기존 탭을 덮어쓴다. 새 탭은 반드시 tab new "URL" 사용.

조작 명령
페이지 이동
agent-browser open "https://대상URL"

JavaScript 실행 (기본 조작 방법)
# 값 읽기
agent-browser eval "document.title"
agent-browser eval "document.querySelector('#field').value"
agent-browser eval "document.querySelectorAll('tr').length"

# 조건부 읽기
agent-browser eval "document.querySelector('.cls') ? document.querySelector('.cls').innerText.trim() : '없음'"

# 목록 추출 (JSON.stringify 패턴)
agent-browser eval "JSON.stringify(Array.from(document.querySelectorAll('li')).map(function(el){return el.innerText}))"

# 클릭
agent-browser eval "document.querySelector('a.link').click()"

# 값 입력
agent-browser eval "document.querySelector('#keyword').value = '검색어'"


eval은 단순 표현식만. IIFE (function(){...})() 사용 금지 -- 직렬화 오류 발생. 여러 동작은 각각 별도 eval로 나눠서 실행한다.

요소 탐색 (snapshot -- 부득이할 때만)
# 인터랙티브 요소만 + 컴팩트 출력 (필수 옵션)
agent-browser snapshot -i -c

# CSS 범위 제한 (더 절약)
agent-browser snapshot -i -c -s "table"


전체 snapshot 금지. 토큰 비교:

전체 snapshot: ~65,700 토큰
snapshot -i -c: ~9,800 토큰
eval: 1460 토큰

snapshot 후 ref로 조작:

agent-browser click e10
agent-browser fill e37 "검색어"
agent-browser press Enter


ref는 DOM 변경 시 무효. 클릭/이동 후 반드시 다시 snapshot.

클릭 / 입력 / 키보드 (ref 기반)
agent-browser click e10
agent-browser fill e37 "검색어"
agent-browser press Enter

스크린샷
agent-browser screenshot          # 터미널 출력
agent-browser screenshot result.png  # 파일 저장 (토큰 미소비)

fallback: playwright-cli (iframe/모달)

agent-browser가 지원하지 못하는 경우 playwright-cli로 전환한다.

전환이 필요한 경우
iframe 내부 요소 접근 (jQuery UI Dialog + iframe 모달)
agent-browser snapshot에 iframe 태그만 보이고 내부가 비어있을 때
사전 확인 (e2e/ 폴더 불필요)
# playwright-cli 설치 확인
command -v playwright-cli || echo "❌ 미설치 → npm i -g @playwright/cli"

# config 파일 확인 — 없으면 생성
if [ ! -f "$HOME/.playwright/cli.config.json" ]; then
  mkdir -p "$HOME/.playwright"
  echo '{"browser":{"cdpEndpoint":"http://localhost:9222","isolated":false}}' > "$HOME/.playwright/cli.config.json"
  echo "✅ playwright-cli config 생성됨"
fi


isolated: false 필수 — 기본값 true면 CDP에 연결해도 새 브라우저가 열린다.

직접 호출 방법

e2e/ 폴더의 pwc.sh 래퍼 없이 직접 호출한다:

# playwright-cli 세션 오픈 (1회)
playwright-cli --config="$HOME/.playwright/cli.config.json" open

# 탭 전환
playwright-cli --config="$HOME/.playwright/cli.config.json" tab-select N

# iframe 내부 읽기
playwright-cli --config="$HOME/.playwright/cli.config.json" eval "document.querySelector('iframe[src*=대상]').contentDocument.querySelector('#element').innerText"

# iframe 내부 입력 + 클릭 -- 별도 eval로 분리
playwright-cli --config="$HOME/.playwright/cli.config.json" eval "document.querySelector('iframe[src*=대상]').contentDocument.querySelector('#keyword').value = '검색어'"
playwright-cli --config="$HOME/.playwright/cli.config.json" eval "document.querySelector('iframe[src*=대상]').contentDocument.querySelector('input[type=submit]').click()"


e2e/ 폴더가 있다면 ./e2e/pwc.sh 래퍼를 사용해도 동일하다. 상세 패턴은 references/iframe-모달-패턴.md 참조

실측 비교 데이터

동일 시나리오 (구글 → Gmail → 메일 15개 추출), Chrome Beta CDP 9222:

항목	agent-browser	playwright-cli	배율
eval 평균 속도	189ms	1,249ms	6.6x
총 명령 시간	1,521ms	6,257ms	4.1x
총 출력 바이트	1,918B	4,343B	2.3x
eval 출력 형식	결과값만	결과+코드+탭목록+페이지정보	-
핵심 규칙
eval 우선 -- 데이터 읽기, 클릭, 입력 모두 eval로 먼저 시도. snapshot은 셀렉터를 모를 때만.
작업 탭을 사용자에게 확인 -- CDP는 사용자의 포커스 탭을 알 수 없음. tab list를 보여주고 탭 번호를 명시적으로 확인한다.
새 탭은 tab new URL -- open URL --new-tab 사용 금지 (기존 탭 덮어씀).
snapshot은 -i -c 필수 -- 전체 snapshot 금지. 토큰 폭발.
eval은 단순 표현식만 -- IIFE 금지, 여러 동작은 별도 eval로 분리.
ref는 매번 변경됨 -- DOM이 바뀌면 이전 ref 무효, 다시 snapshot.
iframe → playwright-cli fallback -- agent-browser는 iframe 내부 접근 불가.
connect 9222 필수 -- 모든 작업 전 CDP 연결 확인.
프로필 경로 고정 -- Chrome Beta 실행 시 --user-data-dir은 반드시 $HOME/.chrome-beta-e2e-profile. 오류가 나도 경로 변경 금지.
eval click()은 isTrusted:false -- 보안 폼에서 무시될 수 있음. 안 되면 snapshot → click ref.
Flutter 사이트는 API 직접 호출이 최강 -- dart.js에서 method 추출 → fetch 호출. UI 탐색 대비 토큰 99% 절약. (references/Flutter-웹앱-패턴.md 참조)
세션 끊김 감지 -- eval 실패 시 connect 9222 재실행. 매번 connect 반복은 금지.
screenshot + Read 절대 금지 -- 이미지 열기 = 수천 토큰. eval "body.innerText.substring(0,200)"으로 대체.
수동 native dialog 검증 전 CDP 상주 세션 점검 -- agent-browser daemon이 붙어 있으면 alert/confirm이 즉시 닫힐 수 있다. 새 탭/새로고침보다 lsof → ps → kill이 우선이다. (references/native-dialog-주의사항.md)
dialog를 가로챈 시나리오는 반드시 원복 -- window.alert/confirm override, 전역 dialog listener, 강제 dismiss 코드는 finally에서 해제한다. (references/native-dialog-주의사항.md)
외부 서비스 전환은 fallback 필수 -- click() 한 줄이 아니라 load + 지연 + 직접 이동 fallback 패턴 사용. (references/외부서비스-링크전환-패턴.md)
디버깅/재현은 E2E_TAB_ID 우선 -- --tab N 인덱스는 흔들릴 수 있다. 특정 URL 탭 재현은 targetId 고정이 안전하다. (references/탭-선택-패턴.md)
탭 번호 확인 전 조작 금지 -- tab list는 필수 게이트다. 사용자 탭 선택 전에는 open/tab/eval/click/fill/press 실행 금지.
로그인/프로필 민감 작업은 분석 우선 -- Google/OAuth/관리자/결제/기존 세션 유지 페이지는 분석만 수행하고 실행은 사용자 확인 후 진행.
OS 레벨 브라우저 우회 금지 -- agent-browser 실패 시 open -a, 다른 브라우저 호출, 프로필 무시 실행 금지. 보고 후 대기. (references/고정프로필-강제게이트-패턴.md)
인증은 사용자, 세션 활용은 AI -- 로그인/2차 인증/보안 확인은 사용자가 Chrome Beta 고정 프로필에서 직접 수행하고, AI는 완료된 세션만 이어받아 작업한다. (references/고정프로필-강제게이트-패턴.md)
Angular/React fill 실패 → 이벤트 발행 추가 -- fill 후 버튼이 [disabled]이면 eval dispatchEvent(new Event('input', {bubbles:true}))를 반드시 시도한다. 여전히 안 되면 change 이벤트도 발행. (references/SPA-프레임워크-입력패턴.md)
tab N 직후 title 재확인 -- tab list → 사용자 응답 → tab N 후 반드시 eval "document.title + ' | ' + location.href"로 탭이 맞는지 검증한다. 예상과 다르면 tab list 재출력 후 재선택.
OS 파일 다이얼로그는 인터셉트로 차단 -- CDP Escape 키 이벤트와 agent-browser press Escape 모두 macOS 네이티브 파일 다이얼로그(XPC 서비스)에는 무효다. Page.setInterceptFileChooserDialog(enabled:true) → agent-browser click → Page.fileChooserOpened → setFileInputFiles(backendNodeId) 순서로 OS 다이얼로그 자체를 차단한다. (references/SPA-프레임워크-입력패턴.md §3)
참조 문서
문서	용도
references/agent-browser-명령어.md	agent-browser 전체 명령어 레퍼런스
references/playwright-cli-명령어.md	fallback 전용 (iframe 등 agent-browser 미지원 시)
references/iframe-모달-패턴.md	jQuery UI Dialog + iframe 모달 접근 패턴
references/Flutter-웹앱-패턴.md	Flutter 웹앱 판별 / accessibility / API 직접 호출
references/토큰-최적화-실측데이터.md	명령별 토큰 비용 실측 비교표 + 예산 가이드
references/native-dialog-주의사항.md	CDP 상주 세션의 native dialog 자동 dismiss 문제 + 점검 절차
references/외부서비스-링크전환-패턴.md	외부 서비스 링크 전환 시 fallback 패턴
references/탭-선택-패턴.md	--tab N vs E2E_TAB_ID 선택 기준
references/SPA-프레임워크-입력패턴.md	Angular/React controlled input 이벤트 발행, 숨겨진 file input TreeWalker 탐색, CDP Input.insertText
references/고정프로필-강제게이트-패턴.md	민감 세션/고정 프로필 작업의 중단 조건과 우회 금지 규칙
Weekly Installs
34
Repository
peachsolution/p…-harness
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn