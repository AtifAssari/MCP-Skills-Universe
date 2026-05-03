---
title: data-query
url: https://skills.sh/vikiboss/60s-skills/data-query
---

# data-query

skills/vikiboss/60s-skills/data-query
data-query
Installation
$ npx skills add https://github.com/vikiboss/60s-skills --skill data-query
SKILL.md
Data Query Skill

Query various data and information including exchange rates, calendar, history, encyclopedia, and prices.

Available Queries
Exchange Rates - Currency conversion rates
Lunar Calendar - Chinese lunar calendar conversion
Today in History - Historical events
Encyclopedia (Baike) - Search Chinese encyclopedia
Fuel Prices - Gasoline/diesel prices in China
Gold Prices - Current gold prices
Chemical Elements - Element information
API Endpoints
Query Type	Endpoint	Method
Exchange Rate	/v2/exchange-rate	GET
Lunar Calendar	/v2/lunar	GET
History	/v2/today-in-history	GET
Encyclopedia	/v2/baike	GET
Fuel Price	/v2/fuel-price	GET
Gold Price	/v2/gold-price	GET
Chemical	/v2/chemical	GET
Quick Examples
Exchange Rates
import requests

# Get exchange rate
params = {'from': 'USD', 'to': 'CNY'}
response = requests.get('https://60s.viki.moe/v2/exchange-rate', params=params)
rate = response.json()

print(f"💱 1 {rate['from']} = {rate['rate']} {rate['to']}")
print(f"更新时间：{rate['update_time']}")

Lunar Calendar
# Get today's lunar date
response = requests.get('https://60s.viki.moe/v2/lunar')
lunar = response.json()

print(f"📅 公历：{lunar['solar_date']}")
print(f"🏮 农历：{lunar['lunar_date']}")
print(f"🐲 生肖：{lunar['zodiac']}")
print(f"🌾 节气：{lunar['solar_term']}")

# Specific date
params = {'date': '2024-01-15'}
response = requests.get('https://60s.viki.moe/v2/lunar', params=params)

Today in History
# Get today's historical events
response = requests.get('https://60s.viki.moe/v2/today-in-history')
history = response.json()

print(f"📜 历史上的今天 ({history['date']})")
for event in history['events'][:5]:
    print(f"{event['year']}年：{event['title']}")

# Specific date
params = {'month': 1, 'day': 15}
response = requests.get('https://60s.viki.moe/v2/today-in-history', params=params)

Encyclopedia Search
# Search encyclopedia
params = {'keyword': 'Python编程'}
response = requests.get('https://60s.viki.moe/v2/baike', params=params)
result = response.json()

print(f"📖 {result['title']}")
print(f"📝 {result['summary']}")
print(f"🔗 {result['url']}")

Fuel Prices
# Get fuel prices
params = {'province': '北京'}
response = requests.get('https://60s.viki.moe/v2/fuel-price', params=params)
prices = response.json()

print(f"⛽ {prices['province']} 油价")
print(f"92号汽油：{prices['92号汽油']} 元/升")
print(f"95号汽油：{prices['95号汽油']} 元/升")
print(f"98号汽油：{prices['98号汽油']} 元/升")
print(f"0号柴油：{prices['0号柴油']} 元/升")

Gold Prices
# Get current gold prices
response = requests.get('https://60s.viki.moe/v2/gold-price')
gold = response.json()

print(f"💰 黄金价格")
print(f"国际金价：{gold['国际金价']} 美元/盎司")
print(f"国内金价：{gold['国内金价']} 元/克")
print(f"更新时间：{gold['update_time']}")

Chemical Elements
# Search chemical element
params = {'query': 'H'}  # Can be symbol, name, or atomic number
response = requests.get('https://60s.viki.moe/v2/chemical', params=params)
element = response.json()

print(f"⚛️ {element['name']} ({element['symbol']})")
print(f"原子序数：{element['atomic_number']}")
print(f"原子量：{element['atomic_mass']}")
print(f"元素类别：{element['category']}")

Use Cases
Currency Converter Bot
def convert_currency(amount, from_currency, to_currency):
    params = {'from': from_currency, 'to': to_currency}
    response = requests.get('https://60s.viki.moe/v2/exchange-rate', params=params)
    rate = response.json()
    
    converted = amount * float(rate['rate'])
    return f"{amount} {from_currency} = {converted:.2f} {to_currency}"

# Usage
print(convert_currency(100, 'USD', 'CNY'))  # 100 USD = 725.50 CNY

Historical Event Reminder
def get_today_history():
    response = requests.get('https://60s.viki.moe/v2/today-in-history')
    history = response.json()
    
    message = f"📜 历史上的今天 ({history['date']})\n\n"
    for event in history['events'][:3]:
        message += f"· {event['year']}年：{event['title']}\n"
    
    return message

Lunar Calendar Widget
def get_lunar_info():
    response = requests.get('https://60s.viki.moe/v2/lunar')
    lunar = response.json()
    
    return f"""
📅 今日日历

公历：{lunar['solar_date']} {lunar['weekday']}
农历：{lunar['lunar_date']}
生肖：{lunar['zodiac']}
节气：{lunar['solar_term'] or '无'}
    """

Example Interactions
User: "美元兑人民币汇率是多少？"
params = {'from': 'USD', 'to': 'CNY'}
response = requests.get('https://60s.viki.moe/v2/exchange-rate', params=params)
rate = response.json()
print(f"💱 1 美元 = {rate['rate']} 人民币")

User: "今天农历是几月几号？"
lunar = requests.get('https://60s.viki.moe/v2/lunar').json()
print(f"🏮 今天是农历 {lunar['lunar_date']}")
print(f"🐲 生肖：{lunar['zodiac']}")

User: "查询一下氢元素的信息"
params = {'query': '氢'}
element = requests.get('https://60s.viki.moe/v2/chemical', params=params).json()
print(f"⚛️ {element['name']} (H)")
print(f"原子序数：{element['atomic_number']}")
print(f"元素类别：{element['category']}")

Related Resources
60s API Documentation
GitHub Repository
Weekly Installs
46
Repository
vikiboss/60s-skills
GitHub Stars
32
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn