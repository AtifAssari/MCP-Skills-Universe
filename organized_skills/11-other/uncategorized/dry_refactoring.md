---
rating: ⭐⭐⭐
title: dry-refactoring
url: https://skills.sh/yyh211/claude-meta-skill/dry-refactoring
---

# dry-refactoring

skills/yyh211/claude-meta-skill/dry-refactoring
dry-refactoring
Installation
$ npx skills add https://github.com/yyh211/claude-meta-skill --skill dry-refactoring
SKILL.md
DRY 标准化流程：从识别到重构

这个技能指导你系统性地应用 DRY (Don't Repeat Yourself) 原则，通过四步标准化流程消除代码重复，提升代码质量和可维护性。

When to Use This Skill

使用此技能当用户请求：

消除代码重复或冗余
重构有明显复制粘贴痕迹的代码
应用 DRY 原则优化代码库
识别并修复"代码坏味道"（如魔术数字、重复逻辑）
提取公共逻辑为可复用单元
改善代码的可维护性

关键触发词: DRY, 重复代码, 代码重复, 重构, 消除重复, 复制粘贴, 魔术数字, 代码坏味道, 抽象, 提取函数

核心思想

系统中的每一处知识都必须拥有一个单一、明确、权威的表示。

这意味着：

任何业务逻辑、算法或配置信息都应该只存在于代码库的一个地方
如果需要修改，你只需改这一个地方
修改会自动反映到所有使用该逻辑的地方

两次法则 (Rule of Two)： 当你第二次写下几乎相同的代码块时，警钟就应该敲响。这是开始重构的信号。

四步标准化流程

这是一个可在编码任何阶段应用的微循环。严格按照步骤执行，确保重构的安全性和有效性。

第一步：识别重复 (Identify Repetition)

目标: 像侦探一样，对代码中的"坏味道"保持警惕，找出所有重复。

1.1 明显的重复

直接复制粘贴：

两块或多块代码长得几乎一模一样
只有变量名或少数值不同
这是最明显、最需要被消除的重复

示例：

// 重复 1
function calculateOrderDiscount(orderTotal) {
  if (orderTotal > 100) {
    return orderTotal * 0.1;
  }
  return 0;
}

// 重复 2
function calculateCouponDiscount(couponTotal) {
  if (couponTotal > 100) {
    return couponTotal * 0.1;
  }
  return 0;
}


"魔术数字"或字符串：

同一个配置值或字符串在多处以字面量形式出现
例如：0.08、"http://api.example.com"、100

示例：

# 魔术数字重复
def calculate_tax_1(amount):
    return amount * 0.08  # ❌ 魔术数字

def calculate_tax_2(amount):
    return amount * 0.08  # ❌ 再次出现

def calculate_total(amount):
    tax = amount * 0.08   # ❌ 第三次
    return amount + tax

1.2 语义上的重复

结构性重复：

代码结构相似，但具体变量名或值不同
多个 if-else 结构都在做类似的条件判断和赋值

示例：

// 结构性重复
function processUserData(user: User) {
  if (user.age >= 18) {
    user.status = 'adult';
  } else {
    user.status = 'minor';
  }
}

function processProductData(product: Product) {
  if (product.price >= 100) {
    product.category = 'premium';
  } else {
    product.category = 'standard';
  }
}


逻辑重复：

两个不同的函数，代码看起来不一样
但它们在业务逻辑层面实现的是同一个目标

示例：

// 逻辑重复：都在计算折扣，只是来源不同
function applyMembershipDiscount(price, memberLevel) {
  const discountRates = { gold: 0.2, silver: 0.1, bronze: 0.05 };
  return price * (1 - (discountRates[memberLevel] || 0));
}

function applySeasonalDiscount(price, season) {
  const discountRates = { winter: 0.2, spring: 0.1, summer: 0.05 };
  return price * (1 - (discountRates[season] || 0));
}

识别清单

当你审查代码时，检查以下信号：

 复制粘贴的代码块（完全相同或高度相似）
 相同的数字、字符串在多处出现
 相似的 if-else 或 switch-case 结构
 功能相似但命名不同的函数
 相同的算法在不同地方重新实现
 相同的验证逻辑分散在多个地方

💡 Action: 使用搜索功能查找重复的字面量、相似的函数名模式。记录所有重复出现的位置。

第二步：抽象逻辑 (Abstract the Logic)

目标: 将重复的逻辑提取出来，封装到一个独立、可复用的单元中。

2.1 识别可变与不变部分

不变部分：

这是重复的核心逻辑
每次重复时都保持不变的代码
这将成为你的抽象主体

可变部分：

每次重复时发生变化的东西
不同的值、变量名、配置
这些将成为函数或类的参数

分析示例：

// 原始重复代码
const userEmail = validateEmail(user.email);
const adminEmail = validateEmail(admin.email);
const supportEmail = validateEmail(support.email);

// 分析：
// 不变部分：validateEmail() 调用
// 可变部分：不同的 email 值

2.2 选择合适的抽象形式

根据重复的特点，选择最合适的抽象方式：

抽象形式	适用场景	示例
函数 (Function)	封装一段算法或行为	计算折扣、验证输入、格式化数据
类 (Class)	封装行为 + 关联状态	用户管理器、数据处理器、配置管理器
模块/组件	一组相关的函数、类和配置	认证模块、日志模块、API 客户端
配置文件/常量	重复的魔术数字或字符串	API 端点、税率、阈值
高阶函数	重复的控制流程或模式	重试逻辑、缓存包装、错误处理
2.3 设计抽象接口

函数抽象示例：

# ❌ 重复代码
def process_user_order(user_id, order_data):
    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        raise ValueError("User not found")
    # 处理订单...

def process_user_payment(user_id, payment_data):
    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        raise ValueError("User not found")
    # 处理支付...

# ✅ 抽象后
def get_user_or_error(user_id):
    """不变部分：获取用户并验证"""
    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        raise ValueError("User not found")
    return user

def process_user_order(user_id, order_data):
    user = get_user_or_error(user_id)  # 可变部分：user_id
    # 处理订单...

def process_user_payment(user_id, payment_data):
    user = get_user_or_error(user_id)  # 可变部分：user_id
    # 处理支付...


常量抽象示例：

// ❌ 魔术数字
function calculateTax(amount) {
  return amount * 0.08;
}

function displayTaxInfo(amount) {
  console.log(`Tax (8%): $${amount * 0.08}`);
}

// ✅ 抽象为常量
const TAX_RATE = 0.08;

function calculateTax(amount) {
  return amount * TAX_RATE;
}

function displayTaxInfo(amount) {
  console.log(`Tax (${TAX_RATE * 100}%): $${amount * TAX_RATE}`);
}


类抽象示例：

// ❌ 重复的状态和行为
const userCache = new Map();
function getUserFromCache(id: string) { /*...*/ }
function setUserInCache(id: string, user: User) { /*...*/ }

const productCache = new Map();
function getProductFromCache(id: string) { /*...*/ }
function setProductInCache(id: string, product: Product) { /*...*/ }

// ✅ 抽象为类
class Cache<T> {
  private store = new Map<string, T>();

  get(id: string): T | undefined {
    return this.store.get(id);
  }

  set(id: string, value: T): void {
    this.store.set(id, value);
  }
}

const userCache = new Cache<User>();
const productCache = new Cache<Product>();

抽象设计原则

Do:

✅ 参数化可变部分（值、配置、行为）
✅ 保持接口简单（参数数量 ≤ 4 个）
✅ 使用描述性命名（说明"做什么"而非"怎么做"）
✅ 考虑未来的扩展性（但不要过度设计）

Don't:

❌ 创建过于通用的抽象（"万能函数"）
❌ 过早抽象（只有一次使用时不要抽象）
❌ 忽略性能影响（例如不必要的函数调用开销）
❌ 使用难以理解的抽象（增加认知负担）

💡 Action: 创建一个新的函数、类或配置文件，将"不变部分"放进去，将"可变部分"定义为参数。

第三步：替换实现 (Replace the Implementation)

目标: 用新的抽象单元替换所有旧的重复代码。

3.1 系统性替换

步骤：

定位所有重复点：回到第一步记录的所有位置
逐一替换：删除旧代码，调用新抽象
传入正确参数：确保参数对应正确
保持行为一致：确保替换前后功能完全相同

替换示例：

Before (重复代码)：

# 位置 1: user_service.py
def create_user(data):
    if not data.get('email'):
        return {'error': 'Email is required'}, 400
    if not data.get('password'):
        return {'error': 'Password is required'}, 400
    # 创建用户...

# 位置 2: product_service.py
def create_product(data):
    if not data.get('name'):
        return {'error': 'Name is required'}, 400
    if not data.get('price'):
        return {'error': 'Price is required'}, 400
    # 创建产品...


After (使用抽象)：

# 新抽象: validation_utils.py
def validate_required_fields(data, required_fields):
    """验证必填字段"""
    for field in required_fields:
        if not data.get(field):
            return {'error': f'{field.capitalize()} is required'}, 400
    return None

# 位置 1: user_service.py (已替换)
def create_user(data):
    error = validate_required_fields(data, ['email', 'password'])
    if error:
        return error
    # 创建用户...

# 位置 2: product_service.py (已替换)
def create_product(data):
    error = validate_required_fields(data, ['name', 'price'])
    if error:
        return error
    # 创建产品...

3.2 处理边缘情况

有时候重复代码之间存在细微差异，需要特殊处理：

策略 1：添加可选参数

// 大部分重复，但有一个地方需要额外日志
function processData(data, options = {}) {
  // 通用处理...

  if (options.enableLogging) {
    console.log('Processing:', data);
  }

  return result;
}

// 使用
processData(data1);  // 无日志
processData(data2, { enableLogging: true });  // 有日志


策略 2：回调函数

// 核心流程相同，但中间步骤不同
function processWithCustomStep<T>(
  data: T,
  customStep: (item: T) => T
): T {
  // 前置处理
  const prepared = prepare(data);

  // 可变的自定义步骤
  const processed = customStep(prepared);

  // 后置处理
  return finalize(processed);
}

// 使用
processWithCustomStep(userData, (user) => validateUser(user));
processWithCustomStep(productData, (product) => enrichProduct(product));


策略 3：保留特殊情况

# 如果某个重复有本质上的不同，考虑保留它
def process_standard_order(order):
    return apply_dry_abstraction(order, 'standard')

def process_vip_order(order):
    # VIP 订单有完全不同的业务逻辑，不强行抽象
    # 保留独立实现
    pass

替换清单
 确认所有重复点都已替换（不要遗漏）
 删除旧的重复代码（避免混用新旧方式）
 检查导入语句和依赖关系
 确保参数顺序和类型正确
 处理了所有边缘情况

⚠️ 警告: 如果只替换了一部分，你就创造了另一种不一致，情况可能更糟。确保全部替换或全部不替换。

💡 Action: 使用 IDE 的"查找所有引用"功能，确保没有遗漏任何重复点。

第四步：验证与测试 (Verify and Test)

目标: 确保重构没有破坏任何功能，程序行为在重构前后完全一致。

4.1 单元测试

为你新创建的抽象编写独立的单元测试：

测试覆盖要点：

✅ 正常输入的正确输出
✅ 边界值测试（空值、最大值、最小值）
✅ 异常输入的错误处理
✅ 不同参数组合的行为

示例：

# 抽象函数
def calculate_discount(price, discount_rate):
    """计算折扣后价格"""
    if not 0 <= discount_rate <= 1:
        raise ValueError("Discount rate must be between 0 and 1")
    return price * (1 - discount_rate)

# 单元测试
def test_calculate_discount():
    # 正常情况
    assert calculate_discount(100, 0.1) == 90
    assert calculate_discount(100, 0) == 100

    # 边界情况
    assert calculate_discount(0, 0.5) == 0
    assert calculate_discount(100, 1) == 0

    # 异常情况
    with pytest.raises(ValueError):
        calculate_discount(100, 1.5)
    with pytest.raises(ValueError):
        calculate_discount(100, -0.1)

4.2 集成测试

运行那些覆盖了被修改代码区域的集成测试：

# 运行特定模块的测试
pytest tests/test_user_service.py
pytest tests/test_product_service.py

# 或运行整个测试套件
npm test
pytest


检查要点：

 所有测试都通过
 没有新的失败或错误
 性能没有显著下降
 覆盖率没有降低
4.3 手动验证

如果没有自动化测试（或测试覆盖不足），进行手动验证：

验证清单：

 启动应用程序，检查是否正常运行
 测试被修改的功能（通过 UI 或 API）
 检查日志输出是否正常
 测试错误场景（无效输入、边界条件）
 在不同环境中测试（开发、测试、预发布）
4.4 性能验证

确保抽象没有引入性能问题：

import time

# 性能测试
def benchmark_function(func, *args, iterations=1000):
    start = time.time()
    for _ in range(iterations):
        func(*args)
    end = time.time()
    return (end - start) / iterations

# 对比重构前后
old_time = benchmark_function(old_implementation, test_data)
new_time = benchmark_function(new_implementation, test_data)

print(f"Old: {old_time:.6f}s, New: {new_time:.6f}s")
print(f"Difference: {((new_time - old_time) / old_time * 100):.2f}%")

4.5 代码审查

如果在团队中工作，进行代码审查：

审查要点：

抽象是否合理且易于理解？
命名是否清晰且符合约定？
是否有遗漏的重复点？
是否过度抽象或设计复杂？
文档和注释是否充分？

💡 Action: 运行所有相关测试，确保程序的外部行为在重构前后完全一致。没有测试？现在是编写测试的最佳时机。

完整示例：从头到尾
场景：电商系统的折扣计算
原始代码（存在重复）
// order_service.js
function calculateOrderTotal(order) {
  let total = 0;
  for (const item of order.items) {
    total += item.price * item.quantity;
  }

  // 会员折扣
  if (order.memberLevel === 'gold') {
    total = total * 0.8;  // ❌ 魔术数字
  } else if (order.memberLevel === 'silver') {
    total = total * 0.9;  // ❌ 魔术数字
  }

  return total;
}

// cart_service.js
function calculateCartTotal(cart) {
  let total = 0;
  for (const item of cart.items) {
    total += item.price * item.quantity;  // ❌ 重复计算逻辑
  }

  // 优惠券折扣
  if (cart.couponType === 'premium') {
    total = total * 0.8;  // ❌ 重复的折扣计算
  } else if (cart.couponType === 'standard') {
    total = total * 0.9;  // ❌ 重复的折扣计算
  }

  return total;
}

步骤 1：识别重复

发现的重复：

计算商品总价的循环逻辑（结构重复）
折扣计算逻辑（逻辑重复）
魔术数字 0.8 和 0.9（明显重复）
步骤 2：抽象逻辑
// pricing_utils.js (新建)

// 抽象 1：商品总价计算
function calculateItemsTotal(items) {
  return items.reduce((total, item) => {
    return total + (item.price * item.quantity);
  }, 0);
}

// 抽象 2：折扣配置（消除魔术数字）
const DISCOUNT_RATES = {
  membership: {
    gold: 0.2,    // 20% off
    silver: 0.1,  // 10% off
    bronze: 0.05  // 5% off
  },
  coupon: {
    premium: 0.2,   // 20% off
    standard: 0.1,  // 10% off
    basic: 0.05     // 5% off
  }
};

// 抽象 3：应用折扣
function applyDiscount(amount, discountRate) {
  if (discountRate < 0 || discountRate > 1) {
    throw new Error('Invalid discount rate');
  }
  return amount * (1 - discountRate);
}

// 抽象 4：获取折扣率
function getDiscountRate(category, level) {
  return DISCOUNT_RATES[category]?.[level] || 0;
}

export { calculateItemsTotal, applyDiscount, getDiscountRate };

步骤 3：替换实现
// order_service.js (重构后)
import { calculateItemsTotal, applyDiscount, getDiscountRate } from './pricing_utils.js';

function calculateOrderTotal(order) {
  const subtotal = calculateItemsTotal(order.items);
  const discountRate = getDiscountRate('membership', order.memberLevel);
  return applyDiscount(subtotal, discountRate);
}

// cart_service.js (重构后)
import { calculateItemsTotal, applyDiscount, getDiscountRate } from './pricing_utils.js';

function calculateCartTotal(cart) {
  const subtotal = calculateItemsTotal(cart.items);
  const discountRate = getDiscountRate('coupon', cart.couponType);
  return applyDiscount(subtotal, discountRate);
}

步骤 4：验证与测试
// pricing_utils.test.js
import { calculateItemsTotal, applyDiscount, getDiscountRate } from './pricing_utils.js';

describe('Pricing Utils', () => {
  describe('calculateItemsTotal', () => {
    it('should calculate total for multiple items', () => {
      const items = [
        { price: 10, quantity: 2 },
        { price: 5, quantity: 3 }
      ];
      expect(calculateItemsTotal(items)).toBe(35);
    });

    it('should return 0 for empty items', () => {
      expect(calculateItemsTotal([])).toBe(0);
    });
  });

  describe('applyDiscount', () => {
    it('should apply 20% discount correctly', () => {
      expect(applyDiscount(100, 0.2)).toBe(80);
    });

    it('should throw error for invalid discount rate', () => {
      expect(() => applyDiscount(100, 1.5)).toThrow('Invalid discount rate');
    });
  });

  describe('getDiscountRate', () => {
    it('should return correct membership discount', () => {
      expect(getDiscountRate('membership', 'gold')).toBe(0.2);
    });

    it('should return 0 for unknown level', () => {
      expect(getDiscountRate('membership', 'unknown')).toBe(0);
    });
  });
});

// 运行测试
// npm test pricing_utils.test.js


重构成果：

✅ 消除了所有重复代码
✅ 魔术数字集中管理
✅ 每个函数职责单一
✅ 易于测试和维护
✅ 如果需要添加新的会员等级或折扣类型，只需修改 DISCOUNT_RATES
常见陷阱与解决方案
陷阱 1：过度抽象 (Over-Abstraction)

症状：创建了过于通用、难以理解的抽象。

示例：

// ❌ 过度抽象
function universalProcessor(data, options, callbacks, config, meta) {
  // 100 行通用处理逻辑...
}

// ✅ 合理抽象
function processUserData(user) {
  return validate(user) && transform(user);
}


解决方案：

只在有明确重复时才抽象
保持抽象简单明了
如果参数超过 4 个，考虑重新设计
陷阱 2：不完全替换

症状：只替换了部分重复点，留下了一些旧代码。

后果：

代码库中存在新旧两种实现
未来修改时容易遗漏
造成新的不一致

解决方案：

使用全局搜索确保找到所有重复
一次性完成所有替换
使用 linter 或静态分析工具检测未使用的代码
陷阱 3：忽略性能影响

症状：抽象引入了不必要的性能开销。

示例：

# ❌ 每次调用都重新编译正则表达式
def validate_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)

# ✅ 复用编译后的正则表达式
EMAIL_PATTERN = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

def validate_email(email):
    return EMAIL_PATTERN.match(email)


解决方案：

对性能敏感的代码进行基准测试
使用缓存、记忆化等优化技术
必要时使用性能分析工具
陷阱 4：破坏封装性

症状：抽象暴露了过多内部实现细节。

示例：

// ❌ 暴露内部状态
class UserManager {
  public users: Map<string, User>;  // 直接暴露内部数据结构

  getUser(id: string) {
    return this.users.get(id);
  }
}

// ✅ 隐藏内部实现
class UserManager {
  private users: Map<string, User>;

  getUser(id: string): User | undefined {
    return this.users.get(id);
  }

  addUser(user: User): void {
    this.users.set(user.id, user);
  }
}


解决方案：

使用访问控制（private, protected）
提供明确的公共接口
隐藏实现细节
最佳实践
1. 渐进式重构

不要试图一次性重构整个代码库：

策略：

✅ 每次重构一个小的重复区域
✅ 重构后立即测试
✅ 提交小的、原子性的变更
✅ 逐步扩大重构范围

示例工作流：

# 1. 创建特性分支
git checkout -b refactor/dry-pricing-logic

# 2. 重构一个模块
# 编辑 pricing_utils.js

# 3. 测试
npm test

# 4. 提交
git add pricing_utils.js
git commit -m "Extract pricing calculation to reusable utility"

# 5. 重构使用该模块的文件
# 编辑 order_service.js

# 6. 再次测试和提交
npm test
git add order_service.js
git commit -m "Refactor order service to use pricing utility"

# 7. 继续其他模块...

2. 文档化你的抽象

好的抽象需要好的文档：

/**
 * 计算商品折扣后的价格
 *
 * @param price - 原始价格（必须 >= 0）
 * @param discountRate - 折扣率（0-1 之间，0.2 表示 20% 折扣）
 * @returns 折扣后的价格
 * @throws {Error} 如果 discountRate 不在有效范围内
 *
 * @example
 * applyDiscount(100, 0.2) // 返回 80
 * applyDiscount(50, 0) // 返回 50（无折扣）
 */
function applyDiscount(price: number, discountRate: number): number {
  if (discountRate < 0 || discountRate > 1) {
    throw new Error(`Invalid discount rate: ${discountRate}. Must be between 0 and 1.`);
  }
  return price * (1 - discountRate);
}

3. 使用类型系统

利用类型系统防止误用：

// 使用类型别名增强可读性
type DiscountRate = number; // 0-1 之间
type Price = number;        // >= 0

// 更好：使用品牌类型确保类型安全
type DiscountRate = number & { __brand: 'DiscountRate' };

function createDiscountRate(value: number): DiscountRate {
  if (value < 0 || value > 1) {
    throw new Error('Discount rate must be between 0 and 1');
  }
  return value as DiscountRate;
}

function applyDiscount(price: Price, discountRate: DiscountRate): Price {
  return (price * (1 - discountRate)) as Price;
}

// 使用
const rate = createDiscountRate(0.2); // 类型检查通过
applyDiscount(100, rate);

// applyDiscount(100, 0.2); // ❌ 类型错误！必须使用 createDiscountRate

4. 重构前先写测试

如果没有测试，先写测试再重构：

// 步骤 1：为现有（重复的）代码写测试
describe('Original Implementation', () => {
  it('should calculate order total correctly', () => {
    const order = {
      items: [{ price: 10, quantity: 2 }],
      memberLevel: 'gold'
    };
    expect(calculateOrderTotal(order)).toBe(16); // 20 * 0.8
  });
});

// 步骤 2：重构代码

// 步骤 3：确保测试仍然通过
// npm test

检查清单

在完成 DRY 重构后，验证以下内容：

识别阶段
 找到了所有明显的代码重复
 识别了魔术数字和硬编码字符串
 发现了结构性和逻辑性重复
 记录了所有重复出现的位置
抽象阶段
 清楚区分了可变和不变部分
 选择了合适的抽象形式（函数/类/配置）
 抽象有清晰、描述性的命名
 参数数量合理（≤ 4 个）
 没有过度抽象
替换阶段
 所有重复点都已替换
 没有遗留旧代码
 导入和依赖关系正确
 处理了所有边缘情况
验证阶段
 编写了单元测试
 所有现有测试仍然通过
 进行了手动验证（如适用）
 性能没有显著下降
 代码审查已完成（如在团队中工作）
整体质量
 代码更易读、易维护
 单一职责原则得到遵守
 修改只需在一个地方进行
 有充分的文档和注释
总结

DRY 原则是软件工程的基石之一。通过系统性地应用这个四步流程，你可以：

识别重复：培养对代码坏味道的敏感度
抽象逻辑：创建可复用、易维护的代码单元
替换实现：消除重复，统一实现
验证测试：确保重构的安全性

记住：

不要过早抽象（等到有明确重复时再抽象）
不要过度抽象（保持简单明了）
小步前进（渐进式重构比一次性大重构更安全）
测试是你的安全网（重构前先写测试）

最终目标：

让每一处知识在系统中都有唯一的、权威的表示。当需要修改时，你只改一个地方，所有使用该知识的地方自动更新。

这就是 DRY 的力量。

Weekly Installs
49
Repository
yyh211/claude-meta-skill
GitHub Stars
260
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass