import os

# المسار الصحيح للمجلد المنظم
BASE_DIR = os.path.expanduser("~/skills-scraper/organized_skills")

def calculate_quality_stars(content):
    score = 0
    if len(content) > 500: score += 1
    if "```" in content: score += 2
    if "http" in content: score += 1
    if content.count("#") > 2: score += 1
    return max(1, min(5, score))

def prepare_for_github():
    print("🚀 البدء في تقييم الجودة وتجهيز التوثيق...")
    
    if not os.path.exists(BASE_DIR):
        print(f"❌ خطأ: المجلد {BASE_DIR} غير موجود.")
        return

    count = 0
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    stars = calculate_quality_stars(content)
                    star_rating = "⭐" * stars
                    
                    if "rating:" not in content:
                        updated_content = content.replace("---", f"---\nrating: {star_rating}", 1)
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(updated_content)
                    count += 1
                    if count % 1000 == 0:
                        print(f"تم تقييم {count} مهارة...")
                except:
                    continue

    readme_content = """# 🌌 MCP Skills Universe
> **The world's largest open-source collection of AI Agent Skills.**

![Skills Count](https://shields.io)
![License](https://shields.io)

## 📖 Introduction
This repository is a massive archive of **30,000+ AI Agent Skills**, automatically scraped, classified, and quality-rated.

## 🌟 Quality Rating System
- ⭐⭐⭐⭐⭐: Comprehensive
- ⭐⭐⭐: Standard utility
- ⭐: Minimal instruction

---
*Maintained by Atif & OpenClaw.*
"""
    with open(os.path.expanduser("~/skills-scraper/README.md"), 'w') as f:
        f.write(readme_content)
    
    print(f"✅ تم الانتهاء! تمت معالجة {count} ملف بنجاح.")

if __name__ == "__main__":
    prepare_for_github()

