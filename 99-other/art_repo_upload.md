---
title: art-repo-upload
url: https://skills.sh/cmkim/mj-download-test/art-repo-upload
---

# art-repo-upload

skills/cmkim/mj-download-test/art-repo-upload
art-repo-upload
Installation
$ npx skills add https://github.com/cmkim/mj-download-test --skill art-repo-upload
SKILL.md
개요

로컬 디렉토리에 저장된 파일을 아트 저장소(구글 드라이브)의 지정된 디렉토리에 업로드하는 스킬이다.

사전 조건
Google API 패키지가 설치되어 있지 않으면: art-repo-package-install을 먼저 실행하라고 안내 후 중단.
서비스 계정 키 파일(ace-art-repo-secret.json)이 프로젝트 루트에 존재해야 한다.
Windows PowerShell UTF-8 설정
PowerShell에서 스킬을 실행할 때 UTF-8 인코딩을 강제한다.
프로필에 아래 설정을 넣거나, 실행 스크립트에서 먼저 적용한다. (NoProfile 옵션은 사용하지 않는다)
chcp 65001 > $null
[Console]::InputEncoding  = [System.Text.UTF8Encoding]::new($false)
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$OutputEncoding           = [System.Text.UTF8Encoding]::new($false)
$PSDefaultParameterValues['*:Encoding'] = 'utf8'

인자
$0 — 로컬 백업 디렉토리명 (downloads/ 아래 하위 디렉토리, 예: midj)
$1 — 구글 드라이브 대상 폴더명 (예: midj)

두 인자 모두 필수이다. 인자가 누락된 경우 아래 기본값 매핑을 참고하여 자동으로 추론한다. 추론할 수 없는 경우에만 사용자에게 물어본다.

기본값 매핑
키워드 (사용자 요청에 포함된 단어)	local_dir	drive_dir
미드저니, midjourney, midj, mj	midj	midj
나노바나나, nanobanana, nanob, nb	nanob	nanob
실행 방법

스킬 디렉토리의 upload.ts를 직접 호출한다:

pnpm exec tsx .agents/skills/art-repo-upload/upload.ts "$0" "$1"
# 샌드박스 환경(codex 인터랙티브)에서 IPC 소켓 오류 발생 시:
node --import tsx/esm .agents/skills/art-repo-upload/upload.ts "$0" "$1"


또는 npm 스크립트 사용:

npm run art-repo-upload

동작 상세
로컬 디렉토리(downloads/{local_dir})에서 오늘 날짜(yyyymmdd)가 포함된 zip 파일을 찾는다
구글 드라이브에 {drive_dir}/yyyy/mm/dd 폴더를 생성한다 (이미 존재하면 재사용)
zip을 임시 디렉토리에 압축 해제한다
구글 드라이브 대상 폴더에 이미 같은 이름의 파일이 있으면 건너뛴다
새 파일만 업로드한다
결과 보고

각 단계의 콘솔 출력을 확인하여 사용자에게 전달한다.

업로드 완료: {파일명} → 업로드된 파일 이름을 알린다.
건너뜀 (이미 존재): {파일명} → 중복 파일은 건너뛰었음을 알린다.
{drive_dir} 백업 업로드 완료! → 전체 업로드 성공을 알린다.
오늘 날짜(...) 가 포함된 zip 파일이 없습니다 → 업로드할 파일이 없음을 전달한다. 먼저 다운로드 스킬을 실행했는지 확인하도록 안내한다.
인증 오류 발생 시 → 서비스 계정 키 파일 존재 여부를 확인하도록 안내한다.
사용 예시
/art-repo-upload midj midj
/art-repo-upload nanob nanob

Weekly Installs
10
Repository
cmkim/mj-download-test
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass