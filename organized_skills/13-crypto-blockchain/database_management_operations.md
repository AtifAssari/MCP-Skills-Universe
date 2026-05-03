---
rating: ⭐⭐⭐
title: database-management-operations
url: https://skills.sh/findinfinitelabs/chuuk/database-management-operations
---

# database-management-operations

skills/findinfinitelabs/chuuk/database-management-operations
database-management-operations
Installation
$ npx skills add https://github.com/findinfinitelabs/chuuk --skill database-management-operations
SKILL.md
Database Management Operations
Overview

All persistence uses Azure Cosmos DB with MongoDB API via pymongo==4.3.3 (pinned for Cosmos DB wire-protocol v6 compatibility). There is no SQLAlchemy, SQLite, or relational layer.

Key Files
File	Purpose
src/database/db_factory.py	Connection helpers (get_database_client(), get_database_config())
src/database/dictionary_db.py	DictionaryDB class — all CRUD operations
app.py	Instantiates dict_db = DictionaryDB() at module level
DictionaryDB
Constructor
class DictionaryDB:
    def __init__(self, connection_string: str = None):
        from .db_factory import get_database_client, get_database_config
        self.config = get_database_config()
        self.db_type = self.config['type']          # 'cosmos'
        # Cosmos path
        self.client = get_database_client()
        db = self.client[self.config['database_name']]
        self.dictionary_collection  = db[self.config['container_name']]
        self.pages_collection       = db[self.config['pages_container']]
        self.words_collection       = db[self.config['words_container']]
        self.phrases_collection     = db[self.config['phrases_container']]
        self.paragraphs_collection  = db[self.config['paragraphs_container']]

Collection overview
Attribute	Container	Primary use
dictionary_collection	Main dictionary	Chuukese entries with definitions
words_collection	Words index	Individual word search records
phrases_collection	Phrases	Multi-word expressions
pages_collection	Pages	OCR page scan records
paragraphs_collection	Paragraphs	Paragraph-level text blocks
db_factory.py

Module-level functions — not a class:

from src.database.db_factory import get_database_client, get_database_config

client = get_database_client()   # returns MongoClient
config = get_database_config()   # returns dict with container names, db name


Supports two auth methods:

COSMOS_DB_CONNECTION_STRING env var (primary)
Azure Managed Identity via azure-identity (production fallback)
Common Operations
# Search with accent-folding regex (always re.escape user input)
pattern = re.escape(user_input)
results = dict_db.dictionary_collection.find(
    {'chuukese_word': {'$regex': pattern, '$options': 'i'}},
    limit=50
)

# Insert entry
dict_db.dictionary_collection.insert_one({
    'chuukese_word': word,
    'english_translation': definition,
    'grammar_type': pos,
    'created_at': datetime.now(timezone.utc)
})

# Bulk insert
dict_db.bulk_insert_entries(entries_list)

Environment Variables
COSMOS_DB_CONNECTION_STRING=mongodb://account:key@account.mongo.cosmos.azure.com:10255/...
COSMOS_DB_NAME=chuuk-dictionary
COSMOS_CONTAINER_NAME=dictionary

Cosmos DB Notes
retryWrites=False is required for Cosmos DB
Use pymongo 4.3.3 exactly — newer versions break Cosmos DB wire protocol
RU budget: cache list queries; avoid full collection scans
Source Files
src/database/dictionary_db.py — full implementation (~2100 lines)
src/database/db_factory.py — connection factory
Weekly Installs
10
Repository
findinfinitelabs/chuuk
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass