---
rating: ⭐⭐⭐
title: media-info
url: https://skills.sh/vikiboss/60s-skills/media-info
---

# media-info

skills/vikiboss/60s-skills/media-info
media-info
Installation
$ npx skills add https://github.com/vikiboss/60s-skills --skill media-info
SKILL.md
Media Information Skill

Get music and movie information including charts, lyrics, box office, and ratings.

Available Information
Netease Music Ranks - Music chart lists
Music Rank Details - Detailed song lists
Lyrics Search - Find song lyrics
Movie Information - All movies database
Movie Box Office - Real-time box office rankings
TV Ratings - TV drama ratings
Web Series Rankings - Online series popularity
API Endpoints
Type	Endpoint	Method
Music Ranks	/v2/ncm-rank/list	GET
Rank Detail	/v2/ncm-rank/{id}	GET
Lyrics	/v2/lyric	POST
All Movies	/v2/maoyan/all/movie	GET
Box Office	/v2/maoyan/realtime/movie	GET
TV Ratings	/v2/maoyan/realtime/tv	GET
Web Series	/v2/maoyan/realtime/web	GET
Quick Examples
Netease Music Charts
import requests

# Get all music rank lists
response = requests.get('https://60s.viki.moe/v2/ncm-rank/list')
ranks = response.json()

print("🎵 网易云音乐榜单")
for rank in ranks['data']:
    print(f"· {rank['name']} (ID: {rank['id']})")

# Get specific rank details
rank_id = '3778678'  # 飙升榜
response = requests.get(f'https://60s.viki.moe/v2/ncm-rank/{rank_id}')
songs = response.json()

print(f"\n🎵 {songs['name']}")
for i, song in enumerate(songs['songs'][:10], 1):
    print(f"{i}. {song['name']} - {song['artist']}")

Lyrics Search
# Search for lyrics
data = {'keyword': '稻香 周杰伦'}
response = requests.post('https://60s.viki.moe/v2/lyric', json=data)
result = response.json()

print(f"🎤 {result['song']} - {result['artist']}")
print(f"\n{result['lyrics']}")

Movie Box Office
# Get real-time box office
response = requests.get('https://60s.viki.moe/v2/maoyan/realtime/movie')
movies = response.json()

print("🎬 实时电影票房")
for movie in movies['data'][:5]:
    print(f"{movie['rank']}. {movie['name']}")
    print(f"   票房：{movie['box_office']}")
    print(f"   上座率：{movie['attendance_rate']}")

TV Ratings
# Get TV drama ratings
response = requests.get('https://60s.viki.moe/v2/maoyan/realtime/tv')
shows = response.json()

print("📺 电视剧收视率排行")
for show in shows['data'][:5]:
    print(f"{show['rank']}. {show['name']}")
    print(f"   收视率：{show['rating']}")

Web Series Rankings
# Get web series rankings
response = requests.get('https://60s.viki.moe/v2/maoyan/realtime/web')
series = response.json()

print("📱 网剧热度排行")
for s in series['data'][:5]:
    print(f"{s['rank']}. {s['name']}")
    print(f"   热度：{s['popularity']}")

Use Cases
Music Recommendation Bot
def get_trending_music():
    # Get soaring charts (飙升榜)
    response = requests.get('https://60s.viki.moe/v2/ncm-rank/3778678')
    songs = response.json()
    
    message = "🎵 当前最火的歌曲：\n\n"
    for i, song in enumerate(songs['songs'][:5], 1):
        message += f"{i}. {song['name']} - {song['artist']}\n"
    
    return message

Movie Box Office Tracker
def get_box_office_summary():
    response = requests.get('https://60s.viki.moe/v2/maoyan/realtime/movie')
    movies = response.json()
    
    top_3 = movies['data'][:3]
    
    summary = "🎬 今日票房TOP3\n\n"
    for movie in top_3:
        summary += f"🏆 {movie['rank']}. {movie['name']}\n"
        summary += f"   💰 票房：{movie['box_office']}\n"
        summary += f"   📊 上座率：{movie['attendance_rate']}\n\n"
    
    return summary

Lyrics Finder
def find_lyrics(song_name, artist=''):
    keyword = f"{song_name} {artist}".strip()
    data = {'keyword': keyword}
    
    response = requests.post('https://60s.viki.moe/v2/lyric', json=data)
    result = response.json()
    
    if result.get('lyrics'):
        return f"🎤 {result['song']} - {result['artist']}\n\n{result['lyrics']}"
    else:
        return "未找到歌词"

Entertainment Digest
def get_entertainment_digest():
    # Music
    music_rank = requests.get('https://60s.viki.moe/v2/ncm-rank/3778678').json()
    top_song = music_rank['songs'][0]
    
    # Movies
    movies = requests.get('https://60s.viki.moe/v2/maoyan/realtime/movie').json()
    top_movie = movies['data'][0]
    
    # TV shows
    shows = requests.get('https://60s.viki.moe/v2/maoyan/realtime/tv').json()
    top_show = shows['data'][0]
    
    digest = f"""
🎭 娱乐资讯速递

🎵 音乐：{top_song['name']} - {top_song['artist']}
🎬 电影：{top_movie['name']} 票房{top_movie['box_office']}
📺 电视剧：{top_show['name']} 收视率{top_show['rating']}
    """
    
    return digest

Example Interactions
User: "现在什么歌最火？"
response = requests.get('https://60s.viki.moe/v2/ncm-rank/3778678')
songs = response.json()

print("🎵 网易云飙升榜 TOP 5")
for i, song in enumerate(songs['songs'][:5], 1):
    print(f"{i}. {song['name']} - {song['artist']}")

User: "帮我找《稻香》的歌词"
data = {'keyword': '稻香'}
response = requests.post('https://60s.viki.moe/v2/lyric', json=data)
result = response.json()

print(f"🎤 {result['song']} - {result['artist']}\n")
print(result['lyrics'])

User: "今天电影票房排行"
response = requests.get('https://60s.viki.moe/v2/maoyan/realtime/movie')
movies = response.json()

print("🎬 实时票房排行")
for movie in movies['data'][:5]:
    print(f"{movie['rank']}. {movie['name']} - {movie['box_office']}")

Best Practices
Music Ranks: Cache rank lists as they don't change frequently
Lyrics: Include artist name in search for better accuracy
Box Office: Data updates frequently, show timestamp
Error Handling: Handle cases where lyrics or data not found
Formatting: Present data in a clean, readable format
Related Resources
60s API Documentation
GitHub Repository
Weekly Installs
78
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