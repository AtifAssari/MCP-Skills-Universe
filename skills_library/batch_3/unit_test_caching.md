---
title: unit-test-caching
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/unit-test-caching
---

# unit-test-caching

skills/giuseppe-trisciuoglio/developer-kit/unit-test-caching
unit-test-caching
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill unit-test-caching
Summary

Testing Spring Cache annotations without external infrastructure using in-memory cache managers.

Covers testing @Cacheable, @CacheEvict, and @CachePut annotations with patterns for verifying cache hits, misses, and invalidation
Uses ConcurrentMapCacheManager for fast, isolated unit tests instead of Redis or other external caches
Includes verification strategies via mock call counts, conditional caching with unless and condition parameters, and custom cache key generation with SpEL expressions
Provides setup examples for Maven and Gradle, plus complete test patterns for cache behavior, eviction, updates, and edge cases like null result handling
SKILL.md
Unit Testing Spring Caching
Overview

This skill provides patterns for unit testing Spring caching annotations (@Cacheable, @CacheEvict, @CachePut) without full Spring context. It covers cache hits/misses, invalidation, key generation, and conditional caching using in-memory ConcurrentMapCacheManager.

When to Use
Writing unit tests for @Cacheable method behavior
Verifying @CacheEvict cache invalidation works correctly
Testing @CachePut cache updates
Validating cache key generation from SpEL expressions
Testing conditional caching with unless/condition parameters
Mocking cache managers in fast unit tests without Redis
Instructions
Configure in-memory CacheManager: Use ConcurrentMapCacheManager for tests
Set up test fixtures: Mock repository and create service instance in @BeforeEach
Verify repository call counts: Use times(n) assertions to confirm cache behavior
Test cache hit: Call method twice, verify repository called once
Test cache miss: Verify repository called on each invocation
Test eviction: After @CacheEvict, verify repository called again on next read
Test key generation: Verify compound keys from SpEL expressions
Validate conditional caching: Test unless (null results) and condition (parameter-based)

Validation checkpoints:

Run test → If cache not working: verify @EnableCaching annotation present
If proxy issues: ensure method calls go through Spring proxy (no direct this calls)
If key mismatches: log actual cache key and compare with @Cacheable(key="...") expression
Examples
Maven
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-cache</artifactId>
</dependency>
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-test</artifactId>
  <scope>test</scope>
</dependency>

Gradle
dependencies {
  implementation("org.springframework.boot:spring-boot-starter-cache")
  testImplementation("org.springframework.boot:spring-boot-starter-test")
}

Testing @Cacheable (Cache Hit/Miss)
// Service
@Service
public class UserService {
  private final UserRepository userRepository;

  public UserService(UserRepository userRepository) {
    this.userRepository = userRepository;
  }

  @Cacheable("users")
  public User getUserById(Long id) {
    return userRepository.findById(id).orElse(null);
  }
}

// Test
class UserServiceCachingTest {

  private UserRepository userRepository;
  private UserService userService;

  @BeforeEach
  void setUp() {
    userRepository = mock(UserRepository.class);
    userService = new UserService(userRepository);
  }

  @Test
  void shouldCacheUserAfterFirstCall() {
    User user = new User(1L, "Alice");
    when(userRepository.findById(1L)).thenReturn(Optional.of(user));

    // First call - hits database
    User firstCall = userService.getUserById(1L);
    // Second call - hits cache
    User secondCall = userService.getUserById(1L);

    assertThat(firstCall).isEqualTo(secondCall);
    verify(userRepository, times(1)).findById(1L); // Only once due to cache
  }

  @Test
  void shouldInvokeRepositoryOnCacheMiss() {
    when(userRepository.findById(1L)).thenReturn(Optional.of(new User(1L, "Bob")));

    userService.getUserById(1L);
    userService.getUserById(1L);

    verify(userRepository, times(2)).findById(1L); // No caching occurred
  }
}

Testing @CacheEvict
// Service
@Service
public class ProductService {
  private final ProductRepository productRepository;

  public ProductService(ProductRepository productRepository) {
    this.productRepository = productRepository;
  }

  @Cacheable("products")
  public Product getProductById(Long id) {
    return productRepository.findById(id).orElse(null);
  }

  @CacheEvict("products")
  public void deleteProduct(Long id) {
    productRepository.deleteById(id);
  }
}

// Test
class ProductCacheEvictTest {

  private ProductRepository productRepository;
  private ProductService productService;

  @BeforeEach
  void setUp() {
    productRepository = mock(ProductRepository.class);
    productService = new ProductService(productRepository);
  }

  @Test
  void shouldEvictProductFromCacheWhenDeleted() {
    Product product = new Product(1L, "Laptop", 999.99);
    when(productRepository.findById(1L)).thenReturn(Optional.of(product));

    productService.getProductById(1L); // Cache the product
    productService.deleteProduct(1L); // Evict from cache

    // Repository called again after eviction
    productService.getProductById(1L);
    verify(productRepository, times(2)).findById(1L);
  }

  @Test
  void shouldClearAllEntriesWithAllEntriesTrue() {
    Product product1 = new Product(1L, "Laptop", 999.99);
    Product product2 = new Product(2L, "Mouse", 29.99);
    when(productRepository.findById(anyLong())).thenAnswer(i ->
      Optional.of(new Product(i.getArgument(0), "Product", 10.0)));

    productService.getProductById(1L);
    productService.getProductById(2L);

    // Use reflection or clear() on ConcurrentMapCache
    productService.clearAllProducts();

    productService.getProductById(1L);
    productService.getProductById(2L);

    verify(productRepository, times(4)).findById(anyLong());
  }
}

Testing @CachePut
@Service
public class OrderService {
  private final OrderRepository orderRepository;

  public OrderService(OrderRepository orderRepository) {
    this.orderRepository = orderRepository;
  }

  @Cacheable("orders")
  public Order getOrder(Long id) {
    return orderRepository.findById(id).orElse(null);
  }

  @CachePut(value = "orders", key = "#order.id")
  public Order updateOrder(Order order) {
    return orderRepository.save(order);
  }
}

class OrderCachePutTest {

  private OrderRepository orderRepository;
  private OrderService orderService;

  @BeforeEach
  void setUp() {
    orderRepository = mock(OrderRepository.class);
    orderService = new OrderService(orderRepository);
  }

  @Test
  void shouldUpdateCacheWhenOrderIsUpdated() {
    Order original = new Order(1L, "Pending", 100.0);
    Order updated = new Order(1L, "Shipped", 100.0);

    when(orderRepository.findById(1L)).thenReturn(Optional.of(original));
    when(orderRepository.save(updated)).thenReturn(updated);

    orderService.getOrder(1L);
    orderService.updateOrder(updated);

    // Next call returns updated version from cache
    Order cachedOrder = orderService.getOrder(1L);
    assertThat(cachedOrder.getStatus()).isEqualTo("Shipped");
  }
}

Testing Conditional Caching
@Service
public class DataService {
  private final DataRepository dataRepository;

  public DataService(DataRepository dataRepository) {
    this.dataRepository = dataRepository;
  }

  // Don't cache null results
  @Cacheable(value = "data", unless = "#result == null")
  public Data getData(Long id) {
    return dataRepository.findById(id).orElse(null);
  }

  // Only cache when id > 0
  @Cacheable(value = "users", condition = "#id > 0")
  public User getUser(Long id) {
    return dataRepository.findById(id).map(u -> new User(u.getId(), u.getName())).orElse(null);
  }
}

class ConditionalCachingTest {

  @Test
  void shouldNotCacheNullResults() {
    DataRepository dataRepository = mock(DataRepository.class);
    when(dataRepository.findById(999L)).thenReturn(Optional.empty());
    DataService service = new DataService(dataRepository);

    service.getData(999L);
    service.getData(999L);

    verify(dataRepository, times(2)).findById(999L); // Called twice - no caching
  }

  @Test
  void shouldNotCacheWhenConditionIsFalse() {
    DataRepository dataRepository = mock(DataRepository.class);
    when(dataRepository.findById(-1L)).thenReturn(Optional.of(new Data(-1L, "Test")));

    DataService service = new DataService(dataRepository);

    service.getUser(-1L);
    service.getUser(-1L);

    verify(dataRepository, times(2)).findById(-1L); // Condition "#id > 0" = false
  }
}

Testing Cache Keys with SpEL
@Service
public class InventoryService {
  private final InventoryRepository inventoryRepository;

  public InventoryService(InventoryRepository inventoryRepository) {
    this.inventoryRepository = inventoryRepository;
  }

  // Compound key: productId-warehouseId
  @Cacheable(value = "inventory", key = "#productId + '-' + #warehouseId")
  public InventoryItem getInventory(Long productId, Long warehouseId) {
    return inventoryRepository.findByProductAndWarehouse(productId, warehouseId);
  }
}

class CacheKeyTest {

  @Test
  void shouldUseCorrectCacheKeyForDifferentCombinations() {
    InventoryRepository repository = mock(InventoryRepository.class);
    InventoryItem item = new InventoryItem(1L, 1L, 100);
    when(repository.findByProductAndWarehouse(1L, 1L)).thenReturn(item);

    InventoryService service = new InventoryService(repository);

    // Same key: "1-1" - should cache
    service.getInventory(1L, 1L);
    service.getInventory(1L, 1L); // Cache hit
    verify(repository, times(1)).findByProductAndWarehouse(1L, 1L);

    // Different key: "2-1" - cache miss
    service.getInventory(2L, 1L); // Cache miss
    verify(repository, times(2)).findByProductAndWarehouse(any(), any());
  }
}

Best Practices
Mock repository calls: Use verify(mock, times(n)) to assert cache behavior
Test both hit and miss scenarios: Don't just test the happy path
Clear cache state: Reset between tests to avoid flaky results
Use ConcurrentMapCacheManager: Fast, no external dependencies
Verify eviction: Always test that @CacheEvict actually invalidates cached data
Constraints and Warnings
@Cacheable requires proxy: Direct method calls (this.method()) bypass caching - use dependency injection
Cache key collisions: Compound keys from SpEL must be unique per dataset
Null caching: Null results are cached by default - use unless = "#result == null" to exclude
@CachePut always executes: Unlike @Cacheable, it always runs the method
Memory usage: In-memory caches grow unbounded - consider TTL for long-running tests
Thread safety: ConcurrentMapCacheManager is thread-safe; distributed caches may require additional config
Troubleshooting
Issue	Solution
Cache not working	Verify @EnableCaching on test config
Proxy bypass	Use autowired/constructor injection, not direct this calls
Key mismatch	Log cache key with cache.getNativeKey() to debug SpEL
Flaky tests	Clear cache in @BeforeEach before each test
References
Spring Caching Documentation
Cacheable Annotation
SpEL Expressions
Weekly Installs
698
Repository
giuseppe-trisci…oper-kit
GitHub Stars
233
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass