---
title: k-research-note
url: https://skills.sh/ujon/skills/k-research-note
---

# k-research-note

skills/ujon/skills/k-research-note
k-research-note
Installation
$ npx skills add https://github.com/ujon/skills --skill k-research-note
SKILL.md
대한민국 정부과제 연구노트 작성 스킬

국가연구개발혁신법 시행령 제65조 및 연구노트 지침(과기정통부 고시)에 부합하는 연구노트를 생성한다. 상세 작성 가이드와 법적 근거는 references/research-note-guide.md를 참조한다.

워크플로우
1단계: 정보 수집

독립적인 질문은 묶어서 한 턴에 수집한다. 이전 대화에서 수집된 정보는 [기본값]으로 표시하고, 이미 제공된 항목은 건너뛴다. 선택형은 번호 입력, 자유입력은 텍스트 입력으로 받는다. 포맷 자동 판별: "한글/hwp/hwpx/한컴"→HWPX, "워드/docx/word"→DOCX, "pdf/피디에프"→PDF, "마크다운/markdown/md"→Markdown.

그룹 A: 기본 정보 (한 턴에 묶어서 질문)

아래 정보를 입력해주세요:

1) 출력 포맷: 1.DOCX  2.HWPX  3.PDF  4.Markdown
2) 과제명 (정부과제 공식 명칭):
3) 연구 제목 (이번 노트의 주제):
4) 기록자 (작성 연구원):
5) 작성일자 [2026-03-26]:


그룹 B: 옵션 설정 (그룹 A 응답 후 한 턴에 질문)

옵션을 선택해주세요:

1) 폰트: 1.맑은 고딕 11pt(기본)  2.직접 지정    ← DOCX/HWPX/PDF만, Markdown은 생략
2) 추가 데이터: 1.없음  2.파일 경로  3.직접 입력
3) 머리글/바닥글: 1.기본 포함  2.머리글만  3.바닥글만  4.없음    ← DOCX/HWPX/PDF만

폰트 직접 지정 시: 폰트명, 크기를 추가로 질문
데이터 파일 제공 시: 파일 경로를 추가로 질문. 파일 형식별 처리(CSV→테이블, JSON/XML→구조 정리, 텍스트→코드블록, 이미지→임베딩). 추가 첨부 여부 확인
데이터를 먼저 수집하면 이후 AI 작성 시 참고 가능

그룹 C: 작성 스타일 (그룹 B 응답 후 한 턴에 질문)

작성 스타일을 선택해주세요:

[기록 중심] 무엇을 했는가
  1) 서술형        — 시간순 일기체 ("~했다, ~을 발견했다")
  2) 프로토콜형    — 재현 가능한 단계별 절차 기록
  3) 데이터형      — 표·수치·측정값 위주, 해석 최소화
  4) 회의록형      — 참석자·논의·결정사항·후속조치

[사고 중심] 왜, 어떻게 판단했는가
  5) 문제해결형    — 문제→원인→시도→결과 구조
  6) 의사결정형    — 선택지·근거·결정 기록
  7) 학습기록형    — 새로 배운 내용·이해·의문점 정리

[관리 중심] 어디까지 왔는가
  8) 진척보고형    — 계획 대비 실적·이슈·대응
  9) 문헌정리형    — 논문/자료 요약 + 본 연구 연관성


스타일에 따라 섹션 구성이 자동으로 결정된다:

#	스타일	기본 섹션
1	서술형	연구 배경 / 수행 내용 / 관찰 및 발견 / 소감 및 향후 계획
2	프로토콜형	목적 / 재료 및 장비 / 실험 절차 / 결과 / 비고
3	데이터형	실험 조건 / 측정 데이터 / 통계 요약 / 비고
4	회의록형	회의 정보 / 논의 사항 / 결정 사항 / 후속 조치
5	문제해결형	문제 상황 / 원인 분석 / 시도한 해결책 / 결과 및 교훈
6	의사결정형	의사결정 배경 / 검토한 대안 / 선택 및 근거 / 후속 조치
7	학습기록형	학습 주제 / 핵심 내용 정리 / 의문점 및 미해결 사항 / 추가 학습 계획
8	진척보고형	보고 기간 / 계획 대비 실적 / 이슈 및 대응 / 향후 계획
9	문헌정리형	문헌 정보 / 핵심 내용 요약 / 본 연구와의 관련성 / 적용 방안

그룹 D: 섹션 내용 (그룹 C 응답 후)

스타일에서 결정된 섹션 목록을 보여주고, 각 섹션의 작성 방식을 한 턴에 질문한다.

[{스타일명}] 스타일의 섹션입니다. 각 섹션의 작성 방식을 선택해주세요:
(1.직접 입력  2.AI 작성  3.생략)

1) {섹션1}:
2) {섹션2}:
3) {섹션3}:
4) {섹션4}:

AI 작성 시: 웹 검색(web_search)으로 관련 정보 조사 → 초안 작성 → 사용자에게 보여주고 확인 (y/수정 입력)
결과 AI 작성 시 "예상 결과 초안"임을 명시
AI 작성 시 반드시 references/research-note-guide.md의 '작성 스타일별 톤 가이드'를 참조하여 해당 스타일의 문체·원칙·피해야 할 패턴을 따른다
특히: bullet 나열 대신 문장 서술 / 볼드 소제목 나열 금지 / 섹션 간 맥락 연결 / 참고자료는 본문에 녹이기

그룹 E: 선택 정보 — 추가 입력 여부 확인 (기본 n)

과제번호, 연구책임자, 주관연구기관, 점검자, 참고문헌
2단계: 스킬 검색

포맷별 처리:

DOCX/PDF: 외부 스킬 불필요 — generate_note.py가 직접 생성
HWPX: hwpx 스킬 검색 (user → private → public 순). 없으면 generate_note.py 사용. 스킬을 찾으면 해당 SKILL.md를 읽고 파일 생성 지침을 따른다.
Markdown: 직접 .md 파일 작성
3단계: 문서 생성

JSON 설정 파일 작성 후 스크립트 호출. 별도 Python 스크립트를 작성하지 않는다.

python skills/k-research-note/scripts/generate_note.py /tmp/note_config.json
# 데이터 첨부 시
python skills/k-research-note/scripts/generate_note.py /tmp/note_config.json --data file1.csv file2.json


JSON 설정 형식:

{
  "format": "hwpx|docx|pdf|markdown",
  "output": "./연구노트_2026-03-13.hwpx",
  "style": "narrative",
  "metadata": {
    "과제명": "", "연구제목": "", "기록자": "", "작성일자": "",
    "과제번호": null, "연구책임자": null, "주관연구기관": null
  },
  "font": {"name": "맑은 고딕", "size": 11},
  "sections": [
    {"title": "연구 배경", "content": "..."},
    {"title": "수행 내용", "content": "..."},
    {"title": "관찰 및 발견", "content": "..."},
    {"title": "소감 및 향후 계획", "content": "..."}
  ],
  "signature": {"기록자": "김연구", "점검자": "박검토"},
  "header_footer": {"mode": 1, "과제명": "", "기관명": null}
}


style 값 매핑:

번호	style 값	스타일명
1	narrative	서술형
2	protocol	프로토콜형
3	data-driven	데이터형
4	meeting	회의록형
5	troubleshooting	문제해결형
6	decision	의사결정형
7	study-log	학습기록형
8	progress	진척보고형
9	literature	문헌정리형
sections의 title은 스타일별 기본 섹션명을 사용 (위 그룹 C 테이블 참조)
생략한 섹션은 sections에서 제외
font, signature.점검자 생략 시 기본값 적용
파일명 규칙: 연구노트_[YYYY-MM-DD]_[순번].{ext} (사용자 지정 시 그것을 따름)
여러 건 요청 시 각각 개별 파일로 생성
스크립트 구조
skills/k-research-note/scripts/
├── generate_note.py         ← CLI 엔트리 (JSON → 문서 생성)
├── data_processor.py        ← 데이터 파일 파싱/변환 (--data 시 자동 호출)
├── research_note_builder.py ← 문서 조립 (내부 사용)
├── docx_builder.py          ← DOCX 생성 (내부 사용)
└── pdf_builder.py           ← PDF 생성 (내부 사용)


디자인 규격(색상, 폰트, 머리글/바닥글 레이아웃)은 스크립트가 자동 처리한다.

주의사항
연구노트는 연구 수행의 1차 기록물이다. 제3자가 재현 가능한 수준으로 구체적으로 기술한다.
사용자 분야(실험/SW/설계/조사)에 맞게 용어와 세부 내용을 조정한다.
상세 작성 요령, 법적 근거, 과제 평가 연관성은 references/research-note-guide.md 참조.
Weekly Installs
14
Repository
ujon/skills
GitHub Stars
1
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn