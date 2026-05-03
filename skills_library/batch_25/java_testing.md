---
title: java-testing
url: https://skills.sh/pluginagentmarketplace/custom-plugin-java/java-testing
---

# java-testing

skills/pluginagentmarketplace/custom-plugin-java/java-testing
java-testing
Installation
$ npx skills add https://github.com/pluginagentmarketplace/custom-plugin-java --skill java-testing
Summary

Comprehensive Java testing with JUnit 5, Mockito, and integration testing frameworks.

Covers unit testing with JUnit 5 (parameterized tests, lifecycle annotations, extensions), mocking with Mockito (stubbing, verification, BDD style), and fluent assertions with AssertJ
Includes integration testing patterns using Spring Boot Test slices, Testcontainers for database isolation, and MockMvc for API testing
Provides test data builders, TDD/BDD practices, and JaCoCo coverage configuration with 80% line coverage targets
Supports both JUnit 5 and TestNG frameworks with configurable test types (unit, integration, e2e, contract)
SKILL.md
Java Testing Skill

Write comprehensive tests for Java applications with modern testing practices.

Overview

This skill covers Java testing with JUnit 5, Mockito, AssertJ, and integration testing with Spring Boot Test and Testcontainers. Includes TDD patterns and test coverage strategies.

When to Use This Skill

Use when you need to:

Write unit tests with JUnit 5
Create mocks with Mockito
Build integration tests with Testcontainers
Implement TDD/BDD practices
Improve test coverage
Topics Covered
JUnit 5
@Test, @Nested, @DisplayName
@ParameterizedTest with sources
Lifecycle annotations
Extensions and custom annotations
Mockito
@Mock, @InjectMocks, @Spy
Stubbing (when/thenReturn)
Verification (verify, times)
BDD style (given/willReturn)
AssertJ
Fluent assertions
Collection assertions
Exception assertions
Custom assertions
Integration Testing
@SpringBootTest slices
Testcontainers setup
MockMvc for APIs
Database testing
Quick Reference
// Unit Test with Mockito
@ExtendWith(MockitoExtension.class)
class UserServiceTest {

    @Mock
    private UserRepository userRepository;

    @InjectMocks
    private UserService userService;

    @Test
    @DisplayName("Should find user by ID")
    void shouldFindUserById() {
        // Given
        User user = new User(1L, "John");
        given(userRepository.findById(1L)).willReturn(Optional.of(user));

        // When
        Optional<User> result = userService.findById(1L);

        // Then
        assertThat(result)
            .isPresent()
            .hasValueSatisfying(u ->
                assertThat(u.getName()).isEqualTo("John"));
        then(userRepository).should().findById(1L);
    }
}

// Parameterized Test
@ParameterizedTest
@CsvSource({
    "valid@email.com, true",
    "invalid-email, false",
    "'', false"
})
void shouldValidateEmail(String email, boolean expected) {
    assertThat(validator.isValid(email)).isEqualTo(expected);
}

// Integration Test with Testcontainers
@Testcontainers
@SpringBootTest
class OrderRepositoryIT {

    @Container
    static PostgreSQLContainer<?> postgres =
        new PostgreSQLContainer<>("postgres:15");

    @DynamicPropertySource
    static void configure(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", postgres::getJdbcUrl);
        registry.add("spring.datasource.username", postgres::getUsername);
        registry.add("spring.datasource.password", postgres::getPassword);
    }

    @Autowired
    private OrderRepository repository;

    @Test
    void shouldPersistOrder() {
        Order saved = repository.save(new Order("item", 100.0));
        assertThat(saved.getId()).isNotNull();
    }
}

// API Test with MockMvc
@WebMvcTest(UserController.class)
class UserControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private UserService userService;

    @Test
    void shouldReturnUser() throws Exception {
        given(userService.findById(1L))
            .willReturn(Optional.of(new User(1L, "John")));

        mockMvc.perform(get("/api/users/1"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.name").value("John"));
    }
}

Test Data Builders
public class UserTestBuilder {
    private Long id = 1L;
    private String name = "John Doe";
    private String email = "john@example.com";
    private boolean active = true;

    public static UserTestBuilder aUser() {
        return new UserTestBuilder();
    }

    public UserTestBuilder withName(String name) {
        this.name = name;
        return this;
    }

    public UserTestBuilder inactive() {
        this.active = false;
        return this;
    }

    public User build() {
        return new User(id, name, email, active);
    }
}

// Usage
User user = aUser().withName("Jane").inactive().build();

Coverage Goals
<!-- JaCoCo configuration -->
<configuration>
    <rules>
        <rule>
            <element>BUNDLE</element>
            <limits>
                <limit>
                    <counter>LINE</counter>
                    <value>COVEREDRATIO</value>
                    <minimum>0.80</minimum>
                </limit>
            </limits>
        </rule>
    </rules>
</configuration>

Troubleshooting
Common Issues
Problem	Cause	Solution
Mock not working	Missing @ExtendWith	Add MockitoExtension
NPE in test	Mock not initialized	Check @InjectMocks
Flaky test	Shared state	Isolate test data
Context fails	Missing bean	Use @MockBean
Debug Checklist
□ Run single test in isolation
□ Check mock setup matches invocation
□ Verify @BeforeEach setup
□ Review @Transactional boundaries
□ Check for shared mutable state

Usage
Skill("java-testing")

Related Skills
java-testing-advanced - Advanced patterns
java-spring-boot - Spring test slices
Weekly Installs
589
Repository
pluginagentmark…gin-java
GitHub Stars
34
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass