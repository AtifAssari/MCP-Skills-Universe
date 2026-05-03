---
title: van-tu-tu-training
url: https://skills.sh/hoangvantuan/claude-plugin/van-tu-tu-training
---

# van-tu-tu-training

skills/hoangvantuan/claude-plugin/van-tu-tu-training
van-tu-tu-training
Installation
$ npx skills add https://github.com/hoangvantuan/claude-plugin --skill van-tu-tu-training
SKILL.md
Văn-Tư-Tu Training Builder

"Văn nhi bất tư tắc võng, tư nhi bất học tắc đãi." (Học mà không suy ngẫm thì vô nghĩa, suy ngẫm mà không thực hành thì nguy.)

Đào tạo không phải là chuyển kiến thức từ sách vào đầu. Đào tạo là chuyển kiến thức qua đầu, vào tay, thành hành vi.

Skill xây dựng bộ tài liệu training theo mô hình Văn-Tư-Tu (Tam Tuệ Học / Śruta-Cintā-Bhāvanā) — framework 2.600 năm từ Phật giáo, ứng dụng vào đào tạo hiện đại.

Nguyên tắc cốt lõi

Mô hình Văn-Tư-Tu:

Giai đoạn	Tỷ lệ	Bản chất
Văn	10%	Tiếp nhận kiến thức — tinh gọn, chỉ giữ cái cần thiết
Tư	20%	Tiêu hoá kiến thức — đặt câu hỏi, liên hệ bản thân
Tu	70%	Sống với kiến thức — thực hành, đúc kết, chuyển hoá thành hành vi

5 nguyên tắc vàng:

Tu > Tư > Văn — 70% cho thực hành, không phải lý thuyết
1 module = 1 chủ đề = 1 chu trình Văn-Tư-Tu hoàn chỉnh
Module độc lập — bỏ bớt, thêm vào, đổi thứ tự đều không ảnh hưởng
Phương pháp theo cấp độ — Người mới cần yêu thương, người giỏi cần áp lực
Đúc kết là bắt buộc — Không đúc kết = không học
Lăng kính xuyên suốt

3 nguyên tắc áp dụng ở MỌI bước, không chỉ một bước cụ thể:

Lăng kính	Câu hỏi tự vấn mỗi khi quyết định
Nhân quả xa hơn gần	Thiết kế này tạo Quả gần tốt hay Quả xa tốt? Quick fix hôm nay có giết năng lực học dài hạn không?
Ba gốc hơn ba độc	Hoạt động này đẩy người học về Giác-Từ-Tĩnh hay Tham-Sân-Si? (Tham bằng cấp, Sân so sánh, Si copy đáp án)
Độc lập hơn hoàn chỉnh	Module này đứng một mình có giá trị không? Hay bắt buộc dính chùm với module khác mới dùng được?

Rule khi 2 lăng kính xung đột: Ưu tiên Nhân quả xa. Đào tạo là khoản đầu tư, không phải tiêu dùng.

Failure modes — 5 cái bẫy phải tránh

Khi thiết kế bộ tài liệu, chủ động kiểm tra không rơi vào 5 bẫy sau. Mỗi bẫy có triệu chứng + cách thoát.

Bẫy	Triệu chứng	Cách thoát
Văn phình to	Module Văn > 20 phút đọc / > 10 trang, nhiều khái niệm không dẫn tới Tư-Tu nào cụ thể	Cắt mọi đoạn không trả lời được câu "Bỏ đoạn này người học còn làm bài thực hành được không?"
Tu làm cho có	Bài thực hành chỉ là bài tập viết, không có hành động thực tế, không có AAR, không đo hành vi sau 30/60/90 ngày	Mỗi bài Tu phải có: hành động cụ thể + bằng chứng verify + câu hỏi đúc kết
Module đá nhau	Không học module trước không hiểu module sau, nhưng prerequisite không ghi rõ	Vẽ prerequisite map (bảng "Module → Phụ thuộc"). Nếu dính chùm >3 module → tách lại
Tóm tắt giả đúc kết	Đúc kết module chỉ là liệt kê lại 3 ý chính đã học	Tìm LÕI chi phối (bỏ đi thử, câu hỏi đệ quy). Nếu bỏ 1 ý mà cả module vẫn đứng được → ý đó chưa phải lõi
Tài liệu đẹp, hành vi không đổi	Survey cuối khoá điểm cao, nhưng sau 60 ngày tỷ lệ áp dụng < 30%	Kiểm tra lại Tu: có action rõ chưa? Có môi trường áp dụng không? Có follow-up không?

Quy tắc vàng: Sau khi draft xong module, đọc lại và tick từng bẫy. Dính bẫy nào → sửa bẫy đó trước khi qua module tiếp.

References index — Khi cần tra cứu gì, đọc file nào

Chỉ load reference khi thực sự cần cho bước đang làm. Không load tất cả cùng lúc.

Khi cần...	Đọc file
Tra triết lý nền (Tam Tuệ Học, Văn-Hoá, Gà-Đại Bàng, 2 chiều đi)	references/philosophy-foundation.md
Chuẩn đặt tên folder/file/link (kebab-case, zero-pad, relative link)	references/naming-convention.md
Tránh vỡ layout khi upload Google Docs (cấm kỵ, element OK)	references/gdocs-compatibility.md
Kiến trúc modular, tier system, folder structure	references/modular-architecture.md
Tỷ lệ Văn-Tư-Tu theo loại kiến thức / cấp độ người học	references/ratio-adjustment.md
Xây Training Brief 1 trang (Bước 1)	references/template-training-brief.md
Viết phần Văn — kiến thức nền 10%	references/template-van.md
Viết phần Tư — suy tư, phản chiếu 20%	references/template-tu-suy-tu.md
Viết phần Tu — thực hành, chuyển hoá 70%	references/template-tu-thuc-hanh.md
Viết phần Đánh giá (AAR, rubric, survey, follow-up 30-60-90)	references/template-danh-gia.md
Xây facilitator hub (lịch, buddy pairs, phản biện)	references/template-facilitator-hub.md
Chuẩn đặt tên & liên kết

Tuyệt đối tuân thủ chuẩn trong references/naming-convention.md khi tạo bộ tài liệu:

Folder/file: kebab-case, tiếng Việt không dấu, zero-pad 2 chữ số (01-, 02-). Ví dụ: module-01-nen-tang-feedback/, cau-hoi-phan-chieu.md.
Phase folder cố định: 01-van/, 02-tu-suy-tu/, 03-tu-thuc-hanh/, 04-danh-gia/.
Folder meta prefix _: _facilitator-hub/, _danh-gia-khoa/.
Link: luôn markdown + relative path — [Module 2](../module-02-slug/README.md). Không đường dẫn tuyệt đối, không text trần.
README mỗi module bắt buộc link: tổng quan khoá, 4 phase, prerequisite (nếu có), module tiếp theo.

Đọc references/naming-convention.md để biết chi tiết tên chuẩn theo vị trí, cách tạo slug, bản đồ link bắt buộc, và checklist kiểm tra cuối.

Google Docs Compatibility — BẮT BUỘC

Output của skill này là file .md, thường được upload lên Google Drive và auto-convert sang Google Docs. Để không vỡ layout:

6 cấm kỵ tuyệt đối:

Không ASCII art box — cấm ký tự ┌ ┐ └ ┘ │ ─ ├ ┤ ┬ ┴ ┼. Docs đổi font → lệch hàng thê thảm.
Không multi-column bằng khoảng trắng — dùng table markdown 2+ cột thay thế.
Không ASCII tree folder (├── └──) ngoài code block — chuyển nested bullet list.
Không Mermaid diagram trong deliverable — export ảnh PNG hoặc thay bằng bảng quan hệ "Từ → Đến".
Không --- horizontal rule trong content — Docs convert thành đường kẻ mảnh phá nhịp. Dùng heading mới hoặc blank line thay thế. (Ngoại lệ: YAML frontmatter ở đầu file giữ nguyên.)
Không link relative path chéo file khi upload Drive — thay bằng Docs URL sau convert. Naming-convention relative link chỉ dùng cho Git/local.

Element OK (đã verify): heading, bullet, numbered list, task list - [ ] / - [x] → render thành checkbox native tick được, table, bold/italic, blockquote, inline code, code block, link, ảnh URL public.

Element né: HTML tags (trừ <br> trong cell bảng OK), footnote [^1].

Khi cần diagram/layout phức tạp:

Ý định	Thay bằng
Hộp so sánh A vs B	Table markdown 2 cột
Folder tree	Nested bullet list (hoặc code block nếu buộc)
Flow chart	Ảnh PNG (export từ mermaid.live) hoặc bảng "Bước → Hành động"
Prerequisite map	Bảng "Module → Prerequisite"
2x2 matrix	Table markdown 2 cột × 2 row

Đọc references/gdocs-compatibility.md để biết chi tiết: whitelist/blacklist element, rules bảng, ký tự Unicode an toàn, và checklist test convert cuối cùng.

Quick Start — Cá nhân, 1 chủ đề đơn

Nếu chỉ cần tạo 1 module cho cá nhân tự học, bỏ qua quy trình 6 bước, tạo 1 file duy nhất. Đặt tên file theo chuẩn: module-01-<slug-chu-de>.md (kebab-case, VN không dấu). Ví dụ: module-01-ky-thuat-sbi.md.

# [Tên Module] — Training Cá Nhân

## VĂN: Tôi cần biết gì? (10%)
- 3-5 ý chính, mỗi ý kèm 1 ví dụ thực tế
- 1 framework/mô hình tóm tắt

## TƯ: Điều này có ý nghĩa gì với tôi? (20%)
- Liên hệ với công việc hiện tại
- 1 tình huống cụ thể tôi sẽ áp dụng
- Kế hoạch thử nghiệm

## TU: Thực hành (70%)
- Tuần 1: Thử [hành động cụ thể] — ghi nhật ký mỗi ngày
- Tuần 2: Mở rộng + điều chỉnh
- Đúc kết: 3 bài học rút ra + 1 nguyên tắc giữ lại


Nếu cần nhiều module, cho team/công ty → dùng quy trình 6 bước bên dưới.

Quy trình 6 bước

Khi user yêu cầu tạo tài liệu training, thực hiện theo 6 bước sau:

Bước 1: Xác định mục tiêu tổng thể

Output bắt buộc: 1 Training Brief 1 trang, user confirm trước khi qua Bước 2. Lock-in mục tiêu, tránh trôi ở các bước sau.

Dòng chảy: Thu thập thông tin → Tóm tắt Training Brief → Validate 3 tiêu chí → Hỏi bổ sung câu mơ hồ → User confirm → Bước 2.

Core (5 câu, bắt buộc mọi quy mô):

Chủ đề đào tạo là gì? — Cụ thể, 1-2 câu, không dùng từ ô dù ("kỹ năng mềm", "soft skills")
Sau khoá, người học CÓ THỂ LÀM GÌ? (Quả) — Viết theo công thức "Sau [thời điểm], [X]% [đối tượng] có thể [hành động] [tần suất/ngữ cảnh], verify bằng [bằng chứng]" (scaffolding + ví dụ: references/template-training-brief.md mục 2.1). Validate value prop: hỏi thêm "Nếu KHÔNG có khoá này, họ mất bao lâu để tự mò ra?". Nếu trả lời "vài ngày Google" → khoá có thể không cần thiết, cân nhắc lại.
Ai là người học? (Nhân) — Cấp độ nhóm (mới/có nền tảng/tiềm năng cao/expert) + tự chấm 1-10 về chủ đề này + kiến thức nền hiện tại (đã biết gì, đã thử gì, thất bại gì) + nỗi đau cá nhân lớn nhất khiến họ cần khoá (khác pain business ở câu 6, câu này là "nỗi đau mất ngủ" của từng học viên)
Áp dụng ở đâu? — Tình huống công việc cụ thể + tần suất áp dụng
Đo lường thành công bằng gì? — Viết theo công thức "[Chỉ số] đo bằng [công cụ], tại [thời điểm], đạt khi [ngưỡng]" (ví dụ: references/template-training-brief.md mục 2.2). Metric phụ (retention): "Sau 3 tháng, họ còn đọng lại được gì?" đo bằng follow-up quiz / behaviour spot-check / interview ngắn.

Context (3 câu, bật khi team/công ty hoặc khi user chỉ có topic mơ hồ):

Vì sao mở khoá NGAY BÂY GIỜ? — Pain / trigger cụ thể (nỗi đau kinh doanh của tổ chức), tránh "đào tạo định kỳ" chung chung
Ràng buộc (Duyên) — Tổng thời lượng + daily budget (bao nhiêu phút/ngày học viên dành được, không phải tổng thời lượng) + format (online/offline/blended) + learning style (đọc Substack / xem video / làm workshop) + mức cần kỷ luật ngoài (tự giác được hay cần facilitator đẩy mông) + ngân sách + stakeholder bảo trợ
Tài liệu gốc — Có sách/video/framework/notes/case study không? Quyết định rẽ nhánh 2A Content Extraction

Validate thay vì skip cứng: Ngay cả khi user đã cung cấp đủ thông tin, KHÔNG skip ngay. Tóm tắt thành Training Brief, check từng câu theo 3 tiêu chí (số liệu / danh từ cụ thể / bằng chứng verify), đánh dấu ⚠️ Cần làm rõ các câu fail, hỏi lại gộp 1 lần. Chỉ lock-in khi 5 câu Core đều đạt.

Quy tắc làm giàu thông tin: Khi user cung cấp topic quá mơ hồ (chỉ 1-2 câu mô tả chung, không có tài liệu gốc, không có data về nhóm học), chủ động dùng WebSearch hoặc skill deep-research để bổ sung:

Benchmark ngành: chủ đề này thường được đào tạo thế nào, framework phổ biến nào đang dùng?
Case study thực tế: ai đã đào tạo thành công/thất bại chủ đề này, vì sao?
Data về nhóm học: học viên cấp độ tương tự thường vướng rào cản gì?
Trend: chủ đề có thay đổi gì 1-3 năm gần đây không?

Gộp tất cả insight thu thập được vào Training Brief dưới mục "Bối cảnh & Research" trước khi qua Bước 2. Tránh tạo modules dựa trên kiến thức chung chung — rơi vào bẫy "Tài liệu đẹp, hành vi không đổi".

Chiều đi sơ bộ: Dựa câu 3, đề xuất Văn→Tư→Tu (người mới/nền thấp) hoặc Tu→Tư→Văn (có nền cao / chủ đề trải nghiệm như leadership, sáng tạo). Chốt chính thức ở Bước 3.

Đọc references/template-training-brief.md để lấy: khung Training Brief đầy đủ, scaffolding chi tiết cho câu 2 + câu 5, quy trình validate 5 bước, ví dụ Training Brief hoàn chỉnh, và rule bật 3 câu Context theo quy mô.

Bước 2: Trích xuất nội dung & Phân tách modules

Đây là bước quyết định chất lượng toàn bộ khoá đào tạo.

Rẽ nhánh: Nếu user KHÔNG cung cấp tài liệu gốc (chỉ có topic/mục tiêu) → bỏ qua 2A, chuyển thẳng 2B — xây dựng modules từ mục tiêu Bước 1 và kiến thức chuyên môn. Nếu CÓ tài liệu → thực hiện đầy đủ 2A-2B-2C để không sót nội dung.

2A. Trích xuất nội dung gốc (Content Extraction)

Nếu user cung cấp tài liệu (sách, bài viết, video transcript, notes, slide...), BẮT BUỘC trích xuất trước khi phân module:

Đọc/phân tích toàn bộ tài liệu gốc — không bỏ sót phần nào
Liệt kê tất cả ý chính (key ideas) — mỗi ý 1 dòng, giữ nguyên ngữ nghĩa gốc
Phân loại từng ý theo bản chất:
Ký hiệu	Loại	Ví dụ
K	Kiến thức (khái niệm, định nghĩa, framework)	"SBI gồm 3 bước: Situation-Behavior-Impact"
N	Nguyên tắc (quy tắc, mindset, giá trị)	"Feedback phải kịp thời, không để qua 48h"
T	Kỹ thuật (cách làm, quy trình, tool)	"Dùng câu hỏi mở thay vì phán xét"
V	Ví dụ/Câu chuyện (case, minh hoạ)	Câu chuyện CEO nhận feedback từ intern
C	Cảnh báo/Sai lầm (anti-pattern, trap)	"Đừng feedback khi đang tức giận"
Tạo bảng Content Inventory:
## Content Inventory — [Tên tài liệu gốc]

| # | Ý chính | Loại | Nguồn (trang/phút/đoạn) | → Module |
|---|---------|------|-------------------------|----------|
| 1 | [Ý chính 1] | K | Trang 12 | M1 |
| 2 | [Ý chính 2] | N | Video 05:30 | M2 |
| 3 | [Ý chính 3] | T | Chương 3 | M2 |
| ... | ... | ... | ... | ... |


Cột "→ Module" để trống lúc đầu, điền sau khi phân module ở bước 2B.

2B. Phân tách modules

Quy trình:

Từ Content Inventory, nhóm các ý chính thành clusters (mỗi cluster = 1 module tiềm năng)
Kiểm tra tính độc lập (3 câu hỏi):
Học xong cluster này, làm được ít nhất 1 việc cụ thể?
Bỏ cluster này, các cluster còn lại vẫn có giá trị?
Hoàn thành trong 1-5 ngày (cá nhân) / 1-2 tuần (team)?
Xác định tier: Foundation → Core → Advanced → Specialized
Vẽ prerequisite map (dùng Mermaid)
Tạo bảng tóm tắt module
2C. Đối chiếu Content Coverage (BẮT BUỘC)

Sau khi phân module xong, điền cột "→ Module" trong Content Inventory và kiểm tra:

## Content Coverage Check

| Kiểm tra | Kết quả |
|----------|---------|
| Tổng ý chính trích xuất | ___ ý |
| Đã gán vào module | ___ ý |
| CHƯA gán (orphan) | ___ ý |
| Loại bỏ có lý do | ___ ý |

### Ý chưa được gán (nếu có)
| # | Ý chính | Lý do chưa gán | Quyết định |
|---|---------|----------------|-----------|
| _ | ___ | ___ | Thêm vào Module X / Tạo module mới / Loại bỏ (lý do) |


Quy tắc:

0 ý orphan = đạt — mọi nội dung quan trọng đều có chỗ
Nếu có ý orphan → quyết định: gán vào module phù hợp, tạo module mới, hoặc loại bỏ (phải ghi rõ lý do)
Trình bày Content Coverage Check cho user xác nhận trước khi chuyển Bước 3
Nếu user bổ sung tài liệu mới giữa chừng → lặp lại 2A-2C cho phần bổ sung
2D. Đối chiếu Brief Coverage (BẮT BUỘC)

Content Coverage bảo đảm không sót tài liệu gốc. Brief Coverage bảo đảm không lệch mục tiêu khoá. Hai việc khác nhau, phải chạy cả hai.

Mở lại Training Brief (Bước 1) và điền bảng sau:

## Brief Coverage Map

| Outcome Brief (câu 2) | Metric Brief (câu 5) | Module phục vụ | Deliverable verify |
|---|---|---|---|
| [Hành vi 1] | [Chỉ số đo hành vi 1] | M2, M3 | Bài thực hành áp dụng 5 lần + AAR |
| [Hành vi 2] | [Chỉ số đo hành vi 2] | M4 | Dự án 2 tuần + teach-back |
| [Hành vi 3] | [Chỉ số đo hành vi 3] | ??? ORPHAN | ??? |

## Brief Coverage Check

| Kiểm tra | Kết quả |
|----------|---------|
| Tổng outcome trong Brief | ___ outcome |
| Đã có module phục vụ | ___ outcome |
| CHƯA có module (outcome orphan) | ___ outcome |
| Tổng metric trong Brief | ___ metric |
| Đã có deliverable verify | ___ metric |
| CHƯA có deliverable (metric orphan) | ___ metric |


Quy tắc:

0 outcome orphan + 0 metric orphan = đạt.
Outcome orphan → thêm module hoặc mở rộng module hiện có. Không được bỏ qua (outcome là cam kết với user/stakeholder).
Metric orphan → thêm deliverable Tu hoặc checkpoint đánh giá. Module có hay không mà không có cách verify metric = module vô nghĩa với Brief.
Ngược lại: module KHÔNG phục vụ outcome nào trong Brief → cảnh báo scope creep, hỏi user có cần giữ không. Không giữ module chỉ vì "hay ho".
Trình bày Brief Coverage Map cho user xác nhận trước khi chuyển Bước 3. Cùng với Content Coverage Check (2C) thành 1 gói xác nhận duy nhất.

5 quy tắc phân tách:

1 module = 1 chủ đề trọng tâm
Độc lập tối đa (ghi rõ prerequisite nếu có)
Đủ nhỏ để hoàn thành (1-5 ngày)
Đủ lớn để có giá trị
Cùng cấp độ trừu tượng

Đọc references/modular-architecture.md để hiểu chi tiết về kiến trúc modular, tier system, và folder structure.

Bước 3: Thiết kế từng module

Brief là compass — Mở lại TRƯỚC khi thiết kế từng module:

Training Brief (Bước 1) không phải checkpoint 1 lần rồi treo tường. Nó là la bàn. MỖI module, trước khi quyết định tỷ lệ / chiều đi / deliverable, mở lại Brief và trả lời 3 câu sau:

Câu hỏi compass	Nguồn trong Brief	Ảnh hưởng quyết định nào
Module này phục vụ outcome hành vi nào?	Câu 2 (Outcome)	Xác định deliverable chính
Module này sinh bằng chứng cho metric nào?	Câu 5 (Metric)	Xác định format bài thực hành + checkpoint đánh giá
Người học module này đang ở cấp độ nào (câu 3 Brief) và bối cảnh áp dụng ra sao (câu 4 Brief)?	Câu 3 + Câu 4	Xác định tỷ lệ Văn-Tư-Tu + chiều đi + mức độ guided

Rule: Nếu không trả lời được câu 1 hoặc câu 2 → quay lại Bước 2 (Brief Coverage Map). Đừng thiết kế module mồ côi.

Với mỗi module, xác định:

Quyết định	Lựa chọn	Tham chiếu Brief
Tỷ lệ Văn-Tư-Tu	Dựa vào loại kiến thức và cấp độ người học	Câu 3 Brief (cấp độ)
Chiều đi	Văn→Tư→Tu (mặc định) hay Tu→Tư→Văn (kiến tạo)?	Câu 3 Brief (có nền tảng chưa)
Mức độ guided	Step-by-step / Semi-guided / Independent?	Câu 3 Brief + câu 7 (kỷ luật ngoài)
Deliverable chính	Người học nộp/trình bày gì cuối module?	Câu 2 + câu 5 Brief (phải verify được)

Khi chọn chiều kiến tạo (Tu→Tư→Văn):

Áp dụng khi người học có nền tảng hoặc chủ đề mang tính trải nghiệm (kỹ năng mềm, leadership, sáng tạo).

Bước	Hoạt động	Facilitator làm gì
Tu trước	Đặt người học vào tình huống thực tế / mô phỏng — CHƯA dạy lý thuyết	Tạo môi trường, quan sát, không can thiệp
Tư giữa	Người học tự đúc kết: "Mình vừa làm gì? Tại sao kết quả như vậy?"	Hỏi ngược, dẫn dắt phản tư
Văn cuối	Cung cấp framework/lý thuyết — người học đối chiếu với trải nghiệm	Bổ sung, hệ thống hoá

Lưu ý: Chiều kiến tạo xuất phát chậm nhưng về đích trước — hành vi thay đổi sâu và bền hơn. Đo sau 30-60-90 ngày, không chỉ quiz ngay sau buổi học.

Đọc references/ratio-adjustment.md để tra cứu tỷ lệ phù hợp theo loại kiến thức và cấp độ.

Bước 4: Xây dựng nội dung

Thứ tự viết tối ưu cho MỖI module (tên phase folder theo chuẩn naming-convention.md):

1. Viết README.md (thẻ căn cước module)
2. Viết 03-tu-thuc-hanh/ trước — bài thực hành, dự án (70% giá trị)
3. Viết 02-tu-suy-tu/ — câu hỏi phản chiếu, case study
4. Viết 01-van/ — chỉ kiến thức CẦN CHO Tư và Tu
5. Viết 04-danh-gia/ — rubric, After-Action Review template
6. Đối chiếu với Content Inventory — đảm bảo mọi ý chính gán cho module này đều xuất hiện trong nội dung


Quy tắc vàng: Với mỗi đoạn trong Văn, tự hỏi: "Bỏ đoạn này, người học có làm được bài thực hành không?" Nếu có → bỏ.

Quy tắc đối chiếu: Sau khi viết xong module, check lại Content Inventory — mọi ý có ký hiệu K/N/T/V/C gán cho module này phải xuất hiện trong ít nhất 1 thành phần (Văn, Tư, hoặc Tu). Nếu thiếu → bổ sung hoặc ghi lý do loại bỏ.

Micro-cycle Văn-Tư-Tu trong MỖI hoạt động:

Module lớn = 1 chu trình Văn-Tư-Tu. Nhưng mỗi bài thực hành, mỗi case study bên trong module cũng là 1 chu trình Văn-Tư-Tu thu nhỏ. Đây là nguyên tắc fractal — cấu trúc lặp lại ở mọi cấp độ.

Cấp	Ví dụ	Văn	Tư	Tu
Bài thực hành 1 giờ	Tập feedback 1:1	5' đọc tình huống	10' phân tích SBI	30' đóng vai + 15' AAR
Case study 30 phút	Phân tích cú feedback của CEO	5' đọc case	15' tìm nhân-duyên-quả	10' rút nguyên lý + áp dụng vào việc mình
Journal entry 15 phút	Ghi chép hàng ngày	2' ôn khái niệm	5' liên hệ việc trong ngày	8' viết hành động mai làm khác

Rule bắt buộc: Mỗi hoạt động đều có đủ 3 bước. Thiếu Đúc kết (Tu cuối) = không học. Thiếu Phân tích (Tư giữa) = bắt chước mù. Thiếu tiếp nhận (Văn đầu) = thực hành không nền.

Templates chi tiết cho từng thành phần — chỉ load file cần dùng:

references/template-van.md — Template cho phần VĂN
references/template-tu-suy-tu.md — Template cho phần TƯ
references/template-tu-thuc-hanh.md — Template cho phần TU
references/template-danh-gia.md — Template cho phần ĐÁNH GIÁ
Bước 5: Triển khai

Điều chỉnh theo quy mô:

Cá nhân:

1 file/module là đủ (gộp Văn-Tư-Tu vào 1 file)
Tự đặt deadline cho mỗi module (1-5 ngày)
Dùng checklist hành động để duy trì kỷ luật

Team (5-15 người):

Buddy pairs: Ghép chéo trình độ, trao đổi bài Tư + review deliverable của nhau
Facilitator: 1 người dẫn dắt, không giảng bài — hỏi ngược + phản biện
Kick-off: Giới thiệu khoá, chia buddy, gửi pre-work (Văn Module 1)
Check-in: Giữa tuần (15-30 phút) — tiến độ + rào cản
Wrap-up: Teach-back (mỗi người 5 phút) + After-Action Review

Công ty (rolling deployment):

Pilot: 1 team đi trước (4-6 tuần) → thu feedback → điều chỉnh tài liệu
Train-the-trainer: Alumni pilot trở thành facilitator cho đợt sau
Module Library: Modules đã validate đưa vào thư viện chung — team tự chọn theo tier + prerequisite
Rolling: Team mới bắt đầu mỗi 2-4 tuần, không cần đợi tất cả cùng lúc

Đọc references/template-facilitator-hub.md để tra cứu chi tiết: hướng dẫn facilitation, module map, lịch trình gợi ý, và cách ghép buddy pairs.

Bước 6: Đánh giá & cải tiến

Cấp module: After-Action Review sau mỗi module + Rubric đánh giá deliverable. Cấp khoá: Survey cuối khoá + đo hành vi thay đổi sau 30-60-90 ngày.

Thời điểm	Công cụ	Đo gì
Cuối mỗi module	After-Action Review + Rubric	Mức độ nắm kiến thức + chất lượng thực hành
Cuối khoá	Survey cuối khoá	Đánh giá tổng thể + mức độ hài lòng
Sau 30 ngày	Follow-up check-in	Đang thử áp dụng? Rào cản gì?
Sau 60 ngày	Check-in 1:1	Hành vi đã thay đổi chưa? Kết quả cụ thể?
Sau 90 ngày	Follow-up + Meeting nhóm	Thói quen bền vững? Tác động đo lường được?

Phân tích & cải tiến:

Tỷ lệ áp dụng < 30% → Kiểm tra lại phần Tu (thiếu thực hành?)
Tỷ lệ áp dụng 30-60% → Kiểm tra rào cản môi trường
Tỷ lệ áp dụng > 60% → Khoá hiệu quả — đúc kết best practices

Templates đánh giá cấp module (rubric, AAR) và cấp khoá (survey, follow-up 30-60-90): đọc references/template-danh-gia.md.

Facilitation

Nguyên tắc vàng: Đừng trả lời — hãy hỏi ngược. Facilitator dẫn dắt bằng câu hỏi, không giảng bài.

Chi tiết facilitation (mô hình Gà-Đại Bàng, hai chiều đi, phương pháp theo cấp độ): đọc references/philosophy-foundation.md. Tỷ lệ Văn-Tư-Tu theo cấp độ người học: đọc references/ratio-adjustment.md.

Output format

Tạo bộ tài liệu theo cấu trúc folder chuẩn trong references/modular-architecture.md (Section 4 + 5). Mọi tên folder, tên file, và link bắt buộc tuân thủ references/naming-convention.md.

Trước khi bàn giao, chạy ba checklist (nội dung → hình thức → tương thích):

Checklist 0 — Chất lượng nội dung (mỗi module)

Với MỖI module, tự chấm 6 tiêu chí. Module đạt khi tiêu chí 1, 5, 6 = Có, và trung bình 2-3-4 ≥ 3/5.

#	Tiêu chí	Câu hỏi kiểm tra	Thang
1	Cốt lõi	Module có 1 thông điệp chi phối tất cả, bỏ đi thì module sụp?	Có/Không
2	Giải thích lực	Phần Văn giúp người không biết gì hiểu trong bao nhiêu %?	1-5
3	Dự đoán lực	Người học áp dụng module này dự đoán được tình huống mới không có trong bài?	1-5
4	Truyền đạt	Một người đã học xong giải thích module cho đồng nghiệp trong 2 phút?	1-5
5	Hành động	Sau module, người học biết CHÍNH XÁC phải làm gì tiếp, ở đâu, khi nào?	Có/Không
6	Brief alignment	Module map rõ ít nhất 1 outcome (câu 2 Brief) + 1 metric (câu 5 Brief)? Deliverable sinh bằng chứng verify được metric?	Có/Không

Tiêu chí 6 fail = module thiết kế ngoài Brief. Không đạt → quay Bước 3 mở lại Brief, map lại. Nếu thực sự Brief thiếu outcome cho nội dung này → quay Bước 1 bổ sung Brief (có confirm user).

Không đạt các tiêu chí khác → quay lại Bước 4 bổ sung, tối đa 2 vòng. Nếu vẫn fail sau 2 vòng → cấu trúc module sai, quay Bước 2 phân tách lại.

Checklist 1 — Naming & liên kết

Tra cuối file references/naming-convention.md (Section 5):

Mọi folder/file kebab-case, VN không dấu, zero-pad số.
Đủ 4 phase folder mỗi module.
Mọi link bắt buộc (tổng quan ↔ module ↔ phase ↔ facilitator) có mặt, không link placeholder.
Checklist 2 — Google Docs compatibility

Tra cuối file references/gdocs-compatibility.md (Section 8):

Không ASCII box-drawing ngoài code block.
Không multi-column bằng space.
Folder tree đã trong code block hoặc nested bullet.
Mermaid đã thay bằng ảnh/table.
Không --- horizontal rule trong content (YAML frontmatter được miễn).
Không HTML tags (trừ <br> trong cell bảng).
Không footnote [^1] — chuyển "Ghi chú" cuối file.
Link chéo file đã plan theo mục tiêu (Git giữ relative, Drive thay Docs URL).
Bảng ≤ 6 cột, không merge cell, có blank line trước và sau.
Heading không nhảy cóc, không in đậm.
Không 2+ blank line liên tiếp.
(Khuyến khích) test 1 file đại diện: upload Drive → mở Docs → kiểm tra.

Lưu ý theo quy mô:

Cá nhân: đơn giản hoá — 1 file/module là đủ (tên file vẫn theo chuẩn kebab-case).
Team: full structure.
Công ty: thêm Module Library.
Ví dụ áp dụng — Map nhanh chủ đề sang cấu hình

Bảng tra nhanh để chọn chiều đi + tỷ lệ Văn-Tư-Tu + deliverable cho các nhóm chủ đề phổ biến. Đây là điểm xuất phát, điều chỉnh theo nhóm học cụ thể.

Loại chủ đề	Ví dụ	Chiều đi	Văn/Tư/Tu	Deliverable Tu
Kỹ thuật có quy trình rõ	SBI feedback, OKR, sử dụng tool	Văn→Tư→Tu	15/15/70	Áp dụng thật 5 lần, ghi AAR
Kỹ năng mềm / Leadership	Lãnh đạo, ra quyết định, huấn luyện	Tu→Tư→Văn	5/15/80	Dự án 4-6 tuần + teach-back
Tư duy / Mindset	Systems thinking, first principles	Tu→Tư→Văn	10/30/60	Case study thực tế + nguyên lý rút ra
Onboarding tool cụ thể	Dùng Notion, Jira, Figma	Văn→Tu→Tư	20/10/70	Làm 1 dự án nhỏ end-to-end
Kiến thức chuyên môn	Kế toán, luật, kỹ thuật chuyên sâu	Văn→Tư→Tu	30/20/50	Case + làm đề thực tế có chấm
Văn hoá / Giá trị tổ chức	Trung thực, phục vụ vô điều kiện	Tu→Tư→Văn	5/25/70	Ghi nhận 30 ngày + chia sẻ câu chuyện thật
Sáng tạo / Nghệ thuật	Viết, design, brainstorm	Tu→Tư→Văn	10/20/70	Sản phẩm thật + peer critique
Sức khoẻ / Thói quen	Thiền, tập gym, dinh dưỡng	Văn→Tu→Tư	15/5/80	Nhật ký 60-90 ngày + đo số liệu

Cách đọc bảng:

Cột "Chiều đi" quyết định thứ tự trình bày module, không phải tỷ lệ thời gian.
Cột "Văn/Tư/Tu" là tỷ lệ thời gian/sức lực, không phải số trang.
Nếu chủ đề không map được vào 8 dòng trên → mô tả đặc tính (có quy trình rõ không? mang tính trải nghiệm không? đo được kết quả ngay không?) và tự suy luận theo 3 nguyên tắc: chủ đề có quy trình rõ → chiều truyền thống; chủ đề trải nghiệm → chiều kiến tạo; đo ngay được → tỷ lệ Văn cao hơn, đo chậm → tỷ lệ Tu cao hơn.

Đừng lầm: Bảng này chỉ là default. Quyết định cuối cùng vẫn phải dựa vào cấp độ người học (Gà công nghiệp / Gà rừng / Đại bàng — xem references/philosophy-foundation.md). Cùng chủ đề, Gà công nghiệp cần nhiều Văn hơn; Đại bàng cần nhiều Tu hơn.

Weekly Installs
14
Repository
hoangvantuan/cl…e-plugin
First Seen
Mar 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn