---
rating: ⭐⭐⭐
title: ai-model-reference
url: https://skills.sh/monicajeon28/gmcruise/ai-model-reference
---

# ai-model-reference

skills/monicajeon28/gmcruise/ai-model-reference
ai-model-reference
Installation
$ npx skills add https://github.com/monicajeon28/gmcruise --skill ai-model-reference
SKILL.md
AI Model Reference Guide (2025년 12월 기준)

AI 모델 API 호출 시 정확한 모델명과 가격 정보를 빠르게 참조할 수 있는 가이드입니다.

🚀 Quick Reference - 즉시 사용 가능한 모델명
🧠 추론 모델 (복잡한 문제 해결)
제공사	모델	API 호출명	Context	Input/Output (/1M)
OpenAI	o3	o3-2025-04-16	200K	$2.00 / $8.00
OpenAI	o4-mini	o4-mini-2025-04-16	200K	$1.10 / $4.40
DeepSeek	R1	deepseek-reasoner	64K	$0.55 / $2.19
Google	Gemini 3 Pro	gemini-3-pro-preview	1M	$2.00~$4.00 / $12.00~$18.00
Google	Gemini 2.5 Pro	gemini-2.5-pro	1M	$1.25 / $10.00
Anthropic	Opus 4.5	claude-opus-4-5-20251101	200K	$5.00 / $25.00
⚡ FAST 모델 (일반 작업)
제공사	모델	API 호출명	Context	Input/Output (/1M)
OpenAI	GPT-5.1	gpt-5.1	272K	$1.25 / $10.00
OpenAI	GPT-5	gpt-5-2025-08-07	272K	$1.25 / $10.00
OpenAI	GPT-5 최신	gpt-5-chat-latest	272K	$1.25 / $10.00
OpenAI	GPT-4.1	gpt-4.1-2025-04-14	1M	$2.00 / $8.00
Anthropic	Sonnet 4.5	claude-sonnet-4-5-20250929	200K	$3.00 / $15.00
Anthropic	Sonnet 4	claude-sonnet-4-20250514	200K	$3.00 / $15.00
Google	Gemini 2.5 Flash	gemini-2.5-flash	1M	$0.15 / $0.60~$3.50
💰 가성비 모델 (대량 처리/저비용)
제공사	모델	API 호출명	Context	Input/Output (/1M)
OpenAI	GPT-5 Nano	gpt-5-nano	272K	$0.05 / $0.40
OpenAI	GPT-4o Mini	gpt-4o-mini	128K	$0.15 / $0.60
OpenAI	GPT-4.1 Nano	gpt-4.1-nano-2025-04-14	1M	$0.10 / $0.40
Google	Gemini 2.5 Flash-Lite	gemini-2.5-flash-lite	1M	$0.10 / $0.40
Google	Gemini 2.0 Flash-Lite	gemini-2.0-flash-lite	1M	$0.075 / $0.30
Anthropic	Haiku 3	claude-3-haiku-20240307	200K	$0.25 / $1.25
DeepSeek	Chat	deepseek-chat	64K	$0.27 / $1.10
📏 Context Window 비교
제공사	최대 Context	대표 모델
Google	1M (1,048,576)	Gemini 2.5 시리즈 전체
OpenAI	1M	GPT-4.1 시리즈
OpenAI	272K	GPT-5 시리즈
Anthropic	200K	Claude 전체
DeepSeek	64K	R1, Chat
상세 정보 참조
전체 모델 목록 및 API 호출명: references/models.md
상세 가격 및 캐싱 비용: references/pricing.md
빠른 선택 가이드
복잡한 추론/코딩 작업
OpenAI: o3, o4-mini
Anthropic: claude-opus-4-5-20251101, claude-opus-4-20250514
Google: gemini-3-pro-preview, gemini-2.5-pro
DeepSeek: deepseek-reasoner

빠른 응답이 필요한 일반 작업
OpenAI: gpt-5.1, gpt-5, gpt-4o
Anthropic: claude-sonnet-4-5-20250929, claude-sonnet-4-20250514
Google: gemini-2.5-flash

대량 처리/비용 최적화
OpenAI: gpt-5-nano ($0.05/$0.40)
Anthropic: claude-3-5-haiku-20241022 ($0.80/$4.00)
Google: gemini-2.5-flash-lite ($0.10/$0.40)
DeepSeek: deepseek-chat (off-peak 75% 할인)

비용 절감 전략
1. 프롬프트 캐싱 (90% 절감 가능)
Anthropic: cache write 1.25x, cache read 0.1x (90% 절감)
OpenAI: cached input $0.125/1M (GPT-5 기준 90% 절감)
Google: cache read 10% of base price
2. 배치 처리 (50% 절감)
24시간 내 비동기 처리로 입출력 50% 할인
OpenAI Batch API, Anthropic Batch Processing 지원
3. 모델 계층화 전략
간단한 작업 → Nano/Haiku (저비용)
     ↓ 복잡도 증가 시
중간 작업 → Mini/Flash (균형)
     ↓ 복잡도 증가 시
복잡한 작업 → Pro/Opus (고성능)

코드 예시
OpenAI API 호출
from openai import OpenAI
client = OpenAI()

# GPT-5.1 (최신 플래그십)
response = client.chat.completions.create(
    model="gpt-5.1",  # 또는 "gpt-5-2025-08-07"
    messages=[{"role": "user", "content": "Hello"}]
)

# 추론 모델
response = client.chat.completions.create(
    model="o3-2025-04-16",
    messages=[{"role": "user", "content": "복잡한 수학 문제"}]
)

Anthropic API 호출
import anthropic
client = anthropic.Anthropic()

# Claude Opus 4.5 (최신 플래그십)
response = client.messages.create(
    model="claude-opus-4-5-20251101",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}]
)

# 가성비 모델
response = client.messages.create(
    model="claude-3-5-haiku-20241022",
    max_tokens=1024,
    messages=[{"role": "user", "content": "간단한 질문"}]
)

Google Gemini API 호출
import google.generativeai as genai

# Gemini 3 Pro (최신 추론 모델)
model = genai.GenerativeModel('gemini-3-pro-preview')
response = model.generate_content("Hello")

# Gemini 2.5 Pro
model = genai.GenerativeModel('gemini-2.5-pro')
response = model.generate_content("Hello")

# Gemini 2.5 Flash (빠른 응답)
model = genai.GenerativeModel('gemini-2.5-flash')
response = model.generate_content("Hello")

DeepSeek API 호출
from openai import OpenAI

client = OpenAI(
    api_key="your-deepseek-key",
    base_url="https://api.deepseek.com"
)

# DeepSeek Chat (일반)
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "Hello"}]
)

# DeepSeek Reasoner (추론)
response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{"role": "user", "content": "복잡한 문제"}]
)

Weekly Installs
10
Repository
monicajeon28/gmcruise
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass