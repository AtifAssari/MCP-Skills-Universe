---
rating: ⭐⭐
title: strava
url: https://skills.sh/vm0-ai/vm0-skills/strava
---

# strava

skills/vm0-ai/vm0-skills/strava
strava
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill strava
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name STRAVA_TOKEN or zero doctor check-connector --url https://www.strava.com/api/v3/athlete --method GET

Athlete
Get Authenticated Athlete Profile
curl -s "https://www.strava.com/api/v3/athlete" --header "Authorization: Bearer $STRAVA_TOKEN" | jq '{id, firstname, lastname, city, country, sex, premium, created_at, follower_count, friend_count}'

Get Athlete Statistics

Replace <athlete-id> with the id from the athlete profile above:

curl -s "https://www.strava.com/api/v3/athletes/<athlete-id>/stats" --header "Authorization: Bearer $STRAVA_TOKEN" | jq '{recent_run_totals, recent_ride_totals, ytd_run_totals, ytd_ride_totals, all_run_totals, all_ride_totals}'

Activities
List Recent Activities
curl -s "https://www.strava.com/api/v3/athlete/activities?per_page=30" --header "Authorization: Bearer $STRAVA_TOKEN" | jq '.[] | {id, name, sport_type, distance, moving_time, elapsed_time, total_elevation_gain, start_date_local, average_speed, max_speed}'


Query parameters:

before=EPOCH — Activities before timestamp
after=EPOCH — Activities after timestamp
page=1 — Page number
per_page=30 — Results per page (max 200)
Get Activity Details
curl -s "https://www.strava.com/api/v3/activities/<activity-id>" --header "Authorization: Bearer $STRAVA_TOKEN" | jq '{id, name, sport_type, distance, moving_time, elapsed_time, total_elevation_gain, average_speed, max_speed, average_heartrate, max_heartrate, calories, description, gear_id}'

Create Manual Activity

Write to /tmp/strava_request.json:

{
  "name": "Morning Run",
  "sport_type": "Run",
  "start_date_local": "2025-01-15T08:00:00Z",
  "elapsed_time": 3600,
  "distance": 10000,
  "description": "Easy morning run"
}


Then run:

curl -s -X POST "https://www.strava.com/api/v3/activities" --header "Authorization: Bearer $STRAVA_TOKEN" --header "Content-Type: application/json" -d @/tmp/strava_request.json | jq '{id, name, sport_type, distance}'


Required fields: name, sport_type, start_date_local (ISO 8601), elapsed_time (seconds). Optional: distance (meters), description, trainer (0/1), commute (0/1).

Sport types: Run, TrailRun, Ride, MountainBikeRide, GravelRide, EBikeRide, Swim, Walk, Hike, WeightTraining, Yoga, Workout, Rowing, Kayaking, Surfing, RockClimbing, Golf, Soccer, Tennis, Pickleball, Skateboard, Snowboard, AlpineSki, NordicSki, etc.

Update Activity

Write to /tmp/strava_request.json:

{
  "name": "Updated Name",
  "description": "Updated description",
  "sport_type": "Run",
  "gear_id": "<gear-id>",
  "commute": false,
  "hide_from_home": false
}


Then run:

curl -s -X PUT "https://www.strava.com/api/v3/activities/<activity-id>" --header "Authorization: Bearer $STRAVA_TOKEN" --header "Content-Type: application/json" -d @/tmp/strava_request.json | jq '{id, name, description, sport_type}'


Updatable fields: name, sport_type, description, gear_id (set to "none" to remove), trainer, commute, hide_from_home.

Uploads
Upload Activity File (GPX/FIT/TCX)
curl -s -X POST "https://www.strava.com/api/v3/uploads" --header "Authorization: Bearer $STRAVA_TOKEN" -F "data_type=gpx" -F "file=@/path/to/activity.gpx" -F "name=My Activity" -F "description=Uploaded via API"


Supported formats: fit, fit.gz, tcx, tcx.gz, gpx, gpx.gz.

Check Upload Status

Uploads are processed asynchronously. Poll for status:

curl -s "https://www.strava.com/api/v3/uploads/<upload-id>" --header "Authorization: Bearer $STRAVA_TOKEN" | jq '{id, status, error, activity_id}'


When activity_id is populated, the upload is complete.

Activity Details
List Activity Comments
curl -s "https://www.strava.com/api/v3/activities/<activity-id>/comments" --header "Authorization: Bearer $STRAVA_TOKEN" | jq '.[] | {id, text, created_at, athlete: .athlete.firstname}'

List Activity Kudoers
curl -s "https://www.strava.com/api/v3/activities/<activity-id>/kudos" --header "Authorization: Bearer $STRAVA_TOKEN" | jq '.[] | {id, firstname, lastname}'

Get Activity Laps
curl -s "https://www.strava.com/api/v3/activities/<activity-id>/laps" --header "Authorization: Bearer $STRAVA_TOKEN" | jq '.[] | {id, name, elapsed_time, distance, average_speed, average_heartrate}'

Get Activity Streams (GPS/HR/Power Data)
curl -s "https://www.strava.com/api/v3/activities/<activity-id>/streams?keys=time,distance,heartrate,velocity_smooth&key_by_type=true" --header "Authorization: Bearer $STRAVA_TOKEN" | jq 'keys'


Available stream keys: time, distance, latlng, altitude, velocity_smooth, heartrate, cadence, watts, temp, moving, grade_smooth.

Segments
List Starred Segments
curl -s "https://www.strava.com/api/v3/segments/starred" --header "Authorization: Bearer $STRAVA_TOKEN" | jq '.[] | {id, name, distance, average_grade, maximum_grade, city, state, country}'

Get Segment Details
curl -s "https://www.strava.com/api/v3/segments/<segment-id>" --header "Authorization: Bearer $STRAVA_TOKEN" | jq '{id, name, activity_type, distance, average_grade, maximum_grade, elevation_high, elevation_low, city, country, effort_count, athlete_count}'

Gear
Get Athlete's Gear
curl -s "https://www.strava.com/api/v3/athlete" --header "Authorization: Bearer $STRAVA_TOKEN" | jq '{bikes: .bikes, shoes: .shoes}'

Get Gear Details

Bike IDs start with b, shoe IDs start with g:

curl -s "https://www.strava.com/api/v3/gear/<gear-id>" --header "Authorization: Bearer $STRAVA_TOKEN" | jq '{id, name, brand_name, model_name, distance, converted_distance}'

Clubs
List Athlete Clubs
curl -s "https://www.strava.com/api/v3/athlete/clubs" --header "Authorization: Bearer $STRAVA_TOKEN" | jq '.[] | {id, name, sport_type, city, country, member_count}'

Get Club Details
curl -s "https://www.strava.com/api/v3/clubs/<club-id>" --header "Authorization: Bearer $STRAVA_TOKEN" | jq '{id, name, sport_type, city, country, member_count, description}'

List Club Activities
curl -s "https://www.strava.com/api/v3/clubs/<club-id>/activities?per_page=20" --header "Authorization: Bearer $STRAVA_TOKEN" | jq '.[] | {name, sport_type, distance, moving_time, athlete: (.athlete.firstname + " " + .athlete.lastname)}'

Routes
Get Athlete Routes
curl -s "https://www.strava.com/api/v3/athletes/<athlete-id>/routes?per_page=20" --header "Authorization: Bearer $STRAVA_TOKEN" | jq '.[] | {id, name, type, distance, elevation_gain, estimated_moving_time}'

Guidelines
Token expiry: Access tokens expire every 6 hours — the platform handles refresh automatically via the connector
Pagination: Use page and per_page (max 200) for list endpoints
Time filters: Use Unix epoch timestamps for before/after parameters
Scope requirements: Ensure token has correct scopes; activity:read_all needed for private activities, activity:write needed to create/edit
Rate limits: 200 req/15min, 2000 req/day — add delays for bulk operations. Returns 429 when exceeded
Distance units: All distances are in meters, speeds in meters/second
Time units: All durations are in seconds
Sport type vs type: Prefer sport_type over deprecated type field
API Reference
REST Reference: https://developers.strava.com/docs/reference/
Authentication: https://developers.strava.com/docs/authentication/
Rate Limits: https://developers.strava.com/docs/rate-limits/
Uploads: https://developers.strava.com/docs/uploads/
Weekly Installs
73
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn