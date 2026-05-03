---
title: telnyx-account-access-javascript
url: https://skills.sh/team-telnyx/skills/telnyx-account-access-javascript
---

# telnyx-account-access-javascript

skills/team-telnyx/skills/telnyx-account-access-javascript
telnyx-account-access-javascript
Installation
$ npx skills add https://github.com/team-telnyx/skills --skill telnyx-account-access-javascript
SKILL.md
Telnyx Account Access - JavaScript
Installation
npm install telnyx

Setup
import Telnyx from 'telnyx';

const client = new Telnyx({
  apiKey: process.env['TELNYX_API_KEY'], // This is the default and can be omitted
});


All examples below assume client is already initialized as shown above.

Error Handling

All API calls can fail with network errors, rate limits (429), validation errors (422), or authentication errors (401). Always handle errors in production code:

try {
  const result = await client.messages.send({ to: '+13125550001', from: '+13125550002', text: 'Hello' });
} catch (err) {
  if (err instanceof Telnyx.APIConnectionError) {
    console.error('Network error — check connectivity and retry');
  } else if (err instanceof Telnyx.RateLimitError) {
    // 429: rate limited — wait and retry with exponential backoff
    const retryAfter = err.headers?.['retry-after'] || 1;
    await new Promise(r => setTimeout(r, retryAfter * 1000));
  } else if (err instanceof Telnyx.APIError) {
    console.error(`API error ${err.status}: ${err.message}`);
    if (err.status === 422) {
      console.error('Validation error — check required fields and formats');
    }
  }
}


Common error codes: 401 invalid API key, 403 insufficient permissions, 404 resource not found, 422 validation error (check field formats), 429 rate limited (retry with exponential backoff).

Important Notes
Pagination: List methods return an auto-paginating iterator. Use for await (const item of result) { ... } to iterate through all pages automatically.
List all Access IP Addresses

GET /access_ip_address

// Automatically fetches more pages as needed.
for await (const accessIPAddressResponse of client.accessIPAddress.list()) {
  console.log(accessIPAddressResponse.id);
}


Returns: created_at (date-time), description (string), id (string), ip_address (string), source (string), status (enum: pending, added), updated_at (date-time), user_id (string)

Create new Access IP Address

POST /access_ip_address — Required: ip_address

Optional: description (string)

const accessIPAddressResponse = await client.accessIPAddress.create({ ip_address: 'ip_address' });

console.log(accessIPAddressResponse.id);


Returns: created_at (date-time), description (string), id (string), ip_address (string), source (string), status (enum: pending, added), updated_at (date-time), user_id (string)

Retrieve an access IP address

GET /access_ip_address/{access_ip_address_id}

const accessIPAddressResponse = await client.accessIPAddress.retrieve('access_ip_address_id');

console.log(accessIPAddressResponse.id);


Returns: created_at (date-time), description (string), id (string), ip_address (string), source (string), status (enum: pending, added), updated_at (date-time), user_id (string)

Delete access IP address

DELETE /access_ip_address/{access_ip_address_id}

const accessIPAddressResponse = await client.accessIPAddress.delete('access_ip_address_id');

console.log(accessIPAddressResponse.id);


Returns: created_at (date-time), description (string), id (string), ip_address (string), source (string), status (enum: pending, added), updated_at (date-time), user_id (string)

List all addresses

Returns a list of your addresses.

GET /addresses

// Automatically fetches more pages as needed.
for await (const address of client.addresses.list()) {
  console.log(address.id);
}


Returns: address_book (boolean), administrative_area (string), borough (string), business_name (string), country_code (string), created_at (string), customer_reference (string), extended_address (string), first_name (string), id (string), last_name (string), locality (string), neighborhood (string), phone_number (string), postal_code (string), record_type (string), street_address (string), updated_at (string), validate_address (boolean)

Creates an address

Creates an address.

POST /addresses — Required: first_name, last_name, business_name, street_address, locality, country_code

Optional: address_book (boolean), administrative_area (string), borough (string), customer_reference (string), extended_address (string), neighborhood (string), phone_number (string), postal_code (string), validate_address (boolean)

const address = await client.addresses.create({
  business_name: "Toy-O'Kon",
  country_code: 'US',
  first_name: 'Alfred',
  last_name: 'Foster',
  locality: 'Austin',
  street_address: '600 Congress Avenue',
});

console.log(address.data);


Returns: address_book (boolean), administrative_area (string), borough (string), business_name (string), country_code (string), created_at (string), customer_reference (string), extended_address (string), first_name (string), id (string), last_name (string), locality (string), neighborhood (string), phone_number (string), postal_code (string), record_type (string), street_address (string), updated_at (string), validate_address (boolean)

Validate an address

Validates an address for emergency services.

POST /addresses/actions/validate — Required: country_code, street_address, postal_code

Optional: administrative_area (string), extended_address (string), locality (string)

const response = await client.addresses.actions.validate({
  country_code: 'US',
  postal_code: '78701',
  street_address: '600 Congress Avenue',
});

console.log(response.data);


Returns: errors (array[object]), record_type (string), result (enum: valid, invalid), suggested (object)

Retrieve an address

Retrieves the details of an existing address.

GET /addresses/{id}

const address = await client.addresses.retrieve('550e8400-e29b-41d4-a716-446655440000');

console.log(address.data);


Returns: address_book (boolean), administrative_area (string), borough (string), business_name (string), country_code (string), created_at (string), customer_reference (string), extended_address (string), first_name (string), id (string), last_name (string), locality (string), neighborhood (string), phone_number (string), postal_code (string), record_type (string), street_address (string), updated_at (string), validate_address (boolean)

Deletes an address

Deletes an existing address.

DELETE /addresses/{id}

const address = await client.addresses.delete('550e8400-e29b-41d4-a716-446655440000');

console.log(address.data);


Returns: address_book (boolean), administrative_area (string), borough (string), business_name (string), country_code (string), created_at (string), customer_reference (string), extended_address (string), first_name (string), id (string), last_name (string), locality (string), neighborhood (string), phone_number (string), postal_code (string), record_type (string), street_address (string), updated_at (string), validate_address (boolean)

Accepts this address suggestion as a new emergency address for Operator Connect and finishes the uploads of the numbers associated with it to Microsoft.

POST /addresses/{id}/actions/accept_suggestions

Optional: id (string)

const response = await client.addresses.actions.acceptSuggestions(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(response.data);


Returns: accepted (boolean), id (uuid), record_type (enum: address_suggestion)

List all SSO authentication providers

Returns a list of your SSO authentication providers.

GET /authentication_providers

// Automatically fetches more pages as needed.
for await (const authenticationProvider of client.authenticationProviders.list()) {
  console.log(authenticationProvider.id);
}


Returns: activated_at (date-time), active (boolean), created_at (date-time), id (uuid), name (string), organization_id (uuid), record_type (string), settings (object), short_name (string), updated_at (date-time)

Creates an authentication provider

Creates an authentication provider.

POST /authentication_providers — Required: name, short_name, settings

Optional: active (boolean), settings_url (uri)

const authenticationProvider = await client.authenticationProviders.create({
  name: 'Okta',
  settings: {
    idp_cert_fingerprint: '13:38:C7:BB:C9:FF:4A:70:38:3A:E3:D9:5C:CD:DB:2E:50:1E:80:A7',
    idp_entity_id: 'https://myorg.myidp.com/saml/metadata',
    idp_sso_target_url: 'https://myorg.myidp.com/trust/saml2/http-post/sso',
  },
  short_name: 'myorg',
});

console.log(authenticationProvider.data);


Returns: activated_at (date-time), active (boolean), created_at (date-time), id (uuid), name (string), organization_id (uuid), record_type (string), settings (object), short_name (string), updated_at (date-time)

Retrieve an authentication provider

Retrieves the details of an existing authentication provider.

GET /authentication_providers/{id}

const authenticationProvider = await client.authenticationProviders.retrieve('550e8400-e29b-41d4-a716-446655440000');

console.log(authenticationProvider.data);


Returns: activated_at (date-time), active (boolean), created_at (date-time), id (uuid), name (string), organization_id (uuid), record_type (string), settings (object), short_name (string), updated_at (date-time)

Update an authentication provider

Updates settings of an existing authentication provider.

PATCH /authentication_providers/{id}

Optional: active (boolean), name (string), settings (object), settings_url (uri), short_name (string)

const authenticationProvider = await client.authenticationProviders.update('id', {
  active: true,
  name: 'Okta',
  settings: {
    idp_entity_id: 'https://myorg.myidp.com/saml/metadata',
    idp_sso_target_url: 'https://myorg.myidp.com/trust/saml2/http-post/sso',
    idp_cert_fingerprint: '13:38:C7:BB:C9:FF:4A:70:38:3A:E3:D9:5C:CD:DB:2E:50:1E:80:A7',
    idp_cert_fingerprint_algorithm: 'sha1',
  },
  short_name: 'myorg',
});

console.log(authenticationProvider.data);


Returns: activated_at (date-time), active (boolean), created_at (date-time), id (uuid), name (string), organization_id (uuid), record_type (string), settings (object), short_name (string), updated_at (date-time)

Deletes an authentication provider

Deletes an existing authentication provider.

DELETE /authentication_providers/{id}

const authenticationProvider = await client.authenticationProviders.delete('550e8400-e29b-41d4-a716-446655440000');

console.log(authenticationProvider.data);


Returns: activated_at (date-time), active (boolean), created_at (date-time), id (uuid), name (string), organization_id (uuid), record_type (string), settings (object), short_name (string), updated_at (date-time)

List all billing groups

GET /billing_groups

// Automatically fetches more pages as needed.
for await (const billingGroup of client.billingGroups.list()) {
  console.log(billingGroup.id);
}


Returns: created_at (date-time), deleted_at (date-time), id (uuid), name (string), organization_id (uuid), record_type (enum: billing_group), updated_at (date-time)

Create a billing group

POST /billing_groups

Optional: name (string)

const billingGroup = await client.billingGroups.create({ name: 'my-resource' });

console.log(billingGroup.data);


Returns: created_at (date-time), deleted_at (date-time), id (uuid), name (string), organization_id (uuid), record_type (enum: billing_group), updated_at (date-time)

Get a billing group

GET /billing_groups/{id}

const billingGroup = await client.billingGroups.retrieve('f5586561-8ff0-4291-a0ac-84fe544797bd');

console.log(billingGroup.data);


Returns: created_at (date-time), deleted_at (date-time), id (uuid), name (string), organization_id (uuid), record_type (enum: billing_group), updated_at (date-time)

Update a billing group

PATCH /billing_groups/{id}

Optional: name (string)

const billingGroup = await client.billingGroups.update('f5586561-8ff0-4291-a0ac-84fe544797bd', {
  name: 'my-resource',
});

console.log(billingGroup.data);


Returns: created_at (date-time), deleted_at (date-time), id (uuid), name (string), organization_id (uuid), record_type (enum: billing_group), updated_at (date-time)

Delete a billing group

DELETE /billing_groups/{id}

const billingGroup = await client.billingGroups.delete('f5586561-8ff0-4291-a0ac-84fe544797bd');

console.log(billingGroup.data);


Returns: created_at (date-time), deleted_at (date-time), id (uuid), name (string), organization_id (uuid), record_type (enum: billing_group), updated_at (date-time)

List integration secrets

Retrieve a list of all integration secrets configured by the user.

GET /integration_secrets

// Automatically fetches more pages as needed.
for await (const integrationSecret of client.integrationSecrets.list()) {
  console.log(integrationSecret.id);
}


Returns: created_at (date-time), id (string), identifier (string), record_type (string), updated_at (date-time)

Create a secret

Create a new secret with an associated identifier that can be used to securely integrate with other services.

POST /integration_secrets — Required: identifier, type

Optional: password (string), token (string), username (string)

const integrationSecret = await client.integrationSecrets.create({
  identifier: 'my_secret',
  type: 'bearer',
  token: 'my_secret_value',
});

console.log(integrationSecret.data);


Returns: created_at (date-time), id (string), identifier (string), record_type (string), updated_at (date-time)

Delete an integration secret

Delete an integration secret given its ID.

DELETE /integration_secrets/{id}

await client.integrationSecrets.delete('550e8400-e29b-41d4-a716-446655440000');

Create an Access Token.

Create an Access Token (JWT) for the credential.

POST /telephony_credentials/{id}/token

const response = await client.telephonyCredentials.createToken('550e8400-e29b-41d4-a716-446655440000');

console.log(response);

Weekly Installs
32
Repository
team-telnyx/skills
GitHub Stars
171
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass