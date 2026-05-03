---
title: proxychains
url: https://skills.sh/2025emma/vibe-coding-cn/proxychains
---

# proxychains

skills/2025emma/vibe-coding-cn/proxychains
proxychains
Installation
$ npx skills add https://github.com/2025emma/vibe-coding-cn --skill proxychains
SKILL.md
Proxychains Network Proxy Skill

自动使用代理解决网络问题 - 当遇到网络连接失败、超时或访问受限时，自动使用 proxychains4 强制走代理。

When to Use This Skill

触发条件（自动应用）:

❌ Connection timeout errors
❌ DNS resolution failures
❌ "Connection refused" errors
❌ HTTP 403/451 blocked access
❌ GitHub/PyPI/npm 等国外资源访问失败
❌ curl/wget/git/pip 等命令失败

Claude 应该：

检测到网络错误后，自动在命令前添加 proxychains4
使用默认代理配置：http://127.0.0.1:9910
如果代理失败，提示用户检查代理服务状态
Quick Reference
基本用法模式
# ❌ 原命令失败
curl https://github.com/user/repo

# ✅ 使用代理重试
proxychains4 curl https://github.com/user/repo

常见场景自动应用

场景 1: Git 操作失败

# 原命令
git clone https://github.com/user/repo.git

# 自动改为
proxychains4 git clone https://github.com/user/repo.git


场景 2: Python pip 安装失败

# 原命令
pip install requests

# 自动改为
proxychains4 pip install requests


场景 3: npm/yarn 安装失败

# 原命令
npm install package-name

# 自动改为
proxychains4 npm install package-name


场景 4: wget/curl 下载失败

# 原命令
wget https://example.com/file.tar.gz

# 自动改为
proxychains4 wget https://example.com/file.tar.gz


场景 5: Docker 拉取镜像失败

# 原命令
docker pull image:tag

# 自动改为
proxychains4 docker pull image:tag


场景 6: SSH 连接失败

# 原命令
ssh user@remote-host

# 自动改为
proxychains4 ssh user@remote-host

配置详情
默认代理配置

本地代理地址： http://127.0.0.1:9910

配置文件位置：

~/.proxychains/proxychains.conf (推荐)
/etc/proxychains.conf (系统级)
快速配置脚本

创建用户级配置（自动使用 127.0.0.1:9910）：

mkdir -p ~/.proxychains
cat > ~/.proxychains/proxychains.conf << 'EOF'
# Proxychains configuration
strict_chain
proxy_dns
remote_dns_subnet 224
tcp_read_time_out 15000
tcp_connect_time_out 8000

[ProxyList]
http 127.0.0.1 9910
EOF

环境变量方式（临时使用）
# 设置代理环境变量
export PROXYCHAINS_SOCKS5_HOST=127.0.0.1
export PROXYCHAINS_SOCKS5_PORT=9910

# 使用
proxychains4 curl https://github.com

工作原理

Proxychains 通过 LD_PRELOAD 机制拦截程序的网络调用：

拦截系统调用：Hook socket 相关的 libc 函数
重定向连接：将所有 TCP 连接重定向到代理服务器
DNS 代理：通过代理服务器解析域名
透明代理：应用程序无需修改

重要限制：

只支持动态链接的程序（statically linked 程序不支持）
只支持 TCP 连接（UDP 不支持）
部分使用特殊网络库的程序可能不兼容
Claude 自动化规则
规则 1: 网络错误自动重试
IF 命令返回网络相关错误（timeout, connection refused, DNS failure）
THEN 自动使用 proxychains4 重试该命令

规则 2: 已知慢速源强制代理
IF 访问以下域名/服务：
  - github.com
  - raw.githubusercontent.com
  - pypi.org
  - npmjs.org
  - registry.npmjs.org
  - docker.io
  - gcr.io
THEN 直接使用 proxychains4（不等待失败）

规则 3: 失败提示
IF proxychains4 命令也失败
THEN 提示用户：
  1. 检查代理服务是否运行（127.0.0.1:9910）
  2. 检查 proxychains 配置文件
  3. 尝试其他代理地址

故障排除
检查代理服务状态
# 测试代理是否可用
curl -x http://127.0.0.1:9910 https://www.google.com

# 检查端口是否监听
netstat -tunlp | grep 9910
# 或
ss -tunlp | grep 9910

验证 proxychains 配置
# 测试配置是否正确
proxychains4 curl https://ipinfo.io/json
# 应该显示代理服务器的 IP，而不是本机 IP

常见错误处理

错误 1: "proxychains: command not found"

# 安装 proxychains4
sudo apt install proxychains4  # Debian/Ubuntu
sudo yum install proxychains-ng  # CentOS/RHEL


错误 2: "timeout"

# 检查代理地址配置是否正确
cat ~/.proxychains/proxychains.conf | grep -A 2 "\[ProxyList\]"

# 修改超时时间（在配置文件中）
tcp_connect_time_out 15000
tcp_read_time_out 30000


错误 3: "can't read configuration file"

# 创建配置文件
mkdir -p ~/.proxychains
cp /etc/proxychains.conf ~/.proxychains/proxychains.conf
# 然后编辑配置

高级用法
多代理链
# ~/.proxychains/proxychains.conf
strict_chain  # 按顺序使用所有代理

[ProxyList]
http 127.0.0.1 9910
socks5 127.0.0.1 1080

动态代理链
dynamic_chain  # 自动跳过死代理

[ProxyList]
http 127.0.0.1 9910
http 127.0.0.1 8080
socks5 127.0.0.1 1080

随机代理链
random_chain
chain_len = 2  # 随机选择 2 个代理

[ProxyList]
http 127.0.0.1 9910
socks5 127.0.0.1 1080
socks5 127.0.0.1 1081

自定义 DNS 服务器
# 使用自定义 DNS 通过代理解析
export PROXY_DNS_SERVER=8.8.8.8
proxychains4 curl https://example.com

参考资源
官方仓库: https://github.com/haad/proxychains
配置文件: references/proxychains.conf (完整示例)
故障排除: references/troubleshooting.md
命令速查: references/quick-reference.md
总结

记住这些原则：

❌ 遇到网络错误 → ✅ 自动加上 proxychains4
🌐 访问国外资源 → ✅ 主动使用 proxychains4
🔧 代理也失败 → ✅ 提示用户检查代理服务

默认代理: http://127.0.0.1:9910

这个技能让 Claude 在遇到网络问题时自动使用代理，无需用户手动干预！

Weekly Installs
117
Repository
2025emma/vibe-coding-cn
GitHub Stars
20.1K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn