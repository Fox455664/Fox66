import os
import threading
import asyncio
from flask import Flask

# 1. سيرفر Flask عشان Koyeb ميقفلش البوت (Health Check)
app = Flask(__name__)

@app.route('/')
def health_check():
    return "Bot is Running!", 200

def run_flask():
    # هيشتغل على منفذ 8000 اللي Koyeb عاوزه
    app.run(host='0.0.0.0', port=8000)

threading.Thread(target=run_flask, daemon=True).start()

# 2. تشغيل البوت الأساسي
from bot import start_zombiebot

async def start_app():
    print("✅ السيرفر الوهمي يعمل بنجاح..")
    print("🚀 جاري تشغيل بوت فوكس...")
    try:
        await start_zombiebot()
    except Exception as e:
        print(f"❌ خطأ أثناء التشغيل: {e}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_app())
