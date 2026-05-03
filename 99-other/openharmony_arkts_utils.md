---
title: openharmony-arkts-utils
url: https://skills.sh/mengfei0053/skills/openharmony-arkts-utils
---

# openharmony-arkts-utils

skills/mengfei0053/skills/openharmony-arkts-utils
openharmony-arkts-utils
Installation
$ npx skills add https://github.com/mengfei0053/skills --skill openharmony-arkts-utils
SKILL.md
OpenHarmony ArkTS 工具库快速参考

OpenHarmony ArkTS工具库、并发和运行时特性的快速查找指南。

概述

ArkTS提供全面的工具库，包括异步并发、多线程（TaskPool/Worker）、数据结构（XML/Buffer/JSON/容器）、运行时特性和构建工具。

官方文档： https://docs.openharmony.cn/

📁 详细 API 参考文件

本技能文件提供概念指南和常用示例。详细 API 签名和完整示例请参考 refs/ 文件夹：

文件	内容	适用场景
refs/taskpool.md	TaskPool 完整 API	Task、TaskGroup、优先级、延时执行
refs/worker.md	Worker 完整 API	ThreadWorker、消息通信、生命周期
refs/collections.md	共享容器 API	collections.Array/Map/Set (跨线程)
refs/utils.md	ArkTSUtils API	AsyncLock、ASON、Sendable工具
refs/buffer.md	Buffer API	二进制数据处理、编码转换
refs/xml.md	XML API	XmlSerializer、XmlPullParser
refs/containers.md	线性/非线性容器 API	ArrayList、HashMap 等普通容器
refs/error-codes.md	错误码速查表	10200001-10200301 错误处理
异步并发 (Promise & async/await)
Promise

基本用法：

const promise: Promise<number> = new Promise((resolve: Function, reject: Function) => {
  setTimeout(() => {
    const randomNumber: number = Math.random();
    if (randomNumber > 0.5) {
      resolve(randomNumber);
    } else {
      reject(new Error('Random number is too small'));
    }
  }, 1000);
})

// 处理结果
promise.then((result: number) => {
  console.info(`The number for success is ${result}`);
}).catch((error: Error) => {
  console.error(error.message);
}).finally(() => {
  console.info('finally complete');
})


使用场景： I/O操作（网络、文件）、定时器、轻量级非阻塞任务

说明： 当Promise被reject且未通过catch方法处理时，会触发globalUnhandledRejectionDetected事件。可使用errorManager.on('globalUnhandledRejectionDetected')接口监听该事件，以全局捕获未处理的Promise reject。

async/await
async function myAsyncFunction(): Promise<string> {
  try {
    const result: string = await new Promise((resolve: Function) => {
      resolve('Hello, world!');
    });
    console.info(result); // 输出： Hello, world!
    return result;
  } catch (e) {
    console.error(`Get exception: ${e}`);
  }
}

myAsyncFunction();


优势： 以同步方式编写异步代码，通过try-catch实现更好的错误处理

说明： 等待异步操作时，需将操作包在async函数中，并搭配await使用，且await关键字只在async函数内有效。

多线程 - TaskPool

TaskPool自动管理线程池，无需生命周期管理。系统默认启动一个任务工作线程，任务多时会自动扩容。工作线程数量上限由设备的物理核数决定。

基本TaskPool使用
import { taskpool } from '@kit.ArkTS';

@Concurrent
function add(num1: number, num2: number): number {
  return num1 + num2;
}

async function concurrentFunc(): Promise<void> {
  const task: taskpool.Task = new taskpool.Task(add, 1, 2);
  console.info(`taskpool res is: ${await taskpool.execute(task)}`); // 输出结果：taskpool res is: 3
}

TaskGroup批量执行
@Concurrent
function processData(data: number): number {
  return data * 2;
}

function executeTaskGroup() {
  const group = new taskpool.TaskGroup();
  group.addTask(processData, 10);
  group.addTask(processData, 20);
  group.addTask(processData, 30);

  taskpool.execute(group).then((results: number[]) => {
    console.info(`Group results: ${results}`); // [20, 40, 60]
  });
}

任务配置
const task = new taskpool.Task(computeTask, 1000);

// 设置优先级
task.priority = taskpool.Priority.HIGH; // HIGH, MEDIUM, LOW, IDLE

// 设置ArrayBuffer转移列表（零拷贝，移动所有权）
task.setTransferList([buffer]);

// 设置ArrayBuffer拷贝列表（复制数据）
task.setCloneList([buffer]);

// 指定优先级执行
taskpool.execute(task, taskpool.Priority.HIGH);

异步队列控制并发度
import { taskpool } from '@kit.ArkTS';

// 创建异步队列：名称、并发数、队列大小
const asyncRunner = new taskpool.AsyncRunner("camera", 5, 5);

@Concurrent
function collectFrame(): void {
  // 采集帧数据
}

for (let i = 0; i < 20; i++) {
  const task = new taskpool.Task(collectFrame);
  asyncRunner.execute(task);
}

任务取消
@Sendable
class TaskManager {
  taskId: number = 0;

  setTaskId(id: number) { this.taskId = id; }
  getTaskId(): number { return this.taskId; }
}

@Concurrent
function cancelTask(manager: TaskManager) {
  taskpool.cancel(manager.getTaskId());
}

const task = new taskpool.Task(delayedTask);
taskpool.executeDelayed(2000, task);

const manager = new TaskManager();
manager.setTaskId(task.taskId);
taskpool.execute(cancelTask, manager);

延时执行任务
@Concurrent
function delayedTask(): void {
  console.info('Delayed task executed');
}

// 延时2秒执行
const task = new taskpool.Task(delayedTask);
taskpool.executeDelayed(2000, task);

@Concurrent装饰器规范

| 装饰器参数 | 无 | | 装饰的函数类型 | async函数或普通函数。禁止generator、箭头函数、类方法。不支持类成员函数或者匿名函数 | | 装饰的函数内的变量类型 | 允许使用局部变量、入参和通过import引入的变量，禁止使用闭包变量 | | 使用场景限制 | 仅支持在Stage模型的工程中使用，仅支持在.ets文件中使用 |

注意： @Concurrent标记的函数不能访问闭包，因此函数内部不能调用当前文件的其他函数。

TaskPool vs Worker 对比
特性	TaskPool	Worker
使用场景	短期独立任务	长期后台任务
线程管理	自动	手动（生命周期管理）
任务时长	< 3分钟（不含异步操作耗时）	无限制
线程分配	系统管理	显式指定
优先级控制	支持	API 18+支持
任务取消	支持	不支持
线程复用	支持	不支持
任务延时执行	支持	不支持
任务依赖关系	支持	不支持
串行队列	支持	不支持
任务组	支持	不支持
周期任务	支持	不支持
异步队列	支持	不支持
TaskPool约束和注意事项
任务必须使用@Concurrent装饰器
任务执行时长不能超过3分钟（不包含Promise或async/await异步调用的耗时）
序列化传输的数据量限制为16MB
参数必须满足序列化支持的类型，不支持@State/@Prop/@Link等装饰器修饰的复杂类型
ArrayBuffer参数在TaskPool中默认转移，需多次使用时通过setCloneList设置拷贝
工作线程只能使用线程安全的库，不能使用UI相关的非线程安全库
不支持在TaskPool工作线程中使用AppStorage
Promise不支持跨线程传递
Priority的IDLE优先级用于标记需要在后台运行的耗时任务，只在所有线程都空闲时触发执行

📖 详细 API 参考: refs/taskpool.md — Task、TaskGroup、优先级、延时执行的完整 API 签名和示例

多线程 - Worker

Worker提供专用的长期后台线程。同个进程下，最多支持同时开启64个Worker线程，实际数量由进程内存决定。

基本Worker使用
// 主线程
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker('entry/ets/workers/Worker.ets');

// 发送消息
workerInstance.postMessage('hello world');

// 接收消息
workerInstance.onmessage = (event: MessageEvents) => {
  console.info(`Received: ${event.data}`);
};

// 捕获全局异常（推荐）
workerInstance.onAllErrors = (error: ErrorEvent) => {
  console.error(`Worker error: ${error.message}`);
  // 异常后Worker线程继续运行
};

// 销毁Worker
workerInstance.terminate();


Worker线程 (Worker.ets):

import { worker } from '@kit.ArkTS';

const workerPort = worker.workerPort;

workerPort.onmessage = (event: MessageEvents) => {
  const data = event.data;
  // 处理数据
  workerPort.postMessage({ result: 'done' });
};

Worker通信模式

即时消息传递：

// 主线程 → Worker
workerInstance.postMessage(message);

// Worker → 主线程
workerPort.postMessage(result);


同步调用：

// 在Worker中同步调用主线程方法
const result = workerPort.syncCall(method, params);

Worker生命周期管理
// 创建Worker
const workerInstance = new worker.ThreadWorker('entry/ets/workers/Worker.ets', {
  type: 'classic'  // 或 'module' 类型
});

// 监听退出事件
workerInstance.onexit = () => {
  console.info('Worker terminated');
  isTerminate = true;
};

// 销毁Worker
workerInstance.terminate();

// 等待Worker完全退出
while (!isTerminate) {
  await promiseCase();
}

Worker错误处理
// 推荐使用onAllErrors捕获所有异常
workerInstance.onAllErrors = (error: ErrorEvent) => {
  console.error(`Type: ${error.type}, Message: ${error.message}`);
  // 异常后Worker线程继续运行
};

// onerror仅捕获onmessage回调中的同步异常
workerInstance.onerror = (error: ErrorEvent) => {
  console.error(`Error: ${error.message}`);
  // 异常后Worker线程进入销毁流程
};

Worker vs TaskPool 选择

推荐使用TaskPool的场景：

运行时间不超过3分钟的独立任务
CPU密集型任务（图像处理、数据分析）
I/O密集型任务（文件读写、网络请求）
需要设置优先级的任务
需要频繁取消的任务
大量或调度点分散的任务

推荐使用Worker的场景：

运行时间超过3分钟的长时任务
有关联的一系列同步任务（使用同一句柄）
需要指定运行线程的任务

📖 详细 API 参考: refs/worker.md — ThreadWorker、消息通信、生命周期管理的完整 API

Sendable - 跨线程共享对象

Sendable启用安全的对象跨线程共享。Sendable对象分配在共享堆（SharedHeap）中，实现跨并发实例的内存共享。

基本@Sendable使用
@Sendable
class SendableTestClass {
  desc: string = "sendable: this is SendableTestClass ";
  num: number = 5;

  printName() {
    console.info("sendable: SendableTestClass desc is: " + this.desc);
  }

  getNum(): number {
    return this.num;
  }
}

// 可直接传递给TaskPool/Worker，无需拷贝
const data = new SendableTestClass();
taskpool.execute(task, data);

@Sendable函数使用
@Sendable
type SendableFuncType = () => void;

@Sendable
function TopLevelSendableFunction() {
  console.info("Top level sendable function");
}

@Sendable
class SendableTestClass {
  callback: SendableFuncType;

  constructor(func: SendableFuncType) {
    this.callback = func;
  }

  CallSendableFunc() {
    TopLevelSendableFunction();
  }
}

@Sendable装饰器规范

| 装饰器参数 | 无 | | 使用场景限制 | 仅支持在Stage模型的.ets文件中使用 | | 装饰的类继承关系限制 | Sendable class只能继承Sendable class，普通class不可继承Sendable class | | 装饰的对象内的属性类型限制 | 支持string、number、boolean、bigint、null、undefined、Sendable class、collections容器集、ArkTSUtils.locks.AsyncLock等。禁止使用闭包变量（顶层Sendable类和函数除外） | | 装饰的对象内的属性的其他限制 | 成员属性必须显式初始化，不能使用感叹号。不支持增加或删除属性，允许修改属性，修改前后类型必须一致 | | 适用场景 | 1. 在TaskPool或Worker中使用类方法或Sendable函数2. 传输对象数据量较大的场景（100KB数据效率提升约20倍，1M数据效率提升约100倍） |

Sendable支持的数据类型

基本数据类型：

boolean、number、string、bigint、null、undefined

容器类型（需显式引入@arkts.collections）：

collections.Array、collections.Map、collections.Set
collections.TypedArray（Int8Array、Uint8Array等）
collections.ArrayBuffer

并发工具类型（需显式引入@arkts.utils）：

ArkTSUtils.locks.AsyncLock
ArkTSUtils.locks.ConditionVariable
ArkTSUtils.SendableLruCache

复合类型：

标注了@Sendable装饰器的class
标注了@Sendable装饰器的function
继承了ISendable的interface
元素均为Sendable类型的union type

注意： JS内置对象在并发实例间传递时遵循结构化克隆算法，跨线程行为是拷贝传递。对象字面量和数组字面量也不是Sendable类型。

共享容器
import { collections, ArkTSUtils, taskpool } from '@kit.ArkTS';

// 共享Array
const arr = collections.Array.create<number>(100, 0);

// 共享Map
const map = new collections.Map<string, number>();
map.set('key1', 100);

// 配合异步锁使用（防止并发修改）
@Concurrent
async function add(arr: collections.Array<number>, lock: ArkTSUtils.locks.AsyncLock) {
  await lock.lockAsync(() => {
    arr[0]++;
  })
}


说明： ArkTS共享容器不是线程安全的，内部使用了fail-fast机制。在多线程场景下修改容器内属性时，需要使用ArkTS提供的异步锁机制保证安全访问。

📖 详细 API 参考: refs/collections.md — collections.Array/Map/Set 跨线程共享容器完整 API

异步锁 (AsyncLock)
import { ArkTSUtils, taskpool } from '@kit.ArkTS';

@Sendable
export class A {
  private count_: number = 0;
  lock_: ArkTSUtils.locks.AsyncLock = new ArkTSUtils.locks.AsyncLock();

  public getCount(): Promise<number> {
    return this.lock_.lockAsync(() => {
      return this.count_;
    })
  }

  public async increaseCount() {
    await this.lock_.lockAsync(() => {
      this.count_++;
    })
  }
}

@Concurrent
async function printCount(a: A) {
  a.increaseCount();
  console.info("InputModule: count is:" + await a.getCount());
}

条件变量 (ConditionVariable)
import { ArkTSUtils } from '@kit.ArkTS';

const conditionVariable: ArkTSUtils.locks.ConditionVariable = new ArkTSUtils.locks.ConditionVariable();

// 等待条件（无限等待）
await conditionVariable.wait();

// 等待条件（超时等待）
await conditionVariable.waitFor(timeout);

// 唤醒一个等待线程
conditionVariable.notifyOne();

// 唤醒所有等待线程
conditionVariable.notifyAll();

共享模块
// sharedModule.ets
"use shared"

@Sendable
class GlobalCounter {
  private count_: number = 0;
  lock_: ArkTSUtils.locks.AsyncLock = new ArkTSUtils.locks.AsyncLock();

  async increment(): Promise<number> {
    return this.lock_.lockAsync(() => {
      return ++this.count_;
    });
  }
}

export let globalCounter = new GlobalCounter();


共享模块约束：

共享模块只支持.ets文件
共享模块内不允许使用side-effects-import
共享模块导出的所有对象必须是可共享的Sendable类型
共享模块不支持re-export写法

📖 详细 API 参考: refs/utils.md — AsyncLock、ConditionVariable、ASON、LruCache 完整 API

容器库
ArkTS共享容器 (@arkts.collections)
容器	用途	特性
collections.Array	动态数组，引用传递，跨线程高效	支持push、pop、splice、forEach等
collections.Map	键值对集合，引用传递	支持set、get、has、delete等
collections.Set	值集合，引用传递	支持add、has、delete等
collections.TypedArray	类型化数组（Int8Array、Uint8Array等）	固定类型，高性能
collections.ArrayBuffer	数组缓冲区	支持slice、byteLength

注意： ArkTS共享容器采用引用传递方式跨线程传递，与原生容器相比效率更高。如果需要跨线程传输大量数据，建议使用ArkTS共享容器。

线性容器 (@arkts.collections)
容器	用途	复杂度
ArrayList	动态数组，频繁读取	O(1) 访问
Vector	动态数组，固定类型	O(1) 访问（已废弃，推荐ArrayList）
LinkedList	双向链表，频繁插入删除	O(1) 插入
Deque	双端队列，头尾操作	O(1) 头尾
List	单向链表，频繁插入删除	O(1) 插入
Queue	队列，先进先出	O(1) 入队/出队
Stack	栈，先进后出	O(1) push/pop

ArrayList示例：

import { collections } from '@kit.ArkTS';

const list = new collections.ArrayList<string>();
list.add('item1');
list.add('item2');
list.has('item1'); // true
list.remove(0);
const size = list.size;

非线性容器 (@arkts.collections)
容器	用途	顺序
HashMap	哈希映射，快速存取	无序
HashSet	哈希集合，唯一值	无序
TreeMap	有序映射，支持自定义排序	按键排序
TreeSet	有序集合，支持自定义排序	按值排序
LightWeightMap	轻量级映射，内存占用小	无序
LightWeightSet	轻量级集合，内存占用小	无序
PlainArray	轻量级数组，键为number类型	-

HashMap示例：

import { collections } from '@kit.ArkTS';

const map = new collections.HashMap<string, number>();
map.set('key1', 100);
map.set('key2', 200);
map.has('key1'); // true
const value = map.get('key1'); // 100

线性 vs 非线性容器
线性容器：按顺序访问，底层基于数组或链表实现。优化数据访问速度，适合频繁读取元素或顺序操作
非线性容器：快速查找，底层基于哈希或红黑树实现。支持快速查找，key/value类型符合ECMA标准

📖 详细 API 参考: refs/containers.md — ArrayList、HashMap、TreeMap 等普通容器完整 API

XML处理
XML生成
import { xml, util } from '@kit.ArkTS';

// 方式1：使用XmlSerializer（固定缓冲区）
let arrayBuffer: ArrayBuffer = new ArrayBuffer(2048);
let serializer: xml.XmlSerializer = new xml.XmlSerializer(arrayBuffer);

serializer.setDeclaration(); // 写入XML声明
serializer.startElement('bookstore');
serializer.startElement('book');
serializer.setAttributes('category', 'COOKING');
serializer.startElement('title');
serializer.setAttributes('lang', 'en');
serializer.setText('Everyday');
serializer.endElement();
serializer.startElement('author');
serializer.setText('Giana');
serializer.endElement();
serializer.endElement();
serializer.endElement();

// 方式2：使用XmlDynamicSerializer（动态扩容）
let DySerializer = new xml.XmlDynamicSerializer('utf-8');
DySerializer.setDeclaration();
DySerializer.startElement('bookstore');
// ... 添加元素
let arrayBuffer = DySerializer.getOutput();

// 解码输出
let uint8Array: Uint8Array = new Uint8Array(arrayBuffer);
let result: string = util.TextDecoder.create().decodeToString(uint8Array);
console.info(result);

XML解析
import { xml } from '@kit.ArkTS';

const xmlString = '<note><to>User</to><from>System</from></note>';

// 使用XmlPullParser解析
let parser = new xml.XmlPullParser(xmlString);
parser.parseXml({
  supportDoctype: true,
  ignoreNameSpace: true,
  tagValueCallbackFunction: (name, value) => {
    console.info(`Tag: ${name}, Value: ${value}`);
  }
});

XML转换
import { xml } from '@kit.ArkTS';

// 将XML转换为JavaScript对象
const jsonObj = xml.fastConvertToJSObject(xmlString, {
  trim: true,
  declarationKey: '_declaration',
  attributesKey: '_attributes'
});

// 转换结果示例：
// {
//   "_declaration": {"_attributes": {"version": "1.0", "encoding": "UTF-8"}},
//   "note": {
//     "_attributes": {"priority": "high"},
//     "to": "User",
//     "from": "System"
//   }
// }


📖 详细 API 参考: refs/xml.md — XmlSerializer、XmlPullParser、XML转换完整 API

Buffer和二进制
Buffer
import { buffer } from '@kit.ArkTS';

// 创建buffer
const buf = buffer.from('Hello World', 'utf-8');

// 写入
buf.writeUInt8(0, 65);

// 读取
const byte = buf.readUInt8(0);

// 转换
const str = buf.toString('utf-8');
const arrayBuffer = buf.buffer;

ArrayBuffer转移/拷贝

转移（零拷贝，移动所有权）：

task.setTransferList([arrayBuffer]);
// 转移后原始ArrayBuffer变为不可用


拷贝（复制数据）：

task.setCloneList([arrayBuffer]);
// 拷贝后原始ArrayBuffer仍可用


📖 详细 API 参考: refs/buffer.md — Buffer 创建、读写、编码转换完整 API

JSON工具
import { JSON } from '@kit.ArkTS';

// 解析（支持BigInt模式）
let numberText = '{"number": 10, "largeNumber": 112233445566778899}';

// 使用PARSE_AS_BIGINT模式解析大整数
let options: JSON.ParseOptions = {
  bigIntMode: JSON.BigIntMode.PARSE_AS_BIGINT,
}
let numberObj = JSON.parse(numberText, null, options) as Object;
console.info(typeof (numberObj as object)?.["largeNumber"]); // bigint

// 序列化（支持BigInt）
let bigIntObject = BigInt(112233445566778899n);
let result: string = JSON.stringify(bigIntObject);
console.info(result); // 112233445566778899

// 带格式的序列化
let obj = { name: "Tom", age: 20 };
let str = JSON.stringify(obj, null, 2);

// 检查属性
let hasProp = JSON.has(obj, "name"); // true

// 删除属性
JSON.remove(obj, "age");


JSON扩展库特性：

支持BigInt解析和序列化
循环引用检测
强参数校验
增强的错误处理（BusinessError）
额外方法（has/remove）
运行时特性
动态导入
// 常量动态导入
import('myhar').then((ns:ESObject) => {
  console.info(ns.add(3, 5));
});

// 异步处理
async function asyncDynamicImport() {
  let ns:ESObject = await import('myhar');
  console.info(ns.add(3, 5));
}

// 变量动态导入（需配置runtimeOnly）
let packageName = 'myhar';
import(packageName).then((ns:ESObject) => {
  console.info(ns.add(3, 5));
});


runtimeOnly配置（仅变量动态导入需要）：

// build-profile.json5
{
  "buildOption": {
    "arkOptions": {
      "runtimeOnly": {
        "packages": ["myhar"],  // 其他模块名
        "sources": ["./src/main/ets/utils/Calc.ets"]  // 本模块文件路径
      }
    }
  }
}


支持的动态导入场景：

本地工程模块（./、../开头的路径）
HSP/HAR模块名
远程HAR模块名
ohpm包名
@system.、@ohos.、@arkui-x.* API
libNativeLibrary.so
懒导入
// 基本语法（API 12+）
import lazy { x } from "mod";
import lazy { x as v } from "mod";
import lazy x from "mod";  // API 18+
import lazy { KitClass } from "@kit.SomeKit";  // API 18+


不支持的语法：

// 以下写法将引起编译报错
import lazy * as ns from "mod";
import lazy type { obj } from "./mod";


使用场景：

文件在冷启动阶段未被实际调用
减少冷启动时间，延迟执行到实际使用时

注意： 不建议盲目增加lazy，这会增加编译和运行时的识别开销。后续执行的加载是同步加载，可能阻塞任务执行。

原生模块加载

静态导入：

// 具名导入
import { add } from 'libentry.so';

// 默认导入
import entry from 'libentry.so';
entry.add(2, 3);

// 命名空间导入
import * as entry from 'libentry.so';
entry.add(2, 3);


动态导入：

import('libentry.so').then((ns:ESObject) => {
  ns.default.add(2, 3);
});

async function asyncDynamicImport() {
  let ns:ESObject = await import('libentry.so');
  ns.default.add(2, 3);
}

模块副作用优化

问题代码：

// Bad - 导入时立即执行
console.log("Module loaded!");
export const data = 1;

// Bad - 直接修改全局
globalThis.someGlobalVar = 100;

// Bad - 导入时修改AppStorage
AppStorage.setOrCreate("SomeAppStorageVar", 200);


优化方案：

// Good - 移除顶层代码
export const data = 1;
export function initialize() {
  console.log("Module loaded!");
}

// Good - 延迟到需要时执行
export function changeGlobalVar() {
  globalThis.someGlobalVar = 100;
}

// Good - 按需调用
export function initializeAppStorage() {
  AppStorage.setOrCreate("SomeAppStorageVar", 200);
}

并发最佳实践
任务选择指南
场景	推荐方案
CPU密集型短期任务	TaskPool
I/O密集型操作	async/await
长期后台任务	Worker
独立并行任务	TaskGroup
跨线程共享状态	Sendable + 容器
有序任务执行	TaskPool + 优先级
常见模式

并行数据处理：

@Concurrent
function processChunk(chunk: collections.Array<number>): number {
  return chunk.reduce((sum, val) => sum + val, 0);
}

const chunks = [new collections.Array([1,2,3]), new collections.Array([4,5,6])];
const group = new taskpool.TaskGroup();

chunks.forEach(chunk => {
  group.addTask(new taskpool.Task(processChunk, chunk));
});

const results = await taskpool.execute(group);
const total = results.reduce((sum, val) => sum + val, 0);


Worker消息传递：

// 主线程
workerInstance.postMessage({ type: 'fetch', url: '...' });

workerInstance.onmessage = (event) => {
  if (event.data.type === 'result') {
    handleResult(event.data.payload);
  }
};

性能考虑
TaskPool开销： 每个任务约1-2ms，批量处理小操作
数据传输： 16MB限制，大缓冲区使用Transferable
线程数量： 最大为CPU核数，自动扩缩容
优先级： 后台同步/备份任务使用IDLE
Sendable： 复杂对象优先使用Sendable而非序列化
常见问题
问题	原因	解决方案
任务未执行	缺少@Concurrent装饰器	添加装饰器
数据损坏	参数不可序列化	仅使用支持类型
任务超时	> 3分钟CPU时间	拆分为更小任务
UI冻结	阻塞主线程	使用TaskPool处理繁重工作
内存泄漏	Worker未终止	调用terminate()
数据未更新	共享对象非Sendable	标记为@Sendable
竞态条件	缺少异步锁	使用AsyncLock
Promise未捕获	缺少catch处理	使用errorManager监听unhandled rejection

📖 错误码速查: refs/error-codes.md — 10200001-10200301 错误码含义和修复建议

进一步参考

📁 本地 API 参考 (refs/ 文件夹):

文件	内容
refs/taskpool.md	TaskPool 完整 API — Task、TaskGroup、优先级、延时执行
refs/worker.md	Worker 完整 API — ThreadWorker、消息通信、生命周期
refs/collections.md	共享容器 API — collections.Array/Map/Set (跨线程传递)
refs/utils.md	ArkTSUtils API — AsyncLock、ASON、Sendable工具
refs/buffer.md	Buffer API — 二进制数据处理、编码转换
refs/xml.md	XML API — XmlSerializer、XmlPullParser
refs/containers.md	线性/非线性容器 API — ArrayList、HashMap 等普通容器
refs/error-codes.md	错误码速查表 — 10200001-10200301 错误处理

官方文档：

TaskPool API: https://docs.openharmony.cn/application-dev/reference/apis-arkui/js-apis-taskpool/
Worker API: https://docs.openharmony.cn/application-dev/reference/apis-arkui/js-apis-worker/
容器 API: https://docs.openharmony.cn/application-dev/reference/apis-arkts/js-apis-util/
XML API: https://docs.openharmony.cn/application-dev/reference/apis-arkts/js-apis-xml/
JSON API: https://docs.openharmony.cn/application-dev/reference/apis-arkts/js-apis-json/

详细指南：

异步并发概述: async-concurrency-overview.md
TaskPool简介: taskpool-introduction.md
Worker简介: worker-introduction.md
Sendable对象: arkts-sendable.md
共享容器: arkts-collections-introduction.md
异步锁: arkts-async-lock-introduction.md
动态导入: arkts-dynamic-import.md
懒导入: arkts-lazy-import.md
XML生成: xml-generation.md
JSON扩展: arkts-json.md
Weekly Installs
28
Repository
mengfei0053/skills
GitHub Stars
1
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass