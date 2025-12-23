import os
import threading
import asyncio
import subprocess
import sys
import importlib
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

# تشغيل السيرفر فوراً
threading.Thread(target=run_web_server, daemon=True).start()

# 2. مثبت المكتبات الإجباري مع تحديث الـ Cache
def force_install_libs():
    # القائمة الكاملة والنهائية
    libs = ["unidecode", "pytube", "telethon", "oldpyro", "flask", "pyro-listener", "youtube-search"]
    
    for lib in libs:
        try:
            # محاولة الاستدعاء للتأكد
            module_name = lib.replace("-", "_")
            importlib.import_module(module_name)
        except ImportError:
            print(f"🔄 جاري تثبيت {lib} فوراً...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
            # الخطوة السحرية: تحديث بايثون عشان يشوف المكتبة اللي لسه نازلة
            importlib.invalidate_caches()
            print(f"✅ تم تثبيت وتفعيل {lib}")

# تشغيل التثبيت الإجباري قبل استيراد أي حاجة من البوت
force_install_libs()

# 3. الآن نستورد البوت بأمان
from bot import start_zombiebot

async def start_app():
    print("✅ السيرفر يعمل، المكتبات مفعلة، والآن وقت الانطلاق!")
    print("🚀 جاري تشغيل بوت فوكس...")
    try:
        await start_zombiebot()
    except Exception as e:
        print(f"❌ خطأ أثناء التشغيل: {e}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_app())
