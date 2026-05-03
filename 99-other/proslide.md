---
rating: ⭐⭐⭐⭐⭐
title: proslide
url: https://skills.sh/hoangvantuan/claude-plugin/proslide
---

# proslide

skills/hoangvantuan/claude-plugin/proslide
proslide
Installation
$ npx skills add https://github.com/hoangvantuan/claude-plugin --skill proslide
SKILL.md
ProSlide - Professional Slide Generator

Tạo professional text-only slides từ content input. Vietnamese default. Activate slidev skill (built-in, cùng context) cho Slidev Markdown generation + PDF export.

Output Folder Structure

Mỗi lần tạo presentation, output được lưu trong folder có cấu trúc:

output/
└── {slug}-{YYMMDD-HHmm}/
    ├── outline.md
    ├── content-map.md
    ├── coverage-report.md
    ├── research-notes.md
    └── slides/
        └── {slug}-{theme-name}/    # Slidev project
            ├── package.json
            ├── slides.md
            └── dist/               # After export (gitignored)
                └── {slug}.pdf


Naming rules:

{slug}: kebab-case từ topic chính (max 30 chars)

{YYMMDD-HHmm}: timestamp lúc tạo folder

{theme-name}: tên Slidev theme đã chọn (VD: default, seriph, apple-basic)

Khi reuse outline để generate thêm slide mới, folder mới được thêm vào slides/ của folder đã có

Step 0: Detect Mode (New / Reuse)

Kiểm tra input từ user:

Nếu user chỉ vào folder output đã có (chứa outline.md) → Reuse mode

Nếu user cung cấp nội dung mới (text, file path) → New mode

Nếu user nói "dùng lại outline", "reuse", "tạo thêm slide" + chỉ folder → Reuse mode

Reuse mode → nhảy thẳng tới Step 2.5 (skip Step 1 & 2)

New mode → tiếp tục Step 1

Step 1: Tiếp nhận nội dung & Cấu hình
Đọc input từ user: text trực tiếp hoặc file path (.md, .txt, .pdf)
Nếu input là file path, đọc nội dung file
Phân tích sơ bộ: topic, length, complexity
Hỏi user bằng AskUserQuestion (4 câu hỏi trong 1 lần):

Câu hỏi 1 - Loại nội dung (header: "Content type"):

"Hướng dẫn/Giáo dục" - Giải thích khái niệm, tutorial, hướng dẫn học (Gagné + scaffolding)

"Business/Báo cáo" - Phân tích, đề xuất, báo cáo kết quả (Pyramid Principle)

"Thuyết phục/Pitch" - Bán ý tưởng, pitch sản phẩm, proposal (PAS + Sparkline)

"Technical/Process" - Quy trình, kiến trúc, hệ thống, so sánh kỹ thuật (SCR + step-by-step)

Câu hỏi 2 - Mức độ chi tiết (header: "Detail level"):

"L1 - Tổng quan" - Chỉ ý chính, bullet ngắn gọn (5+ slides)

"L2 - Cân bằng" - Ý chính + giải thích + ví dụ minh họa (10+ slides)

"L3 - Chi tiết" - Đầy đủ nội dung, deep dive, code examples (18+ slides)

Câu hỏi 3 - Ngôn ngữ (header: "Language"):

"Tiếng Việt" - Toàn bộ nội dung tiếng Việt (Recommended)

"English" - Toàn bộ nội dung tiếng Anh

"Song ngữ" - Title tiếng Anh, body tiếng Việt (phù hợp technical/academic)

Câu hỏi 4 - Research bổ sung (header: "Research"):

"Chỉ dùng source" - Tạo slide 100% từ nội dung đầu vào, không tìm thêm

"Research thêm" - Tìm thêm data, statistics, examples từ web để bổ sung slide

"Auto" - Tự động: research nếu source ít thông tin (<500 words hoặc thiếu data/metrics), skip nếu đủ

Logic đánh dấu Recommended cho câu hỏi 4:

Nếu source < 500 words HOẶC source chỉ có bullet points không context HOẶC thiếu data/metrics/examples → đánh dấu "Research thêm" là (Recommended)

Nếu source >= 500 words VÀ có đầy đủ data/context → đánh dấu "Chỉ dùng source" là (Recommended)

Step 1.1: Audience & Framework Selection

Chạy ngay sau Step 1. Hỏi user bằng AskUserQuestion (1-2 câu hỏi tùy content type):

Câu hỏi 1 — Audience (header: "Audience", luôn hỏi):

"Executive/Decision maker" - C-level, board — cần bottom-line upfront, metrics, ngắn gọn
"Technical team" - Engineers, developers — jargon OK, code OK, chi tiết kỹ thuật
"Mixed/General" - Đa dạng trình độ — cần giải thích thuật ngữ, ví dụ cụ thể
"Workshop/Hands-on" - Đào tạo thực hành — interactive, knowledge checks, bài tập

Câu hỏi 2 — Framework (header: "Framework", chỉ hỏi khi content type = "Business/Báo cáo"):

"Pyramid Principle" - Kết luận/đề xuất trước, rồi supporting arguments (Recommended khi audience = Mixed/General)
"SCQA" - Situation → Complication → Question → Answer — framing vấn đề trước khi answer (Recommended khi audience = Executive)

Logic đánh dấu Recommended cho câu hỏi 2:

Nếu audience = Executive/Decision maker → recommend SCQA
Nếu audience = Technical/Mixed/Workshop → recommend Pyramid Principle

Audience ảnh hưởng đến Step 2:

Audience	Ảnh hưởng
Executive	Ưu tiên metric slides, bottom-line upfront, force L1-L2 nếu user chọn L3 thì warning
Technical	Sequential IA, jargon OK, code examples ưu tiên, L2-L3 phù hợp
Mixed	Thêm definition cho thuật ngữ, ví dụ concrete bắt buộc mỗi concept
Workshop	Force Gagné framework bất kể content type, thêm knowledge check slides (Gagné Event 6)
Step 1.5: Research bổ sung (Optional)

Chạy sau Step 1, trước Step 2. Quyết định dựa trên câu hỏi 4 ở Step 1.

Khi nào chạy:

User chọn "Research thêm" → luôn chạy

User chọn "Auto" → chạy NẾU source < 500 words HOẶC source thiếu data/metrics/examples cụ thể

User chọn "Chỉ dùng source" → SKIP hoàn toàn, nhảy tới Step 2

Process:

Extract 3-5 topic keywords từ source input (dựa trên content type đã chọn)

Tạo 2-3 search queries phù hợp:

Query 1: "{topic chính}" statistics data {năm hiện tại} (tìm số liệu mới nhất)

Query 2: "{topic chính}" trends insights (tìm xu hướng, insights)

Query 3: "{topic chính}" examples best practices (tìm ví dụ, case studies)

Chạy WebSearch cho mỗi query

Extract findings relevant: statistics, data points, examples, quotes, trends

Lưu kết quả vào {output_folder}/research-notes.md theo format:

# Research Notes — [Topic]

## Search Queries

1. [query 1]
2. [query 2]
3. [query 3]

## Findings

### Statistics & Data

- [stat 1] — Source: [url/name]
- [stat 2] — Source: [url/name]

### Trends & Insights

- [insight 1]
- [insight 2]

### Examples & Case Studies

- [example 1]
- [example 2]

## Selected for Slides

Items below sẽ được đưa vào Content Map với tag [R]:

1. [item] — lý do chọn
2. [item] — lý do chọn

Append selected items vào Content Map (Step 2) với prefix [R] để phân biệt source gốc vs researched
Thông báo user: "Research xong: tìm thấy X data points, Y insights. Đã lưu tại research-notes.md"

Quy tắc research:

Chỉ lấy thông tin factual, có nguồn rõ ràng

Ưu tiên: số liệu cụ thể > xu hướng > ví dụ > quotes

KHÔNG thay thế nội dung source, chỉ BỔ SUNG

Max 10 items đưa vào Content Map (tránh overwhelming)

Research items trong outline phải ghi rõ "(Nguồn: research)" trong speaker notes hoặc content

Visual Patterns per Content Type

Khi tạo slides, áp dụng visual patterns phù hợp với content type đã chọn:

Content Type	Visual Patterns	Recommended Slide Types
Hướng dẫn/Giáo dục	Numbered step indicators, before/after comparison, warm decorations	content, comparison, statement, quote (expert quotes)
Business/Báo cáo	Accent bars, data callout slides, conservative decorations	content, metric, comparison, table, summary
Thuyết phục/Pitch	Bold statement slides, high contrast, CTA emphasis	statement (30%+), metric, quote (social proof), content, cta
Technical/Process	Code blocks, process flow indicators, Mermaid diagrams	content, comparison, code, diagram, table, transition
Auto Theme Recommendation

Dựa trên content type, gợi ý Slidev theme (user có quyền chọn khác hoặc nhập tên theme bất kỳ):

Content Type	Primary Recommendation	Secondary
Hướng dẫn/Giáo dục	seriph	default
Business/Báo cáo	default	apple-basic
Thuyết phục/Pitch	apple-basic	seriph
Technical/Process	default	seriph
Slidev Theme List

Danh sách themes chính thức và community phổ biến, hiển thị cho user khi chọn:

Official themes:

Theme	Package	Mô tả
default	@slidev/theme-default	Minimalist, light/dark
seriph	@slidev/theme-seriph	Serif-based formal, light/dark
apple-basic	@slidev/theme-apple-basic	Keynote-inspired, light/dark
bricks	@slidev/theme-bricks	Playful blocks, light
shibainu	@slidev/theme-shibainu	Cute dark theme

Community themes (phổ biến):

Theme	Package	Mô tả
geist	slidev-theme-geist	Vercel design system, light/dark
academic	slidev-theme-academic	Formal academic, light/dark
dracula	slidev-theme-dracula	Vibrant dark theme

User cũng có thể nhập tên bất kỳ Slidev theme từ npm.

Step 2: Phân tích nội dung & Tạo outline (New mode)

Tạo output folder: output/{slug}-{YYMMDD-HHmm}/ và subfolder slides/

Đọc references/outline-rules.md (relative to this skill folder) để nắm quy tắc outline

Áp dụng framework tương ứng với content type đã chọn ở Step 1. Nếu content type = "Business/Báo cáo", dùng framework user chọn ở Step 1.1 (Pyramid hoặc SCQA). Nếu audience = "Workshop", override sang Gagné bất kể content type. (Xem Content Type → Framework Mapping + SCQA Framework + Audience-Aware Adjustments trong outline-rules.md)

Content Map (xem "Content Map Rules" trong outline-rules.md):

Parse source → silent clustering (nhóm topics tương đồng thành section buckets) → extract topics → assign priority (must/should/nice) theo detail level

Clustering tự động: nhóm topics "naturally discuss together" thành sections, tránh overlap và topics liên quan nằm xa nhau trong outline

Nếu Step 1.5 đã chạy → append research items vào Content Map với prefix [R] (xem outline-rules.md)

Lưu Content Map ra file {output_folder}/content-map.md

Phân tích nội dung theo detail level đã chọn + audience-aware adjustments (xem Detail Level Mapping + Content Selection Criteria + Audience-Aware Adjustments trong outline-rules.md)

Tạo outline theo cấu trúc bắt buộc: Opening > Body > Closing. Áp dụng Cognitive Sequencing (simple→complex, activate prior knowledge) và Narrative Arc tương ứng framework đã chọn (xem Cognitive Sequencing Rules + Narrative Arc per Framework trong outline-rules.md). Cross-check với Content Map: mọi must topics phải xuất hiện, should/nice theo threshold

Lưu outline ra file {output_folder}/outline.md với metadata header (xem Outline File Format trong outline-rules.md)

Hiển thị outline cho user review (numbered list với slide titles + brief content description)

Coverage Report (xem "Coverage Report Rules" trong outline-rules.md):

Generate file {output_folder}/coverage-report.md mapping source topics → slides + omission justification

Thông báo cho user: tóm tắt 1 dòng coverage % + mention report file path

Feedback loop: Hỏi user "Outline OK? Bạn có muốn chỉnh sửa gì không?" bằng AskUserQuestion (header: "Outline review"):

"OK, tiếp tục" - Chấp nhận outline, chuyển sang chọn theme

"Chỉnh sửa" - User sẽ mô tả thay đổi → cập nhật outline file + re-check coverage → show lại → hỏi lại

Step 2.5: Reuse mode (khi đã có outline)
Đọc {output_folder}/outline.md — parse metadata header để lấy: content_type, detail_level, language, slug
Hiển thị tóm tắt cho user: "Reuse outline: {title}, {detail_level}, {language}, {N} slides"
Tiếp tục chọn theme ở Step 2.6
Step 2.6: Chọn Slidev theme (cả New và Reuse mode)
Hiển thị bảng Slidev Theme List (xem section ở trên)
Kiểm tra {output_folder}/slides/ xem đã có Slidev project folder nào chưa → show user "(đã tạo)" bên cạnh theme đã dùng
Hỏi user bằng AskUserQuestion (header: "Theme"): "Chọn Slidev theme:" + đánh dấu recommended theme dựa trên bảng Auto Theme Recommendation + cho phép nhập tên theme khác qua "Other"
Step 3: Tạo slide (Slidev)

Xác định theme package name:

Official themes: @slidev/theme-{name} (VD: @slidev/theme-seriph)

Community themes: slidev-theme-{name} (VD: slidev-theme-geist)

Nếu user nhập custom name → dùng nguyên tên

Đọc references/slide-templates.md (relative to this skill folder) để nắm Slidev Markdown patterns cho từng slide type

Đọc outline từ {output_folder}/outline.md (nếu Reuse mode) hoặc từ context (nếu vừa tạo)

Activate slidev skill trong cùng agent context. Cung cấp:

Headmatter config:

theme: { theme-name }
fonts:
  sans: Tahoma
  serif: Arial
  mono: Fira Code
  provider: none


Layout mapping table cho mỗi slide type:

Slide Type	Slidev Layout
title	cover
agenda	default
content	default
comparison	two-cols-header
comparison-simple	two-cols
summary	default
cta	end
transition	section
statement	statement
metric	fact
quote	quote
table	default
diagram	default
code	default

Nội dung từng slide theo outline (title, body content, slide type → layout)

Slidev Markdown templates từ references/slide-templates.md

Vietnamese fonts requirement: Tahoma, Arial, sans-serif qua fonts config

Output path: {output_folder}/slides/{slug}-{theme-name}/

Slidev skill tạo Slidev project:

package.json:

{
  "name": "{slug}-{theme-name}",
  "private": true,
  "scripts": {
    "dev": "slidev",
    "build": "slidev build",
    "export": "slidev export --output dist/{slug}.pdf --timeout 60000"
  },
  "dependencies": {
    "@slidev/cli": "latest",
    "{theme-package}": "latest"
  },
  "devDependencies": {
    "playwright-chromium": "latest"
  }
}


slides.md: Headmatter + all slides theo Slidev Markdown format

Install dependencies: pnpm install trong Slidev project folder

Export PDF: npx slidev export --output dist/{slug}.pdf --timeout 60000

Thông báo output:

Slidev project path

PDF path (nếu export thành công)

Output folder path (nhắc user có thể reuse outline: /proslide + chỉ folder path)

Hướng dẫn: cd {project-path} && pnpm dev để xem slides trong browser

Slidev Constraints (CRITICAL)

Khi activate slidev skill, PHẢI tuân thủ các constraints sau:

Vietnamese fonts: Dùng Tahoma, Arial, sans-serif qua fonts config trong headmatter với provider: none (system fonts, không fetch từ Google Fonts). KHÔNG dùng Impact, Courier New (Vietnamese rendering kém)

Text-only: Không dùng image layouts, không embed images. Chỉ text, bullets, code blocks

Speaker notes: Dùng HTML comments <!-- notes --> sau content mỗi slide

Code blocks: Dùng native Markdown fenced blocks với language tag (python, javascript, etc.). Slidev tự động syntax highlight. Max 10-15 dòng/slide. Dùng line highlighting {2,3} để nhấn mạnh dòng quan trọng, hoặc click-based highlighting {1|3-4|all} để walkthrough từng phần (xem templates trong references/slide-templates.md)

Nested lists: Slidev Markdown hỗ trợ nested lists tốt (indent 2 spaces). Dùng thoải mái cho L2/L3 sub-bullets

Max content per slide: Tuân theo rules từ outline-rules.md:

L1: 2-3 bullets, <8 words/bullet

L2: 3-5 bullets + 1-2 sub-bullets

L3: 3-5 bullets + 2-3 sub-bullets, max 100 words/slide

Slide separator: Dùng --- giữa các slides (Slidev convention)

Layout front matter: Mỗi slide PHẢI có layout specification trong front matter block

Projector contrast: Đảm bảo text/background contrast ratio >= 4.5:1 (WCAG AA). Theme đã chọn sẽ handle phần lớn, nhưng vẫn cần verify

v-click progressive disclosure: Dùng <v-clicks> wrapper cho L2/L3 bullet lists để reveal từng point. L1 KHÔNG dùng v-click. Xem patterns chi tiết trong references/slide-templates.md → "Advanced Features"

Mermaid diagrams: Built-in, dùng cho Technical/Process slides. Cú pháp: ```mermaid code block. Max 8-10 nodes per diagram. Text-based → phù hợp text-only constraint

Slide transitions: Dùng transition: fade hoặc slide-left trong frontmatter. Đặt global transition trong headmatter, override per-slide chỉ khi cần nhấn mạnh

v-mark text emphasis: Dùng <span v-mark.highlight> cho key terms. Max 1-2 per slide. Click-triggered với v-mark="N"

Shiki Magic Move: Code morphing animation cho L2/L3 technical. Cú pháp: magic-move ````. Max 3-4 steps per block

Inline code trên dark slides: Slides có nền tối (layout: cover, layout: end, hoặc dark theme) thường render inline code (backtick) với màu tối trên nền tối → không đọc được. Rule: Sau khi generate slides.md, scan tất cả slides có layout: cover, layout: end, hoặc layout: section. Nếu slide chứa inline code (backtick `), thêm scoped <style> block cuối slide (trước speaker notes nếu có):

<style>
code {
  color: #e2e8f0 !important;
  background: rgba(255,255,255,0.15) !important;
}
</style>


Scoped style chỉ áp dụng cho slide hiện tại (Slidev convention). Không thêm nếu slide không chứa inline code.

Important Notes

Chỉ tạo text-only slides, không hình ảnh

Vietnamese fonts: Tahoma, Arial, sans-serif (qua Slidev fonts config, provider: none)

Chi tiết quy tắc outline: xem references/outline-rules.md

Slidev Markdown templates cho slide types: xem references/slide-templates.md

Theme do user chọn từ Slidev ecosystem, không cần custom CSS

Slidev project có thể chạy local bằng pnpm dev để preview slides trong browser

PDF export dùng Playwright (cần playwright-chromium dependency)

Weekly Installs
12
Repository
hoangvantuan/cl…e-plugin
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn