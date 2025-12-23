import os
import threading
import asyncio
import subprocess
import sys
from flask import Flask

# 1. سيرفر Flask لإرضاء Koyeb (Health Check)
app = Flask(__name__)
@app.route('/')
def health_check():
    return "Bot is Running!", 200

def run_web_server():
    try:
        app.run(host='0.0.0.0', port=8000)
    except Exception:
        pass

threading.Thread(target=run_web_server, daemon=True).start()

# 2. الحل النهائي: مثبت إجباري للمكتبات الناقصة (unidecode وغيرها)
def force_install_libs():
    # القائمة اللي دايماً بتعمل مشاكل
    libs = ["unidecode", "pytube", "telethon", "oldpyro", "flask", "pyro-listener", "youtube-search"]
    for lib in libs:
        try:
            # بنجرب نستدعي المكتبة (الأسماء اللي فيها شرطة بتتحول لشرطة تحتانية في الـ import)
            module_name = lib.replace("-", "_")
            __import__(module_name)
        except ImportError:
            print(f"🔄 جاري تثبيت المكتبة الناقصة إجبارياً: {lib}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

# بنشغل المثبت الإجباري أول حاجة
force_install_libs()

# 3. استيراد وتشغيل البوت
from bot import start_zombiebot

async def start_app():
    print("✅ السيرفر الوهمي يعمل والمكتبات تم التأكد منها..")
    print("🚀 جاري تشغيل بوت فوكس...")
    try:
        await start_zombiebot()
    except Exception as e:
        print(f"❌ خطأ أثناء التشغيل: {e}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_app())
