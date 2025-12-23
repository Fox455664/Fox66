import os
import threading
import asyncio
from flask import Flask

# 1. تشغيل سيرفر ويب بسيط للرد على Koyeb على منفذ 8000
app = Flask(__name__)

@app.route('/')
def health_check():
    return "OK", 200

def run_web_server():
    app.run(host='0.0.0.0', port=8000)

# تشغيل السيرفر في الخلفية فوراً
threading.Thread(target=run_web_server, daemon=True).start()

# 2. استيراد وتشغيل البوت
from bot import start_zombiebot

async def start_app():
    print("✅ السيرفر الوهمي يعمل على المنفذ 8000")
    print("🚀 جاري تشغيل بوت فوكس...")
    try:
        await start_zombiebot()
    except Exception as e:
        print(f"❌ خطأ في التشغيل: {e}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_app())
