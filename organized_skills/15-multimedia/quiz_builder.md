---
rating: ⭐⭐⭐
title: quiz-builder
url: https://skills.sh/bingo-taiwan/claude-code-skills/quiz-builder
---

# quiz-builder

skills/bingo-taiwan/claude-code-skills/quiz-builder
quiz-builder
Installation
$ npx skills add https://github.com/bingo-taiwan/claude-code-skills --skill quiz-builder
SKILL.md
LINE Bot 題庫建立指南
專案資訊（2026-01-19 更新）
⚠️ 重要：兩個 Bot 的區別
Bot 名稱	Webhook URL	config.php 位置
Dietitian Dilbert（主要）	https://lt4.mynet.com.tw/linebot/webhook.php	/linebot/config.php
Quiz Bot（測試用）	https://lt4.mynet.com.tw/linebot/quiz/webhook.php	/linebot/quiz/config.php

修改題庫章節時，必須修改 /linebot/config.php，不是 /linebot/quiz/config.php！

路徑對照表
項目	路徑/URL
主 Bot config	/home/lt4.mynet.com.tw/public_html/linebot/config.php
題庫 JSON 目錄	/home/lt4.mynet.com.tw/public_html/linebot/quiz/
圖片 URL	https://lt4.mynet.com.tw/linebot/images/
核心程式庫	/home/lt4.mynet.com.tw/linebot_core/
檔案結構（2026-01-19 更新）
/home/lt4.mynet.com.tw/
│
├── linebot_core/              # 共用程式庫
│   ├── LineBot.php
│   ├── Analytics.php
│   └── ...
│
└── public_html/linebot/
    │
    │  # ===== 主 Bot：Dietitian Dilbert =====
    ├── webhook.php            # ⭐ 主 Webhook
    ├── config.php             # ⭐ 主設定（修改章節改這裡！）
    ├── handlers/
    │   └── MainHandler.php
    ├── data/
    │   └── sessions.json
    │
    │  # ===== 題庫 JSON（供主 Bot 使用）=====
    ├── quiz/
    │   ├── chemistry/         # 普通化學（29 章節）
    │   │   ├── {chapter}-quiz.json
    │   │   └── {chapter}-answers.json
    │   ├── physiology/        # 人體生理學（6 章節）
    │   ├── nutrition/         # 營養學（2 章節）
    │   ├── biology/           # 普通生物學（9 章節）
    │   │   ├── ch1-intro-biology-quiz.json
    │   │   ├── ch1-1-lecture-simulation-quiz.json  # 講義模擬試題
    │   │   └── ...
    │   │
    │   │  # --- 以下是獨立 Quiz Bot（測試用）---
    │   ├── config.php         # 另一個 Bot 的設定
    │   ├── webhook.php        # 另一個 Bot 的 Webhook
    │   └── handlers/
    │
    └── images/                # 共用圖片

命名規則
檔案命名
ch{章}-{節}-{英文主題}-quiz.json
ch{章}-{節}-{英文主題}-answers.json


範例：

ch2-1-classification-quiz.json - 2.1 物質的分類
ch3-4-atomic-number-mass-quiz.json - 3.4 原子序與質量數
ch5-3-naming-ionic-compounds-quiz.json - 5.3 離子化合物命名
config.php 對應
'chapters' => [
    'ch2-1-classification' => '2.1 物質的分類',
    'ch3-4-atomic-number-mass' => '3.4 原子序與質量數',
]


注意：config.php 的 key 要與檔名前綴一致（不含 -quiz.json）

JSON 格式規範
題目檔 (*-quiz.json)
{
  "metadata": {
    "title": "章節標題（中文）",
    "subject": "普通化學",
    "chapter": "2",
    "section": "2.1",
    "topic": "English Topic Name",
    "description": "本章節涵蓋的內容說明",
    "total_questions": 30,
    "version": "1.0",
    "created_date": "2026-01-06"
  },
  "questions": [
    {
      "id": 1,
      "question": "題目文字",
      "question_image": null,
      "options": {
        "A": "選項A",
        "B": "選項B",
        "C": "選項C",
        "D": "選項D"
      },
      "options_image": null
    }
  ]
}

答案檔 (*-answers.json)
{
  "metadata": {
    "title": "章節標題 - 答案與解析",
    "subject": "普通化學",
    "chapter": "2",
    "section": "2.1",
    "total_questions": 30,
    "version": "1.0",
    "created_date": "2026-01-06"
  },
  "answers": [
    {
      "id": 1,
      "answer": "C",
      "explanation": "詳細解釋為什麼答案是 C...",
      "explanation_image": null
    }
  ]
}

題目設計原則
每節題目數量
標準：每節 30 題
分布：基礎概念 10 題、應用計算 10 題、進階理解 10 題
題目類型分配
類型	數量	說明
定義/概念	8-10 題	基本名詞定義
判斷/比較	6-8 題	比較差異、判斷正誤
計算題	5-8 題	數值計算（視章節）
應用題	4-6 題	生活應用、實驗情境
圖表題	2-4 題	需要圖片的題目
題目撰寫要點
題幹清晰：避免歧義，一題一問
選項對等：長度相近，格式一致
干擾項合理：常見錯誤概念
答案明確：只有一個最佳答案
圖片規範
圖片命名
ch{章}-{節}-q{題號}-{描述}.png      # 題目圖片
ch{章}-{節}-a{題號}-{描述}-answer.png  # 答案解析圖片


範例：

ch2-7-q12-heating-curve.png - 題目圖
ch2-7-a12-heating-curve-answer.png - 答案解析圖
圖片 URL 格式
https://lt4.mynet.com.tw/linebot/images/{檔名}.png

需要圖片的題目類型
加熱/冷卻曲線圖
相圖 (Phase Diagram)
週期表區域標示
原子/分子結構圖
路易士結構式
離子晶格結構
實驗裝置圖
數據比較圖表
建立流程
Step 1：規劃題目
## 章節：2.7 狀態變化

### 主題涵蓋
- 熔化、凝固、汽化、凝結、昇華、凝華
- 熔化熱、汽化熱
- 加熱曲線
- 相圖

### 題目分配
- 定義題：10 題 (Q1-10)
- 計算題：8 題 (Q11-18)
- 應用題：8 題 (Q19-26)
- 圖表題：4 題 (Q12, Q15, Q27, Q30)

Step 2：建立題目檔

使用 Write 工具建立 JSON：

# 檔案路徑
C:\Users\user\linebot-quiz\quiz\chemistry\ch2-7-state-changes-quiz.json

Step 3：建立答案檔
# 檔案路徑
C:\Users\user\linebot-quiz\quiz\chemistry\ch2-7-state-changes-answers.json

Step 4：驗證 JSON
cd /c/Users/user/linebot-quiz
python -m json.tool quiz/chemistry/ch2-7-state-changes-quiz.json > /dev/null && echo "Quiz JSON valid"
python -m json.tool quiz/chemistry/ch2-7-state-changes-answers.json > /dev/null && echo "Answers JSON valid"

Step 5：更新 config.php
'ch2-7-state-changes' => '2.7 狀態變化',

Step 6：推送到 GitHub
cd /c/Users/user/linebot-quiz
git add .
git commit -m "新增 2.7 狀態變化 (30題)"
git push origin master

Step 7：部署到伺服器
# 同步題庫
scp quiz/chemistry/ch2-7-*.json lt4:/home/lt4.mynet.com.tw/public_html/linebot/quiz/chemistry/

# 更新 config.php
scp config.php lt4:/home/lt4.mynet.com.tw/public_html/linebot/

批量建立技巧
使用 TodoWrite 追蹤進度
- [ ] 2.1 物質的分類 (30題)
- [ ] 2.2 物質的狀態與性質 (30題)
- [x] 2.3 溫度 (30題) ✓

平行建立多章節

同時建立題目檔和答案檔，減少來回切換：

1. 規劃所有章節的題目大綱
2. 逐一建立 quiz.json
3. 逐一建立 answers.json
4. 批量驗證
5. 一次性推送

驗證清單
 JSON 語法正確（python -m json.tool）
 題目數量正確（30題）
 id 從 1 開始連續編號
 每題都有 4 個選項 (A/B/C/D)
 答案只有一個字母
 圖片 URL 格式正確
 config.php 已更新
 Git 已推送
 伺服器已同步
題庫自動化審計（2026-01-13 新增）
審計腳本功能

建立 Python 腳本自動檢測題目與答案的適配問題：

# audit_quiz.py

# 圖片關鍵字 - 題目提到這些字眼但沒圖片時發出警告
IMAGE_KEYWORDS = ['上圖', '下圖', '圖中', '看圖', '圖片', '圖表', '圖示', '觀察圖']

# 無意義選項 - 選項只有 A/B/C/D 沒有實際內容
MEANINGLESS_OPTIONS = [
    {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D'},
    {'A': '選項A', 'B': '選項B', 'C': '選項C', 'D': '選項D'},
]

def audit_quiz_file(quiz_path):
    """審計單一題庫檔案"""
    issues = []

    with open(quiz_path, 'r', encoding='utf-8') as f:
        quiz_data = json.load(f)

    for q in quiz_data.get('questions', []):
        qid = q['id']
        question_text = q['question']
        question_image = q.get('question_image')
        options = q.get('options', {})

        # 檢查 1：題目提到圖但沒有圖片
        needs_image = any(kw in question_text for kw in IMAGE_KEYWORDS)
        if needs_image and not question_image:
            issues.append({
                'id': qid,
                'type': 'missing_image',
                'detail': 'Question mentions image but question_image is null'
            })

        # 檢查 2：無意義選項
        if options in MEANINGLESS_OPTIONS:
            issues.append({
                'id': qid,
                'type': 'meaningless_options',
                'detail': 'Options are just A/B/C/D with no content'
            })

        # 檢查 3：圖片 URL 不可存取
        if question_image:
            if not check_image_url(question_image):
                issues.append({
                    'id': qid,
                    'type': 'broken_image',
                    'detail': 'Image URL returns non-200 status'
                })

    return issues

審計輸出範例
[Nutrition] ch7-protein-quiz.json: 46/50 OK, 4 issues
  - Q9: missing_image
  - Q10: missing_image
  - Q18: meaningless_options
  - Q29: missing_image

TOTAL: 326/330 OK (4 issues)

問題修復方式
問題類型	修復方法
missing_image	用 matplotlib 生成圖片並上傳，更新 JSON 中的 question_image
meaningless_options	修改選項為有意義的內容（如「鍵結 A」「胺基酸 A」）
broken_image	檢查 URL 路徑，確認圖片已上傳至伺服器
圖片 URL 快取破壞

修復圖片後，記得加上版本參數避免 LINE 快取：

"question_image": "https://lt4.mynet.com.tw/linebot/images/ch7-q9-peptide-bond.png?v=1"

常見錯誤
題目文字方向性錯誤

問題：LINE Bot 的 Flex Message 中，圖片顯示在題目文字上方，但題目文字卻寫「下圖」。

// 錯誤：使用「下圖」
"question": "下圖顯示某些元素符號，標示 X 的元素是？"

// 正確：使用「上圖」
"question": "上圖顯示某些元素符號，標示 X 的元素是？"


批量修正：

ssh lt4 "cd /home/lt4.mynet.com.tw/public_html/linebot/quiz/chemistry && sed -i 's/下圖/上圖/g' *.json"

「標示 X」題目的圖片缺少 X 標記

問題：題目問「標示 X 的是什麼？」，但圖片中所有內容都完整顯示，沒有任何 X 標記。

正確做法：圖片中必須用 X 遮蓋答案，讓學生猜測。

題目類型	圖片應該顯示
「標示 X 的元素是？」答案：銅(Cu)	元素表中 Cu 的位置顯示紅色 X
「標示 X 的區域是？」答案：過渡金屬	週期表中過渡金屬區域顯示 X
「標示 X 的部分是？」答案：原子核	原子結構圖中原子核位置顯示 X

Python 範例（用 PIL 加入 X 標記）：

from PIL import Image, ImageDraw, ImageFont

def add_x_mark(draw, x, y, font_size=72, color='red'):
    """在指定位置加入 X 標記"""
    font = ImageFont.truetype("C:/Windows/Fonts/msjh.ttc", font_size)
    draw.text((x, y), "X", font=font, fill=color, anchor='mm')

「標示 X」圖片必須有邏輯可循

問題：圖片中的元素隨意排列，即使有 X 標記，學生也無法從規律推斷答案，等於盲猜。

錯誤示範：

隨便放 12 個元素（H, C, N, O, Na, Mg...），把其中一個改成 X
學生無法從排列規律判斷 X 是什麼

正確做法：圖片排列必須有邏輯，讓學生可以根據規律推斷答案。

題目	正確設計
「原子序 29，標示 X 的元素是？」	按週期表順序排列：K(19)→Ca(20)→...→Ni(28)→X(29)→Zn(30)
「3-12族，標示 X 的區域是？」	顯示 s區(1-2族)、X(3-12族)、p區(13-18族)

範例：有邏輯的元素符號圖

# 按週期表第四週期順序排列，顯示原子序
elements = [
    ('K', '鉀', '19'),
    ('Ca', '鈣', '20'),
    ('Fe', '鐵', '26'),
    ('Co', '鈷', '27'),
    ('Ni', '鎳', '28'),
    ('X', '?', '29'),   # Cu 遮蓋成 X
    ('Zn', '鋅', '30'),
]
# 學生看到原子序 29，可推斷是 Cu（銅）


字體大小建議（PIL/Pillow）：

title_font = get_font(60)      # 標題
element_font = get_font(72)    # 元素符號/X 標記
number_font = get_font(36)     # 原子序
chinese_font = get_font(40)    # 中文名稱
question_font = get_font(44)   # 題目文字

圖片與題目不匹配的排查

檢查清單：

圖片中是否有題目描述的標記（X、箭頭、問號等）
圖片中標記的位置是否對應正確答案
題目文字的方向描述（上圖/下圖）是否正確

排查指令：

# 找出所有「標示 X」的題目
ssh lt4 "grep -rn '標示.*X' /home/lt4.mynet.com.tw/public_html/linebot/quiz/*/*.json"

# 列出這些題目對應的圖片 URL
ssh lt4 "grep -B1 '標示.*X' /home/lt4.mynet.com.tw/public_html/linebot/quiz/*/*.json | grep question_image"

JSON 語法錯誤
// 錯誤：最後一項有逗號
{"id": 30, "answer": "C", "explanation": "..."},
]

// 正確：最後一項無逗號
{"id": 30, "answer": "C", "explanation": "..."}
]

選項格式錯誤
// 錯誤：選項是陣列
"options": ["A選項", "B選項", "C選項", "D選項"]

// 正確：選項是物件
"options": {"A": "選項A", "B": "選項B", "C": "選項C", "D": "選項D"}

圖片路徑錯誤
// 錯誤：相對路徑
"question_image": "images/ch2-7-q12.png"

// 正確：完整 URL
"question_image": "https://lt4.mynet.com.tw/linebot/images/ch2-7-q12-heating-curve.png"

範本
快速建立範本

複製此範本開始新章節：

{
  "metadata": {
    "title": "【填入中文標題】",
    "subject": "普通化學",
    "chapter": "【章】",
    "section": "【章.節】",
    "topic": "【English Topic】",
    "description": "【描述】",
    "total_questions": 30,
    "version": "1.0",
    "created_date": "【YYYY-MM-DD】"
  },
  "questions": [
    {"id": 1, "question": "", "question_image": null, "options": {"A": "", "B": "", "C": "", "D": ""}, "options_image": null}
  ]
}

圖片生成指南（手機可讀性）
重要：LINE Bot 圖片字體大小

LINE Bot 在手機上顯示圖片時，使用者無法放大圖片。因此圖片中的文字必須足夠大才能閱讀。

建議字體大小
用途	字體大小	說明
標題	48pt	圖片主標題
標籤	36pt	重要元素標籤
說明文字	32pt	一般解說文字
小字	28pt	次要資訊（最小不要低於此）

注意：原本建議的 36/28/24/20pt 在 LINE Bot 手機上仍可能太小，建議使用上述更大的字體。

Python 圖片生成範本

使用 matplotlib 生成教育圖片：

# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Ellipse
import os

# 中文字體設定
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 字體大小常數（適合手機閱讀）
FONT_TITLE = 36
FONT_LABEL = 28
FONT_TEXT = 24
FONT_SMALL = 20

# 輸出目錄
OUTPUT_DIR = r"C:\Users\user\Documents\temp\images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_fig(fig, filename):
    """儲存圖片 - 150 DPI 足夠清晰且檔案不會太大"""
    filepath = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(filepath, dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"已儲存: {filename}")

def create_example_diagram():
    """範例圖片生成函數"""
    fig, ax = plt.subplots(figsize=(14, 10))  # 14x10 英寸
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # 標題
    ax.set_title('圖片標題', fontsize=FONT_TITLE, fontweight='bold', pad=20)

    # 繪製內容...
    box = FancyBboxPatch((2, 3), 4, 3, boxstyle="round,pad=0.1",
                         facecolor='#BBDEFB', edgecolor='#1565C0', linewidth=2)
    ax.add_patch(box)
    ax.text(4, 4.5, '標籤文字', ha='center', fontsize=FONT_LABEL, fontweight='bold')
    ax.text(4, 3.5, '說明文字', ha='center', fontsize=FONT_TEXT)

    save_fig(fig, 'example-diagram.png')

圖片生成腳本組織

建議為每個章節建立獨立的 Python 腳本：

C:\Users\user\Documents\temp\
├── generate_physiology_ch1_large.py
├── generate_physiology_ch2_large.py
├── generate_physiology_ch7_large.py
├── generate_physiology_ch8_large.py
├── generate_physiology_ch17_large.py
└── images/
    ├── ch1-a3-organization-levels.png
    ├── ch1-a9-negative-feedback.png
    └── ...

圖片命名規則

人體生理學（無小節）：

ch{章}-a{題號}-{英文描述}.png


範例：ch8-a9-neuron-structure.png

普通化學（有小節）：

ch{章}-{節}-a{題號}-{英文描述}.png


範例：ch2-7-a12-heating-curve-answer.png

常用 matplotlib 元件
from matplotlib.patches import (
    FancyBboxPatch,  # 圓角方框
    Circle,          # 圓形
    Ellipse,         # 橢圓
    Polygon,         # 多邊形
    Rectangle,       # 矩形
)

# 圓角方框
box = FancyBboxPatch((x, y), width, height,
                     boxstyle="round,pad=0.1",
                     facecolor='#BBDEFB',
                     edgecolor='#1565C0',
                     linewidth=2)

# 箭頭
ax.annotate('', xy=(end_x, end_y), xytext=(start_x, start_y),
            arrowprops=dict(arrowstyle='->', color='#424242', lw=2))

# 雙向箭頭
ax.annotate('', xy=(x2, y), xytext=(x1, y),
            arrowprops=dict(arrowstyle='<->', color='#424242', lw=2))

配色建議

使用 Material Design 色彩，易於辨識：

顏色	填充色	邊框色	用途
藍色	#BBDEFB	#1565C0	一般元素
綠色	#C8E6C9	#2E7D32	正確/正面
紅色	#FFCDD2	#C62828	警告/重點
橘色	#FFE0B2	#E65100	次要元素
紫色	#E1BEE7	#7B1FA2	特殊標記
灰色	#ECEFF1	#607D8B	背景/中性
多科目支援
目前支援科目
$SUBJECTS = [
    'chemistry' => [
        'name' => '普通化學',
        'chapters' => [...]
    ],
    'physiology' => [
        'name' => '人體生理學',
        'chapters' => [...]
    ],
    'nutrition' => [
        'name' => '營養學',
        'chapters' => [
            'ch6-lipids' => '第六章 脂質',
            'ch7-protein' => '第七章 蛋白質',
        ]
    ],
];

檔案結構（多科目）
linebot-quiz/
├── config.php
├── quiz/
│   ├── chemistry/
│   │   ├── ch2-1-classification-quiz.json
│   │   └── ch2-1-classification-answers.json
│   └── physiology/
│       ├── ch1-introduction-quiz.json
│       └── ch1-introduction-answers.json
└── images/
    ├── ch2-1-q30-classification.png  # 化學
    └── ch8-a9-neuron-structure.png   # 人體生理學

新增科目步驟
在 quiz/ 下建立科目目錄
在 config.php 的 $SUBJECTS 新增科目設定
建立題目和答案 JSON 檔案
生成所需圖片並上傳
部署注意事項
SSH 連線設定

確保 ~/.ssh/config 有正確設定：

Host lt4
    HostName 172.104.67.123
    User root
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes

批量上傳圖片
# 上傳特定章節圖片
scp "C:/Users/user/Documents/temp/images/ch8-a"*.png lt4:/home/lt4.mynet.com.tw/public_html/linebot/images/

# 上傳所有人體生理學圖片
scp "C:/Users/user/Documents/temp/images/ch1-a"*.png \
    "C:/Users/user/Documents/temp/images/ch2-a"*.png \
    "C:/Users/user/Documents/temp/images/ch7-a"*.png \
    "C:/Users/user/Documents/temp/images/ch8-a"*.png \
    "C:/Users/user/Documents/temp/images/ch17-a"*.png \
    lt4:/home/lt4.mynet.com.tw/public_html/linebot/images/

驗證上傳
ssh lt4 "ls /home/lt4.mynet.com.tw/public_html/linebot/images/ch*-a*.png | wc -l"

LINE 圖片快取問題與解決方案
問題描述

LINE 會積極快取圖片。當你更新伺服器上的圖片後，LINE 可能仍顯示舊版本（甚至空白圖片），因為 URL 沒變。

解決方案：快取破壞參數

在圖片 URL 後加入版本參數，強制 LINE 重新載入：

// 更新前
"explanation_image": "https://lt4.mynet.com.tw/linebot/images/ch2-2-a15-states-answer.png"

// 更新後（加入 ?v=2）
"explanation_image": "https://lt4.mynet.com.tw/linebot/images/ch2-2-a15-states-answer.png?v=2"

批量更新快取破壞參數
# 更新所有化學答案檔
ssh lt4 "cd /home/lt4.mynet.com.tw/public_html/linebot/quiz/chemistry && sed -i 's/\.png\"/\.png?v=2\"/g' *-answers.json"

# 更新所有人體生理學答案檔
ssh lt4 "cd /home/lt4.mynet.com.tw/public_html/linebot/quiz/physiology && sed -i 's/\.png\"/\.png?v=2\"/g' *-answers.json"

LINE Flex Message 圖片顯示優化
圖片比例設定

webhook.php 中的 aspectRatio 設定影響圖片顯示大小：

比例	效果	適用場景
16:9	寬扁，文字較小	橫向圖表
4:3	較高，文字較大	教育圖片（推薦）
1:1	正方形	圖標類
修改方式
// webhook.php 中的 hero 設定
$flexContents['hero'] = [
    'type' => 'image',
    'url' => $imageUrl,
    'size' => 'full',
    'aspectRatio' => '4:3',  // 改為 4:3 讓圖片更高
    'aspectMode' => 'fit'
];

Python 圖片生成進階技巧
超大字體設定（強烈建議）

原本的 36/28/24/20pt 在手機上仍可能太小。建議使用 48/36/32/28pt：

# 超大字體設定 (LINE Bot 手機閱讀優化)
FONT_TITLE = 48  # 標題
FONT_LABEL = 36  # 標籤
FONT_TEXT = 32   # 內文
FONT_SMALL = 28  # 小字（最小不要低於此）

save_fig 函數陷阱

問題：連續呼叫 save_fig 兩次會導致第二個檔案為空白！

# 錯誤示範
save_fig('ch2-2-q15-states.png')       # 正常儲存
save_fig('ch2-2-a15-states-answer.png') # 空白！因為 figure 已關閉

def save_fig(filename):
    plt.savefig(...)
    plt.close()  # 這行關閉了 figure


正確做法：修改 save_fig 同時儲存 q 和 a 版本：

def save_fig(fig, filename):
    """儲存圖片 - 同時儲存 q 和 a 兩種版本"""
    # 儲存 a 版本 (原始)
    filepath_a = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(filepath_a, dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"已儲存: {filename}")

    # 儲存 q 版本 (將 -a 改為 -q)
    if '-a' in filename:
        filename_q = filename.replace('-a', '-q', 1)
        filepath_q = os.path.join(OUTPUT_DIR, filename_q)
        fig.savefig(filepath_q, dpi=150, bbox_inches='tight',
                    facecolor='white', edgecolor='none')
        print(f"已儲存: {filename_q}")

    plt.close(fig)

完整範例腳本結構
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
import os

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

OUTPUT_DIR = r"C:\Users\user\Documents\temp\images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 超大字體
FONT_TITLE = 48
FONT_LABEL = 36
FONT_TEXT = 32
FONT_SMALL = 28

def save_fig(fig, filename):
    """儲存圖片 - 同時儲存 q 和 a 兩種版本"""
    filepath_a = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(filepath_a, dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"已儲存: {filename}")

    if '-a' in filename:
        filename_q = filename.replace('-a', '-q', 1)
        filepath_q = os.path.join(OUTPUT_DIR, filename_q)
        fig.savefig(filepath_q, dpi=150, bbox_inches='tight',
                    facecolor='white', edgecolor='none')
        print(f"已儲存: {filename_q}")

    plt.close(fig)

def create_example():
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('範例圖', fontsize=FONT_TITLE, fontweight='bold', pad=20)

    # ... 繪製內容 ...

    save_fig(fig, 'ch1-a1-example.png')  # 會同時生成 q 和 a 版本

if __name__ == '__main__':
    create_example()

故障排除
答案圖片不顯示

檢查 URL 是否正確：

ssh lt4 "grep 'explanation_image' /path/to/answers.json | head -3"


檢查圖片是否存在：

ssh lt4 "curl -I https://lt4.mynet.com.tw/linebot/images/ch2-2-a15-states-answer.png"


檢查圖片是否為空白（檔案很小可能是空白）：

ssh lt4 "ls -la /path/to/image.png"  # 小於 10KB 可能有問題
ssh lt4 "file /path/to/image.png"    # 確認是有效 PNG


加入快取破壞參數：

ssh lt4 "sed -i 's/\.png\"/\.png?v=2\"/g' /path/to/answers.json"

圖片文字太小
增加字體大小（至少 FONT_SMALL = 28）
修改 webhook.php 的 aspectRatio 為 4:3
重新生成圖片並上傳
更新快取破壞參數
伺服器部署安全須知（重要！）
config.php 敏感資訊保護

問題：本地的 config.php 包含佔位符，伺服器上的 config.php 包含真實的 LINE 憑證。使用 scp 同步時會覆蓋伺服器上的真實憑證，導致 LINE Bot 完全失效。

症狀：

LINE Bot 完全沒有反應
輸入任何文字都沒有回應
debug.log 顯示 Invalid signature

解決方案：

永遠不要直接同步 config.php 到伺服器：

# 危險！不要這樣做
scp config.php lt4:/home/lt4.mynet.com.tw/public_html/linebot/

# 安全做法：只同步題庫和 webhook
scp webhook.php lt4:/home/lt4.mynet.com.tw/public_html/linebot/
scp quiz/chemistry/*.json lt4:/home/lt4.mynet.com.tw/public_html/linebot/quiz/chemistry/


如果需要更新 config.php 的章節設定：

# 只更新章節設定，保留憑證
ssh lt4 "vim /home/lt4.mynet.com.tw/public_html/linebot/config.php"

# 或者用 sed 只修改特定行
ssh lt4 "sed -i \"/chapters/,/]/c\\NEW_CONTENT\" /path/to/config.php"


備份伺服器 config.php：

ssh lt4 "cp /home/lt4.mynet.com.tw/public_html/linebot/config.php /home/lt4.mynet.com.tw/public_html/linebot/config.php.bak"

LINE 憑證位置

如果憑證被覆蓋，需要到 LINE Developers Console 重新取得：

網址：https://developers.line.biz/console/
Channel access token：Messaging API → Channel access token (long-lived)
Channel secret：Basic settings → Channel secret
// 伺服器上的 config.php 應該包含真實憑證
define('LINE_CHANNEL_ACCESS_TOKEN', '實際的token...');
define('LINE_CHANNEL_SECRET', '實際的secret');

LINE Bot 調試技巧
添加調試日誌

當 LINE Bot 沒有反應時，在 webhook.php 開頭添加日誌功能：

<?php
// Debug 日誌
function logDebug($msg) {
    file_put_contents(__DIR__ . '/debug.log', date('Y-m-d H:i:s') . ' ' . $msg . "\n", FILE_APPEND);
}

// 在關鍵位置記錄
logDebug('=== Webhook called ===');
logDebug('Content: ' . substr($content, 0, 300));

在 replyMessages 添加 API 回應日誌
function replyMessages($replyToken, $messages) {
    // ... 原有代碼 ...

    logDebug('Sending: ' . json_encode($data, JSON_UNESCAPED_UNICODE));

    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    logDebug("LINE API Response (HTTP $httpCode): $response");

    curl_close($ch);
}

常見錯誤與解決
日誌訊息	原因	解決方法
Invalid signature	LINE_CHANNEL_SECRET 錯誤	檢查 config.php 憑證
HTTP 400	訊息格式錯誤	檢查 Flex Message JSON
HTTP 401	ACCESS_TOKEN 錯誤	重新取得 token
沒有任何日誌	webhook URL 錯誤	檢查 LINE Console 設定
查看調試日誌
# 即時監控
ssh lt4 "tail -f /home/lt4.mynet.com.tw/public_html/linebot/debug.log"

# 查看最近 50 行
ssh lt4 "tail -50 /home/lt4.mynet.com.tw/public_html/linebot/debug.log"

# 清除日誌
ssh lt4 "echo '' > /home/lt4.mynet.com.tw/public_html/linebot/debug.log"

LINE Flex Message 注意事項
Button vs Box 的 Action

Button 組件（推薦）：

穩定可靠
label 有 20 字元限制
適合短文字按鈕
[
    'type' => 'button',
    'style' => 'primary',
    'height' => 'sm',
    'action' => [
        'type' => 'message',
        'label' => '[1] 章節名稱',  // 最多 20 字元
        'text' => '1'
    ]
]


Box 組件的 Action：

可以包含更長的文字（使用 wrap: true）
某些情況下 action 可能不被觸發
需要測試確認
[
    'type' => 'box',
    'layout' => 'horizontal',
    'contents' => [...],
    'action' => [
        'type' => 'message',
        'text' => '1'
    ]
]

長章節名稱處理

如果章節名稱超過 button label 限制：

// 截短名稱
$shortName = mb_strlen($name) > 12 ? mb_substr($name, 0, 12) . '..' : $name;

$buttons[] = [
    'type' => 'button',
    'action' => [
        'type' => 'message',
        'label' => "[{$i}] {$shortName}",
        'text' => (string)$i
    ]
];

部署檢查清單
安全部署步驟
# 1. 備份伺服器設定
ssh lt4 "cp /home/lt4.mynet.com.tw/public_html/linebot/config.php /home/lt4.mynet.com.tw/public_html/linebot/config.php.bak.$(date +%Y%m%d%H%M)"

# 2. 同步 webhook.php（先檢查語法）
scp webhook.php lt4:/home/lt4.mynet.com.tw/public_html/linebot/
ssh lt4 "php -l /home/lt4.mynet.com.tw/public_html/linebot/webhook.php"

# 3. 同步題庫檔案
scp quiz/chemistry/*.json lt4:/home/lt4.mynet.com.tw/public_html/linebot/quiz/chemistry/

# 4. 手動更新 config.php 章節設定（如需要）
ssh lt4 "vim /home/lt4.mynet.com.tw/public_html/linebot/config.php"

# 5. 測試 LINE Bot
# 在 LINE 輸入「開始」確認正常運作

緊急恢復

如果 LINE Bot 壞掉：

# 恢復 config.php 備份
ssh lt4 "cp /home/lt4.mynet.com.tw/public_html/linebot/config.php.bak /home/lt4.mynet.com.tw/public_html/linebot/config.php"

# 恢復 webhook.php 備份
ssh lt4 "cp /home/lt4.mynet.com.tw/public_html/linebot/webhook.php.bak /home/lt4.mynet.com.tw/public_html/linebot/webhook.php"

# 檢查日誌找出問題
ssh lt4 "tail -50 /home/lt4.mynet.com.tw/public_html/linebot/debug.log"

伺服器修改最佳實踐（重要！）
每次修改後必做檢查
# 1. 檢查 PHP 語法
ssh lt4 "php -l /home/lt4.mynet.com.tw/public_html/linebot/config.php"
ssh lt4 "php -l /home/lt4.mynet.com.tw/public_html/linebot/webhook.php"

# 2. 檢查 HTTP 狀態（應該是 400，不是 500）
curl -s -o /dev/null -w '%{http_code}' https://lt4.mynet.com.tw/linebot/webhook.php
# 400 = 正常（缺少 LINE 簽名）
# 500 = PHP 錯誤！

# 3. 清除 session 讓用戶重新開始
ssh lt4 "echo '{}' > /home/lt4.mynet.com.tw/public_html/linebot/data/sessions.json"

不要用 sed 修改 PHP 陣列！

危險操作（容易產生語法錯誤）：

# 這樣刪除會留下多餘的括號！
ssh lt4 "sed -i \"/'physiology' => \[/,/\]/d\" config.php"


問題：sed 刪除多行 PHP 陣列時，容易留下多餘的 ] 或 , 導致語法錯誤。

安全做法：

用 vim 直接編輯：

ssh lt4 "vim /home/lt4.mynet.com.tw/public_html/linebot/config.php"


用 PHP 腳本修改：

ssh lt4 "php -r \"
\\\$config = file_get_contents('config.php');
// 做修改...
file_put_contents('config.php', \\\$config);
\""


完整重寫該段落（推薦）：

# 先備份
ssh lt4 "cp config.php config.php.bak"
# 用 heredoc 重寫整個 $SUBJECTS 陣列

LINE Bot 完全沒反應的排查流程
1. 檢查 HTTP 狀態
   curl -s -o /dev/null -w '%{http_code}' https://lt4.mynet.com.tw/linebot/webhook.php

   ├─ 500 → PHP 錯誤
   │        → php -l config.php
   │        → php -l webhook.php
   │
   ├─ 400 → 正常，檢查日誌
   │        → tail debug.log
   │        ├─ "Invalid signature" → 憑證錯誤
   │        └─ 空的 → LINE webhook URL 設定錯誤
   │
   └─ 其他 → 伺服器/網路問題

修改 config.php 科目設定的安全流程
# 1. 備份
ssh lt4 "cp /home/lt4.mynet.com.tw/public_html/linebot/config.php /home/lt4.mynet.com.tw/public_html/linebot/config.php.bak.$(date +%Y%m%d%H%M)"

# 2. 用 sed 做簡單的文字替換（安全）
ssh lt4 "sed -i \"s/'舊名稱'/'新名稱'/\" /path/to/config.php"

# 3. 驗證語法
ssh lt4 "php -l /path/to/config.php"

# 4. 測試 HTTP 狀態
curl -s -o /dev/null -w '%{http_code}' https://lt4.mynet.com.tw/linebot/webhook.php

# 5. 清除 session
ssh lt4 "echo '{}' > /path/to/sessions.json"

# 6. 在 LINE 輸入「開始」測試

LINE Flex Message 按鈕折行解法（2026-01-08 新增）
問題：Button label 字元限制

LINE Flex Message 的 type: button 元件，label 有約 20 字元限制，超過會被截斷，無法顯示完整選項。

解法：改用 Box + Text (wrap: true)
// 原本的 button（會截斷）
$optionButtons[] = [
    'type' => 'button',
    'style' => 'primary',
    'action' => [
        'type' => 'message',
        'label' => "({$key}) {$value}",  // 超過 20 字元會截斷！
        'text' => $key
    ]
];

// 改用 box + text（支援折行）
$optionButtons[] = [
    'type' => 'box',
    'layout' => 'vertical',
    'contents' => [
        [
            'type' => 'text',
            'text' => "({$key}) {$value}",
            'wrap' => true,           // 關鍵：啟用折行
            'color' => '#ffffff',
            'size' => 'sm',
            'align' => 'center'
        ]
    ],
    'backgroundColor' => '#5B8DEF',
    'cornerRadius' => 'md',
    'paddingAll' => '12px',
    'margin' => 'sm',
    'action' => [
        'type' => 'message',
        'label' => $key,
        'text' => $key
    ]
];

圖片 URL 串接邏輯（避免雙重路徑）
問題

JSON 中已存完整 URL，但 PHP 又加上 IMAGE_BASE_URL，導致：

https://lt4.mynet.com.tw/linebot/images/https://lt4.mynet.com.tw/linebot/images/ch2-7-q12.png

解法：先檢查是否已有 http 開頭
// question_image
$imageUrl = (strpos($q['question_image'], 'http') === 0)
    ? $q['question_image']
    : IMAGE_BASE_URL . '/' . $q['question_image'];

// explanation_image
$explanationUrl = (strpos($explanationImage, 'http') === 0)
    ? $explanationImage
    : IMAGE_BASE_URL . '/' . $explanationImage;

matplotlib 圖片生成標準（手機 LINE Bot 可讀）
字體大小標準
元素	字體大小	說明
標籤 (X, A-E)	44-50pt	粗體 + 黃底紅字，必須醒目
圖片標題	28pt	粗體
軸標題	24pt	粗體
一般文字	18-20pt	—
標準設定
import matplotlib.pyplot as plt

# 中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 儲存設定
fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='white')

LINE Bot 最佳圖片尺寸（2026-01-13 更新）

使用 figsize=(10.4, 7.8) + dpi=100 可以得到精確的 1040×780 像素輸出，這是 LINE Bot 最佳顯示尺寸：

# LINE Bot 優化尺寸
FIG_W, FIG_H = 10.4, 7.8  # 英寸
DPI = 100

# 字體大小（配合此尺寸）
FONT_TITLE = 42   # 標題（最大）
FONT_LARGE = 32   # 大標籤
FONT_MEDIUM = 26  # 中等文字
FONT_SMALL = 22   # 小字（最小建議）

def create_image():
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    ax.set_xlim(0, 10.4)  # X 範圍對應寬度
    ax.set_ylim(0, 7.8)   # Y 範圍對應高度
    ax.axis('off')

    # 繪製內容...

    fig.savefig(filepath, dpi=DPI, bbox_inches='tight',
                facecolor='white', edgecolor='none', pad_inches=0.1)


為何選擇這個尺寸？

1040×780 = 4:3 比例，LINE Bot 顯示時圖片夠大
100 DPI 讓座標計算直覺（1 單位 = 100 像素）
檔案大小適中（通常 30-80 KB）
重點：圖片標記必須與題目一致

題目問「區域 B 代表什麼？」→ 圖片中必須有 B 標記

# 標籤範例：大字體 + 醒目背景
ax.text(x, y, 'B', fontsize=44, fontweight='bold',
        ha='center', va='center', color='red',
        bbox=dict(boxstyle='circle,pad=0.3',
                  facecolor='yellow', edgecolor='red', linewidth=2))

Git 推送衝突處理

當 git push 被拒絕（remote 有新變更）：

# 一行搞定：暫存 → 拉取 → 恢復 → 推送
git stash && git pull --rebase && git stash pop && git push

題目圖片洩題檢測與修復（2026-01-11 新增）
問題描述

題目圖片（Q版本）不應該顯示答案，應該用「？」隱藏答案，讓學生思考。如果 Q 和 A 圖片相同，等於直接洩漏答案。

洩題檢測方法

關鍵洞見：如果 Q 和 A 圖片的檔案大小完全相同，代表它們是同一張圖片（洩題）。

# 檢測所有 Q/A 檔案大小相同的圖片
ssh lt4 'cd /home/lt4.mynet.com.tw/public_html/linebot/images && \
for qfile in ch*-q*.png; do
  afile=$(echo "$qfile" | sed "s/-q/-a/")
  if [ -f "$afile" ]; then
    qsize=$(stat -c%s "$qfile")
    asize=$(stat -c%s "$afile")
    if [ "$qsize" = "$asize" ]; then
      echo "SAME SIZE: $qfile ($qsize bytes) = $afile"
    fi
  fi
done'

Q/A 圖片設計原則
版本	目的	設計方式
Q 版本	題目圖（隱藏答案）	答案處顯示「？」
A 版本	解答圖（顯示答案）	完整顯示所有資訊
修復範例

負回饋調控圖（ch1-q9 vs ch1-a9）：

# Q版本 - 隱藏答案
def create_q9_negative_feedback_Q():
    ax.add_patch(FancyBboxPatch(...))
    ax.text(x, y, '？', fontsize=FONT_TITLE, color='#C62828')  # 用問號隱藏
    ax.text(7, 1.5, '哪種生理調節是負回饋的例子？', style='italic')

# A版本 - 顯示答案
def create_a9_negative_feedback_A():
    ax.add_patch(FancyBboxPatch(...))
    ax.text(x, y, '血壓調節', fontweight='bold')  # 顯示答案
    ax.text(7, 0.5, '答案：血壓調節是負回饋的典型例子',
            bbox=dict(boxstyle='round', facecolor='#E8F5E9', edgecolor='#4CAF50'))

圖片命名規則
ch{章}-q{題號}-{描述}.png   # 題目版（隱藏答案）
ch{章}-a{題號}-{描述}.png   # 解答版（顯示答案）


範例：

ch1-q9-negative-feedback.png - 題目版
ch1-a9-negative-feedback.png - 解答版
完整修復流程
檢測洩題：比較 Q/A 檔案大小
分析題目：讀取 JSON 了解題目內容
設計 Q 版本：用「？」隱藏答案
設計 A 版本：完整顯示答案並加強調
生成圖片：使用 matplotlib 生成
驗證大小：確認 Q 和 A 檔案大小不同
上傳伺服器：scp 到圖片目錄
批次修復腳本結構
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle
import os

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

OUTPUT_DIR = r"C:\Users\user\Documents\temp\images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

FONT_TITLE = 42
FONT_LABEL = 32
FONT_TEXT = 28
FONT_SMALL = 24

def save_single(fig, filename):
    """儲存單一圖片"""
    filepath = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f"已儲存: {filename}")
    plt.close(fig)

def create_qXX_topic_Q():
    """題目版 - 隱藏答案"""
    fig, ax = plt.subplots(figsize=(14, 10))
    # ... 用「？」隱藏答案 ...
    save_single(fig, 'ch1-q9-topic.png')

def create_aXX_topic_A():
    """解答版 - 顯示答案"""
    fig, ax = plt.subplots(figsize=(14, 10))
    # ... 顯示完整答案 ...
    save_single(fig, 'ch1-a9-topic.png')

if __name__ == '__main__':
    create_qXX_topic_Q()
    create_aXX_topic_A()

常見洩題類型與修復策略
題目類型	Q 版本應隱藏	A 版本應顯示
回饋系統	隱藏「受器/控制中樞/動器」	顯示完整名稱和功能
體腔分類	隱藏腔室名稱	顯示腔室名稱和包含器官
肌肉收縮	隱藏哪個結構會縮短	標示 I帶/H帶 縮短
動作電位	隱藏離子種類	標示 Na⁺ 流入 / K⁺ 流出
突觸構造	隱藏囊泡名稱	標示「突觸囊泡」
荷爾蒙機轉	隱藏作用機制	標示「第二傳訊者」
驗證修復成功
# 確認所有修復的圖片 Q/A 大小不同
ssh lt4 'cd /home/lt4.mynet.com.tw/public_html/linebot/images && \
ls -la ch1-q9*.png ch1-a9*.png'

# 應該看到不同的檔案大小，例如：
# -rw-r--r-- 1 root root  92287 ch1-q9-negative-feedback.png
# -rw-r--r-- 1 root root 122518 ch1-a9-negative-feedback.png

視覺審查頁面

建立 HTML 審查頁面，人工檢視所有 Q/A 圖片：

<div class="card">
    <div class="images">
        <div class="image-box">
            <p>📝 題目圖（應隱藏答案）</p>
            <img src="https://lt4.mynet.com.tw/linebot/images/ch1-q9-negative-feedback.png">
        </div>
        <div class="image-box">
            <p>✅ 解答圖（顯示完整答案）</p>
            <img src="https://lt4.mynet.com.tw/linebot/images/ch1-a9-negative-feedback.png">
        </div>
    </div>
    <div class="checklist">
        <label><input type="checkbox"> 題目圖不洩題</label>
        <label><input type="checkbox"> 文字清晰無重疊</label>
        <label><input type="checkbox"> 圖片正常載入</label>
    </div>
</div>


審查頁面 URL: https://lt4.mynet.com.tw/linebot/review.html

給 Claude 的執行指引
下次執行類似任務時，請遵循：

開工前先檢查版本同步狀態（最重要！）

用戶可能在家裡、公司、或直接在伺服器上修改程式碼。開始任何修改前，必須先確認版本一致：

# 檢查本地 Git 狀態
cd /c/Users/user/linebot-quiz
git status
git fetch origin
git log HEAD..origin/master --oneline  # 遠端有但本地沒有

# 比對本地和伺服器的 webhook.php
ssh lt4 "cat /home/lt4.mynet.com.tw/public_html/linebot/webhook.php" | head -20
# 與本地 webhook.php 比較關鍵部分


如果發現差異：

提醒用戶：「發現本地/GitHub/伺服器版本不一致，請確認哪個是最新版本」
不要貿然覆蓋任何版本
讓用戶決定同步方向

修改伺服器檔案前先備份

ssh lt4 "cp file file.bak.$(date +%Y%m%d%H%M)"


每次修改後立即驗證 PHP 語法

ssh lt4 "php -l /path/to/file.php"


避免用 sed 刪除 PHP 陣列條目

用簡單的文字替換（如改名稱）是安全的
刪除整個陣列條目容易出錯，改用 vim 或完整重寫

LINE Bot 沒反應時的排查順序

先檢查 HTTP 狀態碼（curl）
如果 500 → 檢查 PHP 語法
如果 400 → 檢查 debug.log
如果日誌空 → 檢查 LINE webhook URL

不要直接 scp config.php

會覆蓋伺服器上的 LINE 憑證
改用 ssh + sed 或 vim 直接在伺服器修改

測試前清除 session

ssh lt4 "echo '{}' > /path/to/sessions.json"

LINE Flex Message 圖片最佳實踐（2026-01-12 新增）
核心原則：一開始就做對

避免「生成圖片 → 測試發現問題 → 修復」的循環，遵循以下規範一開始就產出正確的圖片。

圖片尺寸與 DPI 標準
設定	建議值	說明
figsize	(14, 10)	英寸，約 2100×1500 像素 @150 DPI
DPI	150	平衡清晰度與檔案大小（單張約 60-200KB）
aspectRatio	4:3	LINE Flex Message 中圖片較高，文字更易讀
fig, ax = plt.subplots(figsize=(14, 10))
fig.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white')

字體大小標準（LINE Bot 手機可讀）

重要：LINE Bot 圖片無法放大，必須確保手機上可直接閱讀。

用途	字體大小	範例
主標題	48pt	圖片頂部標題
重要標記	48pt + 粗體 + 紅色	X/Y/Z 標記、關鍵元素
區塊標籤	36pt	方框內的標題
說明文字	32pt	一般解說
最小文字	28pt	次要資訊（絕對最小值！）
# 標準字體常數
FONT_TITLE = 48   # 標題
FONT_LABEL = 36   # 標籤
FONT_TEXT = 32    # 內文
FONT_SMALL = 28   # 小字（最小值）

防止答案洩漏的設計模式
模式一：X/Y/Z 標記法

適用於「比較類」題目，如：「下列何者為骨骼肌的特徵？」

# Q 版本（題目）：使用 X/Y/Z 隱藏名稱
muscles = [
    (1.5, 'X', '#FFCDD2'),   # 實際是骨骼肌
    (5.5, 'Y', '#C8E6C9'),   # 實際是心肌
    (9.5, 'Z', '#BBDEFB'),   # 實際是平滑肌
]
ax.text(x, y, name, fontsize=FONT_TITLE, fontweight='bold', color='#C62828')

# A 版本（解答）：顯示實際名稱
muscles = [
    (1.5, '骨骼肌', '#FFCDD2', ['隨意控制', '有橫紋', '多核']),
    (5.5, '心肌', '#C8E6C9', ['不隨意', '有橫紋', '單核']),
    (9.5, '平滑肌', '#BBDEFB', ['不隨意', '無橫紋', '單核']),
]

模式二：中性標題法

適用於標題會洩漏答案的情況。

# Q 版本：使用中性標題
ax.set_title('回饋機制示意圖', fontsize=FONT_TITLE)     # 不說「負回饋」
ax.set_title('某內分泌腺構造圖', fontsize=FONT_TITLE)   # 不說「腦下垂體」

# A 版本：顯示完整標題
ax.set_title('負回饋調控示意圖', fontsize=FONT_TITLE)
ax.set_title('腦下垂體 (Pituitary Gland)', fontsize=FONT_TITLE)

模式三：問號遮蔽法

適用於單一關鍵資訊需要隱藏的情況。

# Q 版本：用「？」遮蔽答案
ax.text(x, y, '?\n調控機制', ha='center', fontsize=FONT_TEXT)

# A 版本：顯示完整答案
ax.text(x, y, '負回饋\n調控機制', ha='center', fontsize=FONT_TEXT,
        bbox=dict(facecolor='#E8F5E9', edgecolor='#4CAF50'))  # 綠框強調

常見洩題類型對照表
題目類型	洩題風險	Q 版本設計	A 版本設計
三種肌肉比較	直接顯示「骨骼肌」	用 X/Y/Z 標記	顯示「骨骼肌/心肌/平滑肌」
回饋系統類型	標題寫「負回饋」	標題改「回饋機制」	標題寫「負回饋調控」
內分泌腺識別	標題寫「腦下垂體」	標題改「某內分泌腺」	顯示「腦下垂體」
細胞構造識別	標籤寫「粒線體」	標籤改「?」或「構造 A」	顯示「粒線體」
離子識別	顯示「Na⁺」	顯示「X⁺」	顯示「Na⁺」
Q/A 版本生成函數模板
def create_CHAPTER_QNUM_TOPIC_QUESTION():
    """題目版 - 隱藏答案"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # 使用中性標題
    ax.set_title('示意圖', fontsize=FONT_TITLE, fontweight='bold', pad=20)

    # 用 X/Y/Z 或 ? 隱藏答案
    ax.text(7, 5, 'X', fontsize=FONT_TITLE, fontweight='bold', color='#C62828')

    save_single(fig, 'chN-qM-topic.png')

def create_CHAPTER_QNUM_TOPIC_ANSWER():
    """解答版 - 顯示完整答案"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # 顯示完整標題
    ax.set_title('XXX 示意圖', fontsize=FONT_TITLE, fontweight='bold', pad=20)

    # 顯示答案並強調
    ax.text(7, 5, '答案', fontsize=FONT_LABEL, fontweight='bold',
            bbox=dict(facecolor='#E8F5E9', edgecolor='#4CAF50', linewidth=2))

    save_single(fig, 'chN-aM-topic.png')

自動化圖片檢查流程
Playwright + LINE Flex Simulator 檢查

使用 Playwright 自動化在 LINE Flex Message Simulator 中預覽所有題目圖片：

# line_quiz_checker.py 核心流程
from playwright.sync_api import sync_playwright

def run_checker():
    # 1. 從伺服器取得所有有圖片的題目
    questions = get_questions_with_images()

    # 2. 啟動瀏覽器
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 3. 開啟 LINE Flex Simulator
        page.goto('https://developers.line.biz/flex-simulator/')

        # 4. 等待登入（第一次需手動登入，之後用儲存的 session）
        if 'login' in page.url:
            wait_for_login(page)
            context.storage_state(path='line_auth_state.json')

        # 5. 逐一測試每個題目
        for q in questions:
            flex_json = generate_flex_json(q)
            # 輸入 JSON 並截圖
            page.click('button:has-text("View as JSON")')
            page.locator('textarea').fill(flex_json)
            page.click('button:has-text("Apply")')
            page.screenshot(path=f'{q["chapter"]}-q{q["id"]}.png')

VLM 圖片審查

用 Claude 的視覺能力檢查截圖是否有洩題問題：

# 讀取截圖並分析
from anthropic import Anthropic

def check_image_for_leakage(image_path, question_text):
    client = Anthropic()

    with open(image_path, 'rb') as f:
        image_data = base64.b64encode(f.read()).decode()

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=500,
        messages=[{
            "role": "user",
            "content": [
                {"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": image_data}},
                {"type": "text", "text": f"""
檢查這張 LINE Bot 題目圖片是否有洩題問題。

題目：{question_text}

請檢查：
1. 標題是否直接顯示答案？
2. 圖片中的標籤是否洩漏答案？
3. 文字是否清晰可讀？

回答格式：
- 洩題風險：是/否
- 問題描述：（如有）
- 建議修正：（如有）
"""}
            ]
        }]
    )
    return response.content[0].text

伺服器路徑注意事項
正確的檔案路徑

重要：lt4.mynet.com.tw 的 DocumentRoot 是 /home/lt4.mynet.com.tw/public_html/，不是 /var/www/html/！

用途	正確路徑
LINE Bot 根目錄	/home/lt4.mynet.com.tw/public_html/linebot/
圖片目錄	/home/lt4.mynet.com.tw/public_html/linebot/images/
題庫目錄	/home/lt4.mynet.com.tw/public_html/linebot/quiz/
# 正確的上傳指令
scp images/*.png lt4:/home/lt4.mynet.com.tw/public_html/linebot/images/

# 錯誤！這個路徑不會被網頁伺服器服務
scp images/*.png lt4:/var/www/html/linebot/images/

CDN/快取問題處理

如果更新圖片後仍顯示舊版本，可能是 Apache mod_cache 快取問題：

# 1. 清除 Apache 快取
ssh lt4 "rm -rf /var/cache/apache2/mod_cache_disk/* && systemctl restart apache2"

# 2. 如果仍有問題，重新命名檔案
ssh lt4 "mv old.png new.png"

# 3. 更新 JSON 中的圖片 URL
ssh lt4 "sed -i 's/old.png/new.png/g' /path/to/*.json"

# 4. 或使用 cache-busting 參數
# 在 URL 後加上 ?v=2
"question_image": "https://lt4.mynet.com.tw/linebot/images/ch1-q9.png?v=2"

LINE Flex Message 圖片尺寸規範（2026-01-12 新增）
LINE 官方規範
項目	規範值	說明
基準寬度	1040px	LINE Imagemap 和 Flex Message 的參考寬度
aspectRatio	4:3	webhook.php 中設定的圖片比例
最佳尺寸	1040 x 780 px	4:3 比例，符合 LINE 基準
檔案大小	< 1MB	LINE 建議值，實際建議 < 300KB 以加速載入
為什麼不用 Gemini API 製圖

經過多次測試，不建議使用 Gemini API 生成教育圖片，原因：

中文字模糊：AI 生成的中文字經常模糊、變形或出現錯字
無法控制尺寸：無法精確指定輸出尺寸（如 1040x780）
字體不可控：無法指定使用正體中文字體
結果不穩定：每次生成結果不同，難以維持一致品質

建議方案：使用 matplotlib + 微軟正黑體 製圖，完全可控。

matplotlib 製圖特殊字符問題（2026-01-12 新增）
問題：方框字 (□) 出現

使用微軟正黑體時，某些 Unicode 特殊字符會顯示為方框：

問題字符	Unicode	顯示結果	解決方案
− (minus sign)	U+2212	□	改用 - (普通連字符)
₂ (subscript 2)	U+2082	□	改用 2 (普通數字)
₃ (subscript 3)	U+2083	□	改用 3 (普通數字)
α (alpha)	U+03B1	✓ 正常	可以使用
錯誤示範 vs 正確做法
# 錯誤：使用特殊 Unicode 字符
ax.text(x, y, '−NH₂', fontsize=26)     # 顯示為 □NH□
ax.text(x, y, '−COOH', fontsize=26)    # 顯示為 □COOH

# 正確：使用普通 ASCII 字符
ax.text(x, y, '-NH2', fontsize=26)     # 正常顯示
ax.text(x, y, '-COOH', fontsize=26)    # 正常顯示

檢查腳本是否有問題字符
# 檢查 Python 腳本中是否有問題字符
grep -n '[−₀₁₂₃₄₅₆₇₈₉]' your_script.py

執行時的警告訊息

如果看到以下警告，表示有特殊字符問題：

UserWarning: Glyph 8722 (\N{MINUS SIGN}) missing from font(s) Microsoft JhengHei.
UserWarning: Glyph 8322 (\N{SUBSCRIPT TWO}) missing from font(s) Microsoft JhengHei.

matplotlib 製圖完整範本（1040x780 優化版）
標準設定
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
import os

# 中文字體設定（必須）
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False  # 避免負號問題

# 輸出目錄
OUTPUT_DIR = r"C:\Users\user\quiz_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 圖片尺寸 (1040x780 at 100 DPI = 10.4x7.8 inches)
FIG_W, FIG_H = 10.4, 7.8
DPI = 100

# 字體大小（LINE Bot 手機可讀）
FONT_TITLE = 42    # 主標題
FONT_LARGE = 32    # 重要標籤
FONT_MEDIUM = 26   # 一般文字
FONT_SMALL = 22    # 次要資訊（最小值！）

# Material Design 配色
COLORS = {
    'blue': '#1565C0',
    'light_blue': '#BBDEFB',
    'green': '#2E7D32',
    'light_green': '#C8E6C9',
    'red': '#C62828',
    'light_red': '#FFCDD2',
    'orange': '#E65100',
    'light_orange': '#FFE0B2',
    'purple': '#7B1FA2',
    'light_purple': '#E1BEE7',
    'gray': '#607D8B',
    'light_gray': '#ECEFF1',
}

儲存函數
def save_fig(fig, filename):
    """儲存圖片 - 1040x780, 優化檔案大小"""
    filepath = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(filepath, dpi=DPI, bbox_inches='tight',
                facecolor='white', edgecolor='none', pad_inches=0.1)
    plt.close(fig)
    size_kb = os.path.getsize(filepath) / 1024
    print(f"  [OK] {filename} ({size_kb:.0f} KB)")

完整範例：胺基酸結構圖
def create_amino_acid_structure():
    """胺基酸結構圖 - 1040x780"""
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    ax.set_xlim(0, 10.4)
    ax.set_ylim(0, 7.8)
    ax.axis('off')
    ax.set_facecolor('white')

    # 標題
    ax.text(5.2, 7.2, '胺基酸基本結構', fontsize=FONT_TITLE, fontweight='bold',
            ha='center', va='center', color=COLORS['blue'])

    # 中心 - α碳
    center_x, center_y = 5.2, 4.0
    circle = Circle((center_x, center_y), 0.6, facecolor=COLORS['light_blue'],
                    edgecolor=COLORS['blue'], linewidth=3)
    ax.add_patch(circle)
    ax.text(center_x, center_y, 'C', fontsize=FONT_LARGE, fontweight='bold',
            ha='center', va='center', color=COLORS['blue'])

    # 左邊 - 胺基（注意：使用普通連字符和數字！）
    ax.add_patch(FancyBboxPatch((1.5, 3.2), 2.0, 1.6, boxstyle="round,pad=0.1",
                                facecolor=COLORS['light_green'], edgecolor=COLORS['green'], linewidth=2))
    ax.text(2.5, 4.0, '胺基', fontsize=FONT_LARGE, fontweight='bold', ha='center', va='center')
    ax.text(2.5, 3.5, '-NH2', fontsize=FONT_MEDIUM, ha='center', va='center', color=COLORS['green'])
    # 注意：用 '-NH2' 而不是 '−NH₂'

    # 右邊 - 羧基
    ax.add_patch(FancyBboxPatch((6.9, 3.2), 2.0, 1.6, boxstyle="round,pad=0.1",
                                facecolor=COLORS['light_red'], edgecolor=COLORS['red'], linewidth=2))
    ax.text(7.9, 4.0, '羧基', fontsize=FONT_LARGE, fontweight='bold', ha='center', va='center')
    ax.text(7.9, 3.5, '-COOH', fontsize=FONT_MEDIUM, ha='center', va='center', color=COLORS['red'])
    # 注意：用 '-COOH' 而不是 '−COOH'

    save_fig(fig, 'ch7-q1-protein.png')

預期輸出
項目	數值
圖片尺寸	1040 x 780 px
檔案大小	50-110 KB
載入時間	< 0.5 秒
Gemini API 題目生成（文字部分仍可用）

雖然 Gemini API 不適合生成圖片，但生成題目文字仍然有效：

分批生成避免截斷

Gemini 生成大量題目時可能被截斷，建議分批處理：

# 分 5 批，每批 10 題
for batch in range(1, 6):
    start_id = (batch - 1) * 10 + 1
    questions = await generate_batch(batch, start_id, 10, session)
    all_questions.extend(questions)
    await asyncio.sleep(1)  # 避免 rate limit

JSON 解析修復

Gemini 回傳的 JSON 可能有格式問題：

# 修復常見 JSON 錯誤（多餘逗號）
json_str = re.sub(r',(\s*[}\]])', r'\1', json_str)

try:
    data = json.loads(json_str)
except json.JSONDecodeError as e:
    # 儲存原始回應供除錯
    with open(f'debug_batch{batch}.txt', 'w', encoding='utf-8') as f:
        f.write(response)

圖片生成品質檢查清單

生成圖片後，逐一確認以下項目：

可讀性檢查
 標題文字 ≥ 48pt
 標籤文字 ≥ 36pt
 最小文字 ≥ 28pt
 在手機上模擬預覽（實際大小約 350×263 像素）
洩題檢查
 Q 版本標題不含答案關鍵字
 Q 版本使用 X/Y/Z 或 ? 隱藏答案
 Q 版本和 A 版本檔案大小不同（相同 = 洩題）
技術檢查
 檔案大小在 50-250KB 範圍
 圖片比例接近 4:3
 上傳到正確路徑（/home/lt4.mynet.com.tw/...）
 URL 可正常存取（curl -I 測試）
快速驗證指令
# 檢查 Q/A 檔案大小是否不同（相同 = 洩題）
ssh lt4 'cd /home/lt4.mynet.com.tw/public_html/linebot/images && \
for q in ch*-q*.png; do
  a=$(echo "$q" | sed "s/-q/-a/")
  if [ -f "$a" ]; then
    qs=$(stat -c%s "$q")
    as=$(stat -c%s "$a")
    if [ "$qs" = "$as" ]; then
      echo "⚠️ 洩題風險: $q ($qs) = $a"
    fi
  fi
done'

# 檢查圖片是否正常載入
curl -s -o /dev/null -w "%{http_code}" https://lt4.mynet.com.tw/linebot/images/ch1-q9-negative-feedback.png
# 應該返回 200

Weekly Installs
8
Repository
bingo-taiwan/cl…e-skills
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn