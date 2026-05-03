---
rating: ⭐⭐⭐
title: weather-query
url: https://skills.sh/vikiboss/60s-skills/weather-query
---

# weather-query

skills/vikiboss/60s-skills/weather-query
weather-query
Installation
$ npx skills add https://github.com/vikiboss/60s-skills --skill weather-query
Summary

Real-time weather and forecast data for locations across China.

Provides two core endpoints: real-time weather (temperature, humidity, wind, air quality) and multi-day forecasts with daily highs and lows
Accepts Chinese location names (cities or districts) as query parameters; supports major cities and most districts nationwide
Includes practical helper patterns for weather-based recommendations, multi-city comparisons, and travel suitability checks
Returns structured JSON responses with timestamps; best practice is to cache short-term and validate location names before querying
SKILL.md
Weather Query Skill

This skill enables AI agents to fetch real-time weather information and forecasts for locations in China using the 60s API.

When to Use This Skill

Use this skill when users:

Ask about current weather conditions
Want weather forecasts
Need temperature, humidity, wind information
Request air quality data
Plan outdoor activities and need weather info
API Endpoints
1. Real-time Weather

URL: https://60s.viki.moe/v2/weather/realtime
Method: GET

2. Weather Forecast

URL: https://60s.viki.moe/v2/weather/forecast
Method: GET

Parameters
query (required): Location name in Chinese
Can be city name: "北京", "上海", "广州"
Can be district name: "海淀区", "浦东新区"
How to Use
Get Real-time Weather
import requests

def get_realtime_weather(query):
    url = 'https://60s.viki.moe/v2/weather/realtime'
    response = requests.get(url, params={'query': query})
    return response.json()

# Example
weather = get_realtime_weather('北京')
print(f"☁️ {weather['location']}天气")
print(f"🌡️ 温度：{weather['temperature']}°C")
print(f"💨 风速：{weather['wind']}")
print(f"💧 湿度：{weather['humidity']}")

Get Weather Forecast
def get_weather_forecast(query):
    url = 'https://60s.viki.moe/v2/weather/forecast'
    response = requests.get(url, params={'query': query})
    return response.json()

# Example
forecast = get_weather_forecast('上海')
for day in forecast['forecast']:
    print(f"{day['date']}: {day['weather']} {day['temp_low']}°C ~ {day['temp_high']}°C")

Simple bash example
# Real-time weather
curl "https://60s.viki.moe/v2/weather/realtime?query=北京"

# Weather forecast
curl "https://60s.viki.moe/v2/weather/forecast?query=上海"

Response Format
Real-time Weather Response
{
  "location": "北京",
  "weather": "晴",
  "temperature": "15",
  "humidity": "45%",
  "wind": "东北风3级",
  "air_quality": "良",
  "updated": "2024-01-15 14:00:00"
}

Forecast Response
{
  "location": "上海",
  "forecast": [
    {
      "date": "2024-01-15",
      "day_of_week": "星期一",
      "weather": "多云",
      "temp_low": "10",
      "temp_high": "18",
      "wind": "东风3-4级"
    },
    ...
  ]
}

Example Interactions
User: "北京今天天气怎么样？"

Agent Response:

weather = get_realtime_weather('北京')
response = f"""
☁️ 北京今日天气

天气状况：{weather['weather']}
🌡️ 温度：{weather['temperature']}°C
💧 湿度：{weather['humidity']}
💨 风力：{weather['wind']}
🌫️ 空气质量：{weather['air_quality']}
"""

User: "上海未来三天天气"
forecast = get_weather_forecast('上海')
response = "📅 上海未来天气预报\n\n"
for day in forecast['forecast'][:3]:
    response += f"{day['date']} {day['day_of_week']}\n"
    response += f"  {day['weather']} {day['temp_low']}°C ~ {day['temp_high']}°C\n"
    response += f"  {day['wind']}\n\n"

User: "深圳会下雨吗？"
weather = get_realtime_weather('深圳')
if '雨' in weather['weather']:
    print("☔ 是的，深圳现在正在下雨")
    print("建议带伞出门！")
else:
    forecast = get_weather_forecast('深圳')
    rain_days = [d for d in forecast['forecast'] if '雨' in d['weather']]
    if rain_days:
        print(f"未来{rain_days[0]['date']}可能会下雨")
    else:
        print("近期没有降雨预报")

Best Practices

Location Names: Always use Chinese characters for location names

Error Handling: Check if the location is valid before displaying results

Context: Provide relevant context based on weather conditions

Rain: Suggest bringing umbrella
Hot: Recommend staying hydrated
Cold: Advise wearing warm clothes
Poor AQI: Suggest wearing mask

Caching: Weather data is updated regularly but can be cached for short periods

Fallbacks: If a specific district doesn't work, try the city name

Common Use Cases
1. Weather-based Recommendations
def give_weather_advice(location):
    weather = get_realtime_weather(location)
    advice = []
    
    temp = int(weather['temperature'])
    if temp > 30:
        advice.append("🔥 天气炎热，注意防暑降温，多喝水")
    elif temp < 5:
        advice.append("🥶 天气寒冷，注意保暖")
    
    if '雨' in weather['weather']:
        advice.append("☔ 记得带伞")
    
    if weather['air_quality'] in ['差', '重度污染']:
        advice.append("😷 空气质量不佳，建议戴口罩")
    
    return '\n'.join(advice)

2. Multi-city Weather Comparison
def compare_weather(cities):
    results = []
    for city in cities:
        weather = get_realtime_weather(city)
        results.append({
            'city': city,
            'temperature': int(weather['temperature']),
            'weather': weather['weather']
        })
    
    # Find hottest and coldest
    hottest = max(results, key=lambda x: x['temperature'])
    coldest = min(results, key=lambda x: x['temperature'])
    
    return f"🌡️ 最热: {hottest['city']} {hottest['temperature']}°C\n" \
           f"❄️ 最冷: {coldest['city']} {coldest['temperature']}°C"

3. Travel Weather Check
def check_travel_weather(destination, days=3):
    forecast = get_weather_forecast(destination)
    suitable_days = []
    
    for day in forecast['forecast'][:days]:
        if '雨' not in day['weather'] and '雪' not in day['weather']:
            suitable_days.append(day['date'])
    
    if suitable_days:
        return f"✅ {destination}适合出行的日期：{', '.join(suitable_days)}"
    else:
        return f"⚠️ 未来{days}天{destination}天气不太适合出行"

Troubleshooting
Issue: Location not found
Solution: Try using the main city name instead of district
Example: Use "北京" instead of "朝阳区"
Issue: No forecast data
Solution: Verify the location name is correct
Try standard city names: 北京, 上海, 广州, 深圳, etc.
Issue: Data seems outdated
Solution: The API updates regularly, but weather can change quickly
Check the updated timestamp in the response
Supported Locations

The weather API supports most cities and districts in China, including:

Provincial capitals: 北京, 上海, 广州, 深圳, 成都, 杭州, 南京, 武汉, etc.
Major cities: 苏州, 青岛, 大连, 厦门, etc.
Districts: 海淀区, 朝阳区, 浦东新区, etc.
Related Resources
60s API Documentation
GitHub Repository
Weekly Installs
612
Repository
vikiboss/60s-skills
GitHub Stars
32
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass