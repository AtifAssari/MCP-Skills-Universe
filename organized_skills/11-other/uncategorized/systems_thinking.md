---
rating: ⭐⭐
title: systems-thinking
url: https://skills.sh/hoangvantuan/claude-plugin/systems-thinking
---

# systems-thinking

skills/hoangvantuan/claude-plugin/systems-thinking
systems-thinking
Installation
$ npx skills add https://github.com/hoangvantuan/claude-plugin --skill systems-thinking
SKILL.md
Systems Thinking Analysis

"Hành vi của hệ thống không thể biết được chỉ bằng cách biết các phần tử tạo nên nó." — Donella Meadows

Triết lý cốt lõi

Hệ thống tự tạo ra hành vi của chính nó. Một sự kiện bên ngoài có thể kích hoạt hành vi đó, nhưng cùng một sự kiện tác động lên hệ thống khác sẽ cho kết quả khác. Vấn đề dai dẳng (nghèo đói, ô nhiễm, nghiện, xung đột leo thang) tồn tại không phải vì thiếu nỗ lực giải quyết, mà vì chúng là hành vi đặc trưng của cấu trúc hệ thống tạo ra chúng.

Thay vì đổ lỗi cho cá nhân hay sự kiện, tư duy hệ thống tìm kiếm cấu trúc -- các vòng feedback, stocks & flows, delays, mental models -- đang tạo ra hành vi mà ta quan sát được.

Lăng kính xuyên suốt

Ba khái niệm dưới đây áp dụng ở MỌI bước phân tích, không chỉ riêng bước nào:

Nonlinearity & tipping points: Quan hệ trong hệ thống hiếm khi tuyến tính. Tìm ngưỡng tới hạn — điểm mà thay đổi nhỏ tạo ra hệ quả lớn bất ngờ (hoặc ngược lại, nỗ lực lớn không tạo thay đổi gì vì chưa đạt ngưỡng).
Bounded rationality: Mỗi actor trong hệ thống hành động hợp lý trong giới hạn thông tin họ có — nhưng hành động hợp lý của cá nhân có thể tạo ra kết quả tồi tệ cho tổng thể. Đừng đổ lỗi cho cá nhân, hãy tìm cấu trúc thông tin/incentive đang giới hạn họ.
Resilience: Hệ thống khỏe mạnh không chỉ hiệu quả mà còn resilient — khả năng phục hồi sau cú sốc. Tối ưu hóa quá mức giết chết resilience. Hỏi: "Hệ thống này có chịu được bất ngờ không?"
Quy trình phân tích

Khi user đưa ra một chủ đề, vấn đề hoặc tình huống, thực hiện phân tích theo 7 bước dưới đây. Viết output theo template trong templates/analysis-output.md.

Bước 0: Research bối cảnh (nếu cần)

Trước khi phân tích, đánh giá xem bạn đã đủ hiểu biết về chủ đề chưa.

Khi nào cần research:

Chủ đề thuộc lĩnh vực chuyên môn (y tế, luật, tài chính, khoa học)
Cần data/thống kê thực tế để phân tích có chiều sâu
Bối cảnh địa phương/ngành đặc thù mà kiến thức chung không đủ
User đề cập đến hiện tượng cụ thể cần verify

Cách research:

Tìm kiếm thông tin bổ sung (search web, đọc tài liệu liên quan, hoặc research chuyên sâu nếu chủ đề phức tạp)
Tập trung tìm: data thực tế, lịch sử vấn đề, các can thiệp đã thử và kết quả
Ưu tiên nguồn đáng tin cậy, số liệu cụ thể thay vì ý kiến chung chung
Ghi chú nguồn tham khảo để trích dẫn trong phân tích

Khi KHÔNG cần research:

Chủ đề đời sống cá nhân (quan hệ, thói quen, career)
User đã cung cấp đủ bối cảnh
Chủ đề nằm trong kiến thức tổng quát đã có
Bước 1: Lắng nghe nhịp đập của hệ thống

Trước khi can thiệp, hãy quan sát. Hỏi:

Hệ thống này đã hoạt động như thế nào theo thời gian?
Hành vi nào đang lặp lại? Xu hướng nào đang diễn ra?
Ai đang nói gì về nó, và thực tế khác gì so với câu chuyện họ kể?

Tập trung vào hành vi thực tế (data, patterns, history), không phải lý thuyết hay niềm tin. Nếu đã research ở Bước 0, sử dụng data thu được để làm nền tảng cho phân tích.

Bước 2: Vẽ bản đồ hệ thống (System Map)

Xác định 3 thành phần cốt lõi:

Elements (Phần tử): Các thành phần hữu hình và vô hình. Đừng đào quá sâu vào sub-elements -- hãy dừng ở mức đủ để thấy rừng, không chỉ thấy cây.

Interconnections (Kết nối): Các luồng vật chất, thông tin, quy tắc kết nối elements. Interconnections quan trọng hơn elements -- thay đổi cầu thủ không thay đổi trò chơi, thay đổi luật chơi mới thay đổi trò chơi.

Purpose/Function (Mục đích): Mục đích thực sự của hệ thống (quan sát từ hành vi, không phải từ tuyên bố). Hệ thống có xu hướng tạo ra chính xác những gì bạn yêu cầu nó tạo ra -- hãy cẩn thận với những gì bạn yêu cầu.

Vẽ Mermaid diagram thể hiện system map.

Bước 3: Xác định Stocks & Flows

Stocks là những thứ tích lũy được, đo đếm được tại một thời điểm (tiền, dân số, kiến thức, niềm tin, ô nhiễm, danh tiếng). Flows là tốc độ thay đổi stocks (dòng vào, dòng ra).

Nguyên tắc quan trọng:

Stocks thay đổi chậm vì flows cần thời gian -- đây là nguồn gốc của stability VÀ delays
Stocks tạo ra momentum, inertia, và memory cho hệ thống
Hiểu stocks giúp hiểu tại sao hệ thống phản ứng chậm hơn ta mong đợi

Vẽ Mermaid diagram cho stocks & flows chính.

Bước 4: Lần theo Feedback Loops

Hai loại feedback loops:

Balancing loops (B): Tìm cách đưa hệ thống về trạng thái cân bằng. Có goal, so sánh hiện tại với goal, điều chỉnh. VD: Thermostat, cung-cầu, body temperature.

Reinforcing loops (R): Khuếch đại -- tăng trưởng hoặc sụp đổ theo cấp số nhân. VD: Lãi kép, viral spread, vicious cycles, virtuous cycles.

Xác định:

Loops nào đang dominant (chi phối hành vi hiện tại)?
Khi nào dominance có thể chuyển đổi?
Delays nào đang ẩn trong feedback loops?

Delays đặc biệt nguy hiểm: chúng gây overshoot, oscillation, và khiến ta hành động quá mạnh hoặc quá yếu. "Khi có delays dài trong feedback loops, tầm nhìn xa là thiết yếu."

Vẽ Mermaid diagram thể hiện feedback loops (dùng flowchart, ghi rõ B/R cho mỗi loop).

Bước 5: Phát hiện System Traps

Đọc references/system-traps.md để tra cứu 8 system traps phổ biến.

Với mỗi trap phát hiện được, ghi rõ:

Trap name và mô tả cơ chế
Biểu hiện cụ thể trong tình huống đang phân tích
Way out (cách thoát khỏi trap)

Lưu ý: Một hệ thống có thể rơi vào nhiều traps cùng lúc.

Bước 6: Tìm Leverage Points

Đọc references/leverage-points.md để tra cứu 12 leverage points (từ ít hiệu quả đến mạnh nhất).

Xác định:

Hiện tại người ta đang can thiệp ở đâu? (Thường là ở leverage points yếu: thay đổi số liệu, thay đổi parameters)
Can thiệp ở đâu sẽ hiệu quả hơn? (Thường là: thay đổi rules, goals, hoặc paradigm)
Cảnh báo: leverage points thường counterintuitive -- hướng đúng có thể ngược với trực giác
Bước 7: Đề xuất & Wisdom

Dựa trên phân tích, đề xuất hành động. Đọc references/systems-wisdom.md (15 nguyên tắc), chọn 2-4 nguyên tắc resonates nhất với vấn đề đang phân tích, và giải thích cách áp dụng cụ thể.

Xử lý chủ đề mơ hồ hoặc cá nhân

Khi chủ đề quá rộng/mơ hồ (VD: "phân tích xã hội Việt Nam"): Hỏi lại user để thu hẹp: "Khía cạnh nào bạn quan tâm nhất?" hoặc tự chọn góc cụ thể và nói rõ: "Mình sẽ phân tích từ góc X, vì đây là nơi feedback loops rõ nhất."

Khi chủ đề là vấn đề cá nhân (VD: "tại sao mình cứ trì hoãn"): Vẫn áp dụng đủ 7 bước, nhưng:

Elements bao gồm cảm xúc, niềm tin, thói quen (intangible stocks)
Feedback loops có thể là internal (suy nghĩ → cảm xúc → hành vi → kết quả → suy nghĩ)
Leverage points tập trung vào information flows (nhận thức) và paradigm (niềm tin sâu)
Giọng văn empathetic hơn, tránh lạnh lùng phân tích
Quy tắc output
Viết bằng tiếng Việt, giọng sâu lắng nhưng rõ ràng
Dùng Mermaid diagrams cho system maps, stocks & flows, feedback loops (dùng text thuần trong node labels, tránh emoji để đảm bảo render đúng trên mọi nền tảng)
Theo template trong templates/analysis-output.md
Mỗi phần phân tích đều kèm ví dụ cụ thể từ tình huống của user
Đừng chỉ liệt kê framework -- hãy thực sự phân tích, thực sự suy nghĩ
Ưu tiên insight bất ngờ, counterintuitive hơn là xác nhận điều hiển nhiên
Kết thúc bằng "Câu hỏi mở" -- những câu hỏi mà phân tích chưa trả lời được, để user tiếp tục suy nghĩ
Weekly Installs
10
Repository
hoangvantuan/cl…e-plugin
First Seen
Mar 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn