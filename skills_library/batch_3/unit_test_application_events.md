---
title: unit-test-application-events
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/unit-test-application-events
---

# unit-test-application-events

skills/giuseppe-trisciuoglio/developer-kit/unit-test-application-events
unit-test-application-events
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill unit-test-application-events
Summary

Testing Spring ApplicationEvent publishers and listeners with mocked dependencies and event capture patterns.

Mock ApplicationEventPublisher in unit tests and use ArgumentCaptor to verify published events and their data integrity
Test @EventListener method invocation directly by instantiating listeners and invoking handler methods with captured events
Handle asynchronous event processing with Thread.sleep() or Awaitility to verify async listener completion
Verify listener side effects on mocked dependencies and test error handling in both publishers and listeners
SKILL.md
Unit Testing Application Events
Overview

Provides actionable patterns for testing Spring ApplicationEvent publishers and @EventListener consumers using JUnit 5 and Mockito — without booting the full Spring context.

When to Use
Writing unit tests for event publishers or listeners
Verifying that an event was published with correct payload
Testing @EventListener method invocation and side effects
Testing event propagation through multiple listeners
Validating async event handling (@Async + @EventListener)
Mocking ApplicationEventPublisher in service tests
Instructions
Add test dependencies: spring-boot-starter, JUnit 5, Mockito, AssertJ
Mock ApplicationEventPublisher: use @Mock on the publisher field in the service under test
Capture events with ArgumentCaptor: ArgumentCaptor.forClass(EventType.class) to inspect published payload
Verify listener side effects: invoke listener directly against mocked dependencies
Test async handlers: use Thread.sleep() or Awaitility — then assert the async operation was called
Add validation checkpoints:
After capturing an event, confirm eventCaptor.getValue() is not null before asserting fields
If the listener is not invoked, verify publishEvent() was called with the correct event type
If async assertions fail, increase wait time and check the executor pool is not saturated
Cover error scenarios: assert listeners handle exceptions gracefully
Examples
Maven
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter</artifactId>
</dependency>
<dependency>
  <groupId>org.junit.jupiter</groupId>
  <artifactId>junit-jupiter</artifactId>
  <scope>test</scope>
</dependency>
<dependency>
  <groupId>org.mockito</groupId>
  <artifactId>mockito-core</artifactId>
  <scope>test</scope>
</dependency>
<dependency>
  <groupId>org.assertj</groupId>
  <artifactId>assertj-core</artifactId>
  <scope>test</scope>
</dependency>

Gradle
dependencies {
  implementation("org.springframework.boot:spring-boot-starter")
  testImplementation("org.junit.jupiter:junit-jupiter")
  testImplementation("org.mockito:mockito-core")
  testImplementation("org.assertj:assertj-core")
}

Custom Event and Publisher Test
public class UserCreatedEvent extends ApplicationEvent {
  private final User user;

  public UserCreatedEvent(Object source, User user) {
    super(source);
    this.user = user;
  }

  public User getUser() { return user; }
}

@Service
public class UserService {
  private final ApplicationEventPublisher eventPublisher;
  private final UserRepository userRepository;

  public UserService(ApplicationEventPublisher eventPublisher, UserRepository userRepository) {
    this.eventPublisher = eventPublisher;
    this.userRepository = userRepository;
  }

  public User createUser(String name, String email) {
    User savedUser = userRepository.save(new User(name, email));
    eventPublisher.publishEvent(new UserCreatedEvent(this, savedUser));
    return savedUser;
  }
}

Unit Test for Event Publishing
@ExtendWith(MockitoExtension.class)
class UserServiceEventTest {

  @Mock
  private ApplicationEventPublisher eventPublisher;

  @Mock
  private UserRepository userRepository;

  @InjectMocks
  private UserService userService;

  @Test
  void shouldPublishUserCreatedEvent() {
    User newUser = new User(1L, "Alice", "alice@example.com");
    when(userRepository.save(any(User.class))).thenReturn(newUser);

    ArgumentCaptor<UserCreatedEvent> eventCaptor = ArgumentCaptor.forClass(UserCreatedEvent.class);

    userService.createUser("Alice", "alice@example.com");

    verify(eventPublisher).publishEvent(eventCaptor.capture());
    assertThat(eventCaptor.getValue().getUser()).isEqualTo(newUser);
  }
}

Listener Direct Test
@Component
public class UserEventListener {
  private final EmailService emailService;

  public UserEventListener(EmailService emailService) { this.emailService = emailService; }

  @EventListener
  public void onUserCreated(UserCreatedEvent event) {
    emailService.sendWelcomeEmail(event.getUser().getEmail());
  }
}

class UserEventListenerTest {

  @Test
  void shouldSendWelcomeEmailOnUserCreated() {
    EmailService emailService = mock(EmailService.class);
    UserEventListener listener = new UserEventListener(emailService);

    User user = new User(1L, "Alice", "alice@example.com");
    listener.onUserCreated(new UserCreatedEvent(this, user));

    verify(emailService).sendWelcomeEmail("alice@example.com");
  }

  @Test
  void shouldNotThrowWhenEmailServiceFails() {
    EmailService emailService = mock(EmailService.class);
    doThrow(new RuntimeException("down")).when(emailService).sendWelcomeEmail(any());

    UserEventListener listener = new UserEventListener(emailService);
    User user = new User(1L, "Alice", "alice@example.com");

    assertThatCode(() -> listener.onUserCreated(new UserCreatedEvent(this, user)))
      .doesNotThrowAnyException();
  }
}

Async Listener Test
@Component
public class AsyncEventListener {
  private final SlowService slowService;

  @EventListener
  @Async
  public void onUserCreatedAsync(UserCreatedEvent event) {
    slowService.processUser(event.getUser());
  }
}

class AsyncEventListenerTest {

  @Test
  void shouldProcessEventAsynchronously() throws Exception {
    SlowService slowService = mock(SlowService.class);
    AsyncEventListener listener = new AsyncEventListener(slowService);

    User user = new User(1L, "Alice", "alice@example.com");
    listener.onUserCreatedAsync(new UserCreatedEvent(this, user));

    Thread.sleep(200); // checkpoint: allow async executor to run
    verify(slowService).processUser(user);
  }
}

Best Practices
Mock ApplicationEventPublisher — never let it post to a real context in unit tests
Capture events with ArgumentCaptor and assert field-level equality, not just type
Test listeners in isolation: construct them with mocked dependencies and call the handler method directly
Cover error paths: listeners must not propagate exceptions to publishers
Async listeners: prefer Awaitility over Thread.sleep() for deterministic waits
Keep events immutable and serializable — test both if events cross JVM boundaries
Constraints and Warnings
Do not test Spring's own event infrastructure — focus on your business logic and event payload
@Async requires @EnableAsync — tests using Thread.sleep may still pass even if the async proxy is not wired in the test; use a mock verify instead
Spring does not guarantee listener order — do not write tests that depend on execution sequence unless you add @Order
Avoid Thread.sleep() in CI environments — it makes tests flaky under load; replace with Awaitility .atMost() blocks
Events crossing JVM boundaries need serialization tests — null fields in remote listeners often mean missing Serializable
References
Spring ApplicationEvent Javadoc
ApplicationEventPublisher Javadoc
@EventListener Javadoc
Weekly Installs
695
Repository
giuseppe-trisci…oper-kit
GitHub Stars
233
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass