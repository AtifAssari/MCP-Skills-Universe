---
rating: ⭐⭐⭐
title: ocr-service
url: https://skills.sh/lin-a1/skills-agent/ocr-service
---

# ocr-service

skills/lin-a1/skills-agent/ocr-service
ocr-service
Installation
$ npx skills add https://github.com/lin-a1/skills-agent --skill ocr-service
SKILL.md
功能

从图像中提取文字内容，支持多种图像格式和语言。

调用方式
from services.ocr_service.client import OCRServiceClient

client = OCRServiceClient()

# 健康检查
status = client.health_check()

# OCR识别
image_base64 = client.image_to_base64("/path/to/image.jpg")
result = client.ocr(image_base64)

# 获取识别结果
texts = result["rec_texts"]    # ["识别的文字1", "识别的文字2", ...]
scores = result["rec_scores"]  # [0.98, 0.95, ...]

返回格式
{
  "doc_preprocessor_res": {"angle": 0},
  "dt_polys": [[x1,y1], [x2,y2], ...],
  "rec_texts": ["识别的文字1", "识别的文字2"],
  "rec_scores": [0.98, 0.95]
}

字段说明
rec_texts: 识别出的文字列表
rec_scores: 每个文字块的置信度
dt_polys: 检测到的文本区域坐标
Weekly Installs
116
Repository
lin-a1/skills-agent
GitHub Stars
7
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn