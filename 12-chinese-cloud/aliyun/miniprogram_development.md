---
rating: ⭐⭐
title: miniprogram-development
url: https://skills.sh/tencentcloudbase/skills/miniprogram-development
---

# miniprogram-development

skills/tencentcloudbase/skills/miniprogram-development
miniprogram-development
Installation
$ npx skills add https://github.com/tencentcloudbase/skills --skill miniprogram-development
Summary

Complete WeChat Mini Program development lifecycle from project setup through publishing and optimization.

Covers page and component creation, project structure organization, configuration management, and asset handling within mini program conventions
Supports debugging, previewing, and publishing workflows via WeChat Developer Tools or miniprogram-ci command-line automation
Integrates CloudBase (wx.cloud) for cloud functions, database, storage, and identity when explicitly required by the project
Handles real-device validation, WeChat Developer Tools workflows, and release process optimization
SKILL.md
Standalone Install Note

If this environment only installed the current skill, start from the CloudBase main entry and use the published cloudbase/references/... paths for sibling skills.

CloudBase main entry: https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/SKILL.md
Current skill raw source: https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/miniprogram-development/SKILL.md

Keep local references/... paths for files that ship with the current skill directory. When this file points to a sibling skill such as auth-tool or web-development, use the standalone fallback URL shown next to that reference.

Activation Contract
Use this first when
The request is about WeChat Mini Program structure, pages, preview, publishing, or CloudBase mini program integration.
Read before writing code if
The user mentions wx.cloud, CloudBase mini programs, OPENID, or mini program deployment/debug workflows.
Then also read
CloudBase auth -> ../auth-wechat/SKILL.md (standalone fallback: https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/auth-wechat/SKILL.md)
CloudBase document DB -> ../no-sql-wx-mp-sdk/SKILL.md (standalone fallback: https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/no-sql-wx-mp-sdk/SKILL.md)
UI generation -> ../ui-design/SKILL.md (standalone fallback: https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/ui-design/SKILL.md) first
Do NOT use for
Web auth flows or Web SDK-specific frontend implementation.
Common mistakes / gotchas
Generating a Web-style login flow for mini programs.
Mixing Web SDK assumptions into wx.cloud projects.
Applying CloudBase constraints before confirming the project actually uses CloudBase.
When to use this skill

Use this skill for WeChat Mini Program development when you need to:

Build or modify mini program pages and components
Organize mini program project structure and configuration
Debug, preview, or publish mini program projects
Work with WeChat Developer Tools workflows
Handle mini program runtime behavior, assets, or page config files
Integrate CloudBase in a mini program project when explicitly needed

Do NOT use for:

Web frontend development (use web-development)
Pure backend service development (use cloudrun-development or cloud-functions as appropriate)
UI design-only tasks without mini program development context (use ui-design)
How to use this skill (for a coding agent)

Start with the general mini program workflow

Treat WeChat Mini Program development as the default scope
Do not assume the project uses CloudBase unless the user or codebase indicates it

Follow mini program project conventions

Keep mini program source under the configured mini program root
Ensure page files include the required configuration file such as index.json
Check project.config.json before suggesting preview or IDE workflows

Route by scenario

If the task involves CloudBase, wx.cloud, cloud functions, CloudBase database/storage, or CloudBase identity handling, read CloudBase integration reference
If the task involves debugging, previewing, publishing, WeChat Developer Tools, or no-DevTools workflows, read debug and preview reference
If the task involves tabBar, icon assets, or label spacing, prefer the text-only custom tabBar default below unless the user explicitly requires icons

Use CloudBase rules only when applicable

CloudBase is an important mini program integration path, but not a universal requirement
Only apply CloudBase-specific auth, database, storage, or cloud function constraints when the project is using CloudBase

Recommend the right preview/debug path

Prefer WeChat Developer Tools for simulator, panel-based debugging, preview, and real-device validation
If WeChat Developer Tools is unavailable, use miniprogram-ci for preview, upload, and npm build workflows where appropriate
WeChat Mini Program Development Rules
General Project Rules

Project Structure

Mini program code should follow the project root configured in project.config.json
Keep page-level files complete, including .json configuration files
Ensure referenced local assets actually exist to avoid compile failures

Configuration Checks

Check project.config.json before opening, previewing, or publishing a project
Confirm appid is available when a real preview, upload, or WeChat Developer Tools workflow is required
Confirm miniprogramRoot and related path settings are correct

Resource Handling

For tabBar, prefer a text-only custom tabBar by default when the user does not explicitly need icons. This avoids icon asset handling, removes reserved icon space, and makes the label area easier to align.
Only generate local icon assets and configure iconPath / selectedIconPath when the user explicitly asks for tab icons or the design requires them.
When generating local asset references such as icons, ensure the files are downloaded into the project.
Keep file paths stable and consistent with mini program config files.
Recommended default for simple tabBar

Use tabBar.custom = true, keep only pagePath and text in app.json, and render text-only items in the custom component so there is no icon slot and no extra blank area above the label.

app.json

{
  "tabBar": {
    "custom": true,
    "list": [
      { "pagePath": "pages/index/index", "text": "首页" },
      { "pagePath": "pages/travel/travel", "text": "行程" },
      { "pagePath": "pages/my/my", "text": "我的" }
    ]
  }
}


Keep the custom tabBar layout text-only, and use flex centering or matching height and line-height to remove the blank area above the label. Switch to downloaded local icons only when the user explicitly wants icon-based tabs.

CloudBase as a Mini Program Sub-Scenario
If the user explicitly uses CloudBase, wx.cloud, Tencent CloudBase, 腾讯云开发, or 云开发, follow the CloudBase integration reference
In CloudBase mini program projects, use wx.cloud APIs and CloudBase environment configuration appropriately
Do not apply CloudBase-specific rules to non-CloudBase mini program projects
Debugging, Preview, and Publishing
If WeChat Developer Tools is available, use it as the primary path for simulator debugging, panel inspection, preview, and device validation
If WeChat Developer Tools is not available, use miniprogram-ci as the fallback path for preview, upload, and npm build-related automation
For detailed workflows, read debug and preview reference
Minimal project skeleton

app.js

App({
  onLaunch() {
    console.log("Mini Program launched");
  },
});


pages/index/index.js

Page({
  data: {
    message: "Hello CloudBase Mini Program",
  },
});


pages/index/index.wxml

<view class="page">
  <text>{{message}}</text>
</view>


pages/index/index.json

{
  "navigationBarTitleText": "Home"
}


project.config.json

{
  "appid": "your-mini-program-appid",
  "projectname": "cloudbase-mini-program",
  "miniprogramRoot": "./",
  "compileType": "miniprogram"
}

References
CloudBase Mini Program Integration — use this when the mini program project explicitly integrates CloudBase
WeChat DevTools Debug and Preview — use this for debugging, preview, publishing, and no-DevTools fallback workflows
Weekly Installs
2.7K
Repository
tencentcloudbase/skills
GitHub Stars
52
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn