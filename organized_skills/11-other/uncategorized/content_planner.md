---
rating: ⭐⭐⭐
title: content-planner
url: https://skills.sh/hoangvantuan/claude-plugin/content-planner
---

# content-planner

skills/hoangvantuan/claude-plugin/content-planner
content-planner
Installation
$ npx skills add https://github.com/hoangvantuan/claude-plugin --skill content-planner
SKILL.md
Content Planner

Blog-first content workflow: Plan → Write ALL blogs → Derive social posts (1 blog = 1 social).

Nguyên tắc cốt lõi:

Blog là bản gốc chứa 100% nội dung — luôn viết trước, cover toàn bộ input
Mỗi blog tự động có 1 bài social tương ứng — derive từ content blog đó
VD: N blog topics → N blog articles + N social posts (1:1)
Phase 1: Plan
Step 1: Detect Input

Xác định loại input từ user:

Topic thuần — chỉ có chủ đề, cần research từ đầu
Notes/outline — có sẵn ý tưởng, cần structure lại
URL — bài viết/tài liệu online, cần phân tích + mở rộng
File/document — tài liệu đã có, cần extract ideas
Step 2: Interview

Hỏi tất cả câu hỏi trong 1 lượt để tiết kiệm thời gian:

Audience: Ai là người đọc chính? (VD: startup founders, marketer, developer...)
Tone: Tone bạn muốn? (chuyên gia / thân thiện / provocative / storytelling)
Goals: Mục tiêu chính? (educate / engage / convert / thought leadership)
(Optional) Constraints: Có yêu cầu đặc biệt nào không? (deadline, brand guidelines, topics to avoid)
Edge Cases
Input quá ngắn (1-2 câu, không có detail): Hỏi user bổ sung context hoặc dùng web research mở rộng. Giới hạn blog types khả dụng: How-to Guide, Quick Insight, Listicle
Thiếu data cho Deep Analysis / Case Study: Nếu web research không đủ data/số liệu → chuyển sang type phù hợp hơn (Opinion, Explainer) thay vì viết với data thiếu
Input là chủ đề quá rộng: Narrow down bằng Interview (Step 2) — yêu cầu user chọn góc cụ thể trước khi plan
Step 3: Research
WebSearch 3-5 queries liên quan topic + audience + trends
Nếu input là URL → WebFetch phân tích nội dung
Thu thập: data, số liệu, góc nhìn mới, content gaps
Ghi nguồn cho mọi data point
Step 4: Generate Content Plan

Đề xuất số lượng blog articles cover toàn bộ nội dung input:

Topic thuần → 3-10 bài (tùy scope)
Notes/outline → theo số ý tưởng có sẵn
URL/article → 5-15 bài (tùy độ dài + density)
Sách/tài liệu dài → bao phủ toàn bộ giá trị cốt lõi — số bài tỷ lệ thuận với số concepts/chapters cốt lõi, KHÔNG đặt giới hạn trần. Chia thành batches (mỗi batch ~10 bài) để quản lý. Đảm bảo không bỏ sót chapter/concept quan trọng nào.

Nguyên tắc:

Số lượng bài phục vụ mục tiêu truyền tải đầy đủ nội dung gốc. Quality không đánh đổi quantity — mỗi bài vẫn phải self-contained và có giá trị độc lập.
1 bài = 1 chủ đề duy nhất. Mỗi blog tập trung vào đúng 1 ý chính (concept, framework, câu chuyện, bài học). Nếu 1 chapter/section chứa nhiều ý độc lập → tách thành nhiều bài. Không nhồi 2-3 chủ đề vào 1 bài — reader chỉ nhớ được 1 takeaway.

Mỗi bài có brief (blog + social paired):

### Bài [N]: [Tiêu đề đề xuất]

**Blog:**
- **Type:** [Load từ references/blog-types.md]
- **Framework:** [Chọn theo type — xem mapping trong references/blog-types.md]
- **Angle:** [Góc tiếp cận cụ thể]
- **Key points:** [3-5 bullet points]
- **Word count:** [Ước tính]

**Social (derive từ blog):**
- **Type:** [Load từ references/facebook-types.md]
- **Hook idea:** [1-2 câu hook — extract từ insight mạnh nhất của blog]
- **CTA:** [Call to action]

Step 5: Save Output
{CWD}/{output-dir}/plan.md — overview + tất cả briefs (nếu nhiều batch thì ghi rõ batch nào)
{CWD}/{output-dir}/research.md — data đã research với sources

Với input dài (sách, tài liệu lớn):

Trước tiên, tạo content map tổng quan: liệt kê tất cả chapters/concepts cốt lõi cần cover
Chia thành batches, mỗi batch ~10 bài, plan batch đầu tiên chi tiết
Hỏi user confirm trước khi plan batch tiếp theo
Coverage check (BẮT BUỘC): Sau mỗi batch, đối chiếu content map — liệt kê rõ concepts nào ĐÃ cover, concepts nào CHƯA cover. Tiếp tục plan batch mới cho đến khi 100% content map được cover. KHÔNG dừng sớm chỉ vì đã đạt số bài "tròn"

Hỏi user: "Plan đã xong với [N] bài blog + [N] bài social. Bạn muốn bắt đầu viết? (VD: 'viết batch 1' hoặc 'viết tất cả')"

Phase 2: Write Blogs

Trigger: User confirm viết (VD: "viết tất cả" hoặc "viết batch 1").

Blog luôn được viết trước 100%. Social posts sẽ derive ở Phase 3 sau khi blog hoàn thành.

Step 1: Read Plan

Đọc plan.md từ output dir để lấy briefs.

Step 2: Write ALL Blog Articles

Viết toàn bộ blog articles trong batch/plan — không bỏ sót bài nào:

Load type guidelines từ references/blog-types.md
Load references/writing-system.md — áp dụng full writing system
Load framework từ references/content-frameworks.md
Viết full content theo brief + type structure + framework + writing system
Markdown format, đúng structure template của type, headings viết như insight
Step 3: Save Blog Articles

Mỗi bài lưu file riêng: {CWD}/{output-dir}/blog-[NN]-[type]-[slug].md

Sau khi viết xong toàn bộ blog, tự động chuyển sang Phase 3.

Phase 3: Derive Social Posts

Trigger: Tự động sau khi Phase 2 hoàn thành (toàn bộ blog đã viết xong).

Mỗi blog article → 1 social post tương ứng. Mapping 1:1 bắt buộc.

Step 1: Read Blog Article

Đọc blog article vừa viết để extract nội dung cốt lõi.

Step 2: Derive Social Post

Với mỗi blog article:

Load type guidelines từ references/facebook-types.md — chọn type phù hợp theo brief
Load references/writing-system.md — áp dụng anti-AI writing + tone
Extract insight mạnh nhất, story hấp dẫn nhất, hoặc controversial take từ blog
Rewrite cho social format — KHÔNG copy-paste từ blog, mà viết lại cho platform
Plain text, xuống dòng nhiều, hook 3 dòng đầu phải mạnh
Không dùng outbound links (giảm reach) — social post phải self-contained, đọc độc lập được
Step 3: Save Social Posts

Mỗi bài lưu file riêng: {CWD}/{output-dir}/fb-[NN]-[type]-[slug].md

File naming đảm bảo [NN] khớp với blog tương ứng (blog-03 → fb-03).

Constraints
Output tiếng Việt (trừ khi user yêu cầu khác)
Blog luôn viết trước 100%, social derive sau — không đảo thứ tự
Mapping 1:1 bắt buộc: mỗi blog có đúng 1 social post tương ứng
Blog phải đúng structure template theo type definition trong references
Social post KHÔNG copy-paste từ blog — rewrite cho platform, giữ essence
Mỗi bài viết self-contained, đọc độc lập được
Research data phải cite nguồn
Không giới hạn số bài/plan — số lượng tỷ lệ với số concepts cốt lõi trong input, KHÔNG neo vào bất kỳ con số cố định nào. Với input dài (sách, khóa học), chia thành batches ~10 bài, plan từng batch tuần tự + coverage check sau mỗi batch cho đến khi bao phủ 100% content map
Default output dir: {CWD}/content-planner/[topic-slug]/ nếu user không chỉ định
Output Format

Phase 1 output plan.md:

# Content Plan: [Topic]

## Overview
- Audience: [...]
- Tone: [...]
- Goals: [...]
- Tổng số blog: [N]
- Tổng số social: [N] (1:1 với blog)

## Briefs
[Briefs theo format ở Step 4 — mỗi brief gồm cả Blog + Social paired]

## Thứ tự viết
1. Blog: Viết toàn bộ [N] bài blog trước
2. Social: Derive [N] bài social từ blog đã viết


Phase 2 output: Mỗi blog theo structure template của type tương ứng trong references/. Phase 3 output: Mỗi social post theo type guidelines trong references/facebook-types.md.

References
references/writing-system.md — Writing system dùng chung (archetypes, anti-AI writing, self-critique, power techniques)
references/blog-types.md — 6 blog type guidelines
references/facebook-types.md — 4 Facebook post types
references/content-frameworks.md — Writing frameworks (PAS, Inverted Pyramid, etc.)
Weekly Installs
34
Repository
hoangvantuan/cl…e-plugin
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn