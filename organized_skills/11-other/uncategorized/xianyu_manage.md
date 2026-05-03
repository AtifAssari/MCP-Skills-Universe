---
rating: ⭐⭐⭐
title: xianyu_manage
url: https://skills.sh/g3niusyukki/xianyu-openclaw/xianyu_manage
---

# xianyu_manage

skills/g3niusyukki/xianyu-openclaw/xianyu_manage
xianyu_manage
Installation
$ npx skills add https://github.com/g3niusyukki/xianyu-openclaw --skill xianyu_manage
SKILL.md
闲鱼商品管理

当用户想要管理已上架的闲鱼商品时，使用此技能。包括擦亮、调整价格、下架、重新上架等操作。

使用方法

使用 bash 工具执行以下命令：

擦亮商品

擦亮可以让商品排名更靠前，每个商品每天可免费擦亮一次。

# 擦亮所有商品（默认最多 50 个）
cd /home/node/.openclaw/workspace && python -m src.cli polish --all

# 擦亮所有商品，指定最大数量
cd /home/node/.openclaw/workspace && python -m src.cli polish --all --max 100

# 擦亮指定商品
cd /home/node/.openclaw/workspace && python -m src.cli polish --id <product_id>

调整价格
cd /home/node/.openclaw/workspace && python -m src.cli price --id <product_id> --price <新价格>

下架商品
cd /home/node/.openclaw/workspace && python -m src.cli delist --id <product_id> --reason "下架原因"

重新上架
cd /home/node/.openclaw/workspace && python -m src.cli relist --id <product_id>

示例

用户说："帮我擦亮所有商品" →

cd /home/node/.openclaw/workspace && python -m src.cli polish --all


用户说："把那个 iPhone 降到 4000" →

cd /home/node/.openclaw/workspace && python -m src.cli price --id <product_id> --price 4000


用户说："把卖完的那个下架吧" →

cd /home/node/.openclaw/workspace && python -m src.cli delist --id <product_id> --reason "已售出"

注意事项
所有命令输出 JSON 格式，包含 success 字段表示是否成功
批量擦亮会在每个商品之间随机等待 1-3 秒，避免触发平台限制
如果用户没有提供 product_id，询问用户具体是哪个商品
Weekly Installs
24
Repository
g3niusyukki/xia…openclaw
GitHub Stars
5
First Seen
Feb 27, 2026