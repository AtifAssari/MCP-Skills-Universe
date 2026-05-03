---
rating: ⭐⭐
title: sofunny-image
url: https://skills.sh/yhx0516/ai-toolkits/sofunny-image
---

# sofunny-image

skills/yhx0516/ai-toolkits/sofunny-image
sofunny-image
Installation
$ npx skills add https://github.com/yhx0516/ai-toolkits --skill sofunny-image
SKILL.md
sofunny-image
何时使用

在以下场景使用本 skill：

用户要生成图片，而当前客户端主模型并不适合直接承担图片输出
用户要上传一张或多张参考图，再结合文本生成新图片
用户要通过 New-API 出图，并按模型前缀自动选择 Gemini 原生接口或 OpenAI Images API
用户希望优先复用：
进程环境变量
~/.sofunny-image.env

如果只是普通文本问答、代码生成或工具调用，不要使用本 skill。

配置来源

脚本按以下顺序读取配置：

~/.sofunny-image.env
当前 shell 的环境变量

命令行参数 --base-url、--api-key、--model 会覆盖以上配置。

如果没有检测到 ~/.sofunny-image.env，脚本会提示你创建该文件并写入所需变量模板。

优先使用这些变量：

SOFUNNY_BASE_URL
SOFUNNY_API_KEY
SOFUNNY_MODEL

支持的模型：

gemini-3.1-flash-image-preview（Gemini 原生接口）
gemini-3-pro-image-preview（Gemini 原生接口）
gpt-image-2（OpenAI Images API）

默认期望值：

SOFUNNY_BASE_URL=http://127.0.0.1:3000
SOFUNNY_MODEL=gpt-image-2
安装与执行入口
推荐将仓库目录软链接到：
${CLAUDE_PLUGIN_ROOT}/skills/sofunny-image
可执行脚本入口：
${CLAUDE_PLUGIN_ROOT}/skills/sofunny-image/scripts/sofunny-image.js
快速用法

文本生图：

node ${CLAUDE_PLUGIN_ROOT}/skills/sofunny-image/scripts/sofunny-image.js \
  --prompt "生成一张 16:9 的极简香蕉海报，不要任何文字。"


参考图编辑：

node ${CLAUDE_PLUGIN_ROOT}/skills/sofunny-image/scripts/sofunny-image.js \
  --prompt "保持主体不变，把背景改成晨雾中的山谷。" \
  --input /absolute/path/to/ref-1.png \
  --input /absolute/path/to/ref-2.jpg


指定输出、比例和分辨率：

node ${CLAUDE_PLUGIN_ROOT}/skills/sofunny-image/scripts/sofunny-image.js \
  --prompt "生成一张赛博朋克风格香蕉图标。" \
  --aspect-ratio 1:1 \
  --image-size 2K \
  --output /tmp/banana-icon.png


使用 gpt-image-2 文生图：

node ${CLAUDE_PLUGIN_ROOT}/skills/sofunny-image/scripts/sofunny-image.js \
  --model gpt-image-2 \
  --prompt "生成一张极简风格的蓝色机械鸟海报，不要文字。"


使用 gpt-image-2 图生图：

node ${CLAUDE_PLUGIN_ROOT}/skills/sofunny-image/scripts/sofunny-image.js \
  --model gpt-image-2 \
  --prompt "保留主体轮廓，把材质改成磨砂陶瓷。" \
  --input /absolute/path/to/ref-1.png

参数说明
--prompt：必填，图片生成或编辑指令
--input：可重复传入，一张或多张参考图
--output：可选，输出文件路径
--size：可选，OpenAI 图片尺寸；支持 1024x1024、1024x1536、1536x1024、auto；未传时不发送该字段，由上游使用默认 auto
--quality：可选，OpenAI 图片质量；支持 low、medium、high、auto；未传时不发送该字段
--background：可选，OpenAI 背景参数；支持 transparent、opaque、auto
--output-format：可选，OpenAI 输出格式；支持 png、webp、jpeg；未传时不发送该字段
--output-compression：可选，OpenAI 输出压缩率；未传时不发送该字段
--aspect-ratio：可选，默认 16:9
--image-size：可选，默认 1K
--model：可选，默认读取配置，兜底为 gpt-image-2；gemini-* 走 Gemini 原生接口，gpt-image-* 走 OpenAI Images API
--base-url：可选，覆盖配置中的 base URL
--api-key：可选，覆盖配置中的 token
工作流
收集用户的 prompt、参考图、输出路径和画幅要求。
改图/修图判断：当用户提供了图片路径、截图、或明确要求"改图"、"修图"、"基于这张图"、"编辑这张图"时，必须将图片路径作为 --input 参数传递。没有 --input 的调用只会走纯文生图，参考图会被完全忽略。
如果用户提到的图片是对话中之前生成的，使用之前保存的输出路径作为 --input。
如果用户提供了截图或粘贴了图片路径，确认路径有效后作为 --input 传入。
--input 可重复传入多张参考图（如 --input a.png --input b.png）。
运行 scripts/sofunny-image.js。
脚本会按模型前缀自动分流：
gemini-*：调用 {BASE_URL}/v1beta/models/{MODEL}:generateContent
gpt-image-* 且无 --input：调用 {BASE_URL}/v1/images/generations（纯文生图）
gpt-image-* 且有 --input：调用 {BASE_URL}/v1/images/edits（图生图/改图）
Gemini 响应提取最后一个 inlineData.data；OpenAI Images 响应提取最后一个 data[].b64_json，并视为最终图片保存到本地。
把保存路径返回给用户。
错误处理
禁止自动切换模型：如果脚本调用失败，不要自动更换模型重试。用户配置（env 或 --model）指定的模型就是要用的模型。
失败时应按以下顺序提示用户：
展示完整错误信息
建议用户检查配置（API Key、模型名称、渠道是否可用）
询问用户是否要重试（相同模型、相同参数）
询问用户是否要切换到其他模型（给出推荐，如 gpt-image-2、gemini-3.1-flash-image-preview、gemini-3-pro-image-preview），由用户决定
不要在用户未确认的情况下更换模型、更换参数或跳过错误。
注意事项
本 skill 默认不附带 tools 和 thinking，避免图片模型在工具模式下失败。
BASE_URL 应为服务根地址；脚本会自动拼出 /v1beta/... 或 /v1/images/...，不要手动把环境变量写成特定接口路径。
若未指定输出路径，脚本默认保存到：
当前工作目录
~/.sofunny-image.env 中只应使用 SOFUNNY_* 变量，避免旧配置混入导致行为不一致。
如果 Gemini 或 OpenAI Images 在同一次响应中返回多张图片，脚本默认只保存最后一张，前面的图片视为中间产物。
当前 gpt-image-* 先不支持 mask；若用户传入 --input，默认按普通图生图/编辑处理。
gpt-image-* 若未显式传入 --size、--quality、--background、--output-format、--output-compression，脚本不会自动补发这些字段，避免把“脚本默认值”误当成“用户显式指定”传给上游。
若需要稳定复现某个上游参数组合，再显式传入对应参数，例如 --quality auto、--output-format png。
Weekly Installs
21
Repository
yhx0516/ai-toolkits
First Seen
Mar 20, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykPass