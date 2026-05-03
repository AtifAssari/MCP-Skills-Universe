---
title: goose-adventure-game
url: https://skills.sh/insight68/skills/goose-adventure-game
---

# goose-adventure-game

skills/insight68/skills/goose-adventure-game
goose-adventure-game
Installation
$ npx skills add https://github.com/insight68/skills --skill goose-adventure-game
SKILL.md
鹅骑鹅冒险游戏引擎
概述

这是一个完整的文字冒险游戏引擎，专为《尼尔斯骑鹅旅行记》故事设计。游戏引擎支持：

剧情节点系统 - 分支叙事，多个结局
状态管理 - 生命值、道德值、大小值、知识值
存档系统 - 多槽位存档，自动保存
成就系统 - 追踪玩家成就
物品栏管理 - 收集和使用物品
条件触发 - 基于状态的选项解锁
快速开始
1. 运行游戏
# 使用 Python 运行游戏引擎
python3 scripts/game_engine.py

# 或使用 pnpm（如果需要）
pnpm run game

2. 游戏文件结构
goose-adventure-game/
├── scripts/
│   ├── game_engine.py      # 游戏引擎主类
│   ├── game_script.json    # 游戏剧本数据
│   └── save_manager.py     # 存档管理器
├── saves/                  # 存档目录（自动创建）
└── SKILL.md               # 本文档

3. 基本使用
from scripts.game_engine import GameEngine, load_script_from_file

# 加载游戏脚本
script = load_script_from_file("scripts/game_script.json")

# 创建游戏引擎
engine = GameEngine(script, save_dir="./saves")

# 渲染当前场景
scene = engine.render_scene()
print(f"{scene['title']}\n{scene['description']}")

# 显示选项
for choice in scene['choices']:
    print(f"{choice['index']}: {choice['text']}")

# 玩家做出选择
engine.make_choice(0)  # 选择第一个选项

# 保存游戏
engine.save_game("slot1")

核心功能
1. 游戏状态系统

游戏状态包含以下属性：

属性	类型	范围	说明
hp	int	0-100	生命值
morality	int	0-100	道德值（决定结局）
size	int	0-100	大小值（0=拇指大小，100=正常）
knowledge	int	0-1000	知识值
inventory	list	-	物品栏
achievements	list	-	成就列表
flags	dict	-	事件标志
2. 场景系统

每个场景包含：

{
  "id": "scene_id",
  "title": "场景标题",
  "description": "场景描述",
  "choices": [
    {
      "text": "选项文本",
      "next_scene": "下一场景ID",
      "requirements": {
        "morality_min": 50,
        "has_item": "key"
      },
      "effects": {
        "moral_change": 10,
        "add_item": "key",
        "set_flag": {"met_npc": true}
      }
    }
  ]
}

3. 条件触发系统

支持的触发条件：

has_item - 检查物品
flag - 检查事件标志
morality_min/max - 道德值范围
size_min/max - 大小值范围
has_achievement - 检查成就
4. 效果系统

支持的效果类型：

add_item / remove_item - 物品管理
hp_change - 生命值变化
size_change - 大小值变化
set_flag - 设置事件标志
add_achievement - 添加成就
moral_change - 道德值变化
knowledge_gain - 获得知识
存档系统
使用存档管理器
from scripts.save_manager import SaveManager

manager = SaveManager(save_dir="./saves")

# 保存游戏
manager.save_game("slot1", game_data)

# 加载游戏
game_data = manager.load_game("slot1")

# 列出所有存档
saves = manager.list_saves()

# 删除存档
manager.delete_save("slot1")

自动保存
from scripts.save_manager import AutoSaveManager

auto_save = AutoSaveManager(manager, auto_save_interval=5)

# 每个场景变化后检查
auto_save.on_scene_change("autosave", game_data)

# 强制保存
auto_save.force_save("quicksave", game_data)

游戏剧本编辑
添加新场景

在 game_script.json 的 scenes 数组中添加：

{
  "id": "my_new_scene",
  "chapter": 1,
  "title": "新场景标题",
  "description": "场景描述...",
  "choices": [
    {
      "text": "选项1",
      "next_scene": "scene_a"
    },
    {
      "text": "选项2",
      "next_scene": "scene_b",
      "requirements": {"morality_min": 50},
      "effects": {"moral_change": 10}
    }
  ]
}

添加新结局

在 game_script.json 的 endings 数组中添加：

{
  "id": "special_ending",
  "title": "特殊结局",
  "description": "结局描述...",
  "requirements": {
    "morality_min": 80,
    "flag": ["special_event", true]
  }
}

成就系统
预定义成就

游戏包含以下成就：

🥚 初章：变小的人 - 完成第一章
🕊️ 翅膀的守护者 - 救下莫顿
🦊 狐狸的死敌 - 帮助雁群对抗狐狸
🌍 自然观察者 - 知识值达到100
📚 小小博物学家 - 知识值达到300
🗺️ 地理大师 - 知识值达到500
⭐ 智慧之星 - 知识值达到800
💖 善良之心 - 道德值达到80
🦸‍♂️ 真正的勇者 - 达成完美结局
添加自定义成就

在场景的效果中添加：

{
  "effects": {
    "add_achievement": "🏆 自定义成就"
  }
}

游戏调试
查看当前状态
state = engine.state
print(f"生命值: {state.hp}")
print(f"道德值: {state.morality}")
print(f"知识值: {state.knowledge}")
print(f"物品: {state.inventory}")
print(f"成就: {state.achievements}")

跳转到指定场景
engine.state.current_scene = "target_scene_id"

设置状态值
engine.state.morality = 80
engine.state.knowledge = 500
engine.state.inventory.append("special_item")

扩展游戏
创建自定义故事
复制 game_script.json 作为模板
修改 game_info 中的标题和描述
编辑或替换 scenes 数组中的场景
更新 endings 数组中的结局
添加新功能

游戏引擎采用模块化设计，可以轻松扩展：

在 GameEngine 类中添加新方法
在 GameState 类中添加新属性
创建新的效果类型
最佳实践
游戏设计
道德选择 - 提供有意义的选择，让玩家思考
循序渐进 - 从简单开始，逐步增加复杂性
反馈清晰 - 让玩家了解选择的后果
多结局 - 根据玩家选择提供不同结局
剧情编写
描述生动 - 使用感官语言描述场景
选项明确 - 每个选项应该清晰表达后果
逻辑一致 - 确保剧情逻辑连贯
知识融入 - 在剧情中自然地融入知识
技术实现
数据驱动 - 将故事数据与引擎代码分离
可测试性 - 确保每个功能都可以独立测试
错误处理 - 优雅处理加载失败等情况
性能优化 - 避免重复加载资源
Weekly Installs
15
Repository
insight68/skills
GitHub Stars
4
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass