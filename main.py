import os
import threading
import asyncio
import subprocess
import sys
from flask import Flask

# 1. سيرفر وهمي لإرضاء نظام Koyeb
app = Flask(__name__)
@app.route('/')
def health_check():
    return "OK", 200

def run_web_server():
    try:
        app.run(host='0.0.0.0', port=8000)
    except Exception:
        pass

threading.Thread(target=run_web_server, daemon=True).start()

# 2. مثبت المكتبات التلقائي المطور
def install_libs():
    # المكتبات العادية
    normal_libs = ["telethon", "oldpyro", "pytube", "flask", "pyromod"]
    for lib in normal_libs:
        try:
            __import__(lib)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
    
    # تثبيت pyrolistener من الرابط المباشر
    try:
        __import__("pyrolistener")
    except ImportError:
        print("🔄 جاري تثبيت pyrolistener من GitHub...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "git+https://github.com/TeMeS-T/pyrolistener"])

install_libs()

# 3. تشغيل البوت
from bot import start_zombiebot

async def start_app():
    print("✅ النظام جاهز والخدمات تعمل..")
    try:
        await start_zombiebot()
    except Exception as e:
        print(f"❌ خطأ: {e}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_app())
