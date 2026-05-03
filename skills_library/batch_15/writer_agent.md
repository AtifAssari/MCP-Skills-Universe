---
title: writer-agent
url: https://skills.sh/hoangvantuan/claude-plugin/writer-agent
---

# writer-agent

skills/hoangvantuan/claude-plugin/writer-agent
writer-agent
Installation
$ npx skills add https://github.com/hoangvantuan/claude-plugin --skill writer-agent
SKILL.md
Writer Agent

Transform documents and URLs into styled article series.

Quick Reference
Reference	Purpose	Load at Step	DP	T1	T2	T3
directory-structure.md	Output folder layout	Step 1	✓	✓	✓	✓
dimension-selection.md	Custom mode dimension tables	Step 2 (Custom)	✓	✓	✓	✓
decision-trees.md	Workflow decision guides	On confusion only	✓	✓	✓	✓
retry-workflow.md	Error recovery procedures	On error only	-	✓	✓	✓
large-doc-processing.md	Handling documents >50K words	Step 3 (if >20K)	-	-	✓	✓
article-writer-prompt.md	Subagent prompt templates	Step 4	-	✓	✓	✓
context-extractor-prompt.md	Context extraction template	Step 3 (Tier 2)	-	-	✓	-
context-optimization.md	Context optimization anti-patterns	Step 3.1	-	✓	✓	✓
detail-levels.md	Output detail level options	Step 2.5	✓	✓	✓	✓
shared-article-writing.md	Shared Steps 4.0-4.6	Step 4	-	✓	✓	✓

DP = Direct Path | T1-T3 = Tier 1-3 | ✓ = Load | - = Skip

Tier Workflow Files (loaded at Step 2.7 after tier determination):

Tier	File	When
Direct Path	tier-direct-path.md	<20K OR (<50K AND ≤3 articles)
Tier 1	tier-1-workflow.md	20K-50K (fails Direct Path)
Tier 2	tier-2-workflow.md	50K-100K
Tier 3	tier-3-workflow.md	>=100K

Dimension files (loaded at Step 2): voices/{voice}.md, structures/{structure}.md, identities/{identity}.md, audiences/{audience}.md, emotional_maps/{emotion}.md

Workflow Overview

Direct Path (<20K words OR <50K words with <=3 articles):

Main agent writes all articles directly without subagents.

Input → Convert → Style/Structure → Plan → Write(main) → Synthesize → Verify
  1        1           2               3        4            5           6


Standard (Tier 1-2, 20K-100K words):

Input → Convert → Style/Structure → Analyze → Extract → Write → Synthesize → Verify
  1        1           2               3         3         4        5           6


Fast Path (Tier 3, >=100K words):

Input → Convert → Style/Structure → Plan → Write(parallel) → Synthesize → Verify
  1        1           2              3          4              5           6

Step 0: Resolve Skill Paths (BẮT BUỘC)

Tìm wa-env → chạy → dùng paths tuyệt đối cho toàn bộ workflow.

# Tìm wa-env (thử Glob trước, fallback find nếu plugin installed vào dotdir)
Glob("**/writer-agent/scripts/wa-env")  # hoặc Glob(".claude/**/wa-env")

# Chạy (dùng bash, không dùng source — để BASH_SOURCE resolve đúng)
bash {path_to_wa-env}
# → SCRIPTS_DIR, SKILL_DIR, VOICES_DIR, STRUCTURES_DIR, IDENTITIES_DIR,
#   AUDIENCES_DIR, EMOTIONS_DIR, TEMPLATES_DIR, REFERENCES_DIR

# Verify
assert Glob(f"{SCRIPTS_DIR}/wa-convert") and Glob(f"{VOICES_DIR}/*.md")


FAIL CONDITION: Không tìm thấy wa-env → STOP. KHÔNG tự suy đoán paths.

Step 1: Input Handling

GUARD: SCRIPTS_DIR đã resolve từ Step 0. Nếu chưa → STOP, quay lại Step 0.

Detect input type and convert to markdown.

Output language: Luôn là tiếng Việt, bất kể source language.

Input Type	Detection	Action
File (PDF/DOCX/EPUB/etc)	Path + extension	wa-convert {path}
URL (web page)	http:// or https://	wa-convert {url}
YouTube URL	youtube.com or youtu.be	wa-convert {url}
Plain text / .txt / .md	No complex extension	Rewrite → wa-paste-text
File/URL Conversion
{SCRIPTS_DIR}/wa-convert [/path/to/file.pdf or url]


Output: writer-agent/{slug}-{timestamp}/input-handling/content.md

Plain Text Processing
Read content (if file)
Rewrite to structured markdown (add headings, preserve content)
Propose title
Execute:
echo "{rewritten_content}" | {SCRIPTS_DIR}/wa-paste-text - --title "{title}"

Error Handling
Error	Action
File not found	Ask for correct path
Unsupported format	Try Docling, confirm with user
URL fetch failed	Report and stop
Empty content	Warn, confirm before continue
Encrypted PDF	Ask for decrypted version
Step 2: Select Writing Dimensions

Hệ thống 5 chiều độc lập. User chọn preset combo hoặc Custom để mix-match tự do.

Preset Combos (Recommended)

Show bảng sau cho user, hỏi chọn preset hoặc "Custom":

Preset	Voice	Structure	Identity	Audience	Emotion
Educator	Teacher	Building Blocks	Tech Builder	Curious Beginners	Empower & Challenge
Storyteller	Storyteller	Story Arc	Contemplative Thinker	Deep Seekers	Reflect & Discover
Analyst	Objective	BLUF-Evidence	Knowledge Curator	Busy Professionals	Empower & Challenge
Explorer	Investigator	Five Layers	Knowledge Curator	Deep Seekers	Provoke & Transform
Mentor	Guide	Depth-Practice	Contemplative Thinker	Curious Beginners	Reflect & Discover
Reflector	Personal	Spiral Return	Contemplative Thinker	Deep Seekers	Reflect & Discover
Zen Master	Dialogue	Master-Student	Contemplative Thinker	Deep Seekers	Reflect & Discover

Cách dùng: Hiển thị bảng trên → Hỏi user gõ tên preset (e.g. "Educator") hoặc "Custom".

Nếu chọn preset: Tất cả 5 dimensions đã set, skip đến Step 2.5
Nếu chọn Custom: Chuyển sang Step 2a-2f bên dưới (chọn từng chiều)
Adaptive structure: Dùng khi content mixed/không fit structures cố định. Chỉ available qua Custom mode hoặc user yêu cầu trực tiếp.
Custom Mode

Khi user chọn "Custom" → đọc dimension-selection.md để chọn từng chiều (Voice → Structure → Identity → Audience → Emotion) kèm compatibility check.

Step 2.5: Select Detail Level

Hỏi user để confirm output detail level.

Level	Ratio	Description
Concise	15-25%	Tóm lược, giữ ý chính
Standard	30-40%	Cân bằng (Recommended)
Comprehensive	50-65%	Chi tiết, giữ nhiều ví dụ
Faithful	75-90%	Gần như đầy đủ, viết lại theo style

Default: Standard (if user skips or unclear). PASS/FAIL dựa trên section coverage, không phải word count.

Chi tiết calculation (target_ratio, example_percentage) và worked examples → detail-levels.md.

Step 2.6: Tier Reference Table

Canonical tier definitions (referenced throughout documentation):

Tier	Word Count	Strategy	Context Approach	Glossary	max_concurrent
Direct Path	<20K OR (<50K AND ≤3 articles)	Main agent writes all	N/A (no subagents)	Inline (~200 words)	N/A
Tier 1	20K-50K (fails Direct Path)	Subagents read source directly	No context files	Inline (~200 words)	3
Tier 2	50K-100K	Smart compression	Context extractors	Separate file (~600 words)	3
Tier 3	>=100K	Fast Path, minimal overhead	No context files	Inline (~300 words)	2

Priority rules:

Direct Path conditions are checked FIRST and override tier boundaries
Documents 20K-50K with ≤3 articles use Direct Path (not Tier 1)
Only documents failing Direct Path conditions fall through to tier selection

Note: Direct Path <50K condition is further limited by language: EN ~44K, VI ~32K, mixed ~38K words. These limits are pre-computed in structure.json → direct_path.capacity_ok. If capacity exceeded, fallback to Tier 1.

Key differences:

Direct Path: Main agent handles everything (no subagents)
Tier 1: Lightweight subagents, read source via line ranges
Tier 2: Context extraction for compression (only tier with separate glossary file)
Tier 3: Like Tier 1 but larger chunks, more selective glossary, lower concurrency
Step 2.7: Load Tier Workflow (BẮT BUỘC)

Sau khi xác định tier từ Step 2.6, đọc file workflow tương ứng:

tier = determine_tier(structure_json)  # Từ structure.json

if tier == "direct_path":
    Read(f"{SKILL_DIR}/references/tier-direct-path.md")
elif tier == 1:
    Read(f"{SKILL_DIR}/references/tier-1-workflow.md")
elif tier == 2:
    Read(f"{SKILL_DIR}/references/tier-2-workflow.md")
elif tier == 3:
    Read(f"{SKILL_DIR}/references/tier-3-workflow.md")


Tier workflow file chứa Steps 3-4. Sau khi hoàn thành Step 4, load references/steps-5-6-synthesize-verify.md cho Steps 5-6.

FAIL CONDITION: Nếu không load tier workflow file → KHÔNG biết cách xử lý Steps 3-4 cho tier đó. STOP và load file đúng.

Weekly Installs
54
Repository
hoangvantuan/cl…e-plugin
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn