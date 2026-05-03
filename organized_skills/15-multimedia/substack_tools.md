---
rating: ⭐⭐
title: substack-tools
url: https://skills.sh/hoangvantuan/claude-plugin/substack-tools
---

# substack-tools

skills/hoangvantuan/claude-plugin/substack-tools
substack-tools
Installation
$ npx skills add https://github.com/hoangvantuan/claude-plugin --skill substack-tools
SKILL.md
Substack Tools

CLI tự động quản lý bài viết Substack: draft, schedule, publish, list, sections, batch operations + scan/crawl newsletter khác (lấy tất cả bài qua archive API). Dùng python-substack (reverse-engineered) + public JSON API (/api/v1/).

Thiết lập ban đầu
Dependencies
test -d ~/.venv/claude || uv venv ~/.venv/claude
uv pip install --python ~/.venv/claude/bin/python python-substack feedparser httpx beautifulsoup4 markdownify

Cấu hình credentials

Script cần 2 biến: SUBSTACK_COOKIE và SUBSTACK_PUBLICATION_URL. Tìm theo thứ tự: env var → .env trong thư mục skill → .env trong CWD.

Cách	Khi nào
Env var (~/.zshrc)	Dùng thường xuyên — set 1 lần, dùng mãi
File .env	Nhiều publication — mỗi thư mục 1 .env (cần python-dotenv)

Lấy cookie: Substack dashboard (đã login) → F12 → Application → Cookies → copy substack.sid. Hết hạn sau 1-2 tuần.

Chi tiết setup lần đầu → setup-guide.

Commands
PY=~/.venv/claude/bin/python
SCRIPT=<skill-path>/scripts/substack_cli.py

draft — Tạo draft
$PY $SCRIPT draft ARTICLE.md COVER.png [--section "Tên section"] [--subtitle "..."]

ARTICLE.md: dòng 1 = title (tự strip #), dòng 2+ = body markdown
COVER.png: upload lên S3 Substack, chèn đầu bài làm cover + inline image
schedule — Tạo draft + lên lịch
$PY $SCRIPT schedule ARTICLE.md COVER.png --at 2026-04-20T09:00:00 [--audience everyone]

Flag	Mặc định	Giá trị
--at	bắt buộc	ISO 8601. Không timezone → dùng local. Có timezone → dùng luôn
--audience	everyone	everyone / only_paid / only_free / founding
publish — Tạo draft + đăng ngay
$PY $SCRIPT publish ARTICLE.md COVER.png [--no-send]


CẢNH BÁO: không reversible. Bài lên public ngay, email gửi subscriber không recall được. Luôn hỏi user xác nhận trước khi chạy publish.

publish-existing — Đăng draft đã có
$PY $SCRIPT publish-existing DRAFT_ID [--no-send]

unschedule — Huỷ lịch, chuyển về draft
$PY $SCRIPT unschedule DRAFT_ID

list — Liệt kê bài
$PY $SCRIPT list [--filter draft|scheduled|published|all] [--limit 25]

sections — Liệt kê newsletter sections
$PY $SCRIPT sections

set-section — Gán section cho nhiều draft
$PY $SCRIPT set-section "Tên Section" DRAFT_ID1 DRAFT_ID2 ...

Scan / Crawl newsletter khác (read-only, không cần auth)
scan — Quét danh sách bài
$PY $SCRIPT scan <slug> [--limit 10] [--json] [--all]

slug: slug Substack (vd: platformer), full URL, hoặc domain
Hiển thị bảng: ngày, tác giả, tiêu đề
--json: output JSON thay vì bảng
--all: lấy TẤT CẢ bài qua archive API (mặc định dùng RSS, tối đa ~25 bài)
crawl — Tải 1 bài thành .md
$PY $SCRIPT crawl <URL> [--output-dir ./crawled]

Tải full bài, convert HTML → Markdown, lưu với YAML frontmatter
Skip nếu file đã tồn tại (idempotent)
crawl-feed — Batch tải N bài từ feed
$PY $SCRIPT crawl-feed <slug> [--limit 5] [--output-dir ./crawled] [--all]

Mặc định: tải N bài mới nhất từ RSS
--all: tải TẤT CẢ bài qua archive API (bỏ qua --limit)
Delay tự động 2-5s random giữa mỗi bài (tránh rate limit)

Chi tiết troubleshooting → crawl-guide.

Flags chung
--dry-run: in payload, không gọi API. Đặt SAU tên subcommand.
--section "...": gán bài vào section (áp dụng cho draft/schedule/publish).
--subtitle "...": subtitle hiển thị dưới title.
Ranh giới hành động
Tự làm	Phải hỏi user trước
draft, schedule, list, sections, set-section, unschedule	publish / publish-existing — gửi email thật, không recall được
scan, crawl, crawl-feed (read-only)	Xoá bài đã publish
--dry-run để kiểm tra payload	

Không commit .env — chứa cookie auth.

Tài liệu tham khảo
references/setup-guide.md — chi tiết cấu hình credentials lần đầu
references/api-quirks.md — endpoint quirks, rate limit, troubleshooting
references/batch-operations.md — pattern delay + retry cho batch schedule
references/crawl-guide.md — troubleshooting scan/crawl: selectors, rate limit, paywall
Weekly Installs
9
Repository
hoangvantuan/cl…e-plugin
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn