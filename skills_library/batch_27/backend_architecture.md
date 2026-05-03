---
title: backend architecture
url: https://skills.sh/exceptionless/exceptionless/backend-architecture
---

# backend architecture

skills/exceptionless/exceptionless/backend-architecture
backend-architecture
Installation
$ npx skills add https://github.com/exceptionless/exceptionless --skill backend-architecture
SKILL.md
Backend Architecture
Project Layering
Exceptionless.Core        → Domain logic, services, repositories, validation
Exceptionless.Insulation  → Infrastructure implementations (Redis, GeoIP, Mail, HealthChecks)
Exceptionless.Web         → ASP.NET Core host, controllers, WebSocket hubs
Exceptionless.Job         → Background job workers


Dependency Direction: Web → Core ← Insulation / Job → Core ← Insulation

Exceptionless.Core
Services (src/Exceptionless.Core/Services/)

UsageService, EventPostService, StackService, OrganizationService, MessageService, SlackService

Repositories

Repositories extend ElasticRepositoryBase<T> with optional IValidator<T> and AppOptions injection. They use Foundatio Parsers for query parsing. See foundatio-repositories skill for query/pagination/patch patterns.

Validation

Two patterns (transitioning to MiniValidator for new code):

FluentValidation — domain models in repositories (src/Exceptionless.Core/Validation/):

public class OrganizationValidator : AbstractValidator<Organization>
{
    public OrganizationValidator(BillingPlans plans)
    {
        RuleFor(o => o.Name).NotEmpty().WithMessage("Please specify a valid name.");
        RuleFor(o => o.PlanId).NotEmpty().WithMessage("Please specify a valid plan id.");
    }
}


MiniValidator — API request models with DataAnnotations (preferred for new code):

public record Login
{
    [Required]
    public required string Email { get; init; }

    [Required, StringLength(100, MinimumLength = 6)]
    public required string Password { get; init; }
}


AutoValidationActionFilter handles API model validation automatically. MiniValidationValidator wraps MiniValidator.TryValidateAsync and throws MiniValidatorException on failure.

Exceptionless.Insulation

Infrastructure only — Configuration/ (YAML), Geo/ (MaxMind), HealthChecks/, Mail/ (MailKit), Redis/.

Authorization

Use AuthorizationRoles constants (NOT string literals):

public static class AuthorizationRoles
{
    public const string ClientPolicy = nameof(ClientPolicy);
    public const string Client = "client";
    public const string UserPolicy = nameof(UserPolicy);
    public const string User = "user";
    public const string GlobalAdminPolicy = nameof(GlobalAdminPolicy);
    public const string GlobalAdmin = "global";
}

// Usage
[Authorize(Policy = AuthorizationRoles.UserPolicy)]
public class OrganizationController : RepositoryApiController<...> { }

[Authorize(Policy = AuthorizationRoles.GlobalAdminPolicy)]
public class AdminController : ExceptionlessApiController { }

Controller Patterns

Most controllers extend RepositoryApiController<TRepository, TModel, TViewModel, TNewModel, TUpdateModel>. Auth/special-case controllers extend ExceptionlessApiController directly.

[Route(API_PREFIX + "/organizations")]
[Authorize(Policy = AuthorizationRoles.UserPolicy)]
public class OrganizationController : RepositoryApiController<IOrganizationRepository, Organization, ViewOrganization, NewOrganization, NewOrganization>
{
    [HttpGet]
    public async Task<ActionResult<IReadOnlyCollection<ViewOrganization>>> GetAllAsync(string? mode = null)
    {
        var organizations = await GetModelsAsync(GetAssociatedOrganizationIds().ToArray());
        return Ok(await MapCollectionAsync<ViewOrganization>(organizations, true));
    }
}

ProblemDetails and Error Handling

Return helpers from ExceptionlessApiController: Ok(), Created(), NoContent(), Unauthorized(), Forbidden(), NotFound(), ValidationProblem(ModelState).

Exceptions auto-convert via ExceptionToProblemDetailsHandler: MiniValidatorException/ValidationException → 422, others → 500.

WebSocket Hubs (NOT SignalR)

Custom WebSocket implementation using Foundatio IMessageBus. MessageBusBroker subscribes to EntityChanged, PlanChanged, UserMembershipChanged and broadcasts to connected WebSocket clients via WebSocketConnectionManager.

Configuration

Uses YAML files (appsettings.yml) + AddCustomEnvironmentVariables(). All config binds to AppOptions with nested options (EmailOptions, AuthOptions, IntercomOptions, SlackOptions, StripeOptions). Inject AppOptions directly — not IOptions<T>.

Weekly Installs
34
Repository
exceptionless/e…tionless
GitHub Stars
2.5K
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass