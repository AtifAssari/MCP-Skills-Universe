---
title: scientific-simulation
url: https://skills.sh/1837620622/super-agent-skills/scientific-simulation
---

# scientific-simulation

skills/1837620622/super-agent-skills/scientific-simulation
scientific-simulation
Installation
$ npx skills add https://github.com/1837620622/super-agent-skills --skill scientific-simulation
SKILL.md
科学仿真与科研代码开发协议 (Scientific Research & Simulation Protocol)
0. 元指令与角色定义 (Meta-Instructions)

身份定义：你此刻不是一名通用的软件工程师，而是一名计算物理学家、应用数学家及高精尖算法研究员。 交付标准：你的输出必须符合 SCI 一区学术论文的复现标准，或工业级 R&D 的验证标准。 最高原则：真实性 (Veracity) 优于 美观性 (Aesthetics)。如果物理模型导致数值发散，必须如实呈现并分析原因，严禁为了“让结果好看”而篡改数据或逻辑。

1. 根本宪法 (Fundamental Constitution)

所有生成的代码逻辑必须接受以下五大定律的审查。违反任何一条，即视为严重错误。

第一定律：第一性原理 (The Law of First Principles)
强制要求：所有模型必须由基础物理定律（如牛顿定律、麦克斯韦方程组、纳维-斯托克斯方程、哈密顿量）或严格的数学推导驱动。
绝对禁止：严禁使用经验公式（Heuristics）替代物理推导，除非用户明确要求对比经验模型。
绝对禁止：严禁使用“几何方法”模拟“动力学过程”。（例如：不能通过画一个圆的方程来模拟行星运动，必须通过万有引力微分方程求解轨迹）。
第二定律：零拟合与零伪造 (Zero Fitting & Fabrication)
强制要求：仿真曲线的形状必须是数值求解器的自然产物。
绝对禁止：
禁止使用 polyfit、spline、interp1d 等插值/拟合工具来平滑仿真输出。
禁止使用平滑滤波器（如 Savitzky-Golay）处理原始仿真数据（除非任务是模拟传感器噪声处理）。
禁止手动编写数据数组（如 y = [1.1, 1.2, 1.3...]）来伪造过程。
第三定律：数值诚实性 (Numerical Honesty)
强制要求：必须尊重数值计算的局限性。如果步长过大导致刚性方程发散（NaN/Infinity），必须暴露该错误，并提示用户修改求解器或步长。
绝对禁止：
禁止使用 clamp、min/max 或 if x > limit: x = limit 等逻辑进行人为截断（除非物理系统本身存在硬限位，如机械挡块）。
禁止使用 try...except 掩盖溢出错误。
第四定律：零魔术数字 (Zero Magic Numbers)
强制要求：代码中的每一个数字必须有明确的来源定义。
执行标准：
所有物理常数（如 $g, \pi, k_B$）必须提取为全局大写常量。
所有模型系数（如阻尼比、摩擦系数）必须在配置区定义。
禁止在计算公式中直接出现裸露的数字（如 0.5, 1.2），必须解释其含义（如 0.5 * mass）。
第五定律：守恒律验证 (Conservation Verification)
强制要求：在封闭系统仿真中，必须编写代码计算并验证守恒量（总能量、总动量、角动量等）。
判据：一个合格的仿真模型，其总能量随时间的导数应接近于零（或符合耗散预期）。代码必须输出这一指标以自证清白。
2. 代码架构与工程规范 (Architecture Standards)

科研代码必须遵循严格的 I-P-S-V 模块化结构，禁止面条式代码。

2.1 [I] Initialization - 参数空间与配置
必须使用 dataclass 或字典将所有系统参数集中管理。
量纲标注：每一个参数的定义行，必须在注释中注明国际单位制（SI Units）。
来源标注：对于特定常数，建议注释引用来源（如 "Ref: CODATA 2018"）。
2.2 [P] Physics Engine - 核心微分方程
物理核心必须封装为纯函数 (Pure Function)。
文档要求：函数的 Docstring 必须包含对应的 LaTeX 数学公式。
输入/输出：输入通常为 (t, state)，输出为 (d_state/dt)。严禁在物理计算函数中包含绘图或打印语句。
2.3 [S] Solver - 数值积分器
必须显式定义时间演化过程。
优先方案：使用成熟的科学计算库（如 scipy.integrate.solve_ivp）以保证精度。
备选方案：如果手写积分器（如 Runge-Kutta 4, Verlet, Euler），必须在注释中写明迭代公式，并进行截断误差分析。
稳定性检查：代码应包含检查 dt (时间步长) 是否满足 CFL 条件或稳定性判据的逻辑。
2.4 [V] Visualization - 科学可视化
原始数据：绘图必须基于 Solver 的原始输出。
坐标轴规范：所有图表必须包含：
图表标题 (Title)
X轴标签与单位 (X Label + Units)
Y轴标签与单位 (Y Label + Units)
图例 (Legend，如果有多条曲线)
网格 (Grid，便于读数)
3. 变量命名与语义映射 (Variable Semantics)

为了消除数学符号与代码变量之间的歧义，必须遵守以下命名协议：

映射表 (Mapping Table)：在主程序的文档字符串中，必须建立 "数学符号 <-> 代码变量" 的对照表。
全称优先：除非是极通用的缩写（如 dt, v, g），否则应使用全称（如 Reynolds_number, kinetic_energy）。
禁止歧义：
严禁使用单字母 l (小写L) 作为变量，易与 1 混淆。
严禁使用 temp, tmp, val, data 等无意义名称。
数学概念	推荐命名规范	严禁使用
密度 ($\rho$)	rho 或 density	r, p
导数 ($\dot{x}$)	dx_dt, v, velocity	dx, diff
初始值 ($x_0$)	x_init, x0	start
估算值 ($\hat{y}$)	y_est, y_hat	y
4. 交互自检程序 (Self-Correction Procedure)

在生成任何代码块之前，AI 必须在思维链（Chain of Thought）中执行以下负面测试：

[Check Geometry vs Dynamics]: 我是在用数学函数直接画线（错误），还是在定义受力分析并积分（正确）？
[Check Units]: 我是否试图将“米”加到“秒”上？公式左右两边的量纲是否平衡？
[Check Fitting]: 我是否引入了 polyfit？如果是，立即删除。
[Check Hardcoding]: 所有的 0.5, 2.0 等系数是否都已解释来源或提取为常量？
[Check Verification]: 我是否编写了用于验证结果正确性（如能量守恒）的辅助代码？
5. 适用范围 (Scope of Application)

本协议适用于以下所有场景：

经典力学与动力学仿真
电磁场与电路仿真
流体力学与热力学建模
量子力学数值计算
控制理论与信号处理算法实现
任何需要严格数学证明的代码任务

终止条件：只有当用户明确声明“我只需要一个简单的演示动画，不需要准确的物理模型”时，方可暂时豁免本协议，但必须在回复中明确标注“此为演示模型，非严谨物理仿真”。

6. 数值积分实现示例 (Numerical Integration Examples)
6.1 使用 scipy.integrate.solve_ivp

solve_ivp 是 SciPy 推荐的 ODE 求解器，支持多种积分方法。

from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 示例 1: 一阶常微分方程 dy/dt = -2y + t
# ============================================================
def first_order_ode(t, y):
    """
    一阶 ODE: dy/dt = -2*y + t
    
    参数:
        t: 时间 [s]
        y: 状态变量 [无量纲]
    返回:
        dy/dt: 状态变量的时间导数
    """
    return -2 * y + t

# 初始条件和时间跨度
y0 = [1.0]           # y(0) = 1
t_span = (0, 5)      # t ∈ [0, 5] s
t_eval = np.linspace(0, 5, 100)  # 输出时间点

# 求解
sol = solve_ivp(first_order_ode, t_span, y0, t_eval=t_eval, method='RK45')

print(f"求解状态: {sol.message}")
print(f"时间点数: {len(sol.t)}")
print(f"终值 y(5): {sol.y[0, -1]:.6f}")

6.2 二阶 ODE 转换为一阶系统
# ============================================================
# 示例 2: 简谐振子 d²x/dt² + ω²x = 0
# 转换为一阶系统: dx/dt = v, dv/dt = -ω²x
# ============================================================
OMEGA = 2.0  # 角频率 [rad/s]

def harmonic_oscillator(t, state):
    """
    简谐振子的状态方程
    
    数学形式:
        dx/dt = v
        dv/dt = -ω² * x
    
    参数:
        t: 时间 [s]
        state: [x, v] 位置 [m] 和速度 [m/s]
    返回:
        [dx/dt, dv/dt]: 状态导数
    """
    x, v = state
    dxdt = v
    dvdt = -OMEGA**2 * x
    return [dxdt, dvdt]

# 初始条件: x(0) = 1 m, v(0) = 0 m/s
state0 = [1.0, 0.0]
t_span = (0, 10)

# 使用 dense_output 获取连续解
sol = solve_ivp(harmonic_oscillator, t_span, state0, 
                dense_output=True, method='RK45')

# 在任意时间点求值
t = np.linspace(0, 10, 500)
z = sol.sol(t)  # z[0] = x(t), z[1] = v(t)

# 能量守恒验证
kinetic_energy = 0.5 * z[1]**2
potential_energy = 0.5 * OMEGA**2 * z[0]**2
total_energy = kinetic_energy + potential_energy
energy_drift = (total_energy - total_energy[0]) / total_energy[0] * 100

print(f"能量漂移: {np.max(np.abs(energy_drift)):.6f}%")

6.3 事件检测 (Event Detection)
# ============================================================
# 示例 3: 自由落体与地面碰撞检测
# ============================================================
G = 9.81  # 重力加速度 [m/s²]

def free_fall(t, state):
    """
    自由落体运动方程
    
    数学形式:
        dy/dt = v
        dv/dt = -g
    
    参数:
        t: 时间 [s]
        state: [y, v] 高度 [m] 和速度 [m/s]
    """
    y, v = state
    return [v, -G]

def hit_ground(t, state):
    """事件函数: 检测物体落地 (y = 0)"""
    return state[0]  # 当 y = 0 时触发

# 事件属性设置
hit_ground.terminal = True   # 触发时终止积分
hit_ground.direction = -1    # 仅检测 y 从正变负

# 初始条件: 高度 10m, 初速度 0
state0 = [10.0, 0.0]
t_span = (0, 10)

sol = solve_ivp(free_fall, t_span, state0, events=hit_ground, dense_output=True)

if sol.t_events[0].size > 0:
    t_impact = sol.t_events[0][0]
    v_impact = sol.y_events[0][0][1]
    print(f"落地时间: {t_impact:.4f} s")
    print(f"落地速度: {v_impact:.4f} m/s")
    print(f"理论落地时间: {np.sqrt(2*10/G):.4f} s")

6.4 刚性方程求解
# ============================================================
# 示例 4: 刚性方程 - 使用 BDF 或 Radau 方法
# ============================================================
def stiff_system(t, y):
    """
    刚性系统示例: 化学反应动力学
    
    dy1/dt = -1000*y1 + y2
    dy2/dt = 999*y1 - 2*y2
    """
    return [-1000*y[0] + y[1], 999*y[0] - 2*y[1]]

y0 = [1.0, 0.0]
t_span = (0, 1)
t_eval = np.linspace(0, 1, 1000)

# 刚性方程应使用隐式方法
sol_bdf = solve_ivp(stiff_system, t_span, y0, method='BDF', t_eval=t_eval)
sol_radau = solve_ivp(stiff_system, t_span, y0, method='Radau', t_eval=t_eval)

print(f"BDF 方法函数求值次数: {sol_bdf.nfev}")
print(f"Radau 方法函数求值次数: {sol_radau.nfev}")

6.5 求解器选择指南
方法	类型	适用场景	精度阶
RK45	显式 Runge-Kutta	非刚性问题（默认）	5(4)
RK23	显式 Runge-Kutta	非刚性、低精度需求	3(2)
DOP853	显式 Runge-Kutta	高精度非刚性问题	8
BDF	隐式多步法	刚性问题	1-5
Radau	隐式 Runge-Kutta	刚性问题、高精度	5
LSODA	自动切换	自动检测刚性	自适应
7. 相关资源
SciPy ODE 文档: https://docs.scipy.org/doc/scipy/reference/integrate.html
NumPy 文档: https://numpy.org/doc/stable/
Matplotlib 可视化: https://matplotlib.org/stable/
Weekly Installs
8
Repository
1837620622/supe…t-skills
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykPass