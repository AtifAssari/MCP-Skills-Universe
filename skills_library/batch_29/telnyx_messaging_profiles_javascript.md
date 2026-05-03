---
title: telnyx-messaging-profiles-javascript
url: https://skills.sh/team-telnyx/skills/telnyx-messaging-profiles-javascript
---

# telnyx-messaging-profiles-javascript

skills/team-telnyx/skills/telnyx-messaging-profiles-javascript
telnyx-messaging-profiles-javascript
Installation
$ npx skills add https://github.com/team-telnyx/skills --skill telnyx-messaging-profiles-javascript
SKILL.md
Telnyx Messaging Profiles - JavaScript
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
List messaging profiles

GET /messaging_profiles

// Automatically fetches more pages as needed.
for await (const messagingProfile of client.messagingProfiles.list()) {
  console.log(messagingProfile.id);
}


Returns: ai_assistant_id (string | null), alpha_sender (string | null), created_at (date-time), daily_spend_limit (string), daily_spend_limit_enabled (boolean), enabled (boolean), health_webhook_url (url), id (uuid), mms_fall_back_to_sms (boolean), mms_transcoding (boolean), mobile_only (boolean), name (string), number_pool_settings (object | null), organization_id (string), record_type (enum: messaging_profile), redaction_enabled (boolean), redaction_level (integer), resource_group_id (string | null), smart_encoding (boolean), updated_at (date-time), url_shortener_settings (object | null), v1_secret (string), webhook_api_version (enum: 1, 2, 2010-04-01), webhook_failover_url (url), webhook_url (url), whitelisted_destinations (array[string])

Create a messaging profile

POST /messaging_profiles — Required: name, whitelisted_destinations

Optional: ai_assistant_id (string | null), alpha_sender (string | null), daily_spend_limit (string), daily_spend_limit_enabled (boolean), enabled (boolean), health_webhook_url (url), mms_fall_back_to_sms (boolean), mms_transcoding (boolean), mobile_only (boolean), number_pool_settings (object | null), resource_group_id (string | null), smart_encoding (boolean), url_shortener_settings (object | null), webhook_api_version (enum: 1, 2, 2010-04-01), webhook_failover_url (url), webhook_url (url)

const messagingProfile = await client.messagingProfiles.create({
  name: 'My name',
  whitelisted_destinations: ['US'],
});

console.log(messagingProfile.data);


Returns: ai_assistant_id (string | null), alpha_sender (string | null), created_at (date-time), daily_spend_limit (string), daily_spend_limit_enabled (boolean), enabled (boolean), health_webhook_url (url), id (uuid), mms_fall_back_to_sms (boolean), mms_transcoding (boolean), mobile_only (boolean), name (string), number_pool_settings (object | null), organization_id (string), record_type (enum: messaging_profile), redaction_enabled (boolean), redaction_level (integer), resource_group_id (string | null), smart_encoding (boolean), updated_at (date-time), url_shortener_settings (object | null), v1_secret (string), webhook_api_version (enum: 1, 2, 2010-04-01), webhook_failover_url (url), webhook_url (url), whitelisted_destinations (array[string])

Retrieve a messaging profile

GET /messaging_profiles/{id}

const messagingProfile = await client.messagingProfiles.retrieve(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(messagingProfile.data);


Returns: ai_assistant_id (string | null), alpha_sender (string | null), created_at (date-time), daily_spend_limit (string), daily_spend_limit_enabled (boolean), enabled (boolean), health_webhook_url (url), id (uuid), mms_fall_back_to_sms (boolean), mms_transcoding (boolean), mobile_only (boolean), name (string), number_pool_settings (object | null), organization_id (string), record_type (enum: messaging_profile), redaction_enabled (boolean), redaction_level (integer), resource_group_id (string | null), smart_encoding (boolean), updated_at (date-time), url_shortener_settings (object | null), v1_secret (string), webhook_api_version (enum: 1, 2, 2010-04-01), webhook_failover_url (url), webhook_url (url), whitelisted_destinations (array[string])

Update a messaging profile

PATCH /messaging_profiles/{id}

Optional: alpha_sender (string | null), created_at (date-time), daily_spend_limit (string), daily_spend_limit_enabled (boolean), enabled (boolean), id (uuid), mms_fall_back_to_sms (boolean), mms_transcoding (boolean), mobile_only (boolean), name (string), number_pool_settings (object | null), record_type (enum: messaging_profile), smart_encoding (boolean), updated_at (date-time), url_shortener_settings (object | null), v1_secret (string), webhook_api_version (enum: 1, 2, 2010-04-01), webhook_failover_url (url), webhook_url (url), whitelisted_destinations (array[string])

const messagingProfile = await client.messagingProfiles.update(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(messagingProfile.data);


Returns: ai_assistant_id (string | null), alpha_sender (string | null), created_at (date-time), daily_spend_limit (string), daily_spend_limit_enabled (boolean), enabled (boolean), health_webhook_url (url), id (uuid), mms_fall_back_to_sms (boolean), mms_transcoding (boolean), mobile_only (boolean), name (string), number_pool_settings (object | null), organization_id (string), record_type (enum: messaging_profile), redaction_enabled (boolean), redaction_level (integer), resource_group_id (string | null), smart_encoding (boolean), updated_at (date-time), url_shortener_settings (object | null), v1_secret (string), webhook_api_version (enum: 1, 2, 2010-04-01), webhook_failover_url (url), webhook_url (url), whitelisted_destinations (array[string])

Delete a messaging profile

DELETE /messaging_profiles/{id}

const messagingProfile = await client.messagingProfiles.delete(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
);

console.log(messagingProfile.data);


Returns: ai_assistant_id (string | null), alpha_sender (string | null), created_at (date-time), daily_spend_limit (string), daily_spend_limit_enabled (boolean), enabled (boolean), health_webhook_url (url), id (uuid), mms_fall_back_to_sms (boolean), mms_transcoding (boolean), mobile_only (boolean), name (string), number_pool_settings (object | null), organization_id (string), record_type (enum: messaging_profile), redaction_enabled (boolean), redaction_level (integer), resource_group_id (string | null), smart_encoding (boolean), updated_at (date-time), url_shortener_settings (object | null), v1_secret (string), webhook_api_version (enum: 1, 2, 2010-04-01), webhook_failover_url (url), webhook_url (url), whitelisted_destinations (array[string])

List phone numbers associated with a messaging profile

GET /messaging_profiles/{id}/phone_numbers

// Automatically fetches more pages as needed.
for await (const phoneNumberWithMessagingSettings of client.messagingProfiles.listPhoneNumbers(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
)) {
  console.log(phoneNumberWithMessagingSettings.id);
}


Returns: country_code (string), created_at (date-time), eligible_messaging_products (array[string]), features (object), health (object), id (string), messaging_product (string), messaging_profile_id (string | null), organization_id (string), phone_number (string), record_type (enum: messaging_phone_number, messaging_settings), tags (array[string]), traffic_type (string), type (enum: long-code, toll-free, short-code, longcode, tollfree, shortcode), updated_at (date-time)

List short codes associated with a messaging profile

GET /messaging_profiles/{id}/short_codes

// Automatically fetches more pages as needed.
for await (const shortCode of client.messagingProfiles.listShortCodes(
  '182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e',
)) {
  console.log(shortCode.messaging_profile_id);
}


Returns: country_code (string), created_at (date-time), id (uuid), messaging_profile_id (string | null), record_type (enum: short_code), short_code (string), tags (array), updated_at (date-time)

List short codes

GET /short_codes

// Automatically fetches more pages as needed.
for await (const shortCode of client.shortCodes.list()) {
  console.log(shortCode.messaging_profile_id);
}


Returns: country_code (string), created_at (date-time), id (uuid), messaging_profile_id (string | null), record_type (enum: short_code), short_code (string), tags (array), updated_at (date-time)

Retrieve a short code

GET /short_codes/{id}

const shortCode = await client.shortCodes.retrieve('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');

console.log(shortCode.data);


Returns: country_code (string), created_at (date-time), id (uuid), messaging_profile_id (string | null), record_type (enum: short_code), short_code (string), tags (array), updated_at (date-time)

Update short code

Update the settings for a specific short code. To unbind a short code from a profile, set the messaging_profile_id to null or an empty string. To add or update tags, include the tags field as an array of strings.

PATCH /short_codes/{id} — Required: messaging_profile_id

Optional: tags (array)

const shortCode = await client.shortCodes.update('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
  messaging_profile_id: 'abc85f64-5717-4562-b3fc-2c9600000000',
});

console.log(shortCode.data);


Returns: country_code (string), created_at (date-time), id (uuid), messaging_profile_id (string | null), record_type (enum: short_code), short_code (string), tags (array), updated_at (date-time)

Weekly Installs
51
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