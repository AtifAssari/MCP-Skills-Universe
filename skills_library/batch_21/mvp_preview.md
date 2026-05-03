---
title: mvp-preview
url: https://skills.sh/dev-goraebap/skills/mvp-preview
---

# mvp-preview

skills/dev-goraebap/skills/mvp-preview
mvp-preview
Installation
$ npx skills add https://github.com/dev-goraebap/skills --skill mvp-preview
SKILL.md
MVP Preview

AI와 함께 핵심 기능을 빠르게 만들고 링크로 공유하는 워크플로우.

아이디어가 구체적이지 않아도 괜찮다. 토론하면서 범위를 좁히고, 최소한의 코드로 가치를 보여준 뒤, 링크 하나로 팀이나 클라이언트에게 전달한다.

언제 적용하나
아이디어나 기능을 빠르게 눈으로 확인하고 싶을 때
클라이언트·팀원에게 기획을 링크로 공유하고 싶을 때
완성도보다 방향성 검증이 목적일 때
"이런 거 만들면 어떨까요?" 를 말 대신 코드로 보여주고 싶을 때
카테고리
카테고리	적용 상황	참조 파일
제품 맥락	세션 간 맥락 유지, 요구사항·정책·도메인 정보 축적	프로젝트 루트 brief.md (템플릿: templates/brief.md)
토론	아이디어가 막연할 때, 범위를 좁히고 싶을 때, 무엇을 만들지 결정할 때	discovery.md
구현	스택 선택, MVP 빌드 원칙, 목업 데이터, 빠른 프로토타입	build.md
공유	로컬 서버 링크 공유, 빌드 배포, 브라우저 플레이그라운드	share.md
핵심 원칙
우선순위대로 하나씩: 기능이 여러 개여도 한꺼번에 만들지 않는다. 토론에서 우선순위를 정하고, 가장 중요한 것부터 완성한 뒤 다음으로 넘어간다
목업 데이터: 실제 API 연결 불필요. 하드코딩된 데이터로 충분
해피 패스만: 에러 처리·예외·엣지 케이스는 나중에
링크로 공유: 노트북을 들고 가지 않아도 된다
커밋 없으면 미완성: 코드 변경 후 git commit + vN 태그까지 해야 그 작업이 끝난 것이다. 다음 수정 요청을 받기 전에 이전 상태가 커밋되어 있는지 반드시 확인한다
실행 방법
Step 0: 환경 확인

세 가지를 확인한다.

git 설치 여부: git --version 실행. 없으면 설치를 제안하고 진행한다 (설치 명령어는 build.md 참조)

brief.md 확인: 현재 작업 디렉토리(pwd)에 brief.md가 있는지 확인한다. 내용이 있으면 이전 맥락을 이어간다. 없으면 Step 1부터 시작한다

에이전트 권한 설정 (선택): 에이전트가 파일 생성·bash·git 등 매 작업마다 허락을 구하면 흐름이 끊긴다. 사용 중인 에이전트에 맞게 프로젝트 디렉토리에 설정 파일을 만들어두면 자동으로 진행된다. 원하면 설정해드릴 수 있다.

에이전트	파일	내용
Claude Code	.claude/settings.json	{ "defaultMode": "bypassPermissions" }
Codex CLI	.codex/config.toml	approval_policy = "never"
Gemini CLI	.gemini/settings.json	{ "approvalMode": "yolo" }

모두 프로젝트 디렉토리 기준이며 글로벌 설정을 건드리지 않는다. Gemini CLI는 일부 버전에서 이 설정이 무시될 수 있다. 그럴 경우 세션 중 Ctrl+Y로 수동 활성화한다.

Step 1: 토론

막연한 아이디어도 괜찮다. discovery.md의 질문 흐름으로 범위를 확정한다.

"어떤 제품을 만들고 있나요? 이 MVP로 무엇을 보여주고 싶으세요?"

범위가 확정되면 현재 작업 디렉토리에 brief.md를 만들거나 업데이트하고 구현으로 넘어간다.

Step 2: 스택 확인 → 구현

구현에 들어가기 전 반드시 스택을 먼저 확인한다.

현재 디렉토리에 package.json이 있으면 어떤 프레임워크인지 파악한다
없으면 사용자에게 묻는다:

"어떤 방식으로 만들까요? (1) 단일 HTML 파일 — 빌드 없이 바로 공유 가능, (2) 사용 중인 프레임워크가 있으면 알려주세요"

스택이 확정되면 build.md의 방식에 따라 구현한다.

구현 완료 = 코드 + 커밋 + 태그까지다. 아래를 반드시 실행한다:

git add .
git commit -m "feat: MVP [한 줄 요약]"
git tag v1   # 다음 이터레이션은 v2, v3 ...


다음 수정 요청을 받으면, 먼저 git tag로 현재 상태가 태그되어 있는지 확인한다. 태그가 없으면 커밋+태그 먼저, 수정은 그 다음이다.

Step 3: 결과 확인

구현한 화면을 사용자가 직접 브라우저에서 볼 수 있도록 안내한다. 개발 경험 유무에 따라 설명 방식을 조정한다.

단일 HTML 파일인 경우 — 브라우저로 바로 열기

파일 탐색기(Windows) 또는 Finder(macOS)에서 index.html 파일을 더블 클릭하세요. 브라우저가 자동으로 열립니다.

브라우저가 이미 열려 있다면:

브라우저 주소창에 파일을 드래그해서 놓으면 바로 열립니다.

프레임워크 방식인 경우 — 개발 서버 실행

package.json의 scripts를 확인해 실행 명령어를 파악한다. 프레임워크마다 다르다.

# 예시: Next.js, SvelteKit, Vite 계열
npm run dev

# 예시: Create React App
npm start

# 예시: 그 외 — package.json scripts 확인 후 적절한 명령어 안내


사용자에게는 확인한 명령어를 직접 알려준다:

터미널에 [명령어]를 입력하고 엔터를 누르세요. 터미널에 표시되는 주소(예: http://localhost:3000)를 브라우저 주소창에 입력하면 됩니다. 서버를 종료하려면 터미널에서 Ctrl + C를 누르세요.

결과가 마음에 들지 않는 경우 — 이전 버전으로 되돌리기

사용자가 "이전 버전이 나았어요" 또는 "v1로 돌아가 주세요"라고 하면 해당 태그로 되돌린다.

# 태그 목록 확인
git tag

# 특정 버전으로 되돌리기
git checkout v1


되돌린 뒤에는 현재 어느 버전인지 사용자에게 알려준다:

"v1 버전으로 돌아왔습니다. 이 상태에서 다시 수정을 이어갈까요?"

Step 4: 공유

share.md의 상황별 옵션을 골라 링크를 만든다.

상황	방법
지금 바로 링크 필요 (로컬 서버)	cloudflared tunnel --url localhost:PORT
안정적인 URL 필요 (빌드 완료)	surge ./dist my-name.surge.sh
프레임워크 프로젝트 자동 빌드 배포	npx vercel
단일 HTML 파일	CodePen에 붙여넣기
Weekly Installs
12
Repository
dev-goraebap/skills
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass