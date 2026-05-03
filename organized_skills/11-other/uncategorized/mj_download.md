---
rating: ⭐⭐⭐
title: mj-download
url: https://skills.sh/cmkim/mj-download-test/mj-download
---

# mj-download

skills/cmkim/mj-download-test/mj-download
mj-download
Installation
$ npx skills add https://github.com/cmkim/mj-download-test --skill mj-download
SKILL.md
미드저니 작업물 다운로드
사전 조건
Playwright가 설치되어 있지 않으면: art-repo-package-install을 먼저 실행하라고 안내 후 중단.
Windows PowerShell UTF-8 설정
PowerShell에서 스킬을 실행할 때 UTF-8 인코딩을 강제한다.
프로필에 아래 설정을 넣거나, 실행 스크립트에서 먼저 적용한다. (NoProfile 옵션은 사용하지 않는다)
chcp 65001 > $null
[Console]::InputEncoding  = [System.Text.UTF8Encoding]::new($false)
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$OutputEncoding           = [System.Text.UTF8Encoding]::new($false)
$PSDefaultParameterValues['*:Encoding'] = 'utf8'

스크립트
스크립트	위치	역할
check-login.ts	.agents/skills/mj-login/	세션 JSON의 인증 쿠키 유효성 확인
login.ts	.agents/skills/mj-login/	브라우저를 열어 수동 로그인, 세션을 JSON으로 저장
download.ts	.agents/skills/mj-download/	세션 JSON으로 인증하여 오늘 이미지를 zip으로 다운로드
실행 흐름
1단계: 로그인 확인
import { checkLogin } from '../mj-login/check-login.js';

const result = checkLogin("mj_account");
// true: 로그인 정보 존재 → 3단계로 진행
// false: 로그인 정보 없음 → 2단계로 진행


또는 CLI 실행:

pnpm exec tsx .agents/skills/mj-login/check-login.ts ace
# 샌드박스 환경(codex 인터랙티브)에서 IPC 소켓 오류 발생 시:
node --import tsx/esm .agents/skills/mj-login/check-login.ts ace

2단계: 로그인 (1단계에서 false일 때만)
import { login } from '../mj-login/login.js';

const result = await login("mj_account");
// 브라우저가 열린다. 사용자에게 디스코드 계정으로 로그인하라고 안내한다.
// 로그인 완료 시 (/explore 페이지 이동 감지, 최대 2분) 세션이 sessions/mj_{account_name}.json에 저장된다.
// true: 로그인 성공 → 3단계로 진행
// false: 로그인 실패 → 사용자에게 실패를 알리고 중단한다 (3단계 진행하지 않음)


또는 CLI 실행:

pnpm exec tsx .agents/skills/mj-login/login.ts ace
# 샌드박스 환경(codex 인터랙티브)에서 IPC 소켓 오류 발생 시:
node --import tsx/esm .agents/skills/mj-login/login.ts ace

3단계: 다운로드
import { download } from './download.js';

const result = await download("mj_account", "./downloads/midj");
// download_dir 기본값: ./downloads/midj
// true: 다운로드 성공
// false: 다운로드 실패 (세션 파일 없음, 오늘 이미지 없음, 시간 초과 등)


또는 CLI 실행:

pnpm exec tsx .agents/skills/mj-download/download.ts ace
# 샌드박스 환경(codex 인터랙티브)에서 IPC 소켓 오류 발생 시:
node --import tsx/esm .agents/skills/mj-download/download.ts ace

파라미터 (공통)
account_name (string, 필수): 미드저니 계정명. 세션은 sessions/mj_{account_name}.json에 저장된다.
download_dir (string, 선택, download만 해당): 다운로드 파일 저장 디렉토리. 기본값 ./downloads/midj.
결과 보고

각 단계의 콘솔 출력을 확인하여 사용자에게 전달한다.

다운로드 완료: {경로} → 저장된 파일 경로와 파일 크기를 알린다.
파일 크기가 0이면 다운로드 실패로 간주하고 사용자에게 알린다.
오늘 생성한 이미지가 없습니다 → 해당 내용을 전달한다.
[오류] → 에러 메시지를 전달하고 원인을 분석한다.
Weekly Installs
11
Repository
cmkim/mj-download-test
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn