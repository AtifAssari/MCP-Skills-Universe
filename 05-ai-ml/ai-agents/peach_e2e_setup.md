---
rating: ⭐⭐⭐
title: peach-e2e-setup
url: https://skills.sh/peachsolution/peach-harness/peach-e2e-setup
---

# peach-e2e-setup

skills/peachsolution/peach-harness/peach-e2e-setup
peach-e2e-setup
Installation
$ npx skills add https://github.com/peachsolution/peach-harness --skill peach-e2e-setup
SKILL.md
peach-e2e-setup — E2E 테스트 환경 설정

대상 프로젝트에 E2E 테스트 인프라를 설정한다. npm 글로벌 도구 설치를 확인하고, Chrome Beta 존재를 검증하고, e2e/ 폴더에 인프라 코드를 배포한다.

페르소나

E2E 환경 설정 전문가. 글로벌 도구와 Chrome Beta가 준비되었는지 확인하고, 인프라 코드를 프로젝트에 복사한다. 기존 시나리오 폴더는 절대 건드리지 않는다.

전제조건
대상 프로젝트 루트에서 실행 (peach-harness 자체가 아닌 대상 프로젝트)
macOS 또는 Windows 환경 (Windows는 Git Bash 필요)
Workflow
Step 1: npm 글로벌 도구 설치 체크

다음 3개 도구의 설치 여부를 확인한다:

# agent-browser (탐색/검증/확인용 기본 도구)
command -v agent-browser && echo "✅ agent-browser 설치됨" || echo "❌ agent-browser 미설치"

# playwright-cli (시나리오 실행 + iframe fallback용)
command -v playwright-cli && echo "✅ playwright-cli 설치됨" || echo "❌ playwright-cli 미설치"

# playwright-core (CDP 연결 라이브러리)
node -e "require('playwright-core')" 2>/dev/null && echo "✅ playwright-core 설치됨" || echo "❌ playwright-core 미설치"


미설치 도구가 있으면 사용자에게 안내한다:

agent-browser: npm install -g agent-browser
playwright-cli: npm install -g @playwright/cli
playwright-core: npm install -g playwright-core
한 번에 설치: npm install -g agent-browser @playwright/cli playwright-core

자동 설치하지 않는다. 사용자에게 명령어를 안내하고 확인을 받는다.

Step 2: Chrome Beta 설치 여부 확인

OS에 따라 경로가 다르다:

macOS:

ls -d "/Applications/Google Chrome Beta.app" 2>/dev/null && echo "✅ Chrome Beta 설치됨" || echo "❌ Chrome Beta 미설치"


Windows (Git Bash):

[ -f "/c/Program Files/Google/Chrome Beta/Application/chrome.exe" ] && echo "✅ Chrome Beta 설치됨" || echo "❌ Chrome Beta 미설치"


미설치 시 안내:

설치 URL: https://www.google.com/chrome/beta/
기본 Chrome과 동시 실행 가능, E2E 전용으로 분리 사용

참고: e2e.sh는 uname -s로 OS를 자동 감지하여 Chrome 경로를 분기 처리한다. 직접 경로를 하드코딩하지 않아도 된다. 운영 권장: Chrome Beta는 $HOME/.chrome-beta-e2e-profile 같은 고정 프로필로 열어 Google 계정, OAuth, 사내 SSO 인증을 유지한다. 이후 AI는 같은 프로필 세션을 이어받아 작업하고, 인증이 다시 필요하면 사용자가 그 프로필에서 직접 로그인/인증을 완료한다.

Step 3: 프로젝트 루트에 e2e/ 폴더 생성
mkdir -p e2e/lib

Step 4: 인프라 코드 복사

references/ 폴더의 인프라 코드 4개를 e2e/에 복사한다.

소스 (references/)	대상 (e2e/)
e2e.sh	e2e/e2e.sh
pwc.sh	e2e/pwc.sh
connect.js	e2e/lib/connect.js
selector.js	e2e/lib/selector.js
gmail-메일목록.js	e2e/시나리오/gmail-메일목록.js (최초 1회, 없을 때만)

references 파일을 Read 도구로 읽은 뒤 Write 도구로 대상 경로에 작성한다. 인프라 파일은 항상 최신으로 덮어쓴다 (기존 파일이 있어도 덮어씀).

Step 5: 시나리오 폴더 생성 + 테스트 시나리오 배포
# 시나리오 폴더가 없을 때만 생성. 있으면 절대 건드리지 않음.
if [ ! -d "e2e/시나리오" ]; then
  mkdir -p "e2e/시나리오"
  echo "✅ e2e/시나리오/ 폴더 생성됨"
else
  echo "✅ e2e/시나리오/ 폴더 이미 존재 (건드리지 않음)"
fi


테스트 시나리오 배포 (최초 설정 시 동작 검증용):

references/gmail-메일목록.js → e2e/시나리오/gmail-메일목록.js
없으면 무조건 복사 (최초 설치)
있으면 내용 비교 후 다를 때만 사용자에게 업데이트 여부 질문

처리 순서:

파일이 없으면 → 무조건 복사, 질문 없음
파일이 있으면 → references 내용과 비교
동일하면 → "최신 상태" 메시지 출력 후 스킵
다르면 → 변경 요약을 보여주고 "업데이트하시겠습니까? (y/N)" 질문
y → 덮어씀
N (기본) → 스킵
파일 없음          → 복사 (질문 없음)
파일 있음 + 동일   → "✅ gmail-메일목록.js 최신 상태"
파일 있음 + 다름   → diff 요약 출력 → "업데이트하시겠습니까? (y/N)"
                      y → 덮어씀 / N → 스킵


비교는 Read 도구로 두 파일을 읽어 내용이 동일한지 확인한다. diff 요약은 변경된 핵심 부분(몇 줄이 바뀌었는지 등)을 간략히 설명한다.

Step 6: 실행 권한 부여
chmod +x e2e/e2e.sh e2e/pwc.sh

Step 7: 완료 메시지

설정 결과를 요약 출력한다:

✅ E2E 환경 설정 완료

배포된 인프라 코드:
  e2e/e2e.sh        — E2E 통합 CLI
  e2e/pwc.sh        — playwright-cli CDP 래퍼
  e2e/lib/connect.js — Chrome CDP 연결 모듈
  e2e/lib/selector.js — 탭/시나리오 선택기

다음 단계:
  1. cd e2e && ./e2e.sh setup    — 환경 자동 체크 + 설정
  2. cd e2e && ./e2e.sh chrome   — Chrome Beta CDP 모드 실행
  3. Chrome Beta 고정 프로필에서 Google 로그인/필요한 인증 완료
  4. cd e2e && ./e2e.sh run 시나리오/gmail-메일목록.js  — 테스트 시나리오 실행

주의사항
시나리오 폴더 보호: e2e/시나리오/ 폴더가 이미 존재하면 절대 덮어쓰거나 삭제하지 않는다
인프라 파일은 항상 덮어씀: e2e.sh, pwc.sh, connect.js, selector.js는 references의 최신 버전으로 항상 교체
글로벌 도구 자동 설치 금지: 사용자에게 명령어를 안내하고 확인을 받은 후 진행
시나리오 실행은 반드시 ./e2e.sh run: node 시나리오.js 직접 실행 시 playwright-core를 못 찾음. e2e.sh가 NODE_PATH에 전역 npm 모듈 경로를 설정해야 정상 동작
수동 dialog 검증 전 상주 daemon 점검: agent-browser connect 9222 실행 시 생성되는 상주 daemon이 native alert/confirm을 자동으로 닫을 수 있다. 수동 검증이 필요하면 lsof -iTCP:9222 -sTCP:ESTABLISHED -n -P로 확인 후 종료. 상세: peach-e2e-browse/references/native-dialog-주의사항.md
targetId 기반 탭 고정 실행: 특정 탭을 정확히 지정해야 할 때 --tab N 대신 E2E_TAB_ID 환경변수를 사용한다. 상세: peach-e2e-browse/references/탭-선택-패턴.md
인증은 사용자가 직접 처리: 로그인, 2차 인증, 보안 확인은 Chrome Beta 고정 프로필에서 사용자가 직접 완료한다. AI는 완료된 세션만 이어받는다.
완료 조건 체크리스트
 npm 글로벌 도구 3개 설치 상태 확인됨 (agent-browser, playwright-cli, playwright-core)
 Chrome Beta 설치 상태 확인됨
 e2e/ 폴더 구조 생성됨
 인프라 코드 4개 복사됨 (e2e.sh, pwc.sh, connect.js, selector.js)
 e2e/시나리오/ 폴더 생성됨 (기존 존재 시 미변경)
 테스트 시나리오 gmail-메일목록.js 배포됨 (없으면 복사, 있고 다르면 사용자 확인 후 업데이트)
 e2e.sh, pwc.sh 실행 권한 부여됨
 완료 메시지 출력됨
 수동 dialog 검증 전 상주 daemon 점검 방법 안내됨
Weekly Installs
33
Repository
peachsolution/p…-harness
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn