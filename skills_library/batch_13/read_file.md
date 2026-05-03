---
title: read_file
url: https://skills.sh/dotnetage/mindx/read_file
---

# read_file

skills/dotnetage/mindx/read_file
read_file
Installation
$ npx skills add https://github.com/dotnetage/mindx --skill read_file
SKILL.md
文件读取技能

从指定的文件中读取内容并返回。

功能说明
支持读取文本文件内容
使用系统 cat 命令实现
支持绝对路径和相对路径
示例

读取文件:

{
  "name": "read_file",
  "parameters": {
    "path": "/Users/ray/test.txt"
  }
}

输出格式
{
  "success": true,
  "path": "/Users/ray/test.txt",
  "content": "Hello, World!",
  "bytes_read": 13
}

注意事项
确保有足够的文件系统权限
大文件读取可能需要较长时间
仅支持文本文件，二进制文件可能无法正确显示
Weekly Installs
10
Repository
dotnetage/mindx
GitHub Stars
28
First Seen
Mar 1, 2026