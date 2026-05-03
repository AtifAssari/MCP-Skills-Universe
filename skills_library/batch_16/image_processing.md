---
title: image-processing
url: https://skills.sh/z0gsh1u/oh-my-writing-skill/image-processing
---

# image-processing

skills/z0gsh1u/oh-my-writing-skill/image-processing
image-processing
Installation
$ npx skills add https://github.com/z0gsh1u/oh-my-writing-skill --skill image-processing
SKILL.md
图片处理 Skill

你是一个图片处理助手，负责为配图添加文字标注和装饰效果。

核心能力
底部边框式配文：在图片下方添加独立的文字区域，类似画框效果
内部贴纸式配文：在图片内部添加带背景的文字标签，类似小红书贴纸效果
中文支持：使用 Windows 系统自带的微软雅黑字体
Emoji 支持：使用 pilmoji 库渲染 Emoji 表情
使用方式
模式 1：底部边框式配文

在图片下方添加白色/深色背景的文字区域：

python scripts/image_processor.py input.jpg output.jpg --mode frame --text "这是配文 🎉"


效果示例：

┌────────────────────┐
│                    │
│      原图片         │
│                    │
├────────────────────┤
│  这是配文 🎉        │
└────────────────────┘


参数：

--mode frame：边框模式
--text：配文内容（支持中文和 Emoji）
--bg-color：背景颜色（默认 white，可用 black、#RRGGBB）
--text-color：文字颜色（默认 black）
--font-size：字体大小（默认 32）
--padding：内边距（默认 20）
模式 2：内部贴纸式配文

在图片内部指定位置添加带背景的文字标签：

python scripts/image_processor.py input.jpg output.jpg --mode sticker --text "重点！" --position bottom-right


效果示例：

┌────────────────────┐
│                    │
│      原图片    ┌───┤
│               │重点│
└───────────────┴───┘


参数：

--mode sticker：贴纸模式
--text：配文内容
--position：位置，可选 top-left、top-right、bottom-left、bottom-right、center
--bg-color：标签背景色（默认 #FFE4B5，浅橙色）
--text-color：文字颜色（默认 #333333）
--font-size：字体大小（默认 28）
--opacity：背景透明度 0-255（默认 230）
--radius：圆角半径（默认 10）
--margin：距边缘距离（默认 20）
批量处理

处理多张图片：

python scripts/image_processor.py ./images/*.jpg --output-dir ./output --mode frame --text "配文"

字体配置

脚本会按以下顺序查找中文字体：

C:/Windows/Fonts/msyh.ttc - 微软雅黑
C:/Windows/Fonts/simhei.ttf - 黑体
C:/Windows/Fonts/simsun.ttc - 宋体
系统默认字体（可能不支持中文）

如需使用自定义字体：

python scripts/image_processor.py input.jpg output.jpg --font "C:/MyFonts/custom.ttf" --text "配文"

颜色参考

常用颜色值：

名称	代码	用途
白色	white / #FFFFFF	边框背景
黑色	black / #000000	深色背景/文字
浅橙	#FFE4B5	贴纸背景
浅蓝	#E3F2FD	贴纸背景
浅绿	#E8F5E9	贴纸背景
浅粉	#FCE4EC	贴纸背景
与其他 Skill 配合
使用 图片搜索 Skill 找到合适的配图
使用本 Skill 添加配文
在 通用写作 Skill 中引用处理后的图片
注意事项
图片格式：支持 JPG、PNG、WEBP 等常见格式
输出格式：根据输出文件扩展名自动选择格式
Emoji 渲染：需要安装 pilmoji 库
字体权限：确保对字体文件有读取权限
Weekly Installs
86
Repository
z0gsh1u/oh-my-w…ng-skill
GitHub Stars
21
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass