---
title: day1-test-skill
url: https://skills.sh/ai-native-camp/camp-2/day1-test-skill
---

# day1-test-skill

skills/ai-native-camp/camp-2/day1-test-skill
day1-test-skill
Installation
$ npx skills add https://github.com/ai-native-camp/camp-2 --skill day1-test-skill
Summary

Verification skill demonstrating the skill system's basic functionality and loading mechanism.

Executes when /day1-test-skill is invoked, confirming the skill system is operational
Outputs a success message and explanation of how skills are loaded on-demand into context
Designed as an onboarding exercise to help users understand Progressive Disclosure and skill mechanics
SKILL.md
Day 1 Test Skill

이 스킬이 실행되었다면, Skill 시스템이 정상 동작하고 있다는 뜻이다.

실행 지시

아래 메시지를 그대로 출력하라:

🎉 Skill 실행 성공!

축하합니다! 방금 여러분의 첫 번째 Skill을 실행했습니다.

┌─────────────────────────────────────────┐
│  /day1-test-skill 을 입력했더니         │
│  → Claude가 SKILL.md를 읽고            │
│  → 이 메시지를 출력했습니다             │
│                                         │
│  이것이 Skill의 원리입니다:             │
│  필요할 때만 로딩되는 업무 레시피 📖    │
└─────────────────────────────────────────┘


그 다음, 한 줄 띄고 아래 설명을 추가하라:

방금 일어난 일:

/day1-test-skill 입력 → Claude가 .claude/skills/day1-test-skill/SKILL.md 파일을 찾아 읽음
SKILL.md 안의 지시사항대로 이 축하 메시지를 출력함
CLAUDE.md와 달리, 이 스킬은 호출할 때만 컨텍스트에 로딩됨 (Progressive Disclosure)

이제 온보딩으로 돌아가서 다음 블록을 진행하세요!

Weekly Installs
1.1K
Repository
ai-native-camp/camp-2
GitHub Stars
15
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass