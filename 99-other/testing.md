---
title: testing
url: https://skills.sh/nguyenhuuca/assessment/testing
---

# testing

skills/nguyenhuuca/assessment/testing
testing
Installation
$ npx skills add https://github.com/nguyenhuuca/assessment --skill testing
SKILL.md
Testing Software
MCP Tools

Chrome DevTools (E2E testing):

Automate user flows in real browser
Capture screenshots for visual regression
Run Lighthouse for accessibility testing
Profile performance during test runs
Testing Pyramid
Unit Tests (Many): Fast, isolated, test single units
Integration Tests (Some): Test component interactions
E2E Tests (Few): Test complete user flows — use Chrome DevTools
Workflows
 Analyze: Use Glob and Grep to identify untested code
 Unit Tests: Cover all public functions
 Edge Cases: Test boundaries and error conditions
 Integration: Test external dependencies
 E2E: Use Chrome DevTools for browser automation
 Regression: Add test for each bug fix
Test Quality Standards
Deterministic

Tests must produce the same result every time.

Isolated

Tests should not depend on each other or shared state.

Clear

Test names should describe the behavior being tested.

Test Patterns
Arrange-Act-Assert (AAA) (Java + JUnit 5)
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    @Mock
    private EmailService emailService;

    @InjectMocks
    private UserService userService;

    @Test
    void registerUser_ValidEmail_SendsWelcomeEmail() {
        // Arrange
        String email = "test@example.com";
        ArgumentCaptor<Email> emailCaptor = ArgumentCaptor.forClass(Email.class);

        // Act
        userService.register(email);

        // Assert
        verify(emailService).send(emailCaptor.capture());
        Email sentEmail = emailCaptor.getValue();
        assertThat(sentEmail.getTo()).isEqualTo("test@example.com");
        assertThat(sentEmail.getSubject()).isEqualTo("Welcome!");
    }
}

E2E Testing with Chrome DevTools
// Use Chrome DevTools MCP for browser automation
// - Navigate to pages
// - Fill forms and click buttons
// - Capture screenshots for visual regression
// - Run Lighthouse accessibility audits
// - Check console for errors

Commands (Java/Maven)
# Run unit tests
mvn test

# Run tests with coverage
mvn verify

# Run specific test class
mvn test -Dtest=UserServiceTest

# Run specific test method
mvn test -Dtest=UserServiceTest#registerUser_ValidEmail_SendsWelcomeEmail

# Generate coverage report
mvn jacoco:report

# View coverage report
open target/site/jacoco/index.html

Finding Untested Code

Use Glob and Grep to identify gaps:

Use Glob to find all source files and test files
Check which source files have corresponding test files
Use Grep to see if functions are referenced in tests
Weekly Installs
11
Repository
nguyenhuuca/assessment
GitHub Stars
24
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass