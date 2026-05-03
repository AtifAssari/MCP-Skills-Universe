---
rating: ⭐⭐
title: net
url: https://skills.sh/zhinkgit/embeddedskills/net
---

# net

skills/zhinkgit/embeddedskills/net
net
Installation
$ npx skills add https://github.com/zhinkgit/embeddedskills --skill net
SKILL.md
Net Debug Skill

嵌入式网络通信调试工具，统一封装接口发现、抓包、离线分析、连通性测试、端口扫描和流量统计能力。

脚本与配置路径
脚本目录: <skill-dir>/scripts/
环境级配置: <skill-dir>/config.json（仅工具路径）
工程级配置: <workspace>/.embeddedskills/config.json（网络参数）
协议参考: <skill-dir>/references/common_protocols.json
依赖
tshark (随 Wireshark 安装，需加入 PATH)
dumpcap (随 Wireshark 安装)
可选: capinfos
Windows 自带: ipconfig、ping、tracert、netstat、arp、nslookup
Python 3.x (仅标准库)
抓包需要 Npcap 驱动，部分环境需管理员权限
配置
环境级配置 (skill/config.json)

仅保留工具路径相关的环境级配置：

{
  "tshark_exe": "tshark",
  "capinfos_exe": "capinfos"
}

工程级配置 (.embeddedskills/config.json)

工作区下的 .embeddedskills/config.json 存放工程级网络配置：

{
  "net": {
    "interface": "",
    "target": "",
    "capture_filter": "",
    "display_filter": "",
    "duration": 30,
    "timeout_ms": 1000,
    "scan_ports": "",
    "capture_format": "pcapng",
    "log_dir": ".embeddedskills/logs/net"
  }
}

参数解析优先级
CLI 参数 (--interface, --target 等) - 最高优先级
工程级配置 (.embeddedskills/config.json 中的 net 部分)
状态文件 (.embeddedskills/state.json 中的历史记录)
默认值 - 最低优先级

连接和采集参数按优先级解析，脚本通过 CLI 参数接收覆盖值。若配置缺少必要项或连接失败，询问用户并引导修改配置。

执行流程
检查 tshark 是否可用
按优先级解析参数：CLI > 工程级配置 > 状态文件 > 默认值
若无子命令，默认执行 iface（列出网络接口）
成功执行后，将确认的参数写回工程配置
运行对应脚本并输出结构化 JSON 结果
失败时优先提示权限、Npcap、过滤器、接口选择等问题
子命令
iface — 列出网络接口
python <skill-dir>/scripts/net_iface.py [--filter <关键词>] [--tshark] [--json]

--tshark: 同时显示 tshark 抓包接口索引映射
--filter: 按关键词筛选接口
无副作用，可直接执行
capture — 抓包
python <skill-dir>/scripts/net_capture.py [--interface <接口>] [--duration <秒>] [--capture-filter <过滤器>] [--display-filter <过滤器>] [--output <文件路径>] [--format <pcapng|pcap>] [--decode-as <规则>] [--json]

接口、过滤器、时长按优先级解析
--interface: 抓包接口（覆盖配置）
--duration: 抓包时长（覆盖配置）
--capture-filter: BPF 抓包过滤器（覆盖配置）
--display-filter: Wireshark 显示过滤器（覆盖配置）
--output: 保存抓包文件路径
--json: 输出 JSON Lines 格式（基于 tshark -T ek）
--decode-as: 自定义解码规则
默认格式 pcapng，参数完整后直接执行
analyze — 分析 pcap 文件
python <skill-dir>/scripts/net_analyze.py <pcap_file> [--mode <summary|protocols|conversations|endpoints|io|anomalies|all>] [--filter <显示过滤器>] [--top <数量>] [--decode-as <规则>] [--export-fields <字段列表>] [--output <CSV路径>] [--json]

基于 tshark 和 capinfos 进行离线分析
--mode all 输出全部分析维度
无副作用，可直接执行
ping — 连通性测试
python <skill-dir>/scripts/net_ping.py [--target <目标>] [--tcp <端口>] [--count <次数>] [--traceroute] [--concurrent <线程数>] [--timeout <毫秒>] [--json]

目标按优先级解析
--target: 目标地址（覆盖配置）
--tcp: TCP 连通性测试（指定端口）
--traceroute: 执行路由追踪
--timeout: 超时毫秒数（覆盖配置）
参数完整后直接执行
scan — 端口扫描
python <skill-dir>/scripts/net_scan.py [--target <目标>] [--ports <端口范围>] [--timeout <毫秒>] [--banner] [--concurrent <线程数>] [--json]

目标和端口范围按优先级解析
--target: 目标地址（覆盖配置）
--ports: 端口范围，如 '80,443,8000-8100'（覆盖配置）
--banner: 尝试获取服务 Banner
默认收敛到嵌入式常用端口集
参数完整后直接执行
stats — 流量统计
python <skill-dir>/scripts/net_stats.py [--interface <接口>] [--duration <秒>] [--display-filter <过滤器>] [--interval <秒>] [--mode <overview|protocol|endpoint|port>] [--json]

接口和时长按优先级解析
--interface: 抓包接口（覆盖配置）
--duration: 统计时长（覆盖配置）
--display-filter: Wireshark 显示过滤器（覆盖配置）
默认输出按时段汇总的 JSON
无副作用，可直接执行
输出格式

所有脚本输出统一的 JSON 结构:

{
  "status": "ok",
  "action": "<子命令名>",
  "summary": "<简要描述>",
  "details": { ... }
}


错误时:

{
  "status": "error",
  "action": "<子命令名>",
  "error": {
    "code": "<错误码>",
    "message": "<错误描述>"
  }
}


capture --json 输出 JSON Lines，进度信息写入 stderr。

交互策略
按优先级解析参数：CLI > 工程级配置 > 状态文件 > 默认值
优先用解析后的参数直接执行，不额外询问
连接失败时再询问用户并引导修改配置
成功执行后，确认的参数自动写回 .embeddedskills/config.json
未给扫描范围时默认收敛到单主机、小范围端口
结果中明确回显目标范围、过滤器和持续时间
抓包结果优先总结异常协议、重传、RST 等
抓包失败优先提示权限和 Npcap 问题
协议参考

需要查询嵌入式常用端口和协议映射时，读取 references/common_protocols.json。

Weekly Installs
49
Repository
zhinkgit/embeddedskills
GitHub Stars
145
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn