---
rating: ⭐⭐
title: nestjs-code-review
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/nestjs-code-review
---

# nestjs-code-review

skills/giuseppe-trisciuoglio/developer-kit/nestjs-code-review
nestjs-code-review
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill nestjs-code-review
SKILL.md
NestJS Code Review
Overview

Provides structured code review for NestJS applications. Findings categorized by severity (Critical, Warning, Suggestion) with actionable recommendations. Delegates to nestjs-code-review-expert agent for deep analysis.

When to Use
"review NestJS code", "NestJS code review", "check my NestJS controller/service"
Before merging pull requests or after implementing new features
Validating NestJS decorators, DI patterns, guard implementations
Architecture validation for NestJS modules and providers
Reviewing DTOs, pipes, interceptors, and database integration (TypeORM, Prisma, Drizzle)
Instructions

Identify Scope: Determine which NestJS files and modules are under review. Use glob and grep to discover controllers, services, modules, guards, interceptors, and pipes in the target area.

Analyze Module Structure: Verify proper module organization — each feature should have its own module with clearly defined imports, controllers, providers, and exports. Check for circular dependencies and proper module boundaries.

Review Dependency Injection: Validate that all injectable services use constructor injection. Check provider scoping (singleton, request, transient) matches the intended lifecycle. Ensure no direct instantiation bypasses the DI container.

Evaluate Controllers: Review HTTP method usage, route naming, status codes, request/response DTOs, validation pipes, and OpenAPI decorators. Confirm controllers are thin — business logic belongs in services.

Assess Services & Business Logic: Check that services encapsulate business logic properly. Verify error handling, transaction management, and proper separation from infrastructure concerns. Look for service methods that are too large or have too many responsibilities.

Check Security: Review guard implementations, authentication/authorization patterns, input validation with class-validator, and protection against common vulnerabilities (injection, XSS, CSRF).

Review Testing: Assess test coverage for controllers, services, guards, and pipes. Verify proper mocking strategies and that tests validate behavior, not implementation details.

Validate Findings (Required checkpoint): Before finalizing, verify each Critical and Warning finding has reproducible evidence (file path, line numbers, exact code snippet) and a concrete, actionable fix. Remove or downgrade findings that are style preferences, overly subjective, or lack concrete remediation.

Produce Review Report: Generate structured report with severity-classified findings (Critical, Warning, Suggestion), positive observations, and prioritized recommendations with code examples.

Examples
Example 1: Reviewing a Controller
// ❌ Bad: Fat controller with business logic and missing validation
@Controller('users')
export class UserController {
  constructor(private readonly userRepo: Repository<User>) {}

  @Post()
  async create(@Body() body: any) {
    const user = this.userRepo.create(body);
    return this.userRepo.save(user);
  }
}

// ✅ Good: Thin controller with proper DTOs, validation, and service delegation
@Controller('users')
@ApiTags('Users')
export class UserController {
  constructor(private readonly userService: UserService) {}

  @Post()
  @HttpCode(HttpStatus.CREATED)
  @ApiOperation({ summary: 'Create a new user' })
  @ApiResponse({ status: 201, type: UserResponseDto })
  async create(
    @Body(ValidationPipe) createUserDto: CreateUserDto,
  ): Promise<UserResponseDto> {
    return this.userService.create(createUserDto);
  }
}

Example 2: Reviewing Dependency Injection
// ❌ Bad: Direct instantiation bypasses DI
@Injectable()
export class OrderService {
  private readonly logger = new Logger();
  private readonly emailService = new EmailService();

  async createOrder(dto: CreateOrderDto) {
    this.emailService.send(dto.email, 'Order created');
  }
}

// ✅ Good: Proper constructor injection
@Injectable()
export class OrderService {
  private readonly logger = new Logger(OrderService.name);

  constructor(
    private readonly orderRepository: OrderRepository,
    private readonly emailService: EmailService,
  ) {}

  async createOrder(dto: CreateOrderDto): Promise<Order> {
    const order = await this.orderRepository.create(dto);
    await this.emailService.send(dto.email, 'Order created');
    return order;
  }
}

Example 3: Reviewing Error Handling
// ❌ Bad: Generic error handling with information leakage
@Get(':id')
async findOne(@Param('id') id: string) {
  try {
    return await this.service.findOne(id);
  } catch (error) {
    throw new HttpException(error.message, 500);
  }
}

// ✅ Good: Domain-specific exceptions with proper HTTP mapping
@Get(':id')
async findOne(@Param('id', ParseUUIDPipe) id: string): Promise<UserResponseDto> {
  const user = await this.userService.findOne(id);
  if (!user) {
    throw new NotFoundException(`User with ID ${id} not found`);
  }
  return user;
}

Example 4: Reviewing Guard Implementation
// ❌ Bad: Authorization logic in controller
@Get('admin/dashboard')
async getDashboard(@Req() req: Request) {
  if (req.user.role !== 'admin') {
    throw new ForbiddenException();
  }
  return this.dashboardService.getData();
}

// ✅ Good: Guard-based authorization with decorator
@Get('admin/dashboard')
@UseGuards(JwtAuthGuard, RolesGuard)
@Roles(Role.ADMIN)
async getDashboard(): Promise<DashboardDto> {
  return this.dashboardService.getData();
}

Example 5: Reviewing Module Organization
// ❌ Bad: Monolithic module with everything
@Module({
  imports: [TypeOrmModule.forFeature([User, Order, Product, Review])],
  controllers: [UserController, OrderController, ProductController],
  providers: [UserService, OrderService, ProductService, ReviewService],
})
export class AppModule {}

// ✅ Good: Feature-based module organization
@Module({
  imports: [UserModule, OrderModule, ProductModule],
})
export class AppModule {}

@Module({
  imports: [TypeOrmModule.forFeature([User])],
  controllers: [UserController],
  providers: [UserService, UserRepository],
  exports: [UserService],
})
export class UserModule {}

Review Output Format

Structure all code review findings as follows:

1. Summary

Brief overview with an overall quality score (1-10) and key observations.

2. Critical Issues (Must Fix)

Issues that could cause security vulnerabilities, data corruption, or production failures.

3. Warnings (Should Fix)

Issues that violate best practices, reduce maintainability, or could lead to bugs.

4. Suggestions (Consider Improving)

Improvements for code readability, performance, or developer experience.

5. Positive Observations

Well-implemented patterns and good practices to acknowledge and encourage.

6. Recommendations

Prioritized next steps with code examples for the most impactful improvements.

Best Practices
Controllers should be thin — delegate all business logic to services
Use DTOs with class-validator for all request/response payloads
Apply ParseUUIDPipe, ParseIntPipe, etc. for parameter validation
Use domain-specific exception classes extending HttpException
Organize code into feature modules with clear boundaries and exports
Prefer constructor injection — never use new for injectable services
Apply guards for authentication and authorization, not inline checks
Use interceptors for cross-cutting concerns (logging, caching, transformation)
Add OpenAPI decorators (@ApiTags, @ApiOperation, @ApiResponse) to all endpoints
Write unit tests for services and integration tests for controllers
Constraints and Warnings
Do not enforce a single ORM — the codebase may use TypeORM, Prisma, Drizzle, or MikroORM
Respect existing project conventions even if they differ from NestJS defaults
Focus on high-confidence issues — avoid false positives on style preferences
When reviewing microservices patterns, consider transport-layer specific constraints
Do not suggest architectural rewrites unless critical issues warrant them
References

See the references/ directory for detailed review checklists and pattern documentation:

references/patterns.md — NestJS best practice patterns with examples
references/anti-patterns.md — Common NestJS anti-patterns to flag during review
references/checklist.md — Comprehensive review checklist organized by area
Weekly Installs
510
Repository
giuseppe-trisci…oper-kit
GitHub Stars
233
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass