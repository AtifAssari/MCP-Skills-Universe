---
title: wechat-article-formatter
url: https://skills.sh/bnd-1/wechat_article_mini/wechat-article-formatter
---

# wechat-article-formatter

skills/bnd-1/wechat_article_mini/wechat-article-formatter
wechat-article-formatter
Installation
$ npx skills add https://github.com/bnd-1/wechat_article_mini --skill wechat-article-formatter
SKILL.md
微信公众号文章格式化（小龙虾极速版）
核心理念：默认精美，一键完成
执行流程（3步搞定）
步骤1：找到文章
场景	处理方式
用户给了文件路径	直接用
用户粘贴了内容	先 Write 保存为 .md
刚写完文章	自动找最新的 .md 文件
只说"美化文章"	问一下路径
# 自动检测最新文章
ls -t *.md 2>/dev/null | head -1

步骤2：使用精美模板转换

默认使用 VSCode 蓝色科技风 模板，不需要问用户选主题。

执行方式：

读取 examples/VSCode 蓝色科技风.html 模板
跳过 Markdown 中的 H1 标题（微信有独立标题栏）
在 HTML 开头添加：<!-- ⚠️ 标题请在微信公众号编辑器中单独填写 -->
将 Markdown 内容映射到模板的组件结构中：
导语块 → 文章开头引子
序号章节标题 → H2 标题
功能卡片 → 要点列表
操作步骤 → 教程内容
转换代码块格式（如有代码）：
python scripts/convert-code-blocks.py input.html output.html

输出 {文件名}_formatted.html

如果用户不满意默认模板，再提供选择：

模板	适用场景
VSCode 蓝色科技风	技术文章（默认）
红蓝对决·深度测评	对比评测
极客暗黑风	深度技术
现代极简风	通用文章
步骤3：告诉用户结果
✅ 文章已格式化！

文件：{输出路径}

你可以：
1. 说"推送到微信"→ 直接发布到公众号草稿箱
2. 在浏览器打开预览：file://{绝对路径}
3. 手动操作：浏览器打开HTML → Ctrl+A全选 → Ctrl+C复制 → 粘贴到微信编辑器

⚠️ 记得在微信编辑器的标题栏填写文章标题

错误处理
问题	解决
文件找不到	问用户路径
代码没高亮	检查 Markdown 是否指定了语言
图片不显示	提醒在微信编辑器重新上传
样式不满意	提供其他模板选择
与其他skill联动

写完文章 → 说"美化文章"触发本skill → 说"推送到微信"触发 publisher

Weekly Installs
25
Repository
bnd-1/wechat_ar…cle_mini
GitHub Stars
2
First Seen
Mar 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass