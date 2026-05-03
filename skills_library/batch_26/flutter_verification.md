---
title: flutter-verification
url: https://skills.sh/vp-k/flutter-craft/flutter-verification
---

# flutter-verification

skills/vp-k/flutter-craft/flutter-verification
flutter-verification
Installation
$ npx skills add https://github.com/vp-k/flutter-craft --skill flutter-verification
SKILL.md
Flutter Verification Before Completion
Overview

Claiming work is complete without verification is dishonesty, not efficiency.

Core principle: Evidence before claims, always.

Violating the letter of this rule is violating the spirit of this rule.

The Iron Law
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE


If you haven't run the verification command in this message, you cannot claim it passes.

Flutter Verification Commands
1. Static Analysis (Always Required)
flutter analyze


Expected output:

Analyzing <project>...
No issues found!


If issues found:

Analyzing <project>...
   info • ... • lib/path/file.dart:42:10 • ...
   warning • ... • lib/path/file.dart:50:5 • ...

3 issues found. (1 warning, 2 hints)

2. Unit Tests (Priority 1 & 2)
# All tests
flutter test

# Specific feature tests
flutter test test/features/<feature>/

# Specific test file
flutter test test/features/<feature>/data/repositories/user_repository_test.dart


Expected output:

00:05 +12: All tests passed!


If tests fail:

00:03 +10 -2: Some tests failed.

3. Build Verification
# Android debug build
flutter build apk --debug

# iOS debug build (macOS only)
flutter build ios --debug --no-codesign

# Web build
flutter build web


Expected output:

✓ Built build/app/outputs/flutter-apk/app-debug.apk (XX.XMB)

4. Format Check (Optional)
dart format --set-exit-if-changed lib/

The Gate Function
BEFORE claiming any status or expressing satisfaction:

1. IDENTIFY: What command proves this claim?
2. RUN: Execute the FULL command (fresh, complete)
3. READ: Full output, check exit code, count failures
4. VERIFY: Does output confirm the claim?
   - If NO: State actual status with evidence
   - If YES: State claim WITH evidence
5. ONLY THEN: Make the claim

Skip any step = lying, not verifying

Common Flutter Failures
Claim	Requires	Not Sufficient
"Code is clean"	flutter analyze: No issues	"I wrote correct code"
"Tests pass"	flutter test: All passed	"Should pass", "Looks correct"
"Build succeeds"	flutter build: Built successfully	"Analyze passed"
"Feature complete"	All verification + requirements check	"Tests pass"
"Bug fixed"	Test original symptom + verify	"Code changed"
"Widget works"	Widget test or manual verification	"Code looks right"
Red Flags - STOP

If you catch yourself thinking or saying:

"should work now"
"probably passes"
"looks correct"
"I'm confident"
"just this once"
"analyze passed, so build will work"
"the code is right"
ANY wording implying success without running verification

STOP. Run the verification command.

Verification Checklist

Before claiming completion:

### Verification Results

**Static Analysis:**
```bash
$ flutter analyze
Analyzing flutter_app...
No issues found!


✅ Passed

Unit Tests:

$ flutter test test/features/<feature>/
00:05 +12: All tests passed!


✅ 12/12 passed

Build:

$ flutter build apk --debug
✓ Built build/app/outputs/flutter-apk/app-debug.apk


✅ Built successfully

Ready to claim completion.


## Key Patterns

**Static Analysis:**


✅ [Run flutter analyze] [See: No issues found!] "Analysis passes" ❌ "Code looks clean" / "I wrote it correctly"


**Tests:**


✅ [Run flutter test] [See: 34/34 pass] "All tests pass" ❌ "Should pass now" / "Tests look correct"


**Build:**


✅ [Run flutter build] [See: Built successfully] "Build passes" ❌ "Analyze passed" (analyze doesn't check build)


**Feature completion:**


✅ Re-read plan → Verify each requirement → Run all verifications → Report ❌ "Tests pass, feature complete"


## Rationalization Prevention

| Excuse | Reality |
|--------|---------|
| "Should work now" | RUN flutter analyze/test |
| "I'm confident" | Confidence ≠ evidence |
| "Just this once" | No exceptions |
| "Analyze passed" | Analyze ≠ build ≠ test |
| "Code looks right" | Verify independently |
| "I'm tired" | Exhaustion ≠ excuse |
| "It's simple code" | Simple code can still fail |

## Why This Matters

- **Trust:** If you claim "tests pass" without running them, trust is broken
- **Time:** False completion → redirect → rework wastes everyone's time
- **Quality:** Unverified code may crash in production
- **Integrity:** Honesty is a core value

## When To Apply

**ALWAYS before:**
- ANY variation of success/completion claims
- ANY expression of satisfaction ("Done!", "Fixed!", "Works!")
- Committing code
- Creating PRs
- Moving to next task
- Reporting to user

## The Bottom Line

**No shortcuts for verification.**

Run the command. Read the output. THEN claim the result.

```bash
# Always run these before claiming completion:
flutter analyze
flutter test
flutter build apk --debug  # or appropriate build target


This is non-negotiable.

5. Visual Verification (Optional — Flutter Web)

UI 변경이 포함된 작업에서, design-polish 플러그인이 설치되어 있다면 시각적 검증을 수행합니다. 설치되어 있지 않으면 이 단계를 건너뜁니다 (SOFT_FAIL).

전제 조건
design-polish 플러그인 설치됨 (~/.claude/plugins/marketplaces/design-polish 또는 ~/.claude/plugins/design-polish)
scripts/capture.cjs 존재
Node.js + npx 사용 가능
절차

Flutter Web 빌드

flutter build web


빌드 결과 로컬 서빙

npx serve build/web -l 3000 &
SERVER_PID=$!


스크린샷 + WCAG 체크

BASE_URL=http://localhost:3000 node <design-polish-path>/scripts/capture.cjs --wcag /


결과 확인

.design-polish/health-score.json: 디자인 건강 점수 (0-100)
.design-polish/accessibility/wcag-report.json: WCAG 위반 사항
.design-polish/screenshots/current-main.png: 현재 스크린샷

서버 종료

kill $SERVER_PID 2>/dev/null

판정 기준
결과	조건	액션
PASS	WCAG 위반 0개, Health Score ≥ 60	완료
WARN	WCAG 위반 1-3개 (minor/moderate)	개선 권장, 차단 아님
FAIL	WCAG critical 위반 존재	수정 권장 (SOFT_FAIL: 차단하지 않음)
SKIP	design-polish 미설치	건너뜀
증거 기록
**Visual Verification:**
- Health Score: 85/100
- WCAG: 0 violations
- Screenshot: .design-polish/screenshots/current-main.png
✅ Visual check passed (or ⚠️ skipped / ⚠️ warnings found)

Weekly Installs
16
Repository
vp-k/flutter-craft
GitHub Stars
6
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass