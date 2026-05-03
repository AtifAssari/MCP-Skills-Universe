---
title: 1password
url: https://skills.sh/iamzhihuix/happy-claude-skills/1password
---

# 1password

skills/iamzhihuix/happy-claude-skills/1password
1password
Installation
$ npx skills add https://github.com/iamzhihuix/happy-claude-skills --skill 1password
SKILL.md
1Password CLI

使用 op CLI 管理 1Password vault 中的密码和 API credentials。

前置检查

使用前确认 op 已安装并已集成桌面 App：

op --version


未安装则引导安装：

brew install --cask 1password-cli


安装后需在 1Password 桌面 App 中开启集成：Settings → Developer → Integrate with 1Password CLI。

保存 API Credential

用户提供 API Key 信息时，使用以下命令保存。字段按实际提供情况填写，未提供的字段省略。

标题命名规范： {服务商} API Key - {用途标识}（如 OpenAI API Key - agent）

op item create \
  --category="API Credential" \
  --title="{标题}" \
  --vault="Personal" \
  "credential={API Key}" \
  "website[url]={网站 URL}" \
  "base_url[text]={API base URL}" \
  "username[text]={邮箱或用户名}" \
  "用途说明[text]={用途描述}" \
  "过期时间[text]={YYYY-MM-DD}" \
  "创建日期[text]={YYYY-MM-DD}" \
  --tags "{服务商},{项目标签}"


最小必填字段： credential（API Key 本身）。其余字段按用户提供情况填入。

查询/搜索条目

按标题或 URL 关键词模糊查找：

op item list --format=json | python3 -c "
import json, sys
items = json.load(sys.stdin)
keyword = '{关键词}'.lower()
for i in items:
    title_match = keyword in i['title'].lower()
    url_match = any(keyword in str(u) for u in i.get('urls', []))
    if title_match or url_match:
        print('ID:', i['id'], '| Title:', i['title'], '| Updated:', i.get('updated_at', ''))
"

读取 Credential
# 读取（隐藏值）
op item get "{标题}" --fields credential

# 读取（显示明文）
op item get "{标题}" --fields credential --reveal

注入环境变量（开发工作流）

在 .env 文件中使用 Secret References 代替明文，可以安全提交到 git：

OPENAI_API_KEY=op://Personal/OpenAI API Key - agent/credential
DEEPSEEK_API_KEY=op://Personal/DeepSeek API Key - agent skd/credential


运行脚本时注入真实值：

op run --env-file=.env -- your-script.sh
op run --env-file=.env -- python3 main.py

Vault 管理
# 查看所有 vault
op vault list

# 查看某 vault 下所有条目
op item list --vault="Personal"

# 按 tag 筛选
op item list --tags "deepseek"

工作流示例

用户说「帮我保存 OpenAI 的 API Key：sk-xxx」时：

确认 op 已安装可用
收集信息：服务商名、API Key、网站 URL、用途、关联项目（按用户提供情况）
执行 op item create 保存
输出保存结果（ID、标题、字段列表），不显示 credential 明文
Weekly Installs
21
Repository
iamzhihuix/happ…e-skills
GitHub Stars
284
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail