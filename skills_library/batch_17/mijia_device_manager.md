---
title: mijia-device-manager
url: https://skills.sh/dean2021/mijia-device-manager/mijia-device-manager
---

# mijia-device-manager

skills/dean2021/mijia-device-manager/mijia-device-manager
mijia-device-manager
Installation
$ npx skills add https://github.com/dean2021/mijia-device-manager --skill mijia-device-manager
SKILL.md
米家设备管理器
概述

此技能用于管理和控制小米/米家智能家居设备，直接调用 mijiaAPI CLI 通过小米云端 API 控制设备。

功能特性
登录小米账号（扫码登录）
获取设备列表和家庭列表
获取和设置设备属性
执行设备动作
查看设备完整状态
前提条件
安装依赖：
pip install mijiaAPI

登录小米账号（首次使用需要）：
python -m mijiaAPI --list_homes

快速开始
1. 首次登录
python -m mijiaAPI --list_homes


运行后会显示二维码，使用米家 APP 扫描即可完成登录。

2. 查看设备列表
python -m mijiaAPI -l


输出中每条设备信息包含 did，后续控制命令使用该值。

3. 控制设备
# 开灯
python -m mijiaAPI set --did "123456789" --prop_name "on" --value True

# 设置亮度
python -m mijiaAPI set --did "123456789" --prop_name "brightness" --value 50

# 获取状态
python -m mijiaAPI get --did "123456789" --prop_name "brightness"

命令参考
python -m mijiaAPI --help
python -m mijiaAPI get --help
python -m mijiaAPI set --help


常用命令示例：

# 列出所有设备
python -m mijiaAPI -l

# 从列表中找到 did
python -m mijiaAPI -l | grep did

# 列出所有家庭
python -m mijiaAPI --list_homes

# 获取设备属性
python -m mijiaAPI get --did "123456789" --prop_name "brightness"

# 设置设备属性
python -m mijiaAPI set --did "123456789" --prop_name "on" --value True
python -m mijiaAPI set --did "123456789" --prop_name "brightness" --value 50

# 执行场景
python -m mijiaAPI --run_scene "回家"

设备属性参考

常见设备属性名称：

属性名	说明	类型	示例值
on	开关状态	bool	True/False
brightness	亮度	int	0-100
color-temperature	色温	int	2700-6500
color	颜色	int	RGB值

注意： 不同设备支持的属性不同，操作前先使用 --get_device_info DEVICE_MODEL 获取设备属性信息，确认可操作的属性后再执行控制命令。DEVICE_MODEL 可通过 --list_devices 获取。

操作步骤：

使用 python -m mijiaAPI -l 列出设备，确认 did 与 DEVICE_MODEL。
使用 python -m mijiaAPI --get_device_info DEVICE_MODEL 获取可用属性与范围。
根据属性信息执行 get 或 set 命令完成查询或控制。
故障排除
登录问题

问题：无法登录或提示认证失败

删除认证文件重新登录：

rm ~/.config/mijia-api/auth.json
python -m mijiaAPI --list_homes


检查网络连接是否正常

确认米家APP账号和密码正确

设备控制问题

问题：找不到设备

确认设备已在米家APP中添加
检查设备名称是否正确（区分大小写）
使用 -l 命令查看准确的设备名称

问题：不知道 did

使用 python -m mijiaAPI -l 列出设备，在输出中找到设备的 did 字段

问题：属性设置失败

确认设备支持该属性（使用 --get_device_info DEVICE_MODEL 获取属性信息）
检查属性值范围是否正确
确认设备在线且网络正常

问题：想知道某个设备都有哪些属性

先用 --list_devices 获取 DEVICE_MODEL，再用 --get_device_info DEVICE_MODEL 获取属性信息，例如：
python -m mijiaAPI --get_device_info yeelink.light.lamp27

获取帮助
mijiaAPI GitHub: https://github.com/Do1e/mijia-api
米家规格平台: https://home.miot-spec.com/
Weekly Installs
51
Repository
dean2021/mijia-…-manager
GitHub Stars
115
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass