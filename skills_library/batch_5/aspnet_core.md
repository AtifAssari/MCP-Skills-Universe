---
title: aspnet-core
url: https://skills.sh/mindrally/skills/aspnet-core
---

# aspnet-core

skills/mindrally/skills/aspnet-core
aspnet-core
Installation
$ npx skills add https://github.com/mindrally/skills --skill aspnet-core
SKILL.md
ASP.NET Core Development Guidelines

You are an expert in ASP.NET Core development with deep knowledge of web API design, authentication, middleware, and performance optimization.

Project Structure
src/
  Controllers/      # API endpoints
  Models/          # Domain models and DTOs
  Services/        # Business logic
  Data/            # DbContext and repositories
  Middleware/      # Custom middleware
  Extensions/      # Extension methods
  Configuration/   # App configuration
Program.cs
appsettings.json

Controller Design
RESTful Controllers
[ApiController]
[Route("api/[controller]")]
public class ProductsController : ControllerBase
{
    private readonly IProductService _productService;

    public ProductsController(IProductService productService)
    {
        _productService = productService;
    }

    [HttpGet]
    public async Task<ActionResult<IEnumerable<ProductDto>>> GetProducts()
    {
        var products = await _productService.GetAllAsync();
        return Ok(products);
    }

    [HttpGet("{id}")]
    public async Task<ActionResult<ProductDto>> GetProduct(int id)
    {
        var product = await _productService.GetByIdAsync(id);
        if (product == null)
            return NotFound();
        return Ok(product);
    }

    [HttpPost]
    public async Task<ActionResult<ProductDto>> CreateProduct(CreateProductDto dto)
    {
        var product = await _productService.CreateAsync(dto);
        return CreatedAtAction(nameof(GetProduct), new { id = product.Id }, product);
    }
}

Best Practices
Keep controllers thin
Use DTOs for request/response
Return appropriate status codes
Use async/await consistently
Implement proper validation
Middleware
Custom Middleware
public class RequestLoggingMiddleware
{
    private readonly RequestDelegate _next;
    private readonly ILogger<RequestLoggingMiddleware> _logger;

    public RequestLoggingMiddleware(RequestDelegate next, ILogger<RequestLoggingMiddleware> logger)
    {
        _next = next;
        _logger = logger;
    }

    public async Task InvokeAsync(HttpContext context)
    {
        _logger.LogInformation("Request: {Method} {Path}", context.Request.Method, context.Request.Path);
        await _next(context);
        _logger.LogInformation("Response: {StatusCode}", context.Response.StatusCode);
    }
}

Middleware Order
Exception handling
HTTPS redirection
Static files
Routing
CORS
Authentication
Authorization
Custom middleware
Endpoints
Caching
Response Caching
[HttpGet]
[ResponseCache(Duration = 60)]
public async Task<ActionResult<IEnumerable<ProductDto>>> GetProducts()

Memory Caching
public class ProductService : IProductService
{
    private readonly IMemoryCache _cache;

    public async Task<Product?> GetByIdAsync(int id)
    {
        return await _cache.GetOrCreateAsync($"product_{id}", async entry =>
        {
            entry.AbsoluteExpirationRelativeToNow = TimeSpan.FromMinutes(10);
            return await _repository.GetByIdAsync(id);
        });
    }
}

Distributed Caching
Use Redis for multi-server scenarios
Configure in Program.cs
Use IDistributedCache interface
Authentication
JWT Configuration
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(options =>
    {
        options.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true,
            ValidateAudience = true,
            ValidateLifetime = true,
            ValidateIssuerSigningKey = true,
            ValidIssuer = builder.Configuration["Jwt:Issuer"],
            ValidAudience = builder.Configuration["Jwt:Audience"],
            IssuerSigningKey = new SymmetricSecurityKey(
                Encoding.UTF8.GetBytes(builder.Configuration["Jwt:Key"]!))
        };
    });

Token Generation
public string GenerateToken(User user)
{
    var claims = new[]
    {
        new Claim(ClaimTypes.NameIdentifier, user.Id.ToString()),
        new Claim(ClaimTypes.Email, user.Email),
        new Claim(ClaimTypes.Role, user.Role)
    };

    var key = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(_config["Jwt:Key"]!));
    var creds = new SigningCredentials(key, SecurityAlgorithms.HmacSha256);

    var token = new JwtSecurityToken(
        issuer: _config["Jwt:Issuer"],
        audience: _config["Jwt:Audience"],
        claims: claims,
        expires: DateTime.UtcNow.AddHours(1),
        signingCredentials: creds);

    return new JwtSecurityTokenHandler().WriteToken(token);
}

Authorization
Policy-Based Authorization
builder.Services.AddAuthorization(options =>
{
    options.AddPolicy("AdminOnly", policy => policy.RequireRole("Admin"));
    options.AddPolicy("PremiumUser", policy => policy.RequireClaim("Subscription", "Premium"));
});

[Authorize(Policy = "AdminOnly")]
[HttpDelete("{id}")]
public async Task<IActionResult> DeleteProduct(int id)

Error Handling
Global Exception Handler
app.UseExceptionHandler(errorApp =>
{
    errorApp.Run(async context =>
    {
        context.Response.StatusCode = 500;
        context.Response.ContentType = "application/json";

        var error = context.Features.Get<IExceptionHandlerFeature>();
        if (error != null)
        {
            await context.Response.WriteAsJsonAsync(new
            {
                error = "An error occurred",
                detail = app.Environment.IsDevelopment() ? error.Error.Message : null
            });
        }
    });
});

Validation
FluentValidation
public class CreateProductValidator : AbstractValidator<CreateProductDto>
{
    public CreateProductValidator()
    {
        RuleFor(x => x.Name).NotEmpty().MaximumLength(100);
        RuleFor(x => x.Price).GreaterThan(0);
        RuleFor(x => x.Category).NotEmpty();
    }
}

Configuration
Options Pattern
builder.Services.Configure<SmtpSettings>(builder.Configuration.GetSection("Smtp"));

public class EmailService
{
    private readonly SmtpSettings _settings;

    public EmailService(IOptions<SmtpSettings> options)
    {
        _settings = options.Value;
    }
}

Documentation
Swagger/OpenAPI
builder.Services.AddSwaggerGen(c =>
{
    c.SwaggerDoc("v1", new OpenApiInfo { Title = "My API", Version = "v1" });
    c.AddSecurityDefinition("Bearer", new OpenApiSecurityScheme
    {
        Type = SecuritySchemeType.Http,
        Scheme = "bearer",
        BearerFormat = "JWT"
    });
});

Weekly Installs
306
Repository
mindrally/skills
GitHub Stars
88
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass