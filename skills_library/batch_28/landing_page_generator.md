---
title: landing-page-generator
url: https://skills.sh/uxjoseph/landing-page-generator/landing-page-generator
---

# landing-page-generator

skills/uxjoseph/landing-page-generator/landing-page-generator
landing-page-generator
Installation
$ npx skills add https://github.com/uxjoseph/landing-page-generator --skill landing-page-generator
SKILL.md
상세페이지 생성기 (Landing Page Generator)
개요

제품/서비스 정보를 기반으로 고전환 상세페이지를 자동 생성하는 스킬입니다.

실행 흐름
[입력] 제품/서비스 정보
         ↓
[Step 1] 입력 수집 - agents/01-intake.md
         ↓
[Step 2] 타겟 리서치 - agents/02-research.md
         ↓
[Step 3] 13섹션 카피 - agents/03-copy.md
         ↓
[Step 4] 디자인 방향 - agents/04-design-direction.md
         ↓
[Step 5] Gemini 프롬프트 생성 - agents/05-prompt-generator.md
         ↓
[Step 6] Gemini API로 13개 이미지 생성
         ↓
[Step 7] 이미지 스티칭 → 최종 PNG/PDF

필수 입력 정보
필드	설명	예시
product_name	제품/서비스명	"AI 마케팅 자동화 툴"
one_liner	한 줄 정의	"광고비 50% 절감하는 AI 마케팅"
target_audience	핵심 타겟	"월 광고비 100만원 이상 쓰는 스마트스토어 셀러"
main_problem	해결하는 핵심 문제	"광고 최적화에 하루 2시간 소비"
key_benefit	핵심 혜택	"AI가 24시간 자동 최적화, 광고비 50% 절감"
price	가격	"월 99,000원 (정가 199,000원)"
urgency	한정 요소	"선착순 100명 50% 할인"
선택 입력 정보
testimonials: 고객 후기
creator_bio: 제작자 소개
bonus_items: 보너스 구성
guarantee: 환불/보장 정책
faq: FAQ 항목
brand_color: 브랜드 컬러 (미입력시 자동 제안)
13개 섹션 구조

상세 가이드: references/13-section-guide.md

#	섹션명	높이	핵심 요소
01	Hero	800px	헤드라인, CTA, 긴급성 배지
02	Pain	600px	페인포인트 3-4개
03	Problem	500px	진짜 원인, 구조적 문제
04	Story	700px	Before→After 변화
05	Solution	400px	제품 한 줄 정의
06	How It Works	600px	단계별 프로세스
07	Social Proof	800px	후기, 수치
08	Authority	500px	제작자 소개
09	Benefits	700px	혜택, 보너스
10	Risk Removal	500px	환불 정책, FAQ
11	Comparison	400px	Before/After 대비
12	Target Filter	400px	추천/비추천 대상
13	Final CTA	600px	최종 CTA
사용 방법
1. 정보 수집 대화
사용자: 상세페이지 만들어줘
→ 필수 정보 질문 시작

2. 전체 프로세스 자동 실행

정보 수집 후 자동으로:

타겟 리서치
카피라이팅
디자인 방향 설정
Gemini 이미지 생성
최종 조립
3. 출력
output/sections/ - 섹션별 PNG (13장)
output/final_page.png - 최종 상세페이지
output/final_page.pdf - PDF 버전
기술 스펙
이미지 너비: 1200px (고정)
총 높이: ~7,000px (가변)
API: Gemini 3.0 Pro (이미지 생성)
스크립트: Python (Pillow)
참조 문서
13섹션 가이드
카피 패턴
Gemini 프롬프트 패턴
디자인 스펙
Weekly Installs
9
Repository
uxjoseph/landin…enerator
GitHub Stars
32
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn