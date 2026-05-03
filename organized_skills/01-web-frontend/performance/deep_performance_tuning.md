---
rating: ⭐⭐⭐
title: deep performance tuning
url: https://skills.sh/fwrite0920/android-skills/deep-performance-tuning
---

# deep performance tuning

skills/fwrite0920/android-skills/Deep Performance Tuning
Deep Performance Tuning
Installation
$ npx skills add https://github.com/fwrite0920/android-skills --skill 'Deep Performance Tuning'
SKILL.md
Deep Performance Tuning (深度性能优化)
Instructions
仅在有量测数据或明确瓶颈时使用
先填写 Required Inputs（基线、设备、阈值）并冻结
依照下方章节顺序套用
一次只施作一种优化并验证效果
完成后对照 Quick Checklist
When to Use
Scenario D：性能问题排查
Scenario E：发布前性能验证
Example Prompts
"请参考 App Startup Optimization，创建 Macrobenchmark 测量"
"用 Memory Analysis 章节，规划内存分析流程"
"请依照 R8/Proguard Optimization，检查规则是否完整"
Workflow
先确认 Required Inputs（量测设备、指标阈值、回归标准）
创建量测基准（Startup/Memory/UI）
逐一套用对应优化手段（一次一项）
执行 Performance Gate 并记录前后对比
用 Quick Checklist 验收
Practical Notes (2026)
Baseline Profile + Macrobenchmark 作为默认流程
每次只做一项优化并量测差异
性能门槛要进 CI Gate
量测环境必须固定（机型/API/温度状态）避免伪回归
无数据不优化，先采集再改动
Minimal Template
目标: 
量测基准: 
量测设备/环境:
性能阈值:
优化范围: 
回归指标: 
验收: Quick Checklist

Required Inputs (执行前输入)
量测设备（机型/API/系统版本）
性能阈值（startup/jank/memory/apk size）
测试场景（冷启动、列表滚动、关键交易）
回归标准（允许波动范围）
责任人（性能优化 owner）
Deliverables (完成后交付物)
Benchmark 配置与基线数据
优化变更 与前后指标对比
CI performance gate（阻挡规则）
回归报告（失败原因与处置）
Performance Gate (验收门槛)
./gradlew :benchmark:connectedBenchmarkAndroidTest
./gradlew test


需要在 PR 中附上优化前后数据与采样条件。

App Startup Optimization
Macrobenchmark 测量
@LargeTest
@RunWith(AndroidJUnit4::class)
class StartupBenchmark {
    
    @get:Rule
    val benchmarkRule = MacrobenchmarkRule()
    
    @Test
    fun startupCompilationNone() = startup(CompilationMode.None())
    
    @Test
    fun startupCompilationPartial() = startup(CompilationMode.Partial())
    
    private fun startup(compilationMode: CompilationMode) {
        benchmarkRule.measureRepeated(
            packageName = "com.example.app",
            metrics = listOf(StartupTimingMetric()),
            compilationMode = compilationMode,
            iterations = 5,
            startupMode = StartupMode.COLD
        ) {
            pressHome()
            startActivityAndWait()
        }
    }
}

Baseline Profiles
// 生成 Baseline Profile
@RunWith(AndroidJUnit4::class)
class BaselineProfileGenerator {
    
    @get:Rule
    val rule = BaselineProfileRule()
    
    @Test
    fun generate() {
        rule.collect("com.example.app") {
            pressHome()
            startActivityAndWait()
            
            // 关键路径
            device.findObject(By.text("Login")).click()
            device.wait(Until.hasObject(By.text("Home")), 5000)
        }
    }
}

Application onCreate 优化
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        
        // ❌ 同步初始化 (Block UI)
        // Firebase.initialize(this)
        // Timber.plant(DebugTree())
        
        // ✅ 延迟初始化
        AppInitializer.getInstance(this)
            .initializeComponent(FirebaseInitializer::class.java)
        
        // ✅ 背景初始化
        ProcessLifecycleOwner.get().lifecycle.addObserver(
            object : DefaultLifecycleObserver {
                override fun onCreate(owner: LifecycleOwner) {
                    owner.lifecycleScope.launch(Dispatchers.Default) {
                        // 非关键初始化
                    }
                }
            }
        )
    }
}

Memory Analysis
Heap Dump 分析
# 取得 Heap Dump
adb shell am dumpheap com.example.app /data/local/tmp/heap.hprof
adb pull /data/local/tmp/heap.hprof

# 使用 Android Studio Profiler 分析
# 或使用 MAT (Memory Analyzer Tool)

LeakCanary 设置
// build.gradle.kts
debugImplementation("com.squareup.leakcanary:leakcanary-android:2.12")

// 自定义报告
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        LeakCanary.config = LeakCanary.config.copy(
            retainedVisibleThreshold = 3,
            objectInspectors = AndroidObjectInspectors.appDefaults
        )
    }
}

Bitmap 内存管理
// 使用 Coil 自动管理
AsyncImage(
    model = ImageRequest.Builder(LocalContext.current)
        .data(imageUrl)
        .size(Size.ORIGINAL)  // 根据需求调整
        .memoryCachePolicy(CachePolicy.ENABLED)
        .build(),
    contentDescription = null
)

R8/Proguard Optimization
自定义规则
# 保留 Serializable
-keepclassmembers class * implements java.io.Serializable {
    static final long serialVersionUID;
    private static final java.io.ObjectStreamField[] serialPersistentFields;
    !static !transient <fields>;
    private void writeObject(java.io.ObjectOutputStream);
    private void readObject(java.io.ObjectInputStream);
}

# 保留 Retrofit Interface
-keep,allowobfuscation interface * {
    @retrofit2.http.* <methods>;
}

# 保留 Compose stability
-keep class * {
    @androidx.compose.runtime.Stable *;
    @androidx.compose.runtime.Immutable *;
}

APK Size 分析
# 使用 bundletool
bundletool build-apks --bundle=app.aab --output=app.apks
bundletool get-size total --apks=app.apks

# Android Studio: Build > Analyze APK

UI Performance
JankStats
class MainActivity : ComponentActivity() {
    private lateinit var jankStats: JankStats
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        jankStats = JankStats.createAndTrack(window) { frameData ->
            if (frameData.isJank) {
                Log.w("Jank", "Frame took ${frameData.frameDurationUiNanos / 1_000_000}ms")
            }
        }
    }
}

Compose Recomposition Tracking
// 打开 Composition Tracking
@Composable
fun DebugComposable() {
    SideEffect {
        Log.d("Recomposition", "DebugComposable recomposed")
    }
}

// 使用 Layout Inspector 检查 recomposition count

Quick Checklist
 Required Inputs 已填写并冻结（设备/阈值/回归标准）
 Startup: Baseline Profiles 生成
 Startup: Application onCreate 延迟初始化
 Memory: LeakCanary 无泄漏
 APK: R8 规则完善
 UI: JankStats 无严重掉帧
 Performance Gate 已执行并记录结果
Weekly Installs
–
Repository
fwrite0920/andr…d-skills
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass