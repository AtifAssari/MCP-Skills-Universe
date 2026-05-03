---
title: rust-ebpf
url: https://skills.sh/huiali/rust-skills/rust-ebpf
---

# rust-ebpf

skills/huiali/rust-skills/rust-ebpf
rust-ebpf
Installation
$ npx skills add https://github.com/huiali/rust-skills --skill rust-ebpf
SKILL.md
eBPF vs 内核模块
特性	eBPF	内核模块
安全验证	编译时验证	需要手动审查
稳定性	稳定的 API	API 可能变化
性能	即时 JIT	高但有风险
崩溃风险	有限	可能崩溃内核
语言支持	C, Rust	C, Rust
Aya 库
// 使用 aya 创建 eBPF 程序
use aya::{maps::Map, programs::Xdp, Bpf};
use aya::maps::ArrayMap;
use std::sync::atomic::{AtomicU64, Ordering};

static PACKET_COUNT: AtomicU64 = AtomicU64::new(0);

#[repr(C)]
struct PacketStat {
    rx_packets: u64,
    tx_packets: u64,
}

#[panic_handler]
fn panic(_info: &std::panic::PanicInfo) -> ! {
    unsafe { core::hint::unreachable_unchecked() }
}

eBPF Map
// eBPF 共享数据映射
use aya::maps::HashMap;
use aya::util::online_cpus;

// 哈希映射
let mut hash_map = HashMap::try_from(
    (prog.fd().as_ref(), "packet_counts")
)?;

for cpu in online_cpus()? {
    hash_map.insert(cpu as u32, 0u64, 0)?;
}

// 数组映射
use aya::maps::Array;
let mut array = Array::try_from(
    (prog.fd().as_ref(), "config")
)?;

array.insert(0, 64u32, 0)?; // 批量大小

// PERCPU 映射 - 每 CPU 计数器
use aya::maps::PerCpuHashMap;
let mut per_cpu = PerCpuHashMap::try_from(
    (prog.fd().as_ref(), "per_cpu_stats")
)?;

for cpu in online_cpus()? {
    per_cpu.insert(cpu as u32, &0u64, 0)?;
}

XDP 程序
// XDP (Express Data Path) 程序
use aya::programs::XdpContext;
use aya_bpf::helpers::bpf_redirect;
use aya_bpf::macros::xdp;
use aya_bpf::programs::XdpProgram;

#[xdp]
pub fn xdp_packet_counter(ctx: XdpContext) -> u32 {
    let _ = ctx;
    
    // 计数
    PACKET_COUNT.fetch_add(1, Ordering::SeqCst);
    
    // 返回原始接口
    bpf_redirect(ctx.ifindex(), 0)
}

Tracepoint
// 跟踪点程序
use aya_bpf::macros::tracepoint;
use aya_bpf::programs::TracepointContext;

#[tracepoint(name = "sys_enter_open")]
pub fn trace_sys_enter_open(ctx: TracepointContext) -> u32 {
    let _ = ctx;
    0
}

kprobe/kretprobe
// 内核探针
use aya_bpf::macros::{kprobe, kretprobe};
use aya_bpf::programs::KprobeContext;

#[kprobe(name = "tcp_v4_connect", fn_name = "tcp_v4_connect_enter")]
pub fn tcp_v4_connect_enter(_ctx: KprobeContext) -> u32 {
    0
}

#[kretprobe(name = "tcp_v4_connect", fn_name = "tcp_v4_connect_exit")]
pub fn tcp_v4_connect_exit(_ctx: KprobeContext) -> u32 {
    0
}

用户态加载器
// 完整的 eBPF 加载器
use aya::Bpf;
use aya::maps::HashMap;
use std::net::Ipv4Addr;

#[tokio::main]
async fn main() -> Result<(), anyhow::Error> {
    // 加载 eBPF 程序
    let mut bpf = Bpf::load("ebpf.o")?;
    
    // 获取程序
    let program: &mut Xdp = bpf.program_mut("xdp_packet_counter")
        .unwrap()
        .try_into()?;
    program.load()?;
    program.attach("eth0", XdpFlags::default())?;
    
    // 创建映射
    let mut blocked_ips: HashMap<_, Ipv4Addr, u8> = HashMap::try_from(
        (bpf.map("blocked_ips")?.fd().as_ref(), "blocked_ips")
    )?;
    
    blocked_ips.insert(Ipv4Addr::new(1, 2, 3, 4), 1, 0)?;
    
    // 持续监控
    loop {
        tokio::time::sleep(tokio::time::Duration::from_secs(1)).await;
        // 读取统计数据
    }
}

Tail Call
// 尾调用 - 链式程序调用

// 程序 1
#[xdp(name = "packet_parser")]
pub fn packet_parser(ctx: XdpContext) -> u32 {
    let _ = ctx;
    // 解析包头，决定下一个程序
    aya_bpf::helpers::bpf_tail_call(ctx, &JUMP_TABLE, 0)
}

// 程序 2
#[xdp(name = "packet_filter")]
pub fn packet_filter(ctx: XdpContext) -> u32 {
    let _ = ctx;
    aya_bpf::programs::XdpAction::Pass.as_u32()
}

// 用户态设置
let mut jump_table: ProgramArray = ProgramArray::try_from(
    (bpf.map("jump_table")?.fd().as_ref(), "jump_table")
)?;

jump_table.set(0, bpf.program("packet_filter").unwrap().fd(), 0)?;

性能优化
优化点	方法
Map 访问	批量读取，减少系统调用
尾调用	控制链长度，避免过多跳转
数据结构	使用数组而非哈希表
锁竞争	使用 PerCPU map
与其他技能关联
rust-ebpf
    │
    ├─► rust-embedded → no_std, 内核接口
    ├─► rust-performance → 性能分析
    └─► rust-unsafe → 底层内存操作

Weekly Installs
11
Repository
huiali/rust-skills
GitHub Stars
29
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn