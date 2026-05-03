---
rating: ⭐⭐
title: outline-writer
url: https://skills.sh/hoangvantuan/claude-plugin/outline-writer
---

# outline-writer

skills/hoangvantuan/claude-plugin/outline-writer
outline-writer
Installation
$ npx skills add https://github.com/hoangvantuan/claude-plugin --skill outline-writer
SKILL.md
Outline Writer — Content Analysis & Outline Generator

Tạo professional outline từ content input. Hỗ trợ nhiều output types: presentation slides, blog post, documentation. Vietnamese default.

Output Folder Structure
{CWD}/outline-writer/
└── {slug}-{YYMMDD-HHmm}/
    ├── outline.md
    ├── content-map.md
    ├── coverage-report.md
    └── research-notes.md (nếu có research)


Naming rules:

{slug}: kebab-case từ topic chính (max 30 chars)
{YYMMDD-HHmm}: timestamp lúc tạo folder
Output Type Routing

Mỗi output type dùng subset steps và references khác nhau:

Step	Presentation	Blog/Doc
Step 1: Config	Hỏi 4 câu + Step 1A (Audience/Framework)	Hỏi 4 câu (skip Audience/Framework)
Step 1B: Mental Model	Từ audience type đã chọn	Suy luận từ topic + context
Step 2: Research	Tùy user chọn	Tùy user chọn
Step 3: Thesis	Bắt buộc	Bắt buộc
Step 4: Tạo outline	Load: framework-mapping + outline-structure + detail-levels	Load: outline-structure (Content Principles) + detail-levels
Step 4 - Content Map	Load: content-map-rules	Load: content-map-rules
Step 4 - Reports	Load: report-format	Load: report-format

Blog/Doc không dùng: framework-mapping, slide types, visual rhythm, audience adjustments. Sắp xếp logic: Introduction → Body sections (clustered) → Conclusion.

Step 1: Tiếp nhận nội dung & Cấu hình
Đọc input từ user: text trực tiếp hoặc file path (.md, .txt, .pdf)
Nếu input là file path, đọc nội dung file
Phân tích sơ bộ: topic, length, complexity
Hỏi user bằng AskUserQuestion (4 câu hỏi trong 1 lần):

Câu hỏi 1 - Output type (header: "Output type"):

"Presentation slides" - Outline cho slide deck (tiếp tục hỏi audience & framework ở Step 1A)
"Blog post" - Outline cho bài viết blog
"Documentation/Report" - Outline cho tài liệu/báo cáo

Câu hỏi 2 - Mức độ chi tiết (header: "Detail level"):

"L1 - Tổng quan" - Chỉ ý chính, bullet ngắn gọn
"L2 - Cân bằng" - Ý chính + giải thích + ví dụ minh họa
"L3 - Chi tiết" - Đầy đủ nội dung, deep dive, code examples

Câu hỏi 3 - Ngôn ngữ (header: "Language"):

"Tiếng Việt" - Toàn bộ nội dung tiếng Việt (Recommended)
"English" - Toàn bộ nội dung tiếng Anh
"Song ngữ" - Title tiếng Anh, body tiếng Việt

Câu hỏi 4 - Research bổ sung (header: "Research"):

"Chỉ dùng source" - 100% từ nội dung đầu vào, không tìm thêm
"Research thêm" - Tìm thêm data, statistics, examples từ web
"Auto" - Tự động: research nếu source ít thông tin, skip nếu đủ

Logic Recommended cho câu hỏi 4: Source < 500 words HOẶC thiếu data/metrics → recommend "Research thêm". Source >= 500 words VÀ đủ data → recommend "Chỉ dùng source".

Nếu output_type = "Presentation slides" → tiếp Step 1A. Ngược lại → tiếp Step 1B.
Step 1A: Audience & Framework (Chỉ khi Presentation)

Hỏi user bằng AskUserQuestion:

Câu hỏi 1 — Content type (header: "Content type"):

"Hướng dẫn/Giáo dục" - Giải thích khái niệm, tutorial (Gagné + scaffolding)
"Business/Báo cáo" - Phân tích, đề xuất, báo cáo (Pyramid Principle)
"Thuyết phục/Pitch" - Bán ý tưởng, pitch sản phẩm (PAS + Sparkline)
"Technical/Process" - Quy trình, kiến trúc, so sánh kỹ thuật (SCR + step-by-step)

Câu hỏi 2 — Audience (header: "Audience"):

"Executive/Decision maker" - C-level, cần bottom-line upfront, metrics, ngắn gọn
"Technical team" - Engineers, developers — jargon OK, chi tiết kỹ thuật
"Mixed/General" - Đa dạng trình độ — cần giải thích thuật ngữ, ví dụ cụ thể
"Workshop/Hands-on" - Đào tạo thực hành — interactive, knowledge checks

Câu hỏi 3 — Framework (header: "Framework", chỉ hỏi khi content type = "Business/Báo cáo"):

"Pyramid Principle" - Kết luận trước, supporting arguments sau (Recommended khi audience = Mixed)
"SCQA" - Situation → Complication → Question → Answer (Recommended khi audience = Executive)
Step 1B: Audience Mental Model (Tự động — không hỏi user)

Áp dụng cho mọi output type. Với presentation: suy luận từ audience type đã chọn. Với blog/doc: suy luận từ topic + context.

Tự suy luận và giữ trong context:

AUDIENCE MENTAL MODEL:
- Prior knowledge: [Audience đã biết gì về topic này?]
- Existing beliefs: [Họ đang tin gì? — có thể đúng hoặc sai]
- Knowledge gap: [Họ cần biết thêm gì?]
- Belief shift: [Sau outline, họ cần thay đổi suy nghĩ gì?]
- Resistance point: [Rào cản lớn nhất khi tiếp nhận nội dung?]


Cách Mental Model ảnh hưởng outline:

Audience đã tin X (sai) → cần section phá vỡ giả định trước khi trình bày thesis
Audience thiếu kiến thức Y → cần scaffolding từ cái đã biết sang cái mới
Audience kháng cự thay đổi → cần evidence mạnh trước kết luận, không kết luận trước
Knowledge gap nhỏ → có thể dùng L1, gap lớn → cần L2-L3
Step 2: Research bổ sung (Optional)

Quyết định dựa trên câu hỏi Research ở Step 1:

User chọn "Research thêm" → luôn chạy
User chọn "Auto" → chạy NẾU source < 500 words HOẶC thiếu data/metrics
User chọn "Chỉ dùng source" → SKIP hoàn toàn

Process:

Extract 3-5 topic keywords từ source
Tạo 2-3 search queries: "{topic}" statistics data {năm}, "{topic}" trends insights, "{topic}" examples best practices
Chạy WebSearch cho mỗi query
Extract findings relevant: statistics, data points, examples, quotes
Lưu kết quả vào {CWD}/{output_folder}/research-notes.md
Append selected items vào Content Analysis Map với prefix [R]
Thông báo user: "Research xong: X data points, Y insights. Đã lưu tại research-notes.md"

Quy tắc: Chỉ thông tin factual có nguồn. Ưu tiên: số liệu > xu hướng > ví dụ. KHÔNG thay thế source, chỉ BỔ SUNG. Max 10 items.

Step 3: Thesis Extraction (Bắt buộc mọi output type)

Bước quan trọng nhất — xác định core message trước khi tạo outline.

Đọc toàn bộ source (và research notes nếu có)
Trả lời: "Nếu audience chỉ nhớ 1 điều duy nhất từ nội dung này, đó là gì?" → Thesis
Trả lời: "3 arguments/evidence nào mạnh nhất chứng minh thesis?" → Key Arguments
Trả lời: "Audience cần thay đổi gì sau khi tiếp nhận nội dung?" → Intended Transformation:
"không biết X" → "hiểu X" (educate)
"tin X sai" → "tin X đúng" (persuade)
"không hành động" → "hành động Y" (activate)
Giữ trong context, KHÔNG show cho user riêng — thesis sẽ xuất hiện trong outline và quality report

Thesis format (internal):

=== THESIS ===
Core message: [1 câu assertion — KHÔNG phải topic label]
Key arguments:
  1. [Argument 1]
  2. [Argument 2]
  3. [Argument 3]
Intended transformation: [educate/persuade/activate] — [mô tả cụ thể]
=== END THESIS ===


Quy tắc Thesis:

Thesis PHẢI là assertion (nhận định có thể đúng/sai), KHÔNG phải topic label
SAI: "Phương pháp Agile trong phát triển phần mềm"
ĐÚNG: "Agile giúp giảm 60% thời gian delivery nhưng đòi hỏi thay đổi văn hóa toàn tổ chức"
Thesis phải kiểm chứng được bằng evidence từ source
Key arguments PHẢI có evidence trong source hoặc research
Nếu source không có thesis rõ ràng (VD: tài liệu kỹ thuật thuần túy) → thesis = mục tiêu chính mà audience cần đạt được
Step 4: Phân tích nội dung & Tạo outline
Tạo output folder: {CWD}/outline-writer/{slug}-{YYMMDD-HHmm}/
Đọc references cần thiết (xem Output Type Routing ở trên)
Framework selection (presentation only): áp dụng framework tương ứng content type (xem framework-mapping). Nếu audience = "Workshop", override sang Gagné
Content Analysis Map: Đọc content-map-rules. Parse source → extract topics → map relationships → assign priority → link to Thesis. Lưu {CWD}/{output_folder}/content-map.md
Phân tích nội dung theo detail-levels + audience adjustments (xem outline-structure) + Audience Mental Model
Tạo outline xây quanh Thesis: Opening giới thiệu core message > Body chứng minh bằng Key Arguments > Closing khẳng định thesis + CTA. Áp dụng Cognitive Sequencing + Narrative Arc + Content Principles (xem outline-structure). Cross-check Content Analysis Map: mọi must topics phải xuất hiện, mọi Key Arguments phải có evidence
Lưu outline ra {CWD}/{output_folder}/outline.md với YAML frontmatter (xem format trong report-format)
Hiển thị outline cho user review
Coverage & Quality Report: Đọc report-format. Generate {CWD}/{output_folder}/coverage-report.md
Feedback loop: Hỏi "Outline OK?" (AskUserQuestion, header: "Outline review"):
"OK, tiếp tục" - Chấp nhận outline
"Chỉnh sửa" - User mô tả thay đổi → cập nhật → hỏi lại
Khi approved, thông báo: "Outline xong tại {CWD}/{output_folder}/outline.md."

Nguyên lý cốt lõi: Outline tốt = tấm bản đồ đi từ điểm A (audience chưa biết) đến điểm B (insight cốt lõi), KHÔNG phải danh mục liệt kê tất cả những gì source nói.

Weekly Installs
26
Repository
hoangvantuan/cl…e-plugin
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn