---
rating: ⭐⭐⭐
title: ruoyi-code-generator
url: https://skills.sh/alffei/skill_share/ruoyi-code-generator
---

# ruoyi-code-generator

skills/alffei/skill_share/ruoyi-code-generator
ruoyi-code-generator
Installation
$ npx skills add https://github.com/alffei/skill_share --skill ruoyi-code-generator
SKILL.md
RuoYi 代码生成器技能
📌 目标 (Goal)

根据用户提供的数据表信息（表名、字段定义），按照若依框架规范自动生成完整的 CRUD 代码，包括：

Java 后端代码（Domain、Mapper、Service、ServiceImpl、Controller）
MyBatis XML 映射文件
Vue 前端代码（页面组件、API 封装）
菜单初始化 SQL
📥 输入定义 (Input)

用户需要提供以下信息（可以通过对话澄清获取）：

参数	必填	说明	示例
tableName	✅	数据库表名	sys_product
tableComment	✅	表注释/功能名称	产品管理
columns	✅	字段列表（含类型、注释）	见下方示例
packageName	❌	包路径，默认 com.ruoyi.system	com.ruoyi.business
moduleName	❌	模块名，默认取表前缀后的名称	product
businessName	❌	业务名称，默认取表名去前缀	product
author	❌	作者名，默认 ruoyi	zhangsan
tplCategory	❌	模板类型: crud/tree/sub，默认 crud	crud
字段定义示例
{
  "tableName": "sys_product",
  "tableComment": "产品管理",
  "columns": [
    {"name": "product_id", "type": "bigint", "comment": "产品ID", "isPk": true, "isIncrement": true},
    {"name": "product_name", "type": "varchar(100)", "comment": "产品名称", "isRequired": true, "isQuery": true},
    {"name": "product_code", "type": "varchar(50)", "comment": "产品编码", "isRequired": true},
    {"name": "category_id", "type": "bigint", "comment": "分类ID", "dictType": "product_category"},
    {"name": "price", "type": "decimal(10,2)", "comment": "价格"},
    {"name": "status", "type": "char(1)", "comment": "状态（0正常 1停用）", "dictType": "sys_normal_disable"},
    {"name": "create_time", "type": "datetime", "comment": "创建时间"}
  ]
}

📤 输出定义 (Output)

生成以下文件结构的代码：

输出文件清单:
├── java/
│   ├── domain/{ClassName}.java          # 实体类
│   ├── mapper/{ClassName}Mapper.java    # Mapper接口
│   ├── service/I{ClassName}Service.java # Service接口
│   ├── service/impl/{ClassName}ServiceImpl.java  # Service实现
│   └── controller/{ClassName}Controller.java     # REST控制器
├── xml/
│   └── {ClassName}Mapper.xml             # MyBatis映射文件
├── vue/
│   ├── api/{businessName}.js             # API封装
│   └── views/{moduleName}/{businessName}/index.vue  # 页面组件
└── sql/
    └── {businessName}Menu.sql            # 菜单初始化SQL

📋 执行流程 (Workflow)
第一步：信息收集与验证
解析用户请求：识别表名、字段信息
缺省信息追问：如果缺少必要信息，主动询问用户
推断默认值：
className = 表名转大驼峰（去除表前缀如 sys_）
moduleName = 表前缀后的模块名
businessName = 表名去前缀后的小写形式
主键字段 = 字段中 isPk=true 的字段，默认为 {tableName}_id
第二步：变量准备

根据输入计算所有模板变量：

核心变量:
- ${tableName}         表名
- ${tableComment}      表注释  
- ${ClassName}         类名(大驼峰)
- ${className}         类名(小驼峰)
- ${moduleName}        模块名
- ${businessName}      业务名
- ${BusinessName}      业务名(首字母大写)
- ${packageName}       包路径
- ${author}            作者
- ${datetime}          生成日期
- ${pkColumn}          主键字段信息
- ${columns}           所有字段列表
- ${permissionPrefix}  权限前缀 (格式: moduleName:businessName)

第三步：代码生成

按顺序读取并填充模板：

读取模板文件：从 templates/ 目录加载对应模板
变量替换：将 ${变量名} 替换为实际值
条件处理：根据字段配置处理 #if/#foreach 逻辑
输出代码：生成最终代码文件
第四步：自检与交付
代码审查：检查生成的代码是否符合规范
依赖提示：告知用户需要添加的依赖或配置
使用说明：提供后续操作指引
⚠️ 约束条件 (Constraints)

命名规范：

类名必须使用大驼峰 (PascalCase)
变量名必须使用小驼峰 (camelCase)
包路径必须全小写

编码规范：

Java 文件使用 UTF-8 编码
缩进使用 4 个空格
必须包含完整的 Javadoc 注释

安全规范：

Controller 必须添加 @PreAuthorize 权限注解
删除操作必须添加 @Log 日志注解
敏感字段（如密码）不出现在列表展示中

禁止事项：

❌ 不生成测试类（如需要请单独请求）
❌ 不修改已存在的文件（除非用户明确要求）
❌ 不硬编码任何敏感信息
🔧 字段类型映射
数据库类型	Java类型	说明
bigint	Long	长整型
int/integer	Integer	整型
varchar/char/text	String	字符串
datetime/timestamp	Date	日期时间
date	Date	日期
decimal/numeric	BigDecimal	高精度数值
float/double	Double	浮点数
tinyint(1)/bit	Boolean	布尔值
📁 模板引用

生成代码时，请参考以下模板文件：

Java 模板: templates/java/ 目录下的 .vm 文件
Vue 模板: templates/vue/ 目录下的 .vm 文件
XML 模板: templates/xml/ 目录下的 .vm 文件
SQL 模板: templates/sql/ 目录下的 .vm 文件
💡 使用示例
示例对话 1：基础生成

用户: 帮我生成一个产品管理模块的代码，表名是 sys_product

Agent 响应:

首先确认字段信息
推断默认配置
生成完整代码
提供使用说明
示例对话 2：指定配置

用户:

生成代码:
- 表名: biz_order
- 功能: 订单管理  
- 包路径: com.ruoyi.business
- 字段: order_id(主键), order_no(订单号), customer_name(客户名), amount(金额), status(状态), create_time(创建时间)


Agent 响应:

已为您生成订单管理模块代码，包含以下文件：

Java后端:
- Order.java (实体类)
- OrderMapper.java (Mapper接口)
- IOrderService.java (Service接口)
- OrderServiceImpl.java (Service实现)
- OrderController.java (控制器)

MyBatis:
- OrderMapper.xml (映射文件)

Vue前端:
- order.js (API封装)
- index.vue (列表页面)

SQL脚本:
- orderMenu.sql (菜单初始化)

[具体代码内容...]

🔄 版本说明
兼容版本: RuoYi-Vue v3.9.x
前端框架: Vue 2 + Element UI
后端框架: Spring Boot 2.x + MyBatis
Weekly Installs
56
Repository
alffei/skill_share
GitHub Stars
63
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass