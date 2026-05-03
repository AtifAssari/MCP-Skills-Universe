---
title: write_file
url: https://skills.sh/dotnetage/mindx/write_file
---

# write_file

skills/dotnetage/mindx/write_file
write_file
Installation
$ npx skills add https://github.com/dotnetage/mindx --skill write_file
SKILL.md
写入文件技能

将内容写入到文件中，所有文件只能写入当前工作区的 documents 子目录。

功能特点
自动创建不存在的目录
支持自定义文件路径
返回写入文件的绝对路径
记录写入耗时
使用方法
写入到 documents 根目录
{
  "name": "write_file",
  "parameters": {
    "filename": "note.txt",
    "content": "这是要写入的内容"
  }
}

写入到 documents 下的子目录
{
  "name": "write_file",
  "parameters": {
    "filename": "data.json",
    "content": "{\"key\": \"value\"}",
    "path": "notes"
  }
}

写入到 documents 下的多级子目录
{
  "name": "write_file",
  "parameters": {
    "filename": "report.txt",
    "content": "报告内容",
    "path": "reports/2024"
  }
}

输出格式
{
  "file_path": "/Users/ray/projects/mindx/documents/note.txt",
  "content_length": 20,
  "elapsed_ms": 5
}

使用场景
需要保存笔记或文档时
需要导出数据到文件时
需要创建配置文件时
需要记录日志或结果时
Weekly Installs
10
Repository
dotnetage/mindx
GitHub Stars
28
First Seen
Mar 1, 2026