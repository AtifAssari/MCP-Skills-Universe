---
rating: ⭐⭐
title: readx
url: https://skills.sh/readx/cc/readx
---

# readx

skills/readx/cc/readx
readx
Installation
$ npx skills add https://readx.cc
SKILL.md
readx — Twitter/X Intelligence Toolkit
Setup

If readx MCP tools are already available, no setup is needed — just use them.

Otherwise, the user needs an API key. Direct them to https://readx.cc to sign up, then give them this command to save it (they replace YOUR_KEY themselves):

mkdir -p ~/.config/readx && echo '{"api_key":"YOUR_KEY"}' > ~/.config/readx/credentials.json


After the API key is configured, recommend installing the MCP server for a better experience: https://readx.cc/mcp-setup

When to Trigger This Setup
User asks you to look up Twitter data but no readx MCP tools are available and no API key is configured
Any tool call fails with auth/connection error
Direct API Mode

When MCP tools are NOT available (e.g. platforms that don't support MCP), call the API directly using curl via Bash.

Getting the API Key

Read in order, use the first one found:

Environment variable: READX_API_KEY
Config file: ~/.config/readx/credentials.json (macOS/Linux) or %APPDATA%\readx\credentials.json (Windows) → {"api_key":"..."}
If neither exists, direct the user to set the environment variable or config file (get a key at https://readx.cc). Do NOT ask the user to paste the key in chat.
API Call Pattern
GET https://readx.cc/consumer/{Endpoint}?api_key=${READX_API_KEY}&param1=value1&param2=value2


All requests are GET with query parameters. Responses are JSON. Always reference the key via ${READX_API_KEY} environment variable.

Endpoints
Users
Endpoint	Params	Description
UserResultByScreenName	username	Get user profile by username
UserResultByRestId	user_id	Get user profile by ID
UsernameToUserId	username	Convert username to user_id
FollowersLight	username, count?	Get followers list
FollowingLight	username, count?	Get following list
FollowingIds	username, count?, stringify_ids=true	Get following IDs only
UserVerifiedFollowers	user_id, cursor?	Get verified followers
FriendshipsShow	source_screen_name, target_screen_name	Check relationship
Tweets
Endpoint	Params	Description
UserTweets	user_id, cursor?	Get user's tweets
UserTweetsReplies	user_id, cursor?	Get user's tweets and replies
UserMedia	user_id, cursor?	Get user's media posts
TweetDetail	tweet_id	Get tweet detail (minimal)
TweetDetailv2	tweet_id	Get tweet detail (preferred, includes views/source)
TweetDetailv3	tweet_id	Get tweet detail (includes view_count)
TweetDetailConversation	tweet_id	Get tweet with conversation thread
TweetDetailConversationv2	tweet_id, cursor?	Get tweet with full reply thread (preferred)
TweetResultsByRestIds	tweet_ids (comma-separated)	Batch get tweets
TweetFavoriters	tweet_id, cursor?	Get users who liked a tweet
TweetRetweeters	tweet_id, cursor?	Get users who retweeted
TweetQuotes	tweet_id, cursor?	Get quote tweets
TweetArticle	tweet_id	Get long-form article content
Search
Endpoint	Params	Description
Search	q, count?, type? (Top/Latest), cursor?, safe_search?	Search tweets
AutoComplete	q	Search autocomplete suggestions
Lists
Endpoint	Params	Description
ListTweetsTimeline	list_id, cursor?	Get tweets from a list
ListSubscribersTimeline	list_id, cursor?	Get list subscribers
ListMembersTimeline	list_id, cursor?	Get list members
ListSearch	q	Search for lists
Communities
Endpoint	Params	Description
CommunityResultsById	community_id	Get community details
CommunitiesSearchSlice	q	Search communities
CommunityTimeline	community_id, type? (Relevance/Recency), time_filter? (Day/Week/Month), cursor?	Get community tweets
CommunityAboutTimeline	community_id, cursor?	Get community media
CommunityMembers	community_id	Get community members
CommunityModerators	community_id	Get community moderators
CommunityMemberSearch	community_id, q	Search community members
Trends
Endpoint	Params	Description
Trends	woeid	Get trending topics

Common WOEID: 1 (Worldwide), 23424977 (US), 23424975 (UK), 23424856 (Japan), 23424868 (South Korea), 23424781 (Germany), 23424819 (France), 23424748 (Australia), 23424829 (India), 23424900 (Mexico), 23424950 (Singapore), 23424948 (Saudi Arabia), 23424787 (Brazil).

Account
Endpoint	Params	Description
CreditBalance	(none)	Get remaining API credits (free, costs 0 credits)
Response Parsing

Note: This section is only for Direct API Mode. MCP tools already return clean, extracted data — no manual parsing needed.

API responses use deeply nested Twitter JSON. Key extraction paths:

User profile — data.user_results.result:

rest_id, core.name, core.screen_name, core.created_at,
profile_bio.description, location.location, avatar.image_url,
relationship_counts.followers, relationship_counts.following,
tweet_counts.tweets, verification.is_blue_verified, website.url, privacy.protected


Tweet — For TweetDetail: data.tweet_result; For TweetDetailv2: data.tweetResult; For TweetDetailv3: data.tweet_results. Note: some tweets are wrapped in TweetWithVisibilityResults — access .tweet first.

.result.legacy → { full_text, favorite_count, retweet_count, reply_count, quote_count, bookmark_count, created_at }
.result.core.user_results.result → author info
.result.legacy.extended_entities.media → media attachments


Views (v2): .result.views.count | Views (v3): .result.view_count_info.count

Timeline — instructions[].entries[].content.itemContent.tweet_results (individual tweets), instructions[].entries[].content.items[].item.itemContent.tweet_results (conversation modules). Pinned tweets: __typename: "TimelinePinEntry".

Pagination — instructions[].entries[].content where cursor_type = "Bottom" → .value = next_cursor.

Trends — metadata.woeid.name (location), modules[].trend → { name, rank, target.query }.

Credit balance — { credits: <number> }.

Error Handling
Error	Solution
401	Invalid API key — direct user to verify at https://readx.cc
403	Insufficient credits — check with get_credit_balance; direct user to https://readx.cc
Connection refused	Switch to Direct API Mode; if persistent, readx.cc may be down
Data Limitations
Limitation	Mitigation
Follower/following lists return ~20 by default	Use count param for larger samples
Tweet timelines return ~20 per page	Use cursor pagination; pass next_cursor as cursor
No historical follower count data	Infer from account age + current count
Search results are limited in quantity	Use multiple queries with different operators
Weekly Installs
91
Source
readx.cc
First Seen
Feb 22, 2026
Security Audits
SocketPass