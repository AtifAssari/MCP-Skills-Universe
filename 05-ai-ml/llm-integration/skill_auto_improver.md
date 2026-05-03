---
title: skill-auto-improver
url: https://skills.sh/hoangvantuan/claude-plugin/skill-auto-improver
---

# skill-auto-improver

skills/hoangvantuan/claude-plugin/skill-auto-improver
skill-auto-improver
Installation
$ npx skills add https://github.com/hoangvantuan/claude-plugin --skill skill-auto-improver
SKILL.md
Skill Auto-Improver

Phân tích skill hiện có, trích xuất bài học, đề xuất cải tiến tổng quát hóa, và thực hiện sau khi user duyệt. Mọi cải tiến phải giữ skill gọn — không phình to.

Nguyên lý bất biến

Mười một nguyên lý áp dụng cho mọi skill bất kể domain. Đọc chi tiết + ví dụ khi cần tra cứu.

Giải thích lý do thay vì ra lệnh — LLM hiểu "tại sao" tốt hơn "phải làm"
Tổng quát hóa > Cụ thể hóa — Không fix cho case cụ thể
Progressive Disclosure — SKILL.md chứa workflow + quyết định, chi tiết → references/
Mỗi dòng phải earn chỗ đứng — Xoá mà output không đổi = dead content
Single Source of Truth — Mỗi thông tin chỉ định nghĩa 1 nơi
Đo trước, sửa sau — Chấm điểm baseline → sửa → chấm lại
Ranh giới quyết định phải rõ — Không kèm điều kiện = model đoán
Ngắn ≠ Tốt, Dài ≠ Xấu — Ngắn nhất có thể mà không thiếu sót
Degrees of Freedom — Chọn mức tự do (cao/vừa/thấp) phù hợp độ nhạy cảm
Skill = Interface — Định nghĩa contract (output), không phải implementation (cách làm)
Context là tài nguyên hữu hạn — Mỗi token cạnh tranh attention, nội dung dở hại chủ động toàn bộ
Quy trình (4 pha)
Pha 1: Thu thập & Phân tích

Bước 1 — Xác định skill cần cải tiến

Hỏi user nếu chưa rõ skill nào. Đọc SKILL.md + toàn bộ references/ của skill đó.

Bước 2 — Thu thập bài học

Từ 2 nguồn song song:

Nguồn	Cách thu thập
Hội thoại hiện tại	Scan conversation tìm: feedback user, lỗi lặp lại, output không đạt, corrections
Cấu trúc SKILL.md	Đánh giá theo quality-checklist — 8 tiêu chí

Bước 3 — Chấm điểm hiện tại

Đánh giá skill theo 8 tiêu chí trong quality-checklist, mỗi tiêu chí thang 1-5. Ghi lại điểm số làm baseline.

Pha 2: Kế hoạch cải tiến

Bước 4 — Áp dụng improvement patterns

Đọc improvement-patterns và design-patterns. Đối chiếu với kết quả phân tích, xác định patterns nào áp dụng được.

Bước 5 — Soạn kế hoạch

Với mỗi cải tiến đề xuất, ghi rõ:

## Cải tiến [N]: [Tên ngắn]
- Vấn đề: [Mô tả vấn đề phát hiện]
- Pattern áp dụng: [Tên pattern từ improvement-patterns]
- Hành động: [Cụ thể sẽ làm gì]
- Tác động dòng: +X / -Y dòng (ước tính)
- Lý do tổng quát: [Tại sao cải tiến này có giá trị ngoài case hiện tại]


Quy tắc kế hoạch:

Tổng tác động dòng phải <= 0 (không phình to)
Nếu cần thêm nội dung → chỉ rõ sẽ cắt/gộp phần nào
Ưu tiên cải tiến có tác động cao, effort thấp
Tối đa 5 cải tiến mỗi lần (tránh thay đổi quá nhiều cùng lúc)

Bước 6 — Trình user duyệt

Hiển thị kế hoạch cho user theo format Bước 5. User có thể approve toàn bộ, chọn subset, hoặc reject. Chỉ thực hiện các cải tiến được approve — bỏ qua phần bị reject mà không hỏi lại.

Pha 3: Thực hiện

Bước 7 — Áp dụng cải tiến

Thực hiện từng cải tiến đã được duyệt. Sau mỗi thay đổi, kiểm tra:

SKILL.md vẫn hợp lệ (frontmatter đúng, references không broken)
Tổng dòng không tăng so với bản gốc (trừ khi user đồng ý)
Pha 4: Xác nhận

Bước 8 — Chấm điểm lại

Đánh giá lại 8 tiêu chí. Nếu skill chạy đa model, kiểm tra hướng dẫn đủ cụ thể cho model yếu nhất (Haiku) không. So sánh trước/sau:

| Tiêu chí            | Trước | Sau | Delta |
|----------------------|-------|-----|-------|
| Clarity              |       |     |       |
| Specificity          |       |     |       |
| Coverage             |       |     |       |
| Structure            |       |     |       |
| Cognitive Load       |       |     |       |
| Bloat Score          |       |     |       |
| Anti-patterns        |       |     |       |
| Description Quality  |       |     |       |
| **Tổng (/40)**       |       |     |       |
| **Tổng dòng**        |       |     |       |


Bước 9 — Báo cáo

Lưu báo cáo cải tiến vào {CWD}/skill-improver-{skill-name}-{YYMMDD}.md với nội dung:

Điểm trước/sau
Danh sách cải tiến đã thực hiện
Bài học rút ra (dạng tổng quát, áp dụng được cho skill khác)
Xử lý đặc biệt

Skill quá dài (>300 dòng):

Ưu tiên tách nội dung ra references/ thay vì giữ trong SKILL.md
Quy tắc: SKILL.md chứa workflow + quyết định. Chi tiết/ví dụ/API → references/

Skill quá ngắn (<80 dòng):

Kiểm tra coverage — có thiếu edge cases, output format, hoặc constraints không?
Ngắn là tốt, nhưng thiếu sót thì không tốt

Nhiều skill cùng lúc:

Phân tích từng skill riêng biệt, nhưng phát hiện patterns chung
Báo cáo patterns chung ở cuối để user áp dụng hàng loạt
Weekly Installs
10
Repository
hoangvantuan/cl…e-plugin
First Seen
11 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass