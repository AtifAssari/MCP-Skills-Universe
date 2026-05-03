---
rating: ⭐⭐
title: api-conventions
url: https://skills.sh/mx-space/core/api-conventions
---

# api-conventions

skills/mx-space/core/api-conventions
api-conventions
Installation
$ npx skills add https://github.com/mx-space/core --skill api-conventions
SKILL.md
MX Space API Design Conventions
Controller Decorators
// Use @ApiController instead of @Controller
// Dev environment has no prefix, production auto-adds /api/v{version} prefix
@ApiController('posts')  // ✓
@Controller('posts')     // ✗

Authentication
// Endpoints requiring login
@Auth()
async create() {}

// Optional auth (get current user status)
async get(@IsAuthenticated() isAuth: boolean) {}

// Get current user
async get(@CurrentUser() user: UserModel) {}

Response Transformation

ResponseInterceptor automatically handles response format:

Return Type	Transformed Result
Array	{ data: [...] }
Object	Returned directly
undefined	204 No Content
@Paginator	{ data: [...], pagination: {...} }
@Bypass	Returned as-is, skips transformation

JSONTransformInterceptor converts all fields to snake_case:

createdAt → created_at
categoryId → category_id
Pagination
@Get('/')
@HTTPDecorators.Paginator  // Required decorator
async list(@Query() query: PagerDto) {
  // Must return mongoose.PaginateResult
  return this.model.paginate({}, {
    page: query.page,
    limit: query.size,
    sort: { created: -1 },
  })
}

Parameter Validation
// Path parameters
@Get('/:id')
async get(@Param() params: MongoIdDto) {
  return this.service.findById(params.id)
}

// Query parameters
@Get('/')
async list(@Query() query: PagerDto) {}

// Request body
@Post('/')
async create(@Body() body: CreateDto) {}

HTTP Methods
Method	Purpose	Status Code
GET	Retrieve resource	200
POST	Create resource	201
PUT	Full update	200
PATCH	Partial update	200
DELETE	Delete resource	204
Error Handling
import { BusinessException } from '~/common/exceptions/biz.exception'
import { ErrorCodeEnum } from '~/constants/error-code.constant'

// Business errors
throw new BusinessException(ErrorCodeEnum.PostNotFound)
throw new BusinessException(ErrorCodeEnum.SlugNotAvailable, slug)

// HTTP errors
throw new BadRequestException('Invalid input')
throw new NotFoundException('Resource not found')
throw new UnauthorizedException('Not logged in')

Idempotency
// Add idempotency protection for create operations
@Post('/')
@HTTPDecorators.Idempotence()
async create() {}

// Custom idempotency key
@HTTPDecorators.Idempotence({ key: 'custom-key' })

Caching
// Disable cache
@Get('/')
@HttpCache.disable
async list() {}

// Custom cache
@HttpCache({ ttl: 60, key: 'my-key' })
async get() {}

Weekly Installs
33
Repository
mx-space/core
GitHub Stars
518
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass