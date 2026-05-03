---
rating: ⭐⭐⭐
title: bf-metrics
url: https://skills.sh/khaki4/my_skills/bf-metrics
---

# bf-metrics

skills/khaki4/my_skills/bf-metrics
bf-metrics
Installation
$ npx skills add https://github.com/khaki4/my_skills --skill bf-metrics
SKILL.md
Metrics Analysis
Overview

스프린트 메트릭을 집계·분석하여 모델 배당 최적화와 난이도 재태깅을 제안한다. 자동 적용하지 않으며, 사람이 판단한다.

When to Use
사용자가 /bf-metrics를 입력했을 때
/bf-archive-sprint 완료 후 안내에 따라 실행할 때
여러 스프린트를 거친 후 패턴 분석이 필요할 때
Prerequisites
docs/sprint-status.yaml 또는 docs/archive/*/sprint-status.yaml 중 하나 이상 존재
분석 대상 Story에 메트릭 필드가 기록되어 있어야 함 (레거시 Story는 건너뜀)
권장 실행 순서: /bf-archive-sprint → /bf-metrics → /bf-update-conventions. 아카이빙 전에 실행해도 동작하지만, 아카이빙 후 실행하면 현재 + 아카이브 전체 데이터를 분석하여 더 정확한 결과를 제공
Error Handling
sprint-status.yaml도 archive도 없으면: "분석 가능한 스프린트 데이터가 없습니다. /bf-execute로 워크플로우를 먼저 실행하세요." 안내
모든 Story가 레거시이면: "메트릭 필드가 기록된 Story가 없습니다. 현행 워크플로우(v2+)로 실행한 스프린트만 분석할 수 있습니다." 안내
완료된 Story가 없으면: "완료(done) 상태의 Story가 없습니다. 진행 중인 스프린트의 분석은 완료 후 수행하세요." 안내
Instructions
1. 데이터 수집

a. 현재 스프린트 데이터를 수집한다:

docs/sprint-status.yaml 읽기

b. 아카이브된 스프린트 데이터를 수집한다:

docs/archive/*/sprint-status.yaml 패턴으로 모든 아카이브 파일 읽기

c. 분석 대상 필터링:

status: done인 Story만 분석 대상에 포함
레거시 Story 판정 기준: model_used AND ralph_retries YAML key가 모두 존재하지 않는 Story는 레거시로 간주하여 건너뜀. 두 키 중 하나라도 존재하면 현행 포맷으로 처리한다. (model_used: null은 미완료 Story이므로 status: done 조건에서 이미 필터됨)
건너뛴 Story 수를 기록하여 리포트에 표시
2. 집계 테이블 생성

(difficulty, model_used) 페어별로 다음 지표를 집계한다:

지표	계산 방법
story_count	해당 페어의 Story 수
avg_ralph_retries	평균 재시도 횟수
avg_ralph_approaches	평균 접근 전환 횟수
stuck_rate	ralph_stuck: true 비율 (%)
avg_review_blockers	평균 🔴 Blocker 건수
avg_review_recommended	평균 🟡 Recommended 건수
regression_rate	is_regression: true 비율 (%)
3. 모델 배당 최적화 제안

아래 임계값에 해당하는 (difficulty, model_used) 페어에 대해 제안을 생성한다:

조건	임계값	제안
높은 블로커	avg_review_blockers >= 2.0	더 강한 모델 배당 제안 (예: sonnet → opus-lead)
높은 재시도	avg_ralph_retries >= 3.0	구현 모델 업그레이드 제안
높은 stuck	stuck_rate >= 20%	Agent Teams 전략 전환 제안 (예: ralph-loop → opus-lead)
높은 회귀	regression_rate >= 25%	리뷰 모델 강화 제안
임계값에 해당하지 않으면 "현재 모델 배당 적정" 메시지를 표시한다.
제안에는 해당 조건을 충족한 구체적 수치를 함께 표시한다.
4. 난이도 재태깅 제안

완료된 개별 Story의 메트릭을 기준으로 난이도 조정을 제안한다:

과소평가 (상향 제안):

현재 → 제안	조건
S → M	ralph_retries >= 3 OR review_blockers >= 2 OR ralph_stuck == true
M → L	ralph_retries >= 4 OR review_blockers >= 3 OR ralph_approaches >= 2
L → XL	ralph_stuck == true AND ralph_approaches >= 3

과대평가 (하향 제안):

현재 → 제안	조건
M → S	ralph_retries == 0 AND review_blockers == 0 AND review_recommended <= 1
L → M	ralph_retries <= 1 AND review_blockers == 0
XL → L	ralph_retries <= 1 AND review_blockers == 0 AND ralph_approaches == 0
해당 Story ID와 함께 구체적 메트릭 수치를 표시한다.
제안이 없으면 "난이도 태깅 적정" 메시지를 표시한다.
5. E2E 실패 패턴 분석

failure_tag별로 건수와 비율을 집계한다:

failure_tag	건수	비율
spec-gap	N	N%
impl-bug	N	N%
test-design	N	N%
convention-violation	N	N%
integration	N	N%
regression Story가 없으면 "E2E 회귀 없음" 메시지를 표시한다.
특정 태그가 50% 이상이면 해당 영역 집중 개선 제안을 추가한다.
6. 종합 요약

위 분석 결과를 종합하여 우선순위별 액션 아이템을 정리한다:

🔴 즉시 조치: 높은 stuck_rate, 높은 블로커 등 심각한 패턴
🟡 검토 권장: 과소/과대평가된 난이도, 모델 최적화 기회
🟢 양호: 임계값 내 정상 범위
Output Format

대화로만 출력한다 (파일 저장 없음, read-only 스킬).

## 📊 BF Workflow Metrics Report

### 분석 범위
- 스프린트: {수집된 스프린트 목록}
- 분석 대상: {N}개 Story (레거시 {M}개 제외)

### 1. (Difficulty, Model) 페어별 집계
{집계 테이블}

### 2. 모델 배당 최적화 제안
{제안 목록 또는 "현재 모델 배당 적정"}

### 3. 난이도 재태깅 제안
{과소/과대평가 제안 목록 또는 "난이도 태깅 적정"}

### 4. E2E 실패 패턴
{failure_tag 집계 테이블 또는 "E2E 회귀 없음"}

### 5. 종합 액션 아이템
🔴 즉시 조치: ...
🟡 검토 권장: ...
🟢 양호: ...

Weekly Installs
12
Repository
khaki4/my_skills
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass