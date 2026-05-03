---
rating: ⭐⭐⭐
title: webp-to-jpg
url: https://skills.sh/steelan9199/wechat-publisher/webp-to-jpg
---

# webp-to-jpg

skills/steelan9199/wechat-publisher/webp-to-jpg
webp-to-jpg
Installation
$ npx skills add https://github.com/steelan9199/wechat-publisher --skill webp-to-jpg
SKILL.md
WebP到JPG转换技能
功能概述

此技能将帮助您将WebP格式的图片转换为JPG格式，以便在不支持WebP格式的平台上使用。

使用场景
在微信公众号等不支持WebP格式的平台上使用图片
将WebP图片转换为更通用的JPG格式
准备适合特定平台的图片格式
转换步骤

检查Pillow库：确认系统已安装Pillow库用于图片处理

python -c "from PIL import Image; print('Pillow is available')"


安装Pillow库（如果没有安装）：

pip install Pillow


执行格式转换：

from PIL import Image

# 打开WebP图片
img = Image.open('<webp_image_path>')

# 转换为RGB模式（因为JPG不支持透明度）
rgb_img = img.convert('RGB')

# 保存为JPG格式
rgb_img.save('<jpg_image_path>', 'JPEG')

完整转换命令

直接使用Python命令行进行转换：

python -c "from PIL import Image; img = Image.open('<webp_image_path>'); rgb_img = img.convert('RGB'); rgb_img.save('<jpg_image_path>', 'JPEG'); print('图片转换成功')"


将 <webp_image_path> 替换为您的WebP图片路径，将 <jpg_image_path> 替换为您想要保存的JPG图片路径。

注意事项
JPG格式不支持透明度，所以WebP的透明部分会被转换为白色背景
转换后的图片质量可能会略有变化
确保目标路径有写入权限
Weekly Installs
65
Repository
steelan9199/wec…ublisher
GitHub Stars
5
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass