---
title: news-scrap
url: https://skills.sh/g2e-yunseonghun/commit-skils-test/news-scrap
---

# news-scrap

skills/g2e-yunseonghun/commit-skils-test/news-scrap
news-scrap
Installation
$ npx skills add https://github.com/g2e-yunseonghun/commit-skils-test --skill news-scrap
SKILL.md
응급의료 AI 주간 뉴스 스크랩

응급의료 AI 관련 뉴스 기사와 학술 논문을 주간 단위로 수집하고, HTML 대시보드와 NotebookLM 산출물로 정리한다.

IMPORTANT: 모든 출력은 한국어로 작성한다.

Quick Start
수집 기간을 전주 토요일부터 이번 주 금요일까지로 계산한다.
국내 기사, 해외 기사, 학술 논문을 병렬 수집한다.
scripts/extract.py로 원문과 발행일을 확인한다.
결과를 합치고 중복을 제거한다.
원문이 있는 기사만 NotebookLM에 업로드해 요약과 인사이트를 받는다.
scripts/render_dashboard.py로 HTML 대시보드를 생성한다.
선택적으로 NotebookLM 노트와 scripts/slide.py 슬라이드를 생성한다.
Bundled Resources
scripts/extract.py URL 목록을 받아 trafilatura 우선, Playwright 폴백으로 본문과 메타데이터를 추출한다.
scripts/render_dashboard.py 구조화된 JSON 입력을 받아 templates/dashboard.html 기반 HTML 대시보드를 렌더링한다.
scripts/slide.py 주목 기사 JSON을 받아 3장짜리 .pptx를 생성한다.
templates/dashboard.html 대시보드 템플릿. render_dashboard.py가 마커를 채운다.
Environment
Required
trafilatura
notebooklm-py
python-pptx
Optional but recommended
playwright
Chromium 런타임

권장 설치:

pip install trafilatura notebooklm-py python-pptx playwright
playwright install chromium

Runtime Notes
extract.py는 기본적으로 headless Playwright를 사용한다.
디버깅이 필요할 때만 NEWS_SCRAP_HEADED=1로 headed 브라우저를 켠다.
render_dashboard.py와 slide.py는 UTF-8, UTF-8 BOM 입력 둘 다 허용한다.
Trigger Guidance
Activate when
/news-scrap, 뉴스 스크랩, 주간 뉴스, 뉴스 수집
"이번 주 응급의료 AI 뉴스 정리해줘"
"응급의료 AI 기사랑 논문 모아서 브리핑 만들어줘"
Do not activate when
단순 뉴스 검색 질문만 필요한 경우
응급의료와 직접 관련 없는 일반 AI 뉴스 요청인 경우
월간 인포그래픽만 필요한 경우 이 경우 monthly-report가 더 적합하다.
Workflow
Step 1. 기간 계산

오늘 날짜를 기준으로 가장 최근 금요일을 종료일로 잡고, 그로부터 6일 전 토요일을 시작일로 잡는다.

시작일: 전주 토요일
종료일: 이번 주 금요일
파일명용 형식: YYYY-MM-DD
표시용 형식: YYYY년 M월 D일(요일)

사용자에게 먼저 기간을 알려준다.

예시:

수집 기간: 2026년 3월 21일(토) ~ 2026년 3월 27일(금) - 3월 4주차

Step 2. 병렬 수집
Preferred path

TeamCreate와 SendMessage가 있으면 아래 3개 역할을 병렬로 돌린다.

국내기사
해외기사
학술논문

SendMessage는 반드시 한 번의 메시지에서 병렬 호출한다.

Fallback path

해당 도구가 없으면 메인 에이전트가 같은 검색 전략을 로컬에서 순차 또는 병렬로 수행한다. 이 경우에도 결과는 아래 3개 카테고리로 분리해서 유지한다.

국내 기사
해외 기사
학술 논문
Step 3. 공통 수집 규칙

각 수집 담당자에게 아래 규칙을 그대로 적용한다.

1) 검색 규칙
노이즈 도메인은 제외한다. youtube.com, blog.naver.com, tistory.com, brunch.co.kr, medium.com, velog.io, reddit.com
제목만으로 응급의료 관련성이 약하면 제외한다.
와일드카드 검색으로 잡힌 일반 의료 AI 기사는 응급실, 응급의학, EMS, 이송, 중환자와 직접 연결될 때만 포함한다.
2) 발행일 검증

검색 결과만 믿지 말고, URL마다 scripts/extract.py를 실행해 본문과 발행일을 확인한다.

PowerShell 예시:

'["https://url1", "https://url2"]' | python /absolute/path/to/scripts/extract.py


반환 형식:

[
  {
    "url": "...",
    "text": "본문",
    "date": "YYYY-MM-DD",
    "title": "제목",
    "success": true
  }
]


처리 규칙:

success=true 이고 date가 기간 내면 포함한다.
success=true 이지만 date=null이면 검색 스니펫이나 URL 경로에서 날짜를 재확인한다.
success=false여도 날짜만 확정할 수 있으면 포함한다. 이 경우 원문은 빈 문자열로 둔다.
발행일을 확정할 수 없으면 제외한다.
기간 밖이면 제외한다.
3) 수집 결과 계약

각 담당자는 최종적으로 설명 없이 JSON 배열만 반환한다.

[
  {
    "기관매체": "출처 매체명 또는 저널명",
    "관련기관": "기사에 등장하는 병원/기업/기관",
    "활용분야": "트리아지, 영상판독 등",
    "구분": "연구|도입|정책|트렌드",
    "제목": "기사/논문 제목",
    "원문": "추출한 본문 또는 빈 문자열",
    "날짜": "YYYY-MM-DD",
    "링크": "원문 URL"
  }
]

Step 4. 담당자별 검색 프롬프트

아래 키워드는 그대로 쓰되, 검색 엔진 특성에 따라 표현만 약간 바꿀 수 있다.

국내 기사
응급실 AI 인공지능 {시작일}~{종료일}
응급의학 인공지능 병원 도입 {시작일}~{종료일}
응급환자 AI 트리아지 분류 {시작일}~{종료일}
응급의료 AI 정책 정부 {시작일}~{종료일}
응급실 과밀 AI 병상 배정 {시작일}~{종료일}
119 AI 시스템 구급 {시작일}~{종료일}
중증환자 AI 분류 예측 {시작일}~{종료일}
의료 AI 인공지능 병원 도입 {시작일}~{종료일} 와일드카드

우선 도메인:

medigatenews.com
dailymedi.com
mdtoday.co.kr
pharm.edaily.co.kr
mohw.go.kr
medicaltimes.com
docdocdoc.co.kr
해외 기사
emergency department AI triage {시작일}~{종료일}
emergency medicine artificial intelligence {시작일}~{종료일}
emergency room AI clinical decision support {시작일}~{종료일}
emergency department overcrowding AI patient flow {시작일}~{종료일}
prehospital AI EMS prediction {시작일}~{종료일}
ambulance AI routing dispatch real-time {시작일}~{종료일}
hospital AI clinical workflow automation {시작일}~{종료일} 와일드카드

우선 도메인:

healthcareitnews.com
beckershospitalreview.com
statnews.com
fiercehealthcare.com
mobihealthnews.com
ems1.com
학술 논문
emergency triage AI machine learning site:pubmed.ncbi.nlm.nih.gov {시작일}~{종료일}
emergency medicine artificial intelligence peer-reviewed {시작일}~{종료일}
emergency department AI clinical trial {시작일}~{종료일}
emergency department crowding AI resource allocation {시작일}~{종료일}
prehospital emergency AI prediction model {시작일}~{종료일}

우선 도메인:

pubmed.ncbi.nlm.nih.gov
pmc.ncbi.nlm.nih.gov
medinform.jmir.org
jmir.org
annemergmed.com
ai.nejm.org
nature.com
frontiersin.org
mdpi.com
sciencedirect.com
Step 5. 결과 정규화와 중복 제거

담당자 응답이 JSON만 반환되지 않으면, 응답 텍스트에서 가장 바깥 [ 와 ] 사이의 JSON 배열을 추출해서 파싱한다. 파싱 실패 시 해당 담당자 결과는 빈 배열로 처리한다.

정리 규칙:

동일 URL은 1건만 남긴다.
같은 내용을 여러 매체가 재보도한 경우 대표 1건만 남긴다.
응급의료 직접 관련성이 낮은 일반 의료 AI 뉴스는 마지막에 다시 걸러낸다.
최종 결과는 국내기사, 해외기사 2개 섹션으로 나눈다. 학술 논문은 해외기사 섹션에 같이 둬도 된다.
Step 6. NotebookLM 업로드와 분석

이 단계는 선택 사항이다. NotebookLM 인증이나 API가 안 되면 HTML 생성만 진행한다.

6-1. 인증 확인
python -c "
import asyncio
from notebooklm import NotebookLMClient

async def main():
    try:
        async with await NotebookLMClient.from_storage() as client:
            await client.notebooks.list()
            print('AUTH_OK')
    except Exception as e:
        print(f'AUTH_FAIL:{e}')

asyncio.run(main())
"


실패 시:

notebooklm login을 안내한다.
재시도해도 안 되면 Step 7만 수행하고, Step 8~9는 건너뛴다.
6-2. 월간 노트북 확보

노트북 이름 규칙:

응급의료_AI_월간브리핑_{년}_{월}

같은 달 노트북이 있으면 재사용하고, 없으면 만든다.

6-3. 주차별 합본 업로드

원문이 있는 기사만 하나의 텍스트로 합쳐 client.sources.add_text() 1회로 올린다.

합본 형식:

=== 응급의료 AI 주간 뉴스 — {시작일}~{종료일} ({월} {주차}) ===

--- 기사 1 ---
제목: ...
매체: ... | 관련기관: ... | 분야: ... | 구분: ...
날짜: ... | 원문링크: ...

원문...

6-4. NotebookLM 질의

최소 4개 응답을 받는다.

Q0: 기사별 상세 요약
Q1: 이번 주 핵심 동향
Q2: 주목할 기관/기업
Q3: 시사점

중요 규칙:

소스 본문만 근거로 답하라고 명시한다.
추측 금지를 명시한다.
기사별 응답은 제목 기준으로 다시 매칭 가능한 형식을 강제한다.

파싱 실패 시:

기사 요약은 원문 첫 3문장 또는 원문 미확보로 대체한다.
세부 분석 항목은 빈 값으로 둔다.
Step 7. HTML 대시보드 생성

HTML은 수작업 치환 대신 scripts/render_dashboard.py를 사용한다.

입력 JSON 예시:

{
  "시작일": "2026년 3월 21일(토)",
  "종료일": "2026년 3월 27일(금)",
  "생성일": "2026년 3월 27일",
  "국내기사": [
    {
      "제목": "기사 제목",
      "기관매체": "매체명",
      "관련기관": "관련 기관",
      "활용분야": "응급실 AI 어시스턴트",
      "구분": "도입",
      "날짜": "2026-03-26",
      "링크": "https://...",
      "기사요약": "기사 요약",
      "세부분석": {
        "관련 기업/기관": "설명",
        "기술/제품": "설명",
        "핵심 수치": "설명"
      }
    }
  ],
  "해외기사": [],
  "주간요약": {
    "핵심동향": ["동향 1", "동향 2", "동향 3"],
    "주목할기관/기업": ["기관 1", "기관 2"],
    "시사점": "요약 문장"
  }
}


실행:

python /absolute/path/to/scripts/render_dashboard.py \
  /path/to/dashboard_input.json \
  news_output/news_{해당년도월주차}.html


결과:

출력 폴더가 없으면 자동 생성한다.
국내/해외 기사 목록, 요약 섹션, 수치 카드가 채워진다.
비어 있는 섹션에는 안내 문구를 넣는다.
Step 8. NotebookLM 주간 노트 생성

NotebookLM이 사용 가능하면 Step 6 요약을 주간 리포트 노트로 남긴다.

노트 제목:

주간 리서치 리포트 — {시작일}~{종료일}

내용:

이번 주 핵심 동향
주목할 기관/기업
시사점
총 수집 건수
Step 9. 주목 기사 슬라이드 생성

NotebookLM이 사용 가능하면 가장 중요한 기사 1건을 선정한 뒤 scripts/slide.py를 호출한다.

입력 JSON 예시:

{
  "제목": "기사 제목",
  "매체": "출처 매체",
  "날짜": "2026-03-27",
  "주차": "3월 4주차",
  "기사요약": "5~8문장 요약",
  "기관소개": [
    { "기관명": "기관A", "설명": "기관 소개" }
  ],
  "기술소개": [
    { "기술명": "기술A", "설명": "기술 설명" }
  ],
  "적용아이디어": [
    { "제목": "아이디어 1", "설명": "설명" }
  ]
}


실행:

python /absolute/path/to/scripts/slide.py \
  news_output/slide_{해당년도월주차}.pptx \
  /path/to/slide_input.json


주의:

slide.py는 UTF-8 BOM 입력도 허용한다.
출력 디렉터리가 없으면 자동 생성한다.
Output Contract

최종 산출물은 최대 3개다.

news_output/news_{해당년도월주차}.html
news_output/slide_{해당년도월주차}.pptx
NotebookLM 월간 노트북 내 주간 리포트 노트

사용자에게는 최소 아래를 알려준다.

저장 완료: news_output/news_26년 3월 4주차.html (국내 6건, 해외 2건)
슬라이드 생성 완료: news_output/slide_26년_3월_4주차.pptx

Error Handling
검색 결과가 0건인 키워드는 건너뛴다.
해당 주 기사 자체가 없으면 빈 HTML 섹션과 함께 그 사실을 안내한다.
발행일을 확정할 수 없는 기사는 제외한다.
extract.py에서 원문 추출 실패 시에도 날짜가 맞으면 포함한다.
Playwright 폴백이 실패해도 trafilatura 결과가 있으면 계속 진행한다.
NotebookLM 실패 시 HTML 생성은 계속 진행한다.
슬라이드 생성 실패 시에도 HTML과 NotebookLM 노트는 계속 진행한다.
Quality Bar
기사 제목 번역은 의미 보존을 우선한다.
기사 요약에는 누가, 무엇을, 왜, 어떻게를 넣는다.
세부 분석은 실제 소스에 없는 수치를 지어내지 않는다.
와일드카드 검색 결과는 응급의료 직접 관련성을 반드시 다시 검토한다.
가능하면 국내와 해외 섹션의 기사 수를 균형 있게 확보하되, 억지로 채우지 않는다.
Weekly Installs
9
Repository
g2e-yunseonghun…ils-test
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn