---
title: hwpx
url: https://skills.sh/ujon/skills/hwpx
---

# hwpx

skills/ujon/skills/hwpx
hwpx
Installation
$ npx skills add https://github.com/ujon/skills --skill hwpx
SKILL.md
HWPX 문서 생성·편집·분석 스킬
개요

HWPX는 한컴오피스 한글의 개방형 문서 포맷으로, OWPML(Open Word-Processor Markup Language, KS X 6101) 표준을 따른다. ZIP 아카이브 안에 XML 파일들이 들어있어 프로그래밍적 조작이 가능하다.

이 스킬은 Python 표준 라이브러리(xml.etree, zipfile) 만으로 동작하며, 외부 의존성이 없다.

파일 포맷
포맷	확장자	특징
HWP (레거시)	.hwp	바이너리 포맷, 직접 생성 어려움
HWPX (개방형)	.hwpx	ZIP + XML, 프로그래밍 생성 가능

이 스킬은 HWPX 포맷을 기본으로 사용한다. 사용자가 .hwp를 요청해도 HWPX로 생성하며, HWPX는 한컴오피스 2018 이상에서 기본 지원한다.

Quick Reference
작업	방법
문서 생성	scripts/hwpx_builder.py — HwpxBuilder 클래스
기존 HWPX 읽기	scripts/hwpx_reader.py — HwpxReader 클래스
기존 HWPX 편집	scripts/hwpx_reader.py — unpack() → 편집 → repack()
출력 위치	./ (현재 프로젝트 디렉토리 기준)
스크립트 위치
skills/hwpx/scripts/
├── hwpx_builder.py    ← 문서 생성 (HwpxBuilder 클래스)
└── hwpx_reader.py     ← 문서 읽기/편집 (HwpxReader, unpack, repack)


설치 불필요. Python 3.9+ 표준 라이브러리만 사용한다.

문서 생성 — HwpxBuilder
기본 사용법
import sys; sys.path.insert(0, "skills/hwpx/scripts")
from hwpx_builder import HwpxBuilder

doc = HwpxBuilder()
doc.add_heading("문서 제목", level=1)
doc.add_paragraph("본문 텍스트입니다.")
doc.add_table([
    ["항목", "내용", "비고"],
    ["첫 번째", "값", "정상"],
])
doc.save("./문서.hwpx")

API
메서드	설명
add_heading(text, level=1)	제목 추가 (level 1~3)
add_paragraph(text, char_style=0, para_style=0)	문단 추가
add_empty_line()	빈 줄
add_table(rows, header=True)	테이블 (첫 행 헤더)
add_multi_run([(text, char_style), ...], para_style=0)	한 문단 여러 스타일
add_raw_xml(xml)	section0.xml에 직접 XML 삽입
add_char_style(id, font_size_pt, bold, italic, underline, color, font_index)	글자 스타일 정의
add_para_style(id, align, line_spacing, spacing_before, spacing_after, margin_left, indent)	문단 스타일 정의
save(path)	HWPX 저장 (디렉토리 자동 생성)
빌트인 스타일
글자 스타일 (charPr)
id	설명	크기	속성
0	본문	11pt	-
1	제목1	18pt	Bold
2	제목2	14pt	Bold
3	제목3	12pt	Bold
4	테이블 헤더	11pt	Bold
문단 스타일 (paraPr)
id	설명	정렬	줄간격
0	본문	LEFT	160%
1	제목1	CENTER	160%
2	제목2	LEFT	160%
3	제목3	LEFT	160%
커스텀 스타일 추가
doc = HwpxBuilder()

# 빨간 볼드 14pt, 가운데 정렬
doc.add_char_style(id=10, font_size_pt=14, bold=True, color="FF0000")
doc.add_para_style(id=10, align="CENTER", line_spacing=180)

doc.add_paragraph("커스텀 스타일 텍스트", char_style=10, para_style=10)

페이지 설정
# 기본값: A4, 여백 약 2.54cm
doc = HwpxBuilder(
    page_width=59528,     # A4 (HU)
    page_height=84188,
    margin_left=8504,
    margin_right=8504,
    margin_top=5668,
    margin_bottom=4252,
)

# 글꼴 변경
doc = HwpxBuilder(fonts=["나눔고딕", "맑은 고딕"])

복합 문서 예시
import sys; sys.path.insert(0, "skills/hwpx/scripts")
from hwpx_builder import HwpxBuilder

doc = HwpxBuilder()

# 커스텀 스타일: 파란 소제목
doc.add_char_style(id=10, font_size_pt=13, bold=True, color="2E5A88")
doc.add_para_style(id=10, spacing_before=200, spacing_after=100)

# 헤더
doc.add_heading("연 구 노 트", level=1)
doc.add_empty_line()

# 기본 정보 테이블
doc.add_table([
    ["과제명", "AI 기반 스마트 제조 최적화"],
    ["기록자", "홍길동"],
    ["작성일자", "2026-03-13"],
], header=False)
doc.add_empty_line()

# 본문 섹션
doc.add_paragraph("1. 연구 목적", char_style=10, para_style=10)
doc.add_paragraph("본 연구는 제조 공정의 불량률을 감소시키기 위해...")
doc.add_empty_line()

# 한 문단에 볼드 + 일반 텍스트 혼합
doc.add_multi_run([
    ("결과: ", 4),     # 볼드
    ("정상 동작 확인", 0),  # 일반
])

doc.save("./연구노트_2026-03-13.hwpx")

문서 읽기 — HwpxReader
import sys; sys.path.insert(0, "skills/hwpx/scripts")
from hwpx_reader import HwpxReader

reader = HwpxReader("./문서.hwpx")

# 텍스트 추출
print(reader.extract_text())

# ZIP 내 파일 목록
print(reader.list_files())

# XML 직접 확인
print(reader.get_xml("Contents/section0.xml"))

# 스타일 정보
print(reader.get_styles())

CLI
python skills/hwpx/scripts/hwpx_reader.py read document.hwpx

문서 편집 — unpack/repack

기존 HWPX 파일을 수정할 때는 unpack → 편집 → repack 패턴을 사용한다.

Python
import sys; sys.path.insert(0, "skills/hwpx/scripts")
from hwpx_reader import unpack, repack

# 1. 풀기 (linesegarray 자동 제거)
unpack("document.hwpx", "./tmp_edit")

# 2. XML 편집 (예: section0.xml 수정)
with open("./tmp_edit/Contents/section0.xml", "r") as f:
    xml = f.read()
xml = xml.replace("이전 텍스트", "새 텍스트")
with open("./tmp_edit/Contents/section0.xml", "w") as f:
    f.write(xml)

# 3. 재패키징
repack("./tmp_edit", "./edited.hwpx")

CLI
# 풀기
python skills/hwpx/scripts/hwpx_reader.py unpack document.hwpx ./tmp_edit

# ... XML 편집 ...

# 재패키징
python skills/hwpx/scripts/hwpx_reader.py repack ./tmp_edit ./edited.hwpx


주의: 편집 시 linesegarray 요소가 있으면 unpack()이 자동 제거한다. 레이아웃 캐시로 내용 변경 시 꼬임을 유발하기 때문이다.

OWPML 단위 체계
단위	변환
1 HU	1/7200 인치
1cm	2835 HU
1pt (글자)	charSz val = pt × 200
A4	59528 × 84188 HU

HwpxBuilder에서 상수로 제공: A4_WIDTH, A4_HEIGHT, HU_PER_CM, HU_PER_PT

다른 스킬과의 연동

이 스킬은 범용 HWPX 빌더로, 어떤 스킬에서든 HWPX 출력이 필요할 때 사용할 수 있다.

연동 패턴:

import sys; sys.path.insert(0, "skills/hwpx/scripts")
from hwpx_builder import HwpxBuilder

doc = HwpxBuilder()
# ... 호출 스킬의 구조에 맞게 빌드 ...
doc.save("./문서.hwpx")

docx 스킬: MS Word 문서 생성 → 해외/국제 표준
hwpx 스킬: 한컴 한글 문서 생성 → 한국 정부/공공기관 표준
사용자가 "한글로", "hwp로", "한컴으로" 등 명시하면 hwpx 스킬 사용
별도 지정 없으면 docx가 기본값 (호환성 우선)
주의사항
HWPX는 한컴오피스 2018+ 에서 기본 지원. 이전 버전 사용자에게는 호환성 안내 필요
mimetype 파일은 반드시 ZIP 내 첫 번째이며 비압축이어야 한다 → HwpxBuilder가 자동 처리
OWPML 네임스페이스를 정확히 지켜야 한다 → HwpxBuilder가 자동 처리
편집 시 linesegarray 제거 필수 → unpack()이 자동 처리
생성된 파일은 ./ (현재 디렉토리)에 저장
상세 OWPML XML 구조는 references/owpml-reference.md 참조
Weekly Installs
11
Repository
ujon/skills
GitHub Stars
1
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass