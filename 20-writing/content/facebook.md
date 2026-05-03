---
title: facebook
url: https://skills.sh/hoangvantuan/claude-plugin/facebook
---

# facebook

skills/hoangvantuan/claude-plugin/facebook
facebook
Installation
$ npx skills add https://github.com/hoangvantuan/claude-plugin --skill facebook
SKILL.md
Facebook Automation via PinchTab

Đăng bài Facebook (wall/group) + đính kèm ảnh + tag bạn bè qua PinchTab browser control.

Prerequisites
PinchTab installed và server đang chạy (pinchtab server &)
Một PinchTab profile có Facebook login session (cookies đã lưu từ lần login thủ công trước)
Bật pinchtab config set security.allowEvaluate true (bắt buộc cho image upload, khuyến khích cho text input)

Nếu user chưa login: hướng dẫn start headed instance → login thủ công → reuse profile.

Script Usage

Script: scripts/fb-post.sh

# Positional syntax
bash scripts/fb-post.sh "<content>" [options]

# Named syntax
bash scripts/fb-post.sh --content "<content>" [options]


Parameters:

Param	Required	Default	Description
<content>	Yes	—	Post content (positional arg hoặc --content)
--profile	No	default	PinchTab profile name
--user-id	No	100003782705460	Facebook numeric ID (wall mode)
--group	No	—	Group slug hoặc full URL → post vào group thay vì wall
--title	No	—	Tiêu đề bài viết (chỉ group, hiển thị bold phía trên nội dung)
--image	No	—	Đường dẫn ảnh đính kèm (dùng nhiều lần cho nhiều ảnh, tối đa 8)
--tag	No	—	Tên hiển thị của bạn bè cần tag
--tag-id	No	—	Facebook ID của bạn bè (chính xác hơn search theo tên)
--publish	No	false	true = đăng ngay, false = chỉ soạn (user review trước)
--mode	No	headless	headed = hiển thị browser, headless = chạy nền
--debug	No	false	Chụp screenshot mỗi bước vào /tmp/ (flag, không cần value: --debug)
--dry-run	No	—	Log actions mà không mở browser (kiểm tra params)
--keep-instance	No	—	Giữ browser instance sau khi xong (dùng cho chain nhiều posts)
Post lên Wall
bash scripts/fb-post.sh "Hello world!"
bash scripts/fb-post.sh "Hello!" --tag "Hoang Van Tuan" --publish true

Post với ảnh đính kèm
bash scripts/fb-post.sh "Check this out!" --image /path/to/photo.jpg --publish true
bash scripts/fb-post.sh "Ảnh đẹp!" --image photo1.jpg --image photo2.jpg --tag "Ngoc" --group tuhoccungai --publish true

Post vào Group
bash scripts/fb-post.sh "Hello group!" --group tuhoccungai --publish true
bash scripts/fb-post.sh "Nội dung" --group "https://www.facebook.com/groups/tuhoccungai" --keep-instance --publish true
bash scripts/fb-post.sh "Nội dung bài viết" --title "[Series AI Agent] Vòng lặp nghĩ-làm" --group tuhoccungai --publish true

Exit Codes & Lỗi thường gặp
Code	Meaning	Nguyên nhân & cách xử lý
0	Thành công	—
1	Sai arguments	Thiếu content, --user-id nhận vanity URL thay vì numeric ID, file ảnh không tồn tại hoặc sai format (script validate magic bytes trước khi mở browser)
2	Instance failure	PinchTab chưa chạy (pinchtab server &) hoặc profile không tồn tại
3	Element not found	FB UI thay đổi, group URL sai, không có quyền. Dùng --debug kiểm tra screenshot
4	Publish failed	Nút đăng không tìm thấy
5	Upload failed	security.allowEvaluate tắt → pinchtab config set security.allowEvaluate true. Ảnh dispatch nhưng không attach → verify blob: URL trong 10s

Lỗi AI hay mắc (không báo exit code):

Quên --publish true — default là false, user phải xác nhận trước khi thêm
Tag sai người — nhiều người trùng tên, dùng --tag-id cho chính xác
Content chứa quotes — wrap bằng double quotes, escape " bên trong
Chi tiết kỹ thuật

Cách script hoạt động, instance lifecycle, troubleshooting → internals. Đọc khi cần debug hoặc xử lý sự cố.

Weekly Installs
20
Repository
hoangvantuan/cl…e-plugin
First Seen
Mar 21, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn