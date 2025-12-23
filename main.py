import os
import threading
import asyncio
import subprocess
import sys
from flask import Flask

# 1. تشغيل سيرفر ويب بسيط للرد على Koyeb على منفذ 8000
app = Flask(__name__)

@app.route('/')
def health_check():
    return "OK", 200

def run_web_server():
    try:
        app.run(host='0.0.0.0', port=8000)
    except Exception:
        pass

# تشغيل السيرفر في الخلفية فوراً
threading.Thread(target=run_web_server, daemon=True).start()

# 2. مثبت المكتبات التلقائي (لضمان وجود pyrolistener وغيرها)
def install_libs():
    libs = ["telethon", "oldpyro", "pytube", "flask", "pyrolistener"]
    for lib in libs:
        try:
            __import__(lib)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

install_libs()

# 3. استيراد وتشغيل البوت
from bot import start_zombiebot

async def start_app():
    print("✅ السيرفر الوهمي يعمل والمكتبات جاهزة..")
    print("🚀 جاري تشغيل بوت فوكس...")
    try:
        await start_zombiebot()
    except Exception as e:
        print(f"❌ خطأ في التشغيل: {e}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_app())
