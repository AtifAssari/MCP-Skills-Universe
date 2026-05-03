---
title: wechat-draft-publisher
url: https://skills.sh/bnd-1/wechat_article_mini/wechat-draft-publisher
---

# wechat-draft-publisher

skills/bnd-1/wechat_article_mini/wechat-draft-publisher
wechat-draft-publisher
Installation
$ npx skills add https://github.com/bnd-1/wechat_article_mini --skill wechat-draft-publisher
SKILL.md
微信公众号草稿发布器（小龙虾极速版）
核心理念：首次引导配置，之后一键发布
前置：安装依赖

每次使用前，先确保依赖已安装（幂等操作，可重复执行）：

pip3 install -r skills/wechat-draft-publisher/requirements.txt

首次使用：引导配置
第1步：查询IP并告知用户

每次首次使用或遇到IP白名单错误时，先帮用户查询IP：

python publisher.py --query-ip


这会自动查询公网IP并显示：

>>> 你的公网IP是: x.x.x.x

请将此IP添加到微信公众号后台:
1. 登录 https://developers.weixin.qq.com/platform
2. 设置与开发 → 基本配置 → IP白名单
3. 添加IP: x.x.x.x


告诉用户：

首次使用需要配置两件事：

1. IP白名单：我已查到你的服务器IP是 x.x.x.x
   请登录微信公众号后台，在 设置与开发→基本配置→IP白名单 中添加这个IP

2. AppID和AppSecret：
   在同一页面（基本配置）中复制AppID和AppSecret
   运行发布工具时会自动引导你填写

配置好了告诉我，我就帮你发布！

第2步：运行发布器（自动引导输入凭证）
python publisher.py --title "文章标题" --content article.html


首次运行会自动提示输入 AppID 和 AppSecret。

正常发布流程（配置完成后）
一键发布
python publisher.py \
  --title "文章标题" \
  --content xxx_formatted.html \
  --cover cover.png \
  --author "小龙虾"

自动执行步骤
找 HTML 文件：优先 *_formatted.html，回退最新 .html
提取标题：从 HTML 注释或文件名
找封面图：cover.png
调用发布：上传封面 → 上传内容图片 → 创建草稿
返回结果：显示 media_id，提示去后台查看
发布成功后提示
✅ 文章已推送到草稿箱！

接下来：
1. 登录 https://developers.weixin.qq.com/platform
2. 进入"草稿箱"
3. 预览效果，确认后发布

⚠️ 草稿不会自动发布，你可以在后台编辑后再发

常见错误速查
错误	原因	解决
invalid ip not in whitelist	IP不在白名单	运行 python publisher.py --query-ip 查IP并添加
AppSecret error	凭证错误	检查 ~/.wechat-publisher/config.json
title size out of limit	标题太长	工具会自动截断，无需处理
api功能未授权	公众号类型不支持	需要认证的服务号
配置文件位置

~/.wechat-publisher/config.json

{
  "appid": "xxx",
  "appsecret": "xxx"
}

完整工作流联动
写文章(tech-writer/pm-writer) → 美化格式(formatter) → 推送到微信(本skill)


用户只需要说三句话：

"写一篇关于XXX的文章"
"美化文章"
"推送到微信"
Weekly Installs
29
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