---
rating: ⭐⭐
title: mercury
url: https://skills.sh/vm0-ai/vm0-skills/mercury
---

# mercury

skills/vm0-ai/vm0-skills/mercury
mercury
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill mercury
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name MERCURY_TOKEN or zero doctor check-connector --url https://api.mercury.com/api/v1/accounts --method GET

Accounts
List All Accounts
curl -s "https://api.mercury.com/api/v1/accounts" --header "Authorization: Bearer $MERCURY_TOKEN"

Get Account by ID

Replace <your-account-id> with the actual account ID:

curl -s "https://api.mercury.com/api/v1/account/<your-account-id>" --header "Authorization: Bearer $MERCURY_TOKEN"

Get Account Cards

Replace <your-account-id> with the actual account ID:

curl -s "https://api.mercury.com/api/v1/account/<your-account-id>/cards" --header "Authorization: Bearer $MERCURY_TOKEN"

Transactions
List Account Transactions

Replace <your-account-id> with the actual account ID:

curl -s "https://api.mercury.com/api/v1/account/<your-account-id>/transactions" --header "Authorization: Bearer $MERCURY_TOKEN"

List Transactions with Filters

Filter by date range, status, or limit. Replace <your-account-id> with the actual account ID:

curl -s "https://api.mercury.com/api/v1/account/<your-account-id>/transactions?limit=50&start=2024-01-01&end=2024-12-31" --header "Authorization: Bearer $MERCURY_TOKEN"

Get Transaction by ID

Replace <your-account-id> and <your-transaction-id> with the actual IDs:

curl -s "https://api.mercury.com/api/v1/account/<your-account-id>/transaction/<your-transaction-id>" --header "Authorization: Bearer $MERCURY_TOKEN"

Transfers
Create Internal Transfer

Transfer funds between your Mercury accounts.

Write to /tmp/mercury_request.json:

{
  "toAccountId": "target-account-id",
  "amount": 100.00,
  "note": "Internal transfer"
}


Then run. Replace <your-account-id> with the actual account ID:

curl -s -X POST "https://api.mercury.com/api/v1/account/<your-account-id>/internal-transfer" --header "Authorization: Bearer $MERCURY_TOKEN" --header "Content-Type: application/json" -d @/tmp/mercury_request.json

Send Money Request

Initiate a money transfer request.

Write to /tmp/mercury_request.json:

{
  "recipientId": "recipient-id",
  "amount": 100.00,
  "paymentMethod": "ach",
  "idempotencyKey": "unique-key-123"
}


Then run. Replace <your-account-id> with the actual account ID:

curl -s -X POST "https://api.mercury.com/api/v1/account/<your-account-id>/send-money" --header "Authorization: Bearer $MERCURY_TOKEN" --header "Content-Type: application/json" -d @/tmp/mercury_request.json

Get Send Money Request Status

Replace <your-request-id> with the actual request ID:

curl -s "https://api.mercury.com/api/v1/request-send-money/<your-request-id>" --header "Authorization: Bearer $MERCURY_TOKEN"

Recipients
List All Recipients
curl -s "https://api.mercury.com/api/v1/recipients" --header "Authorization: Bearer $MERCURY_TOKEN"

Get Recipient by ID

Replace <your-recipient-id> with the actual recipient ID:

curl -s "https://api.mercury.com/api/v1/recipient/<your-recipient-id>" --header "Authorization: Bearer $MERCURY_TOKEN"

Create Recipient

Write to /tmp/mercury_request.json:

{
  "name": "Vendor Name",
  "emails": ["vendor@example.com"],
  "paymentMethod": "ach",
  "electronicRoutingInfo": {
    "accountNumber": "123456789",
    "routingNumber": "021000021",
    "bankName": "Example Bank",
    "electronicAccountType": "businessChecking"
  }
}


Then run:

curl -s -X POST "https://api.mercury.com/api/v1/recipients" --header "Authorization: Bearer $MERCURY_TOKEN" --header "Content-Type: application/json" -d @/tmp/mercury_request.json

Statements
List Account Statements

Replace <your-account-id> with the actual account ID:

curl -s "https://api.mercury.com/api/v1/account/<your-account-id>/statements" --header "Authorization: Bearer $MERCURY_TOKEN"

Download Statement PDF

Replace <your-account-id> and <your-statement-id> with the actual IDs:

curl -s "https://api.mercury.com/api/v1/account/<your-account-id>/statement/<your-statement-id>/pdf" --header "Authorization: Bearer $MERCURY_TOKEN" > statement.pdf

Organization
Get Organization Info
curl -s "https://api.mercury.com/api/v1/organization" --header "Authorization: Bearer $MERCURY_TOKEN"

Treasury
List Treasury Accounts
curl -s "https://api.mercury.com/api/v1/treasury" --header "Authorization: Bearer $MERCURY_TOKEN"

Get Treasury Account by ID

Replace <your-treasury-id> with the actual treasury ID:

curl -s "https://api.mercury.com/api/v1/treasury/<your-treasury-id>" --header "Authorization: Bearer $MERCURY_TOKEN"

List Treasury Transactions

Replace <your-treasury-id> with the actual treasury ID:

curl -s "https://api.mercury.com/api/v1/treasury/<your-treasury-id>/transactions" --header "Authorization: Bearer $MERCURY_TOKEN"

Users
List Users
curl -s "https://api.mercury.com/api/v1/users" --header "Authorization: Bearer $MERCURY_TOKEN"

Credit
List Credit Accounts
curl -s "https://api.mercury.com/api/v1/credit" --header "Authorization: Bearer $MERCURY_TOKEN"

Accounts Receivable
List Customers
curl -s "https://api.mercury.com/api/v1/accounts-receivable/customers" --header "Authorization: Bearer $MERCURY_TOKEN"

Create Customer

Write to /tmp/mercury_request.json:

{
  "name": "Customer Name",
  "email": "customer@example.com"
}


Then run:

curl -s -X POST "https://api.mercury.com/api/v1/accounts-receivable/customers" --header "Authorization: Bearer $MERCURY_TOKEN" --header "Content-Type: application/json" -d @/tmp/mercury_request.json

List Invoices
curl -s "https://api.mercury.com/api/v1/accounts-receivable/invoices" --header "Authorization: Bearer $MERCURY_TOKEN"

Create Invoice

Write to /tmp/mercury_request.json:

{
  "customerId": "customer-id",
  "lineItems": [{"description": "Service", "amount": 500.00}],
  "dueDate": "2024-12-31"
}


Then run:

curl -s -X POST "https://api.mercury.com/api/v1/accounts-receivable/invoices" --header "Authorization: Bearer $MERCURY_TOKEN" --header "Content-Type: application/json" -d @/tmp/mercury_request.json

Download Invoice PDF

Replace <your-invoice-id> with the actual invoice ID:

curl -s "https://api.mercury.com/api/v1/accounts-receivable/invoice/<your-invoice-id>/pdf" --header "Authorization: Bearer $MERCURY_TOKEN" > invoice.pdf

Guidelines
Rate Limits: Mercury may enforce rate limits; implement appropriate backoff strategies for high-volume operations
Idempotency: Use idempotencyKey for transfer operations to prevent duplicate transactions
Security: Never expose API tokens in logs or client-side code
Amounts: All monetary amounts are typically in USD and represented as decimal numbers
Pagination: For large result sets, use limit and offset parameters where supported
API Reference
Documentation: https://docs.mercury.com/reference/getaccount
Dashboard: https://dashboard.mercury.com
Weekly Installs
66
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn