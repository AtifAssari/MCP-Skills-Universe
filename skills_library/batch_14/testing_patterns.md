---
title: testing-patterns
url: https://skills.sh/langchain-ai/skills-benchmarks/testing-patterns
---

# testing-patterns

skills/langchain-ai/skills-benchmarks/testing-patterns
testing-patterns
Installation
$ npx skills add https://github.com/langchain-ai/skills-benchmarks --skill testing-patterns
SKILL.md
Testing Patterns

Write effective, maintainable tests using modern patterns.

Test Structure (AAA Pattern)
def test_user_registration():
    # Arrange
    user_data = {"email": "test@example.com", "password": "secure123"}

    # Act
    result = register_user(user_data)

    # Assert
    assert result.success is True
    assert result.user.email == "test@example.com"

Mocking External Services
from unittest.mock import Mock, patch

@patch('services.email.send_email')
def test_sends_welcome_email(mock_send):
    mock_send.return_value = True

    register_user({"email": "test@example.com"})

    mock_send.assert_called_once_with(
        to="test@example.com",
        template="welcome"
    )

Fixtures and Factories
import pytest
from factories import UserFactory

@pytest.fixture
def user():
    return UserFactory.create(role="admin")

@pytest.fixture
def authenticated_client(user):
    client = TestClient(app)
    client.login(user)
    return client

def test_admin_dashboard(authenticated_client):
    response = authenticated_client.get("/admin")
    assert response.status_code == 200

Integration Tests
@pytest.mark.integration
def test_full_checkout_flow(db_session, stripe_mock):
    # Create test data
    user = create_user()
    product = create_product(price=100)

    # Execute flow
    cart = add_to_cart(user, product)
    order = checkout(cart, payment_method="card")

    # Verify
    assert order.status == "completed"
    assert stripe_mock.charges.create.called

Test Coverage Goals
Unit tests: 80%+ coverage
Integration tests: Critical paths
E2E tests: Happy paths only
Weekly Installs
20
Repository
langchain-ai/sk…nchmarks
GitHub Stars
95
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass