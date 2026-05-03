---
title: api-security-testing
url: https://skills.sh/ed1s0nz/cyberstrikeai/api-security-testing
---

# api-security-testing

skills/ed1s0nz/cyberstrikeai/api-security-testing
api-security-testing
Installation
$ npx skills add https://github.com/ed1s0nz/cyberstrikeai --skill api-security-testing
SKILL.md
API安全测试
概述

API安全测试是确保API接口安全性的重要环节。本技能提供API安全测试的方法、工具和最佳实践。

测试范围
1. 认证和授权

测试项目：

Token有效性验证
Token过期处理
权限控制
角色权限验证
2. 输入验证

测试项目：

参数类型验证
数据长度限制
特殊字符处理
SQL注入防护
XSS防护
3. 业务逻辑

测试项目：

工作流验证
状态转换
并发控制
业务规则
4. 错误处理

测试项目：

错误信息泄露
堆栈跟踪
敏感信息暴露
测试方法
1. API发现

识别API端点：

# 使用目录扫描
gobuster dir -u https://target.com -w api-wordlist.txt

# 使用Burp Suite被动扫描
# 浏览应用，观察API调用

# 分析JavaScript文件
# 查找API端点定义

2. 认证测试

Token测试：

# 测试无效Token
GET /api/user
Authorization: Bearer invalid_token

# 测试过期Token
GET /api/user
Authorization: Bearer expired_token

# 测试无Token
GET /api/user


JWT测试：

# 使用jwt_tool
python jwt_tool.py <JWT_TOKEN>

# 测试算法混淆
python jwt_tool.py <JWT_TOKEN> -X a

# 测试密钥暴力破解
python jwt_tool.py <JWT_TOKEN> -C -d wordlist.txt

3. 授权测试

水平权限：

# 用户A访问用户B的资源
GET /api/user/123
Authorization: Bearer user_a_token

# 应该返回403


垂直权限：

# 普通用户访问管理员接口
GET /api/admin/users
Authorization: Bearer user_token

# 应该返回403

4. 输入验证测试

SQL注入：

POST /api/search
{
  "query": "test' OR '1'='1"
}


命令注入：

POST /api/execute
{
  "command": "ping; id"
}


XXE：

POST /api/parse
Content-Type: application/xml

<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<foo>&xxe;</foo>

5. 速率限制测试

测试速率限制：

import requests

for i in range(1000):
    response = requests.get('https://target.com/api/endpoint')
    print(f"Request {i}: {response.status_code}")

工具使用
Postman

创建测试集合：

导入API文档
设置认证
创建测试用例
运行自动化测试
Burp Suite

API扫描：

配置API端点
设置认证
运行主动扫描
分析结果
OWASP ZAP
# API扫描
zap-cli quick-scan --self-contained \
  --start-options '-config api.disablekey=true' \
  http://target.com/api

REST-Attacker
# 扫描OpenAPI规范
rest-attacker scan openapi.yaml

常见漏洞
1. 认证绕过

Token验证缺陷：

弱Token生成
Token可预测
Token不验证签名
2. 权限提升

IDOR：

直接对象引用
未验证资源所有权
3. 信息泄露

错误信息：

详细错误信息
堆栈跟踪
敏感数据
4. 注入漏洞

常见注入：

SQL注入
NoSQL注入
命令注入
XXE
5. 业务逻辑

逻辑缺陷：

价格操作
数量限制绕过
状态修改
测试清单
认证测试
 Token有效性验证
 Token过期处理
 弱Token检测
 Token重放攻击
授权测试
 水平权限测试
 垂直权限测试
 角色权限验证
 资源访问控制
输入验证
 SQL注入测试
 XSS测试
 命令注入测试
 XXE测试
 参数污染
业务逻辑
 工作流验证
 状态转换
 并发控制
 业务规则
错误处理
 错误信息泄露
 堆栈跟踪
 敏感信息暴露
防护措施
推荐方案

认证

使用强Token
实现Token刷新
验证Token签名

授权

基于角色的访问控制
资源所有权验证
最小权限原则

输入验证

参数类型验证
数据长度限制
白名单验证

错误处理

统一错误响应
不泄露详细信息
记录错误日志

速率限制

实现API限流
防止暴力破解
监控异常请求
注意事项
仅在授权测试环境中进行
避免对API造成影响
注意不同API版本的差异
测试时注意请求频率
Weekly Installs
36
Repository
ed1s0nz/cyberstrikeai
GitHub Stars
3.5K
First Seen
Feb 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn