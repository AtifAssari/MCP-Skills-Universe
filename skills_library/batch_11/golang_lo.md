---
title: golang-lo
url: https://skills.sh/dcjanus/prompts/golang-lo
---

# golang-lo

skills/dcjanus/prompts/golang-lo
golang-lo
Installation
$ npx skills add https://github.com/dcjanus/prompts --skill golang-lo
SKILL.md
lo Go 工具库速用指南
快速上手
安装：go get github.com/samber/lo@v1。
常用导入：
import (
    "github.com/samber/lo"
    lop "github.com/samber/lo/parallel"
    lom "github.com/samber/lo/mutable"
    loi "github.com/samber/lo/it"
)

常用函数速览：
// Filter: 按条件保留
lo.Filter(nums, func(x int, _ int) bool { return x%2==0 })
// Map: 映射生成新切片
lo.Map(nums, func(x int, _ int) int { return x*x })
// Find: 找到首个满足条件的元素
v, ok := lo.Find(nums, func(x int) bool { return x > 10 })
// Uniq: 去重并保持顺序
uniq := lo.Uniq([]string{"a","a","b"})
// GroupBy: 按键分组
groups := lo.GroupBy(users, func(u User) int { return u.Age })
// Must: 遇 err/false panic，常用于初始化
t := lo.Must(time.Parse(time.RFC3339, ts))

官方清单获取

使用 curl 直接读取最新函数列表：

curl -sSL https://lo.samber.dev/llms.txt


该清单随 Git 仓库最新提交更新，可能包含尚未发布的变更；使用前请核对本地依赖版本。

Weekly Installs
23
Repository
dcjanus/prompts
GitHub Stars
19
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass