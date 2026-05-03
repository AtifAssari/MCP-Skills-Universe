---
rating: ⭐⭐⭐
title: entertainment
url: https://skills.sh/vikiboss/60s-skills/entertainment
---

# entertainment

skills/vikiboss/60s-skills/entertainment
entertainment
Installation
$ npx skills add https://github.com/vikiboss/60s-skills --skill entertainment
SKILL.md
Entertainment Content Skill

Get fun and entertaining content including quotes, jokes, luck predictions, and memes.

Available Content
Hitokoto (一言) - Random meaningful quotes
Dad Jokes - English dad jokes
Duanzi (段子) - Chinese jokes/funny stories
Luck Prediction - Daily fortune telling
KFC Meme - Crazy Thursday meme text
Moyu Calendar - Slacking off calendar
API Endpoints
Content	Endpoint	Method
Hitokoto	/v2/hitokoto	GET
Dad Joke	/v2/dad-joke	GET
Duanzi	/v2/duanzi	GET
Luck	/v2/luck	GET
KFC Meme	/v2/kfc	GET
Moyu	/v2/moyu	GET
Quick Examples
Get Random Quote (Hitokoto)
import requests

# Get random quote
response = requests.get('https://60s.viki.moe/v2/hitokoto')
quote = response.json()

print(f"📖 {quote['hitokoto']}")
print(f"   —— {quote['from']}")

# With category
params = {'category': 'anime'}  # anime, comic, game, literature, original, internet, other
response = requests.get('https://60s.viki.moe/v2/hitokoto', params=params)

Get Dad Joke
response = requests.get('https://60s.viki.moe/v2/dad-joke')
joke = response.json()

print(f"😄 {joke['setup']}")
print(f"   {joke['punchline']}")

Get Chinese Joke (Duanzi)
response = requests.get('https://60s.viki.moe/v2/duanzi')
duanzi = response.json()

print(f"😂 {duanzi['content']}")

Get Daily Luck
response = requests.get('https://60s.viki.moe/v2/luck')
luck = response.json()

print(f"🔮 今日运势")
print(f"综合运势：{luck['总运势']}")
print(f"爱情运势：{luck['爱情运势']}")
print(f"事业运势：{luck['事业运势']}")
print(f"财富运势：{luck['财富运势']}")
print(f"幸运颜色：{luck['幸运颜色']}")
print(f"幸运数字：{luck['幸运数字']}")

Get KFC Meme Text
response = requests.get('https://60s.viki.moe/v2/kfc')
meme = response.json()

print(f"🍗 {meme['text']}")

Get Moyu Calendar
response = requests.get('https://60s.viki.moe/v2/moyu')
# Returns image
with open('moyu.jpg', 'wb') as f:
    f.write(response.content)

Use Cases
Daily Entertainment Bot
def get_morning_entertainment():
    quote = requests.get('https://60s.viki.moe/v2/hitokoto').json()
    luck = requests.get('https://60s.viki.moe/v2/luck').json()
    
    message = f"""
☀️ 早安！

📖 每日一言
{quote['hitokoto']}
—— {quote['from']}

🔮 今日运势
综合：{luck['总运势']} ⭐
幸运色：{luck['幸运颜色']}
    """
    return message

Chatbot Fun Commands
def handle_fun_command(command):
    if 'joke' in command or '笑话' in command:
        joke = requests.get('https://60s.viki.moe/v2/duanzi').json()
        return f"😂 {joke['content']}"
    
    elif 'quote' in command or '名言' in command:
        quote = requests.get('https://60s.viki.moe/v2/hitokoto').json()
        return f"📖 {quote['hitokoto']} —— {quote['from']}"
    
    elif 'luck' in command or '运势' in command:
        luck = requests.get('https://60s.viki.moe/v2/luck').json()
        return f"🔮 今日运势：{luck['总运势']}\n幸运色：{luck['幸运颜色']}"
    
    elif 'kfc' in command:
        meme = requests.get('https://60s.viki.moe/v2/kfc').json()
        return f"🍗 {meme['text']}"

Example Interactions
User: "讲个笑话"
duanzi = requests.get('https://60s.viki.moe/v2/duanzi').json()
print(f"😂 {duanzi['content']}")

User: "今天运势怎么样？"
luck = requests.get('https://60s.viki.moe/v2/luck').json()
response = f"""
🔮 您今日的运势：

综合运势：{luck['总运势']}
爱情运势：{luck['爱情运势']}
事业运势：{luck['事业运势']}
财富运势：{luck['财富运势']}

💡 幸运提示
幸运颜色：{luck['幸运颜色']}
幸运数字：{luck['幸运数字']}
"""

User: "给我一句励志的话"
params = {'category': 'literature'}
quote = requests.get('https://60s.viki.moe/v2/hitokoto', params=params).json()
print(f"✨ {quote['hitokoto']}\n   —— {quote['from']}")

Related Resources
60s API Documentation
GitHub Repository
Weekly Installs
62
Repository
vikiboss/60s-skills
GitHub Stars
32
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn