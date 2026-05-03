---
title: videocut-install
url: https://skills.sh/zrt-ai-lab/opencode-skills/videocut-install
---

# videocut-install

skills/zrt-ai-lab/opencode-skills/videocut-install
videocut-install
Installation
$ npx skills add https://github.com/zrt-ai-lab/opencode-skills --skill videocut-install
SKILL.md
安装

首次使用前的环境准备

快速使用
用户: 安装环境
用户: 初始化
用户: 下载模型

依赖清单
依赖	用途	安装命令
funasr	口误识别	pip install funasr
modelscope	模型下载	pip install modelscope
openai-whisper	字幕生成	pip install openai-whisper
ffmpeg	视频剪辑	brew install ffmpeg
模型清单
FunASR 模型（口误识别用）

首次运行自动下载到 ~/.cache/modelscope/：

模型	大小	用途
paraformer-zh	953MB	语音识别（带时间戳）
punc_ct	1.1GB	标点预测
fsmn-vad	4MB	语音活动检测
小计	~2GB	
Whisper 模型（字幕生成用）

首次运行自动下载到 ~/.cache/whisper/：

模型	大小	用途
large-v3	2.9GB	字幕转录（质量最好）
总计

约 5GB 模型文件

安装流程
1. 安装 Python 依赖
       ↓
2. 安装 FFmpeg
       ↓
3. 下载 FunASR 模型（口误识别）
       ↓
4. 下载 Whisper 模型（字幕生成）
       ↓
5. 验证环境

执行步骤
1. 安装 Python 依赖
pip install funasr modelscope openai-whisper

2. 安装 FFmpeg
# macOS
brew install ffmpeg

# Ubuntu
sudo apt install ffmpeg

# 验证
ffmpeg -version

3. 下载 FunASR 模型（约2GB）
from funasr import AutoModel

model = AutoModel(
    model="paraformer-zh",
    vad_model="fsmn-vad",
    punc_model="ct-punc",
)
print("FunASR 模型下载完成")

4. 下载 Whisper 模型（约3GB）
import whisper

model = whisper.load_model("large-v3")
print("Whisper 模型下载完成")

5. 验证环境
from funasr import AutoModel

model = AutoModel(
    model="paraformer-zh",
    vad_model="fsmn-vad",
    punc_model="ct-punc",
    disable_update=True
)

# 测试转录（用任意音频/视频）
result = model.generate(input="test.mp4")
print("文本:", result[0]['text'][:50])
print("时间戳数量:", len(result[0]['timestamp']))
print("✅ 环境就绪")

常见问题
Q1: 模型下载慢

解决：使用国内镜像或手动下载

Q2: ffmpeg 命令找不到

解决：确认已安装并添加到 PATH

which ffmpeg  # 应该输出路径

Q3: funasr 导入报错

解决：检查 Python 版本（需要 3.8+）

python3 --version

Weekly Installs
36
Repository
zrt-ai-lab/open…e-skills
GitHub Stars
193
First Seen
Feb 4, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass