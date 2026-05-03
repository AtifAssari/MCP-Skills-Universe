---
title: bun
url: https://skills.sh/dalestudy/skills/bun
---

# bun

skills/dalestudy/skills/bun
bun
Installation
$ npx skills add https://github.com/dalestudy/skills --skill bun
SKILL.md
Bun

Node.js 대신 Bun을 기본 런타임으로 사용.

설치
# macOS / Linux
brew install oven-sh/bun/bun

# npm
npm install -g bun

명령어 매핑
Node.js / npm	Bun
npm install	bun install
npm install <pkg>	bun add <pkg>
npm install -D <pkg>	bun add -d <pkg>
npm uninstall <pkg>	bun remove <pkg>
npm run <script>	bun run <script> 또는 bun <script>
npx <cmd>	bunx <cmd>
node <file>	bun <file>
npm init	bun init
npm create <template>	bun create <template>
프로젝트 초기화
# 새 프로젝트
bun init

# 템플릿 사용
bun create next-app my-app
bun create vite my-app

패키지 관리
# 설치 (bun.lockb 생성)
bun install

# 의존성 추가
bun add express zod
bun add -d typescript @types/node  # devDependencies

# 삭제
bun remove lodash


lockfile: bun.lockb (바이너리). .gitignore에 추가하지 않음.

스크립트 실행
# package.json scripts
bun run dev
bun run build

# 파일 직접 실행 (TypeScript 지원)
bun index.ts
bun src/server.ts

# 단축 (run 생략 가능)
bun dev

주의 사항
1. 패키지 설치 전 이름 확인
# ❌ 오타 또는 유사 패키지 - 타이포스쿼팅 위험
bun add expres
bun add lodassh

# ✅ 정확한 패키지명 확인 후 설치
bun add express
bun add lodash


bun add 실행 전 패키지명이 정확한지 확인. npm 레지스트리에 유사한 이름의 악성 패키지가 등록될 수 있음.

2. 신뢰할 수 없는 스크립트 실행 금지
# ❌ 출처 불명의 스크립트 직접 실행
bun run https://example.com/script.ts
curl -fsSL https://example.com/install.sh | bash

# ✅ 로컬 프로젝트 내 스크립트만 실행
bun run src/index.ts
bun run dev


원격 스크립트나 검증되지 않은 파일은 직접 실행하지 않음.

GitHub Actions
- uses: oven-sh/setup-bun@v{N} # 최신 버전 확인: gh api repos/oven-sh/setup-bun/releases/latest --jq '.tag_name'
- run: bun install
- run: bun test

Weekly Installs
345
Repository
dalestudy/skills
GitHub Stars
4
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn