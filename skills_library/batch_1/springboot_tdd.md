---
title: springboot-tdd
url: https://skills.sh/affaan-m/everything-claude-code/springboot-tdd
---

# springboot-tdd

skills/affaan-m/everything-claude-code/springboot-tdd
springboot-tdd
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill springboot-tdd
Summary

Test-driven development framework for Spring Boot with JUnit 5, Mockito, MockMvc, Testcontainers, and JaCoCo enforcement.

Covers unit tests (Mockito), web layer tests (MockMvc), integration tests (SpringBootTest), and persistence tests (DataJpaTest) with concrete examples
Integrates Testcontainers for production-mirroring Postgres/Redis databases and JaCoCo for enforcing 80%+ code coverage
Emphasizes Arrange-Act-Assert patterns, AssertJ assertions, and test data builders for maintainability
Targets feature additions, bug fixes, and refactoring workflows with CI commands for Maven and Gradle
SKILL.md
Spring Boot TDD Workflow

TDD guidance for Spring Boot services with 80%+ coverage (unit + integration).

When to Use
New features or endpoints
Bug fixes or refactors
Adding data access logic or security rules
Workflow
Write tests first (they should fail)
Implement minimal code to pass
Refactor with tests green
Enforce coverage (JaCoCo)
Unit Tests (JUnit 5 + Mockito)
@ExtendWith(MockitoExtension.class)
class MarketServiceTest {
  @Mock MarketRepository repo;
  @InjectMocks MarketService service;

  @Test
  void createsMarket() {
    CreateMarketRequest req = new CreateMarketRequest("name", "desc", Instant.now(), List.of("cat"));
    when(repo.save(any())).thenAnswer(inv -> inv.getArgument(0));

    Market result = service.create(req);

    assertThat(result.name()).isEqualTo("name");
    verify(repo).save(any());
  }
}


Patterns:

Arrange-Act-Assert
Avoid partial mocks; prefer explicit stubbing
Use @ParameterizedTest for variants
Web Layer Tests (MockMvc)
@WebMvcTest(MarketController.class)
class MarketControllerTest {
  @Autowired MockMvc mockMvc;
  @MockBean MarketService marketService;

  @Test
  void returnsMarkets() throws Exception {
    when(marketService.list(any())).thenReturn(Page.empty());

    mockMvc.perform(get("/api/markets"))
        .andExpect(status().isOk())
        .andExpect(jsonPath("$.content").isArray());
  }
}

Integration Tests (SpringBootTest)
@SpringBootTest
@AutoConfigureMockMvc
@ActiveProfiles("test")
class MarketIntegrationTest {
  @Autowired MockMvc mockMvc;

  @Test
  void createsMarket() throws Exception {
    mockMvc.perform(post("/api/markets")
        .contentType(MediaType.APPLICATION_JSON)
        .content("""
          {"name":"Test","description":"Desc","endDate":"2030-01-01T00:00:00Z","categories":["general"]}
        """))
      .andExpect(status().isCreated());
  }
}

Persistence Tests (DataJpaTest)
@DataJpaTest
@AutoConfigureTestDatabase(replace = AutoConfigureTestDatabase.Replace.NONE)
@Import(TestContainersConfig.class)
class MarketRepositoryTest {
  @Autowired MarketRepository repo;

  @Test
  void savesAndFinds() {
    MarketEntity entity = new MarketEntity();
    entity.setName("Test");
    repo.save(entity);

    Optional<MarketEntity> found = repo.findByName("Test");
    assertThat(found).isPresent();
  }
}

Testcontainers
Use reusable containers for Postgres/Redis to mirror production
Wire via @DynamicPropertySource to inject JDBC URLs into Spring context
Coverage (JaCoCo)

Maven snippet:

<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <version>0.8.14</version>
  <executions>
    <execution>
      <goals><goal>prepare-agent</goal></goals>
    </execution>
    <execution>
      <id>report</id>
      <phase>verify</phase>
      <goals><goal>report</goal></goals>
    </execution>
  </executions>
</plugin>

Assertions
Prefer AssertJ (assertThat) for readability
For JSON responses, use jsonPath
For exceptions: assertThatThrownBy(...)
Test Data Builders
class MarketBuilder {
  private String name = "Test";
  MarketBuilder withName(String name) { this.name = name; return this; }
  Market build() { return new Market(null, name, MarketStatus.ACTIVE); }
}

CI Commands
Maven: mvn -T 4 test or mvn verify
Gradle: ./gradlew test jacocoTestReport

Remember: Keep tests fast, isolated, and deterministic. Test behavior, not implementation details.

Weekly Installs
3.7K
Repository
affaan-m/everyt…ude-code
GitHub Stars
171.6K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass