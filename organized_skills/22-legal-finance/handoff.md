---
rating: ⭐⭐⭐
title: handoff
url: https://skills.sh/jh941213/my-claude-code-asset/handoff
---

# handoff

skills/jh941213/my-claude-code-asset/handoff
handoff
Installation
$ npx skills add https://github.com/jh941213/my-claude-code-asset --skill handoff
SKILL.md
HANDOFF.md 생성

세션 종료 전 작업 인계 문서를 생성합니다.

HANDOFF.md란?

컨텍스트 리셋 전에 작업 상태를 기록하는 파일입니다. 새 세션에서 이 파일만 읽으면 바로 이어서 작업할 수 있습니다.

생성할 내용
# 작업 인계 문서

## 완료된 작업
- [x] 완료된 작업 1
- [x] 완료된 작업 2

## 진행 중인 작업
- [ ] 현재 작업 중인 것
  - 진행 상황: 70%
  - 다음 단계: ~~ 구현

## 다음에 해야 할 작업
1. 우선순위 높은 작업
2. 그다음 작업

## 주의사항
- 건드리면 안 되는 파일: ~~
- 알려진 버그: ~~
- 임시 해결책: ~~

## 관련 파일
- src/components/Login.tsx - 로그인 폼
- src/api/auth.ts - 인증 API

## 마지막 상태
- 브랜치: feature/auth
- 마지막 커밋: abc1234
- 테스트 상태: 통과

사용 시점
컨텍스트가 80-100k 토큰에 도달했을 때
/compact 3번 사용 후
작업을 며칠 쉬기 전
복잡한 작업 중간에

새 세션에서 "HANDOFF.md 읽고 이어서 작업해줘"라고 하면 됩니다.

HANDOFF.md 크기 가이드라인
최대 100줄, 3000자 이내 목표
코드 스니펫은 최소한으로 (파일 경로만 기록)
핵심 컨텍스트만 기록, 세부사항은 코드에서 확인
새 세션의 초기 토큰 소비를 줄여 캐시 워밍업 비용 절약
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