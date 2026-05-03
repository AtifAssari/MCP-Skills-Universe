---
title: eac-user-search
url: https://skills.sh/site/skills-eac.bj.bcebos.com/eac-user-search
---

# eac-user-search

skills/skills-eac.bj.bcebos.com/eac-user-search
eac-user-search
$ npx skills add https://skills-eac.bj.bcebos.com
SKILL.md
EAC User Search

企业用户检索技能。通过调用 userSuggest 接口，根据关键词快速定位目标用户的如流个人主页信息。

触发条件

当用户消息符合以下模式时触发此技能：

基础检索模式
包含"检索"、"搜索"、"查找"、"查询"等动词 + 用户名或关键词（如"检索张三"、"帮我查找李四"）
在明确的用户查找上下文中直接提供关键词（如"张三"、"wangwu"）
日常询问模式（智能识别）
部门查询：XXX是哪个部门的、XXX在什么部门、XXX属于哪个部门（如"张三是哪个部门的"）
邮箱查询：XXX的邮箱是什么、XXX的邮箱、XXX邮箱多少、怎么联系XXX（如"李四的邮箱是什么"）
身份查询：XXX是谁、谁是XXX、XXX是干嘛的（如"王五是谁"）
综合查询：XXX的信息、查一下XXX、帮我看看XXX（如"查一下张三的信息"）
其他场景
其他 skill 需要获取用户信息时作为依赖调用
使用方式
方式一：自然语言查询

用户可直接使用日常语言提问，技能会自动识别查询意图：

部门查询示例：

"张三是哪个部门的"
"李四在什么部门"

邮箱查询示例：

"王五的邮箱是什么"
"怎么联系赵六"

身份查询示例：

"钱七是谁"
"谁是孙八"
方式二：执行脚本

运行 scripts/search_user.py 进行检索：

python3 <skill-dir>/scripts/search_user.py <query>


参数说明：

参数	必填	说明
query	是	检索关键词（如"张三"、"lisi"）

示例：

python3 <skill-dir>/scripts/search_user.py "张三"

方式三：被其他 skill 依赖调用

其他 skill 的 Python 脚本可直接调用：

python3 <skill-dir>/scripts/search_user.py <query>

输出格式
成功

返回匹配用户列表的 JSON 数组（可能包含多个结果）：

[
  {
    "uid": "123456",
    "username": "zhangsan",
    "name": "张三",
    "email": "zhangsan@baidu.com",
    "department": "技术部"
  }
]

失败

返回包含错误码和消息的 JSON：

{
  "code": -1,
  "msg": "错误信息",
  "result": []
}

结果展示

根据用户查询意图，智能组织回答内容：

意图识别与回答策略

部门查询（"XXX是哪个部门的"）

优先回答：姓名 + 部门
示例："张三，技术部"

邮箱查询（"XXX的邮箱是什么"）

优先回答：姓名 + 邮箱
示例："李四的邮箱是 lisi@baidu.com"

身份查询（"XXX是谁"）

完整回答：姓名 + 部门 + 邮箱
示例："张三，技术部，zhangsan@baidu.com"

通用查询（"检索XXX"、"查XXX信息"）

展示完整信息卡片：
姓名：张三
部门：技术部
邮箱：zhangsan@baidu.com
用户名：zhangsan

当返回多个匹配结果时，展示所有匹配用户的信息。

依赖
aigate-cli — 通过 aigate-cli 命令调用 userSuggest 接口，自动处理认证。
注意事项
每次请求独立执行，不缓存搜索结果。
接口超时设置为 10 秒，等待完整超时周期后才判定失败。
禁止记住之前的系统异常、网络错误、403、认证失败等历史状态影响当前请求。
使用 aigate-cli 命令调用接口，自动处理认证，无需手动获取 token。
Weekly Installs
9
Source
skills-eac.bj.bcebos.com
First Seen
4 days ago