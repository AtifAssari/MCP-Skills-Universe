---
rating: ⭐⭐
title: maishou
url: https://skills.sh/aahl/skills/maishou
---

# maishou

skills/aahl/skills/maishou
maishou
Installation
$ npx skills add https://github.com/aahl/skills --skill maishou
Summary

Compare product prices and coupons across major Chinese e-commerce platforms.

Supports eight platforms: Taobao, Tmall, JD.com, PinDuoDuo, Suning, VIP.com, Kaola, Douyin, Kuaishou, and 1688
Search products by keyword with pagination support across all platforms or filter by specific source
Retrieve detailed product information and direct purchase links for any item
SKILL.md
买手技能

全网比价，获取中国在线购物平台商品价格、优惠券

# 参数解释
source:
  0: 全部
  1: 淘宝/天猫
  2: 京东
  3: 拼多多
  4: 苏宁
  5: 唯品会
  6: 考拉
  7: 抖音
  8: 快手
  10: 1688

搜索商品
uv run scripts/main.py search --source=0 --keyword='{keyword}'
uv run scripts/main.py search --source=0 --keyword='{keyword}' --page=2

商品详情及购买链接
uv run scripts/main.py detail --source={source} --id={goodsId}

Weekly Installs
1.8K
Repository
aahl/skills
GitHub Stars
120
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn