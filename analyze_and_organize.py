#!/usr/bin/env python3
"""
Skill Library Analyzer & Organizer
Analyzes 29,226 skills and organizes them into a professional structure
"""

import os
import re
import json
import shutil
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime
import hashlib

# Configuration
SOURCE_DIR = Path.home() / "skills-scraper/skills_library"
OUTPUT_DIR = Path.home() / "skills-scraper/organized_skills"
JSON_INDEX_FILE = Path.home() / "skills-scraper/skills_index.json"
STATS_FILE = Path.home() / "skills-scraper/skills_statistics.json"

# Category definitions with keywords
CATEGORIES = {
    "01-web-frontend": {
        "frameworks": {
            "keywords": ["react", "vue", "angular", "svelte", "solid", "preact", "qwik", "lit"],
            "subcategories": ["react", "vue", "angular", "svelte", "other"]
        },
        "ui-frameworks": {
            "keywords": ["tailwind", "bootstrap", "material-ui", "chakra", "antd", "mantine", "shadcn"],
            "subcategories": ["tailwind", "component-libraries"]
        },
        "mobile": {
            "keywords": ["react-native", "flutter", "swift", "kotlin", "ionic", "capacitor", "cordova"],
            "subcategories": ["react-native", "flutter", "ios", "android", "cross-platform"]
        },
        "static-generators": {
            "keywords": ["next.js", "nuxt", "gatsby", "hugo", "jekyll", "astro", "eleventy"],
            "subcategories": ["nextjs", "nuxt", "astro", "other"]
        },
        "performance": {
            "keywords": ["web-vitals", "lazy-loading", "caching", "performance", "optimization"],
            "subcategories": []
        },
        "webassembly": {
            "keywords": ["wasm", "webassembly", "rust-wasm", "assemblyscript"],
            "subcategories": []
        }
    },
    "02-backend": {
        "nodejs": {
            "keywords": ["express", "nestjs", "fastify", "hapi", "koa", "sails", "feathers"],
            "subcategories": ["express", "nestjs", "fastify", "other"]
        },
        "python": {
            "keywords": ["fastapi", "django", "flask", "tornado", "falcon", "bottle"],
            "subcategories": ["fastapi", "django", "flask", "other"]
        },
        "java": {
            "keywords": ["spring", "spring-boot", "micronaut", "quarkus", "jakarta"],
            "subcategories": []
        },
        "go": {
            "keywords": ["gin", "echo", "fiber", "chi", "go-backend"],
            "subcategories": []
        },
        "rust": {
            "keywords": ["axum", "actix", "rocket", "warp", "tonic"],
            "subcategories": []
        },
        "graphql": {
            "keywords": ["graphql", "apollo", "strawberry", "pothos", "hasura"],
            "subcategories": []
        },
        "serverless": {
            "keywords": ["lambda", "vercel", "cloudflare-workers", "netlify-functions", "serverless"],
            "subcategories": []
        }
    },
    "03-databases": {
        "sql": {
            "keywords": ["postgresql", "postgres", "mysql", "sqlite", "cockroachdb", "tidb", "mariadb"],
            "subcategories": ["postgresql", "mysql", "sqlite", "other"]
        },
        "nosql": {
            "keywords": ["mongodb", "redis", "dynamodb", "couchbase", "cassandra", "scylla"],
            "subcategories": []
        },
        "cloud-databases": {
            "keywords": ["supabase", "firebase", "planetscale", "neon", "fauna", "cosmos-db"],
            "subcategories": []
        },
        "orms": {
            "keywords": ["prisma", "drizzle", "typeorm", "sqlalchemy", "peewee", "tortoise"],
            "subcategories": ["prisma", "drizzle", "typeorm", "other"]
        },
        "caching": {
            "keywords": ["redis", "memcached", "cache", "caching"],
            "subcategories": []
        },
        "data-warehousing": {
            "keywords": ["snowflake", "bigquery", "clickhouse", "redshift", "databricks"],
            "subcategories": []
        }
    },
    "04-devops": {
        "containers": {
            "keywords": ["docker", "container", "docker-compose", "containerd", "podman"],
            "subcategories": []
        },
        "kubernetes": {
            "keywords": ["kubernetes", "k8s", "helm", "argo", "rancher", "k3s", "minikube"],
            "subcategories": []
        },
        "cicd": {
            "keywords": ["github-actions", "gitlab-ci", "jenkins", "circleci", "travis", "drone", "tekton"],
            "subcategories": []
        },
        "cloud": {
            "keywords": ["aws", "azure", "gcp", "google-cloud", "amazon-web-services"],
            "subcategories": ["aws", "azure", "gcp"]
        },
        "iac": {
            "keywords": ["terraform", "pulumi", "ansible", "cloudformation", "cdk"],
            "subcategories": []
        }
    },
    "05-ai-ml": {
        "llm-integration": {
            "keywords": ["openai", "anthropic", "claude", "gemini", "ollama", "llama", "llm", "gpt"],
            "subcategories": []
        },
        "ai-agents": {
            "keywords": ["agent", "adk", "langchain", "llamaindex", "crewai", "autogen", "swarm"],
            "subcategories": []
        },
        "ml-frameworks": {
            "keywords": ["tensorflow", "pytorch", "scikit-learn", "jax", "xgboost", "lightgbm"],
            "subcategories": []
        },
        "vector-databases": {
            "keywords": ["pinecone", "weaviate", "chroma", "qdrant", "milvus", "pgvector"],
            "subcategories": []
        },
        "computer-vision": {
            "keywords": ["opencv", "yolo", "detectron", "mediapipe", "vision", "image-processing"],
            "subcategories": []
        },
        "nlp": {
            "keywords": ["huggingface", "spacy", "nltk", "transformers", "bert", "tokenization"],
            "subcategories": []
        },
        "mlops": {
            "keywords": ["mlflow", "wandb", "bentoml", "kubeflow", "sagemaker"],
            "subcategories": []
        }
    },
    "06-security": {
        "app-security": {
            "keywords": ["owasp", "security", "xss", "csrf", "injection", "secure"],
            "subcategories": []
        },
        "auth": {
            "keywords": ["oauth", "jwt", "saml", "sso", "authentication", "authorization", "mfa"],
            "subcategories": []
        },
        "vulnerability": {
            "keywords": ["snyk", "dependabot", "sonarqube", "codeql", "vulnerability"],
            "subcategories": []
        },
        "penetration-testing": {
            "keywords": ["burp", "metasploit", "sqlmap", "nmap", "penetration"],
            "subcategories": []
        },
        "crypto": {
            "keywords": ["encryption", "cryptography", "hashing", "pki", "tls", "ssl"],
            "subcategories": []
        },
        "compliance": {
            "keywords": ["gdpr", "hipaa", "soc2", "iso27001", "compliance"],
            "subcategories": []
        }
    },
    "07-testing": {
        "unit-testing": {
            "keywords": ["jest", "vitest", "pytest", "mocha", "junit", "unit-test"],
            "subcategories": []
        },
        "e2e-testing": {
            "keywords": ["playwright", "cypress", "selenium", "puppeteer", "e2e", "end-to-end"],
            "subcategories": []
        },
        "integration-testing": {
            "keywords": ["postman", "supertest", "rest-assured", "integration-test"],
            "subcategories": []
        },
        "performance-testing": {
            "keywords": ["k6", "artillery", "locust", "jmeter", "load-test"],
            "subcategories": []
        },
        "test-strategies": {
            "keywords": ["tdd", "bdd", "mutation-testing", "fuzzing", "test-strategy"],
            "subcategories": []
        }
    },
    "08-tools-automation": {
        "cli-tools": {
            "keywords": ["commander", "click", "cobra", "oclif", "cli"],
            "subcategories": []
        },
        "build-tools": {
            "keywords": ["webpack", "vite", "rollup", "parcel", "esbuild", "turbopack"],
            "subcategories": []
        },
        "package-managers": {
            "keywords": ["npm", "pnpm", "yarn", "poetry", "cargo", "maven", "gradle"],
            "subcategories": []
        },
        "monorepo": {
            "keywords": ["nx", "turborepo", "lerna", "rush", "bazel", "monorepo"],
            "subcategories": []
        },
        "code-quality": {
            "keywords": ["eslint", "prettier", "black", "ruff", "clippy", "linting"],
            "subcategories": []
        },
        "git": {
            "keywords": ["git", "github", "gitlab", "bitbucket", "gitflow", "conventional-commits"],
            "subcategories": []
        },
        "task-runners": {
            "keywords": ["make", "just", "taskfile", "npm-scripts", "gulp"],
            "subcategories": []
        }
    },
    "09-embedded-iot": {
        "embedded": {
            "keywords": ["arduino", "esp32", "raspberry-pi", "stm32", "embedded", "microcontroller"],
            "subcategories": []
        },
        "robotics": {
            "keywords": ["ros", "robotics", "moveit", "gazebo", "urdf"],
            "subcategories": []
        },
        "iot": {
            "keywords": ["iot", "mqtt", "industrial", "scada", "modbus", "opc-ua"],
            "subcategories": []
        },
        "edge-ai": {
            "keywords": ["edge-ai", "tflite", "onnx-runtime", "edge-tpu", "coral"],
            "subcategories": []
        }
    },
    "10-specialized": {
        "game-dev": {
            "keywords": ["unity", "unreal", "godot", "three.js", "babylon", "gamedev"],
            "subcategories": []
        },
        "desktop": {
            "keywords": ["electron", "tauri", "wpf", "gtk", "qt", "desktop"],
            "subcategories": []
        },
        "blockchain": {
            "keywords": ["solidity", "ethereum", "hardhat", "web3", "ethers", "smart-contract"],
            "subcategories": []
        },
        "data-engineering": {
            "keywords": ["spark", "kafka", "airflow", "dbt", "etl", "data-pipeline"],
            "subcategories": []
        },
        "scientific": {
            "keywords": ["numpy", "scipy", "pandas", "matplotlib", "jupyter", "scientific"],
            "subcategories": []
        },
        "audio-video": {
            "keywords": ["ffmpeg", "webrtc", "web-audio", "streaming", "video-processing"],
            "subcategories": []
        },
        "cad-3d": {
            "keywords": ["blender", "openscad", "freecad", "cad", "3d-modeling"],
            "subcategories": []
        }
    },
    "11-other": {
        "uncategorized": {
            "keywords": [],
            "subcategories": []
        }
    }
}

def extract_skill_info(filepath):
    """Extract information from a skill markdown file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract title from frontmatter
        title_match = re.search(r'title:\s*(.+)', content)
        title = title_match.group(1).strip() if title_match else Path(filepath).stem
        
        # Extract URL
        url_match = re.search(r'url:\s*(.+)', content)
        url = url_match.group(1).strip() if url_match else ""
        
        # Extract summary (first paragraph after frontmatter)
        summary_match = re.search(r'Summary\s*\n\s*\n([^\n]+)', content)
        summary = summary_match.group(1).strip() if summary_match else ""
        
        # Get file size and content hash
        file_size = os.path.getsize(filepath)
        content_hash = hashlib.md5(content.encode()).hexdigest()[:8]
        
        # Combine all text for classification
        search_text = f"{title} {summary} {content[:2000]}".lower()
        
        return {
            "filename": filepath.name,
            "filepath": str(filepath),
            "title": title,
            "url": url,
            "summary": summary[:300],
            "size": file_size,
            "hash": content_hash
        }
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

def classify_skill(skill_info):
    """Classify a skill into category and subcategory"""
    text = f"{skill_info['title']} {skill_info['summary']}".lower()
    
    best_category = "11-other"
    best_subcategory = "uncategorized"
    best_score = 0
    
    for category, subcats in CATEGORIES.items():
        for subcategory, config in subcats.items():
            keywords = config.get("keywords", [])
            score = sum(1 for kw in keywords if kw in text)
            
            # Bonus for exact title matches
            if subcategory.replace("-", "") in text:
                score += 3
            
            if score > best_score:
                best_score = score
                best_category = category
                best_subcategory = subcategory
    
    return best_category, best_subcategory

def main():
    print("=" * 70)
    print("SKILL LIBRARY ANALYZER & ORGANIZER")
    print("=" * 70)
    print(f"Source: {SOURCE_DIR}")
    print(f"Output: {OUTPUT_DIR}")
    print("=" * 70)
    
    # Step 1: Scan all files
    print("\n📂 Scanning skill files...")
    all_files = []
    for batch_dir in SOURCE_DIR.glob("batch_*"):
        if batch_dir.is_dir():
            for md_file in batch_dir.glob("*.md"):
                all_files.append(md_file)
    
    print(f"   Found {len(all_files):,} skill files")
    
    # Step 2: Extract info from each file
    print("\n📊 Extracting skill information...")
    skills = []
    for i, filepath in enumerate(all_files, 1):
        if i % 1000 == 0:
            print(f"   Processed {i:,}/{len(all_files):,} files...")
        
        info = extract_skill_info(filepath)
        if info:
            info["category"], info["subcategory"] = classify_skill(info)
            skills.append(info)
    
    print(f"   Successfully processed {len(skills):,} skills")
    
    # Step 3: Generate statistics
    print("\n📈 Generating statistics...")
    stats = {
        "total_skills": len(skills),
        "total_size_mb": sum(s["size"] for s in skills) / (1024 * 1024),
        "by_category": defaultdict(int),
        "by_subcategory": defaultdict(int),
        "top_keywords": Counter(),
        "batch_distribution": defaultdict(int)
    }
    
    for skill in skills:
        stats["by_category"][skill["category"]] += 1
        stats["by_subcategory"][f"{skill['category']}/{skill['subcategory']}"] += 1
        
        # Extract batch info
        batch = Path(skill["filepath"]).parent.name
        stats["batch_distribution"][batch] += 1
        
        # Count keywords
        text = f"{skill['title']} {skill['summary']}".lower()
        words = re.findall(r'\b[a-z]+\b', text)
        for word in words:
            if len(word) > 3:
                stats["top_keywords"][word] += 1
    
    # Step 4: Save JSON index
    print(f"\n💾 Saving JSON index to {JSON_INDEX_FILE}...")
    index_data = {
        "metadata": {
            "generated_at": datetime.now().isoformat(),
            "total_skills": len(skills),
            "total_size_mb": round(stats["total_size_mb"], 2)
        },
        "skills": skills,
        "categories": list(CATEGORIES.keys()),
        "statistics": {
            "by_category": dict(stats["by_category"]),
            "by_subcategory": dict(stats["by_subcategory"]),
            "top_keywords": dict(stats["top_keywords"].most_common(100)),
            "batch_distribution": dict(stats["batch_distribution"])
        }
    }
    
    with open(JSON_INDEX_FILE, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)
    
    print(f"   ✓ Saved {JSON_INDEX_FILE.name}")
    
    # Step 5: Save statistics
    print(f"\n📊 Saving statistics to {STATS_FILE}...")
    with open(STATS_FILE, 'w', encoding='utf-8') as f:
        json.dump(index_data["statistics"], f, indent=2, ensure_ascii=False)
    
    print(f"   ✓ Saved {STATS_FILE.name}")
    
    # Step 6: Print summary
    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE!")
    print("=" * 70)
    print(f"\n📊 Total Skills: {len(skills):,}")
    print(f"📦 Total Size: {stats['total_size_mb']:.2f} MB")
    print(f"\n📂 Skills by Category:")
    
    for cat, count in sorted(stats["by_category"].items(), key=lambda x: -x[1]):
        cat_name = cat.replace("-", " ").title()
        print(f"   {cat_name:30s}: {count:5,} skills")
    
    print(f"\n🔤 Top 20 Keywords:")
    for word, count in stats["top_keywords"].most_common(20):
        print(f"   {word:20s}: {count:5,}")
    
    # Step 7: Create organized directory structure
    print("\n📁 Creating organized directory structure...")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Create category directories
    for category in CATEGORIES.keys():
        cat_path = OUTPUT_DIR / category
        cat_path.mkdir(parents=True, exist_ok=True)
        
        # Create subcategory directories
        for subcat in CATEGORIES[category].keys():
            subcat_path = cat_path / subcat
            subcat_path.mkdir(parents=True, exist_ok=True)
    
    # Step 8: Copy files to organized structure (create symlinks or copies)
    print("\n🔄 Organizing files into new structure...")
    organized_count = 0
    for skill in skills:
        src = Path(skill["filepath"])
        dst_dir = OUTPUT_DIR / skill["category"] / skill["subcategory"]
        dst = dst_dir / skill["filename"]
        
        try:
            shutil.copy2(src, dst)
            organized_count += 1
            if organized_count % 1000 == 0:
                print(f"   Organized {organized_count:,} files...")
        except Exception as e:
            print(f"   Warning: Could not copy {src}: {e}")
    
    print(f"   ✓ Organized {organized_count:,} files")
    
    print("\n" + "=" * 70)
    print("ALL TASKS COMPLETED SUCCESSFULLY!")
    print("=" * 70)
    print(f"\n📄 Files created:")
    print(f"   • {JSON_INDEX_FILE}")
    print(f"   • {STATS_FILE}")
    print(f"   • {OUTPUT_DIR} (organized structure)")

if __name__ == "__main__":
    main()
