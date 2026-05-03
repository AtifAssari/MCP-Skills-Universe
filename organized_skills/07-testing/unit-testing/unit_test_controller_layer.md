---
rating: ⭐⭐
title: unit-test-controller-layer
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/unit-test-controller-layer
---

# unit-test-controller-layer

skills/giuseppe-trisciuoglio/developer-kit/unit-test-controller-layer
unit-test-controller-layer
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill unit-test-controller-layer
Summary

Unit testing REST controllers in isolation with MockMvc and mocked service dependencies.

Covers testing all HTTP methods (GET, POST, PUT, PATCH, DELETE) with status code and response body validation using JsonPath assertions
Includes patterns for request parameter binding, validation errors, exception handling, and content negotiation across different Accept and Content-Type headers
Uses standalone MockMvc setup with Mockito to mock service layer dependencies, keeping tests focused on HTTP handling without integration test overhead
Provides examples for testing request/response headers, path variables, query parameters, and error scenarios (404, 400, 401, 500)
SKILL.md
Unit Testing REST Controllers with MockMvc
Overview

Provides patterns for unit testing @RestController and @Controller classes using MockMvc. Covers request/response handling, HTTP status codes, request parameter binding, validation, content negotiation, response headers, and exception handling with mocked service dependencies.

When to Use

Use for: controller tests, API endpoint testing, Spring MVC tests, mock HTTP requests, unit testing web layer endpoints, verifying REST controllers in isolation.

Instructions
Setup standalone MockMvc: MockMvcBuilders.standaloneSetup(controller) for isolated testing
Mock service dependencies: Use @Mock for all services, @InjectMocks for the controller
Test HTTP methods: GET, POST, PUT, PATCH, DELETE with correct status codes
Validate responses: JsonPath assertions for JSON, content matchers for body
Test validation: Send invalid input, verify 400 status with error details
Test errors: Verify 404, 400, 401, 403, 500 for appropriate conditions
Validate headers: Both request (Authorization) and response headers
Test content negotiation: Different Accept and Content-Type headers
Validation Workflow
Run test → If fails: add .andDo(print()) → Check actual vs expected → Fix assertion

Examples
Maven / Gradle Dependencies
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-test</artifactId>
  <scope>test</scope>
</dependency>

Basic Pattern: GET Endpoint
import static org.mockito.Mockito.*;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@ExtendWith(MockitoExtension.class)
class UserControllerTest {

  @Mock
  private UserService userService;

  @InjectMocks
  private UserController userController;

  private MockMvc mockMvc;

  @BeforeEach
  void setUp() {
    mockMvc = MockMvcBuilders.standaloneSetup(userController).build();
  }

  @Test
  void shouldReturnAllUsers() throws Exception {
    List<UserDto> users = List.of(new UserDto(1L, "Alice"), new UserDto(2L, "Bob"));
    when(userService.getAllUsers()).thenReturn(users);

    mockMvc.perform(get("/api/users"))
      .andExpect(status().isOk())
      .andExpect(jsonPath("$[0].id").value(1))
      .andExpect(jsonPath("$[0].name").value("Alice"));

    verify(userService, times(1)).getAllUsers();
  }

  @Test
  void shouldReturn404WhenUserNotFound() throws Exception {
    when(userService.getUserById(999L))
      .thenThrow(new UserNotFoundException("User not found"));

    mockMvc.perform(get("/api/users/999"))
      .andExpect(status().isNotFound());

    verify(userService).getUserById(999L);
  }
}

POST: Create Resource
@Test
void shouldCreateUserAndReturn201() throws Exception {
  UserDto createdUser = new UserDto(1L, "Alice", "alice@example.com");
  when(userService.createUser(any())).thenReturn(createdUser);

  mockMvc.perform(post("/api/users")
      .contentType("application/json")
      .content("{\"name\":\"Alice\",\"email\":\"alice@example.com\"}"))
    .andExpect(status().isCreated())
    .andExpect(jsonPath("$.id").value(1))
    .andExpect(jsonPath("$.name").value("Alice"));

  verify(userService).createUser(any(UserCreateRequest.class));
}

PUT: Update Resource
@Test
void shouldUpdateUserAndReturn200() throws Exception {
  UserDto updatedUser = new UserDto(1L, "Updated");
  when(userService.updateUser(eq(1L), any())).thenReturn(updatedUser);

  mockMvc.perform(put("/api/users/1")
      .contentType("application/json")
      .content("{\"name\":\"Updated\"}"))
    .andExpect(status().isOk())
    .andExpect(jsonPath("$.name").value("Updated"));

  verify(userService).updateUser(eq(1L), any());
}

DELETE: Remove Resource
@Test
void shouldDeleteUserAndReturn204() throws Exception {
  doNothing().when(userService).deleteUser(1L);

  mockMvc.perform(delete("/api/users/1"))
    .andExpect(status().isNoContent());

  verify(userService).deleteUser(1L);
}

Query Parameters
@Test
void shouldFilterUsersByName() throws Exception {
  when(userService.searchUsers("Alice")).thenReturn(List.of(new UserDto(1L, "Alice")));

  mockMvc.perform(get("/api/users/search").param("name", "Alice"))
    .andExpect(status().isOk())
    .andExpect(jsonPath("$[0].name").value("Alice"));

  verify(userService).searchUsers("Alice");
}

Path Variables
@Test
void shouldGetUserByIdFromPath() throws Exception {
  when(userService.getUserById(123L)).thenReturn(new UserDto(123L, "Alice"));

  mockMvc.perform(get("/api/users/{id}", 123L))
    .andExpect(status().isOk())
    .andExpect(jsonPath("$.id").value(123));
}

Validation Errors (400)
@Test
void shouldReturn400WhenRequestBodyInvalid() throws Exception {
  mockMvc.perform(post("/api/users")
      .contentType("application/json")
      .content("{\"name\":\"\"}"))
    .andExpect(status().isBadRequest())
    .andExpect(jsonPath("$.errors").isArray());
}

Response Headers
@Test
void shouldReturnCustomHeaders() throws Exception {
  when(userService.getAllUsers()).thenReturn(List.of());

  mockMvc.perform(get("/api/users"))
    .andExpect(status().isOk())
    .andExpect(header().exists("X-Total-Count"))
    .andExpect(header().string("X-Total-Count", "0"));
}

Authorization Header
@Test
void shouldRequireAuthorizationHeader() throws Exception {
  mockMvc.perform(get("/api/users"))
    .andExpect(status().isUnauthorized());

  mockMvc.perform(get("/api/users").header("Authorization", "Bearer token"))
    .andExpect(status().isOk());
}

Content Negotiation
@Test
void shouldReturnJsonWhenAcceptHeaderIsJson() throws Exception {
  when(userService.getUserById(1L)).thenReturn(new UserDto(1L, "Alice"));

  mockMvc.perform(get("/api/users/1").accept("application/json"))
    .andExpect(status().isOk())
    .andExpect(content().contentType("application/json"));
}

Best Practices
Use standaloneSetup() for isolated controller testing
Mock service layer — controllers handle HTTP, services handle business logic
Verify mock interactions: verify(service).method(args)
Test happy path AND error scenarios (404, 400, 500)
Use jsonPath() for fluent JSON assertions
One focused assertion per test method
Constraints and Warnings
Controller tests verify HTTP handling only — not full request flow
standaloneSetup() may not support @Validated without full context
JsonPath requires valid JSON in response body
@PreAuthorize/@Secured need additional setup — consider separate security tests
File uploads require MockMultipartFile
References
Spring MockMvc Documentation
Spring Testing Best Practices
Weekly Installs
725
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