---
title: telnyx-webrtc-python
url: https://skills.sh/team-telnyx/skills/telnyx-webrtc-python
---

# telnyx-webrtc-python

skills/team-telnyx/skills/telnyx-webrtc-python
telnyx-webrtc-python
Installation
$ npx skills add https://github.com/team-telnyx/skills --skill telnyx-webrtc-python
SKILL.md
Telnyx Webrtc - Python
Installation
pip install telnyx

Setup
import os
from telnyx import Telnyx

client = Telnyx(
    api_key=os.environ.get("TELNYX_API_KEY"),  # This is the default and can be omitted
)


All examples below assume client is already initialized as shown above.

Error Handling

All API calls can fail with network errors, rate limits (429), validation errors (422), or authentication errors (401). Always handle errors in production code:

import telnyx

try:
    result = client.messages.send(to="+13125550001", from_="+13125550002", text="Hello")
except telnyx.APIConnectionError:
    print("Network error — check connectivity and retry")
except telnyx.RateLimitError:
    # 429: rate limited — wait and retry with exponential backoff
    import time
    time.sleep(1)  # Check Retry-After header for actual delay
except telnyx.APIStatusError as e:
    print(f"API error {e.status_code}: {e.message}")
    if e.status_code == 422:
        print("Validation error — check required fields and formats")


Common error codes: 401 invalid API key, 403 insufficient permissions, 404 resource not found, 422 validation error (check field formats), 429 rate limited (retry with exponential backoff).

Important Notes
Pagination: List methods return an auto-paginating iterator. Use for item in page_result: to iterate through all pages automatically.
List mobile push credentials

GET /mobile_push_credentials

page = client.mobile_push_credentials.list()
page = page.data[0]
print(page.id)


Returns: alias (string), certificate (string), created_at (date-time), id (string), private_key (string), project_account_json_file (object), record_type (string), type (string), updated_at (date-time)

Creates a new mobile push credential

POST /mobile_push_credentials — Required: type, certificate, private_key, alias

push_credential_response = client.mobile_push_credentials.create(
    create_mobile_push_credential_request={
        "alias": "LucyIosCredential",
        "certificate": "-----BEGIN CERTIFICATE----- MIIGVDCCBTKCAQEAsNlRJVZn9ZvXcECQm65czs... -----END CERTIFICATE-----",
        "private_key": "-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAsNlRJVZn9ZvXcECQm65czs... -----END RSA PRIVATE KEY-----",
        "type": "ios",
    },
)
print(push_credential_response.data)


Returns: alias (string), certificate (string), created_at (date-time), id (string), private_key (string), project_account_json_file (object), record_type (string), type (string), updated_at (date-time)

Retrieves a mobile push credential

Retrieves mobile push credential based on the given push_credential_id

GET /mobile_push_credentials/{push_credential_id}

push_credential_response = client.mobile_push_credentials.retrieve(
    "0ccc7b76-4df3-4bca-a05a-3da1ecc389f0",
)
print(push_credential_response.data)


Returns: alias (string), certificate (string), created_at (date-time), id (string), private_key (string), project_account_json_file (object), record_type (string), type (string), updated_at (date-time)

Deletes a mobile push credential

Deletes a mobile push credential based on the given push_credential_id

DELETE /mobile_push_credentials/{push_credential_id}

client.mobile_push_credentials.delete(
    "0ccc7b76-4df3-4bca-a05a-3da1ecc389f0",
)

List all credentials

List all On-demand Credentials.

GET /telephony_credentials

page = client.telephony_credentials.list()
page = page.data[0]
print(page.id)


Returns: created_at (string), expired (boolean), expires_at (string), id (string), name (string), record_type (string), resource_id (string), sip_password (string), sip_username (string), updated_at (string), user_id (string)

Create a credential

Create a credential.

POST /telephony_credentials — Required: connection_id

Optional: expires_at (string), name (string), tag (string)

telephony_credential = client.telephony_credentials.create(
    connection_id="1234567890",
)
print(telephony_credential.data)


Returns: created_at (string), expired (boolean), expires_at (string), id (string), name (string), record_type (string), resource_id (string), sip_password (string), sip_username (string), updated_at (string), user_id (string)

Get a credential

Get the details of an existing On-demand Credential.

GET /telephony_credentials/{id}

telephony_credential = client.telephony_credentials.retrieve(
    "id",
)
print(telephony_credential.data)


Returns: created_at (string), expired (boolean), expires_at (string), id (string), name (string), record_type (string), resource_id (string), sip_password (string), sip_username (string), updated_at (string), user_id (string)

Update a credential

Update an existing credential.

PATCH /telephony_credentials/{id}

Optional: connection_id (string), expires_at (string), name (string), tag (string)

telephony_credential = client.telephony_credentials.update(
    id="550e8400-e29b-41d4-a716-446655440000",
)
print(telephony_credential.data)


Returns: created_at (string), expired (boolean), expires_at (string), id (string), name (string), record_type (string), resource_id (string), sip_password (string), sip_username (string), updated_at (string), user_id (string)

Delete a credential

Delete an existing credential.

DELETE /telephony_credentials/{id}

telephony_credential = client.telephony_credentials.delete(
    "id",
)
print(telephony_credential.data)


Returns: created_at (string), expired (boolean), expires_at (string), id (string), name (string), record_type (string), resource_id (string), sip_password (string), sip_username (string), updated_at (string), user_id (string)

Weekly Installs
32
Repository
team-telnyx/skills
GitHub Stars
171
First Seen
Feb 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail