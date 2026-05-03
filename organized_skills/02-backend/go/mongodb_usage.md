---
rating: ⭐⭐
title: mongodb_usage
url: https://skills.sh/vuralserhat86/antigravity-agentic-skills/mongodb_usage
---

# mongodb_usage

skills/vuralserhat86/antigravity-agentic-skills/mongodb_usage
mongodb_usage
Installation
$ npx skills add https://github.com/vuralserhat86/antigravity-agentic-skills --skill mongodb_usage
SKILL.md
MongoDB MCP Usage

Use the MongoDB MCP server to integrate database queries into workflows.

Read-Only Access

MongoDB MCP is configured in read-only mode. Only queries and data retrieval are supported. No write, update, or delete operations.

Database Queries

Use mcp__mongodb__* tools for:

Listing databases
Viewing collection schemas
Querying collection data
Analyzing indexes
Integration Pattern
List available databases with mcp__mongodb__list_databases
Explore collections with mcp__mongodb__list_collections
Get schema information with mcp__mongodb__get_collection_schema
Query data as needed for analysis
Format results for user consumption
Environment Variables

MongoDB MCP requires:

MONGODB_URI - Connection string (mongodb://...)

Configure in shell before using the plugin.

Cost Considerations
Minimize database calls when possible
Use schema queries before running analysis queries
Cache results locally if multiple calls needed MongoDB Usage v1.1 - Enhanced
🔄 Workflow

Kaynak: MongoDB Performance Best Practices

Aşama 1: Discovery & Inspection
 Connection: mcp__mongodb__list_databases ile erişimi doğrula.
 Schema Analysis: mcp__mongodb__get_collection_schema ile veri tiplerini ve yapıyı anla.
 Index Check: Mevcut indeksleri listele (list_indexes veya benzeri sorgu ile).
Aşama 2: Query Construction
 Filter: Sorguları indeksli alanlar (Prefix) üzerinden filtrele.
 Projection: Sadece gerekli alanları ({ field: 1 }) seç (Network ve RAM tasarrufu).
 Aggregation: Karmaşık analizler için $match, $group, $project pipeline'ını kur.
Aşama 3: Performance Check (Explain Plan)
 Explain: Sorgunun COLLSCAN (Tam tarama) mı IXSCAN (Index tarama) mı yaptığını kontrol et.
 Optimization: Yavaş sorgular için bileşik indeks (Compound Index) öner.
Kontrol Noktaları
Aşama	Doğrulama
1	Sorgu 100ms'in altında cevap veriyor mu?
2	"In-memory sort" limiti aşılıyor mu (disk kullanımı var mı)?
3	Regex sorguları indeksin başlangıcını (anchor ^...) kullanıyor mu?
Weekly Installs
9
Repository
vuralserhat86/a…c-skills
GitHub Stars
42
First Seen
Jan 24, 2026