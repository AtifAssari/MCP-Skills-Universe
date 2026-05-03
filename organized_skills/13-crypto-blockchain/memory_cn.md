---
rating: ⭐⭐
title: memory-cn
url: https://skills.sh/abczsl520/openclaw-memory-cn/memory-cn
---

# memory-cn

skills/abczsl520/openclaw-memory-cn/memory-cn
memory-cn
Installation
$ npx skills add https://github.com/abczsl520/openclaw-memory-cn --skill memory-cn
SKILL.md
中文记忆优化 Skill (memory-cn)

当用户请求诊断或优化记忆系统时，按以下步骤执行：

1. 诊断

运行诊断脚本检测问题：

bash SKILL_DIR/scripts/diagnose.sh


报告包括：

FTS5 中文分词 bug 检测（unicode61 把连续中文粘成一个 token）
记忆文件大小分布
tags 标签覆盖率
lessons 知识库健康度
2. 优化搜索配置

如果诊断发现问题，应用优化配置：

{
  "agents": {
    "defaults": {
      "memorySearch": {
        "chunking": { "tokens": 250, "overlap": 60 },
        "query": {
          "maxResults": 10,
          "minScore": 0.15,
          "hybrid": {
            "enabled": true,
            "vectorWeight": 0.75,
            "textWeight": 0.25,
            "candidateMultiplier": 8,
            "mmr": { "enabled": true, "lambda": 0.7 },
            "temporalDecay": { "enabled": true, "halfLifeDays": 90 }
          }
        }
      }
    }
  }
}


使用 gateway config.patch 应用。

3. 优化 memoryFlush prompt

让新日志自动加 tags + 中文分词：

{
  "agents": {
    "defaults": {
      "compaction": {
        "memoryFlush": {
          "prompt": "将对话内容整理为结构化日志，写入 memory/YYYY-MM-DD.md。\n\n格式要求：\n1. 文件第一行必须是 <!-- tags: 关键词1, 关键词2, ... --> 标签行\n2. 中文关键词之间加空格分隔\n3. 只保留有价值的信息\n4. 控制在 5KB 以内"
        }
      }
    }
  }
}

4. 批量加 tags

对 memory/projects/*.md 中缺少 tags 的文件，根据内容自动添加 <!-- tags: ... --> 行。

python3 SKILL_DIR/scripts/add-tags.py /path/to/memory/projects/

5. 压缩日志

压缩 >8KB 的旧日志到 <5KB，原文备份到 archive/：

python3 SKILL_DIR/scripts/compress-logs.py /path/to/memory/ --max-kb 5

6. 重建索引
openclaw memory index --force

7. 设置自动维护 cron

建议每周日凌晨自动执行压缩+清理+补标签+重建索引。

关键技术点
FTS5 unicode61 Bug
unicode61 分词器把连续 CJK 字符当作一个 token
搜索 "怀孕" 无法匹配 "老婆刚怀孕"（因为后者是一个 token）
Workaround：中文关键词之间加空格 → FTS5 正确分词
0.6B 模型参数调优
vectorWeight 0.75：向量主导（FTS5 中文不可靠）
minScore 0.15：小模型分数普遍偏低
chunking 250 tokens：更小的 chunk 帮助弱模型匹配
三层架构
P0 (MEMORY.md)：核心事实，<2KB
P1 (projects/ + lessons/)：按需搜索，带 tags
P2 (日志 + archive)：历史记录
Weekly Installs
34
Repository
abczsl520/openc…emory-cn
GitHub Stars
8
First Seen
Mar 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass