---
rating: ⭐⭐
title: ai-ppt-generate
url: https://skills.sh/site/skills.volces.com/ai-ppt-generate
---

# ai-ppt-generate

skills/skills.volces.com/ai-ppt-generate
ai-ppt-generate
$ npx skills add https://skills.volces.com/c/arkclaw-personal/skills/clawhub/jlpjavawayup
SKILL.md
AI PPT Generation

This skill allows OpenClaw agents to generate ppt file, Based solely on the theme provided by the user, if possible, pictures or resource files can be provided, this tool can help generate perfect PPT files.

Setup
API Key: Ensure the BAIDU_API_KEY environment variable is set with your valid API key.
Environment: The API key should be available in the runtime environment.
API table
name	path	description
PPTThemeQuery	/v2/tools/ai_ppt/get_ppt_theme	Query the built-in list of PPT themes and templates
PPTOutlineGenerate	/v2/tools/ai_ppt/generate_outline	Generate a PPT outline based on the provided theme, template ID, style ID, etc
PPTGenerate	/v2/tools/ai_ppt/generate_ppt_by_outline	Generate a PPT file url based on the provided ppt outline
Workflow
The PPTThemeQuery API executes the Python script located at scripts/ppt_theme_list.py
The PPTOutlineGenerate API executes the Python script located at scripts/ppt_outline_generate.py
The PPTGenerate API executes the Python script located at scripts/ppt_generate.py
The first step is for the user to query the PPT style query interface（PPTThemeQuery） to obtain the style ID and template ID
The second step is to use the style ID and template ID queried in the first step as parameters for generating the PPT outline and call the PPT outline generation API（PPTOutlineGenerate） to generate the outline (this API is a sse streaming return. This step depends on the first step. If the first step fails, the request can be terminated).
The third step is to request the PPT intelligent generation API（PPTGenerate） based on the outline generated in the second step. Eventually, a PPT file is generated (the request parameter outline is returned by the outline generation interface, aggregating the sse streaming return result as the input parameter. Meanwhile, users can edit and modify the outline, but the modified outline must be in markdown format). Otherwise, a failure may occur. This step strictly depends on the second step. If the second step fails, the request can be terminated.
APIS
PPTThemeQuery API
Parameters

no parameters

Example Usage
BAIDU_API_KEY=xxx python3 scripts/ppt_theme_list.py

PPTOutlineGenerate API
Parameters
query: ppt title or user query（required）
resource_url: the url of the resource file, such as pdf, word, txt, etc.
page_range: the page range of the ppt file, just include enumerations, 1-10、11-20、21-30、31-40、40+
layout: the layout of the ppt file, optional values: 1,2 (1: Minimalist mode, 2: Professional Mode)
language_option: the language option of the ppt file, optional values: zh, en (zh: Chinese, en: English)
gen_mode: the generation mode of the ppt, optional values: 1,2 (1: Intelligent touch-ups, 2: Creative Mode)
Example Usage
BAIDU_API_KEY=xxx python3 scripts/ppt_outline_generate.py --query "generate a ppt about the future of AI" 

PPTGenerate API
Parameters
query_id: query id from PPTOutlineGenerate API return（required）
chat_id: chat id from PPTOutlineGenerate API return（required）
outline: ppt outline from PPTOutlineGenerate API return，must be in markdown format.Users can make appropriate modifications to the content, adding, modifying or deleting parts of the outline.（required）
query: user orgin query（required）
title: ppt title from PPTOutlineGenerate API return（required）
style_id: ppt stype id from PPTThemeQuery API return（required）
tpl_id: ppt template id from PPTThemeQuery API return（required）
resource_url: the url of the resource file, such as pdf, word, txt, etc.
custom_tpl_url: The path of the user-defined PPT template must be downloadable
gen_mode: the generation mode of the ppt, optional values: 1,2 (1: Intelligent touch-ups, 2: Creative Mode)
ai_info: Information on whether to use AI-generated PPT on the last page of the generated PPT
Example Usage
BAIDU_API_KEY=xxx python3 scripts/ppt_generate.py --query_id "xxx" --chat_id "xxx" ...

Weekly Installs
392
Source
skills.volces.c…avawayup
First Seen
Mar 12, 2026
Security Audits
SocketPass