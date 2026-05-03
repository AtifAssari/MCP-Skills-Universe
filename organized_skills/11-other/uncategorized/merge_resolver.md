---
rating: ⭐⭐⭐⭐⭐
title: merge-resolver
url: https://skills.sh/blueif16/amazing-claude-code-plugins/merge-resolver
---

# merge-resolver

skills/blueif16/amazing-claude-code-plugins/merge-resolver
merge-resolver
Installation
$ npx skills add https://github.com/blueif16/amazing-claude-code-plugins --skill merge-resolver
SKILL.md
合并解决器 v2

所有者: 仅主协调器

职责
接收所有已完成部分的列表
按依赖顺序顺序合并每个部分
自动解决可处理的冲突
记录无法自动解决的冲突
运行完整测试套件验证集成
清理成功合并的 worktrees 和分支
生成最终执行报告
触发条件

当 execution-manager 的监控循环检测到所有部分状态为 completed 或 blocked 时自动触发。

执行流程
Phase 1: 准备和决策
# 切换到主分支
git checkout main
git pull origin main

# 获取所有已完成部分的分支列表
completed_sections=$(yq '.sections | to_entries | map(select(.value.status == "completed")) | .[].key' meta.yaml)
blocked_sections=$(yq '.sections | to_entries | map(select(.value.status == "blocked")) | .[].key' meta.yaml)

# 合并前先决条件检查
for section in $completed_sections; do
  branch="${project_name}/${section}"

  # 检查分支是否有提交（不仅仅是暂存的更改）
  if ! git log main..${branch} --oneline | grep -q .; then
    echo "⚠️ $section: 分支没有提交，跳过"
    continue
  fi

  # 验证没有 .task/ 文件将被合并
  if git diff main..${branch} --name-only | grep -q "^\.task/"; then
    echo "⚠️ $section: 包含 .task/ 文件，需要清理"
    continue
  fi
done

# 验证主分支状态干净
if ! git status --porcelain | grep -q "^$"; then
  echo "⚠️ 主分支有未提交的更改，先清理"
  exit 1
fi

# 如果有阻塞的部分，询问人工
if [ -n "$blocked_sections" ]; then
  echo "以下部分被阻塞: $blocked_sections"
  echo "是否继续合并已完成的部分? (y/n)"
  read -t 30 response || response="y"  # 30秒超时，默认继续

  if [ "$response" != "y" ]; then
    echo "合并已取消，等待人工处理阻塞部分"
    exit 0
  fi
fi

Phase 2: 顺序合并（按依赖顺序）
project_name=$(yq '.project' meta.yaml)
merge_success=()
merge_conflicts=()

for section in $completed_sections; do
  branch="${project_name}/${section}"

  echo "正在合并: $section"

  # 预览变更
  git diff main..${branch} --stat

  # 尝试合并（使用 patience 算法获得更好的差异）
  if git merge -X patience ${branch} --no-ff -m "Merge ${section}: auto-merged by InfiStack"; then
    echo "✅ $section 合并成功"
    merge_success+=("$section")

    # 立即清理该 worktree 和分支
    git worktree remove ../worktrees/${section} --force 2>/dev/null || true
    git branch -d ${branch}

    # 更新 meta.yaml
    yq -i ".sections.${section}.merge_status = \"merged\"" meta.yaml
    yq -i ".sections.${section}.merged_at = \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"" meta.yaml

  else
    echo "⚠️ $section 存在冲突"

    # 尝试自动解决
    if auto_resolve_conflicts "$section"; then
      git add -A
      git commit -m "Merge ${section}: conflicts auto-resolved by InfiStack"
      echo "✅ $section 冲突已自动解决并合并"
      merge_success+=("$section")

      # 清理
      git worktree remove ../worktrees/${section} --force 2>/dev/null || true
      git branch -d ${branch}
      yq -i ".sections.${section}.merge_status = \"merged_with_auto_resolution\"" meta.yaml

    else
      # 记录冲突，中止合并，保留分支和 worktree
      git merge --abort
      merge_conflicts+=("$section")

      # 记录冲突信息
      record_conflict_report "$section" "$branch"
      yq -i ".sections.${section}.merge_status = \"conflict\"" meta.yaml

      echo "❌ $section 需要人工解决冲突"
    fi
  fi
done

Phase 3: 验证集成（必需）

合并所有部分后必须进行验证：

# 只有在至少有一个成功合并时才运行测试
if [ ${#merge_success[@]} -gt 0 ]; then
  echo "运行完整测试套件..."

  # 检测项目类型并运行相应测试
  if [ -f "package.json" ]; then
    npm test || test_failed=true
  elif [ -f "requirements.txt" ]; then
    pytest || test_failed=true
  elif [ -f "Cargo.toml" ]; then
    cargo test || test_failed=true
  fi

  if [ "$test_failed" = true ]; then
    echo "⚠️ 集成测试在合并后失败"
    # 识别哪个合并导致失败（二分或选择性回滚）
    git log --oneline -5
    # 向人工报告失败详情
    yq -i ".test_status = \"failed\"" meta.yaml
  else
    echo "✅ 所有测试通过"
    yq -i ".test_status = \"passed\"" meta.yaml
  fi
fi

Phase 4: 生成最终报告
# 生成执行报告
cat > execution-report.md <<EOF
# InfiStack 执行报告

**项目:** ${project_name}
**完成时间:** $(date -u +%Y-%m-%dT%H:%M:%SZ)

## 总览
- 总部分数: $(yq '.sections | length' meta.yaml)
- 成功合并: ${#merge_success[@]}
- 冲突需处理: ${#merge_conflicts[@]}
- 阻塞部分: $(echo "$blocked_sections" | wc -w)
- 测试状态: $(yq '.test_status' meta.yaml)

## 已合并部分
$(for s in "${merge_success[@]}"; do echo "- ✅ $s (branch deleted, worktree removed)"; done)

## 需要人工处理的冲突
$(for s in "${merge_conflicts[@]}"; do
  report_path="sections/${s}/merge-conflict.md"
  branch="${project_name}/${s}"
  echo "- ⚠️ $s"
  echo "  - 冲突报告: $report_path"
  echo "  - 分支保留: $branch"
  echo "  - Worktree: ../worktrees/$s"
done)

## 阻塞部分
$(for s in $blocked_sections; do
  echo "- ❌ $s: 需要人工干预"
done)

## 下一步

$(if [ ${#merge_conflicts[@]} -gt 0 ]; then
  echo "### 解决冲突"
  echo "1. 查看冲突报告了解详情"
  echo "2. 手动解决冲突文件"
  echo "3. 提交合并: \`git commit -m 'Resolve conflicts in <section>'\`"
  echo "4. 清理: \`git worktree remove ../worktrees/<section> && git branch -d <branch>\`"
elif [ -n "$blocked_sections" ]; then
  echo "### 处理阻塞部分"
  echo "查看各部分的 error-report.md 了解阻塞原因"
else
  echo "### 项目完成"
  echo "所有部分已成功合并并通过测试。项目实现完成！"
fi)
EOF

# 显示报告
cat execution-report.md

自动冲突解决策略
通用解决策略
合并前尝试语义合并
# 使用更好的差异算法
git merge -X patience {branch}

# 针对特定文件类型的策略
git checkout --theirs .task/  # .task 文件始终采用他们的版本

可自动解决的冲突类型

package.json 依赖冲突

合并两边的 dependencies 和 devDependencies
对于版本冲突，选择较新的语义化版本

import 语句冲突

保留两边的 import 语句
去重相同的导入

类型定义添加

合并两边的类型导出
保留所有接口和类型定义

配置文件 (*.json, *.yaml, *.env.example)

深度合并 JSON/YAML 对象
优先使用分支版本的新增字段
必须人工处理的冲突
同一函数体内的逻辑冲突
API 接口变更
数据库 schema 冲突
测试用例逻辑冲突
业务逻辑 (controllers, services, utils)
自动解决实现
auto_resolve_conflicts() {
  local section=$1
  local conflict_files=$(git diff --name-only --diff-filter=U)
  local all_resolved=true

  for file in $conflict_files; do
    case "$file" in
      .task/*)
        # .task 文件：始终采用他们的版本
        echo "自动解决 .task/ 冲突: $file"
        git checkout --theirs $file
        git add $file
        ;;

      package.json)
        # 使用 jq 合并依赖
        echo "自动解决 package.json 依赖冲突..."
        # 提取两边的依赖并合并
        git show :1:$file > base.json
        git show :2:$file > ours.json
        git show :3:$file > theirs.json

        # 合并逻辑（简化示例）
        jq -s '.[0] * .[1] * .[2]' base.json ours.json theirs.json > $file
        git add $file
        rm base.json ours.json theirs.json
        ;;

      *.d.ts|*/types/*)
        # 类型定义：尝试保留两边
        echo "自动解决类型定义冲突: $file"
        git checkout --theirs $file
        git add $file
        ;;

      *.json|*.yaml|*.yml)
        # 配置文件：优先使用分支版本
        echo "自动解决配置文件冲突: $file"
        git checkout --theirs $file
        git add $file
        ;;

      *)
        # 无法自动解决
        echo "无法自动解决: $file"
        all_resolved=false
        ;;
    esac
  done

  if [ "$all_resolved" = true ]; then
    return 0
  else
    return 1
  fi
}

冲突记录格式

当遇到无法自动解决的冲突时，创建 sections/{section-id}/merge-conflict.md。

record_conflict_report 实现
record_conflict_report() {
  local section=$1
  local branch=$2
  local conflict_files=$(git diff --name-only --diff-filter=U)
  local report_path="sections/${section}/merge-conflict.md"

  mkdir -p "sections/${section}"

  cat > "$report_path" <<EOF
# 合并冲突报告

**分支:** ${branch}
**时间:** $(date -u +%Y-%m-%dT%H:%M:%SZ)
**部分:** ${section}

## 冲突文件列表

$(for file in $conflict_files; do
  echo "### $file"
  echo ""
  echo "\`\`\`diff"
  git diff $file | head -100
  echo "\`\`\`"
  echo ""
done)

## 解决步骤

1. 切换到冲突分支的 worktree:
   \`\`\`bash
   cd ../worktrees/${section}
   \`\`\`

2. 手动编辑冲突文件，解决标记的冲突

3. 标记为已解决:
   \`\`\`bash
   git add <冲突文件>
   \`\`\`

4. 完成合并:
   \`\`\`bash
   git commit -m "Resolve conflicts in ${section}"
   \`\`\`

5. 返回主分支并清理:
   \`\`\`bash
   cd <主项目目录>
   git worktree remove ../worktrees/${section}
   git branch -d ${branch}
   \`\`\`

## 建议

- 仔细检查业务逻辑冲突，确保功能正确性
- 运行相关测试确保没有破坏现有功能
- 如有疑问，查看两个版本的完整上下文
EOF

  echo "冲突报告已生成: $report_path"
}

冲突报告示例
# 合并冲突报告

**分支:** reddit-bot/ui-components
**时间:** 2025-12-26T10:30:00Z
**部分:** ui-components

## 冲突文件列表

### src/components/Button.tsx
- **冲突类型:** 业务逻辑
- **冲突行:** 45-62

**主分支版本:**
```typescript
async handleClick() {
  await this.props.onClick();
}


功能分支版本:

async handleClick() {
  this.setState({ loading: true });
  await this.props.onClick();
  this.setState({ loading: false });
}


建议: 功能分支添加了加载状态，建议保留此增强功能



## meta.yaml 状态跟踪

merge-resolver 会更新 meta.yaml 中的合并状态：

```yaml
project: reddit-bot
sections:
  auth:
    status: completed
    merge_status: merged
    merged_at: "2025-12-26T10:15:00Z"

  payments:
    status: completed
    merge_status: merged_with_auto_resolution
    merged_at: "2025-12-26T10:20:00Z"

  ui-components:
    status: completed
    merge_status: conflict
    conflict_report: sections/ui-components/merge-conflict.md
    branch_preserved: reddit-bot/ui-components
    worktree_path: ../worktrees/ui-components

  notifications:
    status: blocked
    escalation_report: sections/notifications/error-report.md

test_status: passed
execution_completed_at: "2025-12-26T10:25:00Z"

关键原则
1. 永不提前退出

merge-resolver 必须处理完所有已完成的部分才能返回控制权给人工。

2. 失败不阻塞

一个部分的冲突不应阻止其他部分的合并。继续处理所有部分，最后统一报告。

3. 自动清理

成功合并的部分立即清理 worktree 和分支，减少后续手动操作。

4. 详细报告

生成完整的执行报告，包含所有成功、失败和阻塞的部分，以及具体的下一步操作指导。

5. 测试验证

在合并后运行完整测试套件，确保集成没有破坏现有功能。

工作流程总结
execution-manager 检测所有部分完成
         ↓
    调用 merge-resolver
         ↓
    Phase 1: 准备和决策
    - 检查是否有阻塞部分
    - 询问人工是否继续（30秒超时）
         ↓
    Phase 2: 顺序合并
    - 遍历所有已完成部分
    - 尝试自动合并
    - 冲突时尝试自动解决
    - 无法解决则记录并继续
    - 成功则立即清理
         ↓
    Phase 3: 验证集成
    - 运行完整测试套件
    - 记录测试结果
         ↓
    Phase 4: 生成报告
    - 统计成功/失败/阻塞
    - 提供具体的下一步指导
    - 显示报告给人工
         ↓
    返回控制权给人工

Weekly Installs
12
Repository
blueif16/amazin…-plugins
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail