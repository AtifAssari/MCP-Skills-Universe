---
title: jenkins-deploy
url: https://skills.sh/abcfed/claude-marketplace/jenkins-deploy
---

# jenkins-deploy

skills/abcfed/claude-marketplace/jenkins-deploy
jenkins-deploy
Installation
$ npx skills add https://github.com/abcfed/claude-marketplace --skill jenkins-deploy
SKILL.md
ABC Jenkins 发布技能

交互式触发 Jenkins 构建，支持智能参数推断（自动解析分支名、环境推断）和实时状态监控。

前置条件
JENKINS_USER 环境变量已设置（Jenkins 用户名）
JENKINS_TOKEN 环境变量已设置（Jenkins API Token）
当前在 Git 仓库中（用于自动获取分支和标签）
安装
npx add-skill https://github.com/ABCFed/claude-marketplace/tree/main/skills/jenkins-deploy

准备
# 编辑 ~/.zshrc 或 ~/.bashrc
export JENKINS_USER="your_jenkins_username"
export JENKINS_TOKEN="your_jenkins_api_token"
source ~/.zshrc

使用流程
方式一：两阶段部署（推荐，进度可见）

步骤 1：触发构建（返回 JSON）

python scripts/jenkins_deploy.py \
  <project_name> \
  --trigger-only-no-monitor \
  --yes \
  --params "<json>"


返回 JSON：

{
  "queue_id": 161484,
  "full_name": "abc-his/test/PcFeatureTest",
  "project_name": "PcFeatureTest",
  "build_url": "http://ci.abczs.cn/job/abc-his/job/test/job/PcFeatureTest/"
}


步骤 2：启动后台监控

Claude Code（使用 run_in_background=true）：

# 在 Claude Code 中使用 Bash 工具，设置 run_in_background=true
python scripts/jenkins_deploy.py \
  --monitor-only \
  --full-name abc-his/test/PcFeatureTest \
  --queue-id 161484 \
  --display-name PcFeatureTest


其他 AI 工具或终端（使用 nohup）：

nohup python scripts/jenkins_deploy.py \
  --monitor-only \
  --full-name abc-his/test/PcFeatureTest \
  --queue-id 161484 \
  --display-name PcFeatureTest > /dev/null 2>&1 &


重要说明：

监控任务作为后台任务运行，不阻塞主对话/终端
Claude Code：进度显示在后台任务输出中
其他工具：使用 nohup 实现后台运行，构建完成后会收到系统通知
用户可以继续进行其他操作

监控输出示例：

📊 开始监控构建: PcFeatureTest
   Queue ID: 161484
   项目: abc-his/test/PcFeatureTest

任务开始执行 (Build #11122)
📦 构建号: #11122
⏳ 监控构建进度...
   需要取消时，请告诉我: "取消构建 #11122"

⏳ [███████████░░░░░░░░░░░░░░░] 42% (125s)
...
✅ PcFeatureTest 构建成功!

参数说明
--trigger-only-no-monitor 模式（触发构建）
参数	必填	说明
project_name	✓	Jenkins 项目名称（如 PcFeatureTest）
--trigger-only-no-monitor	✓	仅触发构建，不启动监控，返回 JSON
--yes	✓	跳过交互式确认
--params	✓	JSON 格式的完整构建参数
--monitor-only 模式
参数	必填	说明
--monitor-only	✓	后台监控模式
--full-name	✓	项目完整路径（如 abc-his/test/PcFeatureTest）
--queue-id	✓	队列 ID
--display-name	✓	项目显示名称（用于通知）
完整示例
测试环境发布
# 步骤 1: 触发构建
python scripts/jenkins_deploy.py \
  PcFeatureTest \
  --trigger-only-no-monitor \
  --yes \
  --params '{"repoTag":"pc-t2025.53.19","tapdId":"1167459320001118371","featureNo":"70"}'

# 返回 JSON:
# {"queue_id": 161484, "full_name": "abc-his/test/PcFeatureTest", ...}

# 步骤 2: 启动后台监控
# Claude Code: 直接运行（会使用 run_in_background=true）
# 其他工具: 添加 nohup 和 & 放到后台
python scripts/jenkins_deploy.py \
  --monitor-only \
  --full-name abc-his/test/PcFeatureTest \
  --queue-id 161484 \
  --display-name PcFeatureTest

开发环境发布
python scripts/jenkins_deploy.py \
  staticPcOwn \
  --trigger-only-no-monitor \
  --yes \
  --params '{"repoBranch":"hotfix/xxx-1167459320001118371"}'

其他命令
# 列出所有项目
python scripts/jenkins_deploy.py --list --all

# 列出当前仓库相关的项目（自动过滤）
python scripts/jenkins_deploy.py --list

# 停止指定构建号
python scripts/jenkins_deploy.py --stop <build_number>

测试与验证

每次修改技能后，建议按以下流程验证：

快速测试命令
# 自动化运行所有测试用例
python scripts/run_tests.py

手动测试

1. 参数验证（必做）

python scripts/jenkins_deploy.py \
  PcFeatureTest \
  --validate \
  --params '{"repoTag":"pc-t2025.53.19","featureNo":"70"}'


2. 模拟运行（必做）

python scripts/jenkins_deploy.py \
  PcFeatureTest \
  --dry-run \
  --params '{"repoTag":"pc-t2025.53.19","featureNo":"70"}'


详细测试用例：参见 test-cases.md

工作流程（推荐模式）
┌─────────────────────────────────────────────────────────────┐
│ 1. Claude Code: 使用 AskUserQuestion 收集参数               │
│    其他 AI 工具: 通过对话收集参数                            │
│    - 项目名称                                               │
│    - Git 分支 / 标签                                         │
│    - TAPD ID（从分支名自动解析）                             │
│    - featureNo（如果项目有此参数，**必填**）                 │
│    - 其他构建参数                                            │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. 调用脚本 --trigger-only 模式                            │
│    - 传递完整的 JSON 参数                                    │
│    - 直接触发 Jenkins API                                   │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. 返回构建信息                                            │
│    - Queue ID                                               │
│    - 构建页面 URL                                           │
└─────────────────────────────────────────────────────────────┘

智能参数推断
参数	推断规则	示例
repoBranch	当前 Git 分支	hotfix/盘点页面增加备注及搜索-1167459320001118371
repoTag	最新 Git 标签	pc-f2026.05.48
tapdId / tapdid	从分支名自动解析（标准化流程：分支名末尾的数字）	1167459320001118371
execType	有 tag=deploy，无 tag=build	有 tag → deploy
featureNo	必填（当项目有此参数时），需用户明确指定	1122044681001112866
envNo	部分项目需要，需用户明确指定	001
TAPD ID 自动解析

标准化流程下，分支名格式为 feature/xxx-{TAPD_ID} 或 hotfix/xxx-{TAPD_ID}：

分支名：hotfix/盘点页面增加备注及搜索-1167459320001118371
                                         └────────────────────┘
                                          自动提取 TAPD ID


无需手动配置，发布时会自动填充到 tapdId 或 tapdid 参数。

⚠️ 重要：

featureNo（功能编号）：当项目有此参数时必填，需由用户提供
envNo（环境编号）：部分项目需要，需由用户提供
支持的参数类型
参数类型	说明	交互方式
StringParameterDefinition	文本输入	直接输入或回车使用默认值
ChoiceParameterDefinition	下拉选择	显示选项列表，输入编号选择
PT_CHECKBOX	复选框多选	显示选项列表，输入逗号分隔的编号
BooleanParameterDefinition	布尔值	y/n 选择
WReadonlyStringParameterDefinition	只读参数	自动使用，不可修改
常见项目类型

详细项目参数参考：参见 projects.md

1. PcFeatureTest (测试环境发布)

用途：使用标签发布到测试环境

关键参数：

repoTag：发布标签（如 pc-t2025.53.19）
tapdId：TAPD 需求 ID（自动从分支名解析）
featureNo：功能编号（必填），需用户提供
buildEnv：固定为 test

示例：

python scripts/jenkins_deploy.py \
  PcFeatureTest \
  --trigger-only \
  --params '{"repoTag":"pc-f2026.05.48","tapdId":"1167459320001118371","featureNo":"1122044681001112866"}'

2. staticPcOwn (开发环境发布)

用途：使用分支发布到开发环境

关键参数：

repoBranch：发布分支（如 hotfix/xxx-1167459320001118371）
dockerTag：Docker 镜像标签（默认 latest）
buildEnv：固定为 dev

示例：

python scripts/jenkins_deploy.py staticPcOwn

3. static-mf-deepseek (微服务发布)

用途：微服务项目发布，支持多区域部署

关键参数：

projectRootDir：项目子目录（如 packages/mf-deepseek）
deployZone：部署区域（复选框：primary / standby）
repoBranch：发布分支

示例：

python scripts/jenkins_deploy.py static-mf-deepseek

缓存机制

缓存位置： scripts/cache/jobs.json

缓存策略：

首次运行：从 Jenkins API 获取 542 个项目并缓存
后续运行：直接使用缓存（速度快）
强制刷新：使用 --refresh 参数

手动清除缓存：

rm scripts/cache/jobs.json

支持的 Jenkins 环境
环境	Dev	Test
abc-his	✓	✓
abc-bis	✓	✓
abc-cooperation	✓	✓
abc-global	✓	✓
abc-oa	✓	✓
mira	✓	✓
错误处理
场景	处理方式
未配置认证	提示设置 JENKINS_USER 和 JENKINS_TOKEN
项目不存在	列出可用项目
缺少 featureNo	如果项目有此参数，必须提示用户提供
构建失败	显示构建 URL 和日志链接
参数验证失败	提示正确格式
网络超时	提示检查网络连接
触发关键词

Jenkins、发布、部署、构建、Deploy、Build、CI/CD

Weekly Installs
31
Repository
abcfed/claude-m…ketplace
GitHub Stars
19
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass