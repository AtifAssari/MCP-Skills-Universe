---
title: using-llm
url: https://skills.sh/dtyq/magic/using-llm
---

# using-llm

skills/dtyq/magic/using-llm
using-llm
Installation
$ npx skills add https://github.com/dtyq/magic --skill using-llm
SKILL.md
LLM Calling Skill

List available models and send chat requests to any of them — no extra configuration required.

Core Capabilities
List currently available models
Send chat completion requests in OpenAI format (non-streaming)
Usage Guide

When you need to call an LLM in code, use the SDK functions from sdk.llm. There are two ways to execute the code:

Option 1: Use the run_python_snippet tool to execute a code snippet directly
Option 2: Write the code to a .py file, then execute it with shell_exec

create_openai_sync_client is a Python SDK function, not a tool name — import and use it inside your code:

# Option 1: run_python_snippet
run_python_snippet(
    python_code="""
from sdk.llm import create_openai_sync_client
client = create_openai_sync_client()
...
""",
    script_path="temp_llm_xxx.py",
    timeout=300,
)

# Option 2: write a .py file, then run with shell_exec
# First write the script with write_file, then execute:
shell_exec("python scripts/my_llm_script.py")


LLM calls can take a while — consider increasing the timeout based on complexity, e.g. timeout=120 for a single call, timeout=300 or more for multi-model comparisons or batch inference (applies to both options).

Quick Start
Step 1: List available models

When unsure of the model ID, query available models first:

run_python_snippet(
    python_code="""
import json
from sdk.llm import create_openai_sync_client

client = create_openai_sync_client()
models = client.models.list()
print(json.dumps([{"id": m.id} for m in models.data], ensure_ascii=False, indent=2))
""",
    script_path="temp_list_models.py",
)


Example output:

[
  {"id": "claude-3-5-sonnet-20241022"},
  {"id": "gpt-4o"},
  {"id": "deepseek-v3"}
]

Step 2: Send a chat request

Use a real model ID to send a chat:

run_python_snippet(
    python_code="""
from sdk.llm import create_openai_sync_client

client = create_openai_sync_client()

response = client.chat.completions.create(
    model="<模型ID>",
    messages=[
        {"role": "system", "content": "你是一个助手"},
        {"role": "user", "content": "你好"},
    ],
    extra_body={"thinking": {"type": "disabled"}},
)

print(response.choices[0].message.content)
""",
    script_path="temp_chat.py",
    timeout=120,
)

Vision — Attach Images in Messages

When using a vision-capable model, images can be included in messages. The SDK provides two ways to convert a workspace file to a URL:

Function	Use Case
file_to_url(path)	Use this first — returns a directly accessible URL
image_to_base64(path)	Fallback if file_to_url fails — encodes the image as base64

Both accept http/https URLs as input and return them unchanged.

IMPORTANT — image_to_base64 return value: The function already returns a complete data URL string like data:image/jpeg;base64,/9j/4AAQ.... Use the return value directly as url. Do NOT prepend data:image/jpeg;base64, again — doing so will cause an Invalid base64 image_url error.

run_python_snippet(
    python_code="""
from sdk.llm import create_openai_sync_client, file_to_url, image_to_base64

client = create_openai_sync_client()

# 优先使用 file_to_url / use file_to_url first
# 路径相对于 .workspace/ 目录 / path is relative to .workspace/
image_url = file_to_url("test/screenshot.png")

# file_to_url 失败时用 image_to_base64 / fallback to image_to_base64
# image_url = image_to_base64("test/screenshot.png")
# image_to_base64 已返回完整 data URL，直接使用，禁止再拼接前缀
# image_to_base64 returns a complete data URL — use it directly, never prepend "data:...;base64," again

response = client.chat.completions.create(
    model="<视觉模型ID>",
    messages=[{
        "role": "user",
        "content": [
            {"type": "image_url", "image_url": {"url": image_url}},
            {"type": "text", "text": "描述这张图片的内容"},
        ],
    }],
    extra_body={"thinking": {"type": "disabled"}},
)

print(response.choices[0].message.content)
""",
    script_path="temp_vision.py",
    timeout=120,
)

Parameter Reference
Common Parameters for client.chat.completions.create()
Parameter	Type	Required	Description
model	str	Yes	Model ID — use a real ID from Step 1
messages	list	Yes	List of messages, each with role and content
temperature	float	No	Sampling temperature, 0~2, default 1
max_tokens	int	No	Maximum output tokens
tools	list	No	Tool definitions (Function Calling)
extra_body	dict	No	Extra fields not natively supported by the OpenAI SDK, e.g. thinking
thinking Parameter — Control Deep Thinking

Pass thinking via extra_body to control whether the model outputs chain-of-thought content. Recommended default: disabled to avoid unnecessary token usage and latency.

thinking.type value	Description
disabled	Force disable deep thinking — model will not output chain-of-thought (recommended default)
enabled	Force enable deep thinking — model always outputs chain-of-thought
auto	Model decides on its own whether to use deep thinking

Note: The thinking parameter only applies to models that support deep thinking (e.g. doubao-seed series). Passing it to unsupported models may cause errors — check whether the target model supports this parameter before using it.

# 关闭思考（推荐默认）/ disable thinking (recommended default)
extra_body={"thinking": {"type": "disabled"}}

# 开启思考 / enable thinking
extra_body={"thinking": {"type": "enabled"}}

# 模型自行判断 / let model decide
extra_body={"thinking": {"type": "auto"}}

Return Value

client.chat.completions.create() returns a ChatCompletion object:

response.choices[0].message.content      # 文本回复 / text reply
response.choices[0].message.tool_calls   # 工具调用列表 / tool calls (Function Calling)
response.choices[0].finish_reason        # stop / tool_calls / length
response.usage.total_tokens              # 总 token 数 / total tokens used

# 仅当 thinking.type 为 enabled 或 auto（模型决定开启）时存在
# Only present when thinking.type is "enabled" or "auto" (and model decides to think)
response.choices[0].message.reasoning_content   # 思维链内容 / chain-of-thought content
response.usage.completion_tokens_details        # 含 reasoning_tokens 字段 / contains reasoning_tokens


Note: reasoning_content is a non-standard field and is not automatically parsed by the OpenAI SDK as an attribute. Access it as follows:

# 方式一：通过 model_extra 读取 / Option 1: via model_extra
reasoning = response.choices[0].message.model_extra.get("reasoning_content")

# 方式二：转为 dict 读取 / Option 2: convert to dict
import json
msg_dict = json.loads(response.choices[0].message.model_dump_json())
reasoning = msg_dict.get("reasoning_content")

Weekly Installs
12
Repository
dtyq/magic
GitHub Stars
4.8K
First Seen
Mar 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn