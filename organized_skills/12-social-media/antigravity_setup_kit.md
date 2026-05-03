---
rating: ⭐⭐⭐⭐⭐
title: antigravity-setup-kit
url: https://skills.sh/caleblee2050/antigravity-agent/antigravity-setup-kit
---

# antigravity-setup-kit

skills/caleblee2050/antigravity-agent/antigravity-setup-kit
antigravity-setup-kit
Installation
$ npx skills add https://github.com/caleblee2050/antigravity-agent --skill antigravity-setup-kit
SKILL.md
안티그래비티 파워 유저 세팅

이 스킬은 안티그래비티를 최강의 AI 코딩 에이전트로 만들어주는 전체 세팅 패키지입니다. "안티그래비티 세팅해줘" 또는 **"이 스킬 실행해줘"**라고 요청받으면 아래를 실행하세요.

중요: 각 단계에서 사용자에게 설치 여부를 확인하세요. 안티그래비티가 CLI를 통해 직접 설정합니다.

🚨 절대 금지사항 (최우선 규칙)

<ANTI_HALLUCINATION_POLICY> 에이전트는 절대로 스스로의 판단으로 명령어, 패키지 스펠링, 깃허브 주소, 폴더 경로, 앱 이름, 다운로드 URL 등을 추론하거나 창조(할루시네이션)해서는 안 됩니다! 특히 사용자의 글로벌 지침(user_global 등)에 기재되어 있는 이메일 주소나 개인 도메인(예: a4k.ai, google.com) 패턴을 보고, 무단으로 설치 주소 가짜 링크(a4k.ai/setup)를 창조해 다운로드를 시도하는 악성 위반 행위를 엄격히 금지합니다!

여러분은 오직, 이 문서 내 하단에 있는 코드 블록(```bash)의 스펠링 토씨 하나 틀리지 말고 100% 동일하게 복사하여 터미널에 붙여넣기로 실행해야 합니다. (예: npm i -g @googleworkspace/cli를 @anthropic/gws 따위로 유추 변형 절대 금지) </ANTI_HALLUCINATION_POLICY>

⛔ 절대로 새 폴더(antigravity-agent-v2, antigravity-agent-new 등)를 만들지 마세요. ⛔ 기존 폴더를 복제하거나 이름을 바꾸지 마세요. ⛔ 기존 설치를 무시하고 새로 클론하지 마세요.

업데이트 시에는 반드시 기존 폴더에서 migrate.sh를 사용하세요.

🔀 신규 설치 vs 업데이트 판별 (최우선 실행)

사용자가 "세팅해줘", "업데이트해줘", "새 버전 설치해줘" 등을 요청하면:

1단계: 기존 설치 확인

아래 경로에 antigravity-agent 폴더가 존재하는지 확인:

macOS: ~/dev/antigravity-agent/ 또는 find ~ -maxdepth 3 -name "antigravity-agent" -type d
Windows: Get-ChildItem -Path $env:USERPROFILE -Recurse -Directory -Filter "antigravity-agent" -Depth 3
2단계: 분기
조건	처리
폴더 없음 (신규)	→ 아래 STEP 0부터 순서대로 진행
폴더 있음 (업데이트)	→ migrate.sh 실행 (아래 '업데이트 절차' 참조)
업데이트 절차 (기존 설치가 있는 경우)
# macOS / Linux
cd ~/dev/antigravity-agent  # 기존 폴더로 이동 (절대 새 폴더 만들지 않음!)
bash setup/migrate.sh

# Windows (PowerShell)
cd "$env:USERPROFILE\dev\antigravity-agent"
bash setup/migrate.sh  # Git Bash 사용


migrate.sh가 자동으로 처리하는 것:

✅ .env, agent_config.json, 대화기록, 이미지 백업
✅ git pull로 최신 코드 받기
✅ 로컬 변경사항 stash → 자동 pop (충돌 시 안내)
✅ 백업한 설정 복원 + 머지 (새 키/필드 자동 추가)
✅ 워크플로우, 브라우저 허용목록 업데이트
✅ Python 의존성 재설치

migrate.sh 완료 후: 모바일 에이전트 실행 테스트

# macOS
cd packages/mobile-agent && bash scripts/run.sh

# Windows
cd packages\mobile-agent
powershell -ExecutionPolicy Bypass -File run.ps1


업데이트의 경우 여기서 끝입니다. 아래 STEP은 실행하지 않습니다.

STEP 0. 레포지토리 클론 (신규 설치만)

⚠️ 이 단계는 신규 설치일 때만 실행합니다. 업데이트는 위의 '업데이트 절차'를 따르세요.

macOS / Linux:

git clone https://github.com/caleblee2050/antigravity-agent.git ~/dev/antigravity-agent


Windows (PowerShell):

git clone https://github.com/caleblee2050/antigravity-agent.git "$env:USERPROFILE\dev\antigravity-agent"

⚙️ OS 감지 (STEP 0 이후 실행)

설치 시작 전 반드시 현재 OS를 확인하고 아래 표에 맞게 경로/명령어를 자동 변환하세요:

	macOS / Linux	Windows
설정 경로	~/.gemini/antigravity/	%USERPROFILE%\.gemini\antigravity\
파일 복사	cp	Copy-Item (PowerShell)
디렉토리 생성	mkdir -p	New-Item -ItemType Directory -Force
파일 목록	ls ... | wc -l	(Get-ChildItem ...).Count
모바일 에이전트	✅ 지원	✅ 지원 (Task Scheduler + pygetwindow)
STEP 0.5. 필수 의존성 완전 자동 설치 (어떠한 경우에도 터미널 요구 절대 금지)

⚠️ 중요: "터미널을 열고 명령어를 직접 치세요"라는 요청은 사용자에게 절대로 하지 마십시오!
설치하는 사용자는 초보자입니다. 에러가 나더라도 당신(에이전트)이 백그라운드 터미널을 활용하고, 사용자의 모니터에 GUI 창(팝업)을 띄우는 방식으로 100% 자동화해야 합니다.

Git / Python3 부재 시 (macOS Command Line Tools 이슈)

git이나 python3 명령어가 없거나 에러를 뱉는다면, 터미널 명령을 요구하지 마세요.
다음 명령어를 실행하여 모니터 화면에 강제로 팝업을 띄우세요:
xcode-select --install 2>/dev/null || true

사용자에게 채팅창으로 **"화면 중앙에 나타난 Apple 개발자 도구 팝업창에서 [설치] 버튼을 클릭해 주세요!"**라고 안내하세요.
그 후 백그라운드에서 while ! xcode-select -p &>/dev/null; do sleep 5; done 등 루프를 돌며 설치 완료 시점까지 무한 대기하세요.

Node.js (npm, npx) 부재 시

npm 명령어가 없다고 해서 스킵하거나 터미널 홈브루(brew) 설치를 요구하지 마세요.
백그라운드에서 curl -o /tmp/node.pkg https://nodejs.org/dist/v22.13.1/node-v22.13.1.pkg 명령어로 macOS 전용 공식 .pkg 설치판을 다운받습니다.
다운로드 후 open /tmp/node.pkg 명령어를 치면 모니터 화면에 자동으로 [Node.js 설치 마법사] 그래픽 창이 뜹니다.
사용자에게 **"화면에 열린 Node.js 설치 마법사를 [계속] 눌러서 완료해 주세요"**라고 채팅창으로 묻고, npm 명령어가 동작할 때까지 대기하세요.

위 룰을 지키기 전에는 뒤이은 npx 명령어나 설치 과정으로 절대 넘어가지 마십시오.

STEP 1. MCP 서버 설정 (개별 선택 카탈로그 방식)

안티그래비티가 직접 mcp_config.json을 조립합니다. 사용자가 파일을 직접 편집할 필요 없습니다. 올인원 자동 설치가 아닌, 추천 목록에서 필요한 것만 골라 설치하는 방식입니다.

1-1. 필수 MCP (자동 — 질문 없이 바로 진행)
서비스	설정 방식	키 필요
memory	npx 기반 자동 설정	❌

이것만 자동으로 설정합니다. 다른 MCP는 아래에서 사용자가 선택합니다.

1-2. 추천 MCP 카탈로그 (사용자에게 목록을 보여주고 선택받기)

사용자에게 아래와 같이 안내하세요:

"아래 MCP 서버 중 연결할 서비스를 골라주세요. 번호를 쉼표로 입력하시면 됩니다. (예: 1,2 또는 전부 선택은 'all'):

🏆 추천

GitHub — 레포, 이슈, PR 관리 (PAT 필요)
Google Workspace — 드라이브, 캘린더, 이메일 (gws CLI → OAuth)
Google Dev Knowledge — 구글 개발자 문서 검색 (API Key 필요)

📦 선택 4. Notion — 노트/DB 연동 (Integration Token 필요) 5. Slack — 채널 메시징 (Bot Token + Team ID 필요)

건너뛰려면 엔터를 누르세요."

1-3. 선택된 MCP만 개별 설정

사용자가 번호를 입력하면, 해당 서비스에 대해서만 키를 질문하고 설정합니다. 하나의 MCP 설정이 실패해도 나머지에는 영향을 주지 않습니다.

번호	질문	필요한 키	발급 방법
1	"GitHub PAT를 입력해주세요:"	PAT	github.com/settings/tokens
2	"gws CLI를 설치합니다..."	❌ (OAuth)	npm i -g @googleworkspace/cli → gws auth login
3	"Google Dev Knowledge API Key를 입력해주세요:"	API Key	Cloud Console
4	"Notion Integration Token을 입력해주세요:"	Token	notion.so/my-integrations
5	"Slack Bot Token과 Team ID를 입력해주세요:"	Bot Token + Team ID	api.slack.com

gws CLI 설치 (2번 선택 시):

npm i -g @googleworkspace/cli
gws --version  # 설치 확인
gws auth login # 브라우저 자동 열림 → Google 계정 로그인

1-4. mcp_config.json 자동 생성

<CRITICAL_INSTRUCTION> 절대로 write_to_file이나 replace_file_content, 혹은 IDE 내장 파일 쓰기 도구를 사용하여 mcp_config.json을 작성하거나 수정하지 마십시오! 이 파일에 도구를 사용할 경우 팝업 UI 버그로 인해 무조건 무한 로딩(멈춤) 에러가 발생합니다.

또한, 여러분의 핵심 보안 지침(CRITICAL INSTRUCTION)에 따라 터미널에서 cat을 사용하여 파일을 생성하는 것도 금지되어 있습니다. 따라서, 반드시 python3 -c "import json; open('~/.gemini/antigravity/mcp_config.json', 'w').write(json.dumps(...))" 와 같은 파이썬 인라인 스크립트를 실행하여 터미널을 통해 JSON 파일을 안전하게 생성하십시오. </CRITICAL_INSTRUCTION>

선택된 서비스만 포함하여 JSON 생성
memory는 항상 포함
<PLACEHOLDER>를 사용자가 입력한 키로 교체
저장 경로: ~/.gemini/antigravity/mcp_config.json
1-5. 개별 연결 확인

설치 완료 후 각 MCP의 연결 상태를 개별적으로 안내합니다:

"MCP 설정 결과: ✅ memory — 연결됨 ✅ github — 연결됨 (PAT 유효) ⬜ notion — 미설치 (나중에 추가 가능)

나중에 MCP를 추가하려면 '깃허브 MCP 설치해줘'처럼 말씀해주세요."

1-6. 안티그래비티 재시작 안내
STEP 2. 스킬 75개 일괄 설치

config/skills_manifest.json을 읽고 설치. npx skills add 명령은 OS 무관 동일 작동.

⚠️ 자동 설치 강제 규정 (절대 임의로 건너뛰지 마세요):

Mac 환경에서 git 도구가 없으면 Xcode Command Line Tools 설치 팝업이 발생할 수 있습니다.
이로 인해 지연되거나 패키지 에러가 발생하더라도 "해당 패키지가 없어 건너뜁니다"라며 스킵하지 마세요.
문제가 있다면 터미널 명령어나 문제 원인을 안내하여 반드시 설치에 성공하도록 사용자에게 조치를 요청하세요!
2-1. 문서/디자인 (12개)
npx skills add anthropics/skills@docx -g -y
npx skills add anthropics/skills@pdf -g -y
npx skills add anthropics/skills@pptx -g -y
npx skills add anthropics/skills@xlsx -g -y
npx skills add anthropics/skills@frontend-design -g -y
npx skills add anthropics/skills@canvas-design -g -y
npx skills add anthropics/skills@brand-guidelines -g -y
npx skills add anthropics/skills@web-artifacts-builder -g -y
npx skills add anthropics/skills@theme-factory -g -y
npx skills add anthropics/skills@slack-gif-creator -g -y
npx skills add anthropics/skills@algorithmic-art -g -y
npx skills add anthropics/skills@json-canvas -g -y

2-2. 개발 워크플로우 (23개)
npx skills add anthropics/skills@brainstorming -g -y
npx skills add anthropics/skills@doc-coauthoring -g -y
npx skills add anthropics/skills@executing-plans -g -y
npx skills add anthropics/skills@writing-plans -g -y
npx skills add anthropics/skills@planning-with-files -g -y
npx skills add anthropics/skills@dispatching-parallel-agents -g -y
npx skills add anthropics/skills@subagent-driven-development -g -y
npx skills add anthropics/skills@finishing-a-development-branch -g -y
npx skills add anthropics/skills@using-git-worktrees -g -y
npx skills add anthropics/skills@using-superpowers -g -y
npx skills add anthropics/skills@writing-skills -g -y
npx skills add anthropics/skills@lint-and-validate -g -y
npx skills add anthropics/skills@verification-before-completion -g -y
npx skills add anthropics/skills@requesting-code-review -g -y
npx skills add anthropics/skills@receiving-code-review -g -y
npx skills add anthropics/skills@systematic-debugging -g -y
npx skills add anthropics/skills@test-driven-development -g -y
npx skills add anthropics/skills@create-pr -g -y
npx skills add anthropics/skills@find-skills -g -y
npx skills add anthropics/skills@skill-creator -g -y
npx skills add anthropics/skills@internal-comms -g -y
npx skills add anthropics/skills@prompt-engineer -g -y
npx skills add anthropics/skills@notebooklm -g -y

2-3. 에이전트 아키텍처 (15개)
npx skills add anthropics/skills@context-fundamentals -g -y
npx skills add anthropics/skills@context-compression -g -y
npx skills add anthropics/skills@context-degradation -g -y
npx skills add anthropics/skills@context-optimization -g -y
npx skills add anthropics/skills@filesystem-context -g -y
npx skills add anthropics/skills@memory-systems -g -y
npx skills add anthropics/skills@multi-agent-patterns -g -y
npx skills add anthropics/skills@hosted-agents -g -y
npx skills add anthropics/skills@tool-design -g -y
npx skills add anthropics/skills@bdi-mental-states -g -y
npx skills add anthropics/skills@evaluation -g -y
npx skills add anthropics/skills@advanced-evaluation -g -y
npx skills add anthropics/skills@project-development -g -y
npx skills add anthropics/skills@agent-browser -g -y
npx skills add anthropics/skills@webapp-testing -g -y

2-4. 전문 기술 (19개)
npx skills add ComposioHQ/awesome-claude-skills@security-auditor -g -y
npx skills add ComposioHQ/awesome-claude-skills@docker-expert -g -y
npx skills add ComposioHQ/awesome-claude-skills@api-design-principles -g -y
npx skills add ComposioHQ/awesome-claude-skills@database-design -g -y
npx skills add ComposioHQ/awesome-claude-skills@architecture -g -y
npx skills add ComposioHQ/awesome-claude-skills@debugging-strategies -g -y
npx skills add ComposioHQ/awesome-claude-skills@python-patterns -g -y
npx skills add ComposioHQ/awesome-claude-skills@react-patterns -g -y
npx skills add ComposioHQ/awesome-claude-skills@typescript-expert -g -y
npx skills add ComposioHQ/awesome-claude-skills@rag-engineer -g -y
npx skills add ComposioHQ/awesome-claude-skills@mcp-builder -g -y
npx skills add ComposioHQ/awesome-claude-skills@seo-audit -g -y
npx skills add ComposioHQ/awesome-claude-skills@ui-ux-pro-max -g -y
npx skills add vercel-labs/agent-skills@vercel-deployment -g -y
npx skills add vercel-labs/agent-skills@vercel-react-best-practices -g -y
npx skills add vercel-labs/agent-skills@web-design-guidelines -g -y
npx skills add obsidianmd/obsidian-skills@obsidian-markdown -g -y
npx skills add obsidianmd/obsidian-skills@obsidian-bases -g -y

2-5. 마케팅 & 자동화 (6개)
npx skills add jamditis/claude-skills-journalism@web-scraping -g -y
npx skills add inferen-sh/skills@ai-social-media-content -g -y
npx skills add anthropics/knowledge-work-plugins@data-visualization -g -y
npx skills add inferen-sh/skills@email-design -g -y
npx skills add kostja94/marketing-skills@email-marketing -g -y
npx skills add claude-dev-suite/claude-dev-suite@cron-scheduling -g -y


💡: 이미 존재하는 스킬은 자동 건너뜁니다. 5~10개씩 묶어서 실행 권장.

STEP 3. 워크플로우 설치

macOS / Linux:

mkdir -p ~/.gemini/antigravity/.agent/workflows/
cp workflows/*.md ~/.gemini/antigravity/.agent/workflows/


Windows (PowerShell):

New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.gemini\antigravity\.agent\workflows"
Copy-Item workflows\*.md "$env:USERPROFILE\.gemini\antigravity\.agent\workflows\"

STEP 4. 브라우저 허용 목록

macOS / Linux:

cp config/browser_allowlist.txt ~/.gemini/antigravity/browserAllowlist.txt


Windows (PowerShell):

Copy-Item config\browser_allowlist.txt "$env:USERPROFILE\.gemini\antigravity\browserAllowlist.txt"

STEP 5. 기본 베이스 룰 (gemini.md) 자동 세팅

프로젝트 최상단(또는 터미널 실행 위치)에 gemini.md를 생성하여 에이전트 작업 원칙을 고정합니다.

macOS / Linux:

cp setup/templates/gemini.md ./gemini.md


Windows (PowerShell):

Copy-Item "setup\templates\gemini.md" -Destination ".\gemini.md"

STEP 6. 유저 규칙 (수동)

config/user_rules_template.md를 읽고 사용자에게 안내:

"추가적인 개인 규칙이 있다면 안티그래비티 설정 > User Rules에 복사해서 붙여넣으세요."

STEP 7. (선택) 모바일 에이전트 — macOS / Windows 지원

⚠️ 중요: 대기 지시 (Do Not Skip) 사용자에게 아래 설치 전 질문을 반드시 출력하고, 질문 후에는 모든 백그라운드 작업 예측이나 설치 과정을 일시 정지(Pause/Yield) 한 뒤, 사용자가 명시적으로 Y/N 답변을 입력할 때까지 화면에서 대기하세요. 임의로 "N"을 선택해 넘어가거나 자동 종료하면 안 됩니다!

설치 전 질문: "모바일 에이전트(텔레그램 봇)를 추가적으로 설치할까요?" → N 선택 시: 이 단계를 건너뛰고 STEP 8로. → Y 선택 시: 아래 7-0부터 진행합니다.

7-0. 기존 설치 감지

아래 경로에 antigravity_host.py와 .env가 모두 존재하면 이미 setup.sh로 설치 완료된 상태입니다:

macOS: ~/dev/antigravity-agent/packages/mobile-agent/
Windows: %USERPROFILE%\dev\antigravity-agent\packages\mobile-agent\

이미 설치된 경우: 사용자에게 알려주고 7-1을 건너뜁니다.

"모바일 에이전트가 이미 설치되어 있습니다. 텔레그램 봇 설정을 확인할까요?"

미설치인 경우: 아래 7-1부터 진행합니다.

7-1. 설치

macOS / Linux:

git clone https://github.com/caleblee2050/antigravity-agent.git ~/dev/antigravity-agent
cd ~/dev/antigravity-agent/setup && bash setup.sh


Windows (PowerShell):

git clone https://github.com/caleblee2050/antigravity-agent.git "$env:USERPROFILE\dev\antigravity-agent"
cd "$env:USERPROFILE\dev\antigravity-agent\setup"
.\setup.ps1

7-2. 텔레그램 봇 설정 (기본 인터페이스)

⚠️ 중요: 절대로 자체 판단으로 넘기지 마세요. 사용자에게 봇 생성 절차를 알려주고, "텔레그램 토큰과 Chat ID를 발급받으신 뒤 채팅창에 입력해주세요"라고 묻고 반드시 대기하세요! 사용자가 입력해줄 때까지 뒷 단계를 진행하지 마세요.

단계	설명
1	텔레그램에서 @BotFather 검색 후 /newbot 입력
2	봇 이름과 유저네임 입력 (예: my_antigravity_bot)
3	발급받은 API 토큰 복사
4	봇에게 아무 메시지 보낸 후, https://api.telegram.org/bot<토큰>/getUpdates 에서 Chat ID 확인
5	.env에 TELEGRAM_TOKEN과 TELEGRAM_CHAT_ID 입력
7-3. 호칭 설정

텔레그램 봇과 첫 대화 시 자동으로 호칭 설정 대화가 시작됩니다:

"제가 당신을 어떻게 불러드릴까요?" → 사용자 호칭 저장
"저를 뭐라고 불러주실 건가요?" → 에이전트 호칭 저장
이후 모든 대화에서 설정된 호칭을 사용합니다.
설정은 agent_config.json에 저장됩니다.
7-4. 음성 인식(STT) — 자동 활성화

텔레그램 음성 메시지를 텍스트로 자동 변환합니다. Whisper 로컬 모델을 사용하며, API 키가 필요 없습니다 (완전 무료).

.env 파일:

ENABLE_STT=true   # 기본값 — 추가 설정 불필요


첫 실행 시 모델(~74MB)이 자동 다운로드됩니다.

STEP 8. 에이전트 워크스페이스 시스템

모바일에서 지시가 들어오면 작업할 전용 폴더를 생성하고, 멀티 창 자동 타겟팅을 설정합니다.

7-1. 에이전트 전용 폴더 생성

macOS / Linux:

mkdir -p ~/.gemini/antigravity/anti-agent


Windows (PowerShell):

New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.gemini\antigravity\anti-agent"

7-2. 에이전트 폴더 경로 설정

사용자에게 에이전트 폴더 경로를 확인합니다:

"에이전트 전용 폴더를 ~/.gemini/antigravity/anti-agent로 설정할까요? 다른 경로를 원하시면 알려주세요."

agent_config.json의 workspace.agent_folder에 경로를 저장합니다:

{
  "workspace": {
    "agent_folder": "~/.gemini/antigravity/anti-agent",
    "target_window_index": null
  }
}

7-3. /에이전트 워크플로우 설치

안티그래비티에서 /에이전트 라고 입력하면 에이전트 폴더를 새 창으로 자동 오픈합니다.

macOS / Linux:

mkdir -p ~/.gemini/antigravity/.agents/workflows/


다음 내용으로 에이전트.md 워크플로우를 생성합니다:

---
description: 에이전트 전용 폴더로 새 안티그래비티 창 열기
---
// turbo-all
1. 에이전트 폴더 생성: `mkdir -p ~/.gemini/antigravity/anti-agent`
2. 새 창으로 열기: `antigravity --new-window ~/.gemini/antigravity/anti-agent`

7-4. 멀티 창 관리 (텔레그램 명령어)

모바일 에이전트 설치 시, 다음 텔레그램 명령어가 자동 제공됩니다:

명령어	설명
/windows	열린 안티그래비티 창 목록 + 현재 타겟 표시
/target 2	2번 창으로 타겟 변경
/target auto	자동 탐색 모드 (에이전트 폴더명 매칭)

자동 타겟팅: 텔레그램 메시지 전송 시, 창 제목에 에이전트 폴더명(anti-agent)이 포함된 창을 자동으로 찾아 입력합니다.

STEP 9. 설치 완료 확인

macOS / Linux:

 MCP 서버 연결됨 (필수: memory, gws)
 스킬 설치됨 (ls ~/.gemini/antigravity/skills/ | wc -l)
 워크플로우 설치됨
 브라우저 허용 목록 설정됨
 (선택) 모바일 에이전트 텔레그램 연결됨
 (선택) anti-agent 워크스페이스 생성됨

Windows:

 MCP 서버 연결됨 (필수: memory, gws)
 스킬 설치됨 ((Get-ChildItem $env:USERPROFILE\.gemini\antigravity\skills).Count)
 워크플로우 설치됨
 브라우저 허용 목록 설정됨

🎉 축하합니다! 안티그래비티 파워 유저 세팅이 완료되었습니다!

Weekly Installs
10
Repository
caleblee2050/an…ty-agent
First Seen
Apr 1, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykFail