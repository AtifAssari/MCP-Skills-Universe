---
rating: ⭐⭐⭐
title: qoder-ppt-v2
url: https://skills.sh/lexburner/skill-collection/qoder-ppt-v2
---

# qoder-ppt-v2

skills/lexburner/skill-collection/qoder-ppt-v2
qoder-ppt-v2
Installation
$ npx skills add https://github.com/lexburner/skill-collection --skill qoder-ppt-v2
SKILL.md
Qoder PPT 生成器 v2

将文稿转化为 Qoder 品牌风格的 HTML 演示文稿。

模板文件：template.html（同目录下）

核心布局
封面页：完全居中
.slide.cover {
  justify-content: center;
  align-items: center;
  padding: 60px 120px;
}

内容页：标题顶部 + 内容居中
.slide { padding: 120px 120px 80px 120px; }
.content-center { flex: 1; }
.content-center > *:not(h2) { margin: auto 0; }

页面结构
封面页
<section class="slide cover active">
  <div class="brand"><span class="logo">QODER</span></div>
  <div class="content">
    <h1><span class="highlight">关键词</span> 主标题</h1>
    <p class="subtitle">副标题</p>
  </div>
  <span class="page-number">01</span>
</section>

内容页（通用结构）
<section class="slide {type}">
  <div class="brand"><span class="logo">QODER</span></div>
  <div class="content-center">
    <h2 class="section-title">标题</h2>
    <!-- 内容区域 -->
  </div>
  <span class="page-number">02</span>
</section>

内容区域类型
要点列表 (points)
<ul class="point-list">
  <li><span class="bullet"></span><span class="text">要点内容</span></li>
</ul>

卡片网格 (cards)
<div class="card-grid">
  <div class="card">
    <h3 class="card-title"><span class="highlight">标题</span></h3>
    <p class="card-content">内容</p>
  </div>
</div>

对比布局 (compare)
<div class="compare-grid">
  <div class="compare-item">
    <h3><span class="highlight">左侧</span>标题</h3>
    <ul><li>对比点</li></ul>
  </div>
  <div class="compare-divider">VS</div>
  <div class="compare-item">
    <h3><span class="highlight">右侧</span>标题</h3>
    <ul><li>对比点</li></ul>
  </div>
</div>

流程图 (flow)
<div class="flow-container">
  <div class="flow-step">
    <div class="step-number">1</div>
    <div class="step-content">步骤说明</div>
  </div>
  <div class="flow-arrow">→</div>
  <!-- 更多步骤 -->
</div>

数据展示 (data)
<div class="data-grid">
  <div class="data-item">
    <span class="data-value">99%</span>
    <span class="data-label">指标说明</span>
  </div>
</div>

表格 (table)
<table class="data-table">
  <thead><tr><th>维度</th><th>A</th><th>B</th></tr></thead>
  <tbody><tr><td>特征</td><td>值A</td><td><span class="highlight">值B</span></td></tr></tbody>
</table>

总结 (summary)
<div class="summary-content">
  <p class="key-point"><span class="highlight">核心要点</span> 补充说明</p>
</div>

设计规范
颜色
用途	值
背景	#000000
高亮	#2ADB5C
标题	#FFFFFF
正文	#96989A
次级	#68696B
边框	#343434
字体
中文：Alibaba PuHuiTi 2.0 / PingFang SC
英文/数字：Montserrat
字号
元素	大小
大标题 h1	66px
章节标题 h2	36px
卡片标题 h3	28-30px
正文	24px
演示功能
操作	效果
→ / Space	下一页
← / Backspace	上一页
Home / End	首页/末页
点击右 2/3	下一页
点击左 1/3	上一页
检查清单
 第一个 slide 有 active 类
 所有 slide 在 slides-container 内
 h2 标题在 content-center 内部
 封面页使用 .slide.cover
 关键词使用 <span class="highlight">
 页码递增正确
禁止事项
禁止 h2 放在 content-center 外部
禁止遗漏第一个 slide 的 active 类
禁止使用非规定颜色
禁止单页内容过多
Weekly Installs
18
Repository
lexburner/skill…llection
GitHub Stars
47
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass