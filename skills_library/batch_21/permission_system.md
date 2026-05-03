---
title: permission-system
url: https://skills.sh/m19803261706/springboot-vben-admin/permission-system
---

# permission-system

skills/m19803261706/springboot-vben-admin/permission-system
permission-system
Installation
$ npx skills add https://github.com/m19803261706/springboot-vben-admin --skill permission-system
SKILL.md
权限系统开发规范

本项目采用 RBAC (基于角色的访问控制) 权限模型，包含菜单权限、按钮权限和数据权限三个维度。

核心原则

重要: 每次创建新功能模块时，必须 同时创建对应的菜单权限迁移 SQL 文件，否则功能将无法正常使用。

一、权限体系架构
┌─────────────────────────────────────────────────────────────┐
│                      权限体系架构                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  用户 (sys_user)                                            │
│    │                                                        │
│    └── 拥有多个 ──→ 角色 (sys_role)                          │
│                      │                                      │
│                      ├── 拥有多个 ──→ 菜单权限 (sys_menu)     │
│                      │                 ├─ 目录 (type=0)     │
│                      │                 ├─ 菜单 (type=1)     │
│                      │                 └─ 按钮 (type=2)     │
│                      │                                      │
│                      └── 数据权限 (data_scope)               │
│                           ├─ 全部数据 (1)                   │
│                           ├─ 本部门 (2)                     │
│                           ├─ 本部门及下级 (3)               │
│                           ├─ 仅本人 (4)                     │
│                           └─ 自定义部门 (5)                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘

二、数据库表结构
2.1 菜单表 (sys_menu)
字段	类型	说明
id	bigint	主键
parent_id	bigint	父菜单ID (0=顶级)
menu_name	varchar(50)	菜单名称
menu_type	tinyint	类型: 0=目录, 1=菜单, 2=按钮
path	varchar(200)	路由路径
component	varchar(255)	组件路径
permission	varchar(100)	权限标识
icon	varchar(100)	图标
sort	int	排序
visible	tinyint	是否显示: 0=隐藏, 1=显示
status	tinyint	状态: 0=禁用, 1=启用
2.2 角色表 (sys_role)
字段	类型	说明
id	bigint	主键
role_name	varchar(30)	角色名称
role_code	varchar(100)	角色编码
data_scope	tinyint	数据权限范围 (1-5)
sort	int	排序
status	tinyint	状态
2.3 关联表
sys_user_role: 用户-角色关联
sys_role_menu: 角色-菜单关联
sys_role_dept: 角色-部门关联 (自定义数据权限)
三、权限标识命名规范
3.1 格式
{模块}:{实体}:{操作}

3.2 标准操作
操作	权限标识	说明
列表	xxx:entity:list	查看列表
详情	xxx:entity:detail	查看详情
新增	xxx:entity:add	新增数据
编辑	xxx:entity:edit	编辑数据
删除	xxx:entity:delete	删除数据
导出	xxx:entity:export	导出数据
导入	xxx:entity:import	导入数据
3.3 示例
# 系统管理模块
sys:user:list        # 用户列表
sys:user:add         # 新增用户
sys:role:assign      # 分配角色权限

# 业务模块示例
emergency:event:list     # 应急事件列表
emergency:event:handle   # 处理事件
emergency:plan:approve   # 审批预案

四、数据权限类型
类型	值	说明	实现方式
全部数据	1	无限制	不添加过滤条件
本部门	2	只看本部门	WHERE dept_id = 用户部门ID
本部门及下级	3	本部门树	WHERE dept_id IN (部门及子部门ID)
仅本人	4	只看自己创建的	WHERE create_by = 用户ID
自定义	5	指定部门	WHERE dept_id IN (角色配置的部门)
五、CX 命令集成规范
5.1 强制要求

当执行 /cx:do 或 /cx:plan 创建新功能模块时，必须 同时：

创建 Flyway 迁移 SQL 文件
包含菜单数据插入语句
包含管理员角色菜单权限分配语句
5.2 迁移文件命名
V{版本号}__{描述}.sql

示例:
V4__add_emergency_module_menu.sql
V5__add_monitor_module_menu.sql

5.3 迁移 SQL 模板
-- V{N}__add_{module}_menu.sql
-- 作者: CX
-- 日期: {日期}
-- 描述: 添加{模块名}模块菜单和权限

-- =============================================
-- 获取当前最大菜单ID
-- =============================================
SET @max_menu_id = (SELECT COALESCE(MAX(id), 100) FROM sys_menu);

-- =============================================
-- 添加{模块名}目录
-- =============================================
INSERT INTO sys_menu (id, parent_id, menu_name, menu_type, path, component, permission, icon, sort, visible, status) VALUES
(@max_menu_id + 1, 0, '{模块中文名}', 0, '/{module}', NULL, NULL, '{icon}', {sort}, 1, 1);

-- =============================================
-- 添加{功能名}菜单
-- =============================================
INSERT INTO sys_menu (id, parent_id, menu_name, menu_type, path, component, permission, icon, sort, visible, status) VALUES
(@max_menu_id + 2, @max_menu_id + 1, '{功能中文名}', 1, '/{module}/{entity}', '/{module}/{entity}/index', '{module}:{entity}:list', '{icon}', 1, 1, 1),
(@max_menu_id + 3, @max_menu_id + 2, '{功能}新增', 2, NULL, NULL, '{module}:{entity}:add', NULL, 1, 1, 1),
(@max_menu_id + 4, @max_menu_id + 2, '{功能}编辑', 2, NULL, NULL, '{module}:{entity}:edit', NULL, 2, 1, 1),
(@max_menu_id + 5, @max_menu_id + 2, '{功能}删除', 2, NULL, NULL, '{module}:{entity}:delete', NULL, 3, 1, 1);

-- =============================================
-- 为超级管理员分配新菜单权限
-- =============================================
INSERT INTO sys_role_menu (role_id, menu_id)
SELECT 1, id FROM sys_menu WHERE id > @max_menu_id;

六、完整示例：添加应急事件模块
6.1 迁移文件: V4__add_emergency_event_menu.sql
-- V4__add_emergency_event_menu.sql
-- 作者: CX
-- 日期: 2026-01-13
-- 描述: 添加应急事件管理模块菜单和权限

-- =============================================
-- 获取当前最大菜单ID (避免ID冲突)
-- =============================================
SET @max_menu_id = (SELECT COALESCE(MAX(id), 100) FROM sys_menu);

-- =============================================
-- 添加应急管理目录
-- =============================================
INSERT INTO sys_menu (id, parent_id, menu_name, menu_type, path, component, permission, icon, sort, visible, status) VALUES
(@max_menu_id + 1, 0, '应急管理', 0, '/emergency', NULL, NULL, 'ant-design:alert-outlined', 10, 1, 1);

-- =============================================
-- 添加事件管理菜单及按钮
-- =============================================
INSERT INTO sys_menu (id, parent_id, menu_name, menu_type, path, component, permission, icon, sort, visible, status) VALUES
-- 事件管理菜单
(@max_menu_id + 2, @max_menu_id + 1, '事件管理', 1, '/emergency/event', '/emergency/event/index', 'emergency:event:list', 'ant-design:file-exclamation-outlined', 1, 1, 1),
-- 事件管理按钮
(@max_menu_id + 3, @max_menu_id + 2, '事件新增', 2, NULL, NULL, 'emergency:event:add', NULL, 1, 1, 1),
(@max_menu_id + 4, @max_menu_id + 2, '事件编辑', 2, NULL, NULL, 'emergency:event:edit', NULL, 2, 1, 1),
(@max_menu_id + 5, @max_menu_id + 2, '事件删除', 2, NULL, NULL, 'emergency:event:delete', NULL, 3, 1, 1),
(@max_menu_id + 6, @max_menu_id + 2, '事件处理', 2, NULL, NULL, 'emergency:event:handle', NULL, 4, 1, 1),
(@max_menu_id + 7, @max_menu_id + 2, '事件导出', 2, NULL, NULL, 'emergency:event:export', NULL, 5, 1, 1);

-- =============================================
-- 添加预案管理菜单及按钮
-- =============================================
INSERT INTO sys_menu (id, parent_id, menu_name, menu_type, path, component, permission, icon, sort, visible, status) VALUES
-- 预案管理菜单
(@max_menu_id + 8, @max_menu_id + 1, '预案管理', 1, '/emergency/plan', '/emergency/plan/index', 'emergency:plan:list', 'ant-design:solution-outlined', 2, 1, 1),
-- 预案管理按钮
(@max_menu_id + 9, @max_menu_id + 8, '预案新增', 2, NULL, NULL, 'emergency:plan:add', NULL, 1, 1, 1),
(@max_menu_id + 10, @max_menu_id + 8, '预案编辑', 2, NULL, NULL, 'emergency:plan:edit', NULL, 2, 1, 1),
(@max_menu_id + 11, @max_menu_id + 8, '预案删除', 2, NULL, NULL, 'emergency:plan:delete', NULL, 3, 1, 1),
(@max_menu_id + 12, @max_menu_id + 8, '预案审批', 2, NULL, NULL, 'emergency:plan:approve', NULL, 4, 1, 1);

-- =============================================
-- 为超级管理员角色分配新菜单权限
-- =============================================
INSERT INTO sys_role_menu (role_id, menu_id)
SELECT 1, id FROM sys_menu WHERE id > @max_menu_id;

6.2 后端 Controller 权限注解
@RestController
@RequestMapping("/api/emergency/event")
@RequiredArgsConstructor
@Tag(name = "应急事件管理")
public class EmergencyEventController {

    private final EmergencyEventService eventService;

    @GetMapping
    @SaCheckPermission("emergency:event:list")
    @Operation(summary = "事件列表")
    public ApiResponse<Page<EventVO>> list(EventQueryDTO query) {
        return ApiResponse.success(eventService.findPage(query));
    }

    @PostMapping
    @SaCheckPermission("emergency:event:add")
    @Operation(summary = "新增事件")
    public ApiResponse<EventVO> create(@Valid @RequestBody EventCreateDTO dto) {
        return ApiResponse.success(eventService.create(dto));
    }

    @PutMapping("/{id}")
    @SaCheckPermission("emergency:event:edit")
    @Operation(summary = "编辑事件")
    public ApiResponse<EventVO> update(@PathVariable Long id, @Valid @RequestBody EventUpdateDTO dto) {
        return ApiResponse.success(eventService.update(id, dto));
    }

    @DeleteMapping("/{id}")
    @SaCheckPermission("emergency:event:delete")
    @Operation(summary = "删除事件")
    public ApiResponse<Void> delete(@PathVariable Long id) {
        eventService.delete(id);
        return ApiResponse.success();
    }

    @PutMapping("/{id}/handle")
    @SaCheckPermission("emergency:event:handle")
    @Operation(summary = "处理事件")
    public ApiResponse<EventVO> handle(@PathVariable Long id, @Valid @RequestBody EventHandleDTO dto) {
        return ApiResponse.success(eventService.handle(id, dto));
    }
}

6.3 前端路由配置 (由后端动态返回)

前端无需手动配置路由，菜单数据由后端 /api/auth/routes 接口动态返回。

七、数据权限使用
7.1 Service 层添加数据权限注解
@Service
@RequiredArgsConstructor
public class EmergencyEventServiceImpl implements EmergencyEventService {

    private final EmergencyEventRepository eventRepository;
    private final DataScopeHelper dataScopeHelper;

    @Override
    @DataScope(deptAlias = "", userAlias = "")
    public Page<EventVO> findPage(EventQueryDTO query) {
        Specification<EmergencyEvent> spec = (root, criteriaQuery, cb) -> {
            List<Predicate> predicates = new ArrayList<>();

            // 业务查询条件...

            // 数据权限过滤 (必须添加)
            Predicate dataScopePredicate = dataScopeHelper.buildDataScopePredicate(
                root, cb, "deptId", "createBy");
            if (dataScopePredicate != null) {
                predicates.add(dataScopePredicate);
            }

            return cb.and(predicates.toArray(new Predicate[0]));
        };

        return eventRepository.findAll(spec, pageRequest).map(this::convertToVO);
    }
}

八、常用图标参考
图标	图标名称	适用场景
⚙️	ant-design:setting-outlined	系统设置
👤	ant-design:user-outlined	用户管理
👥	ant-design:team-outlined	角色/团队
📋	ant-design:menu-outlined	菜单管理
🏢	ant-design:apartment-outlined	部门/组织
⚠️	ant-design:alert-outlined	告警/应急
📄	ant-design:file-outlined	文件/文档
📊	ant-design:bar-chart-outlined	统计/报表
🔔	ant-design:bell-outlined	通知/消息
📁	ant-design:folder-outlined	目录/分类
🔐	ant-design:safety-outlined	安全/权限
📝	ant-design:form-outlined	表单
九、检查清单

创建新功能模块时，请确认以下事项：

 创建 Flyway 迁移 SQL 文件 (V{N}_add{module}_menu.sql)
 菜单 ID 使用 @max_menu_id + N 避免冲突
 包含目录、菜单、按钮三级结构
 权限标识符合 {module}:{entity}:{action} 规范
 为超级管理员角色分配新菜单权限
 Controller 方法添加 @SaCheckPermission 注解
 需要数据权限的查询添加 DataScopeHelper 过滤
 前端页面组件路径与菜单 component 字段一致

项目: 应急管理系统 创建时间: 2026-01-13 更新时间: 2026-01-13

Weekly Installs
15
Repository
m19803261706/sp…en-admin
GitHub Stars
4
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass