---
rating: ⭐⭐
title: nutmeg-analyse
url: https://skills.sh/withqwerty/nutmeg/nutmeg-analyse
---

# nutmeg-analyse

skills/withqwerty/nutmeg/nutmeg-analyse
nutmeg-analyse
Installation
$ npx skills add https://github.com/withqwerty/nutmeg --skill nutmeg-analyse
SKILL.md
Analyse

Help the user explore and interpret football data. Adapt depth and approach to their experience level from .nutmeg.user.md.

Accuracy

Read and follow docs/accuracy-guardrail.md before answering any question about provider-specific facts (IDs, endpoints, schemas, coordinates, rate limits). Always use search_docs — never guess from training data.

First: check profile

Read .nutmeg.user.md. If it doesn't exist, tell the user to run /nutmeg first.

Adapt to experience level
Beginners

Guide them step by step. Start with simple questions:

"Which team scores the most goals?" (count goals, sort)
"Who takes the most shots?" (filter shots, group by player)
"Where do goals come from?" (plot shot locations)

Avoid jargon. Explain xG before using it. Show them what the data looks like before analysing it.

Common beginner mistake: Drawing conclusions from tiny samples. A player with 2 goals from 3 shots doesn't have a 67% conversion rate worth reporting. Always flag sample size.

Intermediate

They know the basics. Help with:

Comparative analysis (this team vs league average)
Contextual metrics (per-90, possession-adjusted)
Multi-variable analysis (passing profile + pressing intensity)
Basic visualisations (shot maps, pass networks, xG timelines)

Common intermediate mistake: Confusing correlation with causation. High possession doesn't cause wins. Help them think about mechanisms.

Advanced / Professional

Focus on rigour:

Statistical significance (is this difference real or noise?)
Controlling for confounders (opponent quality, game state, home/away)
Model selection and validation
Communicating uncertainty

Common advanced mistake: Over-engineering. Sometimes a bar chart answers the question better than a neural network.

Analysis frameworks
Single match analysis
Match narrative: xG timeline (when did each team create chances?)
Shot map: Location, xG value, outcome for each shot
Passing network: Who connected with whom, average positions
Pressing analysis: Where did each team win the ball back?
Key events: Goals, red cards, substitution impact
Team season analysis
Performance trajectory: Rolling xG, points, form over the season
Style profile: Possession %, PPDA, directness, set piece reliance
Squad analysis: Minutes distribution, key players by contribution
Home vs away: Performance split
Score state: How does the team play when winning vs losing?
Player analysis
Per-90 stats: Normalise by minutes, not matches
Percentile ranks: Where does this player rank among peers (same position, same league)?
Radar charts: Multi-dimensional profile (goals, assists, passes, pressures, etc.)
Progressive actions: Passes, carries, and runs that move the ball significantly forward
Minimum minutes filter: 900 minutes (10 full matches) is a common threshold
Comparison analysis
Define the question first. "Is Player A better than Player B?" is too vague. Better: "Who creates more high-quality chances from open play?"
Control for context. Per-90 stats, adjust for team quality, league quality.
Use appropriate baselines. Compare to positional averages, not all players.
Acknowledge limitations. Different roles, different teammates, different systems.
Visualisation guidance
Chart type	Best for	Football use case
Shot map	Spatial data on pitch	Where shots were taken, sized by xG
Pass network	Relationships	Who passes to whom, team shape
xG timeline	Match narrative	Running xG through a match
Radar chart	Multi-dimensional comparison	Player or team profiles
Bar chart	Ranking / comparison	League tables, top scorers
Heatmap	Density / frequency	Player touch maps, action zones
Scatter plot	Two-variable relationship	xG vs actual goals, creativity vs volume
Beeswarm	Distribution	Player stat distributions by position
Visualisation principles
Label axes clearly. Include units.
Always show what the data IS, not just what you want it to say.
Use football pitch backgrounds for spatial data (mplsoccer in Python, ggsoccer in R).
Colour choices: use team colours when comparing clubs, sequential palettes for values.
Credit your data source.
Data honesty

Football data can tell you whatever you want it to. Guard against this:

State your question before looking at the data. Don't go fishing for interesting patterns.
Report null results. "We found no significant difference" is a valid finding.
Show the raw numbers alongside fancy metrics. xG is meaningless without goals for context.
Be specific about what you're measuring. "Pressing intensity" measured how? Over what period?
Acknowledge what the data can't tell you. Event data doesn't capture off-ball movement, communication, or tactical intelligence.
Weekly Installs
49
Repository
withqwerty/nutmeg
GitHub Stars
18
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass