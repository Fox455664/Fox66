import os
import sys
import subprocess
import threading
import asyncio
from flask import Flask

# --- سيرفر Flask لإبقاء البوت حياً على Koyeb مجاناً ---
app = Flask(name)
@app.route('/')
def health_check():
    return "Bot is Running!", 200

def run_flask():
    app.run(host='0.0.0.0', port=8000)

threading.Thread(target=run_flask, daemon=True).start()

# --- تثبيت المكتبات الناقصة تلقائياً ---
def install_missing_libraries():
    pkgs = ["telethon", "oldpyro", "pytube", "flask", "pyromod", "pytgcalls"]
    for p in pkgs:
        try:
            import(p)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", p])

install_missing_libraries()

# --- إعدادات البوت (التي أرسلتها أنت) ---
# ملاحظة: يفضل وضع هذه البيانات في ملف config.py إذا كان السورس يدعم ذلك
caes = ["f_o_x_351","Foxcc45","Fox567789"]
casery = "f_o_x_351"
caserid = 7669264153
OWNER = "فوكس"
muusiic = "fox MuSiC" 
suorce = "SoUrCe fox" 
source = "https://t.me/fox68899" 
ch = "fox68899" 
group = "https://t.me/fox68899" 
photosource = "https://t.me/fox68899/22604"
# التوكنات (التي أرسلتها)
BOT_TOKEN = "8550161677:AAFAMOORMi_TVRg5uvbObV9GAqext4HdW10"
SESSION = "BAF5OpQAGRbP2KrVZiJGqhgbLnYFXLmSriIrIjPXaOfm7MrMZ9rOX1yVH8T_eMCrmJPOYfGB3jtKQ8X9weHJJ-D1Enrwncbn3oHA0FbSbR1SXATrTtH-F_l7ne-vQwAwyPCvoLVJt3PZhQwrPNGFngiIK0IfxVQ3SVmDHLFNQVsBpZDEf9v-fwwJ_VMPqH0uVZeAsxxBVba9ekoZmbW0tl8bTw4F7W8_4c759Sr5kG1iNFuj414KB2JHhc5sCqMwOhUfYbkWiLU3ECWPglPOD0JBdZM5utjfRioozZLIdE-Icl3teUk65KUwQyl8HA94f9HGYVOuj4eIwRhwkxCFxAQhCuZLdwAAAAHx6C_MAA"

# --- تشغيل السورس ---
from bot import start_zombiebot

async def main():
    print("✅ السيرفر الوهمي يعمل على منفذ 8000")
    print("🚀 جاري تشغيل بوت فوكس...")
    await start_zombiebot()

if name == "main":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
