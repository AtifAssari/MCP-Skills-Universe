---
title: my-fetch-tweet
url: https://skills.sh/ai-native-camp/camp-1/my-fetch-tweet
---

# my-fetch-tweet

skills/ai-native-camp/camp-1/my-fetch-tweet
my-fetch-tweet
Installation
$ npx skills add https://github.com/ai-native-camp/camp-1 --skill my-fetch-tweet
Summary

Fetch X/Twitter tweets with summaries, insights, and full Korean translations via a three-stage pipeline.

Extracts tweet text, author info, and engagement metrics (likes, retweets, views) using the FxEmbed API without JavaScript execution
Supports multiple URL formats: x.com, twitter.com, fxtwitter.com, and fixupx.com
Delivers insights in three stages: concise summary with author context, three-point analysis (core message, industry implications, personal relevance), then full natural Korean translation with quoted tweets
Falls back to direct WebFetch API calls when script execution is unavailable; respects rate limits and cannot retrieve private or deleted tweets
SKILL.md
My Fetch Tweet

X/Twitter URL에서 트윗 원문, 작성자 정보, 인게이지먼트 데이터를 가져오고 요약-인사이트-전체 번역 3단계 파이프라인으로 제공하는 스킬.

API 연동 — FxEmbed

FxEmbed 오픈소스 프로젝트의 API (api.fxtwitter.com)를 활용한다. JavaScript 없이 트윗 데이터를 추출할 수 있다.

URL 변환 규칙
URL에서 screen_name과 status_id를 추출한다
도메인을 api.fxtwitter.com으로 변환한다
WebFetch로 JSON 데이터를 가져온다
https://x.com/garrytan/status/123456
  → https://api.fxtwitter.com/garrytan/status/123456

지원 URL 형식

x.com, twitter.com, fxtwitter.com, fixupx.com

API 응답 주요 필드
필드	설명
tweet.text	트윗 본문 (URL 확장됨)
tweet.author	작성자 (name, screen_name, bio, followers)
tweet.likes / retweets / replies / views	인게이지먼트 수치
tweet.created_at	작성 일시
tweet.media	첨부 미디어 (photos, videos)
tweet.quote	인용 트윗 (동일 구조)
번역 파이프라인 — 3단계

전체 번역을 바로 보여주지 않는다. 단계별로 제공하여 이해도를 높인다.

1단계: 요약 (3-5문장)
트윗의 핵심 주장을 한국어로 요약
작성자 정보 포함 (이름, 팔로워 수)
인게이지먼트 수치 포함 (좋아요, 리트윗, 조회수)
"이 트윗이 뭘 말하는지 30초 만에 파악"
2단계: 인사이트 (3개)
핵심 메시지: 이 트윗이 정말 말하고 싶은 것
시사점: 업계/트렌드에서의 의미
적용점: 나(독자)에게 어떤 의미인지
3단계: 전체 번역
원문 전체를 자연스러운 한국어로 번역
인용 트윗이 있으면 함께 번역
전문 용어는 원문 병기 (예: "에이전트(Agent)")
WebFetch Fallback

스크립트 실행이 어려운 경우 WebFetch 도구로 직접 API 호출 가능:

URL: https://api.fxtwitter.com/{screen_name}/status/{status_id}
Prompt: "Extract the full tweet text, author name, and engagement metrics"

Limitations
비공개 계정 트윗은 조회 불가
삭제된 트윗은 조회 불가
API rate limit은 FxEmbed 서버 정책에 따름
Weekly Installs
671
Repository
ai-native-camp/camp-1
GitHub Stars
234
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn