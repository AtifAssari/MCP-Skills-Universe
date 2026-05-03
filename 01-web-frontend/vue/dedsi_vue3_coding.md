---
rating: ⭐⭐⭐
title: dedsi-vue3-coding
url: https://skills.sh/dedsiteam/dedsi-skills/dedsi-vue3-coding
---

# dedsi-vue3-coding

skills/dedsiteam/dedsi-skills/dedsi-vue3-coding
dedsi-vue3-coding
Installation
$ npx skills add https://github.com/dedsiteam/dedsi-skills --skill dedsi-vue3-coding
SKILL.md
Dedsi Vue3 Coding

Vue 3 + TypeScript 项目开发规范，使用 Dedsi UI 组件库。

何时使用
创建新的 Vue 3 页面组件
实现 CRUD（增删改查）功能
定义 API 服务层
使用 Dedsi UI 组件
处理表单和表格数据
遵循项目代码规范
能力规则

没有这些规则，AI 无法解决问题或生成的代码无法正确运行。

API 服务层
规则	影响	描述
api-service-patterns.md	HIGH	API 服务类定义和标准方法
View 组件
规则	影响	描述
view-component-patterns.md	HIGH	页面组件结构和状态管理
component-mapping.md	HIGH	Dedsi UI 组件映射
icon-usage.md	MEDIUM	图标使用规范
数据处理
规则	影响	描述
table-data-handling.md	HIGH	Table 数据加载和分页
form-handling.md	HIGH	表单状态和提交处理
form-validation.md	HIGH	表单验证规则
delete-operations.md	MEDIUM	删除操作和确认
view-detail-modal.md	MEDIUM	查看详情弹窗
效率规则

这些规则帮助 AI 更有效、更一致地解决问题。

代码模板
规则	影响	描述
code-templates.md	MEDIUM	标准 API Service 和 View 组件模板
技术栈
框架: Vue 3 (Composition API)
语言: TypeScript
UI 组件库: Dedsi UI
前缀: dedsi- (如 dedsi-button, dedsi-table)
图标: @ant-design/icons-vue
日期处理: dayjs
HTTP 客户端: 自定义 AxiosRequest 封装
项目结构
src/
├── apiServices/          # API 服务层
│   ├── identitys/        # 身份认证服务
│   │   ├── userService.ts
│   │   ├── types.ts
│   │   └── index.ts
│   └── index.ts          # 统一导出
├── components/           # 可复用组件
├── configs/             # 配置文件
├── layouts/             # 布局组件
├── router/              # 路由配置
├── stores/              # Pinia 状态管理
├── utils/               # 工具函数
├── views/               # 页面视图
└── App.vue

开发规范
核心原则
组件优先: 优先使用 dedsi- 前缀的 Dedsi UI 组件
Composition API: 所有组件使用 <script setup lang="ts">
类型安全: 严格使用 TypeScript 类型定义
错误处理: 统一使用 try-catch 和 DedsiMessage
API 服务层

位置: src/apiServices/{module}/

使用 class 定义服务
导出服务实例（单例模式）
DTO 类型定义在 types.ts 中
实现标准方法：pagedQuery, get, create, update, delete
View 组件

使用 Composition API:

<script setup lang="ts">
import { reactive, ref, onMounted } from 'vue'
</script>


标准页面结构:

搜索卡片 (dedsi-card + dedsi-form)
表格卡片 (dedsi-card + dedsi-table)
弹窗表单 (dedsi-modal + dedsi-form)
核心状态
// 表格数据
const tableLoading = ref(false)
const tableData = ref<Dto[]>()

// 分页配置
const pagination = reactive({
  current: 1,
  pageSize: 10,
  total: 0
})

// 查询参数
const queryParam = reactive<Partial<InputDto>>({ ... })

// 弹窗表单
const modalVisible = ref(false)
const formState = reactive<any>({ ... })

最佳实践
1. Table 列定义
优先使用 slot 方式定义列，便于自定义渲染
时间字段使用 dayjs 格式化
操作列使用 template #actions 插槽
2. 数据加载
统一封装 fetchData 方法
try-catch 包裹 API 请求
finally 中重置 tableLoading.value = false
3. 表单处理
编辑时使用 Object.assign(formState, detail) 回填数据
新增时需重置 formState
提交时根据是否有 id 判断是 Create 还是 Update
使用 formRef 进行表单验证
4. 表单验证
使用 :rules 定义验证规则
手动调用 formRef.value?.validate() 验证
关闭弹窗时调用 formRef.value?.clearValidate() 清除验证
5. 图标使用
从 @ant-design/icons-vue 导入图标
使用 <template #icon> 插槽添加图标到按钮
6. 删除操作
使用 dedsi-popconfirm 包裹删除按钮
防止误操作
7. 查看详情
提供独立的查看详情弹窗
对关键字段使用 dedsi-typography:copyable 支持复制
参考
Dedsi Vue-UI - Dedsi UI 组件库文档
Vue 3 Documentation - Vue 3 官方文档
TypeScript Documentation - TypeScript 官方文档
Weekly Installs
15
Repository
dedsiteam/dedsi-skills
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass