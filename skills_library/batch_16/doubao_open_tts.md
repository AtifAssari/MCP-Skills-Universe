---
title: doubao-open-tts
url: https://skills.sh/xdrshjr/jr-openclaw-skills/doubao-open-tts
---

# doubao-open-tts

skills/xdrshjr/jr-openclaw-skills/doubao-open-tts
doubao-open-tts
Installation
$ npx skills add https://github.com/xdrshjr/jr-openclaw-skills --skill doubao-open-tts
SKILL.md
Doubao Open TTS

Text-to-Speech (TTS) service using Doubao (Volcano Engine) API V1 interface to convert text into natural-sounding speech.

Features
🎙️ 200+ Voice Options - Default: Shiny (灿灿) for general scenarios
🔊 Multiple Audio Formats - Supports mp3, pcm, wav
⚡ Adjustable Parameters - Speed and volume control
📦 Dual Interface - Command-line tool + Python API
🎯 Voice Categorization - Browse voices by category
Installation
cd skills/doubao-open-tts
pip install -r requirements.txt

Configuration
Method 1: Environment Variables
export VOLCANO_TTS_APPID="your_app_id"
export VOLCANO_TTS_ACCESS_TOKEN="your_access_token"
export VOLCANO_TTS_SECRET_KEY="your_secret_key"
export VOLCANO_TTS_VOICE_TYPE="zh_female_cancan_mars_bigtts"  # Optional: set default voice

Method 2: .env File

Copy .env.example.txt to .env and fill in your credentials:

cp .env.example.txt .env
# Edit the .env file with your credentials

Usage
Command Line
# Basic usage (uses default voice: Shiny)
python scripts/tts.py "Hello, this is a test of Doubao text-to-speech service"

# Specify output file and format
python scripts/tts.py "Welcome to use TTS" -o output.mp3 -e mp3

# Read text from file
python scripts/tts.py -f input.txt -o output.mp3

# Adjust parameters
python scripts/tts.py "Custom voice" --speed 1.2 --volume 0.8 -v zh_female_cancan_mars_bigtts

# List all available voices
python scripts/tts.py --list-voices

# List voices by category
python scripts/tts.py --list-voices --category "General-Multilingual"

# Use different cluster
python scripts/tts.py "Hello" --cluster volcano_tts

# Enable debug mode
python scripts/tts.py "Test" --debug

Python API
from scripts.tts import VolcanoTTS, VOICE_TYPES, VOICE_CATEGORIES

# Initialize client
tts = VolcanoTTS(
    app_id="your_app_id",
    access_token="your_access_token",
    secret_key="your_secret_key",
    voice_type="zh_female_cancan_mars_bigtts"  # Optional: set default voice
)

# List available voices
print("All voices:", tts.list_voices())
print("General voices:", tts.list_voices("General-Normal"))

# Change voice
tts.set_voice("zh_male_xudong_conversation_wvae_bigtts")  # Set to "Happy Xiaodong"

# Synthesize speech
output_path = tts.synthesize(
    text="Hello, this is Doubao text-to-speech",
    voice_type="zh_female_cancan_mars_bigtts",  # Optional: override default
    encoding="mp3",
    cluster="volcano_tts",
    speed=1.0,
    volume=1.0,
    output_file="output.mp3"
)
print(f"Audio saved to: {output_path}")

Available Voice Types
General Category (通用场景)
Voice Name	Voice Type	Description
Shiny (灿灿)	zh_female_cancan_mars_bigtts	Cheerful female voice, suitable for various scenarios
Lively Xiaoning (活泼小宁)	zh_female_wanwanxiaohe_mars_bigtts	Lively and playful female voice
Xiaomo (小莫)	zh_male_xiaomo_mars_bigtts	Warm and friendly male voice
Xiaoqi (小琪)	zh_female_xiaoqi_mars_bigtts	Professional female host
AISuper (AI超级大流利)	zh_female_gaolanfenqu_mars_bigtts	Super fluent female voice
Emotional Category (情感超自然人声)
Voice Name	Voice Type	Description
Happy Xiaodong (开心小东)	zh_male_xudong_conversation_wvae_bigtts	Cheerful and sunny male voice
Sad Xiaoliang (悲伤小亮)	zh_male_sadxiaoliang_sad_mars_bigtts	Melancholic male voice
Neutral Xiaoshuai (中性小帅)	zh_male_zhongxingxiaoshuai_speech_mars_bigtts	Neutral tone male voice
Happy Xiaomei (开心小美)	zh_female_gaoxiaomei_happy_mars_bigtts	Cheerful female voice
Angry Xiaotian (愤怒小甜)	zh_female_shengmoxiaotian_angry_mars_bigtts	Angry tone female voice
Intelligent Customer Service (智能客服)
Voice Name	Voice Type	Description
Customer Service Xiaowen (客服小文)	zh_male_jingyixiaowen_mars_bigtts	Professional customer service male voice
Customer Service Xiaorou (客服小柔)	zh_female_xiaorou_customer_service_mars_bigtts	Gentle customer service female voice
Documentary (纪录片)
Voice Name	Voice Type	Description
Classic Xiaoming (经典小明)	zh_male_jingdianxiaoming_mars_bigtts	Classic documentary male voice
Narration Xiaoran (旁白小然)	zh_female_xiaoran_narration_mars_bigtts	Documentary narration female voice
Audio Novels (有声小说)
Voice Name	Voice Type	Description
Storytelling Xiaotao (讲书小桃)	zh_female_jiangshuxiaotao_mars_bigtts	Storytelling female voice
Warm Xiaochen (温暖小晨)	zh_male_wennuanxiaochen_mars_bigtts	Warm novel reading male voice
News Broadcasting (新闻播报)
Voice Name	Voice Type	Description
News Xiaozhi (新闻小志)	zh_male_xinwenxiaozhi_mars_bigtts	Standard news broadcasting male voice
News Xiaojing (新闻小静)	zh_female_xinwenxiaojing_mars_bigtts	Professional news broadcasting female voice
Cantonese News (粤语新闻)	zh_male_yueyuxiaowu_mars_bigtts	Cantonese news male voice
Amoy News (闽南语新闻)	zh_female_minnanxiaoyue_mars_bigtts	Amoy dialect news female voice
General-Multilingual (通用多语言)
Voice Name	Voice Type	Description
English Gentle (英语男声-柔和)	en_male_mars_bigtts	Gentle English male voice
English Lively (英语女声-活泼)	en_female_mars_bigtts	Lively English female voice
Japanese Male (日语男声)	ja_male_mars_bigtts	Japanese male voice
Japanese Female (日语女声)	ja_female_mars_bigtts	Japanese female voice
Korean Male (韩语男声)	ko_male_mars_bigtts	Korean male voice
Korean Female (韩语女声)	ko_female_mars_bigtts	Korean female voice
French Male (法语男声)	fr_male_mars_bigtts	French male voice
French Female (法语女声)	fr_female_mars_bigtts	French female voice
German Male (德语男声)	de_male_mars_bigtts	German male voice
German Female (德语女声)	de_female_mars_bigtts	German female voice
Spanish Male (西班牙语男声)	es_male_mars_bigtts	Spanish male voice
Spanish Female (西班牙语女声)	es_female_mars_bigtts	Spanish female voice
Russian Male (俄语男声)	ru_male_mars_bigtts	Russian male voice
Russian Female (俄语女声)	ru_female_mars_bigtts	Russian female voice
Portuguese Male (葡萄牙语男声)	pt_male_mars_bigtts	Portuguese male voice
Portuguese Female (葡萄牙语女声)	pt_female_mars_bigtts	Portuguese female voice
Italian Male (意大利语男声)	it_male_mars_bigtts	Italian male voice
Italian Female (意大利语女声)	it_female_mars_bigtts	Italian female voice
Arabic Male (阿拉伯语男声)	ar_male_mars_bigtts	Arabic male voice
Arabic Female (阿拉伯语女声)	ar_female_mars_bigtts	Arabic female voice
Hindi Male (印地语男声)	hi_male_mars_bigtts	Hindi male voice
Hindi Female (印地语女声)	hi_female_mars_bigtts	Hindi female voice
Thai Male (泰语男声)	th_male_mars_bigtts	Thai male voice
Thai Female (泰语女声)	th_female_mars_bigtts	Thai female voice
Vietnamese Male (越南语男声)	vi_male_mars_bigtts	Vietnamese male voice
Vietnamese Female (越南语女声)	vi_female_mars_bigtts	Vietnamese female voice
Indonesian Male (印尼语男声)	id_male_mars_bigtts	Indonesian male voice
Indonesian Female (印尼语女声)	id_female_mars_bigtts	Indonesian female voice
Malay Male (马来语男声)	ms_male_mars_bigtts	Malay male voice
Malay Female (马来语女声)	ms_female_mars_bigtts	Malay female voice
Filipino Male (菲律宾语男声)	fil_male_mars_bigtts	Filipino male voice
Filipino Female (菲律宾语女声)	fil_female_mars_bigtts	Filipino female voice
Turkish Male (土耳其语男声)	tr_male_mars_bigtts	Turkish male voice
Turkish Female (土耳其语女声)	tr_female_mars_bigtts	Turkish female voice
Dutch Male (荷兰语男声)	nl_male_mars_bigtts	Dutch male voice
Dutch Female (荷兰语女声)	nl_female_mars_bigtts	Dutch female voice
Polish Male (波兰语男声)	pl_male_mars_bigtts	Polish male voice
Polish Female (波兰语女声)	pl_female_mars_bigtts	Polish female voice
Ukrainian Male (乌克兰语男声)	uk_male_mars_bigtts	Ukrainian male voice
Ukrainian Female (乌克兰语女声)	uk_female_mars_bigtts	Ukrainian female voice
Hebrew Male (希伯来语男声)	he_male_mars_bigtts	Hebrew male voice
Hebrew Female (希伯来语女声)	he_female_mars_bigtts	Hebrew female voice
Dialect Category (方言场景)
Voice Name	Voice Type	Description
Cantonese Male (粤语男声)	zh_male_yueyuzhongxing_mars_bigtts	Cantonese male voice
Cantonese Female (粤语女声)	zh_female_yueyumars_mars_bigtts	Cantonese female voice
Amoy Male (闽南语男声)	zh_male_taiminmars_mars_bigtts	Amoy dialect male voice
Amoy Female (闽南语女声)	zh_female_minnanAImars_mars_bigtts	Amoy dialect female voice
Sichuanese (四川话)	zh_male_sichuanmars_mars_bigtts	Sichuan dialect male voice
Shanghainese (上海话)	zh_female_shanghaihuamars_mars_bigtts	Shanghainese female voice
Wuhan Dialect (武汉话)	zh_male_wuhanmars_mars_bigtts	Wuhan dialect male voice
Hunan Dialect (湖南话)	zh_male_hunanmars_mars_bigtts	Hunan dialect male voice
Henan Dialect (河南话)	zh_female_henanmars_mars_bigtts	Henan dialect female voice
Northeastern Dialect (东北话)	zh_male_dongbeimars_mars_bigtts	Northeastern dialect male voice
Shandong Dialect (山东话)	zh_male_shandongmars_mars_bigtts	Shandong dialect male voice
Tianjin Dialect (天津话)	zh_female_tianjinmars_mars_bigtts	Tianjin dialect female voice
Special Categories
Voice Name	Voice Type	Description
Audiobook Xiaoyu (有声小予)	zh_female_xiaoyujingxisanguo_mars_bigtts	Three Kingdoms audiobook voice
Animation Xiaohua (动漫小花)	zh_female_xiaohuadongman_mars_bigtts	Anime style voice
Rap Xiaoqiang (Rap小蔷)	zh_female_xiaoqiangrap_mars_bigtts	Rap style female voice
RAP General (Rap大将)	zh_male_rapgeneral_mars_bigtts	Rap style male voice
Wise Voice (智慧的声音)	zh_male_jinyumars_mars_bigtts	Wise and mature voice
Chattering (唠唠叨叨)	zh_female_laolaodaodao_chat_mars_bigtts	Chatty female voice
Talking Beijing (讲话北京)	zh_male_jianghuabeijing_speech_mars_bigtts	Beijing accent
Host Xiaoyang (主播小羊)	zh_female_xiaoyang_host_mars_bigtts	Streamer host style
Output

The generated audio file will be saved to the specified output path (default: output.mp3 in current directory).

Notes
Ensure VOLCANO_TTS_APPID, VOLCANO_TTS_ACCESS_TOKEN, and VOLCANO_TTS_SECRET_KEY environment variables are set
Supports mp3, pcm, and wav formats (mp3 by default)
Speed range: 0.8-2.0 (1.0 is normal)
Volume range: 0.1-3.0 (1.0 is normal)
Voice types can be viewed using --list-voices
Different clusters may support different voice types; default cluster is volcano_tts
For non-Chinese text, use multilingual voices from "General-Multilingual" category
Weekly Installs
90
Repository
xdrshjr/jr-open…w-skills
GitHub Stars
1
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass