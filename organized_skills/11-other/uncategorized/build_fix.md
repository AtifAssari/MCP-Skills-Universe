---
rating: ⭐⭐
title: build-fix
url: https://skills.sh/jh941213/my-claude-code-asset/build-fix
---

# build-fix

skills/jh941213/my-claude-code-asset/build-fix
build-fix
Installation
$ npx skills add https://github.com/jh941213/my-claude-code-asset --skill build-fix
SKILL.md
빌드 에러 수정

TypeScript 및 빌드 에러를 점진적으로 수정합니다.

진행 순서

빌드 실행

npm run build
# 또는
pnpm build


에러 분석

파일별 그룹화
심각도 순 정렬

에러별 수정

에러 컨텍스트 확인 (전후 5줄)
문제 설명
수정 제안 및 적용
빌드 재실행
에러 해결 확인

중단 조건

수정이 새 에러 유발 시
동일 에러 3회 시도 후에도 지속 시
사용자 요청 시

요약 출력

수정된 에러 수
남은 에러 수
새로 발생한 에러
원칙
한 번에 하나의 에러만 수정
수정 후 반드시 빌드 재확인
새 에러 발생 시 롤백 고려
Weekly Installs
15
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