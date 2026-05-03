---
rating: ⭐⭐⭐
title: commit-push-pr
url: https://skills.sh/jh941213/my-claude-code-asset/commit-push-pr
---

# commit-push-pr

skills/jh941213/my-claude-code-asset/commit-push-pr
commit-push-pr
Installation
$ npx skills add https://github.com/jh941213/my-claude-code-asset --skill commit-push-pr
SKILL.md
커밋, 푸시, PR 생성

현재 변경사항을 커밋하고 푸시한 후 PR을 생성합니다.

Step 1: 사전 검증
# 현재 브랜치 확인 — main/master면 STOP
BRANCH=$(git branch --show-current)
if [ "$BRANCH" = "main" ] || [ "$BRANCH" = "master" ]; then
  echo "BLOCKED: main/master 브랜치에서 직접 커밋 금지"
  exit 1
fi

# 상태 확인
git status
git diff --stat
git log --oneline -5

Step 2: 위험 파일 확인
# 민감한 파일이 staged 되었는지 검사
git diff --cached --name-only | grep -E '\.(env|pem|key|credentials)' && echo "WARNING: 민감 파일 포함!"

Step 3: 커밋
# 변경 파일 선택적 staging (git add -A 지양)
git add [specific-files]

# 커밋 메시지 작성
git commit -m "$(cat <<'EOF'
[타입] 제목 (50자 이내)

본문 (선택 — 무엇이 아닌 왜를 설명)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"


타입: feat, fix, docs, style, refactor, test, chore

Step 4: 푸시
# 원격 브랜치 설정 + 푸시
git push -u origin $(git branch --show-current)

Step 5: PR 생성
gh pr create --title "[타입] 제목" --body "$(cat <<'EOF'
## 요약
- 변경 내용 1
- 변경 내용 2

## 테스트
- [ ] typecheck 통과
- [ ] lint 통과
- [ ] test 통과
EOF
)"

출력

완료 시 PR URL을 반환합니다.

Weekly Installs
14
Repository
jh941213/my-cla…de-asset
GitHub Stars
117
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass