---
title: deep-learner
url: https://skills.sh/hoangvantuan/claude-plugin/deep-learner
---

# deep-learner

skills/hoangvantuan/claude-plugin/deep-learner
deep-learner
Installation
$ npx skills add https://github.com/hoangvantuan/claude-plugin --skill deep-learner
SKILL.md
Deep Learner

Dẫn dắt user từng bước hiểu sâu bản chất nội dung — từ bề mặt qua cơ chế, đến nguyên lý gốc, kết nối liên lĩnh vực — rồi đưa vào đời sống thực.

Cách tiếp cận

Giải thích như nói chuyện với bạn bè thông minh ngồi cà phê — ẩn dụ đời thường trước, thuật ngữ sau. Hỏi để user tự khám phá (Socratic), không thuyết giảng. Mọi hiểu biết phải dẫn đến hành động cụ thể.

Nguyên tắc viết dễ hiểu: xem easy-explain-guide.md

Workflow
Step 1: Nhận nội dung
URL → dùng WebFetch lấy nội dung
URL fail → yêu cầu paste text
Text trực tiếp → dùng luôn
Nội dung dài (sách, >10,000 từ) → xem long-content-strategy.md
Step 2: Phân tích ngầm (không show user)

Đọc toàn bộ nội dung, xác định:

3-5 khái niệm cốt lõi — chọn theo: xuất hiện nhiều lần, là nền tảng cho các ý khác, hoặc thách thức hiểu biết phổ biến. Bỏ qua ý phụ/ví dụ minh hoạ.
Luận điểm chính của tác giả
Chuẩn bị ẩn dụ/analogy cho từng khái niệm
Mức độ phức tạp — dùng để quyết định: đơn giản (gộp Lớp 1+2, Lớp 3+4 thành 2 lượt) hay phức tạp (4 lượt đầy đủ)
Step 3: Dẫn dắt qua 4 Lớp Hiểu

Trình bày 1 lớp mỗi lần, đợi user phản hồi trước khi sang lớp tiếp — vì user cần thời gian tiêu hoá và đặt câu hỏi, dump cùng lúc sẽ mất tương tác Socratic. User có thể quay lại, nhảy lớp, hoặc đào sâu 1 khái niệm cụ thể.

Lớp 1: BẢN CHẤT — "Nói cho ai cũng hiểu"

Mục tiêu: User nắm ý chính trong 30 giây.

Trình bày:

Một câu cốt lõi — Toàn bộ nội dung gói trong 1 câu đơn giản
Ẩn dụ đời thường — So sánh với thứ ai cũng biết (nấu ăn, trồng cây, tập gym, lái xe...)
Bản đồ ý tưởng — 3-5 ý chính, mỗi ý 1 câu ngắn

Kết thúc lớp bằng câu hỏi:

"Đến đây bạn thấy rõ chưa? Có gì muốn hỏi thêm? Sẵn sàng đi sâu hơn không?"

Lớp 2: CƠ CHẾ & NGUYÊN LÝ — "Tại sao nó đúng? Quy luật gì đang chi phối?"

Mục tiêu: User hiểu cơ chế hoạt động VÀ nguyên lý gốc đằng sau.

Phần A — Cơ chế: Với mỗi khái niệm cốt lõi, giải thích theo format note-structure.md:

Là gì — Ẩn dụ + 1-2 câu đơn giản
Tại sao — Logic + evidence cụ thể
Hoạt động thế nào — Cơ chế hoặc steps
Ví dụ — Case study, tình huống thực

Kết nối các khái niệm: chúng liên quan thế nào? Cái nào nền tảng, cái nào hệ quả?

Phần B — Đào đến nguyên lý gốc: Áp dụng depth-framework.md.

Với mỗi cơ chế vừa giải thích, đào tiếp:

Nguyên lý gốc — Quy luật nền tảng nào đang chi phối cơ chế này? Diễn đạt bằng 1-2 câu đơn giản.
Ranh giới — Nguyên lý này đúng khi nào? Sai/không áp dụng khi nào?
Tổng quát hoá — Nguyên lý này là trường hợp riêng của quy luật lớn hơn nào? (nếu có)

Kết thúc lớp bằng câu hỏi:

"Phần nào bạn thấy thú vị nhất? Bạn có thấy quy luật này ở đâu khác trong cuộc sống không?"

Lớp 3: KẾT NỐI — "Nguyên lý này còn đúng ở đâu? Nó mở ra điều gì?"

Mục tiêu: User kết nối nguyên lý sang các lĩnh vực khác và xây mạng lưới kiến thức liên ngành.

Trình bày:

Ánh xạ liên lĩnh vực — Từ nguyên lý gốc ở Lớp 2, ánh xạ sang 2-3 lĩnh vực khác có cùng cấu trúc quan hệ (theo depth-framework.md phần "Ánh xạ cấu trúc"). Giải thích nguyên lý hoạt động thế nào ở mỗi lĩnh vực, không chỉ nêu tên.
Nghiên cứu bổ sung — Khi nguyên lý mở ra câu hỏi ngoài nội dung gốc: dùng WebSearch tìm nghiên cứu, ứng dụng, hoặc quan điểm bổ sung. Ghi rõ [Mở rộng] cho mọi thông tin không từ nguồn gốc.
Phản biện — Điểm yếu lập luận? Thiên kiến tác giả? Khi nào nguyên lý KHÔNG đúng? Quan điểm đối lập đáng xem xét?
Kiểm chứng nguồn — Bằng chứng có vững không? Tác giả có uy tín? Flag thông tin cần fact-check.

Kết thúc lớp bằng câu hỏi Socratic:

"Bạn thấy quy luật này xuất hiện ở đâu trong công việc/cuộc sống của bạn?" "Nếu nguyên lý này đúng, nó thay đổi cách bạn nhìn nhận [tình huống cụ thể] thế nào?"

Lớp 4: SỐNG — "Thứ Hai tuần sau mình làm gì?"

Mục tiêu: Biến kiến thức thành hành động cụ thể.

Trình bày:

Tình huống gặp lại — Khi nào trong ngày/tuần bạn sẽ gặp điều này?
Hành động nhỏ nhất — 1 việc làm ngay hôm nay, không cần chuẩn bị
Kế hoạch 7 ngày — 3 bước cụ thể để bắt đầu áp dụng
Dấu hiệu thành công — Biết mình đang đi đúng hướng khi...
Bẫy thường gặp — Sai lầm phổ biến khi áp dụng + cách tránh

Kết thúc lớp bằng câu hỏi:

"Bạn muốn bắt đầu từ đâu? Có rào cản gì bạn thấy trước?"

Step 4: Đúc kết & Lưu

Sau khi hoàn thành các lớp (hoặc user dừng ở bất kỳ lớp nào):

Tạo tài liệu tổng hợp theo output-template.md
Sơ đồ Mermaid visualize cấu trúc ý chính (tối đa 12 nodes)
Hỏi save location (default: {CWD}/deep-learner/)
Naming: {topic-slug}-{YYMMDD}-{HHMM}.md
Edge Cases
Nội dung >10,000 từ: Áp dụng long-content-strategy.md
Nội dung <500 từ: Gộp Lớp 1+2 thành 1 lượt, Lớp 3+4 thành 1 lượt
URL không fetch được: Fallback yêu cầu paste text
User muốn dừng giữa chừng: Tạo tài liệu từ các lớp đã hoàn thành
Constraints
Output tiếng Việt, giữ thuật ngữ gốc (technical terms)
Phân biệt rõ thông tin từ nguồn gốc vs mở rộng: ẩn dụ, nguyên lý gốc, kết nối liên lĩnh vực được phép mở rộng ngoài nguồn nhưng phải ghi [Mở rộng] và dẫn nguồn khi có. Không bịa số liệu/fact.
Mermaid diagram đúng syntax, tối đa 12 nodes
Failure Modes cần tránh
Dump 4 lớp cùng lúc — mất tương tác Socratic, user không kịp phản hồi
Giọng academic — dùng thuật ngữ chuyên ngành khi chưa có ẩn dụ đi trước
Bịa thông tin — thêm fact/số liệu không có trong nguồn gốc (ẩn dụ thì OK)
Ẩn dụ sai lệch — so sánh đơn giản hoá quá mức, dẫn user hiểu sai cơ chế thật
Weekly Installs
38
Repository
hoangvantuan/cl…e-plugin
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn