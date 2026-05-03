---
rating: ⭐⭐
title: react-vite-scaffold
url: https://skills.sh/parkyoungwoong/skills/react-vite-scaffold
---

# react-vite-scaffold

skills/parkyoungwoong/skills/react-vite-scaffold
react-vite-scaffold
Installation
$ npx skills add https://github.com/parkyoungwoong/skills --skill react-vite-scaffold
SKILL.md
Vite React Project Scaffold

참고: https://www.heropy.dev/p/6iFzkB

Vite 기반 React(CSR) 프로젝트를 스캐폴딩하거나, 기존 프로젝트의 누락된 설정을 자동 보완하는 스킬.

필수 실행 체크리스트 (MANDATORY)

스킬 시작 즉시, 아래 항목을 TodoWrite에 1:1로 등록한 뒤 순서대로 진행한다. 건너뛰기 금지.

프로젝트 상태 감지 (1단계)
모드 결정: 스캐폴딩 vs 보완 (2단계)
프로젝트 생성 [스캐폴딩 모드일 때만] (3단계)
Tailwind CSS 설치 및 구성 [tailwindcss 미설치 시] (4단계)
경로 별칭 구성 [vite.config/tsconfig에 alias 미설정 시] (5단계)
ESLint + Prettier 구성 [.prettierrc 또는 prettier 패키지 미설치 시] (6단계)
.prettierrc 생성 [파일 없을 때] (7단계)
.vscode/settings.json 생성 [파일 없을 때] (8단계)
TanStack Query 설치 및 통합 [@tanstack/react-query 미설치 시] (9단계)
React Router 설치 및 라우팅 구성 [react-router 미설치 시] (10단계)
Zustand 설치 및 예제 store 생성 [zustand 미설치 시] (11단계)
최종 검증 — 1단계 감지 표를 다시 돌며 모든 구성이 충족됐는지 확인, 누락 시 해당 단계 재실행 (12단계)

각 항목은 조건 충족 시 "skipped"로 완료 처리하되, 조건 판단 근거(파일/패키지 존재 여부)를 명시한 뒤 넘어간다.

동작 흐름
1단계: 프로젝트 상태 감지

다음 파일들을 확인하여 현재 프로젝트 상태를 판별한다:

확인 대상	감지 방법
빈 디렉토리 여부	현재 디렉토리에 파일이 없거나 package.json이 없음
Vite 프로젝트	vite.config.ts 또는 vite.config.js 존재
TypeScript	tsconfig.json 또는 tsconfig.app.json 존재
TanStack Query	package.json의 dependencies에 @tanstack/react-query 존재
React Router	package.json의 dependencies에 react-router 존재
Zustand	package.json의 dependencies에 zustand 존재
Tailwind CSS	package.json의 dependencies/devDependencies에 tailwindcss 존재
ESLint 구성	eslint.config.js 또는 eslint.config.mjs 존재
Prettier 구성	.prettierrc 존재
VSCode 설정	.vscode/settings.json 존재
패키지 매니저	pnpm-lock.yaml → pnpm, yarn.lock → yarn, bun.lockb/bun.lock → bun, package-lock.json 또는 없음 → npm
2단계: 분기 처리

빈 디렉토리인 경우 (스캐폴딩 모드):

프로젝트 생성 명령 실행
아래 설정 전부 자동 적용

기존 Vite 프로젝트인 경우 (보완 모드):

위 감지 기준으로 설치 상태 자동 판별
누락된 설정만 식별하여 자동 생성
이미 존재하는 설정 파일은 건드리지 않음
3단계: 프로젝트 생성

현재 디렉토리에 Vite 프로젝트 생성:

{pm} create vite@latest .


{pm}은 패키지 매니저 감지 규칙에 따라 결정된 패키지 매니저로 대체한다. (npm, pnpm, yarn, bun)

대화형 선택지:

Current directory is not empty. Please choose how to proceed: Ignore files and continue (디렉토리에 .claude/ 등 스킬 관련 파일이 있는 경우 표시됨)
Select a framework: React
Select a variant: TypeScript + React Compiler
Use rolldown-vite (Experimental)?: No
Install with npm and start now? Yes

요구사항: Node.js 18+, NPM 8+

4단계: Tailwind CSS 설치 [조건: tailwindcss 미설치 시]
{pm} install -D tailwindcss @tailwindcss/vite


vite.config.ts에 Tailwind 플러그인 추가:

import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [
    react(),
    tailwindcss()
  ],
  resolve: {
    alias: [
      { find: '@', replacement: '/src' }
    ]
  }
})


src/index.css 파일 상단에 추가:

@import 'tailwindcss';

5단계: 경로 별칭 구성 [조건: vite.config 또는 tsconfig에 @ alias 미설정 시]

vite.config.ts의 resolve.alias 설정 (위 코드에 포함됨):

resolve: {
  alias: [
    { find: '@', replacement: '/src' }
  ]
}


tsconfig.app.json에 경로 별칭 추가:

{
  "compilerOptions": {
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}


TypeScript v5 이하(tsc --version으로 확인)인 경우, "baseUrl": "." 을 paths 위에 추가한다.

6단계: ESLint + Prettier 구성 [조건: prettier 패키지 또는 eslint-plugin-prettier 미설치 시]

ESLint 관련 패키지는 Vite 프로젝트 생성 시 이미 포함되어 있음. Prettier 관련 패키지를 추가 설치:

{pm} install -D prettier eslint-config-prettier eslint-plugin-prettier prettier-plugin-tailwindcss


eslint.config.js에 Prettier 통합 추가:

import prettierRecommended from 'eslint-plugin-prettier/recommended'

export default defineConfig([
  {
    extends: [
      prettierRecommended
    ]
  }
])


TanStack Query가 포함된 경우, 같은 extends 배열에 추가:

import prettierRecommended from 'eslint-plugin-prettier/recommended'
import tanstackQuery from '@tanstack/eslint-plugin-query'

export default defineConfig([
  {
    extends: [
      prettierRecommended,
      tanstackQuery.configs.recommended
    ]
  }
])

패키지 역할 참고
패키지	설명
eslint	ESLint 코어 패키지 (Vite에 포함)
prettier	Prettier 코어 패키지
eslint-plugin-react	React 문법 분석 및 검사 (Vite에 포함)
eslint-config-prettier	ESLint와 Prettier의 충돌 방지
eslint-plugin-prettier	Prettier 규칙을 ESLint 규칙으로 통합
eslint-plugin-react-hooks	React Hooks 규칙 강제 (Vite에 포함)
eslint-plugin-react-refresh	React Refresh 규칙 (Vite에 포함)
prettier-plugin-tailwindcss	Tailwind CSS 클래스 자동 정렬
@tanstack/eslint-plugin-query	TanStack Query 규칙 (TanStack Query 사용 시)
7단계: .prettierrc [조건: 파일 없을 때]

.prettierrc 파일이 없으면 프로젝트 루트에 생성:

{
  "semi": false,
  "singleQuote": true,
  "singleAttributePerLine": true,
  "bracketSameLine": true,
  "endOfLine": "auto",
  "trailingComma": "none",
  "arrowParens": "avoid",
  "plugins": ["prettier-plugin-tailwindcss"]
}

8단계: .vscode/settings.json [조건: 파일 없을 때]

.vscode/settings.json 파일이 없으면 생성:

{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode"
}

9단계: TanStack Query [조건: @tanstack/react-query 미설치 시]

@tanstack/react-query가 package.json에 없으면:

패키지 설치:

{pm} install @tanstack/react-query
{pm} install -D @tanstack/eslint-plugin-query


ESLint Flat Config(eslint.config.js)에 TanStack Query 플러그인 추가 (6단계 참조)

src/App.tsx에서 QueryClientProvider 래핑:

import { QueryClient, QueryClientProvider } from '@tanstack/react-query'

const queryClient = new QueryClient()

export default function App() {
  return (
    <QueryClientProvider client={queryClient}>
      {/* 기존 컴포넌트 */}
    </QueryClientProvider>
  )
}

10단계: React Router [조건: react-router 미설치 시]

참고: https://www.heropy.dev/p/9tesDt

react-router가 package.json에 없으면:

패키지 설치:

{pm} install react-router


src/routes/index.tsx 생성:

import { createBrowserRouter, RouterProvider } from 'react-router'
import Home from './pages/Home'
import About from './pages/About'

const router = createBrowserRouter([
  {
    path: '/',
    element: <Home />
  },
  {
    path: '/about',
    element: <About />
  }
])

export default function Router() {
  return <RouterProvider router={router} />
}


src/routes/pages/Home.tsx 생성:

export default function Home() {
  return <h1>Home</h1>
}


src/routes/pages/About.tsx 생성:

export default function About() {
  return <h1>About</h1>
}


src/main.tsx에서 Router를 사용하도록 수정:

import { createRoot } from 'react-dom/client'
import Router from './routes'

createRoot(document.getElementById('root')!).render(<Router />)


더 이상 사용하지 않는 기본 파일을 제거:

src/App.tsx 또는 src/App.jsx
src/App.css
11단계: Zustand [조건: zustand 미설치 시]

참고: https://www.heropy.dev/p/n74Tgc

zustand가 package.json에 없으면:

패키지 설치:

{pm} install zustand


src/store/example.ts 생성:

import { create } from 'zustand'

interface ExampleStore {
  count: number
  increase: () => void
  decrease: () => void
}

export const useExampleStore = create<ExampleStore>(set => ({
  count: 0,
  increase: () => set(state => ({ count: state.count + 1 })),
  decrease: () => set(state => ({ count: state.count - 1 }))
}))

12단계: 최종 검증 (MANDATORY)

모든 단계 수행 후, 1단계의 감지 표를 다시 한 번 스캔하여 아래 항목을 확인한다:

 tailwindcss, @tailwindcss/vite 설치됨 + vite.config.ts에 플러그인 등록됨 + src/index.css에 @import 'tailwindcss' 존재
 vite.config.ts와 tsconfig.app.json 모두에 @ 경로 별칭 존재
 prettier, eslint-config-prettier, eslint-plugin-prettier, prettier-plugin-tailwindcss 설치됨
 eslint.config.js에 prettierRecommended 포함됨 (TanStack Query 사용 시 tanstackQuery.configs.recommended도 포함)
 .prettierrc 존재
 .vscode/settings.json 존재
 TanStack Query 사용 시: QueryClientProvider가 앱 루트를 감싸고 있음
 React Router 사용 시: src/routes/index.tsx 및 pages 디렉토리, src/main.tsx가 Router 렌더링, 기본 App.tsx/App.css 제거됨
 Zustand 사용 시: src/store/example.ts 존재

누락 항목이 있으면 해당 단계로 돌아가 즉시 보완한다. 검증 통과 전에는 작업 종료 금지.

주의사항
이미 존재하는 설정 파일은 덮어쓰지 않는다
기존 프로젝트 보완 모드에서는 질문 없이 자동으로 진행한다
패키지 매니저는 기존 프로젝트의 lock 파일로 판별한다:
pnpm-lock.yaml → pnpm
yarn.lock → yarn
bun.lockb 또는 bun.lock → bun
package-lock.json 또는 lock 파일 없음 → npm
빈 디렉토리(스캐폴딩 모드)에서는 npm을 사용한다
Weekly Installs
58
Repository
parkyoungwoong/skills
GitHub Stars
1
First Seen
Apr 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass