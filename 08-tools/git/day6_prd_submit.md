---
rating: ⭐⭐⭐
title: day6-prd-submit
url: https://skills.sh/ai-native-camp/camp-1/day6-prd-submit
---

# day6-prd-submit

skills/ai-native-camp/camp-1/day6-prd-submit
day6-prd-submit
Installation
$ npx skills add https://github.com/ai-native-camp/camp-1 --skill day6-prd-submit
Summary

Template-based PRD authoring, format validation, and GitHub PR submission guidance for Day 6.

Guides participants through environment checks (git, gh CLI, repo access), GitHub ID confirmation, and PRD creation or validation in under 15 minutes
Provides a structured PRD template covering problem definition, skills inventory, and change history; validates eight required sections before submission
Automates git workflow (branch creation, commit, push) and opens a GitHub PR with a single confirmation, handling common errors like missing tools or insufficient permissions
Supports both new PRD authoring with AI-assisted drafting and validation of existing documents; scans local skills directory to populate project examples
SKILL.md
Day 6: PRD 작성 & PR 제출

PRD(Product Requirements Document) 초안을 템플릿 기반으로 작성하고, 필수 형식을 검증한 뒤, GitHub PR 제출 과정을 안내한다.

용어 정리

이 스킬에서 사용하는 핵심 용어:

용어	설명
PRD	Product Requirements Document. "이 프로젝트가 뭘 해결하고, 뭘 만드는지" 정리한 문서
GitHub	코드와 문서를 함께 관리하고 공유하는 온라인 서비스. Google Docs의 코드 버전
GitHub ID	GitHub 사이트에서 나를 식별하는 이름. 프로필 URL의 마지막 부분 (github.com/여기)
Repository (Repo)	프로젝트 파일이 모여있는 폴더. Google Drive의 공유 폴더와 비슷
브랜치(Branch)	원본을 건드리지 않고 내 작업 공간을 따로 만드는 것. "사본으로 저장"과 비슷
커밋(Commit)	변경사항을 저장하는 것. Ctrl+S의 Git 버전
Push	내 컴퓨터에 저장한 것을 온라인(GitHub)에 올리는 것
PR (Pull Request)	"내 작업을 확인해주세요"라고 운영진에게 보내는 검토 요청. 제출 버튼과 같다
gh CLI	터미널에서 GitHub을 조작할 수 있는 도구
사전 요구사항

이 스킬은 아래 환경이 갖춰져 있다고 가정한다. Step 0에서 자동 확인한다.

git이 설치되어 있어야 한다
gh CLI가 설치되고 인증되어 있어야 한다
대상 repo가 clone 되어 있어야 한다
repo에 push 권한(collaborator)이 있어야 한다
소요 시간 가이드
Step	주제	예상 시간
0	환경 체크	~1분
1	GitHub ID 확인	~1분
2	PRD 작성 + 검증	~10분
3	제출 (git + PR)	~3분
합계		~15분

환경이 세팅되어 있으면 15분 내 완료 가능. 환경 문제 발생 시 +5~10분.

PRD 템플릿
# [프로젝트 제목]

## 문제
> 한 줄: 누구의, 어떤 불편을, 어떻게 해결하는가

- **현재 상태**: (구체적 수치 — 몇 건, 몇 분, 몇 명)
- **원하는 상태**: (1주 후 돌아가고 있을 모습)
- **성공 기준**: (숫자로 판단 가능한 것 1~2개)

## 스킬
| # | 스킬명 | 한 줄 설명 | 상태 |
|---|--------|-----------|------|
| 1 | `/my-skill-1` | 입력 → 출력 | ✅ 동작 / 🔨 진행중 |
| 2 | `/my-skill-2` | 입력 → 출력 | ✅ 동작 / 🔨 진행중 |

## 변화 기록
- **Day 1**: "처음 정의" →
- **Day 6**: "지금 정의" →
- **가장 크게 달라진 점**:

실행 흐름
Step 0           Step 1           Step 2          Step 3
환경 체크 →  GitHub ID 확인 → PRD 작성/검증 → 제출 (git + PR)

Step 0: 환경 사전 체크

스킬 시작 시 진행 전에 아래를 자동으로 확인한다:

git --version
gh --version
gh auth status
git remote -v


결과를 참가자에게 보여준다:

=== 환경 체크 ===
✅ git: 설치됨
✅ gh CLI: 설치됨
✅ GitHub 로그인: 완료 (사용자: {detected-id})
✅ 프로젝트 폴더: 연결됨 ({repo-url})

환경 준비가 완료되었습니다!


하나라도 실패하면 해당 항목의 해결 방법을 안내하고, 해결 후 다시 체크한다. 모든 항목이 통과할 때까지 다음 Step으로 진행하지 않는다.

실패 항목	안내
git 미설치	"git이 설치되어있지 않습니다. 운영진에게 도움을 요청해주세요."
gh CLI 미설치	"brew install gh를 터미널에 입력해주세요." (macOS 기준). 실패 시 운영진 호출
gh 미인증	"gh auth login을 입력하고 나오는 안내를 따라주세요. GitHub 계정으로 로그인하면 됩니다."
repo 연결 안 됨	"프로젝트를 아직 내 컴퓨터에 다운로드하지 않았어요. 터미널에서 아래를 입력해주세요: gh repo clone {owner/repo}"
Step 1: GitHub ID 확인

Step 0에서 gh auth status로 감지된 GitHub ID를 보여주고 확인만 받는다:

AskUserQuestion: "GitHub 사용자명이 '{detected-id}'가 맞나요?"
- 네, 맞습니다
- 아니요, 다른 ID입니다 (직접 입력)


ID 형식 검증: 입력된 ID가 영문, 숫자, 하이픈(-)만 포함하는지 확인한다. 특수문자, 공백, 슬래시 등이 포함되면 안내 후 다시 입력받는다.

입력된 ID는 소문자로 정규화한다.

이 ID는 이후 파일 경로와 브랜치명에 사용된다:

파일: {github-id}/PRD.md
브랜치: prd/{github-id}
Step 2: PRD 작성 또는 검증

AskUserQuestion으로 현재 상태를 묻는다:

선택지	동작
PRD 새로 작성하기	Step 2-A: 템플릿 기반 작성 가이드
이미 작성한 PRD 검증하기	Step 2-B: 기존 파일 검증
Step 2-A: PRD 작성 가이드
위 PRD 템플릿을 보여준다
AskUserQuestion으로 프로젝트 주제를 묻는다:
"어떤 프로젝트의 PRD를 작성할까요?"
- 캠프에서 만든 스킬 기반 (이번 주에 만든 스킬을 프로젝트로 발전)
- 업무 자동화 아이디어 (실제 업무에서 자동화하고 싶은 것)
- 직접 입력


"캠프에서 만든 스킬 기반"을 선택하면, .claude/skills/ 디렉토리를 스캔하여 참가자가 만든 스킬 목록을 보여주고 선택하게 한다.

참가자의 답변을 바탕으로 PRD 초안을 생성한다

초안을 터미널에 출력하고 AskUserQuestion:

선택지	동작
이대로 진행	{github-id}/PRD.md에 저장 후 Step 2-B로
수정하고 싶어요	어떤 부분을 수정할지 묻고 (문제 정의 / 스킬 목록 / 변화 기록) 반영 후 다시 출력
중요: PRD 내용은 참가자의 실제 경험과 프로젝트를 반영해야 한다. 일반적인 예시가 아닌 캠프에서 만든 스킬, 실제 업무 문제를 담도록 유도한다.
Step 2-B: PRD 형식 검증

{github-id}/PRD.md 파일을 읽고 아래 체크리스트로 검증한다.

검증 체크리스트
#	항목	검증 방법	필수
1	프로젝트 제목	#으로 시작하는 첫 번째 줄 (큰 제목)이 존재하는가	필수
2	문제 섹션	## 문제 헤딩이 존재하는가	필수
3	현재 상태	현재 상태 텍스트가 존재하고 10자 이상인가	필수
4	원하는 상태	원하는 상태 텍스트가 존재하고 10자 이상인가	필수
5	성공 기준	성공 기준 텍스트가 존재하고 10자 이상인가	필수
6	스킬 섹션	## 스킬 헤딩이 존재하는가	필수
7	스킬 2개 이상	스킬 테이블에서 `	1
8	변화 기록	## 변화 기록 헤딩이 존재하는가	필수
검증 결과 출력
=== PRD 형식 검증 결과 ===

[PASS] 또는 [보완 필요]

✅ 프로젝트 제목: 있음
✅ 문제 섹션: 있음
✅ 현재 상태: 있음
✅ 원하는 상태: 있음
✅ 성공 기준: 있음
✅ 스킬 섹션: 있음
✅ 스킬 2개 이상: 있음 (N개)
✅ 변화 기록: 있음

결과: 8/8 통과 → PASS


보완 필요인 경우 누락된 항목을 구체적으로 안내한다:

❌ 성공 기준: 내용이 너무 짧습니다. 구체적인 숫자를 포함해주세요.
   예) "주 3회 사용, 건당 처리 시간 30분 → 5분"

Step 3: 제출 (git + PR)

검증 PASS 후, AskUserQuestion:

"PRD 검증을 통과했습니다! GitHub에 제출할까요?"
- 네, 제출해주세요 (권장)
- 나중에 할게요


"나중에 할게요" 선택 시: "준비되면 다시 이 스킬을 실행해주세요." 안내 후 종료.

"네, 제출해주세요" 선택 시 아래를 실행한다. 각 단계마다 한글 진행 상태를 출력한다:

[1/5] 최신 상태로 동기화하는 중...

git checkout main && git pull origin main

[2/5] 제출용 공간을 만드는 중...

git checkout -b prd/{github-id}


브랜치가 이미 존재하면 git checkout prd/{github-id}로 전환한다.

[3/5] PRD 파일을 등록하는 중...

git add {github-id}/PRD.md


git status로 스테이징된 파일이 {github-id}/PRD.md 1개뿐인지 확인한다. 다른 파일이 포함되면 해당 파일을 unstage한다.

[4/5] 저장하는 중...

git commit -m "feat: {github-id} PRD 초안 제출"

[5/5] GitHub에 올리는 중...

git push origin prd/{github-id}


push 완료 후, gh CLI로 PR을 생성한다:

gh pr create --repo {owner/repo} --title "PRD: {github-id}" --body "$(cat <<'EOF'
## PRD 초안 제출

- 작성자: {github-id}
- 파일: {github-id}/PRD.md

검증 결과: PASS (8/8)
EOF
)"


PR URL을 출력하고 완료를 안내한다.

완료 리포트
=== Day 6 PRD 제출 완료 ===
GitHub ID: {github-id}
파일: {github-id}/PRD.md
브랜치: prd/{github-id}
검증: PASS (8/8)
PR: {PR URL}

축하합니다! GitHub에 첫 PR을 올렸습니다.
운영진이 확인 후 승인할 예정입니다.

에러 처리
상황	대응
git 미설치	"git이 설치되어있지 않습니다. 운영진에게 도움을 요청해주세요."
gh CLI 미설치	"brew install gh를 입력해주세요." 실패 시 운영진 호출 안내
gh 미인증	"gh auth login을 입력하고 GitHub 계정으로 로그인해주세요."
PRD.md 파일 없음	"PRD 파일이 아직 없어요. 먼저 작성할까요?"
검증 보완 필요	누락 항목 + 구체적 예시 안내 + 수정 도움
git 브랜치 이미 존재	기존 브랜치로 자동 전환
push 실패 (인증)	"GitHub 로그인이 필요합니다. gh auth login을 실행해주세요."
push 실패 (권한)	"이 프로젝트에 제출 권한이 없어요. Slack에서 운영진(@zoon)에게 '권한이 필요합니다'라고 메시지를 보내주세요."
repo clone 안 됨	"프로젝트를 먼저 다운로드해야 해요. 터미널에 gh repo clone {owner/repo}를 입력해주세요."
GitHub ID 형식 오류	"GitHub ID에는 영문, 숫자, 하이픈(-)만 사용할 수 있어요."
출력 위치
경로	내용
{github-id}/PRD.md	참가자 PRD 문서
Weekly Installs
1.2K
Repository
ai-native-camp/camp-1
GitHub Stars
234
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass