---
title: crash monitoring
url: https://skills.sh/fwrite0920/android-skills/crash-monitoring
---

# crash monitoring

skills/fwrite0920/android-skills/Crash Monitoring
Crash Monitoring
Installation
$ npx skills add https://github.com/fwrite0920/android-skills --skill 'Crash Monitoring'
SKILL.md
Crash Monitoring (当机监控)
Instructions
确认需求属于当机/ANR/日志监控
先填写 Required Inputs（告警阈值、Owner、事件字段）
依照下方章节顺序套用
一次只调整一种监控或警报设置
完成后对照 Quick Checklist
When to Use
Scenario D：性能问题排查
Scenario E：发布前监控准备
Example Prompts
"请依照 Firebase Crashlytics Setup，完成 Crashlytics 集成"
"用 ANR Analysis 章节加入 StrictMode 与 ANR Watchdog"
"请依 Structured Logging 章节统一日志格式"
Workflow
先确认 Required Inputs（阈值、渠道、负责人）
完成 Crashlytics 基本设置与 Custom Keys
加入 ANR 与 Structured Logging
配置 Dashboard & Alerting 并演练告警路由
执行 Crash Gate 验收并记录结果
Practical Notes (2026)
Release 前先确立 Crash/ANR 的告警门槛
重要流程必有结构化事件与关键键值
Non-Fatal 记录以高价值事件为主
P0 崩溃告警必须有值班 owner 与升级路径
版本维度（build/version/flavor）必须写入 crash 上下文
监控变更与业务功能变更分开提交，便于回溯
Minimal Template
目标: 
监控范围: 
Owner/Oncall:
告警渠道:
告警门槛: 
事件字段: 
验收: Quick Checklist

Required Inputs (执行前输入)
Crash-free/ANR 阈值（P0/P1）
告警渠道（PagerDuty/Slack/Email）
Owner & Oncall（值班与备援）
关键流程字段（user tier、feature flag、build version）
发布范围（prod/staging、region、flavor）
Deliverables (完成后交付物)
Crashlytics 集成与环境开关策略
Custom Keys 字段规范
ANR 监测策略（StrictMode + Watchdog）
结构化日志策略（Timber tree 与级别规范）
Dashboard + 告警规则（含路由演练记录）
Crash Gate 验收记录
Crash Gate (验收门槛)
# 1) 基础质量
./gradlew lint test assemble

# 2) 设备测试（按项目替换任务名）
./gradlew :app:connectedDebugAndroidTest

# 3) 发布前核查
# - Crashlytics dashboard 最近 24h 有数据
# - Velocity Alert 路由已演练（至少一次）

Firebase Crashlytics Setup
基本设置
// build.gradle.kts (app)
plugins {
    id("com.google.firebase.crashlytics")
}

dependencies {
    implementation(platform("com.google.firebase:firebase-bom:<project-verified-version>"))
    implementation("com.google.firebase:firebase-crashlytics-ktx")
    implementation("com.google.firebase:firebase-analytics-ktx")
}

Custom Keys
// 记录用户状态
Firebase.crashlytics.apply {
    setUserId("user_123")
    setCustomKey("subscription_tier", "premium")
    setCustomKey("feature_flags", "new_checkout:true")
}

Non-Fatal Logging
// 记录非致命错误
try {
    riskyOperation()
} catch (e: Exception) {
    Firebase.crashlytics.recordException(e)
    // 继续正常流程
}

// 带上下文的 Non-Fatal
Firebase.crashlytics.log("Starting payment flow")
try {
    processPayment()
} catch (e: PaymentException) {
    Firebase.crashlytics.apply {
        setCustomKey("payment_amount", amount)
        setCustomKey("payment_method", method)
        recordException(e)
    }
}

ANR Analysis
StrictMode (Debug)
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        
        if (BuildConfig.DEBUG) {
            StrictMode.setThreadPolicy(
                StrictMode.ThreadPolicy.Builder()
                    .detectDiskReads()
                    .detectDiskWrites()
                    .detectNetwork()
                    .penaltyLog()
                    .penaltyDeath()  // 强制 Crash
                    .build()
            )
            
            StrictMode.setVmPolicy(
                StrictMode.VmPolicy.Builder()
                    .detectLeakedClosableObjects()
                    .detectActivityLeaks()
                    .penaltyLog()
                    .build()
            )
        }
    }
}

ANR Watchdog
class ANRWatchDog(private val timeoutMs: Long = 5000) : Thread() {

    private val mainHandler = Handler(Looper.getMainLooper())
    @Volatile private var heartbeat = 0L
    @Volatile private var reported = false

    override fun run() {
        while (!isInterrupted) {
            val currentHeartbeat = heartbeat
            mainHandler.post {
                heartbeat++
                reported = false // 主线程恢复后，允许下一次 ANR 再上报
            }

            try {
                Thread.sleep(timeoutMs)
            } catch (e: InterruptedException) {
                interrupt()
                return
            }

            if (currentHeartbeat == heartbeat && !reported) {
                reported = true
                val stackTraces = Looper.getMainLooper().thread.stackTrace
                Firebase.crashlytics.log("ANR detected")
                Firebase.crashlytics.recordException(ANRException(stackTraces))
            }
        }
    }
}

Structured Logging
Timber Setup
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        
        if (BuildConfig.DEBUG) {
            Timber.plant(Timber.DebugTree())
        } else {
            Timber.plant(CrashlyticsTree())
        }
    }
}

class CrashlyticsTree : Timber.Tree() {
    override fun log(priority: Int, tag: String?, message: String, t: Throwable?) {
        if (priority >= Log.INFO) {
            Firebase.crashlytics.log("[$tag] $message")
        }
        
        t?.let {
            Firebase.crashlytics.recordException(it)
        }
    }
}

Log Levels 使用规范
Level	使用场景	例子
VERBOSE	Debug 专用细节	API Response body
DEBUG	开发调试	ViewModel state changes
INFO	重要里程碑	User login success
WARN	潜在问题	Retry attempt
ERROR	可恢复错误	Network timeout
Dashboard & Alerting
Crashlytics Velocity Alerts
Firebase Console > Crashlytics > Settings
- Enable velocity alerts
- Set threshold: 1% of sessions

Custom Metrics
// 追踪关键指标
Firebase.analytics.logEvent("checkout_started") {
    param("cart_value", cartValue)
}

Firebase.analytics.logEvent("checkout_completed") {
    param("payment_method", method)
    param("time_to_complete_ms", duration)
}

Quick Checklist
 Required Inputs 已填写并冻结（阈值/渠道/owner）
 Crashlytics 集成完成
 Custom Keys 设置 (User tier, Feature flags)
 Non-Fatal 记录重要异常
 StrictMode 在 Debug 激活
 Timber 统一日志
 Velocity Alerts 设置
 每个 P0 告警有 owner 与升级路径
 Crash Gate 已执行并记录结果
Weekly Installs
–
Repository
fwrite0920/andr…d-skills
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass