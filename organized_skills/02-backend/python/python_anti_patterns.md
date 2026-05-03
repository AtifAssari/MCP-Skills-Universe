---
rating: ⭐⭐⭐
title: python-anti-patterns
url: https://skills.sh/wshobson/agents/python-anti-patterns
---

# python-anti-patterns

skills/wshobson/agents/python-anti-patterns
python-anti-patterns
Installation
$ npx skills add https://github.com/wshobson/agents --skill python-anti-patterns
Summary

Common Python anti-patterns to catch during code review and debugging.

Covers 14+ anti-patterns across infrastructure, architecture, error handling, resources, type safety, and testing with before/after code examples
Includes a quick review checklist and summary table for fast reference during code reviews
Focuses on practical fixes: centralized retry logic, DTOs, repository pattern, specific exception handling, and async-native libraries
Emphasizes validation at API boundaries, context managers for resources, and comprehensive test coverage beyond happy paths
SKILL.md
Python Anti-Patterns Checklist

A reference checklist of common mistakes and anti-patterns in Python code. Review this before finalizing implementations to catch issues early.

When to Use This Skill
Reviewing code before merge
Debugging mysterious issues
Teaching or learning Python best practices
Establishing team coding standards
Refactoring legacy code

Note: This skill focuses on what to avoid. For guidance on positive patterns and architecture, see the python-design-patterns skill.

Infrastructure Anti-Patterns
Scattered Timeout/Retry Logic
# BAD: Timeout logic duplicated everywhere
def fetch_user(user_id):
    try:
        return requests.get(url, timeout=30)
    except Timeout:
        logger.warning("Timeout fetching user")
        return None

def fetch_orders(user_id):
    try:
        return requests.get(url, timeout=30)
    except Timeout:
        logger.warning("Timeout fetching orders")
        return None


Fix: Centralize in decorators or client wrappers.

# GOOD: Centralized retry logic
@retry(stop=stop_after_attempt(3), wait=wait_exponential())
def http_get(url: str) -> Response:
    return requests.get(url, timeout=30)

Double Retry
# BAD: Retrying at multiple layers
@retry(max_attempts=3)  # Application retry
def call_service():
    return client.request()  # Client also has retry configured!


Fix: Retry at one layer only. Know your infrastructure's retry behavior.

Hard-Coded Configuration
# BAD: Secrets and config in code
DB_HOST = "prod-db.example.com"
API_KEY = "sk-12345"

def connect():
    return psycopg.connect(f"host={DB_HOST}...")


Fix: Use environment variables with typed settings.

# GOOD
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_host: str = Field(alias="DB_HOST")
    api_key: str = Field(alias="API_KEY")

settings = Settings()

Architecture Anti-Patterns
Exposed Internal Types
# BAD: Leaking ORM model to API
@app.get("/users/{id}")
def get_user(id: str) -> UserModel:  # SQLAlchemy model
    return db.query(UserModel).get(id)


Fix: Use DTOs/response models.

# GOOD
@app.get("/users/{id}")
def get_user(id: str) -> UserResponse:
    user = db.query(UserModel).get(id)
    return UserResponse.from_orm(user)

Mixed I/O and Business Logic
# BAD: SQL embedded in business logic
def calculate_discount(user_id: str) -> float:
    user = db.query("SELECT * FROM users WHERE id = ?", user_id)
    orders = db.query("SELECT * FROM orders WHERE user_id = ?", user_id)
    # Business logic mixed with data access
    if len(orders) > 10:
        return 0.15
    return 0.0


Fix: Repository pattern. Keep business logic pure.

# GOOD
def calculate_discount(user: User, orders: list[Order]) -> float:
    # Pure business logic, easily testable
    if len(orders) > 10:
        return 0.15
    return 0.0

Error Handling Anti-Patterns
Bare Exception Handling
# BAD: Swallowing all exceptions
try:
    process()
except Exception:
    pass  # Silent failure - bugs hidden forever


Fix: Catch specific exceptions. Log or handle appropriately.

# GOOD
try:
    process()
except ConnectionError as e:
    logger.warning("Connection failed, will retry", error=str(e))
    raise
except ValueError as e:
    logger.error("Invalid input", error=str(e))
    raise BadRequestError(str(e))

Ignored Partial Failures
# BAD: Stops on first error
def process_batch(items):
    results = []
    for item in items:
        result = process(item)  # Raises on error - batch aborted
        results.append(result)
    return results


Fix: Capture both successes and failures.

# GOOD
def process_batch(items) -> BatchResult:
    succeeded = {}
    failed = {}
    for idx, item in enumerate(items):
        try:
            succeeded[idx] = process(item)
        except Exception as e:
            failed[idx] = e
    return BatchResult(succeeded, failed)

Missing Input Validation
# BAD: No validation
def create_user(data: dict):
    return User(**data)  # Crashes deep in code on bad input


Fix: Validate early at API boundaries.

# GOOD
def create_user(data: dict) -> User:
    validated = CreateUserInput.model_validate(data)
    return User.from_input(validated)

Resource Anti-Patterns
Unclosed Resources
# BAD: File never closed
def read_file(path):
    f = open(path)
    return f.read()  # What if this raises?


Fix: Use context managers.

# GOOD
def read_file(path):
    with open(path) as f:
        return f.read()

Blocking in Async
# BAD: Blocks the entire event loop
async def fetch_data():
    time.sleep(1)  # Blocks everything!
    response = requests.get(url)  # Also blocks!


Fix: Use async-native libraries.

# GOOD
async def fetch_data():
    await asyncio.sleep(1)
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

Type Safety Anti-Patterns
Missing Type Hints
# BAD: No types
def process(data):
    return data["value"] * 2


Fix: Annotate all public functions.

# GOOD
def process(data: dict[str, int]) -> int:
    return data["value"] * 2

Untyped Collections
# BAD: Generic list without type parameter
def get_users() -> list:
    ...


Fix: Use type parameters.

# GOOD
def get_users() -> list[User]:
    ...

Testing Anti-Patterns
Only Testing Happy Paths
# BAD: Only tests success case
def test_create_user():
    user = service.create_user(valid_data)
    assert user.id is not None


Fix: Test error conditions and edge cases.

# GOOD
def test_create_user_success():
    user = service.create_user(valid_data)
    assert user.id is not None

def test_create_user_invalid_email():
    with pytest.raises(ValueError, match="Invalid email"):
        service.create_user(invalid_email_data)

def test_create_user_duplicate_email():
    service.create_user(valid_data)
    with pytest.raises(ConflictError):
        service.create_user(valid_data)

Over-Mocking
# BAD: Mocking everything
def test_user_service():
    mock_repo = Mock()
    mock_cache = Mock()
    mock_logger = Mock()
    mock_metrics = Mock()
    # Test doesn't verify real behavior


Fix: Use integration tests for critical paths. Mock only external services.

Quick Review Checklist

Before finalizing code, verify:

 No scattered timeout/retry logic (centralized)
 No double retry (app + infrastructure)
 No hard-coded configuration or secrets
 No exposed internal types (ORM models, protobufs)
 No mixed I/O and business logic
 No bare except Exception: pass
 No ignored partial failures in batches
 No missing input validation
 No unclosed resources (using context managers)
 No blocking calls in async code
 All public functions have type hints
 Collections have type parameters
 Error paths are tested
 Edge cases are covered
Common Fixes Summary
Anti-Pattern	Fix
Scattered retry logic	Centralized decorators
Hard-coded config	Environment variables + pydantic-settings
Exposed ORM models	DTO/response schemas
Mixed I/O + logic	Repository pattern
Bare except	Catch specific exceptions
Batch stops on error	Return BatchResult with successes/failures
No validation	Validate at boundaries with Pydantic
Unclosed resources	Context managers
Blocking in async	Async-native libraries
Missing types	Type annotations on all public APIs
Only happy path tests	Test errors and edge cases
Weekly Installs
6.1K
Repository
wshobson/agents
GitHub Stars
34.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass