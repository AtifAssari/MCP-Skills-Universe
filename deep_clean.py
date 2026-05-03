import os
import shutil

# المسارات
UNCATEGORIZED_DIR = os.path.expanduser("~/skills-scraper/organized_skills/11-other/uncategorized")
BASE_TARGET_DIR = os.path.expanduser("~/skills-scraper/organized_skills")

# قائمة تصنيفات جديدة وشاملة للمتبقي
CATEGORIES = {
    "19-arabic-skills": ["تم", "تحميل", "مهارة", "كود", "تصميم", "موقع", "بيانات"], # كلمات عربية شائعة
    "20-gaming": ["minecraft", "roblox", "steam", "game", "xbox", "playstation", "nintendo", "fortnite", "rpg", "fps"],
    "21-education-science": ["homework", "math", "science", "physics", "history", "learning", "study", "university", "quiz"],
    "22-legal-finance": ["legal", "contract", "invoice", "tax", "banking", "finance", "audit", "compliance", "investment"],
    "23-health-fitness": ["fitness", "health", "workout", "medical", "diet", "doctor", "yoga", "nutrition", "training"],
    "24-scripts-automations": ["script", "automation", "zapier", "make.com", "api", "integration", "workflow", "cron"],
    "25-design-creative": ["logo", "ui", "ux", "illustration", "typography", "branding", "animation", "canva", "figma"]
}

def deep_clean_final():
    if not os.path.exists(UNCATEGORIZED_DIR):
        print(f"❌ المجلد غير موجود.")
        return

    files = [f for f in os.listdir(UNCATEGORIZED_DIR) if f.endswith(".md")]
    print(f"🚀 البدء في تصفية آخر {len(files)} مهارة...")
    
    count = 0
    for file in files:
        file_path = os.path.join(UNCATEGORIZED_DIR, file)
        try:
            # قراءة المحتوى (مع دعم اللغة العربية UTF-8)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().lower()
            
            moved = False
            for cat_name, keywords in CATEGORIES.items():
                if any(key in content for key in keywords):
                    target_path = os.path.join(BASE_TARGET_DIR, cat_name)
                    if not os.path.exists(target_path): os.makedirs(target_path)
                    
                    shutil.move(file_path, os.path.join(target_path, file))
                    count += 1
                    moved = True
                    break
            
            if count > 0 and count % 500 == 0 and moved:
                print(f"✅ تم فرز {count} مهارة إضافية...")
        except:
            continue

    print(f"✨ انتهينا! تم نقل {count} مهارة إلى الفئات الجديدة.")
    print(f"المتبقي الآن في uncategorized هو: {len(os.listdir(UNCATEGORIZED_DIR))} فقط.")

if __name__ == "__main__":
    deep_clean_final()
