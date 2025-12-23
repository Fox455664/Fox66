import os
import sys
import subprocess
import threading
import asyncio
from flask import Flask

# 1. إنشاء سيرفر وهمي لإرضاء نظام Koyeb (Health Check)
app = Flask(__name__)

@app.route('/')
def health_check():
    return "Bot is Running!", 200

def run_flask():
    try:
        # التشغيل على المنفذ 8000 الذي يطلبه Koyeb
        app.run(host='0.0.0.0', port=8000)
    except Exception as e:
        print(f"Flask Error: {e}")

# تشغيل السيرفر في خيط منفصل لكي لا يعطل البوت
threading.Thread(target=run_flask, daemon=True).start()

# 2. كود التأكد من تثبيت جميع المكتبات اللازمة
def install_missing_libraries():
    required_packages = ["telethon", "oldpyro", "pytube", "flask", "pyromod", "pytgcalls"]
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"🔄 جاري تثبيت المكتبة الناقصة: {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# تنفيذ التثبيت قبل بدء البوت
install_missing_libraries()

# 3. استيراد ملفات البوت وتشغيله
from pytgcalls import idle
from pyromod import listen
try:
    from bot import start_zombiebot
except ImportError:
    print("❌ خطأ: لم يتم العثور على دالة start_zombiebot في ملف bot.py")

async def main():
    print("✅ تم تشغيل السيرفر الوهمي والمكتبات بنجاح..")
    print("🚀 جاري تشغيل البوت الآن...")
    try:
        await start_zombiebot()
    except Exception as e:
        print(f"❌ خطأ أثناء تشغيل البوت: {e}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
